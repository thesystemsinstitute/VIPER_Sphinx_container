Sphinx Versions Example
=======================

.. note::

   **Package**: sphinx-versions  
   **Purpose**: Version management for Sphinx  
   **Tutorial**: See :doc:`../tutorials/packages/sphinx-versions` for complete tutorial

This page demonstrates **sphinx-versions** - Version management for Sphinx.

.. contents:: Contents
   :local:
   :depth: 3

Overview
--------


Key Features
~~~~~~~~~~~~

- **Multi-version Builds**: Build documentation for multiple versions
- **Git Integration**: Automatic version detection from Git
- **Version Banners**: Display version warnings
- **Navigation**: Easy version switching

Installation
------------

Using pip
~~~~~~~~~

Install the extension:

.. code-block:: bash

   pip install sphinx-versions

Or add to your ``requirements.txt``:

.. code-block:: text

   sphinx-versions
   sphinx>=5.0.0

Configuration
-------------

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_versions',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

Complete configuration with all features:

.. code-block:: python

   extensions = ['sphinx_versions']
   
   # Package-specific configuration
   sphinx_versions_git_root = '.'
   sphinx_versions_banner_main_ref = 'master'
   sphinx_versions_banner_old_format = 'This is documentation for version {ref}. Latest is <a href="/{main}/">here</a>.'
   sphinx_versions_template_dir = '_templates'

Basic Usage
-----------

Example 1: Build All Versions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Build documentation for all versions:

.. code-block:: bash

   # Build all branches and tags
   sphinx-versions build -a docs docs/_build/html
   
   # List available versions
   sphinx-versions list
   
   # Build specific versions
   sphinx-versions build -r master -r v1.0 docs docs/_build/html

Example 2: CI/CD Integration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GitHub Actions workflow:

.. code-block:: yaml

   name: Build Versioned Docs
   
   on:
     push:
       branches: [main, master]
       tags: ['v*']
   
   jobs:
     docs:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
           with:
             fetch-depth: 0
         
         - uses: actions/setup-python@v4
           with:
             python-version: '3.11'
         
         - name: Install dependencies
           run: pip install sphinx sphinx-versions
         
         - name: Build all versions
           run: sphinx-versions build -a docs docs/_build/html

Real-World Examples
-------------------

Example: Complete Version Management
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Full versioned documentation setup:

.. code-block:: bash

   #!/bin/bash
   # build-versions.sh
   
   # Build all versions
   sphinx-versions build -a \
       --git-root . \
       --override-branch master \
       docs docs/_build/html
   
   # Or build specific versions
   sphinx-versions build \
       -r master \
       -r v1.0.0 \
       -r v2.0.0 \
       docs docs/_build/html

Example: Version Banner Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure version warnings:

.. code-block:: python

   # In conf.py
   sphinx_versions_banner_main_ref = 'master'
   
   # Custom banner for old versions
   sphinx_versions_banner_old_format = '''
   <div class="version-warning">
       ⚠️ You are viewing documentation for {ref}.
       <a href="/{main}/">View latest version</a>
   </div>
   '''
   
   # Custom banner for development versions
   sphinx_versions_banner_dev_format = '''
   <div class="dev-warning">
       🚧 This is development documentation for {ref}.
       It may be incomplete or unstable.
   </div>
   '''

Example: Makefile Integration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add to ``Makefile``:

.. code-block:: makefile

   .PHONY: multiversion
   multiversion:
   	sphinx-versions build -a $(SOURCEDIR) $(BUILDDIR)/html
   
   .PHONY: versions
   versions:
   	sphinx-versions list
   
   .PHONY: version-latest
   version-latest:
   	sphinx-versions build -r master $(SOURCEDIR) $(BUILDDIR)/html

Best Practices
--------------

Recommendations
~~~~~~~~~~~~~~~

- Use semantic versioning for tags
- Keep main branch documentation up-to-date
- Add version banners for clarity
- Test all version builds
- Archive outdated versions appropriately

Common Patterns
~~~~~~~~~~~~~~~

Standard patterns for using sphinx-versions:

1. **Latest + Tagged**: Build latest dev + release versions
2. **Version Dropdown**: Add version selector to theme
3. **Banner Warnings**: Display warnings for old versions

Integration Tips
----------------

Working with Other Extensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

sphinx-versions integrates well with:

- sphinx-multiversion for alternative approach
- sphinx-polyversion for version management
- Standard Git workflows

Additional Resources
--------------------

- :doc:`Complete Tutorial <../tutorials/packages/sphinx-versions>`
- `PyPI Package <https://pypi.org/project/sphinx-versions/>`_
- `Official Documentation <https://sphinx-versions.readthedocs.io/>`_
- :ref:`Package API Documentation <pdoc-sphinx-versions>`

Next Steps
----------

- Explore the :doc:`tutorial <../tutorials/packages/sphinx-versions>`
- Check the official documentation
- Try the examples in your own projects
- Customize for your specific needs
