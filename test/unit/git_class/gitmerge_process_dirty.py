#!/usr/bin/python
# Classification (U)

"""Program:  gitmerge_process_dirty.py

    Description:  Unit testing of gitmerge.process_dirty in git_class.py.

    Usage:
        test/unit/git_class/gitmerge_process_dirty.py

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


def diff(arg1):

    """Function:  diff

    Description:  Method stub holder for git.Repo.index.diff().

    Arguments:
        arg1 -> Stub holder.

    """

    INDEX = collections.namedtuple('INDEX', 'a_path change_type')
    file_list = []
    file_list.append(INDEX('file1', 'D'))
    file_list.append(INDEX('file2', 'M'))

    return file_list


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Unit testing initilization.
        test_process_dirty_false -> Test with exception raised from ls_remote call.
        test_process_dirty_true -> Test with successful ls_remote call.

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

    @unittest.skip("Not done")
    def test_process_dirty_false(self):

        """Function:  test_process_dirty_false

        Description:  Test with exception raised from ls_remote call.

        Arguments:
            None

        """

        GIT = collections.namedtuple("GIT", "diff")
        self.gitr.gitrepo = GIT(diff)

        self.assertFalse(self.gitr.process_dirty())

    def test_process_dirty_true(self):

        """Function:  test_process_dirty_true

        Description:  Test with successful ls_remote call.

        Arguments:
            None

        """

        GIT = collections.namedtuple("GIT", "diff")
        INDEX = collections.namedtuple("GITR", "index")
        
        self.gitr.gitrepo = INDEX(index)

        self.assertTrue(self.gitr.process_dirty())


if __name__ == "__main__":
    unittest.main()
