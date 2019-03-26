#!/usr/bin/python
# Classification (U)

"""Program:  process_dirty.py

    Description:  Unit testing of merge in process_dirty.py.

    Usage:
        test/unit/merge_repo/process_dirty.py

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
        diff -> Stub holder for diff method.

    """

    def commit(self, arg1):

        """Method:  commit

        Description:  Stub holder for commit method.

        Arguments:
            (input) arg1 -> Stub holder for argument.

        """

        return True

    def diff(self, arg1):

        """Method:  diff

        Description:  Stub holder for diff method.

        Arguments:
            (input) arg1 -> Stub holder for argument.

        """

        CT = collections.namedtuple('CT', 'change_type')

        return [CT("D"), CT("M")]


class GitCmd(object):

    """Class:  GitCmd

    Description:  Class stub holder for GitCmd class.

    Super-Class:  None

    Sub-Classes:  None

    Methods:
        add -> Stub holder for add method.
        rm -> Stub holder for rm method.

    """

    def add(self, arg1):

        """Method:  add

        Description:  Stub holder for add method.

        Arguments:
            (input) arg1 -> Stub holder for argument.

        """

        return True

    def rm(self, arg1, working_tree):

        """Method:  rm

        Description:  Stub holder for rm method.

        Arguments:
            (input) arg1 -> Stub holder for argument.
            (input) working_tree -> Stub holder for argument.

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
        self.dirty = True

    def is_dirty(self):

        """Method:  is_dirty

        Description:  Stub holder for is_dirty method.

        Arguments:
            None

        """

        return self.dirty


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Unit testing initilization.
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

    def test_is_dirty_true(self):

        """Function:  test_is_dirty_true

        Description:  Test with is_dirty set to True.

        Arguments:
            None

        """

        self.assertFalse(merge_repo.process_dirty(self.gitrepo, self.gitcmd))

    def test_is_dirty_false(self):

        """Function:  test_is_dirty_false

        Description:  Test with is_dirty set to False.

        Arguments:
            None

        """

        self.gitrepo.dirty = False

        self.assertFalse(merge_repo.process_dirty(self.gitrepo, self.gitcmd))


if __name__ == "__main__":
    unittest.main()
