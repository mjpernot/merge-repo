#!/usr/bin/python
# Classification (U)

"""Program:  load_cfg.py

    Description:  Unit testing of merge in load_cfg.py.

    Usage:
        test/unit/merge_repo/load_cfg.py

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


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Unit testing initilization.
        test_false_false_cfg -> Test False and False statuses.
        test_false_true_cfg -> Test False and True statuses.
        test_true_false_cfg -> Test True and False statuses.
        test_work_dir_true -> Test work_dir check returns True.

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
                self.log_file="/home/mark.j.pernot/merge/log_dir/merge_repo.log"
                self.to_line="Mark.J.Pernot@coe.ic.gov"
                self.branch="master"

        self.cfg = CfgTest()

        self.cfg_name = "Configuration_File"
        self.cfg_dir = "Configuration_Directory"

    @unittest.skip("Not done")
    @mock.patch("merge_repo.gen_libs")
    def test_false_false_cfg(self, mock_lib):

        """Function:  test_false_false_cfg

        Description:  Test False and False statuses.

        Arguments:
            mock_lib -> Mock Ref:  merge_repo.gen_libs

        """

        mock_lib.load_module.return_value = self.cfg
        mock_lib.chk_crt_dir.side_effect = [[False, ""], [False, ""]]

        self.assertEqual(merge_repo.load_cfg(self.cfg_name, self.cfg_dir),
                         (self.cfg, False))

    @unittest.skip("Not done")
    @mock.patch("merge_repo.gen_libs")
    def test_false_true_cfg(self, mock_lib):

        """Function:  test_false_true_cfg

        Description:  Test False and True statuses.

        Arguments:
            mock_lib -> Mock Ref:  merge_repo.gen_libs

        """

        mock_lib.load_module.return_value = self.cfg
        mock_lib.chk_crt_dir.side_effect = [[False, ""], [True, ""]]

        self.assertEqual(merge_repo.load_cfg(self.cfg_name, self.cfg_dir),
                         (self.cfg, False))

    @unittest.skip("Not done")
    @mock.patch("merge_repo.gen_libs")
    def test_true_false_cfg(self, mock_lib):

        """Function:  test_true_false_cfg

        Description:  Test True and False statuses.

        Arguments:
            mock_lib -> Mock Ref:  merge_repo.gen_libs

        """

        mock_lib.load_module.return_value = self.cfg
        mock_lib.chk_crt_dir.side_effect = [[True, ""], [False, ""]]

        self.assertEqual(merge_repo.load_cfg(self.cfg_name, self.cfg_dir),
                         (self.cfg, False))

    @mock.patch("merge_repo.gen_libs")
    def test_work_dir_false(self, mock_lib):

        """Function:  test_work_dir_false

        Description:  Test work_dir check returns False.

        Arguments:
            mock_lib -> Mock Ref:  merge_repo.gen_libs

        """

        mock_lib.load_module.return_value = self.cfg
        mock_lib.chk_crt_dir.side_effect = [[False, ""], [True, ""], [True, ""]]
        mock_lib.chk_crt_file.side_effect = [[True, ""]]

        self.assertEqual(merge_repo.load_cfg(self.cfg_name, self.cfg_dir),
                         (self.cfg, False))

    @mock.patch("merge_repo.gen_libs")
    def test_work_dir_true(self, mock_lib):

        """Function:  test_work_dir_true

        Description:  Test work_dir check returns True.

        Arguments:
            mock_lib -> Mock Ref:  merge_repo.gen_libs

        """

        mock_lib.load_module.return_value = self.cfg
        mock_lib.chk_crt_dir.side_effect = [[True, ""], [True, ""], [True, ""]]
        mock_lib.chk_crt_file.side_effect = [[True, ""]]

        self.assertEqual(merge_repo.load_cfg(self.cfg_name, self.cfg_dir),
                         (self.cfg, True))


if __name__ == "__main__":
    unittest.main()
