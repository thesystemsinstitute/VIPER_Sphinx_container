Sphinxcontrib Restbuilder Tutorial
===================================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinxcontrib-restbuilder/>`_
   - :doc:`See Working Example <../../examples/sphinxcontrib-restbuilder-example>`
   - `Official Documentation <https://sphinxcontrib-restbuilder.readthedocs.io/>`_

This tutorial demonstrates how to use sphinxcontrib-restbuilder in your Sphinx documentation.

What is Sphinxcontrib Restbuilder?
-----------------------------------

sphinxcontrib-restbuilder is a Sphinx extension that provides:

- REST builder for Sphinx
- Easy integration with Sphinx
- Comprehensive configuration options
- Professional documentation output

Installation
------------

sphinxcontrib-restbuilder is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinxcontrib.restbuilder; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``docs/conf.py``:

.. code-block:: python

   extensions = [
       'sphinxcontrib.restbuilder',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinxcontrib.restbuilder']
   
   # Configuration options
   # Add package-specific configuration here

Basic Usage
-----------

Getting Started
~~~~~~~~~~~~~~~

Here's a basic example of using sphinxcontrib-restbuilder:

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

- :doc:`Working Example <../../examples/sphinxcontrib-restbuilder-example>`
- `PyPI Package <https://pypi.org/project/sphinxcontrib-restbuilder/>`_
- `Official Documentation <https://sphinxcontrib-restbuilder.readthedocs.io/>`_
