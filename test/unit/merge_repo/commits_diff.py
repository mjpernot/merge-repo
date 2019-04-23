#!/usr/bin/python
# Classification (U)

"""Program:  commits_diff.py

    Description:  Unit testing of merge_repo in commits_diff.py.

    Usage:
        test/unit/merge_repo/commits_diff.py

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
        test_is_two_diff -> Test with two commits difference between repos.
        test_is_one_diff -> Test with one commit difference between repos.
        test_is_zero_diff -> Test with zero commits diff between repos.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        self.gitrepo = GitRepo()
        self.branch = "master"

    def test_is_two_diff(self):

        """Function:  test_is_two_diff

        Description:  Test with two commits difference between repos.

        Arguments:
            None

        """

        self.gitrepo.commit_diff = [1, 2]

        self.assertEqual(merge_repo.commits_diff(self.gitrepo,
                                                 self.branch), 2)

    def test_is_one_diff(self):

        """Function:  test_is_one_diff

        Description:  Test with one commit difference between repos.

        Arguments:
            None

        """

        self.gitrepo.commit_diff = [1]

        self.assertEqual(merge_repo.commits_diff(self.gitrepo,
                                                 self.branch), 1)

    def test_is_zero_diff(self):

        """Function:  test_is_zero_diff

        Description:  Test with zero commits diff between repos.

        Arguments:
            None

        """

        self.assertEqual(merge_repo.commits_diff(self.gitrepo,
                                                 self.branch), 0)


if __name__ == "__main__":
    unittest.main()
