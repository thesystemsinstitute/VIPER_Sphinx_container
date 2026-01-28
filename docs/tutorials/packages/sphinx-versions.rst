Sphinx Versions Tutorial
========================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-versions/>`_
   - `API Documentation <../../pdoc/sphinx_versions/index.html>`_
   - `Manual <https://github.com/sphinx-contrib/versions>`_
   - :doc:`Working Example <../../examples/sphinx-versions-example>`


.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinx-versions in your Sphinx documentation.

What is Sphinx Versions?
-------------------------

sphinx-versions is a Sphinx extension that provides:

- Version management for Sphinx
- Easy integration with Sphinx
- Comprehensive configuration options
- Professional documentation output

sphinx-versions provides:

- Version management for Sphinx
- Integration with Sphinx documentation
- Flexible configuration options
- Professional output formatting

Key Features
~~~~~~~~~~~~

- **Multi-version Builds**: Build documentation for multiple versions
- **Git Integration**: Automatic version detection from Git
- **Version Banners**: Display version warnings
- **Navigation**: Easy version switching
Installation
------------

sphinx-versions is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinx_versions; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``docs/conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_versions',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinx_versions']
   
   # Configuration options
   sphinx_versions_git_root = '.'
   sphinx_versions_banner_main_ref = 'master'


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

Getting Started
~~~~~~~~~~~~~~~

Build versioned documentation:

.. code-block:: bash

   sphinx-versions build docs docs/_build/html

List Versions
~~~~~~~~~~~~~

List available versions:

.. code-block:: bash

   sphinx-versions list

Common Use Cases
----------------

Build All Versions
~~~~~~~~~~~~~~~~~~

Build documentation for all Git refs:

.. code-block:: bash

   sphinx-versions build -a docs docs/_build/html

Specify Branches
~~~~~~~~~~~~~~~~

Build specific branches/tags:

.. code-block:: bash

   sphinx-versions build -r master -r v1.0 -r v2.0 docs docs/_build/html

Advanced Features
-----------------

Version Banner
~~~~~~~~~~~~~~

Configure version banner:

.. code-block:: python

   # In conf.py
   sphinx_versions_banner_main_ref = 'main'
   sphinx_versions_banner_old_format = 'This is an old version. Latest is {ref}'

Custom Templates
~~~~~~~~~~~~~~~~

Use custom version templates:

.. code-block:: python

   sphinx_versions_template_dir = '_templates'

Best Practices
--------------

Tips and Guidelines
~~~~~~~~~~~~~~~~~~~

- Use semantic versioning
- Keep documentation synchronized with code
- Test version builds regularly
- Maintain version navigation
- Archive old versions appropriately

Troubleshooting
---------------

Common Issues
~~~~~~~~~~~~~

**Issue**: Version not found

**Solution**: Check Git tags and branches are properly created.

**Issue**: Build failures

**Solution**: Ensure all versions have compatible configuration.

Additional Resources
--------------------

- :doc:`Working Example <../../examples/sphinx-versions-example>`
- `PyPI Package <https://pypi.org/project/sphinx-versions/>`_
- `Official Documentation <https://sphinx-versions.readthedocs.io/>`_
