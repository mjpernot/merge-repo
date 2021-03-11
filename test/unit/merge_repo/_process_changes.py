#!/usr/bin/python
# Classification (U)

"""Program:  _process_changes.py

    Description:  Unit testing of _process_changes in merge_repo.py.

    Usage:
        test/unit/merge_repo/_process_changes.py

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

# Local
sys.path.append(os.getcwd())
import merge_repo
import version

__version__ = version.__version__


class GitMerge(object):

    """Class:  GitMerge

    Description:  Class which is a representation of GitMerge module.

    Methods:
        __init__ -> Initialize configuration environment.
        is_dirty -> Stub holder for the GitMerge.is_dirty method.
        is_untracked -> Stub holder for GitMerge.is_untracked method.
        process_dirty -> Stub holder for GitMerge.process_dirty method.
        process_untracked -> Stub GitMerge.process_untracked method.
        get_dirty -> Stub holder for the GitMerge.get_dirty method.
        get_untracked -> Stub holder for GitMerge.get_untracked method.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the GitMerge class.

        Arguments:

        """

        self.chg_files = []
        self.new_files = []
        self.rm_files = []
        self.repo_name = "Repo_Name"
        self.dirty = True
        self.untracked = True

    def is_dirty(self):

        """Method:  is_dirty

        Description:  Stub holder for the GitMerge.is_dirty method.

        Arguments:

        """

        return self.dirty

    def is_untracked(self):

        """Method:  is_untracked

        Description:  Stub holder for GitMerge.is_untracked method.

        Arguments:

        """

        return self.untracked

    def process_dirty(self, option):

        """Method:  process_dirty

        Description:  Stub holder for GitMerge.process_dirty method.

        Arguments:
            (input) option -> Stub holder for argument.

        """

        status = True

        if option:
            status = True

        return status

    def process_untracked(self, option):

        """Method:  process_untracked

        Description:  Stub holder GitMerge.process_untracked method.

        Arguments:
            (input) option -> Stub holder for argument.

        """

        status = True

        if option:
            status = True

        return status

    def get_dirty(self):

        """Method:  get_dirty

        Description:  Stub holder for the GitMerge.get_dirty method.

        Arguments:

        """

        return True

    def get_untracked(self):

        """Method:  get_untracked

        Description:  Stub holder for GitMerge.get_untracked method.

        Arguments:

        """

        return True


class CfgTest(object):

    """Class:  CfgTest

    Description:  Class which is a representation of a cfg module.

    Methods:
        __init__ -> Initialize configuration environment.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the CfgTest class.

        Arguments:

        """

        self.prefix = "git@"
        self.git_server = "domain"
        self.git_project = "project"
        self.work_dir = "/directory/work_dir"
        self.err_dir = "/directory/error_dir"
        self.archive_dir = "/directory/archive_dir"
        self.log_file = "/directory/log_dir/merge_repo.log"
        self.to_line = "name@domain"
        self.branch = "branch_name"
        self.mod_branch = "mod_branch"
        self.name = "gituser"
        self.email = "gituser@domain.mail"


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Unit testing initilization.
        test_both_true -> Test with untrack and dirty set to True.
        test_is_untracked_true -> Test untrack set to True and dirty to False.
        test_is_dirty_true -> Test with dirty set to True and untrack to False.
        test_detach_head_false -> Test with detaching head returns False.
        test_detach_head_true -> Test with detaching head returns True.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.gitr = GitMerge()
        self.cfg = CfgTest()

    @mock.patch("merge_repo.process_changes", mock.Mock(return_value=True))
    @mock.patch("merge_repo.post_process", mock.Mock(return_value=True))
    @mock.patch("merge_repo.gen_class.Logger")
    def test_both_true(self, mock_log):

        """Function:  test_both_true

        Description:  Test with untrack and dirty set to True.

        Arguments:

        """

        self.gitr.dirty = True
        self.gitr.untracked = True

        mock_log.return_value = True

        self.assertFalse(merge_repo._process_changes(self.gitr, self.cfg,
                                                     mock_log))

    @mock.patch("merge_repo.process_changes", mock.Mock(return_value=True))
    @mock.patch("merge_repo.post_process", mock.Mock(return_value=True))
    @mock.patch("merge_repo.gen_class.Logger")
    def test_is_untracked_true(self, mock_log):

        """Function:  test_is_untracked_true

        Description:  Test untrack set to True and dirty to False.

        Arguments:

        """

        self.gitr.dirty = False
        self.gitr.untracked = True

        mock_log.return_value = True

        self.assertFalse(merge_repo._process_changes(self.gitr, self.cfg,
                                                     mock_log))

    @mock.patch("merge_repo.process_changes", mock.Mock(return_value=True))
    @mock.patch("merge_repo.post_process", mock.Mock(return_value=True))
    @mock.patch("merge_repo.gen_class.Logger")
    def test_is_dirty_true(self, mock_log):

        """Function:  test_is_dirty_true

        Description:  Test with dirty set to True and untrack to False.

        Arguments:

        """

        self.gitr.dirty = True
        self.gitr.untracked = False

        mock_log.return_value = True

        self.assertFalse(merge_repo._process_changes(self.gitr, self.cfg,
                                                     mock_log))

    @mock.patch("merge_repo.process_changes", mock.Mock(return_value=True))
    @mock.patch("merge_repo.process_project", mock.Mock(return_value=True))
    @mock.patch("merge_repo.post_process", mock.Mock(return_value=True))
    @mock.patch("merge_repo.detach_head")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_detach_head_false(self, mock_log, mock_head):

        """Function:  test_detach_head_false

        Description:  Test with detaching head returns False.

        Arguments:

        """

        self.gitr.dirty = False
        self.gitr.untracked = False

        mock_head.return_value = (False, "Error Message")
        mock_log.return_value = True

        self.assertFalse(merge_repo._process_changes(self.gitr, self.cfg,
                                                     mock_log))

    @mock.patch("merge_repo.process_project", mock.Mock(return_value=True))
    @mock.patch("merge_repo.process_changes", mock.Mock(return_value=True))
    @mock.patch("merge_repo.detach_head")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_detach_head_true(self, mock_log, mock_head):

        """Function:  test_detach_head_true

        Description:  Test with detaching head returns True.

        Arguments:

        """

        self.gitr.dirty = False
        self.gitr.untracked = False

        mock_head.return_value = (True, None)
        mock_log.return_value = True

        self.assertFalse(merge_repo._process_changes(self.gitr, self.cfg,
                                                     mock_log))


if __name__ == "__main__":
    unittest.main()
