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

    def add(self, chg_files):

        """Method:  add

        Description:  Method stub holder for git.gitrepo.index.add().

        Arguments:
            chg_files -> Stub holder.

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
        test_process_all_true_revert -> Test all if statements True w/ revert.
        test_process_all_true_commit -> Test all if statements True w/ commit.
        test_process_all_true2 -> Test with all if statements are True.
        test_process_all_true -> Test with all if statements are True.
        test_chg_files_revert -> Test with chg_files passed with revert option.
        test_chg_files_commit -> Test with chg_files passed with commit option.
        test_chg_files_empty2 -> Test with chg_files passed as empty list.
        test_chg_files_empty -> Test with chg_files passed as empty list.
        test_rm_files_commit -> Test with rm_files passed with commit option.
        test_rm_files_revert -> Test with rm_files passed with revert option.
        test_rm_files_empty2 -> Test with rm_files passed as empty list.
        test_rm_files_empty -> Test with rm_files passed as empty list.

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

    def test_process_all_true_revert(self):

        """Function:  test_process_all_true_revert

        Description:  Test with all if statements are True with revert.

        Arguments:
            None

        """

        GIT = collections.namedtuple('GIT', 'index')
        DIFF = Diff(1)
        self.gitr.gitrepo = GIT(DIFF)

        self.gitr.process_dirty("revert")

        self.assertEqual((self.gitr.rm_files, self.gitr.chg_files),
                         (self.chk_list2, self.chk_list3))

    def test_process_all_true_commit(self):

        """Function:  test_process_all_true_commit

        Description:  Test with all if statements are True with commit.

        Arguments:
            None

        """

        GIT = collections.namedtuple('GIT', 'index')
        DIFF = Diff(1)
        self.gitr.gitrepo = GIT(DIFF)

        self.gitr.process_dirty("commit")

        self.assertEqual((self.gitr.rm_files, self.gitr.chg_files),
                         (self.chk_list2, self.chk_list3))

    def test_process_all_true2(self):

        """Function:  test_process_all_true

        Description:  Test with all if statements are True.

        Arguments:
            None

        """

        GIT = collections.namedtuple('GIT', 'index')
        DIFF = Diff(4)
        self.gitr.gitrepo = GIT(DIFF)

        self.gitr.process_dirty()

        self.assertEqual((self.gitr.rm_files, self.gitr.chg_files),
                         (self.chk_list1, self.chk_list1))

    def test_process_all_true(self):

        """Function:  test_process_all_true

        Description:  Test with all if statements are True.

        Arguments:
            None

        """

        GIT = collections.namedtuple('GIT', 'index')
        DIFF = Diff(1)
        self.gitr.gitrepo = GIT(DIFF)

        self.gitr.process_dirty()

        self.assertEqual((self.gitr.rm_files, self.gitr.chg_files),
                         (self.chk_list2, self.chk_list3))

    def test_chg_files_revert(self):

        """Function:  test_chg_files_revert

        Description:  Test with chg_files passed with revert option.

        Arguments:
            None

        """

        GIT = collections.namedtuple('GIT', 'index')
        DIFF = Diff(2)
        self.gitr.gitrepo = GIT(DIFF)

        self.gitr.process_dirty("revert")

        self.assertEqual(self.gitr.chg_files, self.chk_list3)

    def test_chg_files_commit(self):

        """Function:  test_chg_files_commit

        Description:  Test with chg_files passed with commit option.

        Arguments:
            None

        """

        GIT = collections.namedtuple('GIT', 'index')
        DIFF = Diff(2)
        self.gitr.gitrepo = GIT(DIFF)

        self.gitr.process_dirty("commit")

        self.assertEqual(self.gitr.chg_files, self.chk_list3)

    def test_chg_files_empty2(self):

        """Function:  test_chg_files_empty2

        Description:  Test with chg_files passed as empty list.

        Arguments:
            None

        """

        GIT = collections.namedtuple('GIT', 'index')
        DIFF = Diff(2)
        self.gitr.gitrepo = GIT(DIFF)

        self.gitr.process_dirty()

        self.assertEqual(self.gitr.chg_files, self.chk_list3)

    def test_chg_files_empty(self):

        """Function:  test_chg_files_empty

        Description:  Test with chg_files passed as empty list.

        Arguments:
            None

        """

        GIT = collections.namedtuple('GIT', 'index')
        DIFF = Diff(4)
        self.gitr.gitrepo = GIT(DIFF)

        self.gitr.process_dirty()

        self.assertEqual(self.gitr.chg_files, self.chk_list1)

    def test_rm_files_commit(self):

        """Function:  test_rm_files_commit

        Description:  Test with rm_files passed with commit option.

        Arguments:
            None

        """

        GIT = collections.namedtuple('GIT', 'index')
        DIFF = Diff(3)
        self.gitr.gitrepo = GIT(DIFF)

        self.gitr.process_dirty("commit")

        self.assertEqual(self.gitr.rm_files, self.chk_list2)

    def test_rm_files_revert(self):

        """Function:  test_rm_files_revert

        Description:  Test with rm_files passed with revert option.

        Arguments:
            None

        """

        GIT = collections.namedtuple('GIT', 'index')
        DIFF = Diff(3)
        self.gitr.gitrepo = GIT(DIFF)

        self.gitr.process_dirty("revert")

        self.assertEqual(self.gitr.rm_files, self.chk_list2)

    def test_rm_files_empty2(self):

        """Function:  test_rm_files_empty2

        Description:  Test with rm_files passed as empty list.

        Arguments:
            None

        """

        GIT = collections.namedtuple('GIT', 'index')
        DIFF = Diff(3)
        self.gitr.gitrepo = GIT(DIFF)

        self.gitr.process_dirty()

        self.assertEqual(self.gitr.rm_files, self.chk_list2)

    def test_rm_files_empty(self):

        """Function:  test_rm_files_empty

        Description:  Test with rm_files passed as empty list.

        Arguments:
            None

        """

        GIT = collections.namedtuple('GIT', 'index')
        DIFF = Diff(4)
        self.gitr.gitrepo = GIT(DIFF)

        self.gitr.process_dirty()

        self.assertEqual(self.gitr.rm_files, self.chk_list1)


if __name__ == "__main__":
    unittest.main()
