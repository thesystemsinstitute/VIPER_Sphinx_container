Sphinx-Lint Tutorial
====================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-lint/>`_
   - `API Documentation <../../pdoc/sphinx_lint/index.html>`_
   - `Manual <https://github.com/sphinx-contrib/sphinx-lint>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinx-lint to check and validate your Sphinx documentation for common issues and best practices.

What is Sphinx-Lint?
--------------------
sphinx-lint is a linting tool for Sphinx documentation that helps you:

- Find errors in reStructuredText syntax
- Detect broken internal references
- Identify formatting inconsistencies
- Catch common documentation mistakes
- Enforce documentation quality standards
- Maintain consistent style across your docs

Think of it as a spell-checker and style guide enforcer for your documentation.

sphinx-lint is a quality assurance tool that scans your reStructuredText documentation for issues. This example shows typical linting scenarios and their outputs.


Installation
------------

sphinx-lint is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest sphinx-lint --version

Basic Usage
-----------

Linting a Single File
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm -v $(pwd):/project kensai-sphinx:latest \
       sphinx-lint /project/docs/index.rst

Linting Multiple Files
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm -v $(pwd):/project kensai-sphinx:latest \
       sphinx-lint /project/docs/*.rst

Linting a Directory
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm -v $(pwd):/project kensai-sphinx:latest \
       sphinx-lint /project/docs/

Recursive Linting
~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm -v $(pwd):/project kensai-sphinx:latest \
       sphinx-lint -r /project/docs/

Command-Line Options
--------------------

Available Options
~~~~~~~~~~~~~~~~~

.. code-block:: bash

   sphinx-lint [OPTIONS] [FILES/DIRECTORIES...]

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Option
     - Description
   * - ``-h, --help``
     - Show help message
   * - ``-v, --version``
     - Show version
   * - ``-r, --recursive``
     - Recursively check subdirectories
   * - ``-i, --ignore PATTERN``
     - Ignore files/directories matching pattern
   * - ``--max-line-length N``
     - Maximum line length (default: 80)
   * - ``--enable CHECKS``
     - Enable specific checks
   * - ``--disable CHECKS``
     - Disable specific checks
   * - ``--list-checks``
     - List all available checks

Common Checks
-------------

sphinx-lint performs various checks on your documentation:

Syntax Errors
~~~~~~~~~~~~~

Detects invalid reStructuredText syntax:

**Example Error:**

.. code-block:: rst

   # This is wrong - reST uses = or - for headers
   My Header
   
**Correct:**

.. code-block:: rst

   My Header
   =========

Heading Hierarchy
~~~~~~~~~~~~~~~~~

Ensures proper heading structure:

**Wrong:**

.. code-block:: rst

   Main Title
   ==========
   
   Sub-sub-section  # Skipped level!
   ~~~~~~~~~~~~~~~~

**Correct:**

.. code-block:: rst

   Main Title
   ==========
   
   Section
   -------
   
   Sub-section
   ~~~~~~~~~~~

Indentation
~~~~~~~~~~~

Checks consistent indentation:

**Wrong:**

.. code-block:: rst

   .. code-block:: python
   
     def foo():  # Inconsistent indent
         pass

**Correct:**

.. code-block:: rst

   .. code-block:: python
   
      def foo():
          pass

Line Length
~~~~~~~~~~~

Warns about lines exceeding maximum length:

.. code-block:: bash

   sphinx-lint --max-line-length 100 docs/

Trailing Whitespace
~~~~~~~~~~~~~~~~~~~

Detects unnecessary trailing spaces:

.. code-block:: rst

   This line has trailing spaces    # Bad
   This line is clean# Good

Directive Issues
~~~~~~~~~~~~~~~~

Identifies malformed directives:

**Wrong:**

.. code-block:: rst

   .. note::
   Missing content!

**Correct:**

.. code-block:: rst

   .. note::
      
      Proper content with indentation

Integration with Development Workflow
--------------------------------------

Pre-commit Hook
~~~~~~~~~~~~~~~

Create ``.git/hooks/pre-commit``:

.. code-block:: bash

   #!/bin/bash
   
   echo "Running sphinx-lint..."
   
   # Get changed .rst files
   CHANGED_DOCS=$(git diff --cached --name-only --diff-filter=ACM | grep '\.rst$')
   
   if [ -n "$CHANGED_DOCS" ]; then
       docker run --rm -v $(pwd):/project kensai-sphinx:latest \
           sphinx-lint $CHANGED_DOCS
       
       if [ $? -ne 0 ]; then
           echo "sphinx-lint failed. Please fix the issues before committing."
           exit 1
       fi
   fi

Make it executable:

.. code-block:: bash

   chmod +x .git/hooks/pre-commit

Docker Compose Setup
~~~~~~~~~~~~~~~~~~~~

Create ``docker-compose.yml``:

.. code-block:: yaml

   version: '3.8'
   
   services:
     lint:
       image: kensai-sphinx:latest
       volumes:
         - ./:/project
       working_dir: /project
       command: sphinx-lint -r docs/

Run:

.. code-block:: bash

   docker-compose run --rm lint

Makefile Integration
~~~~~~~~~~~~~~~~~~~~

Add to your ``Makefile``:

.. code-block:: makefile

   .PHONY: lint
   lint:
   	docker run --rm -v $(PWD):/project kensai-sphinx:latest \
   		sphinx-lint -r docs/
   
   .PHONY: lint-strict
   lint-strict:
   	docker run --rm -v $(PWD):/project kensai-sphinx:latest \
   		sphinx-lint --max-line-length 80 -r docs/

Usage:

.. code-block:: bash

   make lint

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

Create ``.github/workflows/lint.yml``:

.. code-block:: yaml

   name: Lint Documentation
   
   on:
     push:
       paths:
         - 'docs/**'
     pull_request:
       paths:
         - 'docs/**'
   
   jobs:
     lint:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Lint Documentation
           run: |
             docker run --rm -v $(pwd):/project kensai-sphinx:latest \
               sphinx-lint -r docs/

GitLab CI
~~~~~~~~~

Add to ``.gitlab-ci.yml``:

.. code-block:: yaml

   lint-docs:
     image: kensai-sphinx:latest
     script:
       - sphinx-lint -r docs/
     only:
       changes:
         - docs/**/*.rst

Jenkins Pipeline
~~~~~~~~~~~~~~~~

.. code-block:: groovy

   pipeline {
       agent any
       stages {
           stage('Lint Documentation') {
               steps {
                   sh '''
                       docker run --rm -v $(pwd):/project kensai-sphinx:latest \
                           sphinx-lint -r docs/
                   '''
               }
           }
       }
   }

Common Issues and Solutions
---------------------------

Issue: "Invalid Directive"
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Error:**

.. code-block:: text

   WARNING: Unknown directive type "note"

**Solution:**

Check directive spelling and indentation:

.. code-block:: rst

   .. note::
      
      Content must be indented

Issue: "Inconsistent Title Underline"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Error:**

.. code-block:: text

   Title underline too short

**Solution:**

Ensure underline matches title length:

.. code-block:: rst

   # Wrong
   My Title
   ===
   
   # Correct
   My Title
   ========

Issue: "Duplicate Label"
~~~~~~~~~~~~~~~~~~~~~~~~~

**Error:**

.. code-block:: text

   Duplicate explicit target name

**Solution:**

Use unique labels for references:

.. code-block:: rst

   # Wrong
   .. _section:
   
   First Section
   
   .. _section:  # Duplicate!
   
   Second Section
   
   # Correct
   .. _first-section:
   
   First Section
   
   .. _second-section:
   
   Second Section

Best Practices
--------------

1. **Run Regularly**
   
   Lint your docs frequently during development:
   
   .. code-block:: bash
   
      # Quick check
      docker run --rm -v $(pwd):/project kensai-sphinx:latest \
          sphinx-lint docs/index.rst

2. **Fix Issues Incrementally**
   
   Don't let lint errors accumulate:
   
   - Fix errors as you write
   - Review lint output before commits
   - Set up pre-commit hooks

3. **Configure Line Length**
   
   Choose a reasonable limit based on your needs:
   
   .. code-block:: bash
   
      # For code-heavy docs
      sphinx-lint --max-line-length 120 docs/

4. **Ignore Generated Files**
   
   Don't lint auto-generated content:
   
   .. code-block:: bash
   
      sphinx-lint -r -i "_build" -i "api/" docs/

5. **Integrate with CI/CD**
   
   Automate linting in your pipeline to catch issues early

6. **Document Exceptions**
   
   If you must ignore a warning, document why:
   
   .. code-block:: rst
   
      .. This line intentionally exceeds 80 chars for URL readability
      See https://very-long-domain-name.example.com/path/to/documentation

Configuration File
------------------

Create ``.sphinx-lint.yml`` for project-wide settings:

.. code-block:: yaml

   # sphinx-lint configuration
   max-line-length: 100
   
   ignore:
     - _build
     - .tox
     - "*.pyc"
   
   enable:
     - trailing-whitespace
     - line-too-long
   
   disable:
     - heading-style  # If you want to disable specific checks

Then run:

.. code-block:: bash

   docker run --rm -v $(pwd):/project kensai-sphinx:latest \
       sphinx-lint docs/

Combining with Other Tools
---------------------------

With Sphinx Build
~~~~~~~~~~~~~~~~~

Check syntax before building:

.. code-block:: bash

   # Lint first
   docker run --rm -v $(pwd):/project kensai-sphinx:latest \
       sphinx-lint -r docs/
   
   # Then build
   docker run --rm -v $(pwd):/project kensai-sphinx:latest \
       sphinx-build -b html docs/ docs/_build/html

With Doc8
~~~~~~~~~

Use both linters for comprehensive checking:

.. code-block:: bash

   # sphinx-lint for Sphinx-specific issues
   docker run --rm -v $(pwd):/project kensai-sphinx:latest \
       sphinx-lint docs/
   
   # doc8 for general reST style
   docker run --rm -v $(pwd):/project kensai-sphinx:latest \
       doc8 docs/

Complete Workflow Script
-------------------------

Create ``check-docs.sh``:

.. code-block:: bash

   #!/bin/bash
   set -e
   
   echo "=== Linting Documentation ==="
   docker run --rm -v $(pwd):/project kensai-sphinx:latest \
       sphinx-lint -r docs/
   
   echo -e "\n=== Building Documentation ==="
   docker run --rm -v $(pwd):/project kensai-sphinx:latest \
       sphinx-build -W -b html docs/ docs/_build/html
   
   echo -e "\n=== Checking Links ==="
   docker run --rm -v $(pwd):/project kensai-sphinx:latest \
       sphinx-build -b linkcheck docs/ docs/_build/linkcheck
   
   echo -e "\n✅ All checks passed!"

Make executable and run:

.. code-block:: bash

   chmod +x check-docs.sh
   ./check-docs.sh

Troubleshooting
---------------

No Output or Errors
~~~~~~~~~~~~~~~~~~~

If sphinx-lint produces no output:

- Check file paths are correct
- Ensure files have ``.rst`` extension
- Verify files contain actual content

Too Many Warnings
~~~~~~~~~~~~~~~~~

If overwhelmed with warnings:

1. Start with critical errors
2. Use ``--disable`` to focus on specific issues
3. Fix issues incrementally
4. Configure ``.sphinx-lint.yml`` with your standards

False Positives
~~~~~~~~~~~~~~~

If you get incorrect warnings:

- Check your reST syntax is actually correct
- Consider if the warning is valid (often it is!)
- Document why you're ignoring if truly a false positive

Performance Issues
~~~~~~~~~~~~~~~~~~

For large documentation sets:

- Lint only changed files during development
- Use full lint in CI/CD
- Exclude generated/vendor directories


Practical Examples
------------------

This page demonstrates **sphinx-lint** in action, showing how it validates Sphinx documentation and catches common errors.


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

Additional Resources
--------------------

- `Sphinx Documentation <https://www.sphinx-doc.org/>`_
- `reStructuredText Primer <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_
- `Sphinx Style Guide <https://documentation-style-guide-sphinx.readthedocs.io/>`_
- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- :doc:`../extensions` - Other useful extensions

Quick Reference
---------------

Common Commands
~~~~~~~~~~~~~~~

.. code-block:: bash

   # Lint single file
   sphinx-lint index.rst
   
   # Lint directory
   sphinx-lint docs/
   
   # Recursive
   sphinx-lint -r docs/
   
   # Custom line length
   sphinx-lint --max-line-length 120 docs/
   
   # Ignore patterns
   sphinx-lint -i "_build" -i "*.tmp" docs/
   
   # List available checks
   sphinx-lint --list-checks
   
   # Version
   sphinx-lint --version

Next Steps
----------

1. Run sphinx-lint on your documentation
2. Fix any critical syntax errors
3. Set up pre-commit hooks
4. Integrate into your CI/CD pipeline
5. Establish documentation quality standards for your team
