Sphinx Sitemap Tutorial
=======================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-sitemap/>`_
   - `API Documentation <../../pdoc/sphinx_sitemap/index.html>`_
   - `Manual <https://sphinx-sitemap.readthedocs.io/>`_
   - :doc:`Working Example <../../examples/sphinx-sitemap-example>`


.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinx-sitemap in your Sphinx documentation.

What is Sphinx Sitemap?
-----------------------

sphinx-sitemap is a Sphinx extension that provides:

- Generate sitemap for docs
- Easy integration with Sphinx
- Comprehensive configuration options
- Professional documentation output

sphinx-sitemap provides:

- Generate sitemap for docs
- Integration with Sphinx documentation
- Flexible configuration options
- Professional output formatting

Key Features
~~~~~~~~~~~~

- **Feature 1**: Description of key feature
- **Feature 2**: Description of key feature
- **Feature 3**: Description of key feature
- **Feature 4**: Description of key feature
Installation
------------

sphinx-sitemap is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinx_sitemap; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``docs/conf.py``:

.. code-block:: python

   extensions = [
       'sphinx-sitemap',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinx-sitemap']
   
   # Configuration options
   # Add package-specific configuration here


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx-sitemap',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

Complete configuration with all features:

.. code-block:: python

   extensions = ['sphinx-sitemap']
   
   # Package-specific configuration
   # Add configuration options here

Basic Usage
-----------

Getting Started
~~~~~~~~~~~~~~~

Here's a basic example of using sphinx-sitemap:

.. code-block:: rst

   .. Add directive examples here

Common Use Cases
----------------

Use Case 1
~~~~~~~~~~

Description of a common use case.

.. code-block:: rst

   .. Example code here

Use Case 2
~~~~~~~~~~

Description of another use case.

.. code-block:: rst

   .. Example code here

Advanced Features
-----------------

Feature 1
~~~~~~~~~

Description of an advanced feature.

.. code-block:: rst

   .. Example code here

Best Practices
--------------

Tips and Guidelines
~~~~~~~~~~~~~~~~~~~

- Follow documentation best practices
- Keep examples clear and concise
- Test your documentation builds
- Use appropriate configuration options

Troubleshooting
---------------

Common Issues
~~~~~~~~~~~~~

**Issue**: Build fails

**Solution**: Check your configuration and syntax.

**Issue**: Output not as expected

**Solution**: Review the package documentation for proper usage.

Additional Resources
--------------------

- :doc:`Working Example <../../examples/sphinx-sitemap-example>`
- `PyPI Package <https://pypi.org/project/sphinx-sitemap/>`_
- `Official Documentation <https://sphinx-sitemap.readthedocs.io/>`_
