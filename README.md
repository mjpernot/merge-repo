# Python project for the merging of a non-local Git repository into an existing Git repository.
# Classification (U)

# Description:
  Designed to take a non-local Git repository and merge it into a remote Git repository.  It will, however, make the new non-local Git repository as the priority repository.  This is a way for an outside repository being modified and then merging those modifications into an existing remote Git respository.

###  This README file is broken down into the following sections:
  * Features
  * Prerequisites
  * Installation
  * Configuration
    - Advance Configuration
  * Program Help Function
  * Testing
    - Unit


# Features:
  * Merge a non-local repository into an existing remote Git repository.
  * Allow for the merging of unrelated Git histories.


# Prerequisites:

  * List of Linux packages that need to be installed on the server.
    - git
    - python-pip

  * Local class/library dependencies within the program structure.
    - lib/gen_class
    - lib/arg_parser
    - lib/gen_libs
    - git_lib/git_class


# Installation:

Install the project using git.
  * Replace **{Python_Project}** with the baseline path of the python program.

```
umask 022
cd {Python_Project}
git clone git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/merge-repo.git
```

Install/upgrade system modules.

```
cd merge-repo
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-git-lib.txt --target git_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-python-lib.txt --target git_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

# Configuration:

Modify configutation file.  Make the appropriate changes to the Git environment in the merge.py file.
  * "git_project" is the Git Project name.
  * "git_server" is the Git Server Fully Qualified Domain Name.
  * "work_dir" is the directory where the merge will take place.
  * "err_dir" is the directory where a project will be archive if an error occurs.
  * "archive_dir" is the directory where the project will be save to after the merge.
  * "quar_dir" is the directory where items that are not processed will be saved to.
  * "to_line" is one or more email addresses to receive emails from the program.
    -  If set to None, then no email notifications will be sent.
  * "log_file" is the directory path and log file name for the program.

  Note:  Ensure directories exist for work_dir, err_dir, archive_dir, quar_dir, and log_file entries.

```
cd config
cp merge.py.TEMPLATE merge.py
vim merge.py
```

# Advance Configuration:

These additional entries in the configuration file should not be modified unless necessary.  These configuration entries are below: "Do not modify the settings below unless you know what you are doing." line in the configuration file.
  * name="gituser":  Is the Local Git Repository user name during the merge process.  Do not modify.
  * email="gituser@domain.mail":  Is the Local Git Repository user email address during the merge process.  Do not modify.
  * branch="develop":  Is the branch name to which the project will be merged in the remote repository.  It can be set to another branch, but it is not recommend setting the entry to the "master" branch.
  * mod_branch="mod_release":  Is the temporary name of the branch which the project will be assigned during the merge process.  Only modify mod_branch if the branch that is being merged to in the remote repository is also called "mod_release"
  * dirty="revert":  There are two options available for this setting:  **revert** and **commit**.  **Revert** (default setting) will reverse any dirty changes back to the original value in the file.  **Commit** will take the dirty changes and commit them to the project before the merge.  It is not recommended to change from the default setting as unsolicited changes during the transfer process could be introduced into the project.
  * untracked="remove":  There are two options available for this setting:  **add** and **remove**.  **Remove** (default setting) will not commit any untracked files in the repository to the project that were introduced during the transfer process.  **Add** will commit all untracked files to the project before the merge takes place.  Again not recommended to be changed from the default setting as untracked files that were added during the transfer process could cause problems.
  * prefix="git@":  Is the prefix to the Git URL setting.  This would only need to be changed if the Git remote repositiory is using a something other than git at the repository to reference the projects.  This can be confirmed by checking on the remote Git repository under Cloning with SSH.

# Program Help Function:

  All of the programs, except the library and class files, will have an -h (Help option) that will show display a help message for that particular program.  The help message will usually consist of a description, usage, arugments to the program, example, notes about the program, and any known bugs not yet fixed.  To run the help command:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
{Python_Project}/merge-repo/merge_repo.py -h
```


# Testing:

# Unit Testing:

### Installation:

Install the project using git.
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

```
umask 022
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/merge-repo.git
```

Install/upgrade system modules.

```
cd merge-repo
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-git-lib.txt --target git_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-python-lib.txt --target git_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

# Unit test runs for merge_repo.py:
  * Replace **{Python_Project}** with the baseline path of the python program.

### Testing:
```
cd {Python_Project}/merge-repo
test/unit/merge_repo/unit_test_run.sh
```

### Code coverage:
```
cd {Python_Project}/merge-repo
test/unit/merge_repo/code_coverage.sh
```

