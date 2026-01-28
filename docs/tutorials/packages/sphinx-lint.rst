Sphinx-Lint Tutorial
====================

.. note::
   
   **Package Resources:**
   
   - :doc:`../../examples/sphinx-lint-example` - Live example
   - `PyPI Package <https://pypi.org/project/sphinx-lint/>`_


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

Practical Examples
------------------

Example 1: Linting During Development
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a script ``lint-docs.sh``:

.. code-block:: bash

   #!/bin/bash
   docker run --rm -v $(pwd):/project kensai-sphinx:latest \
       sphinx-lint -r /project/docs/

Run before committing:

.. code-block:: bash

   chmod +x lint-docs.sh
   ./lint-docs.sh

Example 2: Ignoring Build Directories
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm -v $(pwd):/project kensai-sphinx:latest \
       sphinx-lint -r -i "_build" -i "*.pyc" /project/docs/

Example 3: Custom Line Length
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For wider lines (e.g., code samples):

.. code-block:: bash

   docker run --rm -v $(pwd):/project kensai-sphinx:latest \
       sphinx-lint --max-line-length 120 /project/docs/

Example 4: Checking Specific File Types
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Only .rst files
   docker run --rm -v $(pwd):/project kensai-sphinx:latest \
       find /project/docs -name "*.rst" -exec sphinx-lint {} +

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
