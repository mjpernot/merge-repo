#!/usr/bin/python
# Classification (U)

"""Program:  gitmerge_is_remote.py

    Description:  Unit testing of gitmerge.is_remote in git_class.py.

    Usage:
        test/unit/git_class/gitmerge_is_remote.py

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


def ls_remote2(arg1):

    """Function:  ls_remote2

    Description:  Method stub holder for git.Repo.git.ls_remote().

    Arguments:
        arg1 -> Stub holder for URL address.

    """

    raise git.exc.GitCommandError('git', 128)


def ls_remote(arg1):

    """Function:  ls_remote

    Description:  Method stub holder for git.Repo.git.ls_remote().

    Arguments:
        arg1 -> Stub holder for URL address.

    """

    pass


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Unit testing initilization.
        test_is_remote_false -> Test with exception raised from ls_remote call.
        test_is_remote_true -> Test with successful ls_remote call.

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

    def test_is_remote_false(self):

        """Function:  test_is_remote_false

        Description:  Test with exception raised from ls_remote call.

        Arguments:
            None

        """

        GIT = collections.namedtuple('GIT', 'ls_remote')
        self.gitr.gitcmd = GIT(ls_remote2)

        self.assertFalse(self.gitr.is_remote())

    def test_is_remote_true(self):

        """Function:  test_is_remote_true

        Description:  Test with successful ls_remote call.

        Arguments:
            None

        """

        GIT = collections.namedtuple('GIT', 'ls_remote')
        self.gitr.gitcmd = GIT(ls_remote)

        self.assertTrue(self.gitr.is_remote())


if __name__ == "__main__":
    unittest.main()
