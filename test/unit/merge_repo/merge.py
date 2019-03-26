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


class Url(object):

    """Class:  Url

    Description:  Class stub holder for url.

    Super-Class:  None

    Sub-Classes:  None

    Methods:
        __init__ -> Class initilization.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the Url class.

        Arguments:
                None

        """

        self.url = "Url_Location"


class Origin(object):

    """Class:  Origin

    Description:  Class stub holder for origin.

    Super-Class:  None

    Sub-Classes:  None

    Methods:
        __init__ -> Class initilization.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the Origin class.

        Arguments:
                None

        """

        self.origin = Url()


class Git(object):

    """Class:  Git

    Description:  Class stub holder for git class.

    Super-Class:  None

    Sub-Classes:  None

    Methods:
        remote -> Stub holder for remote method.

    """

    def remote(self, arg1, arg2, arg3):

        """Function:  remote

        Description:  Stub holder for remote method.

        Arguments:
            arg1 -> Arg stub holder.
            arg2 -> Arg stub holder.
            arg3 -> Arg stub holder.

        """

        pass


class Repo(object):

    """Class:  Repo

    Description:  Class stub holder for repo class.

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

        self.remotes = Origin()
        self.git = Git()


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Unit testing initilization.
        test_is_remote_branch_false -> Test with is_remote_branch set to False.
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

                self.url = "git@gitlab.code.dicelab.net:JAC-IDM/"
                self.work_dir = "/home/mark.j.pernot/merge/work_dir"
                self.err_dir = "/home/mark.j.pernot/merge/error_dir"
                self.archive_dir = "/home/mark.j.pernot/merge/archive_dir"
                self.log_file = \
                    "/home/mark.j.pernot/merge/log_dir/merge_repo.log"
                self.to_line = "Mark.J.Pernot@coe.ic.gov"
                self.branch = "master"

        self.cfg = CfgTest()

        self.args = {"-c": "config_file",
                     "-d": "/home/mark.j.pernot/merge_repo/config",
                     "-r": "repo-name",
                     "-p": "/home/mark.j.pernot/merge/repo-name", "-M": True}

    @mock.patch("merge_repo.process_project")
    @mock.patch("merge_repo.process_dirty")
    @mock.patch("merge_repo.process_untracked")
    @mock.patch("merge_repo.is_remote_branch")
    @mock.patch("merge_repo.git")
    @mock.patch("merge_repo.send_mail")
    @mock.patch("merge_repo.is_git_repo")
    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_is_remote_branch_true(self, mock_log, mock_libs, mock_isgit,
                                   mock_mail, mock_git, mock_isremote,
                                   mock_untrack, mock_dirty, mock_project):

        """Function:  test_is_remote_branch_true

        Description:  Test with is_remote_branch set to True.

        Arguments:
            mock_log -> Mock Ref:  merge_repo.gen_class.Logger
            mock_libs -> Mock Ref:  merge_repo.gen_libs
            mock_isgit -> Mock Ref:  merge_repo.is_git_repo
            mock_mail -> Mock Ref:  merge_repo.send_mail
            mock_git -> Mock Ref:  merge_repo.git.Repo
            mock_isremote -> Mock Reg:  merge_repo.is_remote_branch
            mock_untrack -> Mock Reg:  merge_repo.process_untracked
            mock_dirty -> Mock Reg:  merge_repo.process_dirty
            mock_project -> Mock Reg:  merge_repo.process_project

        """

        mock_log.return_value = True
        mock_libs.mv_file.return_value = True
        mock_isgit.return_value = True
        mock_mail.return_value = True
        mock_git.Repo.return_value = Repo()
        mock_isremote.return_value = True
        mock_untrack.return_value = True
        mock_dirty.return_value = True
        mock_project.return_value = True

        self.assertFalse(merge_repo.merge(self.args, self.cfg, mock_log))

    @mock.patch("merge_repo.is_remote_branch")
    @mock.patch("merge_repo.git")
    @mock.patch("merge_repo.send_mail")
    @mock.patch("merge_repo.is_git_repo")
    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_is_remote_branch_false(self, mock_log, mock_libs, mock_isgit,
                                    mock_mail, mock_git, mock_isremote):

        """Function:  test_is_remote_branch_false

        Description:  Test with is_remote_branch set to False.

        Arguments:
            mock_log -> Mock Ref:  merge_repo.gen_class.Logger
            mock_libs -> Mock Ref:  merge_repo.gen_libs
            mock_isgit -> Mock Ref:  merge_repo.is_git_repo
            mock_mail -> Mock Ref:  merge_repo.send_mail
            mock_git -> Mock Ref:  merge_repo.git.Repo
            mock_isremote -> Mock Reg:  merge_repo.is_remote_branch

        """

        mock_log.return_value = True
        mock_libs.mv_file.return_value = True
        mock_isgit.return_value = True
        mock_mail.return_value = True
        mock_git.Repo.return_value = Repo()
        mock_isremote.return_value = False

        self.assertFalse(merge_repo.merge(self.args, self.cfg, mock_log))

    @mock.patch("merge_repo.is_remote_branch")
    @mock.patch("merge_repo.git")
    @mock.patch("merge_repo.send_mail")
    @mock.patch("merge_repo.is_git_repo")
    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_is_git_repo_true(self, mock_log, mock_libs, mock_isgit, mock_mail,
                              mock_git, mock_isremote):

        """Function:  test_is_git_repo_true

        Description:  Test with is_git_repo set to True.

        Arguments:
            mock_log -> Mock Ref:  merge_repo.gen_class.Logger
            mock_libs -> Mock Ref:  merge_repo.gen_libs
            mock_isgit -> Mock Ref:  merge_repo.is_git_repo
            mock_mail -> Mock Ref:  merge_repo.send_mail
            mock_git -> Mock Ref:  merge_repo.git.Repo
            mock_isremote -> Mock Reg:  merge_repo.is_remote_branch

        """

        mock_log.return_value = True
        mock_libs.mv_file.return_value = True
        mock_isgit.return_value = True
        mock_mail.return_value = True
        mock_git.Repo.return_value = Repo()
        mock_isremote.return_value = False

        self.assertFalse(merge_repo.merge(self.args, self.cfg, mock_log))

    @mock.patch("merge_repo.send_mail")
    @mock.patch("merge_repo.is_git_repo")
    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_is_git_repo_false(self, mock_log, mock_libs, mock_isgit,
                               mock_mail):

        """Function:  test_is_git_repo_false

        Description:  Test with is_git_repo set to False.

        Arguments:
            mock_log -> Mock Ref:  merge_repo.gen_class.Logger
            mock_libs -> Mock Ref:  merge_repo.gen_libs
            mock_isgit -> Mock Ref:  merge_repo.is_git_repo
            mock_mail -> Mock Ref:  merge_repo.send_mail

        """

        mock_log.return_value = True
        mock_libs.mv_file.return_value = True
        mock_isgit.return_value = False
        mock_mail.return_value = True

        self.assertFalse(merge_repo.merge(self.args, self.cfg, mock_log))


if __name__ == "__main__":
    unittest.main()
