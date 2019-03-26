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


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Unit testing initilization.
        test_status_flag_true -> Test with status flag set to True.
        test_status_flag_false -> Test with status flag set to False.

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

                self.url="git@gitlab.code.dicelab.net:JAC-IDM/"
                self.work_dir="/home/mark.j.pernot/merge/work_dir"
                self.err_dir="/home/mark.j.pernot/merge/error_dir"
                self.archive_dir="/home/mark.j.pernot/merge/archive_dir"
                self.log_file="/home/mark.j.pernot/merge/log_dir/merge_repo.log"
                self.to_line="Mark.J.Pernot@coe.ic.gov"
                self.branch="master"

        self.cfg = CfgTest()

        self.args = {"-c": "config_file",
                     "-d": "/home/mark.j.pernot/merge_repo/config",
                     "-r": "repo-name",
                     "-p": "/home/mark.j.pernot/merge/repo-name", "-M": True}

    @mock.patch("merge_repo.send_mail")
    @mock.patch("merge_repo.is_git_repo")
    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_is_git_repo_false(self, mock_log, mock_libs, mock_git, mock_mail):

        mock_log.return_value = True
        mock_libs.mv_file.return_value = True
        mock_git.return_value = False
        mock_mail.return_value = True

        self.assertFalse(merge_repo.merge(self.args, self.cfg, mock_log))


if __name__ == "__main__":
    unittest.main()
        
        
