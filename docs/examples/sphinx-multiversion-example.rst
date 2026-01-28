Sphinx Multiversion Example
===========================

.. note::

   **Package**: sphinx-multiversion  
   **Purpose**: Build multiple versions of docs  
   **Tutorial**: See :doc:`../tutorials/packages/sphinx-multiversion` for complete tutorial

This page demonstrates **sphinx-multiversion** - Build multiple versions of docs.

.. contents:: Contents
   :local:
   :depth: 3

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

- :doc:`Complete Tutorial <../tutorials/packages/sphinx-multiversion>`
- `PyPI Package <https://pypi.org/project/sphinx-multiversion/>`_
- `Official Documentation <https://holzhaus.github.io/sphinx-multiversion/>`_
- :ref:`Package API Documentation <pdoc-sphinx-multiversion>`

Next Steps
----------

- Explore the :doc:`tutorial <../tutorials/packages/sphinx-multiversion>`
- Check the official documentation
- Try the examples in your own projects
- Customize for your specific needs
