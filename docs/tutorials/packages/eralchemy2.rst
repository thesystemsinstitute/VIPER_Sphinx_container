Eralchemy2 Tutorial
===================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/eralchemy2/>`_
   - `API Documentation <../../pdoc/eralchemy2/index.html>`_
   - `Manual <https://github.com/maurerle/eralchemy2>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use eralchemy2 in your Sphinx documentation.

What is Eralchemy2?
-------------------
eralchemy2 is a Sphinx extension that provides:

- Entity Relationship diagrams from databases
- Easy integration with Sphinx
- Comprehensive configuration options
- Professional documentation output

eralchemy2 provides:

- Entity Relationship diagrams from databases
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


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'eralchemy2',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

Complete configuration with all features:

.. code-block:: python

   extensions = ['eralchemy2']
   
   # Package-specific configuration
   # Add configuration options here

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

   pip install eralchemy2

Or add to your ``requirements.txt``:

.. code-block:: text

   eralchemy2
   sphinx>=5.0.0

Configuration
-------------

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'eralchemy2',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

Complete configuration with all features:

.. code-block:: python

   extensions = ['eralchemy2']
   
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

Standard patterns for using eralchemy2:

1. **Pattern 1**: Description
2. **Pattern 2**: Description
3. **Pattern 3**: Description

Integration Tips
----------------

Working with Other Extensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

eralchemy2 integrates well with:

- Standard Sphinx extensions
- Other documentation tools
- Custom extensions

Additional Resources
--------------------

- `PyPI Package <https://pypi.org/project/eralchemy2/>`_
- `Official Documentation <https://github.com/maurerle/eralchemy2>`_
- :doc:`Complete Tutorial <../tutorials/packages/eralchemy2>`
- :ref:`Package API Documentation <pdoc-eralchemy2>`
Next Steps
----------
- Explore the :doc:`tutorial <../tutorials/packages/eralchemy2>`
- Check the official documentation
- Try the examples in your own projects
- Customize for your specific needs

