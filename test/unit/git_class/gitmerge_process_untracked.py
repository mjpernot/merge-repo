#!/usr/bin/python
# Classification (U)

"""Program:  gitmerge_process_untracked.py

    Description:  Unit testing of gitmerge.process_untracked in git_class.py.

    Usage:
        test/unit/git_class/gitmerge_process_untracked.py

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
import collections

# Local
sys.path.append(os.getcwd())
import git_class
import lib.gen_libs as gen_libs
import version

# Version
__version__ = version.__version__


class Index(object):

    """Class:  Index

    Description:  Class stub holder for git.gitrepo.index.

    Methods:
        __init -> Class initilization.

    """

    def __init__(self):

        """Function:  __init__

        Description:  Initialization of class instance.

        Arguments:
            None

        """

        pass


class Diff(Index):

    """Class:  Diff

    Description:  Class stub holder for git.gitrepo.index.diff.

    Methods:
        __init -> Class initilization.

    """

    def __init__(self):

        """Function:  __init__

        Description:  Initialization of class instance.

        Arguments:
            None

        """

        super(Diff, self).__init__()

    def add(self, new_files):

        """Method:  add

        Description:  Method stub holder for git.gitrepo.index.add().

        Arguments:
            new_files -> Stub holder.

        """

        return True

    def commit(self, msg):

        """Method:  commit

        Description:  Method stub holder for git.gitrepo.index.commit().

        Arguments:
            msg -> Stub holder.

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Unit testing initilization.
        test_process_all_false -> Test with all if statements are False.
        test_process_all_true -> Test with all if statements are True.

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

        self.gitr = git_class.GitMerge(self.repo_name, self.git_dir, self.url,
                                       self.branch, self.mod_branch)

    def test_process_all_false(self):

        """Function:  test_process_all_false

        Description:  Test with all if statements are False.

        Arguments:
            None

        """

        GIT = collections.namedtuple('GIT', 'index untracked_files')
        DIFF = Diff()
        self.gitr.gitrepo = GIT(DIFF, False)

        self.assertFalse(self.gitr.process_untracked())

    def test_process_all_true(self):

        """Function:  test_process_all_true

        Description:  Test with all if statements are True.

        Arguments:
            None

        """

        GIT = collections.namedtuple('GIT', 'index untracked_files')
        DIFF = Diff()
        self.gitr.gitrepo = GIT(DIFF, True)

        self.assertFalse(self.gitr.process_untracked())


if __name__ == "__main__":
    unittest.main()
