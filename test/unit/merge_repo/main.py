#!/usr/bin/python
# Classification (U)

"""Program:  main.py

    Description:  Unit testing of main in merge_repo.py.

    Usage:
        test/unit/merge_repo/main.py

    Arguments:
        None

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
import contextlib
import io

# Third-party
import mock

# Local
sys.path.append(os.getcwd())
import merge_repo
import lib.gen_libs as gen_libs
import version

# Version Information
__version__ = version.__version__


class ProgramLock(object):

    """Class:  ProgramLock

    Description:  Mock of the gen_class.ProgramLock class.

    Super-Class:  object

    Sub-Classes:

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

    def __del__(self):

        """Method:  __del__

        Description:  Deletion of the ProgramLock instance.

        Arguments:
            None

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

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

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        self.args = {"-c": "config_file", "-d": "config_dir",
                     "-r": "repo-name", "-p": "repo_path", "-M": True}
        self.func_dict = {"-M": merge_repo.merge}

    @mock.patch("merge_repo.gen_libs.help_func")
    @mock.patch("merge_repo.arg_parser")
    @mock.patch("merge_repo.gen_class.ProgramLock")
    def test_exception_handler(self, mock_lock, mock_arg, mock_help):

        """Function:  test_exception_handler

        Description:  Test with exception handler.

        Arguments:
            None

        """

        mock_lock.side_effect = merge_repo.gen_class.SingleInstanceException
        mock_arg.arg_parse2.return_value = self.args
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = False

        with gen_libs.no_std_out():
            self.assertFalse(merge_repo.main())

    @mock.patch("merge_repo.gen_libs.help_func")
    @mock.patch("merge_repo.arg_parser")
    def test_adding_r_option(self, mock_arg, mock_help):

        """Function:  test_adding_r_option

        Description:  Test adding -r option to args_array.

        Arguments:
            None

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_help.return_value = False
        mock_arg.arg_require.return_value = True

        self.args.pop("-r")

        self.assertFalse(merge_repo.main())

    @mock.patch("merge_repo.gen_libs.help_func")
    @mock.patch("merge_repo.arg_parser.arg_parse2")
    def test_help_true(self, mock_arg, mock_help):

        """Function:  test_status_true

        Description:  Test main function with Help_Func returns True.

        Arguments:
            None

        """

        mock_arg.return_value = self.args
        mock_help.return_value = True

        self.assertFalse(merge_repo.main())

    @mock.patch("merge_repo.gen_libs.help_func")
    @mock.patch("merge_repo.arg_parser")
    def test_help_false(self, mock_arg, mock_help):

        """Function:  test_status_false

        Description:  Test main function with Help_Func returns False.

        Arguments:
            None

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_help.return_value = False
        mock_arg.arg_require.return_value = True

        self.assertFalse(merge_repo.main())

    @mock.patch("merge_repo.gen_libs.help_func")
    @mock.patch("merge_repo.arg_parser")
    def test_arg_require_true(self, mock_arg, mock_help):

        """Function:  test_arg_require_true

        Description:  Test main function with arg_require returns True.

        Arguments:
            None

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_help.return_value = False
        mock_arg.arg_require.return_value = True

        self.assertFalse(merge_repo.main())

    @mock.patch("merge_repo.gen_libs.help_func")
    @mock.patch("merge_repo.arg_parser")
    def test_arg_require_false(self, mock_arg, mock_help):

        """Function:  test_arg_require_false

        Description:  Test main function with arg_require returns False.

        Arguments:
            None

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = True

        self.assertFalse(merge_repo.main())

    @mock.patch("merge_repo.gen_libs.help_func")
    @mock.patch("merge_repo.arg_parser")
    def test_arg_dir_chk_crt_true(self, mock_arg, mock_help):

        """Function:  test_arg_dir_chk_crt_true

        Description:  Test main function with arg_dir_chk_crt returns True.

        Arguments:
            None

        """

        mock_arg.arg_parse2.return_value = self.args
        mock_help.return_value = False
        mock_arg.arg_require.return_value = True
        mock_arg.arg_dir_chk_crt.return_value = True

        self.assertFalse(merge_repo.main())

    @mock.patch("merge_repo.run_program")
    @mock.patch("merge_repo.gen_libs.help_func")
    @mock.patch("merge_repo.arg_parser")
    @mock.patch("merge_repo.gen_class")
    def test_arg_dir_chk_crt_false(self, mock_class, mock_arg, mock_help,
                                   mock_run):

        """Function:  test_arg_dir_chk_crt_false

        Description:  Test main function with arg_dir_chk_crt returns False.

        Arguments:
            None

        """

        mock_class.ProgramLock.return_value = ProgramLock([], self.args["-r"])
        mock_arg.arg_parse2.return_value = self.args
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_run.return_value = True

        self.assertFalse(merge_repo.main())


if __name__ == "__main__":
    unittest.main()
