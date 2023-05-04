# Classification (U)

"""Program:  process_project.py

    Description:  Unit testing of process_project in merge_repo.py.

    Usage:
        test/unit/merge_repo/process_project.py

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
import merge_repo
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_status3_true
        test_status3_false
        test_status2_true
        test_status2_false
        test_status1_true
        test_status1_false

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
                __init__

            """

            def __init__(self):

                """Method:  __init__

                Description:  Initialization instance of the CfgTest class.

                Arguments:

                """

                self.archive_dir = "/Arhive/Directory"
                self.err_dir = "/Error/Directory"
                self.to_line = "to@domain"

        self.cfg = CfgTest()
        self.status = True
        self.status2 = False
        self.msg = {}
        self.msg2 = {"Error": "Code"}

    @mock.patch("merge_repo.merge_project")
    @mock.patch("merge_repo.git_class.GitMerge")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_status3_true(self, mock_log, mock_git, mock_merge):

        """Function:  test_status3_true

        Description:  Test with status3 set to True.

        Arguments:

        """

        mock_log.return_value = True
        mock_git.git_fetch.return_value = (self.status, self.msg)
        mock_git.rename_br.return_value = (self.status, self.msg)
        mock_git.git_co.return_value = (self.status, self.msg)
        mock_merge.return_value = True

        self.assertFalse(merge_repo.process_project(mock_git, self.cfg,
                                                    mock_log))

    @mock.patch("merge_repo.post_process")
    @mock.patch("merge_repo.git_class.GitMerge")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_status3_false(self, mock_log, mock_git, mock_post):

        """Function:  test_status3_false

        Description:  Test with status3 set to False.

        Arguments:

        """

        mock_log.return_value = True
        mock_git.git_fetch.return_value = (self.status, self.msg)
        mock_git.rename_br.return_value = (self.status, self.msg)
        mock_git.git_co.return_value = (self.status2, self.msg2)
        mock_git.mod_branch.return_value = "Mod_Branch"
        mock_git.branch.return_value = "Master"
        mock_post.return_value = True

        self.assertFalse(merge_repo.process_project(mock_git, self.cfg,
                                                    mock_log))

    @mock.patch("merge_repo.post_process")
    @mock.patch("merge_repo.git_class.GitMerge")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_status2_true(self, mock_log, mock_git, mock_post):

        """Function:  test_status2_true

        Description:  Test with status2 set to True.

        Arguments:

        """

        mock_log.return_value = True
        mock_git.git_fetch.return_value = (self.status, self.msg)
        mock_git.rename_br.return_value = (self.status, self.msg)
        mock_git.git_co.return_value = (self.status2, self.msg2)
        mock_git.mod_branch.return_value = "Mod_Branch"
        mock_git.branch.return_value = "Master"
        mock_post.return_value = True

        self.assertFalse(merge_repo.process_project(mock_git, self.cfg,
                                                    mock_log))

    @mock.patch("merge_repo.post_process")
    @mock.patch("merge_repo.git_class.GitMerge")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_status2_false(self, mock_log, mock_git, mock_post):

        """Function:  test_status2_false

        Description:  Test with status2 set to False.

        Arguments:

        """

        mock_log.return_value = True
        mock_git.git_fetch.return_value = (self.status, self.msg)
        mock_git.rename_br.return_value = (self.status2, self.msg2)
        mock_git.mod_branch.return_value = "Mod_Branch"
        mock_git.branch.return_value = "Master"
        mock_post.return_value = True

        self.assertFalse(merge_repo.process_project(mock_git, self.cfg,
                                                    mock_log))

    @mock.patch("merge_repo.post_process")
    @mock.patch("merge_repo.git_class.GitMerge")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_status1_true(self, mock_log, mock_git, mock_post):

        """Function:  test_status1_true

        Description:  Test with status1 set to True.

        Arguments:

        """

        mock_log.return_value = True
        mock_git.git_fetch.return_value = (self.status, self.msg)
        mock_git.rename_br.return_value = (self.status2, self.msg2)
        mock_git.mod_branch.return_value = "Mod_Branch"
        mock_git.branch.return_value = "Master"
        mock_post.return_value = True

        self.assertFalse(merge_repo.process_project(mock_git, self.cfg,
                                                    mock_log))

    @mock.patch("merge_repo.post_process")
    @mock.patch("merge_repo.git_class.GitMerge")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_status1_false(self, mock_log, mock_git, mock_post):

        """Function:  test_status1_false

        Description:  Test with status1 set to False.

        Arguments:

        """

        mock_log.return_value = True
        mock_git.git_fetch.return_value = (self.status2, self.msg2)
        mock_post.return_value = True

        self.assertFalse(merge_repo.process_project(mock_git, self.cfg,
                                                    mock_log))


if __name__ == "__main__":
    unittest.main()
