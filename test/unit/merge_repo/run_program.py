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


def merge(args_array, cfg, log):

    """Function:  merge_repo

    Description:  This is a function stub for merge_repo.merge_repo.

    Arguments:

    """

    status = True

    if args_array and cfg and log:
        status = True

    return status


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

        self.cfg = CfgTest()
        self.args = {"-c": "config_file", "-d": "config_dir",
                     "-r": "repo-name", "-p": "repo_path", "-M": True}
        self.args2 = {"-c": "config_file", "-d": "config_dir", "-n": True,
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
