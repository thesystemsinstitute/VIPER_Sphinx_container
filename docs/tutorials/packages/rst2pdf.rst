Rst2Pdf Tutorial
================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/rst2pdf/>`_
   - `API Documentation <../../pdoc/rst2pdf/index.html>`_
   - `Manual <https://rst2pdf.org/>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use rst2pdf in your Sphinx documentation.

What is Rst2Pdf?
----------------
rst2pdf is a Sphinx extension that provides:

- PDF generation from RST
- Easy integration with Sphinx
- Comprehensive configuration options
- Professional documentation output

rst2pdf provides:

- PDF generation from RST
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

rst2pdf is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm viper-sphinx:latest python -c "import rst2pdf; print('Installed')"

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


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'rst2pdf',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

Complete configuration with all features:

.. code-block:: python

   extensions = ['rst2pdf']
   
   # Package-specific configuration
   # Add configuration options here

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


Practical Examples
------------------

Overview
--------


Key Features
~~~~~~~~~~~~

- **Feature 1**: Description of key feature
- **Feature 2**: Description of key feature
- **Feature 3**: Description of key feature
- **Feature 4**: Description of key feature

Installation
------------

Using pip
~~~~~~~~~

Install the extension:

.. code-block:: bash

   pip install rst2pdf

Or add to your ``requirements.txt``:

.. code-block:: text

   rst2pdf
   sphinx>=5.0.0

Configuration
-------------

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'rst2pdf',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

Complete configuration with all features:

.. code-block:: python

   extensions = ['rst2pdf']
   
   # Package-specific configuration
   # Add configuration options here

Basic Usage
-----------

Example 1: Basic Usage
~~~~~~~~~~~~~~~~~~~~~~

Here's a basic example:

.. code-block:: rst

   .. Add example directive here

Example 2: Advanced Usage
~~~~~~~~~~~~~~~~~~~~~~~~~

A more advanced example:

.. code-block:: rst

   .. Add advanced example here

Real-World Examples
-------------------

Example: Practical Application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A practical real-world usage example:

.. code-block:: rst

   .. Add practical example here

Best Practices
--------------

Recommendations
~~~~~~~~~~~~~~~

- Use clear and descriptive content
- Follow documentation standards
- Test your examples
- Keep configuration simple

Common Patterns
~~~~~~~~~~~~~~~

Standard patterns for using rst2pdf:

1. **Pattern 1**: Description
2. **Pattern 2**: Description
3. **Pattern 3**: Description

Integration Tips
----------------

Working with Other Extensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

rst2pdf integrates well with:

- Standard Sphinx extensions
- Other documentation tools
- Custom extensions

Additional Resources
--------------------

- `PyPI Package <https://pypi.org/project/rst2pdf/>`_
- `Official Documentation <https://rst2pdf.org/>`_
- :doc:`Complete Tutorial <../tutorials/packages/rst2pdf>`
- :ref:`Package API Documentation <pdoc-rst2pdf>`
Next Steps
----------
- Explore the :doc:`tutorial <../tutorials/packages/rst2pdf>`
- Check the official documentation
- Try the examples in your own projects
- Customize for your specific needs

