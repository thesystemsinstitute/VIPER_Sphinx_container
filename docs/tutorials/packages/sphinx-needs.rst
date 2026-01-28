Sphinx Needs Tutorial
=====================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-needs/>`_
   - `API Documentation <../../pdoc/sphinx_needs/index.html>`_
   - `Manual <https://sphinx-needs.readthedocs.io/en/latest/>`_
   - :doc:`Working Example <../../examples/sphinx-needs-example>`


.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinx-needs in your Sphinx documentation.

What is Sphinx Needs?
----------------------

sphinx-needs is a Sphinx extension that provides:

- Requirements management extension
- Easy integration with Sphinx
- Comprehensive configuration options
- Professional documentation output

sphinx-needs provides:

- Requirements management extension
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

sphinx-needs is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinx_needs; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``docs/conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_needs',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinx_needs']
   
   # Configuration options
   # Add package-specific configuration here


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_needs',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

Complete configuration with all features:

.. code-block:: python

   extensions = ['sphinx_needs']
   
   # Package-specific configuration
   # Add configuration options here

Basic Usage
-----------

Getting Started
~~~~~~~~~~~~~~~

Here's a basic example of using sphinx-needs:

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

- :doc:`Working Example <../../examples/sphinx-needs-example>`
- `PyPI Package <https://pypi.org/project/sphinx-needs/>`_
- `Official Documentation <https://sphinx-needs.readthedocs.io/>`_
