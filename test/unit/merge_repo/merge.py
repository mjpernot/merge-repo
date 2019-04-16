#!/usr/bin/python
# Classification (U)

"""Program:  merge.py

    Description:  Unit testing of merge in merge_repo.py.

    Usage:
        test/unit/merge_repo/merge.py

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
import merge_repo
import lib.gen_libs as gen_libs
import version

# Version
__version__ = version.__version__


class GitMerge(object):

    """Class:  GitMerge

    Description:  Class stub holder for GitMerge class.

    Super-Class:  None

    Sub-Classes:  None

    Methods:
        __init__ -> Class initilization.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the Repo class.

        Arguments:
                None

        """

        self.name = "Name Holder"

    def create_gitrepo(self):
        val = True
        return val


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Unit testing initilization.
        test_not_dirty -> Test with no dirty files found.
        test_second_check_false -> Test with second check set to False.
        test_second_check_true -> Test with second check set to True.
        test_is_untracked_true -> Test with is_untracked set to True.
        test_is_dirty_true -> Test with is_dirty set to True.
        test_is_remote_true -> Test with is_remote set to True.
        test_is_remote_false -> Test with is_remote set to False.
        test_is_git_repo_false -> Test with is_git_repo set to False.
        test_is_git_repo_true -> Test with is_git_repo set to True.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        class CfgTest(object):

            """Class:  CfgTest

            Description:  Class which is a representation of a cfg module.

            Super-Class:  object

            Sub-Classes:  None

            Methods:
                __init__ -> Initialize configuration environment.

            """

            def __init__(self):

                """Method:  __init__

                Description:  Initialization instance of the CfgTest class.

                Arguments:
                        None

                """

                self.url = "git@domain:project/"
                self.work_dir = "/directory/work_dir"
                self.err_dir = "/directory/error_dir"
                self.archive_dir = "/directory/archive_dir"
                self.log_file = "/directory/log_dir/merge_repo.log"
                self.to_line = "name@domain"
                self.branch = "branch_name"
                self.mod_branch = "mod_branch"

        self.cfg = CfgTest()
        self.args = {"-c": "config_file", "-d": "/directory/merge_repo/config",
                     "-r": "repo-name", "-p": "/directory/repo-name",
                     "-M": True}

    @unittest.skip("Done")
    @mock.patch("merge_repo.process_project")
    @mock.patch("merge_repo.git_class.GitMerge")
    @mock.patch("merge_repo.git_class")
    @mock.patch("merge_repo.is_git_repo")
    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_not_dirty(self, mock_log, mock_lib, mock_isgit, mock_gitc,
                       mock_gitr, mock_proj):

        """Function:  test_not_dirty

        Description:  Test with no dirty files found.

        Arguments:
            None

        """

        mock_log.return_value = True
        mock_lib.mv_file2.return_value = True
        mock_isgit.return_value = True
        mock_gitc.return_value = True
        mock_gitr.create_gitrepo.return_value = True
        mock_gitr.set_remote.return_value = True
        mock_gitr.is_remote.return_value = True
        mock_gitr.is_dirty.side_effect = [False, False]
        mock_gitr.is_untracked.side_effect = [False, False]
        mock_proj.return_value = True

        self.assertFalse(merge_repo.merge(self.args, self.cfg, mock_log))

    @unittest.skip("Done")
    @mock.patch("merge_repo.process_project")
    @mock.patch("merge_repo.git_class.GitMerge")
    @mock.patch("merge_repo.git_class")
    @mock.patch("merge_repo.is_git_repo")
    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_second_check_false(self, mock_log, mock_lib, mock_isgit,
                                mock_gitc, mock_gitr, mock_proj):

        """Function:  test_second_check_false

        Description:  Test with second check set to False.

        Arguments:
            None

        """

        mock_log.return_value = True
        mock_lib.mv_file2.return_value = True
        mock_isgit.return_value = True
        mock_gitc.return_value = True
        mock_gitr.create_gitrepo.return_value = True
        mock_gitr.set_remote.return_value = True
        mock_gitr.is_remote.return_value = True
        mock_gitr.is_dirty.return_value = False
        mock_gitr.is_untracked.return_value = False
        #mock_gitr.is_dirty.side_effect = [False, False]
        #mock_gitr.is_untracked.side_effect = [False, False]
        mock_gitr.process_dirty.return_value = True
        mock_gitr.process_untracked.return_value = True
        mock_proj.return_value = True

        self.assertFalse(merge_repo.merge(self.args, self.cfg, mock_log))

    @unittest.skip("Done")
    @mock.patch("merge_repo.post_process")
    @mock.patch("merge_repo.git_class.GitMerge")
    @mock.patch("merge_repo.git_class")
    @mock.patch("merge_repo.is_git_repo")
    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_second_check_true(self, mock_log, mock_lib, mock_isgit, mock_gitc,
                               mock_gitr, mock_post):

        """Function:  test_second_check_true

        Description:  Test with second check set to True.

        Arguments:
            None

        """

        mock_log.return_value = True
        mock_lib.mv_file2.return_value = True
        mock_isgit.return_value = True
        mock_gitc.return_value = True
        mock_gitr.create_gitrepo.return_value = True
        mock_gitr.set_remote.return_value = True
        mock_gitr.is_remote.return_value = True
        mock_gitr.is_dirty.side_effect = [True, True]
        mock_gitr.is_untracked.side_effect = [True, True]
        mock_gitr.process_dirty.return_value = True
        mock_gitr.process_untracked.return_value = True
        mock_post.return_value = True

        self.assertFalse(merge_repo.merge(self.args, self.cfg, mock_log))

    @unittest.skip("Done")
    @mock.patch("merge_repo.post_process")
    @mock.patch("merge_repo.git_class.GitMerge")
    @mock.patch("merge_repo.git_class")
    @mock.patch("merge_repo.is_git_repo")
    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_is_untracked_true(self, mock_log, mock_lib, mock_isgit, mock_gitc,
                               mock_gitr, mock_post):

        """Function:  test_is_untracked_true

        Description:  Test with is_untracked set to True.

        Arguments:
            None

        """

        mock_log.return_value = True
        mock_lib.mv_file2.return_value = True
        mock_isgit.return_value = True
        mock_gitc.return_value = True
        mock_gitr.create_gitrepo.return_value = True
        mock_gitr.set_remote.return_value = True
        mock_gitr.is_remote.return_value = True
        mock_gitr.is_dirty.side_effect = [True, True]
        mock_gitr.is_untracked.side_effect = [True, True]
        mock_gitr.process_dirty.return_value = True
        mock_gitr.process_untracked.return_value = True
        mock_post.return_value = True

        self.assertFalse(merge_repo.merge(self.args, self.cfg, mock_log))

    @unittest.skip("Done")
    @mock.patch("merge_repo.post_process")
    @mock.patch("merge_repo.git_class.GitMerge")
    @mock.patch("merge_repo.git_class")
    @mock.patch("merge_repo.is_git_repo")
    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_is_dirty_true(self, mock_log, mock_lib, mock_isgit, mock_gitc,
                           mock_gitr, mock_post):

        """Function:  test_is_dirty_true

        Description:  Test with is_dirty set to True.

        Arguments:
            None

        """

        mock_log.return_value = True
        mock_lib.mv_file2.return_value = True
        mock_isgit.return_value = True
        mock_gitc.return_value = True
        mock_gitr.create_gitrepo.return_value = True
        mock_gitr.set_remote.return_value = True
        mock_gitr.is_remote.return_value = True
        mock_gitr.is_dirty.side_effect = [True, True]
        mock_gitr.is_untracked.side_effect = [False, True]
        mock_gitr.process_dirty.return_value = True
        mock_gitr.process_untracked.return_value = True
        mock_post.return_value = True

        self.assertFalse(merge_repo.merge(self.args, self.cfg, mock_log))

    @unittest.skip("Done")
    @mock.patch("merge_repo.post_process")
    @mock.patch("merge_repo.git_class.GitMerge")
    @mock.patch("merge_repo.git_class")
    @mock.patch("merge_repo.is_git_repo")
    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_is_remote_true(self, mock_log, mock_lib, mock_isgit, mock_gitc,
                            mock_gitr, mock_post):

        """Function:  test_is_remote_true

        Description:  Test with is_remote set to True.

        Arguments:
            None

        """

        mock_log.return_value = True
        mock_lib.mv_file2.return_value = True
        mock_isgit.return_value = True
        mock_gitc.return_value = True
        mock_gitr.create_gitrepo.return_value = True
        mock_gitr.set_remote.return_value = True
        mock_gitr.is_remote.return_value = True
        mock_gitr.is_dirty.side_effect = [False, True]
        mock_gitr.is_untracked.side_effect = [False, True]
        mock_post.return_value = True

        self.assertFalse(merge_repo.merge(self.args, self.cfg, mock_log))

    @unittest.skip("Done")
    @mock.patch("merge_repo.post_process")
    @mock.patch("merge_repo.git_class.GitMerge")
    @mock.patch("merge_repo.git_class")
    @mock.patch("merge_repo.is_git_repo")
    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_is_remote_false(self, mock_log, mock_lib, mock_isgit, mock_gitc,
                             mock_gitr, mock_post):

        """Function:  test_is_remote_false

        Description:  Test with is_remote set to False.

        Arguments:
            None

        """

        mock_log.return_value = True
        mock_lib.mv_file2.return_value = True
        mock_isgit.return_value = True
        mock_gitc.return_value = True
        mock_gitr.create_gitrepo.return_value = True
        mock_gitr.set_remote.return_value = True
        mock_gitr.is_remote.return_value = False
        mock_post.return_value = True

        self.assertFalse(merge_repo.merge(self.args, self.cfg, mock_log))

    @unittest.skip("Done")
    @mock.patch("merge_repo.post_process")
    @mock.patch("merge_repo.git_class")
    @mock.patch("merge_repo.is_git_repo")
    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_is_git_repo_true(self, mock_log, mock_lib, mock_isgit,
                              mock_git, mock_post):

        """Function:  test_is_git_repo_true

        Description:  Test with is_git_repo set to True.

        Arguments:
            None

        """

        mock_log.return_value = True
        mock_lib.mv_file2.return_value = True
        mock_isgit.return_value = True
        mock_git.GitMerge.return_value = merge_repo.git_class.GitMerge
        mock_git.GitMerge.create_gitrepo.return_value = False
        mock_git.GitMerge.set_remote.return_value = True
        mock_git.GitMerge.is_remote.return_value = False
        mock_post.return_value = True

        self.assertFalse(merge_repo.merge(self.args, self.cfg, mock_log))

    @unittest.skip("Done")
    @mock.patch("merge_repo.post_process")
    @mock.patch("merge_repo.move")
    @mock.patch("merge_repo.send_mail")
    @mock.patch("merge_repo.is_git_repo")
    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_is_git_repo_false(self, mock_log, mock_lib, mock_isgit, mock_mail,
                               mock_move, mock_post):

        """Function:  test_is_git_repo_false

        Description:  Test with is_git_repo set to False.

        Arguments:
            None

        """

        mock_log.return_value = True
        mock_lib.mv_file2.return_value = True
        mock_isgit.return_value = False
        mock_mail.return_value = True
        mock_move.return_value = True

        self.assertFalse(merge_repo.merge(self.args, self.cfg, mock_log))


if __name__ == "__main__":
    unittest.main()
