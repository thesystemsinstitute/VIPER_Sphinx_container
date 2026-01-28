Sphinx Sql Tutorial
====================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-sql/>`_
   - :doc:`See Working Example <../../examples/sphinx-sql-example>`
   - `Official Documentation <https://sphinx-sql.readthedocs.io/>`_

This tutorial demonstrates how to use sphinx-sql in your Sphinx documentation.

What is Sphinx Sql?
-------------------

sphinx-sql is a Sphinx extension that provides:

- Document SQL in Sphinx
- Easy integration with Sphinx
- Comprehensive configuration options
- Professional documentation output

Installation
------------

sphinx-sql is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinx_sql; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``docs/conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_sql',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinx_sql']
   
   # Configuration options
   # Add package-specific configuration here

Basic Usage
-----------

Getting Started
~~~~~~~~~~~~~~~

Here's a basic example of using sphinx-sql:

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

- :doc:`Working Example <../../examples/sphinx-sql-example>`
- `PyPI Package <https://pypi.org/project/sphinx-sql/>`_
- `Official Documentation <https://sphinx-sql.readthedocs.io/>`_
