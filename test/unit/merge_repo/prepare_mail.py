# Classification (U)

"""Program:  prepare_mail.py

    Description:  Unit testing of prepare_mail in merge_repo.py.

    Usage:
        test/unit/merge_repo/prepare_mail.py

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


class GitMerge(object):                         # pylint:disable=R0903,R0205

    """Class:  GitMerge

    Description:  Class which is a representation of GitMerge module.

    Methods:
        __init__

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the GitMerge class.

        Arguments:

        """

        self.repo_name = "repo-name"
        self.url = "git@github.com:JAC-IDM/"
        self.git_dir = "/data/merge-repo/work_dir/repo-name"
        self.branch = "master"


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_msg_data
        test_linelist_empty
        test_linelist_data
        test_status_false
        test_linelist_none
        test_status_true

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.gitr = GitMerge()
        self.status1 = True
        self.status2 = False
        self.line_list = []
        self.line_list2 = ["Test of line list"]
        self.msg = {"Key": "Value"}
        self.datetime = "(2019, 4, 16, 13, 51, 42, 852147)"

        self.subj = "Merge completed for: " + self.gitr.repo_name
        self.subj2 = "Merge error for: " + self.gitr.repo_name
        self.body = ["Merge of project has been completed."]
        self.body2 = ["Merge of project has failed."]
        self.dtg = "2019-04-16 13:51:42"
        self.keystr = "Git Dir: "
        self.keystr2 = "Branch: "
        self.urls = "URL: "
        self.dtgs = "DTG: "

    @mock.patch("merge_repo.datetime.datetime")
    def test_msg_data(self, mock_date):

        """Function:  test_msg_data

        Description:  Test with msg with data.

        Arguments:

        """

        mock_date.now.return_value = self.datetime
        mock_date.strftime.return_value = self.dtg

        test_body = list(self.body2)

        for line in self.line_list2:
            test_body.append(line)

        for key in self.msg:                            # pylint:disable=C0206
            test_body.append("%s: %s" % (key, self.msg[key]))

        test_body.append(self.urls + self.gitr.url)
        test_body.append(self.keystr + self.gitr.git_dir)
        test_body.append(self.keystr2 + self.gitr.branch)
        test_body.append(self.dtgs + self.dtg)

        subj, body = merge_repo.prepare_mail(self.gitr, self.status2,
                                             self.line_list2, self.msg)

        self.assertEqual((subj, body), (self.subj2, test_body))

    @mock.patch("merge_repo.datetime.datetime")
    def test_linelist_empty(self, mock_date):

        """Function:  test_linelist_empty

        Description:  Test with line_list with empty list.

        Arguments:

        """

        mock_date.now.return_value = self.datetime
        mock_date.strftime.return_value = self.dtg

        test_body = list(self.body2)

        test_body.append(self.urls + self.gitr.url)
        test_body.append(self.keystr + self.gitr.git_dir)
        test_body.append(self.keystr2 + self.gitr.branch)
        test_body.append(self.dtgs + self.dtg)

        subj, body = merge_repo.prepare_mail(self.gitr, self.status2,
                                             self.line_list)

        self.assertEqual((subj, body), (self.subj2, test_body))

    @mock.patch("merge_repo.datetime.datetime")
    def test_linelist_data(self, mock_date):

        """Function:  test_linelist_data

        Description:  Test with line_list with data.

        Arguments:

        """

        mock_date.now.return_value = self.datetime
        mock_date.strftime.return_value = self.dtg

        test_body = list(self.body2)

        for line in self.line_list2:
            test_body.append(line)

        test_body.append(self.urls + self.gitr.url)
        test_body.append(self.keystr + self.gitr.git_dir)
        test_body.append(self.keystr2 + self.gitr.branch)
        test_body.append(self.dtgs + self.dtg)

        subj, body = merge_repo.prepare_mail(self.gitr, self.status2,
                                             self.line_list2)

        self.assertEqual((subj, body), (self.subj2, test_body))

    @mock.patch("merge_repo.datetime.datetime")
    def test_status_false(self, mock_date):

        """Function:  test_status_false

        Description:  Test with status set to False.

        Arguments:

        """

        mock_date.now.return_value = self.datetime
        mock_date.strftime.return_value = self.dtg

        test_body = list(self.body2)
        test_body.append(self.urls + self.gitr.url)
        test_body.append(self.keystr + self.gitr.git_dir)
        test_body.append(self.keystr2 + self.gitr.branch)
        test_body.append(self.dtgs + self.dtg)

        subj, body = merge_repo.prepare_mail(self.gitr, self.status2)

        self.assertEqual((subj, body), (self.subj2, test_body))

    @mock.patch("merge_repo.datetime.datetime")
    def test_linelist_none(self, mock_date):

        """Function:  test_linelist_none

        Description:  Test with line_list set to None.

        Arguments:

        """

        mock_date.now.return_value = self.datetime
        mock_date.strftime.return_value = self.dtg

        test_body = list(self.body)
        test_body.append(self.urls + self.gitr.url)
        test_body.append(self.keystr + self.gitr.git_dir)
        test_body.append(self.keystr2 + self.gitr.branch)
        test_body.append(self.dtgs + self.dtg)

        subj, body = merge_repo.prepare_mail(self.gitr, self.status1,
                                             line_list=None)

        self.assertEqual((subj, body), (self.subj, test_body))

    @mock.patch("merge_repo.datetime.datetime")
    def test_status_true(self, mock_date):

        """Function:  test_status_true

        Description:  Test with status set to True.

        Arguments:

        """

        mock_date.now.return_value = self.datetime
        mock_date.strftime.return_value = self.dtg

        test_body = list(self.body)
        test_body.append(self.urls + self.gitr.url)
        test_body.append(self.keystr + self.gitr.git_dir)
        test_body.append(self.keystr2 + self.gitr.branch)
        test_body.append(self.dtgs + self.dtg)

        subj, body = merge_repo.prepare_mail(self.gitr, self.status1)

        self.assertEqual((subj, body), (self.subj, test_body))


if __name__ == "__main__":
    unittest.main()
