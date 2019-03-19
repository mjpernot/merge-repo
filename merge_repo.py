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


def merge_repo(args_array, **kwargs):

    """Function:  merge_repo

    Description:

    Arguments:
        (input) args_array -> Array of command line options and values.
        (input) **kwargs:
            None

    """

    return NNNN


def run_program(args_array, **kwargs):

    """Function:  run_program

    Description:  Controls the running of the program.

    Arguments:
        (input) args_array -> Dict of command line options and values.
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

            func_dict[opt](cfg, log, **kwargs)

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
