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
import lib.gen_libs as gen_libs
import version

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

    def __init__(self, repo_dir=".", **kwargs):

        """Method:  __init__

        Description:  Initialization of an instance of the GitMerge class.

        Arguments:
            repo_dir -> Git repository path name.

        """

        self.gitrepo = None
        self.gitcmd = None
        self.repo_dir = repo_dir

    def create_repo(self, repo_dir=None, **kwargs):

        """Method:  create_repo

        Description:  Create a git.Repo instance.

        Arguments:
            repo_dir -> Git repository path name.

        """

        if repo_dir:
            self.repo_dir = repo_dir

        self.gitrepo = git.Repo(self.repo_dir)

    def create_cmd(self, **kwargs):

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
        get_dirty -> Find any dirty (i.e. removed or modified) files.
        get_untracked -> Find any untracked (i.e. new) files.
        is_dirty -> Check to see if there is any dirty objects.
        is_untracked -> Check to see if there is any new objects not tracked.
        rename_br -> Rename the current branch to a new name.
        git_co -> Git checkout to another branch.
        priority_merge -> Merge of branch with priority of existing branch.
        git_pu -> Git push to remote respository.
        commits_diff ->  Compares 2 branches & returns number of commits diff.
        is_commits_ahead -> Gets diff - local branch is ahead of remote branch.
        is_commits_behind -> Gets diff - local branch is behind remote branch.
        is_remote_branch -> Determines if the branch exists in remote git repo.

    """

    def __init__(self, repo_name, git_dir, url, branch, mod_branch, **kwargs):

        """Method:  __init__

        Description:  Initialization of an instance of the GitMerge class.

        Arguments:
            repo_name -> Name of repository.
            git_dir -> Directory path to the local git repo.
            url -> URL to the remote git repository.
            branch -> Name of branch at remote to be merged with.
            mod_branch -> Name of branch to be merged into remote.

        """

        self.git_dir = git_dir

        super(GitMerge, self).__init__(self.git_dir)

        self.repo_name = repo_name
        self.url = url
        self.mod_branch = mod_branch
        self.branch = branch
        self.remote_info = None
        self.br_commit = None
        self.rm_files = []
        self.chg_files = []
        self.new_files = []

    def create_gitrepo(self, **kwargs):

        """Method:  create_gitrepo

        Description:  Creates git repo and git command line instances.

        Arguments:
            None

        """

        super(GitMerge, self).create_repo()
        super(GitMerge, self).create_cmd()

    def set_remote(self, **kwargs):

        """Method:  set_remote

        Description:  Sets the url to the origin to a remote git repository.

        Arguments:
            None

        """

        self.gitcmd.remote("set-url", "origin", self.url)

    def is_remote(self, **kwargs):

        """Method:  is_remote

        Description:  Checks to see if remote git repository exists.

        Arguments:
            (output) True|False -> Whether the directory is a git repository.

        """

        try:
            self.remote_info = self.gitcmd.ls_remote(self.url)
            return True

        except git.exc.GitCommandError:
            return False

    def process_dirty(self, option="revert", **kwargs):

        """Function:  process_dirty

        Description:  Process any dirty files.

        Arguments:
            (input) option -> revert|commit - options for the changes.

        """

        # Process deleted files.
        if not self.rm_files:
            self.rm_files = [item.a_path
                             for item in self.gitrepo.index.diff(None)
                             if item.change_type == "D"]

        if self.rm_files:
            if option == "revert":
                self.gitrepo.index.checkout(self.rm_files, force=True)

            elif option == "commit":
                self.gitrepo.index.remove(self.rm_files, working_tree=True)
                self.gitrepo.index.commit("Commit removed files")

        # Process modified files.
        if not self.chg_files:
            self.chg_files = [item.a_path
                              for item in self.gitrepo.index.diff(None)
                              if item.change_type == "M"]

        if self.chg_files:
            if option == "revert":
                self.gitrepo.index.checkout(self.chg_files, force=True)

            elif option == "commit":
                self.gitrepo.index.add(self.chg_files)
                self.gitrepo.index.commit("Commit modified files")

    def process_untracked(self, option="remove", **kwargs):

        """Function:  process_untracked

        Description:  Process any untracked (new) files.

        Arguments:
            (input) option -> add|remove - Options allowed for untracked files.

        """

        if not self.new_files:
            self.new_files = self.gitrepo.untracked_files

        if self.new_files:
            if option == "add":
                self.gitrepo.index.add(self.new_files)
                self.gitrepo.index.commit("Add new files")

            elif option == "remove":
                for f_name in self.new_files:
                    gen_libs.rm_file(os.path.join(self.git_dir, f_name))

    def get_dirty(self, **kwargs):

        """Function:  get_dirty

        Description:  Find any dirty (i.e. removed or modified) files and
            update appropriate attributes.

        Arguments:
            None

        """

        # Deleted files.
        self.rm_files = [item.a_path for item in self.gitrepo.index.diff(None)
                         if item.change_type == "D"]

        # Modified files.
        self.chg_files = [item.a_path for item in self.gitrepo.index.diff(None)
                          if item.change_type == "M"]

    def get_untracked(self, **kwargs):

        """Function:  get_untracked

        Description:  Find any untracked (i.e. new) files and update
            appropriate attribute.

        Arguments:
            None

        """

        self.new_files = self.gitrepo.untracked_files

    def is_dirty(self, **kwargs):

        """Function:  is_dirty

        Description:  Check to see if there is any dirty objects.

        Arguments:
            (output) True|False -> If dirty objects detected.

        """

        return self.gitrepo.is_dirty()

    def is_untracked(self, **kwargs):

        """Function:  is_untracked

        Description:  Check to see if there is any new objects not tracked.

        Arguments:
            (output) True|False -> If untracked objects detected.

        """

        return self.gitrepo.is_dirty(untracked_files=True)

    def git_fetch(self, cnt=0, **kwargs):

        """Function:  git_fetch

        Description:  Fetch from the remote Git repository the master branch.

        Arguments:
            (input) cnt -> Number of recursive calls on method.
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
                status, msg = self.git_fetch(cnt)

            else:
                status = False
                msg["status"] = code.status
                msg["stderr"] = code.stderr
                msg["command"] = code.command

        return status, msg

    def rename_br(self, branch=None, **kwargs):

        """Function:  rename_br

        Description:  Rename the current branch to a new name.

        Arguments:
            (input) branch -> Name of new branch.
            (output) status -> True|False - Success of command.
            (output) msg -> Dictionary of return error code.

        """

        status = True
        msg = {}

        if not branch:
            branch = self.mod_branch

        try:
            self.gitcmd.branch(branch)

        except git.exc.GitCommandError as (code):
            status = False
            msg["status"] = code.status
            msg["stderr"] = code.stderr
            msg["command"] = code.command

        return status, msg

    def git_co(self, branch=None, **kwargs):

        """Function:  git_co

        Description:  Git checkout to another branch.

        Arguments:
            (input) branch -> Name of branch to checkout.
            (output) status -> True|False - Success of command.
            (output) msg -> Dictionary of return error code.

        """

        status = True
        msg = {}

        if not branch:
            branch = self.branch

        try:
            self.gitcmd.checkout(branch)

        except git.exc.GitCommandError as (code):
            status = False
            msg["status"] = code.status
            msg["stderr"] = code.stderr
            msg["command"] = code.command

        return status, msg

    def priority_merge(self, branch=None, **kwargs):

        """Function:  priority_merge

        Description:  Merge of branch with priority of existing branch.

        NOTE:  The branch will have priority over the existing branch.

        Arguments:
            (input) branch -> Name of branch to merge with current branch.
            (output) status -> True|False - Success of command.
            (output) msg -> Dictionary of return error code.

        """

        status = True
        msg = {}

        if not branch:
            branch = self.mod_branch

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
            (output) status -> True|False - Success of command.
            (output) msg -> Dictionary of return error code.

        """

        status = True
        msg = {}
        option = None

        if tags:
            option = "--tags"

        try:
            self.gitcmd.push(option)

        except git.exc.GitCommandError as (code):
            if code.status == 128 and cnt < 5:
                time.sleep(5)
                cnt += 1
                status, msg = self.git_pu(cnt)

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
            (output) -> N commits difference between branches.

        """

        return sum(1 for x in self.gitrepo.iter_commits(data_str))

    def is_commits_ahead(self, branch, **kwargs):

        """Function:  is_commits_ahead

        Description:  Compares the local branch with the remote branch and
            returns a count on whether local branch is ahead of remote branch.
            Output:
                0 -> Local branch not ahead of remote branch.
                >0 ->  Local branch is ahead of remote branch by N commits.

        Arguments:
            (input) branch -> Branch being compared.
            (output) -> N commits local branch ahead of remote branch.

        """

        return self.commits_diff("origin/" + branch + ".." + branch)

    def is_commits_behind(self, branch, **kwargs):

        """Function:  is_commits_behind

        Description:  Compares the local branch with the remote branch and
            returns a count on whether local branch is behind remote branch.
            Output:
                0 -> Local branch not behind remote branch.
                >0 ->  Local branch is behind remote branch by N commits.

        Arguments:
            (input) branch -> Branch being compares.
            (output) -> N commits local branch behind remote branch.

        """

        return self.commits_diff(branch + "..origin/" + branch)

    def is_remote_branch(self, branch, **kwargs):

        """Function:  is_remote_branch

        Description:  Determines if the branch exist in remote git repository.

        Arguments:
            (input) branch -> Branch name.
            (output) True|False -> The branch is in the remote git repo.

        """

        try:
            self.br_commit = self.gitcmd.rev_parse("--verify", branch)
            return True

        except git.exc.GitCommandError:
            return False
