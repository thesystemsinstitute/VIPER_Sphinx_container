Sphinx-Changelog Tutorial
=========================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-changelog/>`_
   - `API Documentation <../../pdoc/sphinx_changelog/index.html>`_
   - `Manual <https://github.com/OpenAstronomy/sphinx-changelog>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

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

What is sphinx-changelog?
~~~~~~~~~~~~~~~~~~~~~~~~~~

sphinx-changelog automatically generates changelog documentation from:

- Git commit messages
- GitHub/GitLab release notes
- Keep a Changelog format files
- Version tags and milestones
- Pull requests and issues

Key Features
~~~~~~~~~~~~

- **Automatic Generation**: Create changelogs from Git history
- **Multiple Sources**: Git, GitHub, GitLab, file-based
- **Semantic Versioning**: Organize by version numbers
- **Category Grouping**: Group changes by type (Added, Changed, Fixed, etc.)
- **Template Customization**: Control changelog appearance
- **Filtering**: Include/exclude commits by pattern
- **Cross-References**: Link to issues and pull requests
- **Multi-Format**: Output as RST, Markdown, HTML


Installation
------------

sphinx-changelog is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm viper-sphinx:latest python -c "import sphinx_changelog; print('Installed')"

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


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_changelog',
       # ... other extensions
   ]
   
   # Basic changelog settings
   changelog_source = 'git'  # 'git', 'github', 'gitlab', 'file'
   changelog_file = 'CHANGELOG.rst'

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

Complete configuration with all options:

.. code-block:: python

   # Source Configuration
   changelog_source = 'git'  # 'git', 'github', 'gitlab', 'file'
   changelog_file = 'CHANGELOG.rst'
   changelog_repo_path = '.'
   
   # Version Management
   changelog_version_pattern = r'^v?(\d+\.\d+\.\d+)$'
   changelog_include_unreleased = True
   changelog_unreleased_title = 'Unreleased'
   
   # Grouping and Categories
   changelog_categories = [
       'Added',
       'Changed',
       'Deprecated',
       'Removed',
       'Fixed',
       'Security',
   ]
   changelog_group_by = 'category'  # 'category', 'version', 'date'
   
   # Commit Filtering
   changelog_include_patterns = [r'.*']
   changelog_exclude_patterns = [
       r'^Merge',
       r'^WIP',
       r'^\[skip\]',
   ]
   changelog_commit_format = 'conventional'  # 'conventional', 'custom'
   
   # GitHub/GitLab Integration
   changelog_github_repo = 'owner/repo'
   changelog_github_token = os.getenv('GITHUB_TOKEN')
   changelog_gitlab_url = 'https://gitlab.com'
   changelog_gitlab_project_id = '12345'
   
   # Cross-References
   changelog_issue_pattern = r'#(\d+)'
   changelog_issue_url = 'https://github.com/owner/repo/issues/{issue}'
   changelog_pr_pattern = r'!(\d+)'
   changelog_pr_url = 'https://github.com/owner/repo/pull/{pr}'
   
   # Display Options
   changelog_show_authors = True
   changelog_show_dates = True
   changelog_show_commits = False
   changelog_show_links = True
   
   # Template Options
   changelog_template = 'changelog.rst_t'
   changelog_section_depth = 2

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
     viper-sphinx:latest \
     sphinx-build -b html /project/docs /project/docs/_build/html

Generate Changelog from Git
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Generate changelog, then build
   docker run --rm \
     -v $(pwd):/project \
     viper-sphinx:latest \
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
               viper-sphinx:latest \
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


Practical Examples
------------------

Installation
------------

Using pip
~~~~~~~~~

Install the extension:

.. code-block:: bash

   pip install sphinx-changelog

Or add to your ``requirements.txt``:

.. code-block:: text

   sphinx-changelog>=1.2.0
   gitpython>=3.0.0

Configuration
-------------

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_changelog',
       # ... other extensions
   ]
   
   # Basic changelog settings
   changelog_source = 'git'  # 'git', 'github', 'gitlab', 'file'
   changelog_file = 'CHANGELOG.rst'

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

Complete configuration with all options:

.. code-block:: python

   # Source Configuration
   changelog_source = 'git'  # 'git', 'github', 'gitlab', 'file'
   changelog_file = 'CHANGELOG.rst'
   changelog_repo_path = '.'
   
   # Version Management
   changelog_version_pattern = r'^v?(\d+\.\d+\.\d+)$'
   changelog_include_unreleased = True
   changelog_unreleased_title = 'Unreleased'
   
   # Grouping and Categories
   changelog_categories = [
       'Added',
       'Changed',
       'Deprecated',
       'Removed',
       'Fixed',
       'Security',
   ]
   changelog_group_by = 'category'  # 'category', 'version', 'date'
   
   # Commit Filtering
   changelog_include_patterns = [r'.*']
   changelog_exclude_patterns = [
       r'^Merge',
       r'^WIP',
       r'^\[skip\]',
   ]
   changelog_commit_format = 'conventional'  # 'conventional', 'custom'
   
   # GitHub/GitLab Integration
   changelog_github_repo = 'owner/repo'
   changelog_github_token = os.getenv('GITHUB_TOKEN')
   changelog_gitlab_url = 'https://gitlab.com'
   changelog_gitlab_project_id = '12345'
   
   # Cross-References
   changelog_issue_pattern = r'#(\d+)'
   changelog_issue_url = 'https://github.com/owner/repo/issues/{issue}'
   changelog_pr_pattern = r'!(\d+)'
   changelog_pr_url = 'https://github.com/owner/repo/pull/{pr}'
   
   # Display Options
   changelog_show_authors = True
   changelog_show_dates = True
   changelog_show_commits = False
   changelog_show_links = True
   
   # Template Options
   changelog_template = 'changelog.rst_t'
   changelog_section_depth = 2

Directives
----------

changelog Directive
~~~~~~~~~~~~~~~~~~~

Generate complete changelog:

.. code-block:: rst

   .. changelog::
      :source: git
      :versions: 1.0.0, 1.1.0, 2.0.0
      :group-by: category
      
      Complete project changelog.

changelog-version Directive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Document specific version:

.. code-block:: rst

   .. changelog-version:: 2.0.0
      :date: 2024-01-20
      :show-commits: true
      :show-authors: true
      
      Changes in version 2.0.0.

changelog-category Directive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Show specific category of changes:

.. code-block:: rst

   .. changelog-category:: Fixed
      :version: 2.0.0
      :show-issues: true
      
      Bug fixes in version 2.0.0.

changelog-unreleased Directive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Show unreleased changes:

.. code-block:: rst

   .. changelog-unreleased::
      :group-by: category
      :show-commits: true
      
      Upcoming changes not yet released.

Roles
-----

Changelog References
~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   See :changelog:`version 2.0.0 <2.0.0>` for details.
   
   Fixed in :issue:`123`.
   
   Merged :pr:`456`.
   
   By :author:`johndoe`.

Practical Examples
------------------

Complete Changelog
~~~~~~~~~~~~~~~~~~

**File**: ``changelog.rst``

.. code-block:: rst

   Changelog
   =========
   
   All notable changes to this project are documented here.
   
   The format is based on `Keep a Changelog <https://keepachangelog.com/>`_,
   and this project adheres to `Semantic Versioning <https://semver.org/>`_.
   
   .. changelog::
      :source: git
      :group-by: category
      :show-authors: true
      :show-dates: true
      :include-unreleased: true
      
      Project changelog generated from Git history.

Version-Specific Changelog
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Version 2.0.0
   =============
   
   *Released: 2024-01-20*
   
   .. changelog-version:: 2.0.0
      :group-by: category
      :show-commits: true
      :show-issues: true
      :show-authors: true
   
   Added
   -----
   
   - New feature X
   - Enhanced functionality Y
   
   Changed
   -------
   
   - Modified behavior of Z
   - Updated dependencies
   
   Fixed
   -----
   
   - Resolved :issue:`123`
   - Fixed :issue:`456`

Categorized Changelog
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Recent Changes
   ==============
   
   Bug Fixes
   ---------
   
   .. changelog-category:: Fixed
      :versions: 2.0.0, 1.9.0
      :show-issues: true
      
      Recent bug fixes.
   
   New Features
   ------------
   
   .. changelog-category:: Added
      :versions: 2.0.0
      :show-details: true
      
      Newly added features.
   
   Breaking Changes
   ----------------
   
   .. changelog-category:: Changed
      :versions: 2.0.0
      :breaking-only: true
      
      Breaking changes requiring attention.

Unreleased Changes
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Upcoming Release
   ================
   
   .. changelog-unreleased::
      :group-by: category
      :show-commits: true
      :since: v1.9.0
      
      Changes since last release.
   
   Planned for v2.1.0
   ------------------
   
   **Added**
   
   - Feature A (in progress)
   - Feature B (planned)
   
   **Fixed**
   
   - Bug fixes committed but not released

Sample Changelog File
---------------------

Keep a Changelog Format
~~~~~~~~~~~~~~~~~~~~~~~

**File**: ``CHANGELOG.md``

.. code-block:: markdown

   # Changelog
   
   All notable changes to this project will be documented in this file.
   
   The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
   and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
   
   ## [Unreleased]
   
   ### Added
   - New API endpoint for user management
   - Support for Python 3.11
   
   ### Changed
   - Improved error messages
   - Updated documentation
   
   ### Fixed
   - Memory leak in cache module
   - Race condition in async operations
   
   ## [2.0.0] - 2024-01-20
   
   ### Added
   - Major refactoring of core modules
   - New plugin system
   - CLI enhancements
   
   ### Changed
   - Breaking: Renamed `old_function()` to `new_function()`
   - Updated all dependencies to latest versions
   
   ### Removed
   - Deprecated functions from v1.x
   
   ### Fixed
   - Critical security vulnerability (#123)
   - Data corruption bug (#456)
   
   ## [1.9.0] - 2024-01-15
   
   ### Added
   - Feature X with configuration options
   - Integration with Service Y
   
   ### Fixed
   - Bug in parser (#789)
   - Incorrect validation (#790)

RST Format
~~~~~~~~~~

**File**: ``CHANGELOG.rst``

.. code-block:: rst

   Changelog
   =========
   
   Unreleased
   ----------
   
   Added
   ~~~~~
   
   - New feature for batch processing
   - Additional validation options
   
   Fixed
   ~~~~~
   
   - Resolved timeout issues
   - Fixed parsing edge cases
   
   2.0.0 - 2024-01-20
   ------------------
   
   Added
   ~~~~~
   
   - Plugin architecture
   - Extended API
   - CLI improvements
   
   Changed
   ~~~~~~~
   
   - **Breaking**: Renamed core functions
   - Updated configuration format
   
   Deprecated
   ~~~~~~~~~~
   
   - Old API will be removed in v3.0
   
   Removed
   ~~~~~~~
   
   - Legacy compatibility layer
   
   Fixed
   ~~~~~
   
   - Security issue in authentication
   - Memory management improvements
   
   Security
   ~~~~~~~~
   
   - Fixed CVE-2024-12345

Conventional Commits
--------------------

Commit Message Format
~~~~~~~~~~~~~~~~~~~~~

Use conventional commit format:

.. code-block:: text

   <type>(<scope>): <subject>
   
   <body>
   
   <footer>

Types:

- ``feat``: New feature (Added)
- ``fix``: Bug fix (Fixed)
- ``docs``: Documentation changes
- ``style``: Code style changes
- ``refactor``: Code refactoring (Changed)
- ``perf``: Performance improvements
- ``test``: Test updates
- ``chore``: Build/tool changes

Examples
~~~~~~~~

.. code-block:: text

   feat(api): add user authentication endpoint
   
   Implements JWT-based authentication for API endpoints.
   Includes middleware for token validation.
   
   Closes #123

.. code-block:: text

   fix(parser): resolve edge case in URL parsing
   
   Fixed issue where URLs with special characters were
   incorrectly parsed.
   
   Fixes #456

.. code-block:: text

   docs(readme): update installation instructions
   
   Added troubleshooting section and updated examples.

Configuration for Conventional Commits
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   changelog_commit_format = 'conventional'
   changelog_conventional_types = {
       'feat': 'Added',
       'fix': 'Fixed',
       'docs': 'Documentation',
       'style': 'Style',
       'refactor': 'Changed',
       'perf': 'Performance',
       'test': 'Testing',
       'chore': 'Chores',
   }

Advanced Features
-----------------

GitHub Integration
~~~~~~~~~~~~~~~~~~

Pull release notes from GitHub:

.. code-block:: python

   # conf.py
   changelog_source = 'github'
   changelog_github_repo = 'owner/repo'
   changelog_github_token = os.getenv('GITHUB_TOKEN')
   changelog_include_pulls = True
   changelog_include_issues = True

.. code-block:: rst

   .. changelog::
      :source: github
      :releases: 3
      :show-pull-requests: true
      
      Recent releases from GitHub.

GitLab Integration
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   changelog_source = 'gitlab'
   changelog_gitlab_url = 'https://gitlab.com'
   changelog_gitlab_project_id = '12345'
   changelog_gitlab_token = os.getenv('GITLAB_TOKEN')

Custom Templates
~~~~~~~~~~~~~~~~

**File**: ``_templates/changelog.rst_t``

.. code-block:: jinja

   Changelog
   =========
   
   {% for version in versions %}
   {{ version.name }} - {{ version.date }}
   {{ "-" * (version.name|length + version.date|length + 3) }}
   
   {% for category in categories %}
   {% if version.changes[category] %}
   {{ category }}
   {{ "~" * category|length }}
   
   {% for change in version.changes[category] %}
   - {{ change.description }}
     {% if change.author %}by {{ change.author }}{% endif %}
     {% if change.issues %}({{ change.issues|join(', ') }}){% endif %}
   {% endfor %}
   
   {% endif %}
   {% endfor %}
   
   {% endfor %}

Filtering Changes
~~~~~~~~~~~~~~~~~

Filter commits by pattern:

.. code-block:: python

   # conf.py
   changelog_include_patterns = [
       r'^feat:',
       r'^fix:',
       r'^BREAKING:',
   ]
   
   changelog_exclude_patterns = [
       r'^Merge',
       r'^chore:',
       r'^\[skip changelog\]',
   ]

Best Practices
--------------

Commit Messages
~~~~~~~~~~~~~~~

1. **Clear and Concise**: Write descriptive commit messages
2. **Follow Convention**: Use conventional commit format
3. **Reference Issues**: Link to issue tracker
4. **Breaking Changes**: Mark breaking changes clearly

Version Tagging
~~~~~~~~~~~~~~~

Use semantic versioning for tags:

.. code-block:: bash

   # Create version tags
   git tag -a v2.0.0 -m "Release version 2.0.0"
   git push origin v2.0.0

Changelog Maintenance
~~~~~~~~~~~~~~~~~~~~~

Keep changelog updated:

.. code-block:: rst

   .. changelog::
      :auto-update: true
      :validate: true
      :warn-missing: true

Troubleshooting
---------------

No Changelog Generated
~~~~~~~~~~~~~~~~~~~~~~

**Problem**: Changelog directive produces no output

**Solution**:

.. code-block:: python

   # Check Git repository
   changelog_repo_path = '.'
   
   # Verify version tags exist
   git tag -l
   
   # Check patterns
   changelog_include_patterns = [r'.*']
   changelog_exclude_patterns = []

Missing Versions
~~~~~~~~~~~~~~~~

**Problem**: Some versions not appearing

**Solution**:

.. code-block:: python

   # Check version pattern
   changelog_version_pattern = r'^v?(\d+\.\d+\.\d+)$'
   
   # List all tags
   git tag -l
   
   # Ensure tags match pattern

GitHub Rate Limiting
~~~~~~~~~~~~~~~~~~~~

**Problem**: GitHub API rate limit exceeded

**Solution**:

.. code-block:: python

   # Use authentication token
   changelog_github_token = os.getenv('GITHUB_TOKEN')
   
   # Cache results
   changelog_cache_github = True
   changelog_cache_ttl = 3600

Integration Examples
--------------------

With ReadTheDocs
~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   import os
   
   on_rtd = os.environ.get('READTHEDOCS') == 'True'
   
   if on_rtd:
       # Ensure Git history is available
       os.system('git fetch --unshallow')
   
   changelog_source = 'git'

With CI/CD
~~~~~~~~~~

.. code-block:: yaml

   # .github/workflows/release.yml
   name: Release
   
   on:
     push:
       tags:
         - 'v*'
   
   jobs:
     release:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v2
           with:
             fetch-depth: 0  # Full history for changelog
         
         - name: Generate Changelog
           run: |
             pip install sphinx sphinx-changelog
             sphinx-build -b html docs build/html

With Sphinx-Autobuild
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Watch for changelog updates
   sphinx-autobuild docs build/html \
     --watch CHANGELOG.md \
     --watch .git/refs/tags


Practical Examples
------------------

Installation
------------

Using pip
~~~~~~~~~

Install the extension:

.. code-block:: bash

   pip install sphinx-changelog

Or add to your ``requirements.txt``:

.. code-block:: text

   sphinx-changelog>=1.2.0
   gitpython>=3.0.0

Configuration
-------------

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_changelog',
       # ... other extensions
   ]
   
   # Basic changelog settings
   changelog_source = 'git'  # 'git', 'github', 'gitlab', 'file'
   changelog_file = 'CHANGELOG.rst'

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

Complete configuration with all options:

.. code-block:: python

   # Source Configuration
   changelog_source = 'git'  # 'git', 'github', 'gitlab', 'file'
   changelog_file = 'CHANGELOG.rst'
   changelog_repo_path = '.'
   
   # Version Management
   changelog_version_pattern = r'^v?(\d+\.\d+\.\d+)$'
   changelog_include_unreleased = True
   changelog_unreleased_title = 'Unreleased'
   
   # Grouping and Categories
   changelog_categories = [
       'Added',
       'Changed',
       'Deprecated',
       'Removed',
       'Fixed',
       'Security',
   ]
   changelog_group_by = 'category'  # 'category', 'version', 'date'
   
   # Commit Filtering
   changelog_include_patterns = [r'.*']
   changelog_exclude_patterns = [
       r'^Merge',
       r'^WIP',
       r'^\[skip\]',
   ]
   changelog_commit_format = 'conventional'  # 'conventional', 'custom'
   
   # GitHub/GitLab Integration
   changelog_github_repo = 'owner/repo'
   changelog_github_token = os.getenv('GITHUB_TOKEN')
   changelog_gitlab_url = 'https://gitlab.com'
   changelog_gitlab_project_id = '12345'
   
   # Cross-References
   changelog_issue_pattern = r'#(\d+)'
   changelog_issue_url = 'https://github.com/owner/repo/issues/{issue}'
   changelog_pr_pattern = r'!(\d+)'
   changelog_pr_url = 'https://github.com/owner/repo/pull/{pr}'
   
   # Display Options
   changelog_show_authors = True
   changelog_show_dates = True
   changelog_show_commits = False
   changelog_show_links = True
   
   # Template Options
   changelog_template = 'changelog.rst_t'
   changelog_section_depth = 2

Directives
----------

changelog Directive
~~~~~~~~~~~~~~~~~~~

Generate complete changelog:

.. code-block:: rst

   .. changelog::
      :source: git
      :versions: 1.0.0, 1.1.0, 2.0.0
      :group-by: category
      
      Complete project changelog.

changelog-version Directive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Document specific version:

.. code-block:: rst

   .. changelog-version:: 2.0.0
      :date: 2024-01-20
      :show-commits: true
      :show-authors: true
      
      Changes in version 2.0.0.

changelog-category Directive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Show specific category of changes:

.. code-block:: rst

   .. changelog-category:: Fixed
      :version: 2.0.0
      :show-issues: true
      
      Bug fixes in version 2.0.0.

changelog-unreleased Directive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Show unreleased changes:

.. code-block:: rst

   .. changelog-unreleased::
      :group-by: category
      :show-commits: true
      
      Upcoming changes not yet released.

Roles
-----

Changelog References
~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   See :changelog:`version 2.0.0 <2.0.0>` for details.
   
   Fixed in :issue:`123`.
   
   Merged :pr:`456`.
   
   By :author:`johndoe`.

Practical Examples
------------------

Complete Changelog
~~~~~~~~~~~~~~~~~~

**File**: ``changelog.rst``

.. code-block:: rst

   Changelog
   =========
   
   All notable changes to this project are documented here.
   
   The format is based on `Keep a Changelog <https://keepachangelog.com/>`_,
   and this project adheres to `Semantic Versioning <https://semver.org/>`_.
   
   .. changelog::
      :source: git
      :group-by: category
      :show-authors: true
      :show-dates: true
      :include-unreleased: true
      
      Project changelog generated from Git history.

Version-Specific Changelog
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Version 2.0.0
   =============
   
   *Released: 2024-01-20*
   
   .. changelog-version:: 2.0.0
      :group-by: category
      :show-commits: true
      :show-issues: true
      :show-authors: true
   
   Added
   -----
   
   - New feature X
   - Enhanced functionality Y
   
   Changed
   -------
   
   - Modified behavior of Z
   - Updated dependencies
   
   Fixed
   -----
   
   - Resolved :issue:`123`
   - Fixed :issue:`456`

Categorized Changelog
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Recent Changes
   ==============
   
   Bug Fixes
   ---------
   
   .. changelog-category:: Fixed
      :versions: 2.0.0, 1.9.0
      :show-issues: true
      
      Recent bug fixes.
   
   New Features
   ------------
   
   .. changelog-category:: Added
      :versions: 2.0.0
      :show-details: true
      
      Newly added features.
   
   Breaking Changes
   ----------------
   
   .. changelog-category:: Changed
      :versions: 2.0.0
      :breaking-only: true
      
      Breaking changes requiring attention.

Unreleased Changes
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Upcoming Release
   ================
   
   .. changelog-unreleased::
      :group-by: category
      :show-commits: true
      :since: v1.9.0
      
      Changes since last release.
   
   Planned for v2.1.0
   ------------------
   
   **Added**
   
   - Feature A (in progress)
   - Feature B (planned)
   
   **Fixed**
   
   - Bug fixes committed but not released

Sample Changelog File
---------------------

Keep a Changelog Format
~~~~~~~~~~~~~~~~~~~~~~~

**File**: ``CHANGELOG.md``

.. code-block:: markdown

   # Changelog
   
   All notable changes to this project will be documented in this file.
   
   The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
   and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
   
   ## [Unreleased]
   
   ### Added
   - New API endpoint for user management
   - Support for Python 3.11
   
   ### Changed
   - Improved error messages
   - Updated documentation
   
   ### Fixed
   - Memory leak in cache module
   - Race condition in async operations
   
   ## [2.0.0] - 2024-01-20
   
   ### Added
   - Major refactoring of core modules
   - New plugin system
   - CLI enhancements
   
   ### Changed
   - Breaking: Renamed `old_function()` to `new_function()`
   - Updated all dependencies to latest versions
   
   ### Removed
   - Deprecated functions from v1.x
   
   ### Fixed
   - Critical security vulnerability (#123)
   - Data corruption bug (#456)
   
   ## [1.9.0] - 2024-01-15
   
   ### Added
   - Feature X with configuration options
   - Integration with Service Y
   
   ### Fixed
   - Bug in parser (#789)
   - Incorrect validation (#790)

RST Format
~~~~~~~~~~

**File**: ``CHANGELOG.rst``

.. code-block:: rst

   Changelog
   =========
   
   Unreleased
   ----------
   
   Added
   ~~~~~
   
   - New feature for batch processing
   - Additional validation options
   
   Fixed
   ~~~~~
   
   - Resolved timeout issues
   - Fixed parsing edge cases
   
   2.0.0 - 2024-01-20
   ------------------
   
   Added
   ~~~~~
   
   - Plugin architecture
   - Extended API
   - CLI improvements
   
   Changed
   ~~~~~~~
   
   - **Breaking**: Renamed core functions
   - Updated configuration format
   
   Deprecated
   ~~~~~~~~~~
   
   - Old API will be removed in v3.0
   
   Removed
   ~~~~~~~
   
   - Legacy compatibility layer
   
   Fixed
   ~~~~~
   
   - Security issue in authentication
   - Memory management improvements
   
   Security
   ~~~~~~~~
   
   - Fixed CVE-2024-12345

Conventional Commits
--------------------

Commit Message Format
~~~~~~~~~~~~~~~~~~~~~

Use conventional commit format:

.. code-block:: text

   <type>(<scope>): <subject>
   
   <body>
   
   <footer>

Types:

- ``feat``: New feature (Added)
- ``fix``: Bug fix (Fixed)
- ``docs``: Documentation changes
- ``style``: Code style changes
- ``refactor``: Code refactoring (Changed)
- ``perf``: Performance improvements
- ``test``: Test updates
- ``chore``: Build/tool changes

Examples
~~~~~~~~

.. code-block:: text

   feat(api): add user authentication endpoint
   
   Implements JWT-based authentication for API endpoints.
   Includes middleware for token validation.
   
   Closes #123

.. code-block:: text

   fix(parser): resolve edge case in URL parsing
   
   Fixed issue where URLs with special characters were
   incorrectly parsed.
   
   Fixes #456

.. code-block:: text

   docs(readme): update installation instructions
   
   Added troubleshooting section and updated examples.

Configuration for Conventional Commits
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   changelog_commit_format = 'conventional'
   changelog_conventional_types = {
       'feat': 'Added',
       'fix': 'Fixed',
       'docs': 'Documentation',
       'style': 'Style',
       'refactor': 'Changed',
       'perf': 'Performance',
       'test': 'Testing',
       'chore': 'Chores',
   }

Advanced Features
-----------------

GitHub Integration
~~~~~~~~~~~~~~~~~~

Pull release notes from GitHub:

.. code-block:: python

   # conf.py
   changelog_source = 'github'
   changelog_github_repo = 'owner/repo'
   changelog_github_token = os.getenv('GITHUB_TOKEN')
   changelog_include_pulls = True
   changelog_include_issues = True

.. code-block:: rst

   .. changelog::
      :source: github
      :releases: 3
      :show-pull-requests: true
      
      Recent releases from GitHub.

GitLab Integration
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   changelog_source = 'gitlab'
   changelog_gitlab_url = 'https://gitlab.com'
   changelog_gitlab_project_id = '12345'
   changelog_gitlab_token = os.getenv('GITLAB_TOKEN')

Custom Templates
~~~~~~~~~~~~~~~~

**File**: ``_templates/changelog.rst_t``

.. code-block:: jinja

   Changelog
   =========
   
   {% for version in versions %}
   {{ version.name }} - {{ version.date }}
   {{ "-" * (version.name|length + version.date|length + 3) }}
   
   {% for category in categories %}
   {% if version.changes[category] %}
   {{ category }}
   {{ "~" * category|length }}
   
   {% for change in version.changes[category] %}
   - {{ change.description }}
     {% if change.author %}by {{ change.author }}{% endif %}
     {% if change.issues %}({{ change.issues|join(', ') }}){% endif %}
   {% endfor %}
   
   {% endif %}
   {% endfor %}
   
   {% endfor %}

Filtering Changes
~~~~~~~~~~~~~~~~~

Filter commits by pattern:

.. code-block:: python

   # conf.py
   changelog_include_patterns = [
       r'^feat:',
       r'^fix:',
       r'^BREAKING:',
   ]
   
   changelog_exclude_patterns = [
       r'^Merge',
       r'^chore:',
       r'^\[skip changelog\]',
   ]

Best Practices
--------------

Commit Messages
~~~~~~~~~~~~~~~

1. **Clear and Concise**: Write descriptive commit messages
2. **Follow Convention**: Use conventional commit format
3. **Reference Issues**: Link to issue tracker
4. **Breaking Changes**: Mark breaking changes clearly

Version Tagging
~~~~~~~~~~~~~~~

Use semantic versioning for tags:

.. code-block:: bash

   # Create version tags
   git tag -a v2.0.0 -m "Release version 2.0.0"
   git push origin v2.0.0

Changelog Maintenance
~~~~~~~~~~~~~~~~~~~~~

Keep changelog updated:

.. code-block:: rst

   .. changelog::
      :auto-update: true
      :validate: true
      :warn-missing: true

Troubleshooting
---------------

No Changelog Generated
~~~~~~~~~~~~~~~~~~~~~~

**Problem**: Changelog directive produces no output

**Solution**:

.. code-block:: python

   # Check Git repository
   changelog_repo_path = '.'
   
   # Verify version tags exist
   git tag -l
   
   # Check patterns
   changelog_include_patterns = [r'.*']
   changelog_exclude_patterns = []

Missing Versions
~~~~~~~~~~~~~~~~

**Problem**: Some versions not appearing

**Solution**:

.. code-block:: python

   # Check version pattern
   changelog_version_pattern = r'^v?(\d+\.\d+\.\d+)$'
   
   # List all tags
   git tag -l
   
   # Ensure tags match pattern

GitHub Rate Limiting
~~~~~~~~~~~~~~~~~~~~

**Problem**: GitHub API rate limit exceeded

**Solution**:

.. code-block:: python

   # Use authentication token
   changelog_github_token = os.getenv('GITHUB_TOKEN')
   
   # Cache results
   changelog_cache_github = True
   changelog_cache_ttl = 3600

Integration Examples
--------------------

With ReadTheDocs
~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   import os
   
   on_rtd = os.environ.get('READTHEDOCS') == 'True'
   
   if on_rtd:
       # Ensure Git history is available
       os.system('git fetch --unshallow')
   
   changelog_source = 'git'

With CI/CD
~~~~~~~~~~

.. code-block:: yaml

   # .github/workflows/release.yml
   name: Release
   
   on:
     push:
       tags:
         - 'v*'
   
   jobs:
     release:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v2
           with:
             fetch-depth: 0  # Full history for changelog
         
         - name: Generate Changelog
           run: |
             pip install sphinx sphinx-changelog
             sphinx-build -b html docs build/html

With Sphinx-Autobuild
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Watch for changelog updates
   sphinx-autobuild docs build/html \
     --watch CHANGELOG.md \
     --watch .git/refs/tags


Practical Examples
------------------

Installation
------------

Using pip
~~~~~~~~~

Install the extension:

.. code-block:: bash

   pip install sphinx-changelog

Or add to your ``requirements.txt``:

.. code-block:: text

   sphinx-changelog>=1.2.0
   gitpython>=3.0.0

Configuration
-------------

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_changelog',
       # ... other extensions
   ]
   
   # Basic changelog settings
   changelog_source = 'git'  # 'git', 'github', 'gitlab', 'file'
   changelog_file = 'CHANGELOG.rst'

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

Complete configuration with all options:

.. code-block:: python

   # Source Configuration
   changelog_source = 'git'  # 'git', 'github', 'gitlab', 'file'
   changelog_file = 'CHANGELOG.rst'
   changelog_repo_path = '.'
   
   # Version Management
   changelog_version_pattern = r'^v?(\d+\.\d+\.\d+)$'
   changelog_include_unreleased = True
   changelog_unreleased_title = 'Unreleased'
   
   # Grouping and Categories
   changelog_categories = [
       'Added',
       'Changed',
       'Deprecated',
       'Removed',
       'Fixed',
       'Security',
   ]
   changelog_group_by = 'category'  # 'category', 'version', 'date'
   
   # Commit Filtering
   changelog_include_patterns = [r'.*']
   changelog_exclude_patterns = [
       r'^Merge',
       r'^WIP',
       r'^\[skip\]',
   ]
   changelog_commit_format = 'conventional'  # 'conventional', 'custom'
   
   # GitHub/GitLab Integration
   changelog_github_repo = 'owner/repo'
   changelog_github_token = os.getenv('GITHUB_TOKEN')
   changelog_gitlab_url = 'https://gitlab.com'
   changelog_gitlab_project_id = '12345'
   
   # Cross-References
   changelog_issue_pattern = r'#(\d+)'
   changelog_issue_url = 'https://github.com/owner/repo/issues/{issue}'
   changelog_pr_pattern = r'!(\d+)'
   changelog_pr_url = 'https://github.com/owner/repo/pull/{pr}'
   
   # Display Options
   changelog_show_authors = True
   changelog_show_dates = True
   changelog_show_commits = False
   changelog_show_links = True
   
   # Template Options
   changelog_template = 'changelog.rst_t'
   changelog_section_depth = 2

Directives
----------

changelog Directive
~~~~~~~~~~~~~~~~~~~

Generate complete changelog:

.. code-block:: rst

   .. changelog::
      :source: git
      :versions: 1.0.0, 1.1.0, 2.0.0
      :group-by: category
      
      Complete project changelog.

changelog-version Directive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Document specific version:

.. code-block:: rst

   .. changelog-version:: 2.0.0
      :date: 2024-01-20
      :show-commits: true
      :show-authors: true
      
      Changes in version 2.0.0.

changelog-category Directive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Show specific category of changes:

.. code-block:: rst

   .. changelog-category:: Fixed
      :version: 2.0.0
      :show-issues: true
      
      Bug fixes in version 2.0.0.

changelog-unreleased Directive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Show unreleased changes:

.. code-block:: rst

   .. changelog-unreleased::
      :group-by: category
      :show-commits: true
      
      Upcoming changes not yet released.

Roles
-----

Changelog References
~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   See :changelog:`version 2.0.0 <2.0.0>` for details.
   
   Fixed in :issue:`123`.
   
   Merged :pr:`456`.
   
   By :author:`johndoe`.

Practical Examples
------------------

Complete Changelog
~~~~~~~~~~~~~~~~~~

**File**: ``changelog.rst``

.. code-block:: rst

   Changelog
   =========
   
   All notable changes to this project are documented here.
   
   The format is based on `Keep a Changelog <https://keepachangelog.com/>`_,
   and this project adheres to `Semantic Versioning <https://semver.org/>`_.
   
   .. changelog::
      :source: git
      :group-by: category
      :show-authors: true
      :show-dates: true
      :include-unreleased: true
      
      Project changelog generated from Git history.

Version-Specific Changelog
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Version 2.0.0
   =============
   
   *Released: 2024-01-20*
   
   .. changelog-version:: 2.0.0
      :group-by: category
      :show-commits: true
      :show-issues: true
      :show-authors: true
   
   Added
   -----
   
   - New feature X
   - Enhanced functionality Y
   
   Changed
   -------
   
   - Modified behavior of Z
   - Updated dependencies
   
   Fixed
   -----
   
   - Resolved :issue:`123`
   - Fixed :issue:`456`

Categorized Changelog
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Recent Changes
   ==============
   
   Bug Fixes
   ---------
   
   .. changelog-category:: Fixed
      :versions: 2.0.0, 1.9.0
      :show-issues: true
      
      Recent bug fixes.
   
   New Features
   ------------
   
   .. changelog-category:: Added
      :versions: 2.0.0
      :show-details: true
      
      Newly added features.
   
   Breaking Changes
   ----------------
   
   .. changelog-category:: Changed
      :versions: 2.0.0
      :breaking-only: true
      
      Breaking changes requiring attention.

Unreleased Changes
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Upcoming Release
   ================
   
   .. changelog-unreleased::
      :group-by: category
      :show-commits: true
      :since: v1.9.0
      
      Changes since last release.
   
   Planned for v2.1.0
   ------------------
   
   **Added**
   
   - Feature A (in progress)
   - Feature B (planned)
   
   **Fixed**
   
   - Bug fixes committed but not released

Sample Changelog File
---------------------

Keep a Changelog Format
~~~~~~~~~~~~~~~~~~~~~~~

**File**: ``CHANGELOG.md``

.. code-block:: markdown

   # Changelog
   
   All notable changes to this project will be documented in this file.
   
   The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
   and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
   
   ## [Unreleased]
   
   ### Added
   - New API endpoint for user management
   - Support for Python 3.11
   
   ### Changed
   - Improved error messages
   - Updated documentation
   
   ### Fixed
   - Memory leak in cache module
   - Race condition in async operations
   
   ## [2.0.0] - 2024-01-20
   
   ### Added
   - Major refactoring of core modules
   - New plugin system
   - CLI enhancements
   
   ### Changed
   - Breaking: Renamed `old_function()` to `new_function()`
   - Updated all dependencies to latest versions
   
   ### Removed
   - Deprecated functions from v1.x
   
   ### Fixed
   - Critical security vulnerability (#123)
   - Data corruption bug (#456)
   
   ## [1.9.0] - 2024-01-15
   
   ### Added
   - Feature X with configuration options
   - Integration with Service Y
   
   ### Fixed
   - Bug in parser (#789)
   - Incorrect validation (#790)

RST Format
~~~~~~~~~~

**File**: ``CHANGELOG.rst``

.. code-block:: rst

   Changelog
   =========
   
   Unreleased
   ----------
   
   Added
   ~~~~~
   
   - New feature for batch processing
   - Additional validation options
   
   Fixed
   ~~~~~
   
   - Resolved timeout issues
   - Fixed parsing edge cases
   
   2.0.0 - 2024-01-20
   ------------------
   
   Added
   ~~~~~
   
   - Plugin architecture
   - Extended API
   - CLI improvements
   
   Changed
   ~~~~~~~
   
   - **Breaking**: Renamed core functions
   - Updated configuration format
   
   Deprecated
   ~~~~~~~~~~
   
   - Old API will be removed in v3.0
   
   Removed
   ~~~~~~~
   
   - Legacy compatibility layer
   
   Fixed
   ~~~~~
   
   - Security issue in authentication
   - Memory management improvements
   
   Security
   ~~~~~~~~
   
   - Fixed CVE-2024-12345

Conventional Commits
--------------------

Commit Message Format
~~~~~~~~~~~~~~~~~~~~~

Use conventional commit format:

.. code-block:: text

   <type>(<scope>): <subject>
   
   <body>
   
   <footer>

Types:

- ``feat``: New feature (Added)
- ``fix``: Bug fix (Fixed)
- ``docs``: Documentation changes
- ``style``: Code style changes
- ``refactor``: Code refactoring (Changed)
- ``perf``: Performance improvements
- ``test``: Test updates
- ``chore``: Build/tool changes

Examples
~~~~~~~~

.. code-block:: text

   feat(api): add user authentication endpoint
   
   Implements JWT-based authentication for API endpoints.
   Includes middleware for token validation.
   
   Closes #123

.. code-block:: text

   fix(parser): resolve edge case in URL parsing
   
   Fixed issue where URLs with special characters were
   incorrectly parsed.
   
   Fixes #456

.. code-block:: text

   docs(readme): update installation instructions
   
   Added troubleshooting section and updated examples.

Configuration for Conventional Commits
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   changelog_commit_format = 'conventional'
   changelog_conventional_types = {
       'feat': 'Added',
       'fix': 'Fixed',
       'docs': 'Documentation',
       'style': 'Style',
       'refactor': 'Changed',
       'perf': 'Performance',
       'test': 'Testing',
       'chore': 'Chores',
   }

Advanced Features
-----------------

GitHub Integration
~~~~~~~~~~~~~~~~~~

Pull release notes from GitHub:

.. code-block:: python

   # conf.py
   changelog_source = 'github'
   changelog_github_repo = 'owner/repo'
   changelog_github_token = os.getenv('GITHUB_TOKEN')
   changelog_include_pulls = True
   changelog_include_issues = True

.. code-block:: rst

   .. changelog::
      :source: github
      :releases: 3
      :show-pull-requests: true
      
      Recent releases from GitHub.

GitLab Integration
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   changelog_source = 'gitlab'
   changelog_gitlab_url = 'https://gitlab.com'
   changelog_gitlab_project_id = '12345'
   changelog_gitlab_token = os.getenv('GITLAB_TOKEN')

Custom Templates
~~~~~~~~~~~~~~~~

**File**: ``_templates/changelog.rst_t``

.. code-block:: jinja

   Changelog
   =========
   
   {% for version in versions %}
   {{ version.name }} - {{ version.date }}
   {{ "-" * (version.name|length + version.date|length + 3) }}
   
   {% for category in categories %}
   {% if version.changes[category] %}
   {{ category }}
   {{ "~" * category|length }}
   
   {% for change in version.changes[category] %}
   - {{ change.description }}
     {% if change.author %}by {{ change.author }}{% endif %}
     {% if change.issues %}({{ change.issues|join(', ') }}){% endif %}
   {% endfor %}
   
   {% endif %}
   {% endfor %}
   
   {% endfor %}

Filtering Changes
~~~~~~~~~~~~~~~~~

Filter commits by pattern:

.. code-block:: python

   # conf.py
   changelog_include_patterns = [
       r'^feat:',
       r'^fix:',
       r'^BREAKING:',
   ]
   
   changelog_exclude_patterns = [
       r'^Merge',
       r'^chore:',
       r'^\[skip changelog\]',
   ]

Best Practices
--------------

Commit Messages
~~~~~~~~~~~~~~~

1. **Clear and Concise**: Write descriptive commit messages
2. **Follow Convention**: Use conventional commit format
3. **Reference Issues**: Link to issue tracker
4. **Breaking Changes**: Mark breaking changes clearly

Version Tagging
~~~~~~~~~~~~~~~

Use semantic versioning for tags:

.. code-block:: bash

   # Create version tags
   git tag -a v2.0.0 -m "Release version 2.0.0"
   git push origin v2.0.0

Changelog Maintenance
~~~~~~~~~~~~~~~~~~~~~

Keep changelog updated:

.. code-block:: rst

   .. changelog::
      :auto-update: true
      :validate: true
      :warn-missing: true

Troubleshooting
---------------

No Changelog Generated
~~~~~~~~~~~~~~~~~~~~~~

**Problem**: Changelog directive produces no output

**Solution**:

.. code-block:: python

   # Check Git repository
   changelog_repo_path = '.'
   
   # Verify version tags exist
   git tag -l
   
   # Check patterns
   changelog_include_patterns = [r'.*']
   changelog_exclude_patterns = []

Missing Versions
~~~~~~~~~~~~~~~~

**Problem**: Some versions not appearing

**Solution**:

.. code-block:: python

   # Check version pattern
   changelog_version_pattern = r'^v?(\d+\.\d+\.\d+)$'
   
   # List all tags
   git tag -l
   
   # Ensure tags match pattern

GitHub Rate Limiting
~~~~~~~~~~~~~~~~~~~~

**Problem**: GitHub API rate limit exceeded

**Solution**:

.. code-block:: python

   # Use authentication token
   changelog_github_token = os.getenv('GITHUB_TOKEN')
   
   # Cache results
   changelog_cache_github = True
   changelog_cache_ttl = 3600

Integration Examples
--------------------

With ReadTheDocs
~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   import os
   
   on_rtd = os.environ.get('READTHEDOCS') == 'True'
   
   if on_rtd:
       # Ensure Git history is available
       os.system('git fetch --unshallow')
   
   changelog_source = 'git'

With CI/CD
~~~~~~~~~~

.. code-block:: yaml

   # .github/workflows/release.yml
   name: Release
   
   on:
     push:
       tags:
         - 'v*'
   
   jobs:
     release:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v2
           with:
             fetch-depth: 0  # Full history for changelog
         
         - name: Generate Changelog
           run: |
             pip install sphinx sphinx-changelog
             sphinx-build -b html docs build/html

With Sphinx-Autobuild
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Watch for changelog updates
   sphinx-autobuild docs build/html \
     --watch CHANGELOG.md \
     --watch .git/refs/tags

Additional Resources
--------------------
- :doc:`sphinx-git` - Git integration
- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `Keep a Changelog <https://keepachangelog.com/>`_
- `Semantic Versioning <https://semver.org/>`_
- `Towncrier <https://towncrier.readthedocs.io/>`_
Related Extensions
~~~~~~~~~~~~~~~~~~
- :doc:`sphinx-git-example` - Git information in docs
- Keep a Changelog: https://keepachangelog.com/
- Semantic Versioning: https://semver.org/
External Resources
- Conventional Commits: https://www.conventionalcommits.org/
- GitHub Releases: https://docs.github.com/en/repositories/releasing-projects-on-github
Summary
-------
sphinx-changelog provides comprehensive changelog generation:
- **Automatic Generation**: From Git history, GitHub, GitLab
- **Multiple Formats**: Keep a Changelog, conventional commits
- **Smart Categorization**: Group by type, version, date
- **Cross-References**: Link issues and pull requests
- **Customizable**: Templates and filtering options
- **Integration**: CI/CD, version control platforms
- **Best Practices**: Semantic versioning, conventional commits
Perfect for maintaining professional, up-to-date changelog documentation automatically.


Summary
-------
sphinx-changelog provides comprehensive changelog generation:
- **Automatic Generation**: From Git history, GitHub, GitLab
- **Multiple Formats**: Keep a Changelog, conventional commits
- **Smart Categorization**: Group by type, version, date
- **Cross-References**: Link issues and pull requests
- **Customizable**: Templates and filtering options
- **Integration**: CI/CD, version control platforms
- **Best Practices**: Semantic versioning, conventional commits
Perfect for maintaining professional, up-to-date changelog documentation automatically.


Summary
-------
sphinx-changelog provides comprehensive changelog generation:
- **Automatic Generation**: From Git history, GitHub, GitLab
- **Multiple Formats**: Keep a Changelog, conventional commits
- **Smart Categorization**: Group by type, version, date
- **Cross-References**: Link issues and pull requests
- **Customizable**: Templates and filtering options
- **Integration**: CI/CD, version control platforms
- **Best Practices**: Semantic versioning, conventional commits
Perfect for maintaining professional, up-to-date changelog documentation automatically.

