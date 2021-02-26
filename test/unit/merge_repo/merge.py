#!/usr/bin/python
# Classification (U)

"""Program:  merge.py

    Description:  Unit testing of merge in merge_repo.py.

    Usage:
        test/unit/merge_repo/merge.py

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
        test_no_email -> Test with no email notifications sent.
        test_git_alias_option -> Test with the git alias option set to True.
        test_not_dirty -> Test with no dirty files found.
        test_detach_head_false -> Test with detaching head returns False.
        test_detach_head_true -> Test with detaching head returns True.
        test_second_check_false -> Test with second check set to False.
        test_second_check_true -> Test with second check set to True.
        test_is_remote_true -> Test with is_remote set to True.
        test_is_remote_false -> Test with is_remote set to False.
        test_is_git_repo_false -> Test with is_git_repo set to False.
        test_is_git_repo_true -> Test with is_git_repo set to True.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

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
                self.work_dir = "/data/merge-repo/work_dir"
                self.err_dir = "/data/merge-repo/error_dir"
                self.archive_dir = "/data/merge-repo/archive_dir"
                self.log_file = "/data/merge-repo/log_dir/merge_repo.log"
                self.to_line = "name@domain"
                self.branch = "branch_name"
                self.mod_branch = "mod_branch"
                self.name = "gituser"
                self.email = "gituser@domain.mail"

        self.cfg = CfgTest()
        self.args = {"-c": "config_file", "-M": True,
                     "-d": "/data/merge-repo/merge_repo/config",
                     "-r": "repo-name", "-p": "/directory/repo-name"}

    @mock.patch("merge_repo.move")
    @mock.patch("merge_repo.is_git_repo")
    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_no_email(self, mock_log, mock_lib, mock_isgit, mock_move):

        """Function:  test_no_email

        Description:  Test with no email notifications sent.

        Arguments:

        """

        self.cfg.to_line = None

        mock_log.return_value = True
        mock_lib.mv_file2.return_value = True
        mock_isgit.return_value = False
        mock_move.return_value = True

        self.assertFalse(merge_repo.merge(self.args, self.cfg, mock_log))

    @mock.patch("merge_repo.post_process")
    @mock.patch("merge_repo.git_class")
    @mock.patch("merge_repo.is_git_repo")
    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_git_alias_option(self, mock_log, mock_lib, mock_isgit, mock_git,
                              mock_post):

        """Function:  test_git_alias_option

        Description:  Test with the git alias option set to True.

        Arguments:

        """

        mock_log.return_value = True
        mock_lib.mv_file2.return_value = True
        mock_isgit.return_value = True
        mock_git.GitConfig.return_value = merge_repo.git_class.GitConfig
        mock_git.GitConfig.set_user.return_value = True
        mock_git.GitConfig.set_email.return_value = True
        mock_git.GitMerge.return_value = merge_repo.git_class.GitMerge
        mock_git.GitMerge.create_gitrepo.return_value = False
        mock_git.GitMerge.set_remote.return_value = True
        mock_git.GitMerge.is_remote.return_value = False
        mock_post.return_value = True
        self.args["-a"] = True

        self.assertFalse(merge_repo.merge(self.args, self.cfg, mock_log))

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

        self.assertFalse(merge_repo.merge(self.args, self.cfg, mock_log))

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

        self.assertFalse(merge_repo.merge(self.args, self.cfg, mock_log))

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

        self.assertFalse(merge_repo.merge(self.args, self.cfg, mock_log))

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

        self.assertFalse(merge_repo.merge(self.args, self.cfg, mock_log))

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

        self.assertFalse(merge_repo.merge(self.args, self.cfg, mock_log))

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

        self.assertFalse(merge_repo.merge(self.args, self.cfg, mock_log))

    @mock.patch("merge_repo.post_process")
    @mock.patch("merge_repo.git_class")
    @mock.patch("merge_repo.is_git_repo")
    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_is_remote_false(self, mock_log, mock_lib, mock_isgit, mock_git,
                             mock_post):

        """Function:  test_is_remote_false

        Description:  Test with is_remote set to False.

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
        mock_git.GitMerge.is_remote.return_value = False
        mock_post.return_value = True

        self.assertFalse(merge_repo.merge(self.args, self.cfg, mock_log))

    @mock.patch("merge_repo.post_process")
    @mock.patch("merge_repo.git_class")
    @mock.patch("merge_repo.is_git_repo")
    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_is_git_repo_true(self, mock_log, mock_lib, mock_isgit, mock_git,
                              mock_post):

        """Function:  test_is_git_repo_true

        Description:  Test with is_git_repo set to True.

        Arguments:

        """

        mock_log.return_value = True
        mock_lib.mv_file2.return_value = True
        mock_isgit.return_value = True
        mock_git.GitConfig.return_value = merge_repo.git_class.GitConfig
        mock_git.GitConfig.set_user.return_value = True
        mock_git.GitConfig.set_email.return_value = True
        mock_git.GitMerge.return_value = merge_repo.git_class.GitMerge
        mock_git.GitMerge.create_gitrepo.return_value = False
        mock_git.GitMerge.set_remote.return_value = True
        mock_git.GitMerge.is_remote.return_value = False
        mock_post.return_value = True

        self.assertFalse(merge_repo.merge(self.args, self.cfg, mock_log))

    @mock.patch("merge_repo.move")
    @mock.patch("merge_repo.send_mail")
    @mock.patch("merge_repo.is_git_repo")
    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_is_git_repo_false(self, mock_log, mock_lib, mock_isgit, mock_mail,
                               mock_move):

        """Function:  test_is_git_repo_false

        Description:  Test with is_git_repo set to False.

        Arguments:

        """

        mock_log.return_value = True
        mock_lib.mv_file2.return_value = True
        mock_isgit.return_value = False
        mock_mail.return_value = True
        mock_move.return_value = True

        self.assertFalse(merge_repo.merge(self.args, self.cfg, mock_log))


if __name__ == "__main__":
    unittest.main()
