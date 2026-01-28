Sphinx-Gitref Example
=====================

This page demonstrates the **sphinx-gitref** extension for referencing Git repositories, commits, and branches directly in Sphinx documentation.

.. contents:: Contents
   :local:
   :depth: 2

Overview
--------

The sphinx-gitref extension provides roles and directives for linking to Git repositories, commits, branches, tags, and files in version control systems.

Basic Git References
--------------------

Repository References
~~~~~~~~~~~~~~~~~~~~~

Link to repositories:

- GitHub repo: :gitrepo:`sphinx-doc/sphinx`
- GitLab repo: :gitrepo:`gitlab-org/gitlab`
- Custom repo: :gitrepo:`myorg/myproject@https://git.example.com`

Commit References
~~~~~~~~~~~~~~~~~

Reference specific commits:

- Short hash: :gitcommit:`abc1234`
- Full hash: :gitcommit:`abc1234567890abcdef1234567890abcdef12345`
- Commit with message: :gitcommit:`abc1234` - "Fix critical bug in parser"
- Commit from specific repo: :gitcommit:`sphinx-doc/sphinx@abc1234`

Branch and Tag References
--------------------------

Branch References
~~~~~~~~~~~~~~~~~

Link to branches:

- Main branch: :gitbranch:`main`
- Development branch: :gitbranch:`develop`
- Feature branch: :gitbranch:`feature/new-parser`
- Release branch: :gitbranch:`release/2.0`

Tag References
~~~~~~~~~~~~~~

Reference version tags:

- Latest release: :gittag:`v2.0.0`
- Specific version: :gittag:`v1.5.2`
- Beta tag: :gittag:`v2.0.0-beta1`

File References
---------------

File at HEAD
~~~~~~~~~~~~

Reference files in the repository:

- Source file: :gitfile:`src/parser.py`
- Documentation: :gitfile:`docs/index.rst`
- Configuration: :gitfile:`setup.cfg`

File at Specific Commit
~~~~~~~~~~~~~~~~~~~~~~~~

Link to file at particular version:

- Old version: :gitfile:`src/parser.py@abc1234`
- Tagged version: :gitfile:`README.md@v1.0.0`
- Branch version: :gitfile:`docs/tutorial.rst@develop`

File Range
~~~~~~~~~~

Reference specific lines in a file:

- Single line: :gitfile:`src/main.py#L42`
- Line range: :gitfile:`src/utils.py#L100-L150`
- At commit: :gitfile:`src/config.py@abc1234#L25-L30`

Comparison References
---------------------

Compare Branches
~~~~~~~~~~~~~~~~

Show differences between branches:

.. gitcompare:: main..develop
   
   Compare main branch with develop branch

Compare Tags
~~~~~~~~~~~~

Compare version releases:

.. gitcompare:: v1.0.0..v2.0.0
   
   Changes from version 1.0.0 to 2.0.0

Compare Commits
~~~~~~~~~~~~~~~

Diff between commits:

.. gitcompare:: abc1234..def5678
   
   Changes between two specific commits

Pull Request References
------------------------

GitHub Pull Requests
~~~~~~~~~~~~~~~~~~~~

Reference pull requests:

- Simple PR: :gitpr:`123`
- PR with title: :gitpr:`456` - "Add new feature"
- PR from repo: :gitpr:`sphinx-doc/sphinx#789`

Merge Requests (GitLab)
~~~~~~~~~~~~~~~~~~~~~~~

GitLab merge requests:

- Simple MR: :gitmr:`!123`
- MR with description: :gitmr:`!456` - "Fix documentation"
- MR from project: :gitmr:`gitlab-org/gitlab!789`

Git History Display
-------------------

Commit Log
~~~~~~~~~~

Display commit history:

.. gitlog::
   :limit: 5
   :branch: main
   
   Shows last 5 commits from main branch

Filtered Log
~~~~~~~~~~~~

Show filtered history:

.. gitlog::
   :author: john@example.com
   :since: 2024-01-01
   :until: 2024-12-31
   :grep: "fix bug"
   
   Shows commits by john@example.com in 2024 containing "fix bug"

Log with Stats
~~~~~~~~~~~~~~

Include file change statistics:

.. gitlog::
   :limit: 3
   :stat:
   :graph:
   
   Shows last 3 commits with file statistics and graph

Contributor Information
-----------------------

Author References
~~~~~~~~~~~~~~~~~

Link to contributors:

- GitHub user: :gitauthor:`octocat`
- Author email: :gitauthor:`john@example.com`
- Full name: :gitauthor:`John Doe <john@example.com>`

Contributors List
~~~~~~~~~~~~~~~~~

Display contributors:

.. gitcontributors::
   :limit: 10
   :sort: commits
   
   Top 10 contributors sorted by commit count

Blame Information
~~~~~~~~~~~~~~~~~

Show file blame:

.. gitblame:: src/parser.py
   :lines: 100-150
   
   Shows who last modified lines 100-150

Repository Statistics
---------------------

Commit Statistics
~~~~~~~~~~~~~~~~~

.. gitstats::
   :type: commits
   :period: month
   :count: 12
   
   Monthly commit count for last 12 months

Code Churn
~~~~~~~~~~

.. gitstats::
   :type: churn
   :files: src/**/*.py
   
   Code churn statistics for Python files in src/

Contribution Graph
~~~~~~~~~~~~~~~~~~

.. gitstats::
   :type: contributions
   :format: heatmap
   :author: all
   
   Contribution heatmap for all authors

Configuration Examples
----------------------

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_gitref',
   ]
   
   # Git repository configuration
   gitref_repository = 'https://github.com/myorg/myproject'
   gitref_default_branch = 'main'

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Multiple repositories
   gitref_repositories = {
       'default': 'https://github.com/myorg/myproject',
       'docs': 'https://github.com/myorg/documentation',
       'lib': 'https://github.com/myorg/library',
   }
   
   # Reference format
   gitref_commit_format = 'short'  # 'short', 'long', or 'abbreviated'
   gitref_link_format = 'github'   # 'github', 'gitlab', 'bitbucket'
   
   # Display options
   gitref_show_hash = True
   gitref_show_message = True
   gitref_show_author = False
   gitref_show_date = True

Custom Formats
~~~~~~~~~~~~~~

.. code-block:: python

   # Custom commit reference format
   gitref_commit_template = '{hash} by {author} on {date}'
   
   # Custom file reference format
   gitref_file_template = '{file}@{ref}#{lines}'
   
   # Link targets
   gitref_link_target = '_blank'  # Open links in new tab

Integration Features
--------------------

With Version Control
~~~~~~~~~~~~~~~~~~~~

Automatically extract current branch/commit:

.. gitcurrent::
   
   Shows current Git branch and commit

With Build Information
~~~~~~~~~~~~~~~~~~~~~~

Include Git info in build:

.. gitbuildinfo::
   :show-branch:
   :show-commit:
   :show-date:
   :show-dirty:
   
   Displays build information including Git status

Release Notes
~~~~~~~~~~~~~

Generate release notes from commits:

.. gitreleasenotes::
   :from: v1.0.0
   :to: v2.0.0
   :group-by: type
   
   **Features**
   
   - Added new parser engine
   - Improved error messages
   
   **Bug Fixes**
   
   - Fixed memory leak in tokenizer
   - Corrected edge case in validator

Changelog Generation
--------------------

Automatic Changelog
~~~~~~~~~~~~~~~~~~~

.. gitchangelog::
   :versions: v2.0.0, v1.5.0, v1.0.0
   :format: markdown
   
   Generates changelog from Git history

Grouped Changelog
~~~~~~~~~~~~~~~~~

.. gitchangelog::
   :since: v1.0.0
   :group-by: type
   :types: feat, fix, docs, chore
   
   Groups commits by type (requires conventional commits)

Practical Examples
------------------

Documentation Versioning
~~~~~~~~~~~~~~~~~~~~~~~~

Track documentation changes:

This documentation applies to version :gittag:`v2.0.0`. 
For previous version, see :gitfile:`docs/index.rst@v1.0.0`.

The main configuration file :gitfile:`conf.py` was last modified 
in commit :gitcommit:`abc1234`.

Code Examples with Links
~~~~~~~~~~~~~~~~~~~~~~~~~

Reference code directly:

The :gitfile:`src/parser.py#L100-L150` contains the main parsing logic.
See the implementation added in :gitcommit:`def5678`.

For the previous implementation, check 
:gitfile:`src/old_parser.py@v1.0.0#L50-L75`.

Change Tracking
~~~~~~~~~~~~~~~

Track feature development:

**Feature: New Parser**

- Initial implementation: :gitcommit:`aaa1111`
- Performance improvements: :gitcommit:`bbb2222`
- Bug fixes: :gitcommit:`ccc3333`
- Merged to main: :gitpr:`123`

Changes can be reviewed in :gitcompare:`main..feature/new-parser`

Repository Overview
~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Current Repository Status
   -------------------------
   
   - Branch: :gitbranch:`main`
   - Latest commit: :gitcommit:`abc1234`
   - Latest tag: :gittag:`v2.0.0`
   - Contributors: :gitcontributors:`count`
   
   Recent activity::
   
      .. gitlog::
         :limit: 5
         :format: oneline

Cross-Repository References
----------------------------

Multiple Projects
~~~~~~~~~~~~~~~~~

Reference across repositories:

- Main project: :gitfile:`myorg/project@src/main.py`
- Documentation: :gitfile:`myorg/docs@index.rst`
- Library: :gitfile:`myorg/lib@api/core.py`

Submodules
~~~~~~~~~~

Reference submodule commits:

.. gitsubmodule:: third_party/parser
   :commit: abc1234
   
   Shows submodule reference

See Also
--------

- :doc:`../tutorials/packages/sphinx-gitref` - Complete tutorial
- Official documentation: https://sphinx-gitref.readthedocs.io/
- GitHub repository: https://github.com/sphinx-doc/sphinx-gitref
