#!/usr/bin/python
# Classification (U)

"""Program:  quarantine_files.py

    Description:  Unit testing of quarantine_files in merge_repo.py.

    Usage:
        test/unit/merge_repo/quarantine_files.py

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
        test_modified_no_list -> Test status set to modified with empty list.
        test_added_no_list -> Test with status set to added with empty list.
        test_no_status -> Test with status not set.
        test_modified_status -> Test with status set to modified.
        test_added_status -> Test with status set to added.

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

                self.quar_dir = "/directory/quarantine"
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
                self.repo_name = "Repo_Name"
                self.git_dir = "/directory/git_dir"

        self.gitr = GitMerge()
        self.cfg = CfgTest()

        self.dtg = "2019-04-16 13:51:42"

    @mock.patch("merge_repo.gen_class.Logger")
    def test_modified_no_list(self, mock_log):

        """Function:  test_modified_no_list

        Description:  Test with status set to modified with empty list.

        Arguments:
            None

        """

        mock_log.return_value = True

        self.assertFalse(merge_repo.quarantine_files(self.gitr, self.cfg,
                                                     mock_log,
                                                     status="modified"))

    @mock.patch("merge_repo.gen_class.Logger")
    def test_added_no_list(self, mock_log):

        """Function:  test_added_no_list

        Description:  Test with status set to added with empty list.

        Arguments:
            None

        """

        mock_log.return_value = True

        self.assertFalse(merge_repo.quarantine_files(self.gitr, self.cfg,
                                                     mock_log, status="added"))

    @mock.patch("merge_repo.gen_class.Logger")
    def test_no_status(self, mock_log):

        """Function:  test_no_status

        Description:  Test with status not set.

        Arguments:
            None

        """

        mock_log.return_value = True

        self.gitr.chg_files = ["File1"]

        self.assertFalse(merge_repo.quarantine_files(self.gitr, self.cfg,
                                                     mock_log))

    @mock.patch("merge_repo.send_mail")
    @mock.patch("merge_repo.post_body")
    @mock.patch("merge_repo.gen_libs.cp_file")
    @mock.patch("merge_repo.datetime.datetime")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_modified_status(self, mock_log, mock_date, mock_cp, mock_body,
                             mock_mail):

        """Function:  test_modified_status

        Description:  Test with status set to modified.

        Arguments:
            None

        """

        mock_date.now.return_value = "(2019, 4, 16, 13, 51, 42, 852147)"
        mock_date.strftime.return_value = self.dtg
        mock_log.return_value = True
        mock_cp.return_value = True
        mock_body.return_value = True
        mock_mail.return_value = True

        self.gitr.chg_files = ["File1"]

        self.assertFalse(merge_repo.quarantine_files(self.gitr, self.cfg,
                                                     mock_log,
                                                     status="modified"))

    @mock.patch("merge_repo.send_mail")
    @mock.patch("merge_repo.post_body")
    @mock.patch("merge_repo.gen_libs.cp_file")
    @mock.patch("merge_repo.datetime.datetime")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_added_status(self, mock_log, mock_date, mock_cp, mock_body,
                          mock_mail):

        """Function:  test_added_status

        Description:  Test with status set to added.

        Arguments:
            None

        """

        mock_date.now.return_value = "(2019, 4, 16, 13, 51, 42, 852147)"
        mock_date.strftime.return_value = self.dtg
        mock_log.return_value = True
        mock_cp.return_value = True
        mock_body.return_value = True
        mock_mail.return_value = True

        self.gitr.new_files = ["File1"]

        self.assertFalse(merge_repo.quarantine_files(self.gitr, self.cfg,
                                                     mock_log, status="added"))


if __name__ == "__main__":
    unittest.main()
