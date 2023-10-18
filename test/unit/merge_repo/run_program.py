# Classification (U)

"""Program:  run_program.py

    Description:  Unit testing of run_program in merge_repo.py.

    Usage:
        test/unit/merge_repo/run_program.py

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
import merge_repo
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


def merge(args, cfg, log):

    """Function:  merge_repo

    Description:  This is a function stub for merge_repo.merge_repo.

    Arguments:

    """

    status = True

    if args and cfg and log:
        status = True

    return status


class ArgParser(object):

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        arg_exist
        get_args_keys
        get_val

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.cmdline = None
        self.args_array = dict()

    def arg_exist(self, arg):

        """Method:  arg_exist

        Description:  Method stub holder for gen_class.ArgParser.arg_exist.

        Arguments:

        """

        return True if arg in self.args_array else False

    def get_args_keys(self):

        """Method:  get_args_keys

        Description:  Method stub holder for gen_class.ArgParser.get_args_keys.

        Arguments:

        """

        return list(self.args_array.keys())

    def get_val(self, skey, def_val=None):

        """Method:  get_val

        Description:  Method stub holder for gen_class.ArgParser.get_val.

        Arguments:

        """

        return self.args_array.get(skey, def_val)


class CfgTest(object):

    """Class:  CfgTest

    Description:  Class which is a representation of a cfg module.

    Methods:
        __init__

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the CfgTest class.

        Arguments:

        """

        self.url = "git@github.com:JAC-IDM/"
        self.work_dir = "/data/merge-repo/work_dir"
        self.err_dir = "/data/merge-repo/error_dir"
        self.archive_dir = "/data/merge-repo/archive_dir"
        self.log_file = "/data/merge-repo/log_dir/merge_repo.log"
        self.to_line = "myemail@mydomain"
        self.branch = "master"


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_no_email_option
        test_status_flag_true
        test_status_flag_false

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.cfg = CfgTest()
        self.args = ArgParser()
        self.args2 = ArgParser()
        self.args.args_array = {
            "-c": "config_file", "-d": "config_dir", "-r": "repo-name",
            "-p": "repo_path", "-M": True}
        self.args2.args_array = {
            "-c": "config_file", "-d": "config_dir", "-n": True,
            "-r": "repo-name", "-p": "repo_path", "-M": True}
        self.func_names = {"-M": merge}
        self.msg_list = ["Error_Message"]

    @mock.patch("merge_repo.gen_class.Logger")
    @mock.patch("merge_repo.load_cfg")
    def test_no_email_option(self, mock_cfg, mock_log):

        """Function:  test_no_email_option

        Description:  Test with -n option selected.

        Arguments:

        """

        mock_cfg.return_value = (self.cfg, True, [])
        mock_log.return_value = merge_repo.gen_class.Logger
        mock_log.log_info.return_value = True
        mock_log.log_close.return_value = True

        self.assertFalse(merge_repo.run_program(self.args2, self.func_names))

    @mock.patch("merge_repo.gen_class.Logger")
    @mock.patch("merge_repo.load_cfg")
    def test_status_flag_true(self, mock_cfg, mock_log):

        """Function:  test_status_flag_true

        Description:  Test with status flag set to True.

        Arguments:

        """

        mock_cfg.return_value = (self.cfg, True, [])
        mock_log.return_value = merge_repo.gen_class.Logger
        mock_log.log_info.return_value = True
        mock_log.log_close.return_value = True

        self.assertFalse(merge_repo.run_program(self.args, self.func_names))

    @mock.patch("merge_repo.load_cfg")
    def test_status_flag_false(self, mock_cfg):

        """Function:  test_status_flag_false

        Description:  Test with status flag set to False.

        Arguments:

        """

        mock_cfg.return_value = (self.cfg, False, self.msg_list)

        with gen_libs.no_std_out():
            self.assertFalse(
                merge_repo.run_program(self.args, self.func_names))


if __name__ == "__main__":
    unittest.main()
