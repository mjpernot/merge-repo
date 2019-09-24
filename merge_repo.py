#!/usr/bin/python
# Classification (U)

"""Program:  merge_repo.py

    Description:  Merge an external local Git repository into an existing
        remote Git repository.  The merge process will clean up the new
        project using Git of dirty and untracked files and it will then pull
        the existing remote Git branch to the local Git repository before
        merging the local Git repo with the existing Git repo.  Once the
        branches have been merged the updated branch will be pushed back to
        the remote Git repository.

        NOTE 1:  The external Git repo being imported will have priority during
            the merge.  This means that the imported Git repo will have
            precedence over the changes made to the remote Git repo.
        NOTE 2:  The external local Git repository must come in as a detached
            head repository and with no named branches in the repository.
        NOTE 3:  The -a option allows for using multiple deploy keys for a
            single user account into Git (e.g. required for Github).  There
            must be an entry in the account's ~/.ssh/config file with an alias
            name that matches the respository name being processed.  See Notes
            section on format of entry in ~/.ssh/config file.

    Usage:
        merge_repo.py -c config -d config_dir -p repo_directory {-r repo_name}
            [-M] {-a} {-v | -h}

    Arguments:
        -c file_name => Name of merge_repo configuration file.
        -d directory_path => Directory path to the configuration file.
        -M => Run the merge function.
        -a => Use the repository name as an alias in the Git url.
        -r repo_name => Repository name being merged (e.g. "hp-python-lib").
        -p directory_path => Project directory which is the full absolute path.
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
            url_project="{ProjectName}"
            # Git Server Fully Qualified Domain Name.
            #  Not required for -a option.
            url_servername="{GitServerFQDN}"
            # Directory of where the merge will take place.
            work_dir="{PATH_DIRECTORY}/work_dir"
            # Directory where projects will be archived if encounter errors.
            err_dir="{PATH_DIRECTORY}/error_dir"
            # Directory where projects will be archived after a merge.
            archive_dir="{PATH_DIRECTORY}/archive_dir"
            # Directory where project items will be quarantined.
            quar_dir="/home/mark.j.pernot/merge/quarantine"
            # Email addresses for notification.
            to_line="{EMAIL_ADDRESS}@{EMAIL_DOMAIN}"
            # Directory where log files will be placed.
            log_file="{PATH_DIRECTORY}/logs/merge-repo.log"
            # Local Git Repository user name.
            name="gituser"
            # Local Git Repository user email address.
            email="gituser@domain.mail"
            # Do not modify unless you know what you are doing.
            # Branch on which the merge will take place on.
            branch="develop"
            # Name of temporary branch on local git repo.
            mod_branch="mod_release"
            # Option setting for dirty items:  revert|commit
            dirty="revert"
            # Option setting for untracked items:  add|remove
            untracked="remove"
            # Git Url Prefix
            url_prefix="git@"

        ~/.ssh/config file (only required for -a option):
            # RepoName is the Git repository name.
            # ServerNameFQDN is the Git server's fully qualified domain name.
            # UserName is the account name connecting to Git.
            Host {RepoName} {ServerNameFQDN}
             Hostname {ServerNameFQDN}
             User {UserName}
             IdentityFile {Path}/id_dsa.{RepoName}

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


def load_cfg(cfg_name, cfg_dir, **kwargs):

    """Function:  load_cfg

    Description:  Load the configuration file and validate the settings.

    Arguments:
        (input) cfg_name -> Configuration file name.
        (input) cfg_dir -> Directory path to the configuration file.
        (output) cfg -> Configuration module handler.
        (output) status_flag -> True|False - successfully validate config file.

    """

    status_flag = True
    cfg = gen_libs.load_module(cfg_name, cfg_dir)
    status, err_msg = gen_libs.chk_crt_dir(cfg.work_dir, write=True, read=True)

    if not status:
        status_flag = status

    status, err_msg = gen_libs.chk_crt_dir(cfg.err_dir, write=True, read=True)

    if not status:
        status_flag = status

    status, err_msg = gen_libs.chk_crt_dir(cfg.archive_dir, write=True,
                                           read=True)

    if not status:
        status_flag = status

    status, err_msg = gen_libs.chk_crt_file(cfg.log_file, create=True,
                                            write=True, read=True)

    if not status:
        status_flag = status

    return cfg, status_flag


def is_git_repo(path, **kwargs):

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


def send_mail(to_line, subj, mail_body, **kwargs):

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


def post_body(gitr, body=None, **kwargs):

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


def prepare_mail(gitr, status, line_list=None, msg=None, **kwargs):

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


def move(from_dir, to_dir, **kwargs):

    """Function:  move

    Description:  Move of git repo to proper directory for storage.

    Arguments:
        (input) from_dir -> Source directory.
        (input) to_dir -> Desitination directory.

    """

    gen_libs.mv_file2(from_dir, to_dir)


def post_process(gitr, cfg, log, status, line_list=None, msg=None, **kwargs):

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


def post_check(gitr, cfg, log, **kwargs):

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


def quarantine_files(gitr, cfg, log, status=None, **kwargs):

    """Function:  quarantine_files

    Description:  Copy files out of Git repo into a quarantine directory.

    Arguments:
        (input) gitr -> Git class instance.
        (input) cfg -> Configuration settings module for the program.
        (input) log -> Log class instance.
        (input) status -> added|modified - Status of the file for quarantine.

    """

    if status == "added":
        file_list = list(gitr.new_files)

    elif status == "modified":
        file_list = list(gitr.chg_files)

    else:
        file_list = []

    for item in file_list:
        log.log_info("quarantine_files:  File '%s' was quarantined." % (item))
        log.log_info("quarantine_files:  Reason -> File was '%s'" % (status))

        if os.path.isdir(os.path.join(self.git_dir, item)):
            q_file = item + "-" + gitr.repo_name + "-" \
                + datetime.datetime.strftime(datetime.datetime.now(),
                                             "%Y%m%d_%H%M%S")
            distutils.dir_util.copy_tree(os.path.join(self.git_dir, item),
                                         os.path.join(cfg.quar_dir, q_file))
            f_type = "Directory"

        else:
            q_file = item + "." + gitr.repo_name + "." \
                + datetime.datetime.strftime(datetime.datetime.now(),
                                             "%Y%m%d_%H%M%S")
            gen_libs.cp_file(item, gitr.git_dir, cfg.quar_dir, q_file)
            f_type = "File"

        log.log_info("quarantine_files:  %s '%s' was moved to: %s"
                     % (f_type, item, os.path.join(cfg.quar_dir, q_file)))
        subj = "File quaratine: %s in Git Repo: %s" % (item, gitr.repo_name)
        body = []
        body.append("Git Repo: %s" % (gitr.repo_name))
        body.append("%s '%s' was moved to: %s"
                    % (f_type, item, os.path.join(cfg.quar_dir, q_file)))
        body.append("Reason:  %s was '%s'" % (f_type, status))
        body = post_body(gitr, body)
        send_mail(cfg.to_line, subj, body)


def quarantine(gitr, cfg, log, **kwargs):

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
                log.log_err("merge_project:  Message: %s" % (msg3))
                line_list = ["Failure to push tags to remote git."]
                post_process(gitr, cfg, log, status3, line_list, msg3)

        else:
            log.log_err("merge_project:  Fail to push to remote git.")
            log.log_err("merge_project:  Message: %s" % (msg2))
            line_list = ["Failure to push to remote git."]
            post_process(gitr, cfg, log, status2, line_list, msg2)

    else:
        log.log_err("merge_project:  Failure to merge branch %s into %s."
                    % (gitr.mod_branch, gitr.branch))
        log.log_err("merge_project:  Message: %s" % (msg1))
        line_list = ["Failure to merge branch %s into %s." % (gitr.mod_branch,
                                                              gitr.branch)]
        post_process(gitr, cfg, log, status1, line_list, msg1)


def process_project(gitr, cfg, log, **kwargs):

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
                log.log_err("process_project:  Message: %s" % (msg3))
                line_list = ["Failure to checkout branch: %s." % (gitr.branch)]
                post_process(gitr, cfg, log, status3, line_list, msg3)

        else:
            log.log_err("process_project:  Fail rename branch to: %s."
                        % (gitr.mod_branch))
            log.log_err("process_project:  Message: %s" % (msg2))
            line_list = ["Failure rename branch to: %s." % (gitr.mod_branch)]
            post_process(gitr, cfg, log, status2, line_list, msg2)

    else:
        log.log_err("process_project:  Fail to fetch from remote Git repo.")
        log.log_err("process_project:  Message: %s" % (msg1))
        line_list = ["Failure to fetch from remote Git repo."]
        post_process(gitr, cfg, log, status1, line_list, msg1)


def process_changes(gitr, cfg, log, **kwargs):

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


def merge(args_array, cfg, log, **kwargs):

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
            process_changes(gitr, cfg, log)

            if not gitr.is_dirty() and not gitr.is_untracked():
                process_project(gitr, cfg, log)

            else:
                log.log_err("merge:  Still dirty entries in local repo.")
                line_list = ["There is still dirty entries in local repo."]
                post_process(gitr, cfg, log, False, line_list)

        else:
            log.log_err("merge:  %s does not exist at remote repo."
                        % (gitr.url))
            line_list = ["Remote git repository does not exist"]
            post_process(gitr, cfg, log, False, line_list)

    else:
        log.log_err("merge:  %s is not a local Git repository" % (git_dir))
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
    cfg, status_flag = load_cfg(args_array["-c"], args_array["-d"])

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
        print("Error:  Problem in configuration file.")


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

    sys.argv = kwargs.get("argv_list", sys.argv)

    dir_chk_list = ["-d", "-p"]
    func_dict = {"-M": merge}
    opt_req_list = ["-c", "-d", "-p", "-r"]
    opt_val_list = ["-c", "-d", "-p", "-r"]

    # Process argument list from command line.
    args_array = arg_parser.arg_parse2(sys.argv, opt_val_list)

    if not gen_libs.help_func(args_array, __version__, help_message):

        # Set Repo Name if not passed
        if "-r" not in args_array.keys():
            args_array["-r"] = os.path.basename(args_array["-p"])

        if not arg_parser.arg_require(args_array, opt_req_list) \
           and not arg_parser.arg_dir_chk_crt(args_array, dir_chk_list):

            try:
                prog_lock = gen_class.ProgramLock(sys.argv,
                                                  args_array.get("-r", ""))
                run_program(args_array, func_dict)
                del prog_lock

            except gen_class.SingleInstanceException:
                print("WARNING:  lock in place for merge with id of: %s"
                      % (args_array.get("-r", "")))


if __name__ == "__main__":
    sys.exit(main())
