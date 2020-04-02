# Python project for the merging of a local Git repository into an existing Git repository.
# Classification (U)

# Description:
  The program is designed to take an outside local Git repository and merge it into an existing remote Git repository.  It will, however, make the local Git repository the priority repository.  This is a way of an outside repository being modified and then merging those modifications into an existing remote Git respository.

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
  * Merge a outside local repository into an existing remote repository.


# Prerequisites:

  * List of Linux packages that need to be installed on the server.
    - python-libs
    - python-devel
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

Setup configuration file.
```
cd config
cp merge.py.TEMPLATE merge.py
```

Modify configutation file.
Make the appropriate changes to the Git environment in the merge.py file.
  * "git_project" is the Git Project name.
  * "git_server" is the Git Server Fully Qualified Domain Name.
  * "work_dir" is the directory where the merge will take place.
  * "err_dir" is the directory where a project will be archive if an error occurs.
  * "archive_dir" is the directory where the project will be save to after the merge.
  * "quar_dir" is the directory where items that are not processed will be saved to.
  * "to_line" is one or more email addresses to receive emails from the program.
  * "log_file" is the directory path and log file name for the program.

```
vim merge.py
```

# Advance Configuration:

These are additional entries in the configuration file that should not be modified unless necessary.  These entries are below: "Do not modify the settings below unless you know what you are doing." line in the configuration file.
  * name="gituser":  Is the Local Git Repository user name during the merge process.  Do not modify.
  * email="gituser@domain.mail":  Is the Local Git Repository user email address during the merge process.  Do not modify.
  * branch="develop":  Is the branch name to which the project will be merged in the remote repository.  Can be set to another branch, but do not recommend setting it to the "master" branch.
  * mod_branch="mod_release":  Is the temporary name of the branch which the project will be assigned.  Only modify if the branch that is being merged to in the remote repository is called "mod_release"
  * dirty="revert":  There are two options available for this setting:  revert and commit.  Revert (default) will reverse any dirty changes back to the original value.  Commit will take the dirty changes and commit them to the project.  Not recommended to be changed from the default setting as unsolicited changes during the transfer process could be introduced into the project.
  * untracked="remove":  There are two options available for this setting:  add and remove.  Remove (default) will not commit any untracked files to the project that were introduced during the transfer process.  Add on the other hand will commit any untracked files to the project.  Not recommended to be changed from the default setting as untracked files that were added during the transfer process could cause problems with the current project.
  * prefix="git@":  Is the prefix to the Git URL setting.  This would only need to be changed if the Git remote repositiory is using a something other than git at the repository to reference the projects.

# Program Help Function:

  All of the programs, except the library and class files, will have an -h (Help option) that will show display a help message for that particular program.  The help message will usually consist of a description, usage, arugments to the program, example, notes about the program, and any known bugs not yet fixed.  To run the help command:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
{Python_Project}/merge-repo/merge_repo.py -h
```


# Testing:

# Unit Testing:

### Description: Testing consists of unit testing for the functions in the merge_repo.py program.

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

### Unit testing:
```
cd {Python_Project}/merge-repo
test/unit/merge_repo/unit_test_run.sh
```

### Code coverage unit testing:
```
cd {Python_Project}/merge-repo
test/unit/merge_repo/code_coverage.sh
```

