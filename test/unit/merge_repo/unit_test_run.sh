#!/bin/bash
# Unit testing program for the merge_repo.py module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file
#   is located at.

echo ""
echo "Unit test:  load_cfg"
test/unit/merge_repo/load_cfg.py

echo ""
echo "Unit test:  is_git_repo"
test/unit/merge_repo/is_git_repo.py

echo ""
echo "Unit test:  prepare_mail"
test/unit/merge_repo/prepare_mail.py

echo ""
echo "Unit test:  move"
test/unit/merge_repo/move.py

echo ""
echo "Unit test:  post_process"
test/unit/merge_repo/post_process.py

echo ""
echo "Unit test:  post_check"
test/unit/merge_repo/post_check.py

echo ""
echo "Unit test:  merge_project"
test/unit/merge_repo/merge_project.py

echo ""
echo "Unit test:  send_mail"
test/unit/merge_repo/send_mail.py

echo ""
echo "Unit test:  quarantine_files"
test/unit/merge_repo/quarantine_files.py

echo ""
echo "Unit test:  quarantine"
test/unit/merge_repo/quarantine.py

echo ""
echo "Unit test:  post_body"
test/unit/merge_repo/post_body.py

echo ""
echo "Unit test:  process_project"
test/unit/merge_repo/process_project.py

echo ""
echo "Unit test:  merge"
test/unit/merge_repo/merge.py

echo ""
echo "Unit test:  help_message"
test/unit/merge_repo/help_message.py

echo ""
echo "Unit test:  run_program"
test/unit/merge_repo/run_program.py

echo ""
echo "Unit test:  main"
test/unit/merge_repo/main.py

