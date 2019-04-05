#!/bin/bash
# Unit test code coverage for merge_repo.py module.
# This will run the Python code coverage module against all unit test modules.
# This will show the amount of code that was tested and which lines of code
#	that was skipped during the test.

coverage erase

echo ""
echo "Running unit test modules in conjunction with coverage"
coverage run -a --source=merge_repo test/unit/merge_repo/is_git_repo.py
coverage run -a --source=merge_repo test/unit/merge_repo/load_cfg.py
coverage run -a --source=merge_repo test/unit/merge_repo/merge.py
coverage run -a --source=merge_repo test/unit/merge_repo/process_project.py
coverage run -a --source=merge_repo test/unit/merge_repo/is_commits_ahead.py
coverage run -a --source=merge_repo test/unit/merge_repo/is_commits_behind.py
coverage run -a --source=merge_repo test/unit/merge_repo/commits_diff.py
coverage run -a --source=merge_repo test/unit/merge_repo/is_remote.py
coverage run -a --source=merge_repo test/unit/merge_repo/is_remote_branch.py
coverage run -a --source=merge_repo test/unit/merge_repo/process_dirty.py
coverage run -a --source=merge_repo test/unit/merge_repo/process_untracked.py
coverage run -a --source=merge_repo test/unit/merge_repo/send_mail.py
coverage run -a --source=merge_repo test/unit/merge_repo/help_message.py
coverage run -a --source=merge_repo test/unit/merge_repo/run_program.py
coverage run -a --source=merge_repo test/unit/merge_repo/main.py

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
