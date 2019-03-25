#!/usr/bin/python
# Classification (U)

"""Program:  run_program.py

    Description:  Unit testing of run_program in merge_repo.py.

    Usage:
        test/unit/merge_repo/run_program.py

    Arguments:
        None

"""

# Libraries and Global Variables

# Standard
import sys
import os

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party
import mock

# Local
sys.path.append(os.getcwd())
import merge_repo
import lib.gen_libs as gen_libs
import version

# Version
__version__ = version.__version__


def merge_repo(args_array, cfg, log, **kwargs):

    """Function:  merge_repo

    Description:  This is a function stub for maimerge_repol_2_rmq.merge_repo.

    Arguments:
        args_array -> Stub argument holder.
        cfg -> Stub argument holder.
        log -> Stub argument holder.

    """

    pass


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Unit testing initilization.
        test_status_flag_true -> Test with true status flag.

        test_all_func -> Test with all functions.
        test_true_func -> Test with true status and function.
        test_false_status -> Test with false status flag.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        class CfgTest(object):

            """Class:  CfgTest

            Description:  Class which is a representation of a cfg module.

            Super-Class:  object

            Sub-Classes:  None

            Methods:
                __init__ -> Initialize configuration environment.

            """

            def __init__(self):

                """Method:  __init__

                Description:  Initialization instance of the CfgTest class.

                Arguments:
                        None

                """

                self.url="git@gitlab.code.dicelab.net:JAC-IDM/"
                self.work_dir="/home/mark.j.pernot/merge/work_dir"
                self.err_dir="/home/mark.j.pernot/merge/error_dir"
                self.archive_dir="/home/mark.j.pernot/merge/archive_dir"
                self.to_line="Mark.J.Pernot@coe.ic.gov"
                self.branch="master"

        self.cfg = CfgTest()

        self.args = {"-c": "config_file", "-d": "config_dir", "-r": "repo-name",
                     "-p": "repo_path", "-M": True}
        self.func_dict = {"-M": merge_repo}

    @mock.patch("merge_repo.gen_class.Logger")
    @mock.patch("merge_repo.load_cfg")
    def test_status_flag_true(self, mock_cfg, mock_log):

        """Function:  test_status_flag_true

        Description:  Test with true status flag.

        Arguments:
            mock_cfg -> Mock Ref:  merge_repo.load_cfg
            mock_log -> Mock Ref:  merge_repo.gen_class.Logger

        """

        mock_cfg.return_value = (self.cfg, True)
        mock_log.return_value = True

        self.assertFalse(merge_repo.run_program(self.args_array,
                                                mock_log,
                                                self.func_dict))


    @unittest.skip("not done yet")
    @mock.patch("merge_repo.gen_class")
    @mock.patch("merge_repo.load_cfg")
    def test_all_func(self, mock_cfg, mock_class):

        """Function:  test_all_func

        Description:  Test with all functions.

        Arguments:
            mock_cfg -> Mock Ref:  merge_repo.load_cfg
            mock_class -> Mock Ref:  merge_repo.gen_class

        """

        mock_cfg.return_value = (self.cfg, True)
        mock_class.Logger.return_value = merge_repo.gen_class.Logger
        mock_class.ProgramLock.return_value = merge_repo.gen_class.ProgramLock

        self.args_array["-M"] = True
        self.args_array["-C"] = True
        self.assertFalse(merge_repo.run_program(self.args_array,
                                                self.func_dict))

    @unittest.skip("not done yet")
    @mock.patch("merge_repo.gen_class")
    @mock.patch("merge_repo.load_cfg")
    def test_true_func(self, mock_cfg, mock_class):

        """Function:  test_true_func

        Description:  Test with true status and function.

        Arguments:
            mock_cfg -> Mock Ref:  merge_repo.load_cfg
            mock_class -> Mock Ref:  merge_repo.gen_class

        """

        mock_cfg.return_value = (self.cfg, True)
        mock_class.Logger.return_value = merge_repo.gen_class.Logger
        mock_class.ProgramLock.return_value = merge_repo.gen_class.ProgramLock

        self.args_array["-M"] = True
        self.assertFalse(merge_repo.run_program(self.args_array,
                                                self.func_dict))

    @unittest.skip("not done yet")
    @mock.patch("merge_repo.load_cfg")
    def test_false_status(self, mock_cfg):

        """Function:  test_false_status

        Description:  Test with false status flag.

        Arguments:
            mock_cfg -> Mock Ref:  merge_repo.load_cfg

        """

        mock_cfg.return_value = (self.cfg, False)

        with gen_libs.no_std_out():
            self.assertFalse(merge_repo.run_program(self.args_array,
                                                    self.func_dict))


if __name__ == "__main__":
    unittest.main()
