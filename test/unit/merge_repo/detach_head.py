#!/usr/bin/python
# Classification (U)

"""Program:  detach_head.py

    Description:  Unit testing of detach_head in merge_repo.py.

    Usage:
        test/unit/merge_repo/detach_head.py

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
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Unit testing initilization.
        test_one_branch -> Test with one branch found.
        test_multiple_branches -> Test with multiple branches found.
        test_zero_branches -> Test with zero branches found.

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
                get_br_name -> Stub holder for the GitMerge.get_br_name method.
                detach_head -> Stub holder for GitMerge.detach_head method.
                remove_branch -> Stub holder for GitMerge.remove_branch method.

            """

            def __init__(self):

                """Method:  __init__

                Description:  Initialization instance of the GitMerge class.

                Arguments:

                """

                self.branch_name = "branch_name"
                self.status = []
                self.branches = []

            def get_br_name(self):

                """Method:  get_br_name

                Description:  Stub holder for the GitMerge.get_br_name method.

                Arguments:

                """

                return self.branch_name

            def detach_head(self):

                """Method:  detach_head

                Description:  Stub holder for GitMerge.detach_head method.

                Arguments:

                """

                return self.status

            def remove_branch(self, branch):

                """Method:  process_dirty

                Description:  Stub holder for GitMerge.remove_branch method.

                Arguments:
                    (input) branch -> Branch name.

                """

                return True

        self.gitr = GitMerge()
        self.branch1 = ["Branch1"]
        self.branch2 = ["Branch1", "Branch2"]
        self.err_msg1 = \
            "WARN:  Multiple branches detected: %s" % (self.branch2)

    @mock.patch("merge_repo.gen_class.Logger")
    def test_one_branch(self, mock_log):

        """Function:  test_one_branch

        Description:  Test with one branch found.

        Arguments:

        """

        mock_log.return_value = True
        self.gitr.branches = list(self.branch1)

        self.assertEqual(merge_repo.detach_head(self.gitr, mock_log),
                         (True, None))

    @mock.patch("merge_repo.gen_class.Logger")
    def test_multiple_branches(self, mock_log):

        """Function:  test_multiple_branches

        Description:  Test with multiple branches found.

        Arguments:

        """

        mock_log.return_value = True
        self.gitr.branches = list(self.branch2)

        self.assertEqual(merge_repo.detach_head(self.gitr, mock_log),
                         (False, self.err_msg1))

    @mock.patch("merge_repo.gen_class.Logger")
    def test_zero_branches(self, mock_log):

        """Function:  test_zero_branches

        Description:  Test with zero branches found.

        Arguments:

        """

        mock_log.return_value = True

        self.assertEqual(merge_repo.detach_head(self.gitr, mock_log),
                         (True, None))


if __name__ == "__main__":
    unittest.main()
