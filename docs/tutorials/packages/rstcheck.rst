Rstcheck Tutorial
=================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/rstcheck/>`_
   - `API Documentation <../../pdoc/rstcheck/index.html>`_
   - `Manual <https://github.com/rstcheck/rstcheck>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use rstcheck in your Sphinx documentation.

What is Rstcheck?
-----------------
rstcheck is a Sphinx extension that provides:

- Checks syntax of reStructuredText
- Easy integration with Sphinx
- Comprehensive configuration options
- Professional documentation output

rstcheck provides:

- Checks syntax of reStructuredText
- Integration with Sphinx documentation
- Flexible configuration options
- Professional output formatting

Key Features
~~~~~~~~~~~~

- **Syntax Checking**: Validates RST syntax
- **Code Block Validation**: Checks code blocks in RST files
- **CI/CD Integration**: Easy integration with build pipelines
- **Custom Filters**: Ignore specific directives and roles


Installation
------------

rstcheck is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm viper-sphinx:latest python -c "import rstcheck; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``docs/conf.py``:

.. code-block:: python

   extensions = [
       'rstcheck',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['rstcheck']
   
   # Configuration options
   rstcheck_ignore_messages = []
   rstcheck_ignore_directives = []
   rstcheck_ignore_roles = []


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'rstcheck',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

Complete configuration with all features:

.. code-block:: python

   extensions = ['rstcheck']
   
   # Package-specific configuration
   rstcheck_ignore_messages = [
       r'.*Duplicate implicit target name.*',
   ]
   
   rstcheck_ignore_directives = [
       'automodule',
       'autoclass',
       'testcode',
       'testoutput',
   ]
   
   rstcheck_ignore_roles = [
       'py:class',
       'py:func',
   ]
   
   rstcheck_report_level = 'warning'

Basic Usage
-----------

Getting Started
~~~~~~~~~~~~~~~

Run rstcheck from command line:

.. code-block:: bash

   rstcheck docs/**/*.rst

Check Specific Files
~~~~~~~~~~~~~~~~~~~~

Check individual RST files:

.. code-block:: bash

   rstcheck docs/index.rst

Common Use Cases
----------------

CI/CD Integration
~~~~~~~~~~~~~~~~~

Add to your CI pipeline:

.. code-block:: yaml

   # .github/workflows/docs.yml
   - name: Check RST syntax
     run: rstcheck -r docs/

Pre-commit Hook
~~~~~~~~~~~~~~~

Add to ``.pre-commit-config.yaml``:

.. code-block:: yaml

   repos:
     - repo: https://github.com/rstcheck/rstcheck
       rev: v6.1.0
       hooks:
         - id: rstcheck
           args: [--report-level=warning]

Advanced Features
-----------------

Ignore Specific Issues
~~~~~~~~~~~~~~~~~~~~~~

Configure what to ignore:

.. code-block:: python

   # In conf.py
   rstcheck_ignore_directives = [
       'automodule',
       'testcode',
   ]
   rstcheck_ignore_roles = [
       'py:class',
   ]

Code Block Validation
~~~~~~~~~~~~~~~~~~~~~

Validate code blocks:

.. code-block:: bash

   rstcheck --report-level=warning docs/*.rst

Best Practices
--------------

Tips and Guidelines
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Run rstcheck before committing
- Integrate with CI/CD pipeline
- Fix warnings early
- Use appropriate ignore rules
- Keep RST syntax clean and valid

Troubleshooting
---------------

Common Issues
~~~~~~~~~~~~~

**Issue**: False positives

**Solution**: Use ignore directives and roles to filter known issues.

**Issue**: Custom directives not recognized

**Solution**: Add them to rstcheck_ignore_directives.


Practical Examples
------------------

Overview
--------


Key Features
~~~~~~~~~~~~

- **Syntax Checking**: Validates RST syntax
- **Code Block Validation**: Checks code blocks in RST files
- **CI/CD Integration**: Easy integration with build pipelines
- **Custom Filters**: Ignore specific directives and roles

Installation
------------

Using pip
~~~~~~~~~

Install the extension:

.. code-block:: bash

   pip install rstcheck

Or add to your ``requirements.txt``:

.. code-block:: text

   rstcheck
   sphinx>=5.0.0

Configuration
-------------

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'rstcheck',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

Complete configuration with all features:

.. code-block:: python

   extensions = ['rstcheck']
   
   # Package-specific configuration
   rstcheck_ignore_messages = [
       r'.*Duplicate implicit target name.*',
   ]
   
   rstcheck_ignore_directives = [
       'automodule',
       'autoclass',
       'testcode',
       'testoutput',
   ]
   
   rstcheck_ignore_roles = [
       'py:class',
       'py:func',
   ]
   
   rstcheck_report_level = 'warning'

Basic Usage
-----------

Example 1: Command Line
~~~~~~~~~~~~~~~~~~~~~~~

Check all RST files:

.. code-block:: bash

   # Check all files recursively
   rstcheck -r docs/
   
   # Check specific file
   rstcheck docs/index.rst
   
   # Report warnings and errors
   rstcheck --report-level=warning docs/**/*.rst

Example 2: Configuration File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create ``.rstcheck.cfg``:

.. code-block:: ini

   [rstcheck]
   report_level = warning
   ignore_directives = automodule,autoclass
   ignore_roles = py:class,py:func
   ignore_messages = (Duplicate implicit target name)|(Unknown directive type)

Real-World Examples
-------------------

Example: CI/CD Integration
~~~~~~~~~~~~~~~~~~~~~~~~~~

GitHub Actions workflow:

.. code-block:: yaml

   name: Documentation Check
   
   on: [push, pull_request]
   
   jobs:
     rstcheck:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Set up Python
           uses: actions/setup-python@v4
           with:
             python-version: '3.11'
         
         - name: Install dependencies
           run: |
             pip install rstcheck sphinx
         
         - name: Check RST syntax
           run: |
             rstcheck -r docs/ --report-level=warning

Example: Pre-commit Hook
~~~~~~~~~~~~~~~~~~~~~~~~

Add to ``.pre-commit-config.yaml``:

.. code-block:: yaml

   repos:
     - repo: https://github.com/rstcheck/rstcheck
       rev: v6.1.0
       hooks:
         - id: rstcheck
           args: [--report-level=warning]
           files: \.(rst|txt)$
           additional_dependencies:
             - sphinx>=5.0.0

Example: Makefile Integration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add to your ``Makefile``:

.. code-block:: makefile

   .PHONY: check-rst
   check-rst:
   	rstcheck -r docs/ --report-level=warning
   
   .PHONY: check-rst-strict
   check-rst-strict:
   	rstcheck -r docs/ --report-level=info

Best Practices
--------------

Recommendations
~~~~~~~~~~~~~~~

- Run rstcheck before committing changes
- Integrate with CI/CD pipelines
- Fix all errors and warnings
- Use configuration files for team consistency
- Keep ignore lists minimal

Common Patterns
~~~~~~~~~~~~~~~

Standard patterns for using rstcheck:

1. **Local Development**: Run rstcheck before committing
2. **CI/CD**: Validate all RST files in pipeline
3. **Pre-commit**: Prevent invalid RST from being committed

Integration Tips
----------------

Working with Other Extensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

rstcheck integrates well with:

- doc8 for additional style checking
- sphinx-build for build validation
- pre-commit for automated checking

Additional Resources
--------------------

- `PyPI Package <https://pypi.org/project/rstcheck/>`_
- `Official Documentation <https://rstcheck.readthedocs.io/>`_
- :doc:`Complete Tutorial <../tutorials/packages/rstcheck>`
- :ref:`Package API Documentation <pdoc-rstcheck>`
Next Steps
----------
- Explore the :doc:`tutorial <../tutorials/packages/rstcheck>`
- Check the official documentation
- Try the examples in your own projects
- Customize for your specific needs

