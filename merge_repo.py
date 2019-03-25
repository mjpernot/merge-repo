#!/usr/bin/python
# Classification (U)

"""Program:  merge_repo.py

    Description:

    Usage:

    Arguments:
        -c (config file)
        -d (config directory path)
        -M (Run merge_repo function)
        -r (project/repository name (e.g. "test-merge"))
        -p (project directory including full path)
        -e (Error directory path) # Use -e or cfg.err_dir?
        -v => Display version of this program.
        -h => Help and usage message.

        NOTE 1:  -v or -h overrides the other options.
    
    Notes:
        Config file:
            url="git@gitlab.code.dicelab.net:JAC-IDM/"
            work_dir="/home/mark.j.pernot/merge/work_dir"
            err_dir="/home/mark.j.pernot/merge/error_dir"
            archive_dir="/home/mark.j.pernot/merge/archive_dir"

    Examples:

"""

# Libraries and Global Variables

# Standard
# For Python 2.6/2.7: Redirection of stdout in a print command.
from __future__ import print_function
import sys
import os

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
        _ = git.Repo(path).git_dir
        return True

    except git.exc.InvalidGitRepositoryError:
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


def merge_repo(args_array, cfg, log, **kwargs):

    """Function:  merge_repo

    Description:  Controls the merging of a non-local repository with a remote
        repository, but having the non-local repository as the priority
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

    proj_dir = os.join.path(cfg.work_dir, os.path.basename(args_array["-p"]))

    # Is directory a git repo.
    if is_git_repo(proj_dir):

        log.log_info("Working in %s directory" % (proj_dir))

        gitrepo = git.Repo(proj_dir)
        gitcmd = gitrepo.git

        # Set the url to the remote Git repo.
        # Git remote set-url origin cfg.url + project_name + ".git"
        # gitcmd.remote('set-url', 'origin', 'git@gitlab.code.dicelab.net:JAC-IDM/test-merge.git')
        gitcmd.remote("set-url", "origin", cfg.url + args_array["-r"] + ".git")

        # Does branch resides in the remote git repo.
        # Make "master" a cfg or variable setting? Cfg as we can then merge another branch if so desired,
        #    but setting not recommended to be changed.
        if is_remote_branch(gitcmd, "master"):

            # Process any untracked files.
            process_untracked(gitrepo, gitcmd)
            
            # Process any dirty files.
            process_dirty(gitrepo, gitcmd)

            # Test this code, not been tested before.
            gitcmd.fetch()

            # Test this code, not been tested before.
            gitcmd.branch("mod_release")

            # Another one with branch name here.
            gitcmd.checkout("master")

            # Test this code, not been tested before.
            # Git merge --no-off -s recursive -X theirs mod_release
            # or gitcmd.merge("--no-off", "-s recursive", "-X theirs", "mod_release")
            gitcmd.merge("--no-off", "-s", "recursive", "-X", "theirs", "mod_release")

            # Test this code, not been tested before.
            gitcmd.push("--tags")

            gen_libs.mv_file2(proj_dir, cfg.archive_dir)

            # Send notification of completion.
            subj = "Merge completed for: " + args_array["-r"]
            body = ["DTG: " + datetime.datetime.strftime(datetime.datetime.now(),
                                                        "%Y-%m-%d %H:%M:%S")]
            body.append("Merge of project has been completed.")

            send_mail(cfg, subj, body)

        else:

            log.log_err("%s.%s does not exist at remote repo: %s" % \
                        (proj_dir, "master", (gitrepo.remotes.origin.url))

            gen_libs.mv_file2(proj_dir, cfg.err_dir)

            # Send notification of error.
            subj = "Merge error for: " + args_array["-r"]
            body = ["DTG: " + datetime.datetime.strftime(datetime.datetime.now(),
                                                        "%Y-%m-%d %H:%M:%S")]
            body.append("Merge of project has failed.")
            body.append("Branch does not exist at remote Git.")
            body.append("Remote URL: " + gitrepo.remotes.origin.url)
            body.append("Project Dir: " + proj_dir)
            body.append("Branch: " + "master")

            send_mail(cfg, subj, body)

    else:

        log.log_err("%s is not a Git repository" % (proj_dir))

        gen_libs.mv_file2(proj_dir, cfg.err_dir)

        # Send notification of error.
        subj = "Merge error for: " + args_array["-r"]
        body = ["DTG: " + datetime.datetime.strftime(datetime.datetime.now(),
                                                    "%Y-%m-%d %H:%M:%S")]
        body.append("Merge of project has failed.")
        body.append("Local Git repository does not exist.")
        body.append("Project Dir: " + proj_dir)

        send_mail(cfg, subj, body)


def run_program(args_array, cfg, log, **kwargs):

    """Function:  run_program

    Description:  Controls the running of the program and sets up a logger
        class for the running instance of the program.

    Arguments:
        (input) args_array -> Dict of command line options and values.
        (input) cfg -> Configuration settings module for the program.
        (input) log -> Log class instance.
        (input) **kwargs:
            None

    """

    cfg, status_flag = load_cfg(args_array["-c"], args_array["-d"])

    if not status_flag:
        print("Error:  Problem in configuration file.")

    else:
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
    func_dict = {"-M": merge_repo]
    opt_req_list = ["-c", "-d", "-r"]
    opt_val_list = ["-c", "-d", "-p", "-r"]

    # Process argument list from command line.
    args_array = arg_parser.arg_parse2(sys.argv, opt_val_list,
                                       multi_val=opt_multi_list)

    if not gen_libs.help_func(args_array, __version__, help_message) \
       and not arg_parser.arg_require(args_array, opt_req_list) \
       and not arg_parser.arg_dir_chk_crt(args_array, dir_chk_list):

        try:
            PROG_LOCK = gen_class.ProgramLock(sys.argv,
                                              args_array.get("-r", ""))

            run_program(args_array)
            del PROG_LOCK

        except gen_class.SingleInstanceException:
            print("WARNING:  lock in place for merge_repo with id of: %s"
                  % (args_array.get("-r", "")))


if __name__ == "__main__":
    sys.exit(main())
