Code2Flow Tutorial
==================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/code2flow/>`_
   - `API Documentation <../../pdoc/code2flow/index.html>`_
   - `Manual <https://github.com/scottrogowski/code2flow>`_
   - :doc:`Working Example <../../examples/code2flow-example>`


.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use code2flow, a call graph generation from source code.

What is Code2Flow?
-----------------
Code2Flow provides features for:

- Core functionality
- Integration with Sphinx
- Configuration options
- Advanced features
- Best practices

The code2flow package provides functionality for working with call graph generation from source code.


Installation
------------

Install via pip:

.. code-block:: bash

   pip install code2flow

Configuration
-------------

Add to your Sphinx ``conf.py``:

.. code-block:: python

   extensions = [
       'code2flow',
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
   code2flow_config = {
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

- `Official Documentation <https://pypi.org/project/code2flow/>`_
- `PyPI Package <https://pypi.org/project/code2flow/>`_
- :doc:`Example Usage <../../examples/code2flow-example>`

See Also
--------

- :doc:`Sphinx Basics <../sphinx-basics>`
- :doc:`Package Overview <../../sphinx-packages>`
