#!/bin/bash
# Unit test code coverage for merge_repo.py module.
# This will run the Python code coverage module against all unit test modules.
# This will show the amount of code that was tested and which lines of code
#	that was skipped during the test.

coverage erase

echo ""
echo "Running unit test modules in conjunction with coverage"
coverage run -a --source=merge_repo test/unit/merge_repo/detach_head.py
coverage run -a --source=merge_repo test/unit/merge_repo/is_git_repo.py
coverage run -a --source=merge_repo test/unit/merge_repo/load_cfg.py
coverage run -a --source=merge_repo test/unit/merge_repo/merge.py
coverage run -a --source=merge_repo test/unit/merge_repo/_process_changes.py
coverage run -a --source=merge_repo test/unit/merge_repo/process_project.py
coverage run -a --source=merge_repo test/unit/merge_repo/process_changes.py
coverage run -a --source=merge_repo test/unit/merge_repo/prepare_mail.py
coverage run -a --source=merge_repo test/unit/merge_repo/move.py
coverage run -a --source=merge_repo test/unit/merge_repo/post_process.py
coverage run -a --source=merge_repo test/unit/merge_repo/post_check.py
coverage run -a --source=merge_repo test/unit/merge_repo/merge_project.py
coverage run -a --source=merge_repo test/unit/merge_repo/send_mail.py
coverage run -a --source=merge_repo test/unit/merge_repo/quarantine_files.py
coverage run -a --source=merge_repo test/unit/merge_repo/quarantine.py
coverage run -a --source=merge_repo test/unit/merge_repo/post_body.py
coverage run -a --source=merge_repo test/unit/merge_repo/help_message.py
coverage run -a --source=merge_repo test/unit/merge_repo/run_program.py
coverage run -a --source=merge_repo test/unit/merge_repo/main.py

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
