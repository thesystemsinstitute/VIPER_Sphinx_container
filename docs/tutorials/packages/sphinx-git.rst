Sphinx-Git Tutorial
===================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-git/>`_
   - `API Documentation <../../pdoc/sphinx_git/index.html>`_
   - `Manual <https://github.com/OddBloke/sphinx-git>`_
   - :doc:`Working Example <../../examples/sphinx-git-example>`


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

   docker run --rm kensai-sphinx:latest python -c "import sphinxcontrib.git; print('Installed')"

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
     kensai-sphinx:latest \
     sphinx-build -b html /project/docs /project/docs/_build/html

Dockerfile with Git
~~~~~~~~~~~~~~~~~~~

.. code-block:: dockerfile

   FROM kensai-sphinx:latest
   
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
               kensai-sphinx:latest \
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
               kensai-sphinx:latest \
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

Additional Resources
--------------------

- :doc:`sphinx-last-updated-by-git` - Git-based timestamps
- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `sphinx-git Documentation <https://github.com/OddBloke/sphinx-git>`_
- `Git Documentation <https://git-scm.com/doc>`_
