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

    def add(self):

        """Method:  add

        Description:  Stub holder for add method.

        Arguments:
            None

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
