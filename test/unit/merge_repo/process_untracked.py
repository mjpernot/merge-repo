#!/usr/bin/python
# Classification (U)

"""Program:  process_untracked.py

    Description:  Unit testing of merge in process_untracked.py.

    Usage:
        test/unit/merge_repo/process_untracked.py

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
import merge_repo
import lib.gen_libs as gen_libs
import version

# Version
__version__ = version.__version__


class Index(object):

    """Class:  Index

    Description:  Class stub holder for Index.

    Super-Class:  None

    Sub-Classes:  None

    Methods:
        commit -> Stub holder for commit method.

    """

    def commit(self, arg1):

        """Method:  commit

        Description:  Stub holder for commit method.

        Arguments:
            (input) arg1 -> Stub holder for argument.

        """

        return True


class GitCmd(object):

    """Class:  GitCmd

    Description:  Class stub holder for GitCmd class.

    Super-Class:  None

    Sub-Classes:  None

    Methods:
        add -> Stub holder for add method.

    """

    def add(self, arg1):

        """Method:  add

        Description:  Stub holder for add method.

        Arguments:
            (input) arg1 -> Stub holder for argument.

        """

        return True


class GitRepo(object):

    """Class:  GitRepo

    Description:  Class stub holder for GitRepo class.

    Super-Class:  None

    Sub-Classes:  None

    Methods:
        __init__ -> Class initialization.
        is_dirty -> Stub holder for is_dirty method.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:
            None

        """

        self.index = Index()
        self.untracked_files = []
        self.dirty = True

    def is_dirty(self, untracked_files):

        """Method:  is_dirty

        Description:  Stub holder for is_dirty method.

        Arguments:
            (input) arg1 -> Stub holder for argument.

        """

        return self.dirty


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Unit testing initilization.
        test_untracked_files -> Test with untracked_files filled.
        test_is_dirty_true -> Test with is_dirty set to True.
        test_is_dirty_false -> Test with is_dirty set to False.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        self.gitcmd = GitCmd()
        self.gitrepo = GitRepo()

    @mock.patch("merge_repo.git")
    def test_untracked_files(self, mock_git):

        """Function:  test_untracked_files

        Description:  Test with untracked_files filled.

        Arguments:
            mock_git -> Mock Ref:  merge_repo.git.Repo

        """

        self.gitrepo.untracked_files = ["File1", "File2"]

        self.assertFalse(merge_repo.process_untracked(self.gitrepo,
                                                      self.gitcmd))

    @mock.patch("merge_repo.git")
    def test_no_untracked_files(self, mock_git):

        """Function:  test_no_untracked_files

        Description:  Test with untracked_files empty.

        Arguments:
            mock_git -> Mock Ref:  merge_repo.git.Repo

        """

        self.assertFalse(merge_repo.process_untracked(self.gitrepo,
                                                      self.gitcmd))

    @mock.patch("merge_repo.git")
    def test_is_dirty_true(self, mock_git):

        """Function:  test_is_dirty_true

        Description:  Test with is_dirty set to True.

        Arguments:
            mock_git -> Mock Ref:  merge_repo.git.Repo

        """

        self.assertFalse(merge_repo.process_untracked(self.gitrepo,
                                                      self.gitcmd))

    @mock.patch("merge_repo.git")
    def test_is_dirty_false(self, mock_git):

        """Function:  test_is_dirty_false

        Description:  Test with is_dirty set to False.

        Arguments:
            mock_git -> Mock Ref:  merge_repo.git.Repo

        """

        self.assertFalse(merge_repo.process_untracked(self.gitrepo,
                                                      self.gitcmd))


if __name__ == "__main__":
    unittest.main()
