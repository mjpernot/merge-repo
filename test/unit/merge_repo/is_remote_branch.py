#!/usr/bin/python
# Classification (U)

"""Program:  is_remote_branch.py

    Description:  Unit testing of merge in is_remote_branch.py.

    Usage:
        test/unit/merge_repo/is_remote_branch.py

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

# Local
sys.path.append(os.getcwd())
import merge_repo
import lib.gen_libs as gen_libs
import version

# Version
__version__ = version.__version__


class GitCmd2(object):

    """Class:  GitCmd2

    Description:  Class stub holder for GitCmd class.

    Super-Class:  None

    Sub-Classes:  None

    Methods:
        rev_parse -> Stub holder for rev_parse method.

    """

    def rev_parse(self, arg1, arg2):

        """Method:  rev_parse

        Description:  Stub holder for rev_parse method.

        Arguments:
            (input) arg1 -> Stub holder for argument.
            (input) arg2 -> Stub holder for argument.
            (output) Return raised error for git.

        """

        raise git.exc.GitCommandError('git', 128)


class GitCmd(object):

    """Class:  GitCmd

    Description:  Class stub holder for GitCmd class.

    Super-Class:  None

    Sub-Classes:  None

    Methods:
        rev_parse -> Stub holder for rev_parse method.

    """

    def rev_parse(self, arg1, arg2):

        """Method:  rev_parse

        Description:  Stub holder for rev_parse method.

        Arguments:
            (input) arg1 -> Stub holder for argument.
            (input) arg2 -> Stub holder for argument.
            (output) True -> Successful git.rev_parse command.

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Unit testing initilization.
        test_is_remote_branch_fail -> Test function raising error.
        test_is_remote_branch -> Test is_remote_branch function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        self.gitcmd = GitCmd()
        self.gitcmd2 = GitCmd2()

    def test_is_remote_branch_fail(self):

        """Function:  test_is_remote_branch_fail

        Description:  Test is_remote_branch function raising error.

        Arguments:
            None

        """

        self.assertFalse(merge_repo.is_remote_branch(self.gitcmd2, "test-brh"))

    def test_is_remote_branch(self):

        """Function:  test_is_remote_branch

        Description:  Test is_remote_branch function.

        Arguments:
            None

        """

        self.assertTrue(merge_repo.is_remote_branch(self.gitcmd, "test-brh"))


if __name__ == "__main__":
    unittest.main()
