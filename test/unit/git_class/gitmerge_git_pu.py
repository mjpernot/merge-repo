#!/usr/bin/python
# Classification (U)

"""Program:  gitmerge_git_pu.py

    Description:  Unit testing of gitmerge.git_pu in git_class.py.

    Usage:
        test/unit/git_class/gitmerge_git_pu.py

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


def push3(option):

    """Function:  push3

    Description:  Method stub holder for git.Repo.git.push().

    Arguments:
        option -> Stub holder.

    """

    raise git.exc.GitCommandError("git", 2, "stderr")


def push2(option):

    """Function:  push2

    Description:  Method stub holder for git.Repo.git.push().

    Arguments:
        option -> Stub holder.

    """

    raise git.exc.GitCommandError("git", 128, "stderr")


def push(option):

    """Function:  push

    Description:  Method stub holder for git.Repo.git.push().

    Arguments:
        option -> Stub holder.

    """

    pass


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Unit testing initilization.
        test_git_pu_tags -> Test with passing tags option.
        test_git_pu_2 -> Test with raised exception - 2 status.
        test_git_pu_128 -> Test with raised exception - 128 status.
        test_git_pu_true -> Test with successful ls_remote call.

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

    def test_git_pu_tags(self):

        """Function:  test_git_pu_tags

        Description:  Test with passing tags option.

        Arguments:
            None

        """

        GIT = collections.namedtuple('GIT', 'push')
        self.gitr.gitcmd = GIT(push)

        status, msg = self.gitr.git_pu(tags=True)
        self.assertEqual((status, msg), (True, {}))

    def test_git_pu_2(self):

        """Function:  test_git_pu_2

        Description:  Test with raised exception - 2 status.

        Arguments:
            None

        """

        GIT = collections.namedtuple('GIT', 'push')
        self.gitr.gitcmd = GIT(push3)

        status, msg = self.gitr.git_pu()
        self.assertEqual((status, msg["status"]), (False, 2))

    def test_git_pu_128(self):

        """Function:  test_git_pu_128

        Description:  Test with raised exception - 128 status.

        Arguments:
            None

        """

        GIT = collections.namedtuple('GIT', 'push')
        self.gitr.gitcmd = GIT(push2)

        status, msg = self.gitr.git_pu()
        self.assertEqual((status, msg["status"]), (False, 128))

    def test_git_pu_true(self):

        """Function:  test_git_pu_true

        Description:  Test with successful git_pu call.

        Arguments:
            None

        """

        GIT = collections.namedtuple('GIT', 'push')
        self.gitr.gitcmd = GIT(push)

        status, msg = self.gitr.git_pu()
        self.assertEqual((status, msg), (True, {}))


if __name__ == "__main__":
    unittest.main()
