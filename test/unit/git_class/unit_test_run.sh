#!/bin/bash
# Unit testing program for the git_class.py module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file
#   is located at.

echo ""
echo "Unit test:  gitmerge_init"
test/unit/git_class/gitmerge_init.py

echo ""
echo "Unit test:  gitmerge_create_gitrepo"
test/unit/git_class/gitmerge_create_gitrepo.py

echo ""
echo "Unit test:  gitmerge_set_remote"
test/unit/git_class/gitmerge_set_remote.py

echo ""
echo "Unit test:  gitmerge_is_remote"
test/unit/git_class/gitmerge_is_remote.py

echo ""
echo "Unit test:  gitmerge_process_dirty"
test/unit/git_class/gitmerge_process_dirty.py

echo ""
echo "Unit test:  gitmerge_process_untracked"
test/unit/git_class/gitmerge_process_untracked.py

echo ""
echo "Unit test:  gitclass_init"
test/unit/git_class/gitclass_init.py

echo ""
echo "Unit test:  gitclass_create_repo"
test/unit/git_class/gitclass_create_repo.py

echo ""
echo "Unit test:  gitclass_create_cmd"
test/unit/git_class/gitclass_create_cmd.py

