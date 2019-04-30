#!/usr/bin/python
# Classification (U)

"""Program:  quarantine.py

    Description:  Unit testing of quarantine in merge_repo.py.

    Usage:
        test/unit/merge_repo/quarantine.py

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
        test_empty_lists -> Test with chg_files & new_files are empty lists.

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

        class GitMerge(object):

            """Class:  GitMerge

            Description:  Class which is a representation of GitMerge module.

            Super-Class:  object

            Sub-Classes:  None

            Methods:
                __init__ -> Initialize configuration environment.
                get_dirty -> Stub holder for the GitMerge.get_dirty method.
                get_untracked -> Stub holder for GitMerge.get_untracked method.

            """

            def __init__(self):

                """Method:  __init__

                Description:  Initialization instance of the GitMerge class.

                Arguments:
                        None

                """

                self.chg_files = []
                self.new_files = []

            def get_dirty(self):

                """Method:  get_dirty

                Description:  Stub holder for the GitMerge.get_dirty method.

                Arguments:
                        None

                """

                return True

            def get_untracked(self):

                """Method:  get_untracked

                Description:  Stub holder for GitMerge.get_untracked method.

                Arguments:
                        None

                """

                return True

        self.gitr = GitMerge()
        self.cfg = CfgTest()

    @mock.patch("merge_repo.quarantine_files")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_empty_lists(self, mock_log, mock_quar):

        """Function:  test_empty_lists

        Description:  Test with both chg_files and new_files are empty lists.

        Arguments:
            None

        """

        mock_log.return_value = True
        mock_quar.return_value = True

        self.assertFalse(merge_repo.quarantine(self.gitr, self.cfg, mock_log))


if __name__ == "__main__":
    unittest.main()
