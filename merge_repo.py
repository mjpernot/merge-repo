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
        merge_repo.py -c config -d config_dir -p repo_directory [-r repo_name]
            {-M [-a] [-n]}
            {-v | -h}

    Arguments:
        -c file_name => Name of merge_repo configuration file.
        -d directory_path => Directory path to the configuration file.
        -p directory_path => Absolute path name to Project directory.
        -r repo_name => Repository name being merged (e.g. "python-lib").

        -M => Run the merge function.
            -a => Use the repository name as an alias in the Git url.  Used in
                a Github repository setting.
            -n => Override email setting and do not send email notifications.

        -v => Display version of this program.
        -h => Help and usage message.

        NOTE 1:  -v or -h overrides the other options.
        NOTE 2:  If -r is not passed, will use the basename from the -p option
            directory path to populate the -r option.
        NOTE 3:  If -a is used, this assumes there is an alias name in the
            account's ~/.ssh/config that matches the repository name.

    Notes:
        Config file:
            # Git Project name.
            git_project="ProjectName"
            # Git Server Fully Qualified Domain Name.
            #  Not required if using the -a option.
            git_server="GitServerFQDN"
            # Directory of where the merge will take place.
            work_dir="/PATH_DIRECTORY/merge-repo/work_dir"
            # Directory where projects will be archived if errors encountered.
            err_dir="/PATH_DIRECTORY/merge-repo/error_dir"
            # Directory where projects will be archived after a merge.
            archive_dir="/PATH_DIRECTORY/merge-repo/archive_dir"
            # Directory where repository items will be quarantined.
            quar_dir="/PATH_DIRECTORY/merge-repo/quarantine"
            # Email addresses for notification.
            #  If set to None, will not email out notifications.
            to_line="EMAIL_ADDRESS@EMAIL_DOMAIN"
            # Directory where log files will be placed.
            log_file="/PATH_DIRECTORY/merge-repo/logs/merge-repo.log"
            # Do not modify the settings below unless you know what you are
            #   doing.
            # Local Git Repository user name.
            name="gituser"
            # Local Git Repository user email address.
            email="gituser@domain.mail"
            # Branch on which the merge will take place on.
            branch="develop"
            # Name of temporary branch on local git repo.
            mod_branch="mod_release"
            # Option setting for dirty items:  revert|commit
            dirty="revert"
            # Option setting for untracked items:  add|remove
            untracked="remove"
            # Git Url Prefix
            prefix="git@"

        Note:  Ensure directories exist or are created for work_dir, err_dir,
            archive_dir, quar_dir, and log_file.

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
                > ssh-keygen -t dsa
                    Name:  id_dsa.GitRepoName
                    Passphrase:  Null
            2.  Add project entry to ssh config file.
                > vim ~/.ssh/config file
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
                > git clone git@GitRepoName:GitProject/GitRepoName.git

    Examples:
        merge_repo.py -c merge -d config -r python-lib -p /local/python-lib -M

"""

# Libraries and Global Variables

# Standard
# For Python 2.6/2.7: Redirection of stdout in a print command.
from __future__ import print_function
import sys
import os
import datetime
import socket
import getpass

# Third-party
import git

# Local
import lib.arg_parser as arg_parser
import lib.gen_libs as gen_libs
import lib.gen_class as gen_class
import git_lib.git_class as git_class
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
        (input) cfg_name -> Configuration file name.
        (input) cfg_dir -> Directory path to the configuration file.
        (output) cfg -> Configuration module handler.
        (output) status_flag -> True|False - successfully validate config file.
        (output) err_messages -> List of error messages.

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
        (input) path -> Directory path to git repository.
        (output)  True|False -> If the directory path is a git repository.

    """

    try:
        git.Repo(path).git_dir
        return True

    except git.exc.InvalidGitRepositoryError:
        return False


def send_mail(to_line, subj, mail_body):

    """Function:  send_mail

    Description:  Compiles and sends out an email notification message.

    Arguments:
        (input) to_line -> Email's to line.
        (input) subj -> Email subject line.
        (input) mail_body -> Email body list.

    """

    body = list(mail_body)
    frm_line = getpass.getuser() + "@" + socket.gethostname()
    email = gen_class.Mail(to_line, subj, frm_line)

    for line in body:
        email.add_2_msg(line + "\n")

    email.send_mail()


def post_body(gitr, body=None):

    """Function:  post_body

    Description:  Append default post-header to mail body.

    Arguments:
        (input) gitr -> Git class instance.
        (input) body -> Mail list body.
        (output) body -> Body of the email.

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
        (input) gitr -> Git class instance.
        (input) status -> True|False - Status success of Git command.
        (input) line_list -> List of lines to add to email body.
        (input) msg -> Dictionary of error message from Git command.
        (output) body -> Body of the email.

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
            for key in msg.keys():
                body.append("%s: %s" % (key, msg[key]))

    body = post_body(gitr, body)

    return subj, body


def move(from_dir, to_dir):

    """Function:  move

    Description:  Move of git repo to proper directory for storage.

    Arguments:
        (input) from_dir -> Source directory.
        (input) to_dir -> Desitination directory.

    """

    gen_libs.mv_file2(from_dir, to_dir)


def post_process(gitr, cfg, log, status, line_list=None, msg=None):

    """Function:  post_process

    Description:  Post processing of the git repository.

    Arguments:
        (input) gitr -> Git class instance.
        (input) cfg -> Configuration settings module for the program.
        (input) log -> Log class instance.
        (input) status -> True|False - Status success of command.
        (input) line_list -> List of lines to add to email body.
        (input) msg -> Dictionary of error message from Git command.

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
        move(gitr.git_dir, os.path.join(cfg.archive_dir, dest_dir))

    else:
        log.log_info("post_process:  Project was moved to: %s."
                     % (os.path.join(cfg.err_dir, dest_dir)))
        move(gitr.git_dir, os.path.join(cfg.err_dir, dest_dir))


def post_check(gitr, cfg, log):

    """Function:  post_check

    Description:  Check to see the local Git is in sync with the remote Git.

    Arguments:
        (input) gitr -> Git class instance.
        (input) cfg -> Configuration settings module for the program.
        (input) log -> Log class instance.

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
        (input) gitr -> Git class instance.
        (input) cfg -> Configuration settings module for the program.
        (input) log -> Log class instance.
        (input) status -> added|modified - Status of the file for quarantine.

    """

    dtg = datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S")
    q_dir = gitr.repo_name + "-" + dtg
    file_list = []

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
        (input) gitr -> Git class instance.
        (input) cfg -> Configuration settings module for the program.
        (input) log -> Log class instance.

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


def merge_project(gitr, cfg, log):

    """Function:  merge_project

    Description:  Merge, and push the project to the remote Git repo.

    Arguments:
        (input) gitr -> Git class instance.
        (input) cfg -> Configuration settings module for the program.
        (input) log -> Log class instance.

    """

    log.log_info("merge_project:  Fetching and setting up branches.")
    status1, msg1 = gitr.priority_merge()

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


def process_project(gitr, cfg, log):

    """Function:  process_project

    Description:  Prepare for the merge of the project.

    Arguments:
        (input) gitr -> Git class instance.
        (input) cfg -> Configuration settings module for the program.
        (input) log -> Log class instance.

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
                merge_project(gitr, cfg, log)

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
        (input) gitr -> Git class instance.
        (input) cfg -> Configuration settings module for the program.
        (input) log -> Log class instance.

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
        (input) gitr -> Git class instance.
        (input) log -> Log class instance.
        (output) status -> True|False - Status of detaching head in project.
        (output) err_msg -> Error messages detected, if any.

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


def merge(args_array, cfg, log):

    """Function:  merge

    Description:  Controls the merging of a local repository with a remote
        repository, but having the local repository as the priority
        repository.

    Arguments:
        (input) args_array -> Dict of command line options and values.
        (input) cfg -> Configuration settings module for the program.
        (input) log -> Log class instance.

    """

    args_array = dict(args_array)
    log.log_info("merge:  Starting merge of:  %s" % (args_array["-r"]))
    gen_libs.mv_file2(args_array["-p"], cfg.work_dir)
    git_dir = os.path.join(cfg.work_dir, os.path.basename(args_array["-p"]))

    if is_git_repo(git_dir):
        log.log_info("merge:  Updating Git config file")
        giti = git_class.GitConfig(git_dir)
        giti.set_user(cfg.name)
        giti.set_email(cfg.email)
        log.log_info("merge:  Processing: %s directory" % (git_dir))

        # Use alias for servername
        if "-a" in args_array:
            url = cfg.prefix + args_array["-r"]

        else:
            url = cfg.prefix + cfg.git_server

        url = url + ":" + cfg.git_project + "/" + args_array["-r"] + ".git"
        gitr = git_class.GitMerge(args_array["-r"], git_dir, url, cfg.branch,
                                  cfg.mod_branch)
        gitr.create_gitrepo()
        gitr.set_remote()

        if gitr.is_remote():
            _process_changes(gitr, cfg, log)

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
            body.append("DTG: "
                        + datetime.datetime.strftime(datetime.datetime.now(),
                                                     "%Y-%m-%d %H:%M:%S"))
            send_mail(cfg.to_line, subj, body)

        dest_dir = os.path.basename(git_dir) + "." \
            + datetime.datetime.strftime(datetime.datetime.now(),
                                         "%Y%m%d_%H%M%S")
        move(git_dir, os.path.join(cfg.err_dir, dest_dir))


def _process_changes(gitr, cfg, log):

    """Function:  _process_changes

    Description:  Private function for merge function.  Checks to ensure head
        is detached and there are not any dirty or untracked changes before
        merging repository.

    Arguments:
        (input) gitr -> Git class instance.
        (input) cfg -> Configuration settings module for the program.
        (input) log -> Log class instance.

    """

    process_changes(gitr, cfg, log)

    if not gitr.is_dirty() and not gitr.is_untracked():
        status, err_msg = detach_head(gitr, log)

        if status:
            log.log_info("merge:  Processing project...")
            process_project(gitr, cfg, log)

        else:
            log.log_err("merge:  Problem detected in detaching head.")
            log.log_err("merge: Message: %s" % (err_msg))
            line_list = [err_msg]
            post_process(gitr, cfg, log, False, line_list)

    else:
        log.log_err("merge:  Still dirty entries in local repo.")
        line_list = ["There is still dirty entries in local repo."]
        post_process(gitr, cfg, log, False, line_list)


def run_program(args_array, func_dict, **kwargs):

    """Function:  run_program

    Description:  Controls the running of the program and sets up a logger
        class for the running instance of the program.

    Arguments:
        (input) args_array -> Dict of command line options and values.
        (input) func_dict -> Dict of function calls and associated options.

    """

    args_array = dict(args_array)
    func_dict = dict(func_dict)
    cfg, status_flag, msg_list = load_cfg(args_array["-c"], args_array["-d"])

    # Disable email capability if option detected
    if args_array.get("-n", False):
        cfg.to_line = None

    if status_flag:
        log = gen_class.Logger(cfg.log_file, cfg.log_file, "INFO",
                               "%(asctime)s %(levelname)s %(message)s",
                               "%Y-%m-%dT%H:%M:%SZ")
        str_val = "=" * 80
        log.log_info("%s Initialized" % (args_array["-r"]))
        log.log_info("%s" % (str_val))
        log.log_info("Project:  %s" % (args_array["-r"]))
        log.log_info("Project Directory:  %s" % (args_array["-p"]))
        log.log_info("%s" % (str_val))

        # Intersect args_array & func_dict to find which functions to call.
        for opt in set(args_array.keys()) & set(func_dict.keys()):
            func_dict[opt](args_array, cfg, log, **kwargs)

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
        dir_chk_list -> contains options which will be directories.
        func_dict -> dictionary list for the function calls or other options.
        opt_req_list -> contains options that are required for the program.
        opt_val_list -> contains options which require values.

    Arguments:
        (input) argv -> Arguments from the command line.
        (input) **kwargs:
            argv_list -> List of arguments from a wrapper program.

    """

    cmdline = gen_libs.get_inst(sys)
    cmdline.argv = kwargs.get("argv_list", cmdline.argv)
    dir_chk_list = ["-d", "-p"]
    func_dict = {"-M": merge}
    opt_req_list = ["-c", "-d", "-p", "-r"]
    opt_val_list = ["-c", "-d", "-p", "-r"]

    # Process argument list from command line.
    args_array = arg_parser.arg_parse2(cmdline.argv, opt_val_list)

    if not gen_libs.help_func(args_array, __version__, help_message):

        # Set Repo Name if not passed
        if "-r" not in args_array.keys() and "-p" in args_array.keys():
            args_array["-r"] = os.path.basename(args_array["-p"])

        if not arg_parser.arg_require(args_array, opt_req_list) \
           and not arg_parser.arg_dir_chk_crt(args_array, dir_chk_list):

            try:
                prog_lock = gen_class.ProgramLock(cmdline.argv,
                                                  args_array.get("-r", ""))
                run_program(args_array, func_dict)
                del prog_lock

            except gen_class.SingleInstanceException:
                print("WARNING:  lock in place for merge with id of: %s"
                      % (args_array.get("-r", "")))


if __name__ == "__main__":
    sys.exit(main())
