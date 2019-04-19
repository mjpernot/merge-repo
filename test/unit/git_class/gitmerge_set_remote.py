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

# Local
sys.path.append(os.getcwd())
import git_class
import lib.gen_libs as gen_libs
import version

# Version
__version__ = version.__version__


class TestGitClass(object):
    def __init__(self):
        pass

def remote2(arg1, arg2, arg3):
    pass

def remote():
    return remote2


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
        #self.gitc = git_class.GitClass(self.git_dir)
        #self.gitcmd = git_class.GitMerge()

    #@mock.patch("git_class.GitClass")
    #@mock.patch("git_class.GitMerge")
    def test_set_remote(self):

        """Function:  test_set_remote

        Description:  Test with default values settings.

        Arguments:
            None

        """

        import collections
        GIT = collections.namedtuple('GIT', 'remote')
        self.gitr.gitcmd = GIT(remote())
        print(self.gitr.gitcmd.remote)
        # It works, but not sure how as it is passing through remote() to
        #   remote2() which is accepting the arguments from
        #   self.gitcmd.remote("set-url", "origin", self.url) in GitMerge
        #   class.
        #  Need to test to see what is being set at each stage and then test
        #   it as the commands progress.
        #  NOTE:  Run 'git remote -v' as somehow the testing program changed
        #   the merge-repo git repo to TESTURL.
        #  To change it back:
        #git remote set-url origin git@gitlab.dicelab.net:JAC-IDM/merge-repo.git
        #  Make sure it's set to this before pushing anything.

        self.gitr.set_remote()
        #gits = TestGitClass()
        #mock_gitc.remote.return_value = gits
        #mock_gitc.return_value = self.gitr

        #self.assertFalse(self.gitr.set_remote())


if __name__ == "__main__":
    unittest.main()
