Sphinx-Issues Example
=====================

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
