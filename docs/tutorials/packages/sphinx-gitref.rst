Sphinx-Gitref Tutorial
======================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-gitref/>`_
   - :doc:`See Working Example <../../examples/sphinx-gitref-example>`


This tutorial demonstrates how to use sphinx-gitref to integrate Git repository information into your Sphinx documentation, including commit history, branches, and contributors.

What is Sphinx-Gitref?
-----------------------

sphinx-gitref is a Sphinx extension that provides Git repository integration:

- Display commit history in documentation
- Show Git blame information
- Track file changes and modifications
- Display branch and tag information
- List contributors and statistics
- Link to Git repository (GitHub, GitLab, Bitbucket)
- Show last commit date for documents
- Track documentation changes with Git history

This is invaluable for keeping documentation synchronized with code changes.

Installation
------------

sphinx-gitref is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinx_gitref; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_gitref',
   ]
   
   # Git repository URL
   gitref_repository_url = 'https://github.com/user/repo'

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinx_gitref']
   
   # Repository configuration
   gitref_repository_url = 'https://github.com/user/repo'
   gitref_branch = 'main'
   gitref_repository_path = '..'  # Path to repo root
   
   # Display options
   gitref_show_commit_date = True
   gitref_show_commit_hash = True
   gitref_show_commit_author = True
   gitref_show_file_history = True
   
   # Link configuration
   gitref_link_to_commit = True
   gitref_link_to_file = True
   gitref_link_to_blame = True
   
   # Commit history
   gitref_max_commits = 50
   gitref_commit_format = 'short'  # or 'long', 'oneline'
   
   # Contributors
   gitref_show_contributors = True
   gitref_min_commits = 1  # Minimum commits to be listed
   
   # Change tracking
   gitref_track_changes = True
   gitref_show_diff_stats = True

Basic Usage
-----------

Show Last Commit
~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. gitref:lastcommit::
      
      This file was last modified on {{ date }} by {{ author }}.

Display Commit History
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. gitref:history::
      :max-commits: 10
      :file: path/to/file.py
      
      Recent changes to this file.

Show Contributors
~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. gitref:contributors::
      :min-commits: 5
      
      List of contributors with 5+ commits.

Link to Repository
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   :gitref:commit:`abc123def` - Link to specific commit
   
   :gitref:file:`src/module.py` - Link to file in repo
   
   :gitref:blame:`src/module.py#L10-L20` - Link to blame view

File Changes
~~~~~~~~~~~~

.. code-block:: rst

   .. gitref:changes::
      :file: docs/api.rst
      :since: v1.0.0
      
      Changes to this file since version 1.0.0.

Practical Examples
------------------

Example 1: Documentation Change Log
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create ``docs/changelog.rst``:

.. code-block:: rst

   Documentation Change Log
   =========================
   
   This page tracks changes to the documentation.
   
   Recent Updates
   --------------
   
   .. gitref:history::
      :max-commits: 20
      :path: docs/
      :format: detailed
   
   Last Modified: .. gitref:lastcommit::
   
   Contributors
   ------------
   
   .. gitref:contributors::
      :path: docs/
      :show-stats: true
   
   Top Contributors:
   
   .. gitref:contributor-list::
      :sort: commits
      :limit: 10

Example 2: Code Documentation with Git Info
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/api/module.rst``:

.. code-block:: rst

   Module API Reference
   ====================
   
   .. automodule:: mymodule
      :members:
   
   Source Code
   -----------
   
   View source: :gitref:file:`src/mymodule.py`
   
   Recent Changes
   --------------
   
   .. gitref:history::
      :file: src/mymodule.py
      :max-commits: 5
      :show-diff: true
   
   Blame Information
   -----------------
   
   See who wrote each line: :gitref:blame:`src/mymodule.py`
   
   File Statistics
   ---------------
   
   .. gitref:stats::
      :file: src/mymodule.py
   
   - Total commits: {{ commit_count }}
   - Last modified: {{ last_modified }}
   - Primary author: {{ main_author }}

Example 3: Version History
~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/versions.rst``:

.. code-block:: rst

   Version History
   ===============
   
   Version 2.0.0
   -------------
   
   Released: 2026-01-15
   
   Commits in this release:
   
   .. gitref:history::
      :since: v1.0.0
      :until: v2.0.0
      :group-by: author
   
   Changes by file:
   
   .. gitref:diff-summary::
      :since: v1.0.0
      :until: v2.0.0
      :show-stats: true
   
   Version 1.0.0
   -------------
   
   Released: 2025-12-01
   
   Initial release.

Example 4: Contributor Attribution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/contributors.rst``:

.. code-block:: rst

   Contributors
   ============
   
   We thank all our contributors!
   
   All Contributors
   ----------------
   
   .. gitref:contributors::
      :show-avatar: true
      :show-stats: true
      :sort: commits
   
   Top 10 Contributors
   -------------------
   
   .. gitref:contributor-table::
      :limit: 10
      :columns: name, commits, additions, deletions
   
   First-Time Contributors
   -----------------------
   
   .. gitref:first-time-contributors::
      :since: v2.0.0
   
   Contact
   -------
   
   Want to contribute? See our `Contributing Guide <contributing.html>`_.

Advanced Features
-----------------

Commit Messages in Docs
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. gitref:commit-message::
      :commit: abc123def
      
      Shows the full commit message for the specified commit.

Branch Information
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. gitref:branches::
      :show-active: true
      :show-merged: false
   
   Current branch: .. gitref:current-branch::

Tag Information
~~~~~~~~~~~~~~~

.. code-block:: rst

   .. gitref:tags::
      :pattern: v*
      :sort: date
      :limit: 10
   
   Latest tag: .. gitref:latest-tag::

Diff Statistics
~~~~~~~~~~~~~~~

.. code-block:: rst

   .. gitref:diff-stats::
      :since: v1.0.0
      :until: HEAD
      :group-by: file
   
   Total changes:
   
   - Files changed: {{ files_changed }}
   - Insertions: +{{ insertions }}
   - Deletions: -{{ deletions }}

File Timeline
~~~~~~~~~~~~~

.. code-block:: rst

   .. gitref:timeline::
      :file: src/core.py
      :show-authors: true
      :show-commits: true

Git Blame Integration
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Code written by:
   
   .. gitref:blame-stats::
      :file: src/module.py
      :group-by: author
   
   - :gitref:author:`user1`: 60%
   - :gitref:author:`user2`: 30%
   - :gitref:author:`user3`: 10%

Docker Integration
------------------

Build with Git Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     -v $(pwd)/.git:/project/.git:ro \
     kensai-sphinx:latest \
     sphinx-build -b html /project/docs /project/docs/_build/html

**Note:** Mount `.git` directory to access Git history.

Generate Git Reports
~~~~~~~~~~~~~~~~~~~~

Create ``git_report.sh``:

.. code-block:: bash

   #!/bin/bash
   
   docker run --rm \
     -v $(pwd):/project \
     -v $(pwd)/.git:/project/.git:ro \
     kensai-sphinx:latest \
     sh -c "
       cd /project
       
       echo 'Git Statistics for Documentation'
       echo '================================'
       echo ''
       
       echo 'Total Commits:'
       git log --oneline docs/ | wc -l
       
       echo ''
       echo 'Contributors:'
       git log --format='%aN' docs/ | sort -u
       
       echo ''
       echo 'Recent Changes:'
       git log --oneline -10 docs/
     "

Docker Compose
~~~~~~~~~~~~~~

``docker-compose.yml``:

.. code-block:: yaml

   version: '3.8'
   
   services:
     docs:
       image: kensai-sphinx:latest
       volumes:
         - ./:/project
         - ./.git:/project/.git:ro
       command: sphinx-build -b html /project/docs /project/docs/_build/html
       environment:
         - GIT_BRANCH=main
         - GIT_REPO_URL=https://github.com/user/repo

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Build Docs with Git Info
   
   on:
     push:
       branches: [main]
   
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
           with:
             fetch-depth: 0  # Full history
         
         - name: Build Documentation
           run: |
             docker run --rm \
               -v $(pwd):/project \
               -e GIT_COMMIT_SHA=${{ github.sha }} \
               -e GIT_BRANCH=${{ github.ref_name }} \
               -e GIT_REPO=${{ github.repository }} \
               kensai-sphinx:latest \
               sphinx-build -b html /project/docs /project/docs/_build/html

GitLab CI
~~~~~~~~~

.. code-block:: yaml

   build-docs:
     image: kensai-sphinx:latest
     script:
       - git fetch --unshallow  # Get full history
       - sphinx-build -b html docs/ public
     variables:
       GIT_DEPTH: 0
     artifacts:
       paths:
         - public

Best Practices
--------------

1. **Fetch Full History**
   
   For accurate Git information:
   
   .. code-block:: bash
   
      git fetch --unshallow

2. **Mount Git Directory**
   
   When using Docker:
   
   .. code-block:: bash
   
      -v $(pwd)/.git:/project/.git:ro

3. **Use Relative Paths**
   
   Configure repository path relative to conf.py:
   
   .. code-block:: python
   
      gitref_repository_path = '..'

4. **Limit History**
   
   Don't show entire history in docs:
   
   .. code-block:: rst
   
      .. gitref:history::
         :max-commits: 20

5. **Cache Git Data**
   
   For faster builds, cache Git information

6. **Attribute Contributors**
   
   Always credit contributors properly

Common Patterns
---------------

Footer with Git Info
~~~~~~~~~~~~~~~~~~~~

Create ``_templates/footer.html``:

.. code-block:: html

   {% extends "!footer.html" %}
   {% block extrafooter %}
   <div class="git-info">
       Last updated: {{ gitref_last_modified }}
       |
       <a href="{{ gitref_commit_url }}">Commit {{ gitref_commit_hash[:7] }}</a>
       |
       <a href="{{ gitref_file_url }}">View source</a>
   </div>
   {% endblock %}

Change Notification
~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. note::
      
      This documentation was updated on .. gitref:lastcommit::.
      See the full history: :gitref:history:`this file`.

Version Badge
~~~~~~~~~~~~~

.. code-block:: rst

   .. gitref:badge::
      :type: version
      :show-commit: true
   
   Documentation for version {{ version }} ({{ commit }})

Troubleshooting
---------------

Git Not Found
~~~~~~~~~~~~~

**Solution:**

Ensure Git repository is accessible:

.. code-block:: bash

   # Check .git directory exists
   ls -la .git
   
   # Mount in Docker
   docker run -v $(pwd)/.git:/project/.git:ro ...

Shallow Clone Issues
~~~~~~~~~~~~~~~~~~~~

**Solution:**

Fetch full history:

.. code-block:: bash

   git fetch --unshallow

Commit Links Broken
~~~~~~~~~~~~~~~~~~~

**Solution:**

Verify repository URL:

.. code-block:: python

   gitref_repository_url = 'https://github.com/user/repo'
   gitref_branch = 'main'

No Git History in CI
~~~~~~~~~~~~~~~~~~~~

**Solution:**

Configure CI to fetch full history:

.. code-block:: yaml

   # GitHub Actions
   - uses: actions/checkout@v3
     with:
       fetch-depth: 0
   
   # GitLab CI
   variables:
     GIT_DEPTH: 0

Next Steps
----------

1. Configure Git repository URL
2. Add Git information to documentation pages
3. Create changelog with commit history
4. Display contributor information
5. Integrate into CI/CD pipeline

Additional Resources
--------------------

- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- :doc:`sphinx-last-updated-by-git` - Alternative Git integration
- :doc:`sphinx-git` - Another Git extension
- `Git Documentation <https://git-scm.com/doc>`_
