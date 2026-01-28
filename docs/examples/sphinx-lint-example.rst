Sphinx-Lint Example
===================

This page demonstrates **sphinx-lint** in action, showing how it validates Sphinx documentation and catches common errors.

Overview
--------

sphinx-lint is a quality assurance tool that scans your reStructuredText documentation for issues. This example shows typical linting scenarios and their outputs.

Example Documentation Files
----------------------------

Let's examine several documentation files and see what sphinx-lint reports.

Example 1: Clean Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**File:** ``docs/clean-example.rst``

.. code-block:: rst

   Getting Started
   ===============
   
   Welcome to our documentation!
   
   Installation
   ------------
   
   Install the package using pip:
   
   .. code-block:: bash
   
      pip install mypackage
   
   Quick Example
   -------------
   
   Here's a simple example:
   
   .. code-block:: python
   
      import mypackage
      result = mypackage.process_data()
      print(result)
   
   See the :doc:`api/reference` for more details.

**Linting Output:**

.. code-block:: console

   $ sphinx-lint docs/clean-example.rst
   
   ✓ No issues found

Example 2: Common Errors
~~~~~~~~~~~~~~~~~~~~~~~~~

**File:** ``docs/problematic-example.rst``

.. code-block:: rst

   User Guide
   ==========
   
   Introduction
   -----------
   
   This section covers the basics
   
   Configuration
   ~~~~~~~~~~~~~~
   
   Here's the configuration::
   
     {
       "key": "value"
       "missing": "comma"
     }
   
   See :doc:`missing-file` for more.
   
   Code Example
   ------------
   
   .. code-block: python
   
      # Missing double colon above
      print("Hello")

**Linting Output:**

.. code-block:: console

   $ sphinx-lint docs/problematic-example.rst
   
   docs/problematic-example.rst:10: Inconsistent heading level (~~~ after ---)
   docs/problematic-example.rst:19: Unknown directive: "code-block:" (did you mean ".. code-block::"?)
   
   ❌ 2 issues found

Example 3: Broken References
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**File:** ``docs/references-example.rst``

.. code-block:: rst

   API Documentation
   =================
   
   Core Modules
   ------------
   
   See the following pages:
   
   * :doc:`api/core` - Core functionality
   * :doc:`api/utils` - Utility functions
   * :doc:`api/nonexistent` - This link is broken
   * :ref:`undefined-label` - This label doesn't exist
   
   Related Documentation
   ---------------------
   
   Check out :doc:`../tutorials/advanced`.

**Linting Output:**

.. code-block:: console

   $ sphinx-lint docs/references-example.rst
   
   docs/references-example.rst:12: Reference target not found: api/nonexistent
   docs/references-example.rst:13: Reference target not found: undefined-label
   
   ❌ 2 issues found

Example 4: Formatting Issues
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**File:** ``docs/formatting-example.rst``

.. code-block:: rst

   Formatting Guide
   ================
   
   Code Blocks
   -----------
   
   Inline code uses `single backticks` which is wrong.
   
   Should use ``double backticks`` for inline code.
   
   Lists
   -----
   
   * Item 1
   *Item 2 (missing space)
     * Subitem
   * Item 3
   
   Tables
   ------
   
   .. list-table::
      :header-rows: 1
   
      * - Column 1
        - Column 2
      * - Value 1
        - Value 2
      * - Value 3
        (missing cell)

**Linting Output:**

.. code-block:: console

   $ sphinx-lint docs/formatting-example.rst
   
   docs/formatting-example.rst:7: Inline literal should use double backticks (``)
   docs/formatting-example.rst:14: Malformed list item (missing space after bullet)
   docs/formatting-example.rst:28: Inconsistent list-table structure
   
   ❌ 3 issues found

Complete Linting Report
------------------------

Running sphinx-lint on an entire documentation directory:

.. code-block:: console

   $ sphinx-lint docs/
   
   Scanning documentation files...
   
   docs/index.rst: ✓ OK
   docs/installation.rst: ✓ OK
   docs/user-guide/index.rst: ✓ OK
   docs/user-guide/basics.rst:45: Heading underline too short
   docs/user-guide/advanced.rst:12: Reference target not found: nonexistent
   docs/api/reference.rst: ✓ OK
   docs/api/examples.rst:78: Inconsistent code block directive
   docs/tutorials/tutorial-1.rst: ✓ OK
   docs/tutorials/tutorial-2.rst:23: Malformed bullet list
   
   Summary:
   --------
   Files scanned: 9
   Files with issues: 4
   Total issues: 5
   
   ❌ Documentation validation failed

Common Issues and Fixes
-----------------------

Issue: Heading Underline Too Short
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Problem:**

.. code-block:: rst

   Configuration Options
   ============

**Fix:**

.. code-block:: rst

   Configuration Options
   =====================

The underline must be at least as long as the heading text.

Issue: Inline Code Formatting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Problem:**

.. code-block:: rst

   Use the `config` parameter to set options.

**Fix:**

.. code-block:: rst

   Use the ``config`` parameter to set options.

Single backticks are for hyperlinks, double backticks are for inline code.

Issue: Broken Cross-References
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Problem:**

.. code-block:: rst

   See :doc:`missing-page` for details.

**Fix:**

.. code-block:: rst

   See :doc:`existing-page` for details.

Ensure the referenced file exists relative to the current document.

Issue: Malformed Directive
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Problem:**

.. code-block:: rst

   .. code-block python

**Fix:**

.. code-block:: rst

   .. code-block:: python

Directives require a double colon (::) after the name.

Continuous Integration Example
-------------------------------

Using sphinx-lint in a CI/CD pipeline:

**.gitlab-ci.yml:**

.. code-block:: yaml

   lint-docs:
     stage: test
     image: kensai-sphinx:latest
     script:
       - echo "Linting documentation..."
       - sphinx-lint docs/
       - echo "Checking for broken links..."
       - sphinx-lint --check-links docs/
     only:
       - merge_requests
       - main

**GitHub Actions (.github/workflows/docs-lint.yml):**

.. code-block:: yaml

   name: Documentation Linting
   
   on:
     pull_request:
       paths:
         - 'docs/**'
     push:
       branches:
         - main
   
   jobs:
     lint:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Lint Documentation
           run: |
             docker run --rm -v $PWD:/project \
               kensai-sphinx:latest \
               sphinx-lint /project/docs/
         
         - name: Check for Issues
           if: failure()
           run: echo "❌ Documentation has linting errors"

Pre-commit Hook Example
------------------------

Add sphinx-lint to pre-commit configuration:

**.pre-commit-config.yaml:**

.. code-block:: yaml

   repos:
     - repo: local
       hooks:
         - id: sphinx-lint
           name: Sphinx Documentation Linter
           entry: sphinx-lint
           language: system
           files: \.rst$
           types: [text]

**Manual pre-commit script (.git/hooks/pre-commit):**

.. code-block:: bash

   #!/bin/bash
   
   echo "Running sphinx-lint on changed documentation files..."
   
   # Get list of changed .rst files
   CHANGED_FILES=$(git diff --cached --name-only --diff-filter=ACM | grep '\.rst$')
   
   if [ -n "$CHANGED_FILES" ]; then
       echo "Checking files:"
       echo "$CHANGED_FILES"
       
       if ! sphinx-lint $CHANGED_FILES; then
           echo ""
           echo "❌ Documentation linting failed!"
           echo "Please fix the issues above before committing."
           exit 1
       fi
       
       echo "✅ Documentation linting passed!"
   fi
   
   exit 0

Configuration File Example
---------------------------

Create a ``.sphinx-lint.yml`` configuration file:

.. code-block:: yaml

   # Sphinx-lint configuration
   
   # Rules to enable
   enable:
     - heading-level
     - directive-format
     - reference-target
     - code-block-syntax
     - table-formatting
     - list-formatting
   
   # Rules to disable
   disable:
     - line-length  # Allow long lines
   
   # Severity levels
   severity:
     broken-reference: error
     heading-level: warning
     inline-code: warning
   
   # Ignore patterns
   ignore:
     - docs/_build/**
     - docs/_templates/**
     - docs/_static/**
   
   # Maximum line length (if enabled)
   max-line-length: 120
   
   # Output format
   output-format: colorized

Using the configuration:

.. code-block:: console

   $ sphinx-lint -c .sphinx-lint.yml docs/

Example Output Formats
----------------------

Default Output
~~~~~~~~~~~~~~

.. code-block:: console

   $ sphinx-lint docs/
   
   docs/file.rst:10: Heading underline too short
   docs/file.rst:25: Reference target not found: missing-doc
   
   ❌ 2 issues found

JSON Output
~~~~~~~~~~~

.. code-block:: console

   $ sphinx-lint --format=json docs/
   
   {
     "files": [
       {
         "path": "docs/file.rst",
         "issues": [
           {
             "line": 10,
             "severity": "error",
             "code": "heading-underline",
             "message": "Heading underline too short"
           },
           {
             "line": 25,
             "severity": "error",
             "code": "broken-reference",
             "message": "Reference target not found: missing-doc"
           }
         ]
       }
     ],
     "summary": {
       "total_files": 1,
       "files_with_issues": 1,
       "total_issues": 2
     }
   }

Best Practices
--------------

1. **Run Early and Often**
   
   Integrate sphinx-lint into your development workflow:
   
   - Before committing changes
   - During code review
   - In CI/CD pipelines

2. **Fix Issues Incrementally**
   
   Don't wait until you have hundreds of issues:
   
   .. code-block:: bash
   
      # Lint only changed files
      sphinx-lint $(git diff --name-only '*.rst')

3. **Use Configuration Files**
   
   Create team standards with shared configuration:
   
   - Consistent rule enforcement
   - Project-specific ignore patterns
   - Standardized severity levels

4. **Combine with Other Tools**
   
   Use sphinx-lint alongside:
   
   - ``sphinx-build -W`` (treat warnings as errors)
   - Link checkers
   - Spell checkers
   - Style guides

Learn More
----------

For complete documentation on sphinx-lint usage and configuration, see:

- :doc:`../tutorials/packages/sphinx-lint` - Complete tutorial
- `Sphinx-lint GitHub <https://github.com/sphinx-contrib/sphinx-lint>`_
- `Sphinx Documentation Best Practices <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_
