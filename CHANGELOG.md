# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


## [0.0.3] - 2019-04-03
### Added
- commits_diff:  Returns count difference between two branches.
- is_commits_ahead:  Returns count on local branch ahead of remote branch.
- is_commits_behind:  Returns count on local branch behind remote branch.

### Changed
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

