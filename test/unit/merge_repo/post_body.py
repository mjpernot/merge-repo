# Classification (U)

"""Program:  post_body.py

    Description:  Unit testing of post_body in merge_repo.py.

    Usage:
        test/unit/merge_repo/post_body.py

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
        test_body_data
        test_body_empty

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.gitr = GitMerge()

        self.body = ["Merge of project has been completed."]
        self.dtg = "2019-04-16 13:51:42"

    @mock.patch("merge_repo.datetime.datetime")
    def test_body_data(self, mock_date):

        """Function:  test_body_data

        Description:  Test with body with data.

        Arguments:

        """

        mock_date.now.return_value = "(2019, 4, 16, 13, 51, 42, 852147)"
        mock_date.strftime.return_value = self.dtg

        test_body = list(self.body)
        test_body.append("URL: " + self.gitr.url)
        test_body.append("Git Dir: " + self.gitr.git_dir)
        test_body.append("Branch: " + self.gitr.branch)
        test_body.append("DTG: " + self.dtg)

        self.assertEqual(merge_repo.post_body(self.gitr, self.body), test_body)

    @mock.patch("merge_repo.datetime.datetime")
    def test_body_empty(self, mock_date):

        """Function:  test_body_empty

        Description:  Test with body with empty list.

        Arguments:

        """

        mock_date.now.return_value = "(2019, 4, 16, 13, 51, 42, 852147)"
        mock_date.strftime.return_value = self.dtg

        test_body = []
        test_body.append("URL: " + self.gitr.url)
        test_body.append("Git Dir: " + self.gitr.git_dir)
        test_body.append("Branch: " + self.gitr.branch)
        test_body.append("DTG: " + self.dtg)

        self.assertEqual(merge_repo.post_body(self.gitr, None), test_body)


if __name__ == "__main__":
    unittest.main()
