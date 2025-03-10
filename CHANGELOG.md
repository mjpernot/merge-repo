# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


## [1.1.4] - 2025-02-28
- Updated git-lib to v1.0.10

### Changed
- quarantine_files: Set subj variable to a default value.
- Documentation changes.


## [1.1.3] - 2024-11-22
- Updated distro==1.9.0 for Python 3
- Added smmap==5.0.0 for Python 3
- Added gitdb==4.0.9 for Python 3
- Updated GitPython==3.1.18 for Python 3
- Updated simplejson==3.13.2 for Python 3
- Removed smmap2 for Python 3
- Removed gitdb2 for Python 3
- Updated python-lib to v3.0.8
- Updated git-lib to v1.0.9

### Deprecated
- Support for Python 2.7


## [1.1.2] - 2024-09-10

### Changed
- main: Removed parsing from gen_class.ArgParser call and called arg_parse2 as part of "if" statement.


## [1.1.1] - 2024-03-04
- Updated to work in Red Hat 8
- Updated python-lib to v3.0.3
- Updated git-lib to v1.0.5

### Changed
- Set gitdb2 to 2.0.5 for Python 3.
- Set simplejson to 3.12.0 for Python 3.
- Set chardet to 3.0.4 for Python 2.
- Documentation updates.


## [1.1.0] - 2023-10-17
- Replaced the arg_parser code with gen_class.ArgParser code.
- Upgraded python-lib to v2.10.1

### Changed
- Multiple functions: Replaced the arg_parser code with gen_class.ArgParser code.
- main: Removed gen_libs.get_inst call.
- Documentation updates.


## [1.0.2] - 2022-12-21
- Updated to work in Python 3 too
- Upgraded python-lib to v2.9.4

### Changed
- Converted imports to use Python 2.7 or Python 3.
- prepare_mail, main:  Converted dictionary keys() call to list.


## [1.0.1] - 2021-03-03
- Upgraded python-lib to v2.9.0

### Fixed
- merge: Copied the original repository into archive directory prior to processing.

### Added
- Added -u option to allow for unrelated Git repository histories to be merged.

### Changed
- merge, post_process: Replaced "move" function call with gen_libs.mv_file2 library call.
- send_mail: Added "newline" option to add_2_msg method call.
- Renamed \_process_changes to cleanup_repo to avoid naming conflict.
- merge_project:  Added "allow" option to gitr.priority_merge call.
- merge:  Processed "-u" option from args_array and passed to \_process_changes call.
- process_project:  Added kwargs passing to merge_project call.
- \_process_changes:  Added kwargs passing to process_project call.
- Documentation updates.

### Removed
- move function


## [1.0.0] - 2021-02-23
- General Release.
- Added -n option and/or setting to_line to None to not send out email notifications.

### Changed
- post_process, quarantine_files, quarantine, merge:  If no "to email" address is detected, do not send email notifications.
- run_program:  Process -n option if detected in the command line arguments.
- run_program: Process error messages from load_cfg function.
- load_cfg:  Return list of error messages detected to calling function.
- Removed unnecessary \*\*kwargs from argument list.
- config/merge.py.TEMPLATE:  Set "merge-repo" as the base directory structure.
- Documentation updates.

### Removed
- distutils.dir_util module.


## [0.3.2] - 2020-03-26
### Fixed
- main:  Fixed handling command line arguments from SonarQube scan finding.
- merge_project, process_project:  Fixed literal SonarQube scan finding.
- detach_head:  Fixed incorrect referencing of branches attribute in Gitmerge class.

### Changed
- detach_head:  Added no_chk to remove_branch call and captured returning status codes.
- Documentation update.


## [0.3.1] - 2020-02-26
### Changed
- merge:  Added calls to \_process_changes and detach_head and check on the status of detach head.

### Added
- \_process_changes:  Private function for merge function to reduce function complexity.
- detach_head:  Detach the head from a project and remove the existing branch.


## [0.3.0] - 2019-11-21
- Field release

### Fixed
- quarantine_files: Fixed error in which each item was written to a seperate sub-directory.

### Changed
- quarantine_files:  Send only one email for all quarantined items identified.
- quarantine_files:  Refactored the function to be more streamline and reduce complexity of the code.


## [0.2.2] - 2019-10-04
### Fixed
- quarantine_files:  Copy the directory and items under the directory to the quarantine directory.

### Changed
- quarantine_files:  Quarantined items will be moved to under a repo project directory instead of individual items.


## [0.2.1] - 2019-09-26
### Fixed
- main:  Added check to see if "-p" option is present when setting "-r" option.
- quarantine_files:  Allow directories to be quarantined in addition to files.

### Changed
- Documentation update.


## [0.2.0] - 2019-09-03
### Changed
- merge:  Set the "url" depending on "-a" option setting.  To allow multiple deploy keys in a Github repository.
- main:  Changed variable name to standard naming convention.
- config/merge.py.TEMPLATE:  Removed "url" entry.  Added "git_project", "git_server", and "prefix" entries.


## [0.1.1] - 2019-06-14
### Changed
- merge:  Update the local Git config file with a local user name and email address.


## [0.1.0] - 2019-06-04
### Added
- process_changes:  Process dirty and untracked files.

### Changed
- Changed import of git_class to a sub-directory.
- main:  Added ability to accept keywords arguments into function.  Will allow wrapper program to implment program.
- merge:  Replaced dirty and untrack code with call to process_changes function.
- post_check, merge, merge_project, process_project:  Added Log instance to post_process calls.
- quarantine:  Removed get_dirty and get_untracked calls and added Log instance to post_process calls.
- quarantine_files:  Change file quarantine to directory to quarantine file to show move properly.
- post_process:  Added Log class instance to function to record entries to log.


## [0.0.4] - 2019-04-29
### Added
- post_body:  Append default post-header to mail body.
- quarantine_files:  Copy files out of Git repo into a quarantine directory.
- quarantine:  Get dirty and untracked files and quarantine them.

### Fixed
- process_project:  Corrected call to git_fetch method.
- prepare_mail:  Corrected logic in 'if' statement.
- run_program, merge, post_process, prepare_mail:  Fixed problem with mutable default arguments issue.
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
- process_project, merge_project:  Added additional logging error statements.


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

