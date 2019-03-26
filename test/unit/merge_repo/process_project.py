#!/usr/bin/python
# Classification (U)

"""Program:  process_project.py

    Description:  Unit testing of process_project in merge_repo.py.

    Usage:
        test/unit/merge_repo/process_project.py

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


class GitCmd(object):

    """Class:  GitCmd

    Description:  Class stub holder for GitCmd class.

    Super-Class:  None

    Sub-Classes:  None

    Methods:
        fetch -> Stub holder for fetch method.
        branch -> Stub holder for branch method.
        checkout -> Stub holder for checkout method.
        merge -> Stub holder for merge method.
        push -> Stub holder for push method.

    """

    def fetch(self):

        """Method:  fetch

        Description:  Stub holder for fetch method.

        Arguments:
                None

        """

        return True

    def branch(self, arg1):

        """Method:  branch

        Description:  Stub holder for branch method.

        Arguments:
            (input) arg1 -> Stub holder for argument.

        """

        return True

    def checkout(self, arg1):

        """Method:  checkout

        Description:  Stub holder for checkout method.

        Arguments:
            (input) arg1 -> Stub holder for argument.

        """

        return True

    def merge(self, arg1, arg2, arg3, arg4, arg5, arg6):

        """Method:  merge

        Description:  Stub holder for merge method.

        Arguments:
            (input) arg1 -> Stub holder for argument.
            (input) arg2 -> Stub holder for argument.
            (input) arg3 -> Stub holder for argument.
            (input) arg4 -> Stub holder for argument.
            (input) arg5 -> Stub holder for argument.
            (input) arg6 -> Stub holder for argument.

        """

        return True

    def push(self, arg1):

        """Method:  push

        Description:  Stub holder for push method.

        Arguments:
            (input) arg1 -> Stub holder for argument.

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Unit testing initilization.
        test_process_project -> Test test_process_project function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        self.branch = "test-master"
        self.gitcmd = GitCmd()

    def test_process_project(self):

        """Function:  test_process_project

        Description:  Test test_process_project function.

        Arguments:
            None

        """

        self.assertFalse(merge_repo.process_project(self.branch, self.gitcmd))


if __name__ == "__main__":
    unittest.main()

