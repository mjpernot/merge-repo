# Python project for the merging of a local Git repository into an existing Git repository.
# Classification (U)

# Description:
  The program is designed to take an outside local Git repository and merge it into an existing remote Git repository.  It will, however, make the local Git repository the priority repository.  This is a way of an outside repository being modified and then merging those modifications into an existing remote Git respository.

###  This README file is broken down into the following sections:
  * Features
  * Prerequisites
  * Installation
  * Configuration
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

