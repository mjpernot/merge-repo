#!/usr/bin/python
# Classification (U)

"""Program:  gitmerge_is_dirty.py

    Description:  Unit testing of gitmerge.is_dirty in git_class.py.

    Usage:
        test/unit/git_class/gitmerge_is_dirty.py

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


def is_dirty2():

    """Function:  is_dirty2

    Description:  Method stub holder for git.Repo.git.is_dirty().

    Arguments:
        None

    """

    return False


def is_dirty():

    """Function:  is_dirty

    Description:  Method stub holder for git.Repo.git.is_dirty().

    Arguments:
        None

    """

    return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Unit testing initilization.
        test_is_dirty_false -> Test with is_dirty returns False.
        test_is_dirty_true -> Test with is_dirty returns True.

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

    def test_is_dirty_false(self):

        """Function:  test_is_dirty_false

        Description:  Test with is_dirty returns False.

        Arguments:
            None

        """

        GIT = collections.namedtuple('GIT', 'is_dirty')
        self.gitr.gitrepo = GIT(is_dirty2)

        self.assertFalse(self.gitr.is_dirty())

    def test_is_dirty_true(self):

        """Function:  test_is_dirty_true

        Description:  Test with is_dirty returns True.

        Arguments:
            None

        """

        GIT = collections.namedtuple('GIT', 'is_dirty')
        self.gitr.gitrepo = GIT(is_dirty)

        self.assertTrue(self.gitr.is_dirty())


if __name__ == "__main__":
    unittest.main()
