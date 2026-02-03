Sphinx-Issues Tutorial
======================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-issues/>`_
   - `API Documentation <../../pdoc/sphinx_issues/index.html>`_
   - `Manual <https://github.com/sloria/sphinx-issues>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinx-issues to easily reference GitHub, GitLab, or Bitbucket issues and pull requests in your Sphinx documentation.

What is Sphinx-Issues?
-----------------------
sphinx-issues is a Sphinx extension that provides simple roles for linking to:

- GitHub issues and pull requests
- GitLab issues and merge requests  
- Bitbucket issues and pull requests
- Custom issue trackers
- Commit references
- User profiles

It automatically generates proper links with minimal markup, making your documentation more maintainable and connected to your project's development.

sphinx-issues simplifies referencing issues and pull requests in your documentation by providing convenient roles that automatically create links to your issue tracker.


Installation
------------

sphinx-issues is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm viper-sphinx:latest python -c "import sphinx_issues; print(sphinx_issues.__version__)"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_issues',
   ]
   
   # GitHub configuration
   issues_github_path = 'user/repo'

GitLab Configuration
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinx_issues']
   
   # GitLab configuration
   issues_uri = 'https://gitlab.com/{group}/{project}/issues/{issue}'
   issues_pr_uri = 'https://gitlab.com/{group}/{project}/merge_requests/{pr}'
   issues_commit_uri = 'https://gitlab.com/{group}/{project}/commit/{commit}'
   issues_user_uri = 'https://gitlab.com/{user}'

Bitbucket Configuration
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinx_issues']
   
   # Bitbucket configuration
   issues_uri = 'https://bitbucket.org/{user}/{repo}/issues/{issue}'
   issues_pr_uri = 'https://bitbucket.org/{user}/{repo}/pull-requests/{pr}'

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinx_issues']
   
   # GitHub (default)
   issues_github_path = 'myorg/myproject'
   
   # Custom issue tracker
   issues_uri = 'https://jira.example.com/browse/{issue}'
   issues_pr_uri = 'https://gerrit.example.com/{pr}'
   issues_commit_uri = 'https://git.example.com/commit/{commit}'
   issues_user_uri = 'https://git.example.com/u/{user}'
   
   # Issue prefix (default is '#')
   issues_default_group_project = 'myorg/myproject'


.. code-block:: python

   # Custom issue URL pattern
   issues_uri = 'https://custom-tracker.com/issues/{issue}'
   
   # Custom PR URL pattern  
   issues_pr_uri = 'https://custom-tracker.com/pr/{pr}'
   
   # Custom user URL pattern
   issues_user_uri = 'https://custom-tracker.com/users/{user}'
   
   # Custom commit URL pattern
   issues_commit_uri = 'https://custom-tracker.com/commit/{commit}'

Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_issues',
       # ... other extensions
   ]
   
   # GitHub configuration
   issues_github_path = 'username/repository'
   
   # Or GitLab
   # issues_gitlab_path = 'username/repository'
   
   # Or Bitbucket
   # issues_bitbucket_path = 'username/repository'

Basic Usage
-----------

Issue References
~~~~~~~~~~~~~~~~

.. code-block:: rst

   This feature is tracked in :issue:`123`.
   
   See also :issue:`456` and :issue:`789`.
   
   Fixed in :issue:`42`.

Renders as:

- This feature is tracked in #123.
- See also #456 and #789.
- Fixed in #42.

Pull Request References
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Implemented in :pr:`100`.
   
   Review :pr:`200` before merging.

Renders as:

- Implemented in #100.
- Review #200 before merging.

Commit References
~~~~~~~~~~~~~~~~~

.. code-block:: rst

   See commit :commit:`abc123def`.
   
   Fixed in :commit:`1234567890abcdef`.

Renders as:

- See commit abc123d.
- Fixed in 1234567.

User References
~~~~~~~~~~~~~~~

.. code-block:: rst

   Thanks to :user:`johndoe` for the contribution.
   
   Reported by :user:`janedoe`.

Renders as:

- Thanks to @johndoe for the contribution.
- Reported by @janedoe.

   Async Processing
   ================
   
   .. versionadded:: 2.0
      Async support added in :pr:`155`
   
   The async processing feature allows non-blocking operations.
   This was requested in :issue:`150` and implemented by :user:`alice`.
   
   Usage
   -----
   
   .. code-block:: python
   
      import asyncio
      from mylib import AsyncProcessor
      
      async def main():
          processor = AsyncProcessor()
          result = await processor.process(data)
      
      asyncio.run(main())
   
   Known Issues
   ------------
   
   - Performance on Windows needs improvement (:issue:`160`)
   - Memory usage is higher than sync version (:issue:`165`)
   
   See the implementation in :commit:`abc123def`.

Example 3: Bug Reports and Fixes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Known Issues
   ============
   
   Critical
   --------
   
   - Data corruption on concurrent writes (:issue:`200`)
     
     Workaround: Use locking mechanism until fixed
     
   - Memory leak in long-running processes (:issue:`195`)
     
     Fix pending in :pr:`198`
   
   Non-Critical
   ------------
   
   - UI glitch in dark mode (:issue:`180`, fixed in :pr:`185`)
   - Typo in error message (:issue:`175`)
   
   Recently Fixed
   --------------
   
   - ✅ Cache invalidation bug (:issue:`170`, :pr:`172`)
   - ✅ Unicode handling (:issue:`165`, :commit:`xyz789`)

Example 4: Development Roadmap
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Development Roadmap
   ===================
   
   Q1 2026
   -------
   
   High Priority
   ~~~~~~~~~~~~~
   
   - [ ] Database migration tool (:issue:`250`)
   - [ ] GraphQL API (:issue:`245`)
   - [ ] Multi-tenant support (:issue:`240`)
   
   Medium Priority
   ~~~~~~~~~~~~~~~
   
   - [ ] Improved logging (:issue:`230`)
   - [ ] Plugin marketplace (:issue:`225`)
   
   Q2 2026
   -------
   
   - [ ] Machine learning integration (:issue:`300`)
   - [ ] Real-time collaboration (:issue:`290`)
   - [ ] Mobile app (:issue:`280`)
   
   Community Requests
   ------------------
   
   Most requested by users:
   
   1. Dark theme (:issue:`350` - 👍 50)
   2. Export to PDF (:issue:`340` - 👍 45)
   3. API versioning (:issue:`330` - 👍 40)

Example 5: Contributing Guide
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Contributing
   ============
   
   We welcome contributions! Here's how to get started.
   
   Finding Issues
   --------------
   
   Good first issues:
   
   - :issue:`100` - Add unit tests
   - :issue:`105` - Improve documentation
   - :issue:`110` - Fix typos
   
   Bug Reports
   -----------
   
   Before reporting a bug, check if it's already reported:
   
   - Search existing issues: https://github.com/user/repo/issues
   - Check recently fixed: :issue:`90`, :issue:`95`
   
   Pull Requests
   -------------
   
   1. Fork the repository
   2. Create a feature branch
   3. Make your changes
   4. Submit a PR referencing the issue:
   
      Example: "Fixes :issue:`123`"
   
   Recent Contributors
   -------------------
   
   Big thanks to:
   
   - :user:`developer1` (:pr:`200`, :pr:`205`)
   - :user:`developer2` (:pr:`195`)
   - :user:`developer3` (:pr:`190`, :pr:`185`)

Advanced Features
-----------------

Cross-Repository References
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Reference issues in other repos:

.. code-block:: python

   # conf.py
   issues_github_path = 'myorg/main-repo'

In RST:

.. code-block:: rst

   Related to issue in other repo: myorg/other-repo#123
   
   (Note: Manual link needed for cross-repo)
   `myorg/other-repo#123 <https://github.com/myorg/other-repo/issues/123>`_

Custom Link Text
~~~~~~~~~~~~~~~~

.. code-block:: rst

   See `bug #123 <:issue:`123`>`_ for details.
   
   The `original request <:issue:`100`>`_ was filed last year.

Issue Lists
~~~~~~~~~~~

.. code-block:: rst

   Open Issues
   ===========
   
   .. list-table::
      :header-rows: 1
      :widths: 10 60 30
   
      * - ID
        - Description
        - Status
      * - :issue:`200`
        - Add dark theme
        - In Progress
      * - :issue:`195`
        - Fix memory leak
        - Under Review (:pr:`198`)
      * - :issue:`190`
        - Improve docs
        - Open

Combining with Other Roles
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   The :func:`process_data` function has a bug (:issue:`150`)
   that was fixed in :commit:`abc123` by :user:`alice`.
   
   See :doc:`api/reference` for usage and :issue:`145` for
   known limitations.

Docker Integration
------------------

Build Documentation with Issue Links
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Build with issue tracking enabled
   docker run --rm \
     -v $(pwd):/project \
     -e GITHUB_PATH="myorg/myrepo" \
     viper-sphinx:latest \
     sphinx-build -b html /project/docs /project/docs/_build/html

Automated Link Validation
~~~~~~~~~~~~~~~~~~~~~~~~~~

Create ``validate_issues.sh``:

.. code-block:: bash

   #!/bin/bash
   
   echo "Building documentation..."
   docker run --rm -v $(pwd):/project viper-sphinx:latest \
     sphinx-build -b html docs/ docs/_build/html
   
   echo "Checking for broken issue links..."
   docker run --rm -v $(pwd):/project viper-sphinx:latest \
     sphinx-build -b linkcheck docs/ docs/_build/linkcheck
   
   echo "Done!"

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Build Docs with Issue Links
   
   on:
     push:
       paths:
         - 'docs/**'
   
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Build Documentation
           env:
             GITHUB_REPO: ${{ github.repository }}
           run: |
             docker run --rm \
               -v $(pwd):/project \
               -e GITHUB_PATH="$GITHUB_REPO" \
               viper-sphinx:latest \
               sphinx-build -b html docs/ docs/_build/html
         
         - name: Deploy to GitHub Pages
           uses: peaceiris/actions-gh-pages@v3
           with:
             github_token: ${{ secrets.GITHUB_TOKEN }}
             publish_dir: ./docs/_build/html

GitLab CI
~~~~~~~~~

.. code-block:: yaml

   build-docs:
     image: viper-sphinx:latest
     variables:
       GITLAB_PROJECT: ${CI_PROJECT_PATH}
     script:
       - sphinx-build -b html docs/ public
     artifacts:
       paths:
         - public

Dynamic Configuration
~~~~~~~~~~~~~~~~~~~~~

``conf.py``:

.. code-block:: python

   import os
   
   extensions = ['sphinx_issues']
   
   # Get from environment or default
   issues_github_path = os.getenv(
       'GITHUB_PATH', 
       'default-org/default-repo'
   )

Best Practices
--------------

1. **Reference Issues Liberally**
   
   Link to issues whenever discussing features, bugs, or changes:
   
   .. code-block:: rst
   
      This behavior was changed in version 2.0 (:issue:`150`)

2. **Use in Changelogs**
   
   Always link to issues and PRs in changelogs:
   
   .. code-block:: rst
   
      - Fixed bug (:issue:`100`, :pr:`105`)

3. **Credit Contributors**
   
   Acknowledge contributors using ``:user:`` role:
   
   .. code-block:: rst
   
      Thanks to :user:`contributor` for implementing this!

4. **Keep Links Updated**
   
   When issues are closed or resolved, update documentation:
   
   .. code-block:: rst
   
      - ~~Known issue (:issue:`50`)~~ - Fixed in v2.0

5. **Document Workarounds**
   
   For known issues, provide workarounds with issue links:
   
   .. code-block:: rst
   
      **Known Issue** (:issue:`75`): Slow performance
      
      Workaround: Use ``--fast`` flag

6. **Combine with Versions**
   
   Use with version directives:
   
   .. code-block:: rst
   
      .. versionadded:: 2.0
         New feature (:issue:`200`)
      
      .. deprecated:: 3.0
         Will be removed (:issue:`300`)

Common Patterns
---------------

Release Notes Template
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Version X.Y.Z
   =============
   
   Released: YYYY-MM-DD
   
   Highlights
   ----------
   
   - Major feature (:issue:`XXX`, :pr:`YYY`)
   - Important fix (:issue:`ZZZ`)
   
   New Features
   ------------
   
   - Feature 1 (:issue:`AAA`, thanks :user:`person1`)
   - Feature 2 (:issue:`BBB`, :pr:`CCC`)
   
   Improvements
   ------------
   
   - Improvement 1 (:issue:`DDD`)
   - Improvement 2 (:pr:`EEE`)
   
   Bug Fixes
   ---------
   
   - Fixed bug 1 (:issue:`FFF`, :pr:`GGG`)
   - Fixed bug 2 (:issue:`HHH`)
   
   Contributors
   ------------
   
   - :user:`person1`
   - :user:`person2`
   - :user:`person3`

Migration Guide Template
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Migrating from v1 to v2
   =======================
   
   Breaking Changes
   ----------------
   
   API Changes
   ~~~~~~~~~~~
   
   The ``old_function()`` was removed (:issue:`500`).
   
   **Before:**
   
   .. code-block:: python
   
      result = old_function(data)
   
   **After:**
   
   .. code-block:: python
   
      result = new_function(data)
   
   See :issue:`500` and :pr:`505` for details.
   
   Configuration Changes
   ~~~~~~~~~~~~~~~~~~~~
   
   Config option ``old_setting`` was renamed (:issue:`510`).
   
   Update your ``config.yml``:
   
   .. code-block:: diff
   
      - old_setting: value
      + new_setting: value

Troubleshooting
---------------

Links Not Resolving
~~~~~~~~~~~~~~~~~~~

**Issue:** Issue links show as plain text

**Solution:**

1. Check extension is enabled:

   .. code-block:: python
   
      extensions = ['sphinx_issues']

2. Verify ``issues_github_path`` is set:

   .. code-block:: python
   
      issues_github_path = 'user/repo'

3. Rebuild documentation:

   .. code-block:: bash
   
      docker run --rm -v $(pwd):/project viper-sphinx:latest \
        sphinx-build -b html docs/ docs/_build/html

Wrong Repository Links
~~~~~~~~~~~~~~~~~~~~~~

**Issue:** Links point to wrong repository

**Solution:**

Check configuration:

.. code-block:: python

   # Make sure this matches your repo
   issues_github_path = 'correct-user/correct-repo'

Custom Tracker Not Working
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Issue:** Custom issue tracker links don't work

**Solution:**

Verify URI templates:

.. code-block:: python

   # Check placeholders match
   issues_uri = 'https://tracker.example.com/issue/{issue}'
   
   # Test with actual values
   # {issue} will be replaced with issue number

Link Check Failures
~~~~~~~~~~~~~~~~~~~

**Issue:** Link checker reports broken issue links

**Solution:**

This may happen if:

- Issue is private or deleted
- Repository is private
- Network/rate limiting issues

Add to ``conf.py``:

.. code-block:: python

   # Skip checking issue links
   linkcheck_ignore = [
       r'https://github.com/.*/issues/.*',
   ]

Additional Examples
-------------------

API Deprecation Notice
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. warning::
      
      This API is deprecated as of version 3.0 (:issue:`400`)
      and will be removed in version 4.0 (:issue:`450`).
      
      Please migrate to :func:`new_api` as shown in :issue:`400`.

Feature Comparison
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Feature Comparison
   ==================
   
   .. list-table::
      :header-rows: 1
   
      * - Feature
        - Status
        - Reference
      * - Dark Theme
        - ✅ Available
        - :issue:`100`
      * - Export PDF
        - 🚧 In Progress
        - :pr:`150`
      * - API v2
        - 📋 Planned
        - :issue:`200`

Next Steps
----------

1. Configure sphinx-issues for your repository
2. Add issue references to your documentation
3. Update changelog with issue/PR links
4. Create a contributing guide with issue references
5. Integrate with your CI/CD pipeline


Practical Examples
------------------

This page demonstrates the **sphinx-issues** extension which provides easy linking to GitHub, GitLab, and Bitbucket issues and pull requests.


Configuration
-------------

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_issues',
       # ... other extensions
   ]
   
   # GitHub configuration
   issues_github_path = 'username/repository'
   
   # Or GitLab
   # issues_gitlab_path = 'username/repository'
   
   # Or Bitbucket
   # issues_bitbucket_path = 'username/repository'

Basic Usage
-----------

Issue References
~~~~~~~~~~~~~~~~

Reference GitHub issues using the ``:issue:`` role:

.. code-block:: rst

   This bug was fixed in :issue:`123`
   
   Multiple issues: :issue:`45`, :issue:`67`, :issue:`89`
   
   See issue :issue:`42` for details

**Renders as:**

- This bug was fixed in #123 (links to https://github.com/username/repository/issues/123)
- Multiple issues: #45, #67, #89
- See issue #42 for details

Pull Request References
~~~~~~~~~~~~~~~~~~~~~~~~

Link to pull requests with the ``:pr:`` role:

.. code-block:: rst

   Merged in :pr:`456`
   
   Thanks to the contributor in :pr:`789`

**Renders as:**

- Merged in PR #456
- Thanks to the contributor in PR #789

User Mentions
~~~~~~~~~~~~~

Reference GitHub users with the ``:user:`` role:

.. code-block:: rst

   Implementation by :user:`octocat`
   
   Review by :user:`torvalds`

**Renders as:**

- Implementation by @octocat
- Review by @torvalds

Commit References
~~~~~~~~~~~~~~~~~

Link to specific commits with the ``:commit:`` role:

.. code-block:: rst

   Fixed in :commit:`a1b2c3d`
   
   See commit :commit:`1234567890abcdef`

**Renders as:**

- Fixed in a1b2c3d
- See commit 1234567

Advanced Examples
-----------------

Changelog Documentation
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Version 2.0.0 (2026-01-26)
   --------------------------
   
   Features
   ~~~~~~~~
   
   - Add new caching system (:issue:`234`, :pr:`245`)
   - Implement async support (:issue:`156`, :pr:`167`)
   - Add plugin architecture (:pr:`289`)
   
   Bug Fixes
   ~~~~~~~~~
   
   - Fix memory leak in parser (:issue:`198`)
   - Resolve race condition (:issue:`201`, :pr:`203`)
   - Handle edge cases in validator (:issue:`178`)
   
   Contributors
   ~~~~~~~~~~~~
   
   Thanks to :user:`alice`, :user:`bob`, and :user:`charlie` 
   for their contributions!

Release Notes
~~~~~~~~~~~~~

.. code-block:: rst

   Release v1.5.0
   ==============
   
   New Features
   ------------
   
   **Database Optimization** (:pr:`567`)
     Improved query performance by 40%. Originally requested 
     in :issue:`543`.
   
   **API Enhancement** (:pr:`589`)
     Extended API with new endpoints. Closes :issue:`512` 
     and :issue:`530`.
   
   Deprecations
   ------------
   
   - Old authentication method deprecated (:issue:`445`)
     Will be removed in v2.0 (:issue:`490`)

Contributing Guide
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Contributing
   ============
   
   Reporting Issues
   ----------------
   
   Before creating an issue, please search existing issues 
   to avoid duplicates.
   
   Template for bug reports: :issue:`1` (pinned)
   
   Submitting Pull Requests
   -------------------------
   
   1. Fork the repository
   2. Create a feature branch
   3. Make your changes
   4. Submit a pull request
   
   Example PR: :pr:`100`
   
   Code Review Process
   -------------------
   
   All PRs require review from :user:`maintainer1` or 
   :user:`maintainer2`.
   
   See :pr:`150` for a good example of a well-documented PR.

Configuration Options
---------------------

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Custom issue URL pattern
   issues_uri = 'https://custom-tracker.com/issues/{issue}'
   
   # Custom PR URL pattern  
   issues_pr_uri = 'https://custom-tracker.com/pr/{pr}'
   
   # Custom user URL pattern
   issues_user_uri = 'https://custom-tracker.com/users/{user}'
   
   # Custom commit URL pattern
   issues_commit_uri = 'https://custom-tracker.com/commit/{commit}'

Multiple Repositories
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Default repository
   issues_github_path = 'main-org/main-repo'
   
   # Reference other repos inline
   # :issue:`org/repo#123`

Role Reference
--------------

.. list-table::
   :header-rows: 1
   :widths: 20 30 50

   * - Role
     - Syntax
     - Output
   * - Issue
     - ``:issue:`123```
     - #123 (linked)
   * - Pull Request
     - ``:pr:`456```
     - PR #456 (linked)
   * - User
     - ``:user:`username```
     - @username (linked)
   * - Commit
     - ``:commit:`abc123```
     - abc123 (linked)

Real-World Example
------------------

**Documentation Page**:

.. code-block:: rst

   Installation Issues
   ===================
   
   Common Problems
   ---------------
   
   **ImportError on Windows**
     See :issue:`89` for the solution. Fixed in :commit:`3c4d5e6`.
   
   **SSL Certificate Errors**
     Workaround documented in :issue:`112`. 
     Permanent fix in :pr:`125` by :user:`security-expert`.
   
   **Database Connection Failures**
     Multiple related issues: :issue:`201`, :issue:`203`, :issue:`208`.
     Comprehensive fix in :pr:`215`.
   
   Migration Guide
   ---------------
   
   Breaking changes in v2.0 are tracked in :issue:`300`.
   Migration script available in :pr:`305`.
   
   Community contributions from :user:`contributor1`, 
   :user:`contributor2`, and many others made this possible!

Benefits
--------

1. **Automatic Linking**: No need to write full URLs
2. **Consistency**: Uniform formatting across documentation
3. **Maintainability**: Change tracker URL in one place
4. **Readability**: Clean, concise syntax
5. **Multi-Platform**: Works with GitHub, GitLab, Bitbucket

Learn More
----------

For complete documentation and configuration options, see:

- :doc:`../tutorials/packages/sphinx-issues` - Full tutorial
- `sphinx-issues GitHub <https://github.com/sloria/sphinx-issues>`_ - Project repository
- `GitHub Issues API <https://docs.github.com/en/rest/issues>`_ - API reference

Additional Resources
--------------------

- `sphinx-issues Documentation <https://github.com/sloria/sphinx-issues>`_
- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- :doc:`../extensions` - Other useful extensions
- `GitHub API <https://docs.github.com/en/rest>`_
- `GitLab API <https://docs.gitlab.com/ee/api/>`_
