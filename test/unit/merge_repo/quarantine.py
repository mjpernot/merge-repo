#!/usr/bin/python
# Classification (U)

"""Program:  quarantine.py

    Description:  Unit testing of quarantine in merge_repo.py.

    Usage:
        test/unit/merge_repo/quarantine.py

    Arguments:

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
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Unit testing initilization.
        test_no_email -> Test with no email notifications.
        test_all_lists -> Test with all lists with data.
        test_rmfiles_list -> Test with rm_files list with data.
        test_both_lists -> Test with both lists with data.
        test_newfiles_list -> Test with new_files list with data.
        test_chgfiles_list -> Test with chg_files list with data.
        test_empty_lists -> Test with chg_files & new_files are empty lists.

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
                __init__ -> Initialize configuration environment.

            """

            def __init__(self):

                """Method:  __init__

                Description:  Initialization instance of the CfgTest class.

                Arguments:

                """

                self.archive_dir = "/data/merge-repo/archive_dir"
                self.err_dir = "/data/merge-repo/error_dir"
                self.to_line = "to@domain"

        class GitMerge(object):

            """Class:  GitMerge

            Description:  Class which is a representation of GitMerge module.

            Methods:
                __init__ -> Initialize configuration environment.

            """

            def __init__(self):

                """Method:  __init__

                Description:  Initialization instance of the GitMerge class.

                Arguments:

                """

                self.chg_files = []
                self.new_files = []
                self.rm_files = []
                self.repo_name = "Repo_Name"

        self.gitr = GitMerge()
        self.cfg = CfgTest()

    @mock.patch("merge_repo.quarantine_files")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_no_email(self, mock_log, mock_quar):

        """Function:  test_no_email

        Description:  Test with no email notifications.

        Arguments:

        """

        self.gitr.new_files = ["File1"]
        self.gitr.chg_files = ["File2"]
        self.gitr.rm_files = ["File3"]
        self.cfg.to_line = None

        mock_log.return_value = True
        mock_quar.return_value = True

        self.assertFalse(merge_repo.quarantine(self.gitr, self.cfg, mock_log))

    @mock.patch("merge_repo.send_mail")
    @mock.patch("merge_repo.post_body")
    @mock.patch("merge_repo.quarantine_files")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_all_lists(self, mock_log, mock_quar, mock_body, mock_mail):

        """Function:  test_all_lists

        Description:  Test with all lists with data.

        Arguments:

        """

        self.gitr.new_files = ["File1"]
        self.gitr.chg_files = ["File2"]
        self.gitr.rm_files = ["File3"]

        mock_log.return_value = True
        mock_quar.return_value = True
        mock_body.return_value = True
        mock_mail.return_value = True

        self.assertFalse(merge_repo.quarantine(self.gitr, self.cfg, mock_log))

    @mock.patch("merge_repo.send_mail")
    @mock.patch("merge_repo.post_body")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_rmfiles_list(self, mock_log, mock_body, mock_mail):

        """Function:  test_rmfiles_list

        Description:  Test with rm_files list with data.

        Arguments:

        """

        self.gitr.rm_files = ["File1"]

        mock_log.return_value = True
        mock_body.return_value = True
        mock_mail.return_value = True

        self.assertFalse(merge_repo.quarantine(self.gitr, self.cfg, mock_log))

    @mock.patch("merge_repo.quarantine_files")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_both_lists(self, mock_log, mock_quar):

        """Function:  test_both_lists

        Description:  Test with both lists with data.

        Arguments:

        """

        self.gitr.new_files = ["File1"]
        self.gitr.chg_files = ["File2"]

        mock_log.return_value = True
        mock_quar.return_value = True

        self.assertFalse(merge_repo.quarantine(self.gitr, self.cfg, mock_log))

    @mock.patch("merge_repo.quarantine_files")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_newfiles_list(self, mock_log, mock_quar):

        """Function:  test_newfiles_list

        Description:  Test with new_files list with data.

        Arguments:

        """

        self.gitr.new_files = ["File1"]

        mock_log.return_value = True
        mock_quar.return_value = True

        self.assertFalse(merge_repo.quarantine(self.gitr, self.cfg, mock_log))

    @mock.patch("merge_repo.quarantine_files")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_chgfiles_list(self, mock_log, mock_quar):

        """Function:  test_chgfiles_list

        Description:  Test with chg_files list with data.

        Arguments:

        """

        self.gitr.chg_files = ["File1"]

        mock_log.return_value = True
        mock_quar.return_value = True

        self.assertFalse(merge_repo.quarantine(self.gitr, self.cfg, mock_log))

    @mock.patch("merge_repo.quarantine_files")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_empty_lists(self, mock_log, mock_quar):

        """Function:  test_empty_lists

        Description:  Test with both chg_files and new_files are empty lists.

        Arguments:

        """

        mock_log.return_value = True
        mock_quar.return_value = True

        self.assertFalse(merge_repo.quarantine(self.gitr, self.cfg, mock_log))


if __name__ == "__main__":
    unittest.main()
