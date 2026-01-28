Sphinx Jsonapi Tutorial
========================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-jsonapi/>`_
   - :doc:`See Working Example <../../examples/sphinx-jsonapi-example>`

This tutorial demonstrates how to use sphinx-jsonapi in your Sphinx documentation.

What is Sphinx Jsonapi?
-----------------------

sphinx-jsonapi is a Sphinx extension that provides:

- JSON API documentation support
- Easy integration with Sphinx
- Comprehensive configuration options
- Professional documentation output

sphinx-jsonapi provides:

- JSON API documentation support
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

sphinx-jsonapi is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinx_jsonapi; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``docs/conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_jsonapi',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinx_jsonapi']
   
   # Configuration options
   # Add package-specific configuration here


Complete configuration with all features:

.. code-block:: python

   extensions = ['sphinx_jsonapi']
   
   # Package-specific configuration
   # Add configuration options here

Basic Usage
-----------

Getting Started
~~~~~~~~~~~~~~~

Here's a basic example of using sphinx-jsonapi:

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

- :doc:`Working Example <../../examples/sphinx-jsonapi-example>`
- `PyPI Package <https://pypi.org/project/sphinx-jsonapi/>`_
