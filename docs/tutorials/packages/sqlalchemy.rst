Sqlalchemy Tutorial
===================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sqlalchemy/>`_
   - `API Documentation <../../pdoc/sqlalchemy/index.html>`_
   - `Manual <https://www.sqlalchemy.org/>`_
   - :doc:`Working Example <../../examples/sqlalchemy-example>`


.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sqlalchemy in your Sphinx documentation.

What is Sqlalchemy?
-------------------

sqlalchemy is a Sphinx extension that provides:

- SQL toolkit and ORM
- Easy integration with Sphinx
- Comprehensive configuration options
- Professional documentation output

sqlalchemy provides:

- SQL toolkit and ORM
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

sqlalchemy is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sqlalchemy; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``docs/conf.py``:

.. code-block:: python

   extensions = [
       'sqlalchemy',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sqlalchemy']
   
   # Configuration options
   # Add package-specific configuration here


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sqlalchemy',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

Complete configuration with all features:

.. code-block:: python

   extensions = ['sqlalchemy']
   
   # Package-specific configuration
   # Add configuration options here

Basic Usage
-----------

Getting Started
~~~~~~~~~~~~~~~

Here's a basic example of using sqlalchemy:

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

- :doc:`Working Example <../../examples/sqlalchemy-example>`
- `PyPI Package <https://pypi.org/project/sqlalchemy/>`_
- `Official Documentation <https://www.sqlalchemy.org/>`_
