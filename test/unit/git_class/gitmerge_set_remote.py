#!/usr/bin/python
# Classification (U)

"""Program:  gitmerge_set_remote.py

    Description:  Unit testing of gitmerge.set_remote in git_class.py.

    Usage:
        test/unit/git_class/gitmerge_set_remote.py

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
import collections

# Local
sys.path.append(os.getcwd())
import git_class
import lib.gen_libs as gen_libs
import version

# Version
__version__ = version.__version__


def remote(arg1, arg2, arg3):

    """Function:  remote

    Description:  Method stub holder for git.Repo.git.remote().

    Arguments:
        arg1 -> Stub holder for option "set-url".
        arg2 -> Stub holder for remote "origin".
        arg3 -> Stub holder for URL address.

    """

    pass


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Unit testing initilization.
        test_set_remote -> Test with default values settings.

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

    def test_set_remote(self):

        """Function:  test_set_remote

        Description:  Test with default values settings.

        Arguments:
            None

        """

        GIT = collections.namedtuple('GIT', 'remote')
        self.gitr.gitcmd = GIT(remote)

        self.assertFalse(self.gitr.set_remote())


if __name__ == "__main__":
    unittest.main()
