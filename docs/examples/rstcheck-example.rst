Rstcheck Example
================

.. note::

   **Package**: rstcheck  
   **Purpose**: Checks syntax of reStructuredText  
   **Tutorial**: See :doc:`../tutorials/packages/rstcheck` for complete tutorial

This page demonstrates **rstcheck** - Checks syntax of reStructuredText.

.. contents:: Contents
   :local:
   :depth: 3

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

- :doc:`Complete Tutorial <../tutorials/packages/rstcheck>`
- `PyPI Package <https://pypi.org/project/rstcheck/>`_
- `Official Documentation <https://rstcheck.readthedocs.io/>`_
- :ref:`Package API Documentation <pdoc-rstcheck>`

Next Steps
----------

- Explore the :doc:`tutorial <../tutorials/packages/rstcheck>`
- Check the official documentation
- Try the examples in your own projects
- Customize for your specific needs
