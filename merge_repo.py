#!/usr/bin/python
# Classification (U)

"""Program:  merge_repo.py

    Description:  Merge a non-local Git repository into an existing local and
        remote Git repository.  The merge process will clean up the non-local
        Git repository of dirty and untracked files by either reverting or
        commiting them.  Then the program will pull the existing remote Git
        branch into the non-local Git repository.  This will then alow the
        program to merge the non-local Git repository with the existing
        Git repository.  Once the branches have been merged the updated branch
        will be pushed back to the remote Git repository in the same branch
        that was pulled.

        NOTE 1:  The non-local Git repository being merged will have priority
            during the merge.  This means that the non-local Git repository
            will have precedence over the changes made to the remote Git
            repository.
        NOTE 2:  The non-local Git repository can come in as a detached
            HEAD repository and with no named branches in the repository or
            come the non-local Git repository can come in with a single branch
            in which case the program will detach the HEAD to the latest commit
            ID and remove the existing branch.
        NOTE 3:  The -a option allows for using multiple deploy keys for a
            single user account into Git (e.g. sometimes required for Github).
            There must be an entry in the account's ~/.ssh/config file with an
            alias name that matches the respository name being processed.  See
            the Notes section on format of entry in ~/.ssh/config file.

    Usage:
        merge_repo.py -c config -d config_dir
            -p project_directory [-r repo_name]
            {-M [-a] [-n] [-u]}
            {-v | -h}

    Arguments:
        -c file_name => Name of merge_repo configuration file.
        -d directory_path => Directory path to the configuration file.

        -p directory_path => Absolute path name to project directory.
            -r repo_name => Repository name being merged with.

        -M => Run the merge function.
            -a => Use the repository name as an alias in the Git url.  Used in
                a Github repository setting.
            -n => Override email setting and do not send email notifications.
            -u => Allows unrelated Git repo histories to be merged.

        -v => Display version of this program.
        -h => Help and usage message.

        WARNING:  Only use the -u option if the below error message appears:
            "fatal: refusing to merge unrelated histories".
            This typically means these projects started independently of each
            other and this needs to be clarified you want to merge these
            repositories.

        NOTE 1:  -v or -h overrides the other options.
        NOTE 2:  If -r is not passed, the program will use the basename from
            the -p option directory path to populate the -r argument.
        NOTE 3:  If -a is used, this assumes there is an alias name in the
            account's ~/.ssh/config that matches the repository name.

    Notes:
        Config file:
            # Basic Git Project set up
            git_project="ProjectName"
            git_server="GitServerFQDN"

            # Directory set up
            work_dir="/PATH_DIRECTORY/merge-repo/work_dir"
            err_dir="/PATH_DIRECTORY/merge-repo/error_dir"
            archive_dir="/PATH_DIRECTORY/merge-repo/archive_dir"
            quar_dir="/PATH_DIRECTORY/merge-repo/quarantine"
            log_file="/PATH_DIRECTORY/merge-repo/logs/merge-repo.log"

            # Email set up
            to_line="EMAIL_ADDRESS@EMAIL_DOMAIN"

            # Do not modify unless you know what you are doing
            name="gituser"
            email="gituser@domain.mail"
            branch="develop"
            mod_branch="mod_release"
            dirty="revert"
            untracked="remove"
            prefix="git@"

        Note:  Ensure directories exist for work_dir, err_dir, archive_dir,
            quar_dir, and log_file configuration settings.

        SSH Deployment Keys:
            This is only if the -a option is used against a Github repository.
            If merging into a Github repository then each project may require
                its own unique deployment key.  Running the following
                procedures to create and setup deployment key for a project.
            Change the repsective variables below to the names required:
                GitRepoName:  The Git repository  project name.
                ServerNameFQDN:  The Git server's fully qualified domain name.
                    Should be the same as the git_server variable in the config
                    file above.
                UserName:  The account name connecting to Git.
                Path:  The directory path to id_dsa.GitRepoName file.
                GitProject:  The name of overall Git Project.  Should be the
                    same as the git_project variable in the config file above.

            1.  Create deployment key.
                $ ssh-keygen -t dsa
                    Name:  id_dsa.GitRepoName
                    Passphrase:  Null
            2.  Add project entry to ssh config file.
                $ vim ~/.ssh/config file
                    Host GitRepoName ServerNameFQDN
                    Hostname ServerNameFQDN
                    User UserName
                    IdentityFile Path/id_dsa.GitRepoName
            3.  In Github setup a deploy key in the repository being merged.
                a.  Go to project in GitHub.
                b.  Click "Settings" -> "Deploy Keys" -> "Add Deploy Key"
                        Title:  SomeNameHere
                        Key:  (Paste public key here)
                c.  Click Button:  "Allow Write Access"
                d.  Clock "Add Key"
            4.  To use the deploy key to clone a git repository:
                $ git clone git@GitRepoName:GitProject/GitRepoName.git

    Examples:
        merge_repo.py -c merge -d config -r python-lib -p /local/python-lib -M

"""

# Libraries and Global Variables
from __future__ import print_function
from __future__ import absolute_import

# Standard
import sys
import os
import datetime
import socket
import getpass
import git

# Local
try:
    from .lib import gen_libs
    from .lib import gen_class
    from .git_lib import git_class
    from . import version

except (ValueError, ImportError) as err:
    import lib.gen_libs as gen_libs                     # pylint:disable=R0402
    import lib.gen_class as gen_class                   # pylint:disable=R0402
    import git_lib.git_class as git_class               # pylint:disable=R0402
    import version

__version__ = version.__version__


def help_message():

    """Function:  help_message

    Description:  Displays the program's docstring which is the help and usage
        message when -h option is selected.

    Arguments:

    """

    print(__doc__)


def load_cfg(cfg_name, cfg_dir):

    """Function:  load_cfg

    Description:  Load the configuration file and validate the settings.

    Arguments:
        (input) cfg_name -> Configuration file name
        (input) cfg_dir -> Directory path to the configuration file
        (output) cfg -> Configuration module handler
        (output) status_flag -> True|False - successfully validate config file
        (output) err_messages -> List of error messages

    """

    status_flag = True
    err_messages = []
    cfg = gen_libs.load_module(cfg_name, cfg_dir)
    status, err_msg = gen_libs.chk_crt_dir(cfg.work_dir, write=True, read=True)

    if not status:
        status_flag = status
        err_messages.append(err_msg)

    status, err_msg = gen_libs.chk_crt_dir(cfg.err_dir, write=True, read=True)

    if not status:
        status_flag = status
        err_messages.append(err_msg)

    status, err_msg = gen_libs.chk_crt_dir(cfg.archive_dir, write=True,
                                           read=True)

    if not status:
        status_flag = status
        err_messages.append(err_msg)

    status, err_msg = gen_libs.chk_crt_file(cfg.log_file, create=True,
                                            write=True, read=True)

    if not status:
        status_flag = status
        err_messages.append(err_msg)

    return cfg, status_flag, err_messages


def is_git_repo(path):

    """Function:  is_git_repo

    Description:  Determines if the path is a local git repository.

    Arguments:
        (input) path -> Directory path to git repository
        (output)  True|False -> If the directory path is a git repository

    """

    try:
        git.Repo(path).git_dir                      # pylint:disable=W0106
        return True

    except git.exc.InvalidGitRepositoryError:       # pylint:disable=E1101
        return False


def send_mail(to_line, subj, mail_body):

    """Function:  send_mail

    Description:  Compiles and sends out an email notification message.

    Arguments:
        (input) to_line -> Email's to line
        (input) subj -> Email subject line
        (input) mail_body -> Email body list

    """

    body = list(mail_body)
    frm_line = getpass.getuser() + "@" + socket.gethostname()
    email = gen_class.Mail(to_line, subj, frm_line)

    for line in body:
        email.add_2_msg(line, new_line=True)

    email.send_mail()


def post_body(gitr, body=None):

    """Function:  post_body

    Description:  Append default post-header to mail body.

    Arguments:
        (input) gitr -> Git class instance
        (input) body -> Mail list body
        (output) body -> Body of the email

    """

    if body is None:
        body = []

    else:
        body = list(body)

    body.append("URL: " + gitr.url)
    body.append("Git Dir: " + gitr.git_dir)
    body.append("Branch: " + gitr.branch)
    body.append("DTG: " + datetime.datetime.strftime(datetime.datetime.now(),
                                                     "%Y-%m-%d %H:%M:%S"))

    return body


def prepare_mail(gitr, status, line_list=None, msg=None):

    """Function:  prepare_mail

    Description:  Prepare email body with a set header.

    Arguments:
        (input) gitr -> Git class instance
        (input) status -> True|False - Status success of Git command
        (input) line_list -> List of lines to add to email body
        (input) msg -> Dictionary of error message from Git command
        (output) body -> Body of the email

    """

    if line_list is None:
        line_list = []

    else:
        line_list = list(line_list)

    if msg is not None:
        msg = dict(msg)

    body = []

    if status:
        subj = "Merge completed for: " + gitr.repo_name
        body.append("Merge of project has been completed.")

    else:
        subj = "Merge error for: " + gitr.repo_name
        body.append("Merge of project has failed.")

        for line in line_list:
            body.append(line)

        if msg:
            for key in list(msg.keys()):
                body.append("%s: %s" % (key, msg[key]))

    body = post_body(gitr, body)

    return subj, body


def post_process(                                       # pylint:disable=R0913
        gitr, cfg, log, status, line_list=None, msg=None):

    """Function:  post_process

    Description:  Post processing of the git repository.

    Arguments:
        (input) gitr -> Git class instance
        (input) cfg -> Configuration settings module for the program
        (input) log -> Log class instance
        (input) status -> True|False - Status success of command
        (input) line_list -> List of lines to add to email body
        (input) msg -> Dictionary of error message from Git command

    """

    if line_list is not None:
        line_list = list(line_list)

    if msg is not None:
        msg = dict(msg)

    if cfg.to_line:
        subj, body = prepare_mail(gitr, status, line_list, msg)
        send_mail(cfg.to_line, subj, body)

    dest_dir = os.path.basename(gitr.git_dir) + "." \
        + datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S")

    if status:
        log.log_info("post_process:  Project was moved to: %s."
                     % (os.path.join(cfg.archive_dir, dest_dir)))
        gen_libs.mv_file2(
            gitr.git_dir, os.path.join(cfg.archive_dir, dest_dir))

    else:
        log.log_info("post_process:  Project was moved to: %s."
                     % (os.path.join(cfg.err_dir, dest_dir)))
        gen_libs.mv_file2(gitr.git_dir, os.path.join(cfg.err_dir, dest_dir))


def post_check(gitr, cfg, log):

    """Function:  post_check

    Description:  Check to see the local Git is in sync with the remote Git.

    Arguments:
        (input) gitr -> Git class instance
        (input) cfg -> Configuration settings module for the program
        (input) log -> Log class instance

    """

    log.log_info("post_check:  Post checking...")

    ahead = gitr.is_commits_ahead(gitr.branch)
    behind = gitr.is_commits_behind(gitr.branch)

    if ahead or behind:
        log.log_err("post_check:  Local repo is not in sync with remote repo")

        if ahead:
            log.log_err("post_check: Local repo is %s commits ahead of remote."
                        % (ahead))
            line_list = ["Local repo is %s commits ahead of remote." % (ahead)]

        else:
            log.log_err("post_check:  Local repo is %s commits behind remote."
                        % (behind))
            line_list = ["Local repo is %s commits behind remote." % (behind)]

        post_process(gitr, cfg, log, False, line_list)

    else:
        log.log_info("post_check:  Processing of: %s completed."
                     % (gitr.git_dir))
        line_list = ["Processing of: %s completed." % (gitr.git_dir)]
        post_process(gitr, cfg, log, True, line_list)


def quarantine_files(gitr, cfg, log, status=None):

    """Function:  quarantine_files

    Description:  Copy files out of Git repo into a quarantine directory.

    Arguments:
        (input) gitr -> Git class instance
        (input) cfg -> Configuration settings module for the program
        (input) log -> Log class instance
        (input) status -> added|modified - Status of the file for quarantine

    """

    dtg = datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S")
    q_dir = gitr.repo_name + "-" + dtg
    file_list = []
    subj = "No Subject"

    if status == "added":
        file_list = list(gitr.new_files)

    elif status == "modified":
        file_list = list(gitr.chg_files)

    if file_list:
        gen_libs.chk_crt_dir(os.path.join(cfg.quar_dir, q_dir), create=True)
        subj = "File quaratine in Git Repo: %s" % (gitr.repo_name)
        body = []
        body.append("Git Repo: %s" % (gitr.repo_name))

    for item in file_list:
        log.log_info("quarantine_files:  File '%s' was quarantined." % (item))
        log.log_info("quarantine_files:  Reason -> File was '%s'" % (status))
        dir_path = os.path.dirname(item)

        if dir_path and not os.path.exists(os.path.join(cfg.quar_dir, q_dir,
                                                        dir_path)):
            os.makedirs(os.path.join(cfg.quar_dir, q_dir, dir_path))

        gen_libs.cp_file(item, gitr.git_dir, os.path.join(cfg.quar_dir, q_dir,
                                                          dir_path))
        f_type = "File"

        log.log_info("quarantine_files:  %s '%s' was moved to: %s"
                     % (f_type, item, os.path.join(cfg.quar_dir, q_dir)))
        body.append("%s '%s' was moved to: %s"
                    % (f_type, item, os.path.join(cfg.quar_dir, q_dir)))
        body.append("\tReason:  %s was '%s'" % (f_type, status))

    if cfg.to_line and file_list:
        body = post_body(gitr, body)
        send_mail(cfg.to_line, subj, body)


def quarantine(gitr, cfg, log):

    """Function:  quarantine

    Description:  Get dirty and untracked files and quarantine them.

    Arguments:
        (input) gitr -> Git class instance
        (input) cfg -> Configuration settings module for the program
        (input) log -> Log class instance

    """

    if gitr.chg_files:
        log.log_info("quarantine:  Quarantine modified files")
        quarantine_files(gitr, cfg, log, status="modified")

    if gitr.new_files:
        log.log_info("quarantine:  Quarantine added files")
        quarantine_files(gitr, cfg, log, status="added")

    if gitr.rm_files:
        log.log_info("quarantine:  Removed files detected")
        log.log_info("quarantine:  Files detected:  %s" % (gitr.rm_files))

        if cfg.to_line:
            subj = "Removed files detected in Git Repo: %s" % (gitr.repo_name)
            body = []
            body.append("Git Repo: %s" % (gitr.repo_name))
            body.append("Removed files detected: %s" % (gitr.rm_files))
            body = post_body(gitr, body)
            send_mail(cfg.to_line, subj, body)


def merge_project(gitr, cfg, log, **kwargs):

    """Function:  merge_project

    Description:  Merge, and push the project to the remote Git repo.

    Arguments:
        (input) gitr -> Git class instance
        (input) cfg -> Configuration settings module for the program
        (input) log -> Log class instance
        (input) **kwargs:
            allow -> True|False - Allow merge of unrelated histories

    """

    log.log_info("merge_project:  Fetching and setting up branches.")
    status1, msg1 = gitr.priority_merge(allow=kwargs.get("allow", False))

    if status1:
        log.log_info("merge_project:  Pushing changes to remote Git.")
        status2, msg2 = gitr.git_pu()

        if status2:
            log.log_info("merge_project:  Pushing tags to remote Git.")
            status3, msg3 = gitr.git_pu(tags=True)

            if status3:
                post_check(gitr, cfg, log)

            else:
                log.log_err("merge_project:  Fail to push tags to remote git.")
                log.log_err("merge_project:  Status 3 Message: %s" % (msg3))
                line_list = ["Failure to push tags to remote git."]
                post_process(gitr, cfg, log, status3, line_list, msg3)

        else:
            log.log_err("merge_project:  Fail to push to remote git.")
            log.log_err("merge_project:  Status 2 Message: %s" % (msg2))
            line_list = ["Failure to push to remote git."]
            post_process(gitr, cfg, log, status2, line_list, msg2)

    else:
        log.log_err("merge_project:  Failure to merge branch %s into %s."
                    % (gitr.mod_branch, gitr.branch))
        log.log_err("merge_project:  Status 1 Message: %s" % (msg1))
        line_list = ["Failure to merge branch %s into %s." % (gitr.mod_branch,
                                                              gitr.branch)]
        post_process(gitr, cfg, log, status1, line_list, msg1)


def process_project(gitr, cfg, log, **kwargs):

    """Function:  process_project

    Description:  Prepare for the merge of the project.

    Arguments:
        (input) gitr -> Git class instance
        (input) cfg -> Configuration settings module for the program
        (input) log -> Log class instance
        (input) **kwargs:
            allow -> True|False - Allow merge of unrelated histories

    """

    log.log_info("process_project:  Fetching and setting up branches.")
    status1, msg1 = gitr.git_fetch()

    if status1:
        log.log_info("process_project:  Renaming branch to: %s."
                     % (gitr.mod_branch))
        status2, msg2 = gitr.rename_br()

        if status2:
            log.log_info("process_project:  Checking out branch: %s."
                         % (gitr.branch))
            status3, msg3 = gitr.git_co()

            if status3:
                merge_project(gitr, cfg, log, **kwargs)

            else:
                log.log_err("process_project:  Fail to checkout branch: %s."
                            % (gitr.branch))
                log.log_err("process_project:  Status 3 Message: %s" % (msg3))
                line_list = ["Failure to checkout branch: %s." % (gitr.branch)]
                post_process(gitr, cfg, log, status3, line_list, msg3)

        else:
            log.log_err("process_project:  Fail rename branch to: %s."
                        % (gitr.mod_branch))
            log.log_err("process_project:  Status 2 Message: %s" % (msg2))
            line_list = ["Failure rename branch to: %s." % (gitr.mod_branch)]
            post_process(gitr, cfg, log, status2, line_list, msg2)

    else:
        log.log_err("process_project:  Fail to fetch from remote Git repo.")
        log.log_err("process_project:  Status 1 Message: %s" % (msg1))
        line_list = ["Failure to fetch from remote Git repo."]
        post_process(gitr, cfg, log, status1, line_list, msg1)


def process_changes(gitr, cfg, log):

    """Function:  process_changes

    Description:  Locate and process dirty and untracked files.

    Arguments:
        (input) gitr -> Git class instance
        (input) cfg -> Configuration settings module for the program
        (input) log -> Log class instance

    """

    if gitr.is_dirty() or gitr.is_untracked():
        gitr.get_dirty()
        gitr.get_untracked()
        log.log_info("process_changes:  Quarantine process running")
        quarantine(gitr, cfg, log)
        log.log_info("process_changes:  Processing dirty files option: %s"
                     % (cfg.dirty))
        gitr.process_dirty(option=cfg.dirty)
        log.log_info("process_changes:  Processing untracked files option: %s"
                     % (cfg.untracked))
        gitr.process_untracked(option=cfg.untracked)


def detach_head(gitr, log):

    """Function:  detach_head

    Description:  Detach the head from a git project, move the head to the
        latest commit id and remove the existing branch.

    Arguments:
        (input) gitr -> Git class instance
        (input) log -> Log class instance
        (output) status -> True|False - Status of detaching head in project
        (output) err_msg -> Error messages detected, if any

    """

    status = True
    err_msg = None

    if len(gitr.gitrepo.branches) == 0:
        log.log_info("detach_head:  Head already detached")

    elif len(gitr.gitrepo.branches) == 1:
        log.log_info("detach_head:  Detaching head...")
        current_br = gitr.get_br_name()
        head_status = gitr.detach_head()

        if head_status:
            log.log_info("detach_head:  Possible problem detected")
            status = False
            err_msg = "WARN: Message detected: %s" % (head_status)

        else:
            log.log_info("detach_head:  Removing branch: %s" % (current_br))
            status, err_msg = gitr.remove_branch(current_br, no_chk=True)

    else:
        log.log_warn("detach_head:  Multiple branches detected: %s"
                     % (gitr.gitrepo.branches))
        status = False
        err_msg = "WARN:  Multiple branches detected: %s" \
                  % (gitr.gitrepo.branches)

    return status, err_msg


def merge(args, cfg, log):

    """Function:  merge

    Description:  Controls the merging of a local repository with a remote
        repository, but having the local repository as the priority
        repository.

    Arguments:
        (input) args -> ArgParser class instance
        (input) cfg -> Configuration settings module for the program
        (input) log -> Log class instance

    """

    log.log_info("merge:  Starting merge of:  %s" % (args.get_val("-r")))
    arch_dir = os.path.join(
        cfg.archive_dir, os.path.basename(args.get_val("-p")) + ".Original." +
        datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S"))
    gen_libs.cp_dir(args.get_val("-p"), arch_dir)
    log.log_info("merge:  Original repo dir copied to:  %s" % (arch_dir))
    gen_libs.mv_file2(args.get_val("-p"), cfg.work_dir)
    git_dir = os.path.join(cfg.work_dir, os.path.basename(args.get_val("-p")))

    if is_git_repo(git_dir):
        log.log_info("merge:  Updating Git config file")
        giti = git_class.GitConfig(git_dir)
        giti.set_user(cfg.name)
        giti.set_email(cfg.email)
        log.log_info("merge:  Processing: %s directory" % (git_dir))

        # Use alias for servername
        if args.arg_exist("-a"):
            url = cfg.prefix + args.get_val("-r")

        else:
            url = cfg.prefix + cfg.git_server

        url = url + ":" + cfg.git_project + "/" + args.get_val("-r") + ".git"
        gitr = git_class.GitMerge(
            args.get_val("-r"), git_dir, url, cfg.branch, cfg.mod_branch)
        gitr.create_gitrepo()
        gitr.set_remote()

        if gitr.is_remote():
            cleanup_repo(gitr, cfg, log, allow=args.arg_exist("-u"))

        else:
            log.log_err("merge:  %s does not exist at remote repo."
                        % (gitr.url))
            line_list = ["Remote git repository does not exist"]
            post_process(gitr, cfg, log, False, line_list)

    else:
        log.log_err("merge:  %s is not a local Git repository" % (git_dir))

        if cfg.to_line:
            subj = "Merge error for: " + git_dir
            body = ["Local directory is not a Git repository.",
                    "Project Dir: " + git_dir]
            body.append(
                "DTG: " + datetime.datetime.strftime(
                    datetime.datetime.now(), "%Y-%m-%d %H:%M:%S"))
            send_mail(cfg.to_line, subj, body)

        dest_dir = os.path.basename(git_dir) + "." \
            + datetime.datetime.strftime(
                datetime.datetime.now(), "%Y%m%d_%H%M%S")
        gen_libs.mv_file2(git_dir, os.path.join(cfg.err_dir, dest_dir))


def cleanup_repo(gitr, cfg, log, **kwargs):

    """Function:  cleanup_repo

    Description:  Checks to ensure head is detached and there are not any dirty
        or untracked changes before merging repository.

    Arguments:
        (input) gitr -> Git class instance
        (input) cfg -> Configuration settings module for the program
        (input) log -> Log class instance
        (input) **kwargs:
            allow -> True|False - Allow merge of unrelated histories

    """

    process_changes(gitr, cfg, log)

    if not gitr.is_dirty() and not gitr.is_untracked():
        status, err_msg = detach_head(gitr, log)

        if status:
            log.log_info("merge:  Processing project...")
            process_project(gitr, cfg, log, **kwargs)

        else:
            log.log_err("merge:  Problem detected in detaching head.")
            log.log_err("merge: Message: %s" % (err_msg))
            line_list = [err_msg]
            post_process(gitr, cfg, log, False, line_list)

    else:
        log.log_err("merge:  Still dirty entries in local repo.")
        line_list = ["There is still dirty entries in local repo."]
        post_process(gitr, cfg, log, False, line_list)


def run_program(args, func_dict, **kwargs):

    """Function:  run_program

    Description:  Controls the running of the program and sets up a logger
        class for the running instance of the program.

    Arguments:
        (input) args -> ArgParser class instance
        (input) func_dict -> Dict of function calls and associated options

    """

    func_dict = dict(func_dict)
    cfg, status_flag, msg_list = load_cfg(
        args.get_val("-c"), args.get_val("-d"))

    # Disable email capability if option detected
    if args.arg_exist("-n"):
        cfg.to_line = None

    if status_flag:
        log = gen_class.Logger(
            cfg.log_file, cfg.log_file, "INFO",
            "%(asctime)s %(levelname)s %(message)s", "%Y-%m-%dT%H:%M:%SZ")
        str_val = "=" * 80
        log.log_info("%s Initialized" % (args.get_val("-r")))
        log.log_info("%s" % (str_val))
        log.log_info("Project:  %s" % (args.get_val("-r")))
        log.log_info("Project Directory:  %s" % (args.get_val("-p")))
        log.log_info("%s" % (str_val))

        # Intersect args_array & func_dict to find which functions to call.
        for opt in set(args.get_args_keys()) & set(func_dict.keys()):
            func_dict[opt](args, cfg, log, **kwargs)

        log.log_close()

    else:
        print("Error:  Problem(s) in configuration file.")
        print("Message(s):")

        for item in msg_list:
            print(item)


def main(**kwargs):

    """Function:  main

    Description:  Initializes program-wide used variables and processes command
        line arguments and values.

    Variables:
        dir_perms_chk -> contains directories and their octal permissions
        func_dict -> dictionary list for the function calls or other options
        opt_req_list -> contains options that are required for the program
        opt_val_list -> contains options which require values

    Arguments:
        (input) argv -> Arguments from the command line
        (input) **kwargs:
            argv_list -> List of arguments from a wrapper program

    """

    sys.argv = kwargs.get("argv_list", sys.argv)
    dir_perms_chk = {"-d": 5, "-p": 5}
    func_dict = {"-M": merge}
    opt_req_list = ["-c", "-d", "-p", "-r"]
    opt_val_list = ["-c", "-d", "-p", "-r"]

    # Process argument list from command line
    args = gen_class.ArgParser(sys.argv, opt_val=opt_val_list)

    if args.arg_parse2()                                            \
       and not gen_libs.help_func(args, __version__, help_message):

        # Set Repo Name if not passed
        if not args.arg_exist("-r") and args.arg_exist("-p"):
            args.insert_arg("-r", os.path.basename(args.get_val("-p")))

        if args.arg_require(opt_req=opt_req_list)           \
           and args.arg_dir_chk(dir_perms_chk=dir_perms_chk):

            try:
                prog_lock = gen_class.ProgramLock(
                    sys.argv, args.get_val("-r", def_val=""))
                run_program(args, func_dict)
                del prog_lock

            except gen_class.SingleInstanceException:
                print("WARNING:  lock in place for merge with id of: %s"
                      % (args.get_val("-r", def_val="")))


if __name__ == "__main__":
    sys.exit(main())
