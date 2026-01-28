Sphinx-Git Example
==================

This page demonstrates the **sphinx-git** extension for including Git repository information in Sphinx documentation.

.. contents:: Contents
   :local:
   :depth: 2

Overview
--------

The sphinx-git extension provides directives for displaying Git changelog, commit history, and repository information directly in your documentation.

Basic Configuration
-------------------

Setup
~~~~~

.. code-block:: python

   # conf.py
   extensions = [
       'sphinxcontrib.git',
   ]

Changelog Directive
-------------------

Basic Changelog
~~~~~~~~~~~~~~~

.. code-block:: rst

   .. git_changelog::

This displays all commits in reverse chronological order.

Limited Commits
~~~~~~~~~~~~~~~

.. code-block:: rst

   .. git_changelog::
      :revisions: 10

Shows only the last 10 commits.

Specific Branch
~~~~~~~~~~~~~~~

.. code-block:: rst

   .. git_changelog::
      :rev-list: main
      :revisions: 5

Shows last 5 commits from the main branch.

Date Range
~~~~~~~~~~

.. code-block:: rst

   .. git_changelog::
      :since: 2024-01-01
      :until: 2024-01-31

Shows commits within date range.

Commit Details
--------------

Detailed Format
~~~~~~~~~~~~~~~

.. code-block:: rst

   .. git_changelog::
      :detailed-message-pre: True
      :revisions: 5

Shows full commit messages with formatting.

Author Information
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. git_changelog::
      :include-author: True
      :revisions: 10

Includes commit author names.

Commit Hash
~~~~~~~~~~~

.. code-block:: rst

   .. git_changelog::
      :include-commit: True
      :revisions: 10

Shows commit hashes.

Filtering
---------

By File Path
~~~~~~~~~~~~

.. code-block:: rst

   .. git_changelog::
      :filename_filter: docs/

Shows only commits that modified files in ``docs/``.

By Pattern
~~~~~~~~~~

.. code-block:: rst

   .. git_changelog::
      :filename_filter: *.py

Shows commits that modified Python files.

Exclude Patterns
~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. git_changelog::
      :filename_filter: .
      :exclude: docs/_build/

Exclude certain paths from changelog.

Formatting Options
------------------

Custom Format
~~~~~~~~~~~~~

.. code-block:: rst

   .. git_changelog::
      :format: [{date}] {subject} - {author}
      :revisions: 10

Available placeholders:

- ``{date}`` - Commit date
- ``{subject}`` - Commit message (first line)
- ``{author}`` - Author name
- ``{hash}`` - Commit hash
- ``{abbrev_hash}`` - Short hash

Grouping by Date
~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. git_changelog::
      :group-by-date: True
      :revisions: 20

Groups commits by date.

Grouping by Author
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. git_changelog::
      :group-by-author: True
      :revisions: 20

Groups commits by author.

Commit Directive
----------------

Single Commit
~~~~~~~~~~~~~

.. code-block:: rst

   .. git_commit:: abc123

Shows details of a specific commit.

Full Details
~~~~~~~~~~~~

.. code-block:: rst

   .. git_commit:: abc123
      :include-diff: True

Includes the diff of the commit.

Multiple Commits
~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. git_commit:: abc123 def456 ghi789

Shows multiple specific commits.

Repository Information
----------------------

Repository Stats
~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. git_stats::

Shows repository statistics:

- Total commits
- Number of contributors
- Date range

Branch Information
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. git_branch_info::

Shows current branch and available branches.

Tag Information
~~~~~~~~~~~~~~~

.. code-block:: rst

   .. git_tag_list::

Lists all Git tags.

Practical Examples
------------------

Release Notes
~~~~~~~~~~~~~

.. code-block:: rst

   Release History
   ===============
   
   Version 2.0.0
   -------------
   
   .. git_changelog::
      :since: v1.9.0
      :until: v2.0.0
      :detailed-message-pre: True
      :include-author: True

Contributor List
~~~~~~~~~~~~~~~~

.. code-block:: rst

   Contributors
   ============
   
   Thank you to all contributors:
   
   .. git_changelog::
      :group-by-author: True
      :include-author: True

Recent Changes
~~~~~~~~~~~~~~

.. code-block:: rst

   Recent Updates
   ==============
   
   .. git_changelog::
      :revisions: 5
      :include-commit: True
      :format: [{abbrev_hash}] {date}: {subject} ({author})

File History
~~~~~~~~~~~~

.. code-block:: rst

   Documentation Changes
   =====================
   
   .. git_changelog::
      :filename_filter: docs/
      :revisions: 10
      :detailed-message-pre: True

Advanced Configuration
----------------------

Custom Templates
~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   git_changelog_template = '''
   <div class="commit">
       <div class="commit-header">
           <span class="commit-hash">{{ commit.hash[:7] }}</span>
           <span class="commit-date">{{ commit.date }}</span>
       </div>
       <div class="commit-message">{{ commit.subject }}</div>
       <div class="commit-author">by {{ commit.author }}</div>
   </div>
   '''

Link to GitHub
~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   git_commit_url_template = 'https://github.com/user/repo/commit/{hash}'

CSS Styling
~~~~~~~~~~~

.. code-block:: css

   /* custom.css */
   .git-changelog {
       border-left: 3px solid #4CAF50;
       padding-left: 15px;
       margin: 20px 0;
   }
   
   .commit {
       margin-bottom: 15px;
       padding: 10px;
       background-color: #f5f5f5;
       border-radius: 4px;
   }
   
   .commit-header {
       display: flex;
       justify-content: space-between;
       margin-bottom: 5px;
       font-size: 0.9em;
       color: #666;
   }
   
   .commit-hash {
       font-family: monospace;
       background-color: #e0e0e0;
       padding: 2px 6px;
       border-radius: 3px;
   }
   
   .commit-message {
       font-weight: bold;
       margin: 5px 0;
   }
   
   .commit-author {
       font-size: 0.85em;
       color: #888;
   }

Integration Examples
--------------------

With Releases
~~~~~~~~~~~~~

.. code-block:: rst

   Changelog
   =========
   
   Version 2.1.0 (2024-01-26)
   --------------------------
   
   .. git_changelog::
      :since: v2.0.0
      :until: v2.1.0
   
   Version 2.0.0 (2024-01-15)
   --------------------------
   
   .. git_changelog::
      :since: v1.9.0
      :until: v2.0.0

With Documentation History
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Page History
   ============
   
   This page was last modified in:
   
   .. git_changelog::
      :filename_filter: docs/current_page.rst
      :revisions: 1
      :detailed-message-pre: True

Automation
----------

Generate Changelog
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # generate_changelog.py
   import subprocess
   from datetime import datetime
   
   def generate_changelog(since_tag=None):
       """Generate changelog from Git history."""
       cmd = ['git', 'log', '--oneline']
       if since_tag:
           cmd.extend([f'{since_tag}..HEAD'])
       
       output = subprocess.check_output(cmd).decode()
       
       with open('docs/changelog.rst', 'w') as f:
           f.write('Changelog\n')
           f.write('=========\n\n')
           f.write(f'Generated on {datetime.now()}\n\n')
           f.write('.. git_changelog::\n')
           if since_tag:
               f.write(f'   :since: {since_tag}\n')

Pre-commit Hook
~~~~~~~~~~~~~~~

.. code-block:: bash

   #!/bin/bash
   # .git/hooks/pre-commit
   
   # Update changelog before commit
   python generate_changelog.py
   git add docs/changelog.rst

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Update Changelog
   
   on:
     push:
       branches: [main]
       tags: ['v*']
   
   jobs:
     changelog:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v2
           with:
             fetch-depth: 0  # Full history
         
         - name: Generate changelog
           run: |
             pip install sphinx sphinxcontrib-git
             sphinx-build -b html docs docs/_build/html

Best Practices
--------------

Commit Messages
~~~~~~~~~~~~~~~

Write meaningful commit messages:

.. code-block:: text

   feat: Add new feature
   
   Detailed description of the feature and
   its implementation.
   
   Closes #123

Use conventional commit format for better changelogs.

Organization
~~~~~~~~~~~~

1. Group by version/tag
2. Separate features, fixes, and breaking changes
3. Link commits to issues
4. Include contributor names

Performance
~~~~~~~~~~~

1. Limit commit count with ``:revisions:``
2. Use date ranges for large repos
3. Cache generated changelogs
4. Exclude build artifacts

Troubleshooting
---------------

Missing Commits
~~~~~~~~~~~~~~~

.. code-block:: bash

   # Ensure full git history
   git fetch --unshallow

Formatting Issues
~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Escape special characters
   git_changelog_escape_html = True

No Git Repository
~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Check for git before using directives
   import os
   
   if not os.path.exists('.git'):
       extensions = [ext for ext in extensions if ext != 'sphinxcontrib.git']

See Also
--------

- :doc:`../tutorials/packages/sphinx-git` - Complete tutorial
- :doc:`sphinx-last-updated-by-git-example` - Related extension
- GitHub repository: https://github.com/OddBloke/sphinx-git
