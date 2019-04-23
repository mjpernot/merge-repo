#!/usr/bin/python
# Classification (U)

"""Program:  is_git_repo.py

    Description:  Unit testing of merge in is_git_repo.py.

    Usage:
        test/unit/merge_repo/is_git_repo.py

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


class Repo(object):

    """Class:  Repo

    Description:  Class stub holder for repo class.

    Super-Class:  None

    Sub-Classes:  None

    Methods:
        __init__ -> Class initilization.

    """

    def __init__(self, arg1):

        """Method:  __init__

        Description:  Initialization instance of the Repo class.

        Arguments:
            (input) arg1 -> Stub holder for argument.

        """

        self.git_dir = "Directory Path"


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Unit testing initilization.
        test_is_git_repo -> Test is_git_repo function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        self.path = "Dir_Path"

    @mock.patch("merge_repo.git")
    def test_is_git_repo(self, mock_git):

        """Function:  test_is_git_repo

        Description:  Test is_git_repo function.

        Arguments:
            None

        """

        mock_git.return_value = Repo(self.path)

        self.assertTrue(merge_repo.is_git_repo(self.path))


if __name__ == "__main__":
    unittest.main()
