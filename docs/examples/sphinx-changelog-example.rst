Sphinx-Changelog Example
=========================

.. note::

   **Package**: sphinx-changelog  
   **Purpose**: Automatically generate changelog documentation from version control  
   **Tutorial**: See :doc:`../tutorials/packages/sphinx-changelog` for complete tutorial

This page demonstrates the **sphinx-changelog** extension for automatically generating and maintaining changelog documentation.

.. contents:: Contents
   :local:
   :depth: 3


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

See Also
--------

Related Extensions
~~~~~~~~~~~~~~~~~~

- :doc:`sphinx-git-example` - Git information in docs
- Keep a Changelog: https://keepachangelog.com/
- Semantic Versioning: https://semver.org/

External Resources
~~~~~~~~~~~~~~~~~~

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
