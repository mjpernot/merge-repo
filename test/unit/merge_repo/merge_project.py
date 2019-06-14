#!/usr/bin/python
# Classification (U)

"""Program:  merge_project.py

    Description:  Unit testing of merge_project in merge_repo.py.

    Usage:
        test/unit/merge_repo/merge_project.py

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


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Unit testing initilization.
        test_status3_true -> Test with status3 set to True.
        test_status3_false -> Test with status3 set to False.
        test_status2_true -> Test with status2 set to True.
        test_status2_false -> Test with status2 set to False.
        test_status1_true -> Test with status1 set to True.
        test_status1_false -> Test with status1 set to False.

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

                self.archive_dir = "/Arhive/Directory"
                self.err_dir = "/Error/Directory"
                self.to_line = "to@domain"

        self.cfg = CfgTest()
        self.status = True
        self.status2 = False
        self.msg = {}
        self.msg2 = {"Error": "Code"}

    @mock.patch("merge_repo.post_check")
    @mock.patch("merge_repo.git_class.GitMerge")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_status3_true(self, mock_log, mock_git, mock_check):

        """Function:  test_status3_true

        Description:  Test with status3 set to True.

        Arguments:
            None

        """

        mock_log.return_value = True
        mock_git.priority_merge.return_value = (self.status, self.msg)
        mock_git.git_pu.side_effect = [(self.status, self.msg),
                                       (self.status, self.msg)]
        mock_check.return_value = True

        self.assertFalse(merge_repo.merge_project(mock_git, self.cfg,
                                                  mock_log))

    @mock.patch("merge_repo.post_process")
    @mock.patch("merge_repo.git_class.GitMerge")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_status3_false(self, mock_log, mock_git, mock_post):

        """Function:  test_status3_false

        Description:  Test with status3 set to False.

        Arguments:
            None

        """

        mock_log.return_value = True
        mock_git.priority_merge.return_value = (self.status, self.msg)
        mock_git.git_pu.side_effect = [(self.status, self.msg),
                                       (self.status2, self.msg2)]
        mock_post.return_value = True

        self.assertFalse(merge_repo.merge_project(mock_git, self.cfg,
                                                  mock_log))

    @mock.patch("merge_repo.post_process")
    @mock.patch("merge_repo.git_class.GitMerge")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_status2_true(self, mock_log, mock_git, mock_post):

        """Function:  test_status2_true

        Description:  Test with status2 set to True.

        Arguments:
            None

        """

        mock_log.return_value = True
        mock_git.priority_merge.return_value = (self.status, self.msg)
        mock_git.git_pu.side_effect = [(self.status, self.msg),
                                       (self.status2, self.msg2)]
        mock_post.return_value = True

        self.assertFalse(merge_repo.merge_project(mock_git, self.cfg,
                                                  mock_log))

    @mock.patch("merge_repo.post_process")
    @mock.patch("merge_repo.git_class.GitMerge")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_status2_false(self, mock_log, mock_git, mock_post):

        """Function:  test_status2_false

        Description:  Test with status2 set to False.

        Arguments:
            None

        """

        mock_log.return_value = True
        mock_git.priority_merge.return_value = (self.status, self.msg)
        mock_git.git_pu.return_value = (self.status2, self.msg2)
        mock_post.return_value = True

        self.assertFalse(merge_repo.merge_project(mock_git, self.cfg,
                                                  mock_log))

    @mock.patch("merge_repo.post_process")
    @mock.patch("merge_repo.git_class.GitMerge")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_status1_true(self, mock_log, mock_git, mock_post):

        """Function:  test_status1_true

        Description:  Test with status1 set to True.

        Arguments:
            None

        """

        mock_log.return_value = True
        mock_git.priority_merge.return_value = (self.status, self.msg)
        mock_git.git_pu.return_value = (self.status2, self.msg2)
        mock_post.return_value = True

        self.assertFalse(merge_repo.merge_project(mock_git, self.cfg,
                                                  mock_log))

    @mock.patch("merge_repo.post_process")
    @mock.patch("merge_repo.git_class.GitMerge")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_status1_false(self, mock_log, mock_git, mock_post):

        """Function:  test_status1_false

        Description:  Test with status1 set to False.

        Arguments:
            None

        """

        mock_log.return_value = True
        mock_git.priority_merge.return_value = (self.status2, self.msg2)
        mock_git.mod_branch.return_value = "Mod_Branch"
        mock_git.branch.return_value = "Master"
        mock_post.return_value = True

        self.assertFalse(merge_repo.merge_project(mock_git, self.cfg,
                                                  mock_log))


if __name__ == "__main__":
    unittest.main()