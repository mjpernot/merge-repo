#!/usr/bin/python
# Classification (U)

"""Program:  gitmerge_init.py

    Description:  Unit testing of gitmerge.__init__ in git_class.py.

    Usage:
        test/unit/git_class/gitmerge_init.py

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
        test_init_default -> Test with default values set.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        self.repo_name = "Repo_name"
        self.git_dir = "/directory/git"
        self.url = "URL"
        self.branch = "Remote_branch"
        self.mod_branch = "Mod_branch"

    def test_init_default(self):

        """Function:  test_init_default

        Description:  Test with default values set.

        Arguments:
            None

        """

        gitr = git_class.GitMerge(self.repo_name, self.git_dir, self.url,
                                  self.branch, self.mod_branch)

        self.assertEqual((gitr.git_dir, gitr.repo_name, gitr.url,
                          gitr.mod_branch, gitr.branch, gitr.remote_info,
                          gitr.br_commit),
                         (self.git_dir, self.repo_name, self.url,
                          self.mod_branch, gitr.branch, None, None))


if __name__ == "__main__":
    unittest.main()
