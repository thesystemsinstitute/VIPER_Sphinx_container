Sphinx-Git Tutorial
===================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-git/>`_
   - `API Documentation <../../pdoc/sphinx_git/index.html>`_
   - `Manual <https://github.com/OddBloke/sphinx-git>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinx-git to integrate Git repository information into your Sphinx documentation.

What is Sphinx-Git?
-------------------
sphinx-git is a Sphinx extension that provides:

- Git changelog generation
- Commit history display
- Contributor lists
- Recent changes tracking
- Git log integration
- Author information
- Commit linking
- Version tracking
- Repository statistics
- Customizable formatting

This allows automatic generation of changelogs and documentation of changes directly from Git history.

The sphinx-git extension provides directives for displaying Git changelog, commit history, and repository information directly in your documentation.


Installation
------------

sphinx-git is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm viper-sphinx:latest python -c "import sphinxcontrib.git; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinxcontrib.git',
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinxcontrib.git']
   
   # Changelog configuration
   git_changelog_max_count = 50
   git_changelog_revisions = 'HEAD'
   
   # Commit details
   git_commit_show_author = True
   git_commit_show_date = True
   git_commit_show_hash = True
   
   # Formatting
   git_changelog_format = '{date} - {hash} - {message} ({author})'

Basic Usage
-----------

Git Changelog Directive
~~~~~~~~~~~~~~~~~~~~~~~~

Display Git commit history:

.. code-block:: rst

   .. git_changelog::

This shows recent commits in a formatted list.

Filtered Changelog
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. git_changelog::
      :revisions: v1.0..HEAD
      :max-count: 20

Show commits between v1.0 and HEAD, limited to 20 entries.

Specific File History
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. git_changelog::
      :filename: docs/index.rst

Show commits that modified a specific file.

   Recent Changes
   --------------
   
   .. git_changelog::
      :revisions: HEAD
      :max-count: 50
   
   All Changes
   -----------
   
   For the complete history, see our `Git repository <https://github.com/user/repo>`_.

Example 2: Version-Specific Changelog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/releases/v2.0.rst``:

.. code-block:: rst

   Version 2.0 Release Notes
   =========================
   
   Released: January 2024
   
   Changes in 2.0
   --------------
   
   .. git_changelog::
      :revisions: v1.9..v2.0
      :max-count: 100
   
   Major Features
   ~~~~~~~~~~~~~~
   
   - New API design
   - Performance improvements
   - Python 3.12 support
   
   Bug Fixes
   ~~~~~~~~~
   
   See the commit log above for detailed bug fixes.

Example 3: Contributor List
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/contributors.rst``:

.. code-block:: rst

   Contributors
   ============
   
   Thank you to everyone who has contributed to this project!
   
   Recent Contributors
   -------------------
   
   .. git_changelog::
      :revisions: HEAD
      :max-count: 100
      :format: {author}
   
   This list is automatically generated from Git commit history.

Example 4: File-Specific History
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/api/history.rst``:

.. code-block:: rst

   API Changes History
   ===================
   
   This page tracks changes to our API documentation.
   
   Recent API Documentation Updates
   ---------------------------------
   
   .. git_changelog::
      :filename: docs/api/reference.rst
      :max-count: 30
   
   Core API Changes
   ----------------
   
   .. git_changelog::
      :filename: src/api/core.py
      :revisions: v2.0..HEAD
      :max-count: 20

Example 5: Formatted Changelog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/conf.py``:

.. code-block:: python

   # Custom format
   git_changelog_format = '**{date}** - {message} (`{hash} <https://github.com/user/repo/commit/{hash}>`_) - *{author}*'

``docs/changes.rst``:

.. code-block:: rst

   Recent Changes
   ==============
   
   .. git_changelog::
      :max-count: 30
   
   This changelog is automatically generated from Git commits.

Result:

.. code-block:: text

   **2024-01-15** - Add new feature (a1b2c3d) - *John Doe*
   **2024-01-14** - Fix bug in parser (e4f5g6h) - *Jane Smith*

Advanced Features
-----------------

Custom Date Formatting
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   import datetime
   
   def format_git_date(date_str):
       """Custom date formatter."""
       dt = datetime.datetime.strptime(date_str, '%Y-%m-%d')
       return dt.strftime('%B %d, %Y')
   
   git_date_formatter = format_git_date

Branch-Specific Logs
~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Development Branch Changes
   --------------------------
   
   .. git_changelog::
      :revisions: origin/develop
      :max-count: 25

Author Filtering
~~~~~~~~~~~~~~~~

.. code-block:: python

   # In custom directive
   def setup(app):
       def filter_by_author(commits, author_email):
           return [c for c in commits if author_email in c['author']]
       
       app.add_config_value('git_author_filter', None, 'html')

Grouped by Date
~~~~~~~~~~~~~~~

.. code-block:: rst

   Changes by Month
   ----------------
   
   January 2024
   ~~~~~~~~~~~~
   
   .. git_changelog::
      :revisions: HEAD
      :since: 2024-01-01
      :until: 2024-01-31
   
   December 2023
   ~~~~~~~~~~~~~
   
   .. git_changelog::
      :revisions: HEAD
      :since: 2023-12-01
      :until: 2023-12-31

Custom Templates
~~~~~~~~~~~~~~~~

``docs/_templates/git_changelog.html``:

.. code-block:: html

   <div class="git-changelog">
     {% for commit in commits %}
     <div class="commit-entry">
       <div class="commit-header">
         <span class="commit-hash">
           <a href="https://github.com/user/repo/commit/{{ commit.hash }}">
             {{ commit.hash[:8] }}
           </a>
         </span>
         <span class="commit-date">{{ commit.date }}</span>
         <span class="commit-author">{{ commit.author }}</span>
       </div>
       <div class="commit-message">{{ commit.message }}</div>
     </div>
     {% endfor %}
   </div>

``docs/_static/git-changelog.css``:

.. code-block:: css

   .git-changelog {
       margin: 20px 0;
   }
   
   .commit-entry {
       padding: 12px;
       margin-bottom: 10px;
       border-left: 3px solid #3498db;
       background-color: #f8f9fa;
   }
   
   .commit-header {
       display: flex;
       gap: 15px;
       margin-bottom: 5px;
       font-size: 13px;
       color: #666;
   }
   
   .commit-hash a {
       font-family: monospace;
       color: #e74c3c;
       text-decoration: none;
   }
   
   .commit-author {
       font-weight: 600;
   }
   
   .commit-message {
       font-size: 14px;
       color: #2c3e50;
   }

Docker Integration
------------------

Build with Git History
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Ensure Git repository is available
   docker run --rm \
     -v $(pwd):/project \
     viper-sphinx:latest \
     sphinx-build -b html /project/docs /project/docs/_build/html

Dockerfile with Git
~~~~~~~~~~~~~~~~~~~

.. code-block:: dockerfile

   FROM viper-sphinx:latest
   
   # Ensure git is installed
   RUN apk add --no-cache git
   
   WORKDIR /project
   
   # Mount point expects .git directory
   VOLUME /project
   
   CMD ["sphinx-build", "-b", "html", "docs", "docs/_build/html"]

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Build Docs with Git Changelog
   
   on: [push, pull_request]
   
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
           with:
             fetch-depth: 0  # Full history
         
         - name: Build Documentation
           run: |
             docker run --rm -v $(pwd):/project \
               viper-sphinx:latest \
               sphinx-build -b html /project/docs /project/docs/_build/html
         
         - name: Verify Changelog
           run: |
             if ! grep -q "git-changelog" docs/_build/html/changelog.html; then
               echo "Changelog not generated!"
               exit 1
             fi
         
         - name: Deploy
           if: github.ref == 'refs/heads/main'
           uses: peaceiris/actions-gh-pages@v3
           with:
             github_token: ${{ secrets.GITHUB_TOKEN }}
             publish_dir: ./docs/_build/html

Automated Release Notes
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Generate Release Notes
   
   on:
     push:
       tags:
         - 'v*'
   
   jobs:
     release:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
           with:
             fetch-depth: 0
         
         - name: Generate Changelog
           run: |
             # Build docs with changelog
             docker run --rm -v $(pwd):/project \
               viper-sphinx:latest \
               sphinx-build -b html /project/docs /project/docs/_build/html
         
         - name: Extract Release Notes
           id: notes
           run: |
             # Extract changelog for this version
             NOTES=$(grep -A 50 "${{ github.ref_name }}" docs/_build/html/changelog.html)
             echo "notes<<EOF" >> $GITHUB_OUTPUT
             echo "$NOTES" >> $GITHUB_OUTPUT
             echo "EOF" >> $GITHUB_OUTPUT
         
         - name: Create Release
           uses: actions/create-release@v1
           env:
             GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
           with:
             tag_name: ${{ github.ref }}
             release_name: Release ${{ github.ref_name }}
             body: ${{ steps.notes.outputs.notes }}

Best Practices
--------------

1. **Full History**
   
   Use ``fetch-depth: 0`` in CI for complete logs

2. **Meaningful Commits**
   
   Write clear commit messages

3. **Limit Display**
   
   Use max-count to avoid overwhelming users

4. **Group Logically**
   
   Organize by version or date

5. **Link Commits**
   
   Include repository links

6. **Filter Appropriately**
   
   Show relevant changes only

Troubleshooting
---------------

No Changelog Generated
~~~~~~~~~~~~~~~~~~~~~~

**Solution:**

Check Git repository exists:

.. code-block:: bash

   git log --oneline

Verify extension loaded:

.. code-block:: python

   extensions = ['sphinxcontrib.git']

Empty Changelog
~~~~~~~~~~~~~~~

**Solution:**

Check revision range:

.. code-block:: rst

   .. git_changelog::
      :revisions: HEAD
      :max-count: 50

Ensure commits exist in range.

Formatting Issues
~~~~~~~~~~~~~~~~~

**Solution:**

Check format string:

.. code-block:: python

   git_changelog_format = '{date} - {message} ({author})'

Docker Git Access
~~~~~~~~~~~~~~~~~

**Solution:**

Mount .git directory:

.. code-block:: bash

   docker run --rm -v $(pwd):/project ...

Shallow Clone
~~~~~~~~~~~~~

**Solution:**

Get full history:

.. code-block:: bash

   git fetch --unshallow

Next Steps
----------

1. Add extension to conf.py
2. Create changelog page
3. Configure formatting
4. Test with git history
5. Deploy with CI/CD


Practical Examples
------------------

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


Practical Examples
------------------

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


Practical Examples
------------------

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

Additional Resources
--------------------
- :doc:`sphinx-last-updated-by-git` - Git-based timestamps
- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `sphinx-git Documentation <https://github.com/OddBloke/sphinx-git>`_
- `Git Documentation <https://git-scm.com/doc>`_
- :doc:`../tutorials/packages/sphinx-git` - Complete tutorial
- :doc:`sphinx-last-updated-by-git-example` - Related extension
- GitHub repository: https://github.com/OddBloke/sphinx-git

