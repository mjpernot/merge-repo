#!/usr/bin/python
# Classification (U)

"""Program:  get_cmdline.py

    Description:  Unit testing of get_cmdline in merge_repo.py.

    Usage:
        test/unit/merge_repo/get_cmdline.py

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
        test_get_cmdline -> Test returning command line.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        class CmdLine(object):

            """Class:  CmdLine

            Description:  Class which is a representation of a sys module.

            Methods:
                __init__ -> Initialize configuration environment.

            """

            def __init__(self):

                """Method:  __init__

                Description:  Initialization instance of the CfgTest class.

                Arguments:

                """

                self.argv = ["./merge_repo.py", "-c"]

        self.cmd_line = CmdLine()
        self.results = ["./merge_repo.py", "-c"]

    def test_get_cmdline(self):

        """Function:  test_get_cmdline

        Description:  Test returning command line.

        Arguments:

        """

        self.assertEqual(merge_repo.get_cmdline(self.cmd_line), self.results)


if __name__ == "__main__":
    unittest.main()
