#!/usr/bin/python
# Classification (U)

"""Program:  merge_repo.py

    Description:

    Usage:

    Arguments:
        -v => Display version of this program.
        -h => Help and usage message.

        NOTE 1:  -v or -h overrides the other options.

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

    gen_libs.mv_file2(args_array["-p"], cfg.work_dir)

    proj_dir = os.join.path(cfg.work_dir, os.path.basename(args_array["-p"]))

    # Does current directory setup as a local git repo.
    if is_git_repo(proj_dir):

        log.log_info("Working in %s directory" % (proj_dir))

        gitrepo = git.Repo(proj_dir)
        gitcmd = gitrepo.git

        # Set the url to the remote Git repo.
        # Git remote set-url origin cfg.url + project_name + ".git"
        # gitcmd.remote('set-url', 'origin', 'git@gitlab.code.dicelab.net:JAC-IDM/test-merge.git')
        gitcmd.remote("set-url", "origin", cfg.url + args_array["-r"] + ".git")

        # Does branch resides in the remote git repo.
        # Make "master" a cfg or variable setting? Cfg as we can then merge another branch if so desired, but not recommended to be changed.
        if is_remote_branch(gitcmd, "master"):

            # Process the untracked files.
            # ### Start function 1 process_untracked
            if gitrepo.is_dirty(untracked_files=True):

                for f_git in gitrepo.untracked_files:

                    # Check this code works.
                    gitcmd.add(f_git)
                
                # Can I stipulate what is in the comments dynamically?
                gitrepo.index.commit("Add untracked files")
            # ### End function 1 process_untracked
            
            # Process the dirty files.
            # ### Start function 2 process_dirty
            if gitrepo.is_dirty():

                for f_git in gitrepo.index.diff(None):

                    if f_git.change_type == "D":

                        # Need to test this code first.
                        gitcmd.rm(f_git)
                    
                    elif f_git.change_type == "M":

                        # Check this code works.
                        gitcmd.add(f_git)

                # Can I stipulate what is in the comments dynamically?
                gitrepo.index.commit("Add untracked files")
            # ### End function 2 process_dirty

            # STOPPED HERE

#           # Continue to process.

        else:

            log.log_err("ERROR:  %s.%s does not exist at remote Git repo" % \
                        (proj_dir, "master"))
            log.log_info("Remote git repo: %s" % (gitrepo.remotes.origin.url))

#           # Send notification of error.
#           # Clean up or archive directory.

    else:

        log.log_err("ERROR:  %s is not a Git repository" % ())

#       # Send notification of error.
#       # Clean up or archive directory.


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
