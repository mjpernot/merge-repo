#!/usr/bin/python
# Classification (U)

"""Program:  gitmerge_commits_diff.py

    Description:  Unit testing of gitmerge.commits_diff in git_class.py.

    Usage:
        test/unit/git_class/gitmerge_commits_diff.py

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


class Commits(object):

    """Class:  Diff

    Description:  Class stub holder for git.gitrepo.iter_commits.

    Methods:
        __init -> Class initilization.

    """

    def __init__(self, test_type):

        """Function:  __init__

        Description:  Initialization of class instance.

        Arguments:
            test_type -> Determine type of test to be created.

        """

        self.test_type = test_type

    def iter_commits(self, data_str):

        """Method:  iter_commits

        Description:  Method stub holder for git.gitrepo.iter_commits().

        Arguments:
            data_str -> Stub holder.

        """

        INDEX = collections.namedtuple('INDEX', 'commits')

        if self.test_type == 1:
            commit_list = []
            commit_list.append(INDEX('file1'))
            commit_list.append(INDEX('file2'))

        elif self.test_type == 2:
            commit_list = []
            commit_list.append(INDEX('file2'))

        elif self.test_type == 3:
            commit_list = []

        return commit_list


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

    def test_commitsdiff_zero(self):

        """Function:  test_commitsdiff_zero

        Description:  Test with zero commits difference.

        Arguments:
            None

        """

        GIT = collections.namedtuple('GIT', 'iter_commits')
        COMMIT = Commits(3).iter_commits
        self.gitr.gitrepo = GIT(COMMIT)

        self.assertEqual(self.gitr.commits_diff("Data"), 0)

    def test_commitsdiff_one(self):

        """Function:  test_commitsdiff_one

        Description:  Test with one commit difference.

        Arguments:
            None

        """

        GIT = collections.namedtuple('GIT', 'iter_commits')
        COMMIT = Commits(2).iter_commits
        self.gitr.gitrepo = GIT(COMMIT)

        self.assertEqual(self.gitr.commits_diff("Data"), 1)

    def test_commitsdiff_two(self):

        """Function:  test_commitsdiff_two

        Description:  Test with two commits difference.

        Arguments:
            None

        """

        GIT = collections.namedtuple('GIT', 'iter_commits')
        COMMIT = Commits(1).iter_commits
        self.gitr.gitrepo = GIT(COMMIT)

        self.assertEqual(self.gitr.commits_diff("Data"), 2)


if __name__ == "__main__":
    unittest.main()
