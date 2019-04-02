#!/usr/bin/python
# Classification (U)

"""Program:  is_remote.py

    Description:  Unit testing of merge in is_remote.py.

    Usage:
        test/unit/merge_repo/is_remote.py

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
        rev_parse -> Stub holder for rev_parse method.

    """

    def ls_remote(self, arg1):

        """Method:  rev_parse

        Description:  Stub holder for ls_remote method.

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
        test_is_remote -> Test is_remote function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        self.gitcmd = GitCmd()

    def test_is_remote(self):

        """Function:  test_is_remote

        Description:  Test is_remote function.

        Arguments:
            None

        """

        self.assertTrue(merge_repo.is_remote(self.gitcmd, "url_address"))


if __name__ == "__main__":
    unittest.main()
