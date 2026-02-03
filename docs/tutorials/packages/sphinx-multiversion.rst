Sphinx Multiversion Tutorial
============================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-multiversion/>`_
   - `API Documentation <../../pdoc/sphinx_multiversion/index.html>`_
   - `Manual <https://github.com/Holzhaus/sphinx-multiversion>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinx-multiversion in your Sphinx documentation.

What is Sphinx Multiversion?
-----------------------------
sphinx-multiversion is a Sphinx extension that provides:

- Build multiple versions of docs
- Easy integration with Sphinx
- Comprehensive configuration options
- Professional documentation output

sphinx-multiversion provides:

- Build multiple versions of docs
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

sphinx-multiversion is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm viper-sphinx:latest python -c "import sphinx_multiversion; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``docs/conf.py``:

.. code-block:: python

   extensions = [
       'sphinx-multiversion',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinx-multiversion']
   
   # Configuration options
   # Add package-specific configuration here


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx-multiversion',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

Complete configuration with all features:

.. code-block:: python

   extensions = ['sphinx-multiversion']
   
   # Package-specific configuration
   # Add configuration options here

Basic Usage
-----------

Getting Started
~~~~~~~~~~~~~~~

Here's a basic example of using sphinx-multiversion:

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

   pip install sphinx-multiversion

Or add to your ``requirements.txt``:

.. code-block:: text

   sphinx-multiversion
   sphinx>=5.0.0

Configuration
-------------

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx-multiversion',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

Complete configuration with all features:

.. code-block:: python

   extensions = ['sphinx-multiversion']
   
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

Standard patterns for using sphinx-multiversion:

1. **Pattern 1**: Description
2. **Pattern 2**: Description
3. **Pattern 3**: Description

Integration Tips
----------------

Working with Other Extensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

sphinx-multiversion integrates well with:

- Standard Sphinx extensions
- Other documentation tools
- Custom extensions

Additional Resources
--------------------

- `PyPI Package <https://pypi.org/project/sphinx-multiversion/>`_
- `Official Documentation <https://holzhaus.github.io/sphinx-multiversion/>`_
- :doc:`Complete Tutorial <../tutorials/packages/sphinx-multiversion>`
- :ref:`Package API Documentation <pdoc-sphinx-multiversion>`
Next Steps
----------
- Explore the :doc:`tutorial <../tutorials/packages/sphinx-multiversion>`
- Check the official documentation
- Try the examples in your own projects
- Customize for your specific needs

