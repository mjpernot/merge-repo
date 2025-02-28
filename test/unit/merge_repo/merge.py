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
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import merge_repo                               # pylint:disable=E0401,C0413
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class ArgParser(object):                                # pylint:disable=R0205

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        arg_exist
        get_val

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.cmdline = None
        self.args_array = {}

    def arg_exist(self, arg):

        """Method:  arg_exist

        Description:  Method stub holder for gen_class.ArgParser.arg_exist.

        Arguments:

        """

        return arg in self.args_array

    def get_val(self, skey, def_val=None):

        """Method:  get_val

        Description:  Method stub holder for gen_class.ArgParser.get_val.

        Arguments:

        """

        return self.args_array.get(skey, def_val)


class CfgTest(object):                          # pylint:disable=R0903,R0205

    """Class:  CfgTest

    Description:  Class which is a representation of a cfg module.

    Methods:
        __init__

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


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_allow_true
        test_no_email
        test_git_alias_option
        test_not_dirty
        test_detach_head_false
        test_detach_head_true
        test_second_check_false
        test_second_check_true
        test_is_remote_true
        test_is_remote_false
        test_is_git_repo_true
        test_is_git_repo_false

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.cfg = CfgTest()
        self.args = ArgParser()
        self.args.args_array = {
            "-c": "config_file", "-M": True,
            "-d": "/data/merge-repo/merge_repo/config", "-r": "repo-name",
            "-p": "/directory/repo-name"}

    @mock.patch("merge_repo.gen_libs.cp_dir", mock.Mock(return_value=True))
    @mock.patch("merge_repo.post_process", mock.Mock(return_value=True))
    @mock.patch("merge_repo.cleanup_repo", mock.Mock(return_value=True))
    @mock.patch("merge_repo.process_project", mock.Mock(return_value=True))
    @mock.patch("merge_repo.is_git_repo", mock.Mock(return_value=True))
    @mock.patch("merge_repo.detach_head")
    @mock.patch("merge_repo.gen_class.Logger")
    @mock.patch("merge_repo.git_class")
    @mock.patch("merge_repo.gen_libs")
    def test_allow_true(self, mock_lib, mock_git, mock_log, mock_head):

        """Function:  test_allow_true

        Description:  Test with allow option set to True.

        Arguments:

        """

        self.args.args_array["-u"] = True

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

    @mock.patch("merge_repo.gen_libs.cp_dir", mock.Mock(return_value=True))
    @mock.patch("merge_repo.gen_libs.mv_file2")
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

    @mock.patch("merge_repo.gen_libs.cp_dir", mock.Mock(return_value=True))
    @mock.patch("merge_repo.post_process")
    @mock.patch("merge_repo.git_class")
    @mock.patch("merge_repo.is_git_repo")
    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_git_alias_option(                          # pylint:disable=R0913
            self, mock_log, mock_lib, mock_isgit, mock_git, mock_post):

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
        self.args.args_array["-a"] = True

        self.assertFalse(merge_repo.merge(self.args, self.cfg, mock_log))

    @mock.patch("merge_repo.gen_libs.cp_dir", mock.Mock(return_value=True))
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

    @mock.patch("merge_repo.gen_libs.cp_dir", mock.Mock(return_value=True))
    @mock.patch("merge_repo.post_process", mock.Mock(return_value=True))
    @mock.patch("merge_repo.cleanup_repo", mock.Mock(return_value=True))
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

    @mock.patch("merge_repo.gen_libs.cp_dir", mock.Mock(return_value=True))
    @mock.patch("merge_repo.cleanup_repo", mock.Mock(return_value=True))
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

    @mock.patch("merge_repo.gen_libs.cp_dir", mock.Mock(return_value=True))
    @mock.patch("merge_repo.cleanup_repo", mock.Mock(return_value=True))
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

    @mock.patch("merge_repo.gen_libs.cp_dir", mock.Mock(return_value=True))
    @mock.patch("merge_repo.cleanup_repo")
    @mock.patch("merge_repo.post_process")
    @mock.patch("merge_repo.git_class")
    @mock.patch("merge_repo.is_git_repo")
    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_second_check_true(                         # pylint:disable=R0913
            self, mock_log, mock_lib, mock_isgit, mock_git, mock_post,
            mock_chg):

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

    @mock.patch("merge_repo.gen_libs.cp_dir", mock.Mock(return_value=True))
    @mock.patch("merge_repo.cleanup_repo")
    @mock.patch("merge_repo.post_process")
    @mock.patch("merge_repo.git_class")
    @mock.patch("merge_repo.is_git_repo")
    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_is_remote_true(                            # pylint:disable=R0913
            self, mock_log, mock_lib, mock_isgit, mock_git, mock_post,
            mock_chg):

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

    @mock.patch("merge_repo.gen_libs.cp_dir", mock.Mock(return_value=True))
    @mock.patch("merge_repo.post_process")
    @mock.patch("merge_repo.git_class")
    @mock.patch("merge_repo.is_git_repo")
    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_is_remote_false(                           # pylint:disable=R0913
            self, mock_log, mock_lib, mock_isgit, mock_git, mock_post):

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

    @mock.patch("merge_repo.gen_libs.cp_dir", mock.Mock(return_value=True))
    @mock.patch("merge_repo.post_process")
    @mock.patch("merge_repo.git_class")
    @mock.patch("merge_repo.is_git_repo")
    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_is_git_repo_true(                          # pylint:disable=R0913
            self, mock_log, mock_lib, mock_isgit, mock_git, mock_post):

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

    @mock.patch("merge_repo.gen_libs.cp_dir", mock.Mock(return_value=True))
    @mock.patch("merge_repo.gen_libs.mv_file2")
    @mock.patch("merge_repo.send_mail")
    @mock.patch("merge_repo.is_git_repo")
    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_is_git_repo_false(                         # pylint:disable=R0913
            self, mock_log, mock_lib, mock_isgit, mock_mail, mock_move):

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
