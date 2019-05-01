#!/usr/bin/python
# Classification (U)

"""Program:  gitmerge_get_dirty.py

    Description:  Unit testing of gitmerge.get_dirty in git_class.py.

    Usage:
        test/unit/git_class/gitmerge_get_dirty.py

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


class Index(object):

    """Class:  Index

    Description:  Class stub holder for git.gitrepo.index.

    Methods:
        __init -> Class initilization.

    """

    def __init__(self):

        """Function:  __init__

        Description:  Initialization of class instance.

        Arguments:
            None

        """

        pass


class Diff(Index):

    """Class:  Diff

    Description:  Class stub holder for git.gitrepo.index.diff.

    Methods:
        __init -> Class initilization.

    """

    def __init__(self, test_type):

        """Function:  __init__

        Description:  Initialization of class instance.

        Arguments:
            test_type -> Determine type of test to be created.

        """

        super(Diff, self).__init__()

        self.test_type = test_type

    def diff(self, arg1):

        """Method:  diff

        Description:  Method stub holder for git.gitrepo.index.diff().

        Arguments:
            arg1 -> Stub holder.

        """

        INDEX = collections.namedtuple('INDEX', 'a_path change_type')

        if self.test_type == 1:
            file_list = []
            file_list.append(INDEX('file1', 'D'))
            file_list.append(INDEX('file2', 'M'))

        elif self.test_type == 2:
            file_list = []
            file_list.append(INDEX('file2', 'M'))

        elif self.test_type == 3:
            file_list = []
            file_list.append(INDEX('file1', 'D'))

        elif self.test_type == 4:
            file_list = []

        return file_list


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Unit testing initilization.
        test_all_lists -> Test with all attributes have a list.
        test_chgfiles_list -> Test with chg_files has a list.
        test_rmfiles_list -> Test with rm_files has a list.
        test_all_empty -> Test with all attributes are empty lists.

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
        self.rm_files = []
        self.chg_files = []

        self.gitr = git_class.GitMerge(self.repo_name, self.git_dir, self.url,
                                       self.branch, self.mod_branch)

        self.chk_list1 = []
        self.chk_list2 = ["file1"]
        self.chk_list3 = ["file2"]

    def test_all_lists(self):

        """Function:  test_all_lists

        Description:  Test with all attributes have a list.

        Arguments:
            None

        """

        GIT = collections.namedtuple('GIT', 'index')
        DIFF = Diff(1)
        self.gitr.gitrepo = GIT(DIFF)

        self.gitr.get_dirty()

        self.assertEqual((self.gitr.rm_files, self.gitr.chg_files),
                         (self.chk_list2, self.chk_list3))

    def test_chgfiles_list(self):

        """Function:  test_chgfiles_list

        Description:  Test with chg_files has a list.

        Arguments:
            None

        """

        GIT = collections.namedtuple('GIT', 'index')
        DIFF = Diff(2)
        self.gitr.gitrepo = GIT(DIFF)

        self.gitr.get_dirty()

        self.assertEqual((self.gitr.rm_files, self.gitr.chg_files),
                         (self.chk_list1, self.chk_list3))

    def test_rmfiles_list(self):

        """Function:  test_rmfiles_list

        Description:  Test with rm_files has a list.

        Arguments:
            None

        """

        GIT = collections.namedtuple('GIT', 'index')
        DIFF = Diff(3)
        self.gitr.gitrepo = GIT(DIFF)

        self.gitr.get_dirty()

        self.assertEqual((self.gitr.rm_files, self.gitr.chg_files),
                         (self.chk_list2, self.chk_list1))

    def test_all_empty(self):

        """Function:  test_all_empty

        Description:  Test with all attributes are empty lists.

        Arguments:
            None

        """

        GIT = collections.namedtuple('GIT', 'index')
        DIFF = Diff(4)
        self.gitr.gitrepo = GIT(DIFF)

        self.gitr.get_dirty()

        self.assertEqual((self.gitr.rm_files, self.gitr.chg_files),
                         (self.chk_list1, self.chk_list1))


if __name__ == "__main__":
    unittest.main()
