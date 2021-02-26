#!/usr/bin/python
# Classification (U)

"""Program:  post_check.py

    Description:  Unit testing of post_check in merge_repo.py.

    Usage:
        test/unit/merge_repo/post_check.py

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
        test_behind_one -> Test with behind set to one.
        test_behind_zero -> Test with behind set to zero.
        test_ahead_one -> Test with ahead set to one.
        test_ahead_zero -> Test with ahead set to zero.

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

                self.archive_dir = "/Arhive/Directory"
                self.err_dir = "/Error/Directory"
                self.to_line = "to@domain"

        self.cfg = CfgTest()
        self.git_results = "/Git/Directory"

    @mock.patch("merge_repo.post_process")
    @mock.patch("merge_repo.git_class.GitMerge")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_behind_one(self, mock_log, mock_git, mock_post):

        """Function:  test_behind_one

        Description:  Test with behind set to one.

        Arguments:

        """

        mock_log.return_value = True
        mock_git.is_commits_ahead.return_value = 0
        mock_git.is_commits_behind.return_value = 1
        mock_git.git_dir.return_value = self.git_results
        mock_post.return_value = True

        self.assertFalse(merge_repo.post_check(mock_git, self.cfg, mock_log))

    @mock.patch("merge_repo.post_process")
    @mock.patch("merge_repo.git_class.GitMerge")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_behind_zero(self, mock_log, mock_git, mock_post):

        """Function:  test_behind_zero

        Description:  Test with ahead set to zero.

        Arguments:

        """

        mock_log.return_value = True
        mock_git.is_commits_ahead.return_value = 0
        mock_git.is_commits_behind.return_value = 0
        mock_git.git_dir.return_value = self.git_results
        mock_post.return_value = True

        self.assertFalse(merge_repo.post_check(mock_git, self.cfg, mock_log))

    @mock.patch("merge_repo.post_process")
    @mock.patch("merge_repo.git_class.GitMerge")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_ahead_one(self, mock_log, mock_git, mock_post):

        """Function:  test_ahead_zero

        Description:  Test with ahead set to one.

        Arguments:

        """

        mock_log.return_value = True
        mock_git.is_commits_ahead.return_value = 1
        mock_git.is_commits_behind.return_value = 0
        mock_git.git_dir.return_value = self.git_results
        mock_post.return_value = True

        self.assertFalse(merge_repo.post_check(mock_git, self.cfg, mock_log))

    @mock.patch("merge_repo.post_process")
    @mock.patch("merge_repo.git_class.GitMerge")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_ahead_zero(self, mock_log, mock_git, mock_post):

        """Function:  test_ahead_zero

        Description:  Test with ahead set to zero.

        Arguments:

        """

        mock_log.return_value = True
        mock_git.is_commits_ahead.return_value = 0
        mock_git.is_commits_behind.return_value = 0
        mock_git.git_dir.return_value = self.git_results
        mock_post.return_value = True

        self.assertFalse(merge_repo.post_check(mock_git, self.cfg, mock_log))


if __name__ == "__main__":
    unittest.main()
