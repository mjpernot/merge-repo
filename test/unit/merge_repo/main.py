#!/usr/bin/python
# Classification (U)

"""Program:  main.py

    Description:  Unit testing of main in merge_repo.py.

    Usage:
        test/unit/merge_repo/main.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Third-party
import mock

# Local
sys.path.append(os.getcwd())
import merge_repo
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


def get_inst(cmd):

    """Function:  get_inst

    Description:  Returns the module instance header.

    Arguments:
        (input) cmd -> Module library.
        (output) cmd -> Return module instance.

    """

    return cmd


class ProgramLock(object):

    """Class:  ProgramLock

    Description:  Mock of the gen_class.ProgramLock class.

    Methods:
        __init__ -> Class instance initilization.
        __del__ -> Deletion of the ProgramLock instance.

    """

    def __init__(self, argv, flavor_id=""):

        """Method:  __init__

        Description:  Initialization of an instance of the ProgramLock class.

        Arguments:
            (input) argv -> Arguments from the command line.
            (input) flavor_id -> Unique identifier for an instance.

        """

        self.lock_created = True
        self.argv = argv
        self.flavor_id = flavor_id

    def __del__(self):

        """Method:  __del__

        Description:  Deletion of the ProgramLock instance.

        Arguments:

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_exception_handler -> Test with exception handler.
        test_adding_r_option -> Test adding -r option to args_array.
        test_help_true -> Test with Help_Func returns True.
        test_help_false -> Test with Help_Func returns False.
        test_arg_require_true -> Test with arg_require returns True.
        test_arg_require_false -> Test with arg_require returns False.
        test_arg_dir_chk_crt_true -> Test with arg_dir_chk_crt returns True.
        test_arg_dir_chk_crt_false -> Test with arg_dir_chk_crt returns False.
        test_run_program -> Test with run_program.
        test_programlock_true -> Test with ProgramLock returns True.
        test_programlock_false -> Test with ProgramLock returns False.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args = {"-c": "config_file", "-d": "config_dir",
                     "-r": "repo-name", "-p": "repo_path", "-M": True}
        self.func_dict = {"-M": merge_repo.merge}
        self.proglock = ProgramLock(["cmdline"], self.args["-r"])

    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.arg_parser")
    @mock.patch("merge_repo.gen_class.ProgramLock")
    def test_exception_handler(self, mock_lock, mock_arg, mock_lib):

        """Function:  test_exception_handler

        Description:  Test with exception handler.

        Arguments:

        """

        mock_lock.side_effect = merge_repo.gen_class.SingleInstanceException
        mock_arg.arg_parse2.return_value = self.args
        mock_lib.help_func.return_value = False
        mock_lib.get_inst.return_value = get_inst(sys)
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = False

        with gen_libs.no_std_out():
            self.assertFalse(merge_repo.main())

    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.arg_parser")
    def test_adding_r_option(self, mock_arg, mock_lib):

        """Function:  test_adding_r_option

        Description:  Test adding -r option to args_array.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_lib.help_func.return_value = False
        mock_lib.get_inst.return_value = get_inst(sys)
        mock_arg.arg_require.return_value = True

        self.args.pop("-r")

        self.assertFalse(merge_repo.main())

    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.arg_parser.arg_parse2")
    def test_help_true(self, mock_arg, mock_lib):

        """Function:  test_help_true

        Description:  Test main function with Help_Func returns True.

        Arguments:

        """

        mock_arg.return_value = self.args
        mock_lib.help_func.return_value = True
        mock_lib.get_inst.return_value = get_inst(sys)

        self.assertFalse(merge_repo.main())

    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.arg_parser")
    def test_help_false(self, mock_arg, mock_lib):

        """Function:  test_help_false

        Description:  Test main function with Help_Func returns False.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_lib.help_func.return_value = False
        mock_lib.get_inst.return_value = get_inst(sys)
        mock_arg.arg_require.return_value = True

        self.assertFalse(merge_repo.main())

    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.arg_parser")
    def test_arg_require_true(self, mock_arg, mock_lib):

        """Function:  test_arg_require_true

        Description:  Test main function with arg_require returns True.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_lib.help_func.return_value = False
        mock_lib.get_inst.return_value = get_inst(sys)
        mock_arg.arg_require.return_value = True

        self.assertFalse(merge_repo.main())

    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.arg_parser")
    def test_arg_require_false(self, mock_arg, mock_lib):

        """Function:  test_arg_require_false

        Description:  Test main function with arg_require returns False.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_lib.help_func.return_value = False
        mock_lib.get_inst.return_value = get_inst(sys)
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = True

        self.assertFalse(merge_repo.main())

    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.arg_parser")
    def test_arg_dir_chk_crt_true(self, mock_arg, mock_lib):

        """Function:  test_arg_dir_chk_crt_true

        Description:  Test main function with arg_dir_chk_crt returns True.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_lib.help_func.return_value = False
        mock_lib.get_inst.return_value = get_inst(sys)
        mock_arg.arg_require.return_value = True
        mock_arg.arg_dir_chk_crt.return_value = True

        self.assertFalse(merge_repo.main())

    @mock.patch("merge_repo.run_program")
    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.arg_parser")
    @mock.patch("merge_repo.gen_class")
    def test_arg_dir_chk_crt_false(self, mock_class, mock_arg, mock_lib,
                                   mock_run):

        """Function:  test_arg_dir_chk_crt_false

        Description:  Test main function with arg_dir_chk_crt returns False.

        Arguments:

        """

        mock_class.ProgramLock.return_value = self.proglock
        mock_arg.arg_parse2.return_value = self.args
        mock_lib.help_func.return_value = False
        mock_lib.get_inst.return_value = get_inst(sys)
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_run.return_value = True

        self.assertFalse(merge_repo.main())

    @mock.patch("merge_repo.run_program")
    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.arg_parser")
    @mock.patch("merge_repo.gen_class")
    def test_run_program(self, mock_class, mock_arg, mock_lib, mock_run):

        """Function:  test_run_program

        Description:  Test with run_program.

        Arguments:

        """

        mock_class.ProgramLock.return_value = self.proglock
        mock_arg.arg_parse2.return_value = self.args
        mock_lib.help_func.return_value = False
        mock_lib.get_inst.return_value = get_inst(sys)
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_run.return_value = True

        self.assertFalse(merge_repo.main())

    @mock.patch("merge_repo.run_program")
    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.arg_parser")
    @mock.patch("merge_repo.gen_class")
    def test_programlock_true(self, mock_class, mock_arg, mock_lib, mock_run):

        """Function:  test_programlock_true

        Description:  Test with ProgramLock returns True.

        Arguments:

        """

        mock_class.ProgramLock.return_value = self.proglock
        mock_arg.arg_parse2.return_value = self.args
        mock_lib.help_func.return_value = False
        mock_lib.get_inst.return_value = get_inst(sys)
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_run.return_value = True

        self.assertFalse(merge_repo.main())

    @mock.patch("merge_repo.run_program")
    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.arg_parser")
    @mock.patch("merge_repo.gen_class.ProgramLock")
    def test_programlock_false(self, mock_lock, mock_arg, mock_lib, mock_run):

        """Function:  test_programlock_false

        Description:  Test with ProgramLock returns False.

        Arguments:

        """

        mock_lock.side_effect = \
            merge_repo.gen_class.SingleInstanceException
        mock_arg.arg_parse2.return_value = self.args
        mock_lib.help_func.return_value = False
        mock_lib.get_inst.return_value = get_inst(sys)
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_run.return_value = True

        with gen_libs.no_std_out():
            self.assertFalse(merge_repo.main())

    @mock.patch("merge_repo.run_program")
    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.arg_parser")
    @mock.patch("merge_repo.gen_class")
    def test_programlock_id(self, mock_class, mock_arg, mock_lib, mock_run):

        """Function:  test_programlock_id

        Description:  Test with ProgramLock with flavor id.

        Arguments:

        """

        mock_class.ProgramLock.return_value = self.proglock
        mock_arg.arg_parse2.return_value = self.args
        mock_lib.help_func.return_value = False
        mock_lib.get_inst.return_value = get_inst(sys)
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_run.return_value = True

        self.assertFalse(merge_repo.main())


if __name__ == "__main__":
    unittest.main()
