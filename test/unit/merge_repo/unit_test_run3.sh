#!/bin/bash
# Unit testing program for the merge_repo.py module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file
#   is located at.

echo ""
echo "Unit testing merge_repo.py"
/usr/bin/python3 test/unit/merge_repo/detach_head.py
/usr/bin/python3 test/unit/merge_repo/load_cfg.py
/usr/bin/python3 test/unit/merge_repo/is_git_repo.py
/usr/bin/python3 test/unit/merge_repo/prepare_mail.py
/usr/bin/python3 test/unit/merge_repo/post_process.py
/usr/bin/python3 test/unit/merge_repo/post_check.py
/usr/bin/python3 test/unit/merge_repo/merge_project.py
/usr/bin/python3 test/unit/merge_repo/send_mail.py
/usr/bin/python3 test/unit/merge_repo/quarantine_files.py
/usr/bin/python3 test/unit/merge_repo/quarantine.py
/usr/bin/python3 test/unit/merge_repo/post_body.py
/usr/bin/python3 test/unit/merge_repo/process_project.py
/usr/bin/python3 test/unit/merge_repo/process_changes.py
/usr/bin/python3 test/unit/merge_repo/merge.py
/usr/bin/python3 test/unit/merge_repo/cleanup_repo.py
/usr/bin/python3 test/unit/merge_repo/help_message.py
/usr/bin/python3 test/unit/merge_repo/run_program.py
/usr/bin/python3 test/unit/merge_repo/main.py

