# Python project for the merging of a non-local Git repository into an existing Git repository.
# Classification (U)

# Description:
  This program is used to take a non-local Git repository that has been modified at a different location and merge it into an existing Git repository and make it the priority repository.

###  This README file is broken down into the following sections:
  * Features
  * Prerequisites
  * Installation
  * Program Description
  * Program Help Function
  * Help Message
  * Testing
    - Unit
    - Integration
    - Blackbox


# Features:
  * Clean up an dirty files in the non-local repository prior to merging.
  * Fetch the remote Git repository along side the non-local repository.
  * Merge the non-local repository into the remote repository, but make the non-local repository the priority.
  * Push the newly merged respository back to the remote Git respository.


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
cd check-log
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.
```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
```


# Program Descriptions:
### Program: merge_repo.py
##### Description: The merge_repo.py program is designed to take a non-local Git repository and merge it into an existing Git repository, but make the non-local Git repository the priority repository.  This is way of a non-local repository being modified and those modifications being merged into an existing baseline on the remote Git respository.  The master branch will be the designated branch which will incur the changes.


# Program Help Function:

  All of the programs, except the command and class files, will have an -h (Help option) that will show display a help message for that particular program.  The help message will usually consist of a description, usage, arugments to the program, example, notes about the program, and any known bugs not yet fixed.  To run the help command:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
{Python_Project}/merge-repo/merge_repo.py -h
```


# Help Message:
  Below is the help message for each of the programs along with the current version for the program.  Recommend running the -h option on the command line to ensure you have the latest help message for the program.

    Program:  merge_repo.py

    Description:  

    Usage:
`

    Arguments:
        -v => Display version of this program.
        -h => Help and usage message.

        NOTE 1:  -v or -h overrides the other options.

    Example:


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
```

# Unit test runs for merge_repo.py:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/merge-repo
```

### Unit tests
```
test/unit/merge_repo/help_message.py
test/unit/merge_repo/NNNN.py
test/unit/merge_repo/NNNN.py
test/unit/merge_repo/NNNN.py
test/unit/merge_repo/NNNN.py
test/unit/merge_repo/NNNN.py
test/unit/merge_repo/NNNN.py
test/unit/merge_repo/NNNN.py
test/unit/merge_repo/NNNN.py
test/unit/merge_repo/NNNN.py
test/unit/merge_repo/NNNN.py
test/unit/merge_repo/run_program.py
test/unit/merge_repo/main.py
```

### All unit testing
```
test/unit/merge_repo/unit_test_run.sh
```

### Code coverage program
```
test/unit/merge_repo/code_coverage.sh
```


# Integration Testing:

### Description: Testing consists of integration testing of functions in the merge_repo.py program.

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
```

# Integration test runs for merge_repo.py:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/merge-repo
```

### Integration tests
```
test/integration/merge_repo/NNNN.py
test/integration/merge_repo/NNNN.py
test/integration/merge_repo/NNNN.py
test/integration/merge_repo/NNNN.py
test/integration/merge_repo/NNNN.py
test/integration/merge_repo/NNNN.py
test/integration/merge_repo/NNNN.py
test/integration/merge_repo/NNNN.py
test/integration/merge_repo/NNNN.py
test/integration/merge_repo/NNNN.py
test/integration/merge_repo/run_program.py
test/integration/merge_repo/main.py
```

### All integration testing
```
test/integration/merge_repo/integration_test_run.sh
```

### Code coverage program
```
test/integration/merge_repo/code_coverage.sh
```


# Blackbox Testing:

### Description: Testing consists of blackbox testing of the merge_repo.py program.

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
```

# Blackbox test run for merge_repo.py:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/merge-repo
```

### Blackbox:  
```
test/blackbox/merge_repo/blackbox_test.sh
```

