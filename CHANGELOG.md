# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


## [0.2.1] - 2019-09-24
### Fixed
- quarantine_files:  Allow directories to be quarantined in addition to files.

### Changed
- Documentation update.


## [0.2.0] - 2019-09-03
### Changed
- merge:  Set the "url" depending on "-a" option setting.  To allow multiple deploy keys in a Github repository.
- main:  Changed variable name to standard naming convention.
- config/merge.py.TEMPLATE:  Removed "url" entry.  No longer required.
- config/merge.py.TEMPLATE:  Added "git_project", "git_server", and "prefix" entries.


## [0.1.1] - 2019-06-14
### Changed
- merge:  Update the local Git config file with a local user name and email address.


## [0.1.0] - 2019-06-04
### Added
- process_changes:  Process dirty and untracked files.

### Changed
- Changed import of git_class to a sub-directory.
- main:  Added ability to accept keywords arguments into function.  Will allow wrapper program to implment program.
- merge:  Added Log instance to post_process calls.
- merge:  Replaced dirty and untrack code with call to process_changes function.
- process_project:  Added Log instance to post_process calls.
- merge_project:  Added Log instance to post_process calls.
- quarantine:  Removed get_dirty and get_untracked calls and added Log instance to post_process calls.
- quarantine_files:  Change file quarantine to directory to quarantine file to show move properly.
- post_check:  Added Log instance to post_process calls.
- post_process:  Added Log class instance to function to record entries to log.


## [0.0.4] - 2019-04-29
### Added
- post_body:  Append default post-header to mail body.
- quarantine_files:  Copy files out of Git repo into a quarantine directory.
- quarantine:  Get dirty and untracked files and quarantine them.

### Fixed
- process_project:  Corrected call to git_fetch method.
- prepare_mail:  Corrected logic in 'if' statement.
- prepare_mail:  Fixed problem with mutable default arguments issue.
- post_process:  Fixed problem with mutable default arguments issue.
- merge:  Fixed problem with mutable default arguments issue.
- run_program:  Fixed problem with mutable default arguments issue.
- send_mail:  Added newline for each line in email.
- post_check:  Added branch name as arg to is_commits_ahead and is_commits_behind calls.

### Changed
- config/merge.py.TEMPLATE:  Added quar_dir entry.
- Added function name to log entries.
- main:  Set the repo name for -r option if not passed to program using -p option setting.
- merge:  Added quarantine function call to quarantine new/modified files.
- merge:  Added arguments to process_dirty and process_untracked method calls.
- prepare_mail:  Replaced post body mail lines with call to post_body function.
- post_process:  Added datetime to destination directory for the archiving of the repo.
- merge:  Added datetime to destination directory for the archiving of the repo.
- merge_project:  Added additional logging error statements.
- process_project:  Added additional logging error statements.


## [0.0.3] - 2019-04-03
### Added
- prepare_mail:  Build body of email message with a set of standard lines.
- commits_diff:  Returns count difference between two branches.
- is_commits_ahead:  Returns count on local branch ahead of remote branch.
- is_commits_behind:  Returns count on local branch behind remote branch.

### Changed
- Modified the program to use the git_class module, which the program will interface with Git through.
- merge:  Added check to see if local and remote branches are in sync.


## [0.0.2] - 2019-04-02
### Added
- is_remote:  Determines if the remote git repository exists.

### Changed
- merge:  Replaced is_remote_branch() call with is_remote() call.
- process_project:  Add second push() to push only changes.
- process_project:  Add log entries.


## [0.0.1] - 2019-03-19
- Initial creation.

