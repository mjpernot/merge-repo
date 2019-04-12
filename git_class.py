# Classification (U)

"""Program:  git_class.py

    Description:  Class that has class definitions for git repository.

    Classes:
        GitClass
            GitMerge

"""

# Libraries and Global Variables

# Standard
import os

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
        create_repo -> Create a git.Repo instance.
        create_cmd -> Create a git.Repo.git command line instance.

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
        create_gitrepo -> Creates git repo and git command line instances.
        set_remote -> Checks to see if remote git repository exists.
        is_remote -> Checks to see if remote git repository exists.

    """

    def __init__(self, base_url, repo_name, work_dir, git_dir, branch,
                 tmp_branch):

        """Method:  __init__

        Description:  Initialization of an instance of the GitMerge class.

        Arguments:
            base_url -> Base URL to remote git repository.
                NOTE: Does not include the git repository name.
            repo_name -> Name of remote git repository.
            work_dir -> Directory path to the working directory.
            git_dir -> Directory name of the local git repository.
            branch -> Name of branch at remote to be merged with.
            tmp_branch -> Name of temporary branch to be merged into remote.

        """

        super(GitMerge, self).__init__()

        # cfg.url
        self.base_url = base_url

        # args_array["-r"]
        self.repo_name = repo_name

        # cfg.url + args_array["-r"] + ".git"
        self.url = self.base_url + self.repo_name + ".git"

        # cfg.work_dir
        self.work_dir = work_dir

        # args_array["-p"]
        self.git_dir = git_dir

        # os.path.join(cfg.work_dir, os.path.basename(args_array["-p"]))
        self.proj_dir = os.path.join(self.work_dir, self.git_dir)

        # "mod_release" -> Needs to be populated from cfg file.
        self.tmp_branch = tmp_branch

        # cfg.branch
        self.branch = branch

        # Set by is_remote().
        self.remote_info = None

    def create_gitrepo(self, **kwargs):

        """Method:  create_gitrepo

        Description:  Creates git repo and git command line instances.

        Arguments:
            (input) **kwargs:
                None

        """

        super(GitMerge, self).create_repo()
        super(GitMerge, self).create_cmd()

    def set_remote(self, **kwargs):

        """Method:  set_remote

        Description:  Sets the url to the origin to a remote git repository.

        Arguments:
            (input) **kwargs:
                None

        """

        self.gitcmd.remote("set-url", "origin",
                           self.url + self.repo_name + ".git")

    def is_remote(self, **kwargs):

        """Method:  is_remote

        Description:  Checks to see if remote git repository exists.

        Arguments:
            (input) **kwargs:
                None
            (output) True|False -> Whether the directory is a git repository.

        """

        try:
            self.remote_info = git.gitcmd.ls_remote(self.url)
            return True

        except git.exc.InvalidGitRepositoryError:
            return False

def process_dirty(self, **kwargs):

    """Function:  process_dirty

    Description:  Process any dirty files.

    Arguments:
        (input) **kwargs:
            None

    """

    # Process deleted files.
    rm_files = [item.a_path for item in self.gitrepo.index.diff(None)
                if item.change_type == "D"]

    if rm_files:
        gitrepo.index.remove(rm_files, working_tree=true)

    # Process modified files.
    chg_files = [item.a_path for item in self.gitrepo.index.diff(None)
                 if item.change_type == "M"]

    if chg_files:
        self.gitrepo.index.add(chg_files)

    msg = "Added dirty files"

    if rm_files or chg_files:
        self.gitrepo.index.commit(msg)

def process_untracked(self, **kwargs):

    """Function:  process_untracked

    Description:  Process any untracked files.

    Arguments:
        (input) **kwargs:
            None

    """

    # Process new files.
    new_files = self.gitrepo.untracked_files

    msg = "Added new files"

    if new_files:
        self.gitrepo.index.add(new_files)
        self.gitrepo.index.commit(msg)
