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


def process_message(cfg, log, **kwargs):

    """Function:  process_message

    Description:  This is a function stub for merge_repo.process_message.

    Arguments:
        cfg -> Stub argument holder.
        log -> Stub argument holder.

    """

    pass


def check_nonprocess(cfg, log, **kwargs):

    """Function:  check_nonprocess

    Description:  This is a function stub for merge_repo.check_nonprocess.

    Arguments:
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
        test_all_func -> Test with all functions.
        test_true_func -> Test with true status and function.
        test_true_status -> Test with true status flag.
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

                self.log_file = "LOG_FILE"
                self.host = "HOSTNAME"
                self.exchange_name = "EXCHANGE_NAME"
                self.exchange_type = "EXCAHNGE_TYPE"
                self.valid_queues = ["QUEUE1", "QUEUE2"]
                self.email_dir = "EMAIL_DIRECTORY"

        self.cfg = CfgTest()

        self.args_array = {"-c": "CONFIG_FILE", "-d": "CONFIG_DIRECTORY"}
        self.func_dict = {"-M": process_message, "-C": check_nonprocess}

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

    @mock.patch("merge_repo.gen_class")
    @mock.patch("merge_repo.load_cfg")
    def test_true_status(self, mock_cfg, mock_class):

        """Function:  test_true_status

        Description:  Test with true status flag.

        Arguments:
            mock_cfg -> Mock Ref:  merge_repo.load_cfg
            mock_class -> Mock Ref:  merge_repo.gen_class

        """

        mock_cfg.return_value = (self.cfg, True)
        mock_class.Logger.return_value = merge_repo.gen_class.Logger

        self.assertFalse(merge_repo.run_program(self.args_array,
                                                self.func_dict))

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
