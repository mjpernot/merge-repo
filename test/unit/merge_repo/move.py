#!/usr/bin/python
# Classification (U)

"""Program:  move.py

    Description:  Unit testing of move in merge_repo.py.

    Usage:
        test/unit/merge_repo/move.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Third-party
import mock

# Local
sys.path.append(os.getcwd())
import merge_repo
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Unit testing initilization.
        test_move -> Test move function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.from_dir = "/From_directory"
        self.to_dir = "/To_directry"

    @mock.patch("merge_repo.gen_libs.mv_file2")
    def test_move(self, mock_move):

        """Function:  test_move

        Description:  Test move function.

        Arguments:

        """

        mock_move.return_value = True

        self.assertFalse(merge_repo.move(self.from_dir, self.to_dir))


if __name__ == "__main__":
    unittest.main()
