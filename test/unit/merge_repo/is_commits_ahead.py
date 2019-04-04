#!/usr/bin/python
# Classification (U)

"""Program:  is_commits_ahead.py

    Description:  Unit testing of merge_repo in is_commits_ahead.py.

    Usage:
        test/unit/merge_repo/is_commits_ahead.py

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


class GitRepo(object):

    """Class:  GitRepo

    Description:  Class stub holder for GitRepo class.

    Super-Class:  None

    Sub-Classes:  None

    Methods:
        __init__ -> Class initialization.
        iter_commits -> Stub holder for iter_commits method.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:
            None

        """

        self.commit_diff = []

    def iter_commits(self, data_str):

        """Method:  iter_commits

        Description:  Stub holder for iter_commits method.

        Arguments:
            (input) data_str -> Stub holder for argument.

        """

        return self.commit_diff


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Unit testing initilization.
        test_is_two_ahead -> Test with two commits ahead of remote repo.
        test_is_one_ahead -> Test with one commit ahead of remote repo.
        test_is_zero_ahead -> Test with zero commits ahead of remote repo.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        self.gitrepo = GitRepo()
        self.branch = "master"

    @mock.patch("merge_repo.commits_diff")
    def test_is_two_ahead(self, mock_diff):

        """Function:  test_is_two_ahead

        Description:  Test with two commits ahead of remote repo.

        Arguments:
            mock_diff -> Mock Ref:  merge_repo.commits_diff

        """

        mock_diff.return_value = 2

        self.assertEqual(merge_repo.is_commits_ahead(self.gitrepo,
                                                     self.branch), 2)

    @mock.patch("merge_repo.commits_diff")
    def test_is_one_ahead(self, mock_diff):

        """Function:  test_is_one_ahead

        Description:  Test with one commit ahead of remote repo.

        Arguments:
            mock_diff -> Mock Ref:  merge_repo.commits_diff

        """

        mock_diff.return_value = 1

        self.assertEqual(merge_repo.is_commits_ahead(self.gitrepo,
                                                     self.branch), 1)

    @mock.patch("merge_repo.commits_diff")
    def test_is_zero_ahead(self, mock_diff):

        """Function:  test_is_zero_ahead

        Description:  Test with zero commits ahead of remote repo.

        Arguments:
            mock_diff -> Mock Ref:  merge_repo.commits_diff

        """

        mock_diff.return_value = 0

        self.assertEqual(merge_repo.is_commits_ahead(self.gitrepo,
                                                     self.branch), 0)


if __name__ == "__main__":
    unittest.main()
