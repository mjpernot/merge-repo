# Classification (U)

"""Program:  load_cfg.py

    Description:  Unit testing of merge in load_cfg.py.

    Usage:
        test/unit/merge_repo/load_cfg.py

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
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class CfgTest(object):                          # pylint:disable=R0903,R0205

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
        test_multiple_errors
        test_log_file_false
        test_log_file_true
        test_archive_dir_false
        test_archive_dir_true
        test_err_dir_false
        test_err_dir_true
        test_work_dir_false
        test_work_dir_true

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.cfg = CfgTest()
        self.cfg_name = "Configuration_File"
        self.cfg_dir = "Configuration_Directory"
        self.err_msg = "Work Directory Failure"
        self.err_msg2 = "Error Directory Failure"
        self.err_msg3 = "Archive Directory Failure"
        self.err_msg4 = "Log File Failure"
        self.true = (True, None)

    @mock.patch("merge_repo.gen_libs")
    def test_multiple_errors(self, mock_lib):

        """Function:  test_multiple_errors

        Description:  Test with multiple errors returned.

        Arguments:

        """

        mock_lib.load_module.return_value = self.cfg
        mock_lib.chk_crt_dir.side_effect = [self.true, self.true,
                                            [False, self.err_msg3]]
        mock_lib.chk_crt_file.side_effect = [[False, self.err_msg4]]

        self.assertEqual(merge_repo.load_cfg(self.cfg_name, self.cfg_dir),
                         (self.cfg, False, [self.err_msg3, self.err_msg4]))

    @mock.patch("merge_repo.gen_libs")
    def test_log_file_false(self, mock_lib):

        """Function:  test_log_file_false

        Description:  Test log_file check returns False.

        Arguments:

        """

        mock_lib.load_module.return_value = self.cfg
        mock_lib.chk_crt_dir.side_effect = [self.true, self.true, self.true]
        mock_lib.chk_crt_file.side_effect = [[False, self.err_msg4]]

        self.assertEqual(merge_repo.load_cfg(self.cfg_name, self.cfg_dir),
                         (self.cfg, False, [self.err_msg4]))

    @mock.patch("merge_repo.gen_libs")
    def test_log_file_true(self, mock_lib):

        """Function:  test_log_file_true

        Description:  Test log_file check returns True.

        Arguments:

        """

        mock_lib.load_module.return_value = self.cfg
        mock_lib.chk_crt_dir.side_effect = [self.true, self.true, self.true]
        mock_lib.chk_crt_file.side_effect = [self.true]

        self.assertEqual(merge_repo.load_cfg(self.cfg_name, self.cfg_dir),
                         (self.cfg, True, []))

    @mock.patch("merge_repo.gen_libs")
    def test_archive_dir_false(self, mock_lib):

        """Function:  test_archive_dir_false

        Description:  Test archive_dir check returns False.

        Arguments:

        """

        mock_lib.load_module.return_value = self.cfg
        mock_lib.chk_crt_dir.side_effect = [self.true, self.true,
                                            [False, self.err_msg3]]
        mock_lib.chk_crt_file.side_effect = [self.true]

        self.assertEqual(merge_repo.load_cfg(self.cfg_name, self.cfg_dir),
                         (self.cfg, False, [self.err_msg3]))

    @mock.patch("merge_repo.gen_libs")
    def test_archive_dir_true(self, mock_lib):

        """Function:  test_archive_dir_true

        Description:  Test archive_dir check returns True.

        Arguments:

        """

        mock_lib.load_module.return_value = self.cfg
        mock_lib.chk_crt_dir.side_effect = [self.true, self.true, self.true]
        mock_lib.chk_crt_file.side_effect = [self.true]

        self.assertEqual(merge_repo.load_cfg(self.cfg_name, self.cfg_dir),
                         (self.cfg, True, []))

    @mock.patch("merge_repo.gen_libs")
    def test_err_dir_false(self, mock_lib):

        """Function:  test_err_dir_false

        Description:  Test err_dir check returns False.

        Arguments:

        """

        mock_lib.load_module.return_value = self.cfg
        mock_lib.chk_crt_dir.side_effect = [self.true, [False, self.err_msg2],
                                            self.true]
        mock_lib.chk_crt_file.side_effect = [self.true]

        self.assertEqual(merge_repo.load_cfg(self.cfg_name, self.cfg_dir),
                         (self.cfg, False, [self.err_msg2]))

    @mock.patch("merge_repo.gen_libs")
    def test_err_dir_true(self, mock_lib):

        """Function:  test_err_dir_true

        Description:  Test err_dir check returns True.

        Arguments:

        """

        mock_lib.load_module.return_value = self.cfg
        mock_lib.chk_crt_dir.side_effect = [self.true, self.true, self.true]
        mock_lib.chk_crt_file.side_effect = [self.true]

        self.assertEqual(merge_repo.load_cfg(self.cfg_name, self.cfg_dir),
                         (self.cfg, True, []))

    @mock.patch("merge_repo.gen_libs")
    def test_work_dir_false(self, mock_lib):

        """Function:  test_work_dir_false

        Description:  Test work_dir check returns False.

        Arguments:

        """

        mock_lib.load_module.return_value = self.cfg
        mock_lib.chk_crt_dir.side_effect = [(False, self.err_msg), self.true,
                                            self.true]
        mock_lib.chk_crt_file.side_effect = [self.true]

        self.assertEqual(merge_repo.load_cfg(self.cfg_name, self.cfg_dir),
                         (self.cfg, False, [self.err_msg]))

    @mock.patch("merge_repo.gen_libs")
    def test_work_dir_true(self, mock_lib):

        """Function:  test_work_dir_true

        Description:  Test work_dir check returns True.

        Arguments:

        """

        mock_lib.load_module.return_value = self.cfg
        mock_lib.chk_crt_dir.side_effect = [self.true, self.true, self.true]
        mock_lib.chk_crt_file.side_effect = [self.true]

        self.assertEqual(merge_repo.load_cfg(self.cfg_name, self.cfg_dir),
                         (self.cfg, True, []))


if __name__ == "__main__":
    unittest.main()
