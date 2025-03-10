# Classification (U)

"""Program:  quarantine_files.py

    Description:  Unit testing of quarantine_files in merge_repo.py.

    Usage:
        test/unit/merge_repo/quarantine_files.py

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

        self.quar_dir = "/data/merge-repo/quarantine"
        self.to_line = "to@domain"


class GitMerge(object):                         # pylint:disable=R0903,R0205

    """Class:  GitMerge

    Description:  Class which is a representation of GitMerge module.

    Methods:
        __init__

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the GitMerge class.

        Arguments:

        """

        self.chg_files = []
        self.new_files = []
        self.repo_name = "Repo_Name"
        self.git_dir = "/data/git_dir"


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_added_status
        test_file_dir
        test_multiple_files
        test_copy_directory2
        test_copy_directory
        test_copy_file
        test_modified_no_list
        test_added_no_list
        test_no_status
        test_modified_status
        test_added_status

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.gitr = GitMerge()
        self.cfg = CfgTest()
        self.dtg = "2019-04-16 13:51:42"
        self.datetime = "(2019, 4, 16, 13, 51, 42, 852147)"
        self.pathfile = "subdirectory/File1"

    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.datetime.datetime")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_no_email(self, mock_log, mock_date, mock_lib):

        """Function:  test_no_email

        Description:  Test with no email notifications.

        Arguments:

        """

        mock_date.now.return_value = self.datetime
        mock_date.strftime.return_value = self.dtg
        mock_log.return_value = True
        mock_lib.cp_file.return_value = True
        mock_lib.chk_crt_dir.return_value = True

        self.gitr.new_files = ["File1"]
        self.cfg.to_line = None

        self.assertFalse(merge_repo.quarantine_files(self.gitr, self.cfg,
                                                     mock_log, status="added"))

    @mock.patch("merge_repo.os.path.exists", mock.Mock(return_value=False))
    @mock.patch("merge_repo.os.makedirs", mock.Mock(return_value=True))
    @mock.patch("merge_repo.send_mail")
    @mock.patch("merge_repo.post_body")
    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.datetime.datetime")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_file_dir(                                  # pylint:disable=R0913
            self, mock_log, mock_date, mock_lib, mock_body, mock_mail):

        """Function:  test_file_dir

        Description:  Test with file and sub-directory being quarantined.

        Arguments:

        """

        mock_date.now.return_value = self.datetime
        mock_date.strftime.return_value = self.dtg
        mock_log.return_value = True
        mock_lib.cp_file.return_value = True
        mock_lib.chk_crt_dir.return_value = True
        mock_body.return_value = True
        mock_mail.return_value = True

        self.gitr.new_files = [self.pathfile, "File2"]

        self.assertFalse(merge_repo.quarantine_files(self.gitr, self.cfg,
                                                     mock_log, status="added"))

    @mock.patch("merge_repo.send_mail")
    @mock.patch("merge_repo.post_body")
    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.datetime.datetime")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_multiple_files(                            # pylint:disable=R0913
            self, mock_log, mock_date, mock_lib, mock_body, mock_mail):

        """Function:  test_copy_file

        Description:  Test with multiple files being quarantined.

        Arguments:

        """

        mock_date.now.return_value = self.datetime
        mock_date.strftime.return_value = self.dtg
        mock_log.return_value = True
        mock_lib.cp_file.return_value = True
        mock_lib.chk_crt_dir.return_value = True
        mock_body.return_value = True
        mock_mail.return_value = True

        self.gitr.new_files = ["File1", "File2"]

        self.assertFalse(merge_repo.quarantine_files(self.gitr, self.cfg,
                                                     mock_log, status="added"))

    @mock.patch("merge_repo.os.path.exists", mock.Mock(return_value=False))
    @mock.patch("merge_repo.os.makedirs", mock.Mock(return_value=True))
    @mock.patch("merge_repo.send_mail")
    @mock.patch("merge_repo.post_body")
    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.datetime.datetime")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_copy_directory2(                           # pylint:disable=R0913
            self, mock_log, mock_date, mock_lib, mock_body, mock_mail):

        """Function:  test_copy_directory2

        Description:  Test with file in sub-directory being quarantined.

        Arguments:

        """

        mock_date.now.return_value = self.datetime
        mock_date.strftime.return_value = self.dtg
        mock_log.return_value = True
        mock_lib.cp_file.return_value = True
        mock_lib.chk_crt_dir.return_value = True
        mock_body.return_value = True
        mock_mail.return_value = True

        self.gitr.new_files = [self.pathfile]

        self.assertFalse(merge_repo.quarantine_files(self.gitr, self.cfg,
                                                     mock_log, status="added"))

    @mock.patch("merge_repo.os.path.exists", mock.Mock(return_value=True))
    @mock.patch("merge_repo.send_mail")
    @mock.patch("merge_repo.post_body")
    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.datetime.datetime")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_copy_directory(                            # pylint:disable=R0913
            self, mock_log, mock_date, mock_lib, mock_body, mock_mail):

        """Function:  test_copy_directory

        Description:  Test with file in sub-directory being quarantined.

        Arguments:

        """

        mock_date.now.return_value = self.datetime
        mock_date.strftime.return_value = self.dtg
        mock_log.return_value = True
        mock_lib.cp_file.return_value = True
        mock_lib.chk_crt_dir.return_value = True
        mock_body.return_value = True
        mock_mail.return_value = True

        self.gitr.new_files = [self.pathfile]

        self.assertFalse(merge_repo.quarantine_files(self.gitr, self.cfg,
                                                     mock_log, status="added"))

    @mock.patch("merge_repo.send_mail")
    @mock.patch("merge_repo.post_body")
    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.datetime.datetime")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_copy_file(                                 # pylint:disable=R0913
            self, mock_log, mock_date, mock_lib, mock_body, mock_mail):

        """Function:  test_copy_file

        Description:  Test with file being quarantined.

        Arguments:

        """

        mock_date.now.return_value = self.datetime
        mock_date.strftime.return_value = self.dtg
        mock_log.return_value = True
        mock_lib.cp_file.return_value = True
        mock_lib.chk_crt_dir.return_value = True
        mock_body.return_value = True
        mock_mail.return_value = True

        self.gitr.new_files = ["File1"]

        self.assertFalse(merge_repo.quarantine_files(self.gitr, self.cfg,
                                                     mock_log, status="added"))

    @mock.patch("merge_repo.gen_class.Logger")
    def test_modified_no_list(self, mock_log):

        """Function:  test_modified_no_list

        Description:  Test with status set to modified with empty list.

        Arguments:

        """

        mock_log.return_value = True

        self.assertFalse(merge_repo.quarantine_files(self.gitr, self.cfg,
                                                     mock_log,
                                                     status="modified"))

    @mock.patch("merge_repo.gen_class.Logger")
    def test_added_no_list(self, mock_log):

        """Function:  test_added_no_list

        Description:  Test with status set to added with empty list.

        Arguments:

        """

        mock_log.return_value = True

        self.assertFalse(merge_repo.quarantine_files(self.gitr, self.cfg,
                                                     mock_log, status="added"))

    @mock.patch("merge_repo.gen_class.Logger")
    def test_no_status(self, mock_log):

        """Function:  test_no_status

        Description:  Test with status not set.

        Arguments:

        """

        mock_log.return_value = True

        self.assertFalse(merge_repo.quarantine_files(self.gitr, self.cfg,
                                                     mock_log))

    @mock.patch("merge_repo.send_mail")
    @mock.patch("merge_repo.post_body")
    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.datetime.datetime")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_modified_status(                           # pylint:disable=R0913
            self, mock_log, mock_date, mock_lib, mock_body, mock_mail):

        """Function:  test_modified_status

        Description:  Test with status set to modified.

        Arguments:

        """

        mock_date.now.return_value = self.datetime
        mock_date.strftime.return_value = self.dtg
        mock_log.return_value = True
        mock_lib.cp_file.return_value = True
        mock_lib.chk_crt_dir.return_value = True
        mock_body.return_value = True
        mock_mail.return_value = True

        self.gitr.chg_files = ["File1"]

        self.assertFalse(merge_repo.quarantine_files(
            self.gitr, self.cfg, mock_log, status="modified"))

    @mock.patch("merge_repo.send_mail")
    @mock.patch("merge_repo.post_body")
    @mock.patch("merge_repo.gen_libs")
    @mock.patch("merge_repo.datetime.datetime")
    @mock.patch("merge_repo.gen_class.Logger")
    def test_added_status(                              # pylint:disable=R0913
            self, mock_log, mock_date, mock_lib, mock_body, mock_mail):

        """Function:  test_added_status

        Description:  Test with status set to added.

        Arguments:

        """

        mock_date.now.return_value = self.datetime
        mock_date.strftime.return_value = self.dtg
        mock_log.return_value = True
        mock_lib.cp_file.return_value = True
        mock_lib.chk_crt_dir.return_value = True
        mock_body.return_value = True
        mock_mail.return_value = True

        self.gitr.new_files = ["File1"]

        self.assertFalse(merge_repo.quarantine_files(self.gitr, self.cfg,
                                                     mock_log, status="added"))


if __name__ == "__main__":
    unittest.main()
