Sphinx-Changelog Tutorial
=========================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-changelog/>`_
   - :doc:`See Working Example <../../examples/sphinx-changelog-example>`


This tutorial demonstrates how to use sphinx-changelog to automatically generate and manage changelog documentation.

What is Sphinx-Changelog?
--------------------------

sphinx-changelog is a Sphinx extension that provides:

- Automatic changelog generation
- Version management
- Release notes creation
- Git integration
- Keep a Changelog format
- Semantic versioning support
- Custom categories
- Changelog templates
- Multi-format output
- Issue tracking integration

This automates changelog creation and keeps it synchronized with your project releases.

Installation
------------

sphinx-changelog is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinx_changelog; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``docs/conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_changelog',
   ]
   
   # Changelog configuration
   changelog_file = '../CHANGELOG.md'

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinx_changelog']
   
   # Changelog source
   changelog_file = '../CHANGELOG.md'
   changelog_format = 'keepachangelog'  # or 'towncrier', 'git'
   
   # Display options
   changelog_sections = [
       'Added',
       'Changed',
       'Deprecated',
       'Removed',
       'Fixed',
       'Security',
   ]
   
   # Git integration
   changelog_from_git = True
   changelog_git_range = 'HEAD~10..HEAD'
   
   # Version detection
   changelog_version_file = '../VERSION'
   
   # Issue tracking
   changelog_issue_pattern = r'#(\d+)'
   changelog_issue_url = 'https://github.com/user/repo/issues/{}'

Basic Usage
-----------

Include Changelog
~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. changelog::

This includes the entire changelog.

Specific Version
~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. changelog:: 2.0.0

Latest Changes
~~~~~~~~~~~~~~

.. code-block:: rst

   .. changelog::
      :latest: true

Practical Examples
------------------

Example 1: Keep a Changelog Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``CHANGELOG.md``:

.. code-block:: markdown

   # Changelog
   
   All notable changes to this project will be documented in this file.
   
   The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
   and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
   
   ## [Unreleased]
   
   ### Added
   - New feature for data export
   - Support for multiple file formats
   
   ### Fixed
   - Bug in date parsing
   - Memory leak in data processor
   
   ## [2.0.0] - 2024-01-15
   
   ### Added
   - Complete API redesign
   - New authentication system
   - Support for async operations
   
   ### Changed
   - Updated all dependencies
   - Improved error messages
   
   ### Deprecated
   - Old API endpoints (will be removed in 3.0.0)
   
   ### Removed
   - Python 2.7 support
   
   ### Fixed
   - Critical security vulnerability
   - Performance issues with large datasets
   
   ### Security
   - Updated crypto library to patch CVE-2023-12345
   
   ## [1.5.0] - 2023-12-01
   
   ### Added
   - Export to CSV feature
   - Batch processing support
   
   ### Fixed
   - Timezone handling bug
   - Validation error messages

``docs/changelog.rst``:

.. code-block:: rst

   Changelog
   =========
   
   This page shows the complete history of changes to this project.
   
   .. changelog::
   
   Version History
   ---------------
   
   For the full changelog, see our `GitHub repository <https://github.com/user/repo/blob/main/CHANGELOG.md>`_.

Example 2: Version-Specific Changes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/releases/v2.0.rst``:

.. code-block:: rst

   Version 2.0 Release Notes
   =========================
   
   Released: January 15, 2024
   
   .. changelog:: 2.0.0
   
   Migration Guide
   ---------------
   
   Breaking Changes
   ~~~~~~~~~~~~~~~~
   
   The old API has been completely redesigned. Here's how to migrate:
   
   **Old API:**
   
   .. code-block:: python
      
      from mylib import Client
      client = Client(api_key='key')
      data = client.fetch('/endpoint')
   
   **New API:**
   
   .. code-block:: python
      
      from mylib import AsyncClient
      async with AsyncClient(api_key='key') as client:
          data = await client.get('/endpoint')
   
   New Features
   ~~~~~~~~~~~~
   
   See the changelog above for all new features in this release.

Example 3: Git-Based Changelog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/conf.py``:

.. code-block:: python

   changelog_from_git = True
   changelog_git_range = 'v1.0.0..HEAD'
   
   # Format git commits
   changelog_git_format = '{hash} - {message} ({author}, {date})'
   
   # Issue linking
   changelog_issue_pattern = r'#(\d+)'
   changelog_issue_url = 'https://github.com/user/repo/issues/{}'

``docs/git-changelog.rst``:

.. code-block:: rst

   Recent Changes
   ==============
   
   Changes since last release:
   
   .. changelog::
      :from-git: true
      :range: v1.5.0..HEAD

Example 4: Categorized Changelog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/changelog-detailed.rst``:

.. code-block:: rst

   Detailed Changelog
   ==================
   
   New Features
   ------------
   
   .. changelog::
      :section: Added
   
   Bug Fixes
   ---------
   
   .. changelog::
      :section: Fixed
   
   Breaking Changes
   ----------------
   
   .. changelog::
      :section: Removed
      :section: Changed

Example 5: Multi-Version Comparison
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/versions.rst``:

.. code-block:: rst

   Version Comparison
   ==================
   
   Version 2.0
   -----------
   
   .. changelog:: 2.0.0
   
   Version 1.5
   -----------
   
   .. changelog:: 1.5.0
   
   Version 1.0
   -----------
   
   .. changelog:: 1.0.0
   
   All Versions
   ------------
   
   .. changelog::
      :all: true

Advanced Features
-----------------

Custom Templates
~~~~~~~~~~~~~~~~

``docs/_templates/changelog.rst``:

.. code-block:: rst

   {% for version in versions %}
   {{ version.number }}
   {{ "=" * version.number|length }}
   
   Released: {{ version.date }}
   
   {% for section in version.sections %}
   {{ section.name }}
   {{ "-" * section.name|length }}
   
   {% for change in section.changes %}
   - {{ change.description }}
     {% if change.issue %}(:issue:`{{ change.issue }}`){% endif %}
   {% endfor %}
   
   {% endfor %}
   {% endfor %}

Towncrier Integration
~~~~~~~~~~~~~~~~~~~~~~

``pyproject.toml``:

.. code-block:: toml

   [tool.towncrier]
   package = "mypackage"
   directory = "changelog.d"
   filename = "CHANGELOG.rst"
   
   [[tool.towncrier.type]]
   directory = "feature"
   name = "Features"
   showcontent = true
   
   [[tool.towncrier.type]]
   directory = "bugfix"
   name = "Bug Fixes"
   showcontent = true

``docs/conf.py``:

.. code-block:: python

   changelog_format = 'towncrier'
   changelog_towncrier_path = '../'

Issue Tracking Integration
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # GitHub Issues
   changelog_issue_pattern = r'#(\d+)'
   changelog_issue_url = 'https://github.com/user/repo/issues/{}'
   
   # Jira
   changelog_issue_pattern = r'([A-Z]+-\d+)'
   changelog_issue_url = 'https://jira.example.com/browse/{}'
   
   # GitLab
   changelog_issue_pattern = r'!(\d+)'
   changelog_issue_url = 'https://gitlab.com/user/repo/-/merge_requests/{}'

Automatic Version Detection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import re
   
   def get_version():
       """Read version from setup.py or __init__.py."""
       with open('../mypackage/__init__.py') as f:
           content = f.read()
           match = re.search(r"__version__ = ['\"]([^'\"]+)['\"]", content)
           return match.group(1) if match else '0.0.0'
   
   version = get_version()
   release = version
   
   changelog_current_version = version

Docker Integration
------------------

Build with Changelog
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     kensai-sphinx:latest \
     sphinx-build -b html /project/docs /project/docs/_build/html

Generate Changelog from Git
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Generate changelog, then build
   docker run --rm \
     -v $(pwd):/project \
     kensai-sphinx:latest \
     sh -c "git log --oneline > CHANGELOG.txt && \
            sphinx-build -b html /project/docs /project/docs/_build/html"

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Build Changelog
   
   on:
     push:
       tags:
         - 'v*'
   
   jobs:
     changelog:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
           with:
             fetch-depth: 0  # Full history
         
         - name: Generate Changelog
           run: |
             # Create changelog from git
             git log --oneline --no-merges > CHANGELOG.txt
         
         - name: Build Documentation
           run: |
             docker run --rm -v $(pwd):/project \
               kensai-sphinx:latest \
               sphinx-build -b html /project/docs /project/docs/_build/html
         
         - name: Extract Release Notes
           id: notes
           run: |
             # Get changes for this version
             VERSION=${GITHUB_REF#refs/tags/v}
             NOTES=$(sed -n "/## \[$VERSION\]/,/## \[/p" CHANGELOG.md | head -n -1)
             echo "notes<<EOF" >> $GITHUB_OUTPUT
             echo "$NOTES" >> $GITHUB_OUTPUT
             echo "EOF" >> $GITHUB_OUTPUT
         
         - name: Create Release
           uses: actions/create-release@v1
           env:
             GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
           with:
             tag_name: ${{ github.ref }}
             release_name: Release ${{ github.ref }}
             body: ${{ steps.notes.outputs.notes }}
         
         - name: Deploy Docs
           uses: peaceiris/actions-gh-pages@v3
           with:
             github_token: ${{ secrets.GITHUB_TOKEN }}
             publish_dir: ./docs/_build/html

Automated Changelog Update
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Update Changelog
   
   on:
     pull_request:
       types: [closed]
   
   jobs:
     update:
       if: github.event.pull_request.merged == true
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Update Changelog
           run: |
             # Add PR to unreleased section
             echo "- ${{ github.event.pull_request.title }} (#${{ github.event.pull_request.number }})" >> CHANGELOG.md
         
         - name: Commit Changes
           run: |
             git config user.name github-actions
             git config user.email github-actions@github.com
             git add CHANGELOG.md
             git commit -m "Update changelog for #${{ github.event.pull_request.number }}"
             git push

Best Practices
--------------

1. **Keep Organized**
   
   Use standard categories

2. **Be Descriptive**
   
   Clear change descriptions

3. **Link Issues**
   
   Reference issue numbers

4. **Follow Semver**
   
   Version appropriately

5. **Update Regularly**
   
   Don't let changes pile up

6. **Review Before Release**
   
   Verify completeness

Troubleshooting
---------------

Changelog Not Found
~~~~~~~~~~~~~~~~~~~

**Solution:**

Check file path:

.. code-block:: python

   changelog_file = '../CHANGELOG.md'

Verify file exists.

Parsing Errors
~~~~~~~~~~~~~~

**Solution:**

Verify format:

.. code-block:: python

   changelog_format = 'keepachangelog'

Check markdown syntax.

Git Integration Issues
~~~~~~~~~~~~~~~~~~~~~~

**Solution:**

Ensure git repository:

.. code-block:: bash

   git log --oneline

Check git range:

.. code-block:: python

   changelog_git_range = 'v1.0.0..HEAD'

Version Not Detected
~~~~~~~~~~~~~~~~~~~~

**Solution:**

Specify version explicitly:

.. code-block:: python

   changelog_current_version = '2.0.0'

Next Steps
----------

1. Create CHANGELOG file
2. Configure extension
3. Add to documentation
4. Automate updates
5. Deploy with releases

Additional Resources
--------------------

- :doc:`sphinx-git` - Git integration
- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `Keep a Changelog <https://keepachangelog.com/>`_
- `Semantic Versioning <https://semver.org/>`_
- `Towncrier <https://towncrier.readthedocs.io/>`_
