#!/usr/bin/python
# Classification (U)

"""Program:  is_remote.py

    Description:  Unit testing of merge in is_remote.py.

    Usage:
        test/unit/merge_repo/is_remote.py

    Arguments:

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

__version__ = version.__version__


class GitCmd2(object):

    """Class:  GitCmd2

    Description:  Class stub holder for GitCmd class.

    Methods:
        ls_remote -> Stub holder for ls_remote method.

    """

    def ls_remote(self, arg1):

        """Method:  rev_parse

        Description:  Stub holder for ls_remote method.

        Arguments:
            (input) arg1 -> Stub holder for argument.
            (output) Return raised error for git.

        """

        raise git.exc.GitCommandError('git', 128)


class GitCmd(object):

    """Class:  GitCmd

    Description:  Class stub holder for GitCmd class.

    Methods:
        ls_remote -> Stub holder for ls_remote method.

    """

    def ls_remote(self, arg1):

        """Method:  rev_parse

        Description:  Stub holder for ls_remote method.

        Arguments:
            (input) arg1 -> Stub holder for argument.
            (output) True -> Successful git.ls_remote command.

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Unit testing initilization.
        test_is_remote_fail -> Test is_remote function raising error.
        test_is_remote -> Test is_remote function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.gitcmd = GitCmd()
        self.gitcmd2 = GitCmd2()

    def test_is_remote_fail(self):

        """Function:  test_is_remote_fail

        Description:  Test is_remote function raising error.

        Arguments:

        """

        self.assertFalse(merge_repo.is_remote(self.gitcmd2, "url_address"))

    def test_is_remote(self):

        """Function:  test_is_remote

        Description:  Test is_remote function.

        Arguments:

        """

        self.assertTrue(merge_repo.is_remote(self.gitcmd, "url_address"))


if __name__ == "__main__":
    unittest.main()
