Pytest-Doctestplus Example
==========================

This page demonstrates the **pytest-doctestplus** extension for enhanced doctest support in Sphinx and pytest.

.. contents:: Contents
   :local:
   :depth: 2

Overview
--------

The pytest-doctestplus extension provides advanced doctest features including floating-point comparison and output normalization.

Basic Usage
-----------

Simple Doctest
~~~~~~~~~~~~~~

.. code-block:: python

   def add(a, b):
       """Add two numbers.
       
       >>> add(2, 3)
       5
       >>> add(10, 20)
       30
       """
       return a + b

Floating Point
~~~~~~~~~~~~~~

.. code-block:: python

   def calculate_pi():
       """Calculate pi approximation.
       
       >>> calculate_pi()  # doctest: +FLOAT_CMP
       3.14159265
       """
       return 3.14159265358979

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx.ext.doctest',
   ]
   
   # pytest configuration in pyproject.toml
   # [tool.pytest.ini_options]
   # doctest_plus = "enabled"

Options
~~~~~~~

.. code-block:: python

   doctest_global_setup = '''
   import numpy as np
   import pandas as pd
   '''
   
   doctest_test_doctest_blocks = 'default'

Examples
--------

Array Comparison
~~~~~~~~~~~~~~~~

.. code-block:: python

   def create_array():
       """Create numpy array.
       
       >>> import numpy as np
       >>> create_array()  # doctest: +FLOAT_CMP
       array([1., 2., 3.])
       """
       return np.array([1.0, 2.0, 3.0])

See Also
--------

- :doc:`../tutorials/packages/pytest-doctestplus` - Complete tutorial
- pytest documentation: https://docs.pytest.org/
- GitHub repository: https://github.com/astropy/pytest-doctestplus
