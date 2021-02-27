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


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Unit testing initilization.
        test_not_dirty -> Test with no dirty files found.
        test_detach_head_false -> Test with detaching head returns False.
        test_detach_head_true -> Test with detaching head returns True.
        test_second_check_false -> Test with second check set to False.
        test_second_check_true -> Test with second check set to True.
        test_is_remote_true -> Test with is_remote set to True.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

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

        self.gitr = GitMerge()
        self.cfg = CfgTest()

    @mock.patch("merge_repo.post_process", mock.Mock(return_value=True))
    @mock.patch("merge_repo.process_changes", mock.Mock(return_value=True))
    @mock.patch("merge_repo.is_git_repo", mock.Mock(return_value=True))
    @mock.patch("merge_repo.process_project", mock.Mock(return_value=True))
    @mock.patch("merge_repo.detach_head")
    @mock.patch("merge_repo.git_class")
    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_not_dirty(self, mock_log, mock_lib, mock_git, mock_head):

        """Function:  test_not_dirty

        Description:  Test with no dirty files found.

        Arguments:

        """

        mock_head.return_value = (True, None)
        mock_log.return_value = True
        mock_lib.mv_file2.return_value = True
        mock_git.GitConfig.return_value = merge_repo.git_class.GitConfig
        mock_git.GitConfig.set_user.return_value = True
        mock_git.GitConfig.set_email.return_value = True
        mock_git.GitMerge.return_value = merge_repo.git_class.GitMerge
        mock_git.GitMerge.create_gitrepo.return_value = True
        mock_git.GitMerge.set_remote.return_value = True
        mock_git.GitMerge.is_remote.return_value = True
        mock_git.GitMerge.is_dirty.side_effect = [False, False]
        mock_git.GitMerge.is_untracked.side_effect = [False, False]

        self.assertFalse(merge_repo._process_changes(self.gitr, self.cfg,
                                                     mock_log))

    @mock.patch("merge_repo.post_process", mock.Mock(return_value=True))
    @mock.patch("merge_repo.process_changes", mock.Mock(return_value=True))
    @mock.patch("merge_repo.process_project", mock.Mock(return_value=True))
    @mock.patch("merge_repo.is_git_repo", mock.Mock(return_value=True))
    @mock.patch("merge_repo.detach_head")
    @mock.patch("merge_repo.gen_class.Logger")
    @mock.patch("merge_repo.git_class")
    @mock.patch("merge_repo.gen_libs")
    def test_detach_head_false(self, mock_lib, mock_git, mock_log, mock_head):

        """Function:  test_detach_head_false

        Description:  Test with detaching head returns False.

        Arguments:

        """

        mock_head.return_value = (False, "Error Message")
        mock_log.return_value = True
        mock_lib.mv_file2.return_value = True
        mock_git.GitConfig.return_value = merge_repo.git_class.GitConfig
        mock_git.GitConfig.set_user.return_value = True
        mock_git.GitConfig.set_email.return_value = True
        mock_git.GitMerge.return_value = merge_repo.git_class.GitMerge
        mock_git.GitMerge.create_gitrepo.return_value = True
        mock_git.GitMerge.set_remote.return_value = True
        mock_git.GitMerge.is_remote.return_value = True
        mock_git.GitMerge.is_dirty.return_value = False
        mock_git.GitMerge.is_untracked.return_value = False
        mock_git.GitMerge.process_dirty.return_value = True
        mock_git.GitMerge.process_untracked.return_value = True

        self.assertFalse(merge_repo._process_changes(self.gitr, self.cfg,
                                                     mock_log))

    @mock.patch("merge_repo.post_process", mock.Mock(return_value=True))
    @mock.patch("merge_repo.process_changes", mock.Mock(return_value=True))
    @mock.patch("merge_repo.process_project", mock.Mock(return_value=True))
    @mock.patch("merge_repo.is_git_repo", mock.Mock(return_value=True))
    @mock.patch("merge_repo.detach_head")
    @mock.patch("merge_repo.gen_class.Logger")
    @mock.patch("merge_repo.git_class")
    @mock.patch("merge_repo.gen_libs")
    def test_detach_head_true(self, mock_lib, mock_git, mock_log, mock_head):

        """Function:  test_detach_head_true

        Description:  Test with detaching head returns True.

        Arguments:

        """

        mock_head.return_value = (True, None)
        mock_log.return_value = True
        mock_lib.mv_file2.return_value = True
        mock_git.GitConfig.return_value = merge_repo.git_class.GitConfig
        mock_git.GitConfig.set_user.return_value = True
        mock_git.GitConfig.set_email.return_value = True
        mock_git.GitMerge.return_value = merge_repo.git_class.GitMerge
        mock_git.GitMerge.create_gitrepo.return_value = True
        mock_git.GitMerge.set_remote.return_value = True
        mock_git.GitMerge.is_remote.return_value = True
        mock_git.GitMerge.is_dirty.return_value = False
        mock_git.GitMerge.is_untracked.return_value = False
        mock_git.GitMerge.process_dirty.return_value = True
        mock_git.GitMerge.process_untracked.return_value = True

        self.assertFalse(merge_repo._process_changes(self.gitr, self.cfg,
                                                     mock_log))

    @mock.patch("merge_repo.post_process", mock.Mock(return_value=True))
    @mock.patch("merge_repo.process_changes", mock.Mock(return_value=True))
    @mock.patch("merge_repo.process_project", mock.Mock(return_value=True))
    @mock.patch("merge_repo.is_git_repo", mock.Mock(return_value=True))
    @mock.patch("merge_repo.detach_head")
    @mock.patch("merge_repo.gen_class.Logger")
    @mock.patch("merge_repo.git_class")
    @mock.patch("merge_repo.gen_libs")
    def test_second_check_false(self, mock_lib, mock_git, mock_log, mock_head):

        """Function:  test_second_check_false

        Description:  Test with second check set to False.

        Arguments:

        """

        mock_head.return_value = (True, None)
        mock_log.return_value = True
        mock_lib.mv_file2.return_value = True
        mock_git.GitConfig.return_value = merge_repo.git_class.GitConfig
        mock_git.GitConfig.set_user.return_value = True
        mock_git.GitConfig.set_email.return_value = True
        mock_git.GitMerge.return_value = merge_repo.git_class.GitMerge
        mock_git.GitMerge.create_gitrepo.return_value = True
        mock_git.GitMerge.set_remote.return_value = True
        mock_git.GitMerge.is_remote.return_value = True
        mock_git.GitMerge.is_dirty.return_value = False
        mock_git.GitMerge.is_untracked.return_value = False
        mock_git.GitMerge.process_dirty.return_value = True
        mock_git.GitMerge.process_untracked.return_value = True

        self.assertFalse(merge_repo._process_changes(self.gitr, self.cfg,
                                                     mock_log))

    @mock.patch("merge_repo.process_changes")
    @mock.patch("merge_repo.post_process")
    @mock.patch("merge_repo.git_class")
    @mock.patch("merge_repo.is_git_repo")
    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_second_check_true(self, mock_log, mock_lib, mock_isgit, mock_git,
                               mock_post, mock_chg):

        """Function:  test_second_check_true

        Description:  Test with second check set to True.

        Arguments:

        """

        mock_log.return_value = True
        mock_lib.mv_file2.return_value = True
        mock_isgit.return_value = True
        mock_git.GitConfig.return_value = merge_repo.git_class.GitConfig
        mock_git.GitConfig.set_user.return_value = True
        mock_git.GitConfig.set_email.return_value = True
        mock_git.GitMerge.return_value = merge_repo.git_class.GitMerge
        mock_git.GitMerge.create_gitrepo.return_value = True
        mock_git.GitMerge.set_remote.return_value = True
        mock_git.GitMerge.is_remote.return_value = True
        mock_git.GitMerge.is_dirty.return_value = True
        mock_git.GitMerge.is_untracked.return_value = True
        mock_post.return_value = True
        mock_chg.return_value = True

        self.assertFalse(merge_repo._process_changes(self.gitr, self.cfg,
                                                     mock_log))

    @mock.patch("merge_repo.process_changes")
    @mock.patch("merge_repo.post_process")
    @mock.patch("merge_repo.git_class")
    @mock.patch("merge_repo.is_git_repo")
    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_is_remote_true(self, mock_log, mock_lib, mock_isgit, mock_git,
                            mock_post, mock_chg):

        """Function:  test_is_remote_true

        Description:  Test with is_remote set to True.

        Arguments:

        """

        mock_log.return_value = True
        mock_lib.mv_file2.return_value = True
        mock_isgit.return_value = True
        mock_git.GitMerge.return_value = merge_repo.git_class.GitMerge
        mock_git.create_gitrepo.return_value = True
        mock_git.GitConfig.return_value = merge_repo.git_class.GitConfig
        mock_git.GitConfig.set_user.return_value = True
        mock_git.GitConfig.set_email.return_value = True
        mock_git.GitMerge.set_remote.return_value = True
        mock_git.GitMerge.is_remote.return_value = True
        mock_git.GitMerge.is_dirty.return_value = True
        mock_git.GitMerge.is_untracked.return_value = True
        mock_post.return_value = True
        mock_chg.return_value = True

        self.assertFalse(merge_repo._process_changes(self.gitr, self.cfg,
                                                     mock_log))


if __name__ == "__main__":
    unittest.main()
