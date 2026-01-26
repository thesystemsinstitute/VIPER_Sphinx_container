API Documentation Example
=========================

This example shows how to automatically generate API documentation from Python code.

Module Documentation
--------------------

example_module
~~~~~~~~~~~~~~

**Module**: ``example_module.py``

.. code-block:: python

   """Example module for demonstration.
   
   This module provides calculator functionality with
   support for basic and advanced operations.
   """
   
   class Calculator:
       """A calculator for mathematical operations.
       
       This calculator supports basic arithmetic and
       advanced mathematical functions.
       
       Attributes:
           history (list): List of previous calculations
           precision (int): Number of decimal places
       
       Example:
           >>> calc = Calculator(precision=2)
           >>> calc.add(1.5, 2.7)
           4.2
       """
       
       def __init__(self, precision=2):
           """Initialize the calculator.
           
           Args:
               precision (int): Decimal precision (default: 2)
           """
           self.precision = precision
           self.history = []
       
       def add(self, a, b):
           """Add two numbers.
           
           Args:
               a (float): First operand
               b (float): Second operand
           
           Returns:
               float: Sum rounded to precision
           
           Example:
               >>> calc.add(5, 3)
               8.0
           """
           result = round(a + b, self.precision)
           self.history.append(('add', a, b, result))
           return result
       
       def subtract(self, a, b):
           """Subtract b from a.
           
           Args:
               a (float): Minuend
               b (float): Subtrahend
           
           Returns:
               float: Difference rounded to precision
           """
           result = round(a - b, self.precision)
           self.history.append(('subtract', a, b, result))
           return result
       
       def get_history(self):
           """Get calculation history.
           
           Returns:
               list: List of (operation, a, b, result) tuples
           """
           return self.history

Using autodoc
~~~~~~~~~~~~~

To document this automatically, use:

.. code-block:: rst

   .. automodule:: example_module
      :members:
      :undoc-members:
      :show-inheritance:

Class Documentation
~~~~~~~~~~~~~~~~~~~

Document a specific class:

.. code-block:: rst

   .. autoclass:: example_module.Calculator
      :members:
      :special-members: __init__
      :member-order: bysource

Function Documentation
~~~~~~~~~~~~~~~~~~~~~~

Document individual functions:

.. code-block:: rst

   .. autofunction:: example_module.Calculator.add
   
   .. autofunction:: example_module.Calculator.subtract

Advanced Example with NumPy Style
----------------------------------

.. code-block:: python

   import numpy as np
   
   def process_data(data, method='mean', axis=0):
       """Process numerical data using various methods.
       
       Parameters
       ----------
       data : array_like
           Input data to process
       method : {'mean', 'median', 'std'}, optional
           Processing method (default: 'mean')
       axis : int, optional
           Axis along which to process (default: 0)
       
       Returns
       -------
       ndarray
           Processed data
       
       Raises
       ------
       ValueError
           If method is not recognized
       TypeError
           If data cannot be converted to array
       
       See Also
       --------
       numpy.mean : Compute mean of array
       numpy.median : Compute median of array
       
       Notes
       -----
       This function uses NumPy for efficient computation.
       
       Examples
       --------
       >>> data = [[1, 2], [3, 4]]
       >>> process_data(data, method='mean')
       array([2., 3.])
       
       >>> process_data(data, method='mean', axis=1)
       array([1.5, 3.5])
       """
       arr = np.asarray(data)
       
       if method == 'mean':
           return np.mean(arr, axis=axis)
       elif method == 'median':
           return np.median(arr, axis=axis)
       elif method == 'std':
           return np.std(arr, axis=axis)
       else:
           raise ValueError(f"Unknown method: {method}")

Complete conf.py for API Docs
------------------------------

.. code-block:: python

   # conf.py
   
   extensions = [
       'sphinx.ext.autodoc',
       'sphinx.ext.napoleon',
       'sphinx.ext.viewcode',
       'sphinx.ext.intersphinx',
   ]
   
   # Napoleon settings
   napoleon_google_docstring = True
   napoleon_numpy_docstring = True
   napoleon_include_init_with_doc = True
   napoleon_include_private_with_doc = False
   napoleon_include_special_with_doc = True
   napoleon_use_admonition_for_examples = False
   napoleon_use_admonition_for_notes = False
   napoleon_use_admonition_for_references = False
   napoleon_use_ivar = False
   napoleon_use_param = True
   napoleon_use_rtype = True
   
   # Autodoc settings
   autodoc_default_options = {
       'members': True,
       'member-order': 'bysource',
       'special-members': '__init__',
       'undoc-members': True,
       'exclude-members': '__weakref__'
   }
   
   # Intersphinx
   intersphinx_mapping = {
       'python': ('https://docs.python.org/3', None),
       'numpy': ('https://numpy.org/doc/stable/', None),
   }
