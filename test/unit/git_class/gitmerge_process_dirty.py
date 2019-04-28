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

    def remove(self, rm_files, working_tree):

        """Method:  remove

        Description:  Method stub holder for git.gitrepo.index.remove().

        Arguments:
            rm_files -> Stub holder.
            working_tree -> Stub holder.

        """

        return True

    def checkout(self, chg_files, force):

        """Method:  checkout

        Description:  Method stub holder for git.gitrepo.index.checkout().

        Arguments:
            chg_files -> Stub holder.
            force -> Stub holder.

        """

        return True

    def commit(self, msg):

        """Method:  commit

        Description:  Method stub holder for git.gitrepo.index.commit().

        Arguments:
            msg -> Stub holder.

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Unit testing initilization.
        test_process_all_false -> Test with all if statements are False.
        test_process_no_chgfiles -> Test with no chg_files present.
        test_process_no_rmfiles -> Test with no rm_files present.
        test_process_all_true -> Test with all if statements are True.
        test_chg_files_empty -> Test with chg_files is empty,
        test_rm_files_empty -> Test with rm_files is empty.

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

    def test_process_all_false(self):

        """Function:  test_process_all_false

        Description:  Test with all if statements are False.

        Arguments:
            None

        """

        GIT = collections.namedtuple('GIT', 'index')
        DIFF = Diff(4)
        self.gitr.gitrepo = GIT(DIFF)

        self.assertFalse(self.gitr.process_dirty())

    def test_process_no_chgfiles(self):

        """Function:  test_process_no_chgfiles

        Description:  Test with no chg_files present.

        Arguments:
            None

        """

        GIT = collections.namedtuple('GIT', 'index')
        DIFF = Diff(3)
        self.gitr.gitrepo = GIT(DIFF)

        self.assertFalse(self.gitr.process_dirty())

    def test_process_no_rmfiles(self):

        """Function:  test_process_no_rmfiles

        Description:  Test with no rm_files present.

        Arguments:
            None

        """

        GIT = collections.namedtuple('GIT', 'index')
        DIFF = Diff(2)
        self.gitr.gitrepo = GIT(DIFF)

        self.assertFalse(self.gitr.process_dirty())

    def test_process_all_true(self):

        """Function:  test_process_all_true

        Description:  Test with all if statements are True.

        Arguments:
            None

        """

        GIT = collections.namedtuple('GIT', 'index')
        DIFF = Diff(1)
        self.gitr.gitrepo = GIT(DIFF)

        self.assertFalse(self.gitr.process_dirty())

    def test_chg_files_empty(self):

        """Function:  test_chg_files_empty

        Description:  Test with chg_files is empty.

        Arguments:
            None

        """

        GIT = collections.namedtuple('GIT', 'index')
        DIFF = Diff(3)
        self.gitr.gitrepo = GIT(DIFF)

        self.assertFalse(self.gitr.process_dirty())

    def test_rm_files_empty(self):

        """Function:  test_rm_files_empty

        Description:  Test with rm_files is empty.

        Arguments:
            None

        """

        GIT = collections.namedtuple('GIT', 'index')
        DIFF = Diff(3)
        self.gitr.gitrepo = GIT(DIFF)

        self.assertFalse(self.gitr.process_dirty())


if __name__ == "__main__":
    unittest.main()
