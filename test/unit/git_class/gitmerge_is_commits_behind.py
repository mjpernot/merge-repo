#!/usr/bin/python
# Classification (U)

"""Program:  gitmerge_is_commits_behind.py

    Description:  Unit testing of gitmerge.is_commits_behind in git_class.py.

    Usage:
        test/unit/git_class/gitmerge_is_commits_behind.py

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
import git
import collections

# Local
sys.path.append(os.getcwd())
import git_class
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
        test_commitsdiff_zero -> Test with zero commits difference.
        test_commitsdiff_one -> Test with one commit difference.
        test_commitsdiff_two -> Test with two commits difference.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        self.repo_name = "Repo_name"
        self.git_dir = "/directory/git"
        self.url = "URL"
        self.branch = "Remote_branch"
        self.mod_branch = "Mod_branch"

        self.gitr = git_class.GitMerge(self.repo_name, self.git_dir, self.url,
                                       self.branch, self.mod_branch)

    @mock.patch("git_class.GitMerge.commits_diff")
    def test_commitsdiff_zero(self, mock_commit):

        """Function:  test_commitsdiff_zero

        Description:  Test with zero commits difference.

        Arguments:
            None

        """

        mock_commit.return_value = 0

        self.assertEqual(self.gitr.is_commits_behind("Data"), 0)

    @mock.patch("git_class.GitMerge.commits_diff")
    def test_commitsdiff_one(self, mock_commit):

        """Function:  test_commitsdiff_one

        Description:  Test with one commit difference.

        Arguments:
            None

        """

        mock_commit.return_value = 1

        self.assertEqual(self.gitr.is_commits_behind("Data"), 1)

    @mock.patch("git_class.GitMerge.commits_diff")
    def test_commitsdiff_two(self, mock_commit):

        """Function:  test_commitsdiff_two

        Description:  Test with two commits difference.

        Arguments:
            None

        """

        mock_commit.return_value = 2

        self.assertEqual(self.gitr.is_commits_behind("Data"), 2)


if __name__ == "__main__":
    unittest.main()
