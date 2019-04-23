#!/usr/bin/python
# Classification (U)

"""Program:  gitmerge_git_fetch.py

    Description:  Unit testing of gitmerge.git_fetch in git_class.py.

    Usage:
        test/unit/git_class/gitmerge_git_fetch.py

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


def fetch3():

    """Function:  fetch3

    Description:  Method stub holder for git.Repo.git.fetch().

    Arguments:
        None

    """

    raise git.exc.GitCommandError("git", 2, "stderr")


def fetch2():

    """Function:  fetch2

    Description:  Method stub holder for git.Repo.git.fetch().

    Arguments:
        None

    """

    raise git.exc.GitCommandError("git", 128, "stderr")


def fetch():

    """Function:  fetch

    Description:  Method stub holder for git.Repo.git.fetch().

    Arguments:
        None

    """

    pass


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Unit testing initilization.
        test_git_fetch_2 -> Test with raised exception - 2 status.
        test_git_fetch_128 -> Test with raised exception - 128 status.
        test_git_fetch_true -> Test with successful ls_remote call.

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

    def test_git_fetch_2(self):

        """Function:  test_git_fetch_2

        Description:  Test with raised exception - 2 status.

        Arguments:
            None

        """

        GIT = collections.namedtuple('GIT', 'fetch')
        self.gitr.gitcmd = GIT(fetch3)

        status, msg = self.gitr.git_fetch()
        self.assertEqual((status, msg["status"]), (False, 2))

    def test_git_fetch_128(self):

        """Function:  test_git_fetch_128

        Description:  Test with raised exception - 128 status.

        Arguments:
            None

        """

        GIT = collections.namedtuple('GIT', 'fetch')
        self.gitr.gitcmd = GIT(fetch2)

        status, msg = self.gitr.git_fetch()
        self.assertEqual((status, msg["status"]), (False, 128))

    def test_git_fetch_true(self):

        """Function:  test_git_fetch_true

        Description:  Test with successful git_fetch call.

        Arguments:
            None

        """

        GIT = collections.namedtuple('GIT', 'fetch')
        self.gitr.gitcmd = GIT(fetch)

        status, msg = self.gitr.git_fetch()
        self.assertEqual((status, msg), (True, {}))


if __name__ == "__main__":
    unittest.main()
