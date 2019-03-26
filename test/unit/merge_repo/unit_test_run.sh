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
echo "Unit test:  is_remote_branch"
test/unit/merge_repo/is_remote_branch.py

echo ""
echo "Unit test:  process_dirty"
test/unit/merge_repo/process_dirty.py

echo ""
echo "Unit test:  process_untracked"
test/unit/merge_repo/process_untracked.py

echo ""
echo "Unit test:  send_mail"
test/unit/merge_repo/send_mail.py

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

