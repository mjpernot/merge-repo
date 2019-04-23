#!/usr/bin/python
# Classification (U)

"""Program:  gitclass_create_repo.py

    Description:  Unit testing of GitClass.create_repo in git_class.py.

    Usage:
        test/unit/git_class/gitclass_create_repo.py

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
        test_default_arg -> Test with using default arguments.
        test_repodir_arg -> Test with passing repo_dir argument.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        self.gitc = git_class.GitClass()
        self.repo_dir = "/directory/git"

    @mock.patch("git_class.git")
    def test_repodir_arg(self, mock_git):

        """Function:  test_repodir_arg

        Description:  Test with passing repo_dir argument.

        Arguments:
            None

        """

        mock_git.Repo.return_value = "Git Class Instance"

        self.gitc.create_repo(self.repo_dir)

        self.assertEqual((self.gitc.gitrepo, self.gitc.gitcmd,
                          self.gitc.repo_dir),
                         ("Git Class Instance", None, self.repo_dir))

    @mock.patch("git_class.git")
    def test_default_arg(self, mock_git):

        """Function:  test_default_arg

        Description:  Test with using default arguments.

        Arguments:
            None

        """

        mock_git.Repo.return_value = "Git Class Instance"

        self.gitc.create_repo()

        self.assertEqual((self.gitc.gitrepo, self.gitc.gitcmd,
                          self.gitc.repo_dir),
                         ("Git Class Instance", None, "."))


if __name__ == "__main__":
    unittest.main()
