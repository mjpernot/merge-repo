#!/usr/bin/python
# Classification (U)

"""Program:  gitclass_init.py

    Description:  Unit testing of GitClass.__init__ in git_class.py.

    Usage:
        test/unit/git_class/gitclass_init.py

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
import git_class
import lib.gen_libs as gen_libs
import version

# Version
__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Unit testing initilization.
        test_repo_dir_set -> Test with repo_dir being set.
        test_init_default -> Test with default values set.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        self.repo_dir = "/repo/directory"

    def test_repo_dir_set(self):

        """Function:  test_repo_dir_set

        Description:  Test with repo_dir being set.

        Arguments:
            None

        """

        gitc = git_class.GitClass(self.repo_dir)

        self.assertEqual((gitc.gitrepo, gitc.gitcmd, gitc.repo_dir),
                         (None, None, self.repo_dir))

    def test_init_default(self):

        """Function:  test_init_default

        Description:  Test with default values set.

        Arguments:
            None

        """

        gitc = git_class.GitClass()

        self.assertEqual((gitc.gitrepo, gitc.gitcmd, gitc.repo_dir),
                         (None, None, "."))


if __name__ == "__main__":
    unittest.main()
