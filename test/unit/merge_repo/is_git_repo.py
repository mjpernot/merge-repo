# Classification (U)

"""Program:  is_git_repo.py

    Description:  Unit testing of merge in is_git_repo.py.

    Usage:
        test/unit/merge_repo/is_git_repo.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import merge_repo                               # pylint:disable=E0401,C0413
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class Repo(object):                             # pylint:disable=R0903,R0205

    """Class:  Repo

    Description:  Class stub holder for repo class.

    Methods:
        __init__

    """

    def __init__(self, arg1):

        """Method:  __init__

        Description:  Initialization instance of the Repo class.

        Arguments:

        """

        self.git_dir = "Directory Path"
        self.arg1 = arg1


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_is_git_repo

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.path = "Dir_Path"

    @mock.patch("merge_repo.git")
    def test_is_git_repo(self, mock_git):

        """Function:  test_is_git_repo

        Description:  Test is_git_repo function.

        Arguments:

        """

        mock_git.return_value = Repo(self.path)

        self.assertTrue(merge_repo.is_git_repo(self.path))


if __name__ == "__main__":
    unittest.main()
