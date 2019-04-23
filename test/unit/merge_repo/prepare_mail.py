#!/usr/bin/python
# Classification (U)

"""Program:  prepare_mail.py

    Description:  Unit testing of prepare_mail in merge_repo.py.

    Usage:
        test/unit/merge_repo/prepare_mail.py

    Arguments:
        None

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Third-party
import mock

# Local
sys.path.append(os.getcwd())
import merge_repo
import lib.gen_libs as gen_libs
import version

# Version Information
__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Unit testing initilization.
        test_msg_data -> Test with msg with data.
        test_linelist_empty -> Test with line_list with empty list.
        test_linelist_data -> Test with line_list with data.
        test_status_true -> Test with status set to True.
        test_linelist_none -> Test with line_list set to None.
        test_help_message -> Test with no arguments.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

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

                self.repo_name = "repo-name"
                self.url = "git@gitlab.code.dicelab.net:JAC-IDM/"
                self.git_dir = "/home/mark.j.pernot/merge/work_dir/repo-name"
                self.branch = "master"

        self.gitr = GitMerge()
        self.status1 = True
        self.status2 = False
        self.line_list = []
        self.line_list2 = ["Test of line list"]
        self.msg = {"Key": "Value"}

        self.subj = "Merge completed for: " + self.gitr.repo_name
        self.subj2 = "Merge error for: " + self.gitr.repo_name
        self.body = ["Merge of project has been completed."]
        self.body2 = ["Merge of project has failed."]
        self.dtg = "2019-04-16 13:51:42"

    @mock.patch("merge_repo.datetime.datetime")
    def test_msg_data(self, mock_date):

        """Function:  test_msg_data

        Description:  Test with msg with data.

        Arguments:
            None

        """

        mock_date.now.return_value = "(2019, 4, 16, 13, 51, 42, 852147)"
        mock_date.strftime.return_value = self.dtg

        test_body = list(self.body2)

        for line in self.line_list2:
            test_body.append(line)

        for key in self.msg.keys():
            test_body.append("%s: %s" % (key, self.msg[key]))

        test_body.append("URL: " + self.gitr.url)
        test_body.append("Git Dir: " + self.gitr.git_dir)
        test_body.append("Branch: " + self.gitr.branch)
        test_body.append("DTG: " + self.dtg)

        subj, body = merge_repo.prepare_mail(self.gitr, self.status1,
                                             self.line_list2, self.msg)

        self.assertEqual((subj, body), (self.subj2, test_body))

    @mock.patch("merge_repo.datetime.datetime")
    def test_linelist_empty(self, mock_date):

        """Function:  test_linelist_empty

        Description:  Test with line_list with empty list.

        Arguments:
            None

        """

        mock_date.now.return_value = "(2019, 4, 16, 13, 51, 42, 852147)"
        mock_date.strftime.return_value = self.dtg

        test_body = list(self.body2)

        test_body.append("URL: " + self.gitr.url)
        test_body.append("Git Dir: " + self.gitr.git_dir)
        test_body.append("Branch: " + self.gitr.branch)
        test_body.append("DTG: " + self.dtg)

        subj, body = merge_repo.prepare_mail(self.gitr, self.status1,
                                             self.line_list)

        self.assertEqual((subj, body), (self.subj2, test_body))

    @mock.patch("merge_repo.datetime.datetime")
    def test_linelist_data(self, mock_date):

        """Function:  test_linelist_data

        Description:  Test with line_list with data.

        Arguments:
            None

        """

        mock_date.now.return_value = "(2019, 4, 16, 13, 51, 42, 852147)"
        mock_date.strftime.return_value = self.dtg

        test_body = list(self.body2)

        for line in self.line_list2:
            test_body.append(line)

        test_body.append("URL: " + self.gitr.url)
        test_body.append("Git Dir: " + self.gitr.git_dir)
        test_body.append("Branch: " + self.gitr.branch)
        test_body.append("DTG: " + self.dtg)

        subj, body = merge_repo.prepare_mail(self.gitr, self.status1,
                                             self.line_list2)

        self.assertEqual((subj, body), (self.subj2, test_body))

    @mock.patch("merge_repo.datetime.datetime")
    def test_status_true(self, mock_date):

        """Function:  test_status_true

        Description:  Test with status set to True.

        Arguments:
            None

        """

        mock_date.now.return_value = "(2019, 4, 16, 13, 51, 42, 852147)"
        mock_date.strftime.return_value = self.dtg

        test_body = list(self.body2)
        test_body.append("URL: " + self.gitr.url)
        test_body.append("Git Dir: " + self.gitr.git_dir)
        test_body.append("Branch: " + self.gitr.branch)
        test_body.append("DTG: " + self.dtg)

        subj, body = merge_repo.prepare_mail(self.gitr, self.status1)

        self.assertEqual((subj, body), (self.subj2, test_body))

    @mock.patch("merge_repo.datetime.datetime")
    def test_linelist_none(self, mock_date):

        """Function:  test_linelist_none

        Description:  Test with line_list set to None.

        Arguments:
            None

        """

        mock_date.now.return_value = "(2019, 4, 16, 13, 51, 42, 852147)"
        mock_date.strftime.return_value = self.dtg

        test_body = list(self.body)
        test_body.append("DTG: " + self.dtg)

        subj, body = merge_repo.prepare_mail(self.gitr, self.status2,
                                             line_list=None)

        self.assertEqual((subj, body), (self.subj, test_body))

    @mock.patch("merge_repo.datetime.datetime")
    def test_status_false(self, mock_date):

        """Function:  test_status_false

        Description:  Test with status set to False.

        Arguments:
            None

        """

        mock_date.now.return_value = "(2019, 4, 16, 13, 51, 42, 852147)"
        mock_date.strftime.return_value = self.dtg

        test_body = list(self.body)
        test_body.append("DTG: " + self.dtg)

        subj, body = merge_repo.prepare_mail(self.gitr, self.status2)

        self.assertEqual((subj, body), (self.subj, test_body))


if __name__ == "__main__":
    unittest.main()
