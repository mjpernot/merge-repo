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
import mock

# Local
sys.path.append(os.getcwd())
import merge_repo                               # pylint:disable=E0401,C0413
import lib.gen_libs as gen_libs             # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class ArgParser(object):                                # pylint:disable=R0205

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        arg_dir_chk
        arg_exist
        arg_require
        get_val
        insert_arg
        arg_parse2

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.cmdline = None
        self.args_array = {}
        self.opt_req = None
        self.opt_req2 = True
        self.dir_perms_chk = None
        self.dir_perms_chk2 = True
        self.argparse2 = True

    def arg_dir_chk(self, dir_perms_chk):

        """Method:  arg_dir_chk

        Description:  Method stub holder for gen_class.ArgParser.arg_dir_chk.

        Arguments:

        """

        self.dir_perms_chk = dir_perms_chk

        return self.dir_perms_chk2

    def arg_exist(self, arg):

        """Method:  arg_exist

        Description:  Method stub holder for gen_class.ArgParser.arg_exist.

        Arguments:

        """

        return arg in self.args_array

    def arg_require(self, opt_req):

        """Method:  arg_require

        Description:  Method stub holder for gen_class.ArgParser.arg_require.

        Arguments:

        """

        self.opt_req = opt_req

        return self.opt_req2

    def get_val(self, skey, def_val=None):

        """Method:  get_val

        Description:  Method stub holder for gen_class.ArgParser.get_val.

        Arguments:

        """

        return self.args_array.get(skey, def_val)

    def insert_arg(self, arg_key, arg_val):

        """Method:  insert_arg

        Description:  Method stub holder for gen_class.ArgParser.insert_arg.

        Arguments:

        """

        self.args_array[arg_key] = arg_val

    def arg_parse2(self):

        """Method:  arg_parse2

        Description:  Method stub holder for gen_class.ArgParser.arg_parse2.

        Arguments:

        """

        return self.argparse2


class ProgramLock(object):                      # pylint:disable=R0903,R0205

    """Class:  ProgramLock

    Description:  Mock of the gen_class.ProgramLock class.

    Methods:
        __init__
        __del__

    """

    def __init__(self, argv, flavor_id=""):

        """Method:  __init__

        Description:  Initialization of an instance of the ProgramLock class.

        Arguments:

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
        setUp
        test_arg_parse2_false
        test_arg_parse2_true
        test_exception_handler
        test_adding_r_option
        test_help_true
        test_help_false
        test_arg_require_false
        test_arg_require_true
        test_arg_dir_chk_crt_false
        test_arg_dir_chk_crt_true
        test_run_program
        test_programlock_true
        test_programlock_false

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args = ArgParser()
        self.args.args_array = {
            "-c": "config_file", "-d": "config_dir", "-r": "repo-name",
            "-p": "repo_path", "-M": True}
        self.proglock = ProgramLock(["cmdline"], self.args.get_val("-r"))

    @mock.patch("merge_repo.gen_class.ArgParser")
    def test_arg_parse2_false(self, mock_arg):

        """Function:  test_arg_parse2_false

        Description:  Test arg_parse2 returns false.

        Arguments:

        """

        self.args.argparse2 = False

        mock_arg.return_value = self.args

        self.assertFalse(merge_repo.main())

    @mock.patch("merge_repo.gen_libs.help_func")
    @mock.patch("merge_repo.gen_class.ArgParser")
    def test_arg_parse2_true(self, mock_arg, mock_help):

        """Function:  test_arg_parse2_true

        Description:  Test arg_parse2 returns true.

        Arguments:

        """

        mock_arg.return_value = self.args
        mock_help.return_value = True

        self.assertFalse(merge_repo.main())

    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.gen_class.ArgParser")
    @mock.patch("merge_repo.gen_class.ProgramLock")
    def test_exception_handler(self, mock_lock, mock_arg, mock_lib):

        """Function:  test_exception_handler

        Description:  Test with exception handler.

        Arguments:

        """

        mock_lock.side_effect = merge_repo.gen_class.SingleInstanceException
        mock_arg.return_value = self.args
        mock_lib.help_func.return_value = False

        with gen_libs.no_std_out():
            self.assertFalse(merge_repo.main())

    @mock.patch("merge_repo.run_program", mock.Mock(return_value=True))
    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.gen_class.ArgParser")
    def test_adding_r_option(self, mock_arg, mock_lib):

        """Function:  test_adding_r_option

        Description:  Test adding -r option to args_array.

        Arguments:

        """

        mock_arg.return_value = self.args
        mock_lib.help_func.return_value = False
        mock_arg.arg_require.return_value = True

        self.args.args_array.pop("-r")

        self.assertFalse(merge_repo.main())

    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.gen_class.ArgParser")
    def test_help_true(self, mock_arg, mock_lib):

        """Function:  test_help_true

        Description:  Test main function with Help_Func returns True.

        Arguments:

        """

        mock_arg.return_value = self.args
        mock_lib.help_func.return_value = True

        self.assertFalse(merge_repo.main())

    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.gen_class.ArgParser")
    def test_help_false(self, mock_arg, mock_lib):

        """Function:  test_help_false

        Description:  Test main function with Help_Func returns False.

        Arguments:

        """

        self.args.opt_req2 = False

        mock_arg.return_value = self.args
        mock_lib.help_func.return_value = False

        self.assertFalse(merge_repo.main())

    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.gen_class.ArgParser")
    def test_arg_require_false(self, mock_arg, mock_lib):

        """Function:  test_arg_require_false

        Description:  Test main function with arg_require returns False.

        Arguments:

        """

        self.args.opt_req2 = False

        mock_arg.return_value = self.args
        mock_lib.help_func.return_value = False

        self.assertFalse(merge_repo.main())

    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.gen_class.ArgParser")
    def test_arg_require_true(self, mock_arg, mock_lib):

        """Function:  test_arg_require_true

        Description:  Test main function with arg_require returns True.

        Arguments:

        """

        self.args.dir_perms_chk2 = False

        mock_arg.return_value = self.args
        mock_lib.help_func.return_value = False

        self.assertFalse(merge_repo.main())

    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.gen_class.ArgParser")
    def test_arg_dir_chk_crt_false(self, mock_arg, mock_lib):

        """Function:  test_arg_dir_chk_crt_false

        Description:  Test main function with arg_dir_chk_crt returns False.

        Arguments:

        """

        self.args.dir_perms_chk2 = False

        mock_arg.return_value = self.args
        mock_lib.help_func.return_value = False

        self.assertFalse(merge_repo.main())

    @mock.patch("merge_repo.run_program", mock.Mock(return_value=True))
    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.gen_class.ArgParser")
    @mock.patch("merge_repo.gen_class.ProgramLock")
    def test_arg_dir_chk_crt_true(self, mock_class, mock_arg, mock_lib):

        """Function:  test_arg_dir_chk_crt_true

        Description:  Test main function with arg_dir_chk_crt returns True.

        Arguments:

        """

        mock_class.return_value = self.proglock
        mock_arg.return_value = self.args
        mock_lib.help_func.return_value = False

        self.assertFalse(merge_repo.main())

    @mock.patch("merge_repo.run_program", mock.Mock(return_value=True))
    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.gen_class.ArgParser")
    @mock.patch("merge_repo.gen_class.ProgramLock")
    def test_run_program(self, mock_class, mock_arg, mock_lib):

        """Function:  test_run_program

        Description:  Test with run_program.

        Arguments:

        """

        mock_class.return_value = self.proglock
        mock_arg.return_value = self.args
        mock_lib.help_func.return_value = False

        self.assertFalse(merge_repo.main())

    @mock.patch("merge_repo.run_program", mock.Mock(return_value=True))
    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.gen_class.ArgParser")
    @mock.patch("merge_repo.gen_class.ProgramLock")
    def test_programlock_true(self, mock_class, mock_arg, mock_lib):

        """Function:  test_programlock_true

        Description:  Test with ProgramLock returns True.

        Arguments:

        """

        mock_class.return_value = self.proglock
        mock_arg.return_value = self.args
        mock_lib.help_func.return_value = False

        self.assertFalse(merge_repo.main())

    @mock.patch("merge_repo.run_program", mock.Mock(return_value=True))
    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.gen_class.ArgParser")
    @mock.patch("merge_repo.gen_class.ProgramLock")
    def test_programlock_false(self, mock_lock, mock_arg, mock_lib):

        """Function:  test_programlock_false

        Description:  Test with ProgramLock returns False.

        Arguments:

        """

        mock_lock.side_effect = \
            merge_repo.gen_class.SingleInstanceException
        mock_arg.return_value = self.args
        mock_lib.help_func.return_value = False

        with gen_libs.no_std_out():
            self.assertFalse(merge_repo.main())

    @mock.patch("merge_repo.run_program", mock.Mock(return_value=True))
    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.gen_class.ArgParser")
    @mock.patch("merge_repo.gen_class.ProgramLock")
    def test_programlock_id(self, mock_class, mock_arg, mock_lib):

        """Function:  test_programlock_id

        Description:  Test with ProgramLock with flavor id.

        Arguments:

        """

        mock_class.return_value = self.proglock
        mock_arg.return_value = self.args
        mock_lib.help_func.return_value = False

        self.assertFalse(merge_repo.main())


if __name__ == "__main__":
    unittest.main()
