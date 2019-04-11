# Classification (U)

"""Program:  gen_class.py

    Description:  Class that has class definitions for general use.

    Classes:
        Daemon
        ProgressBar
        SingleInstanceException
        ProgramLock
        System
            Mail
        Logger
        Yum

"""

# Libraries and Global Variables

# Standard

# Third-party
import git

# Local
import version

# Version
__version__ = version.__version__


class GitClass(object):

    """Class:  GitMerge

    Description:  Class that initializes and sets up instances to the Python
        git repository and git command line instances.

    Super-Class:  object

    Sub-Classes:
        GitMerge

    Methods:
        __init__ -> Class instance initilization.

    """

    def __init__(self, repo_dir="."):

        """Method:  __init__

        Description:  Initialization of an instance of the GitMerge class.

        Arguments:
            repo_dir -> Git repository path name.

        """

        self.gitrepo = None
        self.gitcmd = None
        self.repo_dir = repo_dir

    def create_repo(self, repo_dir=None):

        """Method:  create_repo

        Description:  Create a git.Repo instance.

        Arguments:
            repo_dir -> Git repository path name.

        """

        if repo_dir:
           self.repo_dir = repo_dir

        self.gitrepo = git.Repo(self.repo_dir)

    def create_cmd(self):

        """Method:  create_cmd

        Description:  Create a git.Repo.git command line instance.

        Arguments:
            None

        """

        if self.gitrepo:
            self.gitcmd = self.gitrepo.git


class GitMerge(GitClass):

    """Class:  GitMerge

    Description:  Class that handles operations of merging a git repository
        with a remote git repository.

    Super-Class:  GitClass

    Sub-Classes:
        None

    Methods:
        __init__ -> Class instance initilization.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization of an instance of the GitMerge class.

        Arguments:
            None

        """

        super(GitMerge, self).__init__()

        # os.path.join(cfg.work_dir, os.path.basename(args_array["-p"]))
        self.proj_dir = None

        # cfg.url
        self.base_url = None

        # cfg.url + args_array["-r"] + ".git"
        self.url = None

        # args_array["-r"]
        self.repo_name = None

        # cfg.work_dir
        self.work_dir = None

        # args_array["-p"] -> Do I need this in the class?
        self.init_path = None

        # Set by is_git_repo().
        self.git_path = None

        # Set by is_remote().
        self.remote_info = None

        # "mod_release" -> Needs to be populated from cfg file.
        self.tmp_branch = None

    def create_gitrepo(self):

        """Method:  create_gitrepo

        Description:  Creates git repo and git command line instances.

        Arguments:
            None

        """

        super(GitMerge, self).create_repo()
        super(GitMerge, self).create_cmd()

    def set_remote(self):

        """Method:  set_remote

        Description:  Sets the url to the origin to a remote git repository.

        Arguments:
            None

        """

        self.gitcmd.remote("set-url", "origin",
                           self.url + self.repo_name + ".git")

    def is_git_repo(self, path):

        """Method:  is_git_repo

        Description:  Checks to see if the path is a git repository.

        Arguments:
            (input) path -> Directory path.
            (output) True|False -> Whether the directory is a git repository.

        """

        try:
            self.git_path = git.Repo(path).git_dir
            return True

        except git.exc.InvalidGitRepositoryError:
            return False

    def is_remote(self):

        """Method:  is_remote

        Description:  Checks to see if remote git repository exists.

        Arguments:
            (output) True|False -> Whether the directory is a git repository.

        """

        try:
            self.remote_info = git.gitcmd.ls_remote(self.url)
            return True

        except git.exc.InvalidGitRepositoryError:
            return False
