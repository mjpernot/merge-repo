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
import time

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
        process_dirty -> Process any dirty files.
        process_untracked -> Process any untracked files.
        is_dirty -> Check to see if there is any dirty objects.
        is_untracked -> Check to see if there is any new objects not tracked.
        rename_br -> Rename the current branch to a new name.
        git_co -> Git checkout to another branch.
        priority_merge -> Merge of branch with priority of existing branch.
        git_pu -> Git push to remote respository.
        commits_diff ->  Compares 2 branches & returns number of commits diff.
        is_commits_ahead -> Gets diff - local branch is ahead of remote branch.
        is_commits_behind -> Gets diff - local branch is behind remote branch.

    """

    def __init__(self, base_url, repo_name, work_dir, git_dir, branch,
                 new_branch):

        """Method:  __init__

        Description:  Initialization of an instance of the GitMerge class.

        Arguments:
            base_url -> Base URL to remote git repository.
                NOTE: Does not include the git repository name.
            repo_name -> Name of remote git repository.
            work_dir -> Directory path to the working directory.
            git_dir -> Directory name of the local git repository.
            branch -> Name of branch at remote to be merged with.
            new_branch -> Name of branch to be merged into remote.

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
        self.new_branch = new_branch

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

        except git.exc.GitCommandError:
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

        if new_files:
            msg = "Added new files"
            self.gitrepo.index.add(new_files)
            self.gitrepo.index.commit(msg)

    def is_dirty(self, **kwargs):

        """Function:  is_dirty

        Description:  Check to see if there is any dirty objects.

        Arguments:
            (input) **kwargs:
                None
            (output) True|False -> If dirty objects detected.

        """
        
        return self.gitrepo.is_dirty()

    def is_untracked(self, **kwargs):

        """Function:  is_untracked

        Description:  Check to see if there is any new objects not tracked.

        Arguments:
            (input) **kwargs:
                None
            (output) True|False -> If untracked objects detected.

        """
        
        return self.gitrepo.is_dirty(untracked_files=True)

    def git_fetch(self, cnt=0, **kwargs):

        """Function:  git_fetch

        Description:  Fetch from the remote Git repository the master branch.

        Arguments:
            (input) cnt -> Number of recursive calls on method.
            (input) **kwargs:
                None
            (output) status -> True|False - Success of command.
            (output) msg -> Dictionary of return error code.

        """

        status = True
        msg = {}

        try:
            self.gitcmd.fetch()

        except git.exc.GitCommandError as (code):

            if code.status == 128 and cnt < 5:

                time.sleep(5)
                cnt += 1
                git_fetch(cnt)

            else:

                status = False
                msg["status"] = code.status
                msg["stderr"] = code.stderr
                msg["command"] = code.command

        return status, msg

    def rename_br(self, branch=self.new_branch, **kwargs):

        """Function:  rename_br

        Description:  Rename the current branch to a new name.

        Arguments:
            (input) brach -> Name of new branch.
            (input) **kwargs:
                None
            (output) status -> True|False - Success of command.
            (output) msg -> Dictionary of return error code.

        """

        status = True
        msg = {}

        try:
            self.gitcmd.branch(branch)

        except git.exc.GitCommandError as (code):

            status = False
            msg["status"] = code.status
            msg["stderr"] = code.stderr
            msg["command"] = code.command

        return status, msg

    def git_co(self, branch=self.branch, **kwargs):

        """Function:  git_co

        Description:  Git checkout to another branch.

        Arguments:
            (input) brach -> Name of branch to checkout.
            (input) **kwargs:
                None
            (output) status -> True|False - Success of command.
            (output) msg -> Dictionary of return error code.

        """

        status = True
        msg = {}

        try:
            self.gitcmd.checkout(branch)

        except git.exc.GitCommandError as (code):

            status = False
            msg["status"] = code.status
            msg["stderr"] = code.stderr
            msg["command"] = code.command

        return status, msg

    def priority_merge(self, branch=self.new_branch, **kwargs):

        """Function:  priority_merge

        Description:  Merge of branch with priority of existing branch.
        
        NOTE:  The branch will have priority over the existing branch.

        Arguments:
            (input) branch -> Name of branch to merge with current branch.
            (input) **kwargs:
                None
            (output) status -> True|False - Success of command.
            (output) msg -> Dictionary of return error code.

        """

        status = True
        msg = {}

        try:
            self.gitcmd.merge("--no-ff", "-s", "recursive", "-X", "theirs",
                              branch)

        except git.exc.GitCommandError as (code):

            status = False
            msg["status"] = code.status
            msg["stdout"] = code.stdout
            msg["command"] = code.command

        return status, msg

    def git_pu(self, cnt=0, tags=False, **kwargs):

        """Function:  git_pu

        Description:  Git push to remote respository.

        Arguments:
            (input) cnt -> Number of recursive calls on method.
            (input) tags -> True|False - Push tags instead.
            (input) **kwargs:
                None
            (output) status -> True|False - Success of command.
            (output) msg -> Dictionary of return error code.

        """

        status = True
        msg = {}
        option = ""

        if tags:
            option = "--tags"
        
        try:
            self.gitcmd.push(option)

        except git.exc.GitCommandError as (code):

            if code.status == 128 and cnt < 5:

                time.sleep(5)
                cnt += 1
                git_pu(cnt)

            else:

                status = False
                msg["status"] = code.status
                msg["stderr"] = code.stderr
                msg["command"] = code.command

        return status, msg

    def commits_diff(self, data_str, **kwargs):

        """Function:  commits_diff

        Description:  Compares a branch with another branch and returns a count
            on the number of commits difference between the two branches.
                0 -> Branch not ahead of other branch.
                >0 ->  Branch is ahead of other branch by N commits.

        Note:
            The data_str will contain the order of the branches being compared,
                whether local to remote or remote to local.
            The format of the data_str is:
                Local to Remote:
                    "BRANCH_NAME..origin/BRANCH_NAME"
                Remote to Local:
                    "origin/BRANCH_NAME..BRANCH_NAME"

        Arguments:
            (input) data_str -> Contains the order of branches to be compared.
            (input) **kwargs:
                None
            (output) -> N commits difference between branches.

        """

        return sum(1 for x in self.gitrepo.iter_commits(data_str))

def is_commits_ahead(self, branch, **kwargs):

    """Function:  is_commits_ahead

    Description:  Compares the local branch with the remote branch and returns
        a count on whether local branch is ahead of remote branch.
        Output:
            0 -> Local branch not ahead of remote branch.
            >0 ->  Local branch is ahead of remote branch by N commits.

    Arguments:
        (input) branch -> Branch being compared.
        (input) **kwargs:
            None
        (output) -> N commits local branch ahead of remote branch.

    """

    return commits_diff("origin/" + branch + ".." + branch)

def is_commits_behind(self, branch, **kwargs):

    """Function:  is_commits_behind

    Description:  Compares the local branch with the remote branch and returns
        a count on whether local branch is behind remote branch.
        Output:
            0 -> Local branch not behind remote branch.
            >0 ->  Local branch is behind remote branch by N commits.

    Arguments:
        (input) branch -> Branch being compares.
        (input) **kwargs:
            None
        (output) -> N commits local branch behind remote branch.

    """

    return commits_diff(branch + "..origin/" + branch)
