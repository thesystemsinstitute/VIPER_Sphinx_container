Eralchemy2 Tutorial
===================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/eralchemy2/>`_
   - :doc:`See Working Example <../../examples/eralchemy2-example>`
   - `Official Documentation <https://github.com/maurerle/eralchemy2>`_


This tutorial demonstrates how to use eralchemy2 in your Sphinx documentation.

What is Eralchemy2?
-------------------

eralchemy2 is a Sphinx extension that provides:

- Entity Relationship diagrams from databases
- Easy integration with Sphinx
- Comprehensive configuration options
- Professional documentation output

Installation
------------

eralchemy2 is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import eralchemy2; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``docs/conf.py``:

.. code-block:: python

   extensions = [
       'eralchemy2',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['eralchemy2']
   
   # Configuration options
   # Add package-specific configuration here

Basic Usage
-----------

Getting Started
~~~~~~~~~~~~~~~

Here's a basic example of using eralchemy2:

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

- :doc:`Working Example <../../examples/eralchemy2-example>`
- `PyPI Package <https://pypi.org/project/eralchemy2/>`_
- `Official Documentation <https://github.com/maurerle/eralchemy2>`_
