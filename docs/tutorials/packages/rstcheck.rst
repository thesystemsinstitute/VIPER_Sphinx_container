Rstcheck Tutorial
=================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/rstcheck/>`_
   - `API Documentation <../../pdoc/rstcheck/index.html>`_
   - `Manual <https://github.com/rstcheck/rstcheck>`_
   - :doc:`Working Example <../../examples/rstcheck-example>`


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

   docker run --rm kensai-sphinx:latest python -c "import rstcheck; print('Installed')"

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

Additional Resources
--------------------

- :doc:`Working Example <../../examples/rstcheck-example>`
- `PyPI Package <https://pypi.org/project/rstcheck/>`_
- `Official Documentation <https://rstcheck.readthedocs.io/>`_
