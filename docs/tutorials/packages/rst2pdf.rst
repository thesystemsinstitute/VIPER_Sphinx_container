Rst2Pdf Tutorial
================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/rst2pdf/>`_
   - :doc:`See Working Example <../../examples/rst2pdf-example>`
   - `Official Documentation <https://rst2pdf.org/>`_


This tutorial demonstrates how to use rst2pdf in your Sphinx documentation.

What is Rst2Pdf?
----------------

rst2pdf is a Sphinx extension that provides:

- PDF generation from RST
- Easy integration with Sphinx
- Comprehensive configuration options
- Professional documentation output

Installation
------------

rst2pdf is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import rst2pdf; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``docs/conf.py``:

.. code-block:: python

   extensions = [
       'rst2pdf',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['rst2pdf']
   
   # Configuration options
   # Add package-specific configuration here

Basic Usage
-----------

Getting Started
~~~~~~~~~~~~~~~

Here's a basic example of using rst2pdf:

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

- :doc:`Working Example <../../examples/rst2pdf-example>`
- `PyPI Package <https://pypi.org/project/rst2pdf/>`_
- `Official Documentation <https://rst2pdf.org/>`_
