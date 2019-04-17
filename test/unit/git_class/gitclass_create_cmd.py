#!/usr/bin/python
# Classification (U)

"""Program:  gitclass_create_cmd.py

    Description:  Unit testing of GitClass.create_cmd in git_class.py.

    Usage:
        test/unit/git_class/gitclass_create_cmd.py

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
        test_repodir_not_set -> Test with repo_dir attribute not set.
        test_repodir_set -> Test with repo_dir attribute set.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        self.gitc = git_class.GitClass()

    def test_repodir_not_set(self):

        """Function:  test_repodir_not_set

        Description:  Test with repo_dir attribute not set.

        Arguments:
            None

        """

        self.gitc.create_cmd()

        self.assertEqual((self.gitc.gitcmd, self.gitc.repo_dir), (None, "."))

    def test_repodir_set(self):

        """Function:  test_repodir_set

        Description:  Test with repo_dir attribute set.

        Arguments:
            None

        """

        GIT = collections.namedtuple('GIT', 'git')
        self.gitc.gitrepo = GIT("Cmd Instance")

        self.gitc.create_cmd()

        self.assertEqual((self.gitc.gitcmd, self.gitc.repo_dir),
                         ("Cmd Instance", "."))


if __name__ == "__main__":
    unittest.main()
