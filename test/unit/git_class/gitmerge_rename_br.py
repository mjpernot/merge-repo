#!/usr/bin/python
# Classification (U)

"""Program:  gitmerge_rename_br.py

    Description:  Unit testing of gitmerge.rename_br in git_class.py.

    Usage:
        test/unit/git_class/gitmerge_rename_br.py

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


def branch2(branch):

    """Function:  fetch2

    Description:  Method stub holder for git.Repo.git.branch().

    Arguments:
        branch -> Stub holder.

    """

    raise git.exc.GitCommandError("git", 128, "stderr")


def branch(branch):

    """Function:  fetch

    Description:  Method stub holder for git.Repo.git.branch().

    Arguments:
        branch -> Stub holder.

    """

    pass


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Unit testing initilization.
        test_rename_br_branch -> Test with branch parameter passed.
        test_rename_br_exception -> Test with raised exception.
        test_rename_br_true -> Test with successful branch call.

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

    def test_rename_br_branch(self):

        """Function:  test_rename_br_branch

        Description:  Test with branch parameter passed.

        Arguments:
            None

        """

        GIT = collections.namedtuple('GIT', 'branch')
        self.gitr.gitcmd = GIT(branch)

        status, msg = self.gitr.rename_br(branch="New_Branch")
        self.assertEqual((status, msg), (True, {}))

    def test_rename_br_exception(self):

        """Function:  test_rename_br_exception

        Description:  Test with raised exception.

        Arguments:
            None

        """

        GIT = collections.namedtuple('GIT', 'branch')
        self.gitr.gitcmd = GIT(branch2)

        status, msg = self.gitr.rename_br()
        self.assertEqual((status, msg["status"]), (False, 128))

    def test_rename_br_true(self):

        """Function:  test_rename_br_true

        Description:  Test with successful branch call.

        Arguments:
            None

        """

        GIT = collections.namedtuple('GIT', 'branch')
        self.gitr.gitcmd = GIT(branch)

        status, msg = self.gitr.rename_br()
        self.assertEqual((status, msg), (True, {}))


if __name__ == "__main__":
    unittest.main()
