#!/bin/bash
# Unit test code coverage for git_class.py module.
# This will run the Python code coverage module against all unit test modules.
# This will show the amount of code that was tested and which lines of code
#	that was skipped during the test.

coverage erase

echo ""
echo "Running unit test modules in conjunction with coverage"
coverage run -a --source=git_class test/unit/git_class/gitmerge_init.py
coverage run -a --source=git_class test/unit/git_class/gitmerge_create_gitrepo.py
coverage run -a --source=git_class test/unit/git_class/gitmerge_set_remote.py
coverage run -a --source=git_class test/unit/git_class/gitmerge_is_remote.py
coverage run -a --source=git_class test/unit/git_class/gitmerge_process_dirty.py
coverage run -a --source=git_class test/unit/git_class/gitmerge_process_untracked.py
coverage run -a --source=git_class test/unit/git_class/gitclass_init.py
coverage run -a --source=git_class test/unit/git_class/gitclass_create_repo.py
coverage run -a --source=git_class test/unit/git_class/gitclass_create_cmd.py

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
