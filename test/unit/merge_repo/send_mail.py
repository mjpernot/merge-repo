#!/usr/bin/python
# Classification (U)

"""Program:  send_mail.py

    Description:  Unit testing of send_mail in merge_repo.py.

    Usage:
        test/unit/merge_repo/send_mail.py

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
        test_send_mail -> Test send_mail function.

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

                self.url = "git@github.com:JAC-IDM/"
                self.work_dir = "/data/merge-repo/work_dir"
                self.err_dir = "/data/merge-repo/error_dir"
                self.archive_dir = "/data/merge-repo/archive_dir"
                self.log_file = "/data/merge-repo/log_dir/merge_repo.log"
                self.to_line = "myemail@mydomain"
                self.branch = "master"

        self.cfg = CfgTest()
        self.subj = "Email_Subject"
        self.email_body = ["Email Body Line 1", "Email Body Line 2"]

    @mock.patch("merge_repo.gen_class.Mail")
    def test_send_mail(self, mock_mail):

        """Function:  test_send_mail

        Description:  Test send_mail function.

        Arguments:

        """

        mock_mail.send_mail.return_value = True

        self.args_array = {"-t": "Email Addresses", "-z": True}

        self.assertFalse(merge_repo.send_mail(self.cfg, self.subj,
                                              self.email_body))


if __name__ == "__main__":
    unittest.main()
