#!/usr/bin/python
# Classification (U)

"""Program:  post_process.py

    Description:  Unit testing of post_process in merge_repo.py.

    Usage:
        test/unit/merge_repo/post_process.py

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
        test_msg_passed -> Test with msg passed with data.
        test_linelist_passed -> Test with line_list passed with data.
        test_status_false -> Test with status set to False.
        test_status_true -> Test with status set to True.

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

                self.git_dir = "/directory/git_repo"

        self.gitr = GitMerge()
        self.cfg = CfgTest()
        self.subj = "Email_Subject"
        self.body = ["Email Body Line 1", "Email Body Line 2"]
        self.status1 = True
        self.status2 = False

    @mock.patch("merge_repo.gen_class.Logger")
    @mock.patch("merge_repo.move")
    def test_no_email(self, mock_move, mock_log):

        """Function:  test_no_email

        Description:  Test with no email notifications.

        Arguments:

        """

        mock_log.return_value = True
        mock_move.return_value = True

        msg = {"1": "Line1", "2": "Line2"}
        self.cfg.to_line = None

        self.assertFalse(merge_repo.post_process(self.gitr, self.cfg, mock_log,
                                                 self.status1, msg=msg))

    @mock.patch("merge_repo.gen_class.Logger")
    @mock.patch("merge_repo.move")
    @mock.patch("merge_repo.prepare_mail")
    @mock.patch("merge_repo.send_mail")
    def test_msg_passed(self, mock_mail, mock_prepare, mock_move, mock_log):

        """Function:  test_msg_passed

        Description:  Test with msg passed with data.

        Arguments:

        """

        mock_log.return_value = True
        mock_mail.return_value = True
        mock_prepare.return_value = (self.subj, self.body)
        mock_move.return_value = True

        msg = {"1": "Line1", "2": "Line2"}

        self.assertFalse(merge_repo.post_process(self.gitr, self.cfg, mock_log,
                                                 self.status1, msg=msg))

    @mock.patch("merge_repo.gen_class.Logger")
    @mock.patch("merge_repo.move")
    @mock.patch("merge_repo.prepare_mail")
    @mock.patch("merge_repo.send_mail")
    def test_linelist_passed(self, mock_mail, mock_prepare, mock_move,
                             mock_log):

        """Function:  test_linelist_passed

        Description:  Test with line_list passed with data.

        Arguments:

        """

        mock_log.return_value = True
        mock_mail.return_value = True
        mock_prepare.return_value = (self.subj, self.body)
        mock_move.return_value = True

        line_list = ["Line1", "Line2"]

        self.assertFalse(merge_repo.post_process(self.gitr, self.cfg, mock_log,
                                                 self.status1,
                                                 line_list=line_list))

    @mock.patch("merge_repo.gen_class.Logger")
    @mock.patch("merge_repo.move")
    @mock.patch("merge_repo.prepare_mail")
    @mock.patch("merge_repo.send_mail")
    def test_status_false(self, mock_mail, mock_prepare, mock_move, mock_log):

        """Function:  test_status_false

        Description:  Test with status set to False.

        Arguments:

        """

        mock_log.return_value = True
        mock_mail.return_value = True
        mock_prepare.return_value = (self.subj, self.body)
        mock_move.return_value = True

        self.assertFalse(merge_repo.post_process(self.gitr, self.cfg, mock_log,
                                                 self.status2))

    @mock.patch("merge_repo.gen_class.Logger")
    @mock.patch("merge_repo.move")
    @mock.patch("merge_repo.prepare_mail")
    @mock.patch("merge_repo.send_mail")
    def test_status_true(self, mock_mail, mock_prepare, mock_move, mock_log):

        """Function:  test_status_true

        Description:  Test with status set to True.

        Arguments:

        """

        mock_log.return_value = True
        mock_mail.return_value = True
        mock_prepare.return_value = (self.subj, self.body)
        mock_move.return_value = True

        self.assertFalse(merge_repo.post_process(self.gitr, self.cfg, mock_log,
                                                 self.status1))


if __name__ == "__main__":
    unittest.main()
