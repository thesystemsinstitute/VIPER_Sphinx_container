Markdown-it-py Tutorial
=======================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/markdown-it-py/>`_
   - `API Documentation <../../pdoc/markdown_it_py/index.html>`_
   - `Manual <https://markdown-it-py.readthedocs.io/>`_
   - :doc:`Working Example <../../examples/markdown-it-py-example>`


.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use markdown-it-py, a Python port of markdown-it parser.

What is Markdown-it-py?
----------------------
Markdown-it-py provides features for:

- Core functionality
- Integration with Sphinx
- Configuration options
- Advanced features
- Best practices

The markdown-it-py package provides functionality for working with Python port of markdown-it parser.


Installation
------------

Install via pip:

.. code-block:: bash

   pip install markdown-it-py

Configuration
-------------

Add to your Sphinx ``conf.py``:

.. code-block:: python

   extensions = [
       'markdown_it_py',
   ]

Basic Usage
-----------

Simple Example
~~~~~~~~~~~~~~

Basic usage example:

.. code-block:: python

   # Example code here
   pass

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

Advanced configuration options:

.. code-block:: python

   # Configuration in conf.py
   markdown_it_py_config = {
       'option1': 'value1',
       'option2': 'value2',
   }

Best Practices
--------------

1. Follow documentation conventions
2. Use appropriate settings
3. Test thoroughly
4. Keep configuration simple
5. Document usage patterns

Common Issues
-------------

Issue 1
~~~~~~~

**Problem:** Common issue description

**Solution:** How to resolve it

Issue 2
~~~~~~~

**Problem:** Another common issue

**Solution:** Resolution steps

Resources
---------

- `Official Documentation <https://pypi.org/project/markdown-it-py/>`_
- `PyPI Package <https://pypi.org/project/markdown-it-py/>`_
- :doc:`Example Usage <../../examples/markdown-it-py-example>`

See Also
--------

- :doc:`Sphinx Basics <../sphinx-basics>`
- :doc:`Package Overview <../../sphinx-packages>`
