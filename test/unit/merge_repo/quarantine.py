#!/usr/bin/python
# Classification (U)

"""Program:  quarantine.py

    Description:  Unit testing of quarantine in merge_repo.py.

    Usage:
        test/unit/merge_repo/quarantine.py

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

                self.archive_dir = "/Arhive/Directory"
                self.err_dir = "/Error/Directory"
                self.to_line = "to@domain"

        class GitMerge(object):

            """Class:  GitMerge

            Description:  Class which is a representation of GitMerge module.

            Super-Class:  object

            Sub-Classes:  None

            Methods:
                __init__ -> Initialize configuration environment.

            """

            def __init__(self):

                """Method:  __init__

                Description:  Initialization instance of the GitMerge class.

                Arguments:
                        None

                """

                self.chg_files = []
                self.new_files = []
                self.rm_files = []
                self.repo_name = "Repo_Name"

        self.gitr = GitMerge()
        self.cfg = CfgTest()

    @mock.patch("merge_repo.send_mail")
    @mock.patch("merge_repo.post_body")
    @mock.patch("merge_repo.quarantine_files")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_all_lists(self, mock_log, mock_quar, mock_body, mock_mail):

        """Function:  test_all_lists

        Description:  Test with all lists with data.

        Arguments:
            None

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
            None

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
            None

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
            None

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
            None

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
            None

        """

        mock_log.return_value = True
        mock_quar.return_value = True

        self.assertFalse(merge_repo.quarantine(self.gitr, self.cfg, mock_log))


if __name__ == "__main__":
    unittest.main()