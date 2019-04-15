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

        NOTE 1:  The local Git repo will be marked as the priority, which
            means the local Git repo will have priority over the changes
            made to the project.
        NOTE 2:  The default branch to be merged will be the master branch.
            This can be changed in the configuration file, but is not
            recommended.
        NOTE 3:  The external local Git repository must come in as a detached
            head repository with no named branches for the merge to take place.

    Usage:
        merge_repo.py -c config -d config_dir -p repo_directory {-r repo_name}
            [-M] {-v | -h}

    Arguments:
        -c file_name => Name of merge_repo configuration file.
        -d directory_path => Directory path to the configuration file.
        -M => Run the merge function.
        -r repo_name => Repository name being merged (e.g. "hp-python-lib").
        -p directory_path => Project directory which is the full absolute path.
        -v => Display version of this program.
        -h => Help and usage message.

        NOTE 1:  -v or -h overrides the other options.
        NOTE 2:  If -r is not passed, will use the basename from the -p option
            directory path to populate the -r option.

    Notes:
        Config file:
            # Base URL address to remote Git repository.  Not to include
            #   repository name.  This will be supplied by command line
            #   arguments.
            url="git@gitlab.code.dicelab.net:JAC-IDM/"

            # Directory of where the merge will take place.
            work_dir="{PATH_DIRECTORY}/work_dir"

            # Directory where projects will be archived if encounter errors.
            err_dir="{PATH_DIRECTORY}/error_dir"

            # Directory where projects will be archived after a merge.
            archive_dir="{PATH_DIRECTORY}/archive_dir"

            # Email addresses for notification.
            to_line="{EMAIL_ADDRESS}@{EMAIL_DOMAIN}"

            # Directory where log files will be placed.
            log_file="{PATH_DIRECTORY}/logs/merge-repo.log"

            # Do not modify unless you know what you are doing.
            # Branch on which the merge will take place on.
            branch="master"

    Examples:
        merge_repo.py -c merge -d config -r hp-python-lib
            -p /opt/local/hp-python-lib -M

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
import version

# Version
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
        (input) **kwargs:
            None
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
        (input) **kwargs:
            None
        (output)  True|False -> If the directory path is a git repository.

    """

    try:
        git.Repo(path).git_dir
        return True

    except git.exc.InvalidGitRepositoryError:
        return False


def is_remote(gitcmd, url, **kwargs):

    """Function:  is_remote

    Description:  Determines if the remote git repository exists.

    Arguments:
        (input) gitcmd -> Git command instance.
        (input) url -> Git URL address.
        (input) **kwargs:
            None
        (output)  True|False -> If the remote git repository exists.

    """

    try:
        _ = gitcmd.ls_remote(url)
        return True

    except git.exc.GitCommandError:
        return False


def is_remote_branch(gitcmd, branch, **kwargs):

    """Function:  is_remote_branch

    Description:  Determines if the branch exist in remote git repository.

    Arguments:
        (input) gitcmd -> Git command instance.
        (input) branch -> Git branch name.
        (input) **kwargs:
            None
        (output)  True|False -> If the branch in remote git repository.

    """

    try:
        gitcmd.rev_parse('--verify', branch)
        return True

    except git.exc.GitCommandError:
        return False


# Moved to git_class module.
def process_dirty(gitrepo, gitcmd, **kwargs):

    """Function:  process_dirty

    Description:  Check for and process dirty files.

    Arguments:
        (input) gitrepo -> Git repo class instance.
        (input) gitcmd -> Git command line class instance.
        (input) **kwargs:
            None

    """

    if gitrepo.is_dirty():

        for f_git in gitrepo.index.diff(None):

            if f_git.change_type == "D":

                # Test this code, not been tested before.
                gitcmd.rm([f_git], working_tree=True)

            elif f_git.change_type == "M":

                # Check this code works.
                gitcmd.add(f_git)

        # Can I stipulate what is in the comments dynamically?
        gitrepo.index.commit("Add dirty files")


# Moved to git_class module.
def process_untracked(gitrepo, gitcmd, **kwargs):

    """Function:  process_untracked

    Description:  Check for and process untracked files.

    Arguments:
        (input) gitrepo -> Git repo class instance.
        (input) gitcmd -> Git command line class instance.
        (input) **kwargs:
            None

    """

    if gitrepo.is_dirty(untracked_files=True):

        for f_git in gitrepo.untracked_files:

            # Check this code works.
            gitcmd.add(f_git)

        if gitrepo.untracked_files:

            # Can I stipulate what is in the comments dynamically?
            gitrepo.index.commit("Add untracked files")


def send_mail(cfg, subj, email_body, **kwargs):

    """Function:  send_mail

    Description:  Compiles and sends out an email notification message.

    Arguments:
        (input) cfg -> Configuration settings module for the program.
        (input) subj -> Email subject line.
        (input) email_body -> Email body list.
        (input) **kwargs:
            None

    """

    body = list(email_body)
    frm_line = getpass.getuser() + "@" + socket.gethostname()

    email = gen_class.Mail(cfg.to_line, subj, frm_line)

    for line in body:
        email.add_2_msg(line)

    email.send_mail()


def process_project(branch, gitcmd, log, **kwargs):

    """Function:  process_project

    Description:  Fetch, merge, and push the project to the
        remote Git repo.

    Arguments:
        (input) branch -> Branch being merge into.
        (input) gitcmd -> Git command line class instance.
        (input) log -> Log class instance.
        (input) **kwargs:
            None

    """

    log.log_info("Fetching and setting up branches.")
    gitcmd.fetch()
    gitcmd.branch("mod_release")
    gitcmd.checkout(branch)

    log.log_info("Merging new repo into branch: %s" % (branch))
    gitcmd.merge("--no-ff", "-s", "recursive", "-X", "theirs", "mod_release")

    log.log_info("Pushing local repo to remote repo.")

    # Push changes and then push tags.
    gitcmd.push()
    gitcmd.push("--tags")


def commits_diff(gitrepo, data_str, **kwargs):

    """Function:  commits_diff

    Description:  Compares a branch with another branch and returns a count
        on the number of commits difference between the two branches.
            0 -> Branch not ahead of other branch.
            >0 ->  Branch is ahead of other branch by N commits.

    Note:
        The data_str will contain the order of the branches being compared,
            whether local to remote or remote to local.
        The format of the data_str is:
            Local to Remote:
                "BRANCH_NAME..origin/BRANCH_NAME"
            Remote to Local:
                "origin/BRANCH_NAME..BRANCH_NAME"

    Arguments:
        (input) gitcmd -> Git command line class instance.
        (input) data_str -> Contains the order of branches to be compared.
        (input) **kwargs:
            None
        (output) -> N commits difference between branches.

    """

    return sum(1 for x in gitrepo.iter_commits(data_str))


def is_commits_behind(gitrepo, branch, **kwargs):

    """Function:  is_commits_behind

    Description:  Compares the local branch with the remote branch and returns
        a count on whether local branch is behind remote branch.
        Output:
            0 -> Local branch not behind remote branch.
            >0 ->  Local branch is behind remote branch by N commits.

    Arguments:
        (input) gitcmd -> Git command line class instance.
        (input) branch -> Branch being compares.
        (input) **kwargs:
            None
        (output) -> N commits local branch behind remote branch.

    """

    return commits_diff(gitrepo, branch + "..origin/" + branch)


def is_commits_ahead(gitrepo, branch, **kwargs):

    """Function:  is_commits_ahead

    Description:  Compares the local branch with the remote branch and returns
        a count on whether local branch is ahead of remote branch.
        Output:
            0 -> Local branch not ahead of remote branch.
            >0 ->  Local branch is ahead of remote branch by N commits.

    Arguments:
        (input) gitcmd -> Git command line class instance.
        (input) branch -> Branch being compares.
        (input) **kwargs:
            None
        (output) -> N commits local branch ahead of remote branch.

    """

    return commits_diff(gitrepo, "origin/" + branch + ".." + branch)


def merge(args_array, cfg, log, **kwargs):

    """Function:  merge

    Description:  Controls the merging of a local repository with a remote
        repository, but having the local repository as the priority
        repository.

    Arguments:
        (input) args_array -> Dict of command line options and values.
        (input) cfg -> Configuration settings module for the program.
        (input) log -> Log class instance.
        (input) **kwargs:
            None

    """

    log.log_info("Starting merge of:  %s" % (args_array["-r"]))

    gen_libs.mv_file2(args_array["-p"], cfg.work_dir)

    proj_dir = os.path.join(cfg.work_dir, os.path.basename(args_array["-p"]))

    # Is directory a git repo.
    if is_git_repo(proj_dir):

        log.log_info("Processing: %s directory" % (proj_dir))

        gitrepo = git.Repo(proj_dir)
        gitcmd = gitrepo.git

        # Set the url to the remote Git repo.
        # gitcmd.remote('set-url', 'origin',
        #               'git@gitlab.code.dicelab.net:JAC-IDM/test-merge.git')
        gitcmd.remote("set-url", "origin", cfg.url + args_array["-r"] + ".git")

        # Does remote git repo exist.
        if is_remote(gitcmd, cfg.url + args_array["-r"] + ".git"):

            log.log_info("Processing dirty files")
            process_dirty(gitrepo, gitcmd)

            log.log_info("Processing untracked files")
            process_untracked(gitrepo, gitcmd)

            process_project(cfg.branch, gitcmd, log)

            if is_commits_ahead(gitrepo, cfg.branch):

                log.log_err("Local branch: %s not in sync with remote repo" \
                            % (cfg.branch))

                gen_libs.mv_file2(proj_dir, cfg.err_dir)

                # Send notification of error.
                subj = "Merge error for: " + args_array["-r"]
                body = ["DTG: "
                        + datetime.datetime.strftime(datetime.datetime.now(),
                                                     "%Y-%m-%d %H:%M:%S")]
                body.append("Local branch: %s not in sync with remote repo." \
                            % (cfg.branch))
                body.append("Local branch is %s commits ahead of remote." \
                            % (is_commits_ahead(gitrepo, cfg.branch)))
                body.append("Remote URL: " + gitrepo.remotes.origin.url)
                body.append("Project Dir: " + proj_dir)
                body.append("Branch: " + cfg.branch)

                send_mail(cfg, subj, body)

            else:
                gen_libs.mv_file2(proj_dir, cfg.archive_dir)
                log.log_info("Processing of: %s complete." % (proj_dir))

                # Send notification of completion.
                subj = "Merge completed for: " + args_array["-r"]
                body = ["DTG: "
                        + datetime.datetime.strftime(datetime.datetime.now(),
                                                     "%Y-%m-%d %H:%M:%S")]
                body.append("Merge of project has been completed.")

                send_mail(cfg, subj, body)

        else:

            log.log_err("%s.%s does not exist at remote repo: %s" %
                        (proj_dir, cfg.branch, (gitrepo.remotes.origin.url)))

            gen_libs.mv_file2(proj_dir, cfg.err_dir)

            # Send notification of error.
            subj = "Merge error for: " + args_array["-r"]
            body = ["DTG: "
                    + datetime.datetime.strftime(datetime.datetime.now(),
                                                 "%Y-%m-%d %H:%M:%S")]
            body.append("Merge of project has failed.")
            body.append("Branch does not exist at remote Git.")
            body.append("Remote URL: " + gitrepo.remotes.origin.url)
            body.append("Project Dir: " + proj_dir)
            body.append("Branch: " + cfg.branch)

            send_mail(cfg, subj, body)

    else:

        log.log_err("%s is not a Git repository" % (proj_dir))

        gen_libs.mv_file2(proj_dir, cfg.err_dir)

        # Send notification of error.
        subj = "Merge error for: " + args_array["-r"]
        body = ["DTG: " +
                datetime.datetime.strftime(datetime.datetime.now(),
                                           "%Y-%m-%d %H:%M:%S")]
        body.append("Merge of project has failed.")
        body.append("Local Git repository does not exist.")
        body.append("Project Dir: " + proj_dir)

        send_mail(cfg, subj, body)


def run_program(args_array, func_dict, **kwargs):

    """Function:  run_program

    Description:  Controls the running of the program and sets up a logger
        class for the running instance of the program.

    Arguments:
        (input) args_array -> Dict of command line options and values.
        (input) func_dict -> Dict of function calls and associated options.
        (input) **kwargs:
            None

    """

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


def main():

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

    """

    dir_chk_list = ["-d", "-p"]
    func_dict = {"-M": merge}
    opt_req_list = ["-c", "-d", "-p", "-r"]
    opt_val_list = ["-c", "-d", "-p", "-r"]

    # Process argument list from command line.
    args_array = arg_parser.arg_parse2(sys.argv, opt_val_list)

    if not gen_libs.help_func(args_array, __version__, help_message) \
       and not arg_parser.arg_require(args_array, opt_req_list) \
       and not arg_parser.arg_dir_chk_crt(args_array, dir_chk_list):

        try:
            PROG_LOCK = gen_class.ProgramLock(sys.argv,
                                              args_array.get("-r", ""))

            run_program(args_array, func_dict)
            del PROG_LOCK

        except gen_class.SingleInstanceException:
            print("WARNING:  lock in place for merge with id of: %s"
                  % (args_array.get("-r", "")))


if __name__ == "__main__":
    sys.exit(main())
