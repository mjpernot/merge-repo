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
    - Integration (Not yet implemented)
    - Blackbox (Not yet implemented)


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
  * "url" is URL address to the Git repository.  Do not include the project name in the url.
  * "work_dir" is the directory where the merge will take place.
  * "err_dir" is the directory where a project will be archive if an error occurs.
  * "archive_dir" is the directory where the project will be save to after the merge.
  * "quar_dir" is the directory where items that are not processed will be saved to.
  * "to_line" is one or more email addresses to receive emails from the program.
  * "log_file" is the directory path and log file name for the program.
  * "name" is the name of the Git user for the local repository.
  * "email" is the email address of the Git user for the local repository.

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

### Unit tests
```
cd {Python_Project}/merge-repo
test/unit/merge_repo/merge_project.py
test/unit/merge_repo/is_git_repo.py
test/unit/merge_repo/post_check.py
test/unit/merge_repo/post_process.py
test/unit/merge_repo/move.py
test/unit/merge_repo/prepare_mail.py
test/unit/merge_repo/send_mail.py
test/unit/merge_repo/quarantine.py
test/unit/merge_repo/quarantine_files.py
test/unit/merge_repo/post_body.py
test/unit/merge_repo/load_cfg.py
test/unit/merge_repo/merge.py
test/unit/merge_repo/process_project.py
test/unit/merge_repo/process_changes.py
test/unit/merge_repo/help_message.py
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
  * "url" is URL address to the Git repository.  Do not include the project name in the url.
  * "work_dir" is the directory where the merge will take place.
  * "err_dir" is the directory where a project will be archive if an error occurs.
  * "archive_dir" is the directory where the project will be save to after the merge.
  * "quar_dir" is the directory where items that are not processed will be saved to.
  * "to_line" is one or more email addresses to receive emails from the program.
  * "log_file" is the directory path and log file name for the program.
  * "name" is the name of the Git user for the local repository.
  * "email" is the email address of the Git user for the local repository.

```
vim merge.py
```

# Integration test runs for merge_repo.py:
  * Replace **{Python_Project}** with the baseline path of the python program.

### Integration tests
```
cd {Python_Project}/merge-repo
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
  * "url" is URL address to the Git repository.  Do not include the project name in the url.
  * "work_dir" is the directory where the merge will take place.
  * "err_dir" is the directory where a project will be archive if an error occurs.
  * "archive_dir" is the directory where the project will be save to after the merge.
  * "quar_dir" is the directory where items that are not processed will be saved to.
  * "to_line" is one or more email addresses to receive emails from the program.
  * "log_file" is the directory path and log file name for the program.
  * "name" is the name of the Git user for the local repository.
  * "email" is the email address of the Git user for the local repository.

```
vim merge.py
```

# Blackbox test run for merge_repo.py:
  * Replace **{Python_Project}** with the baseline path of the python program.

### Blackbox test:  
```
cd {Python_Project}/merge-repo
test/blackbox/merge_repo/blackbox_test.sh
```

