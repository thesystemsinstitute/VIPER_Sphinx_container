Basic Example
=============

This is a complete example of a basic Sphinx documentation page.

Project Overview
----------------

This example demonstrates how to create simple, clean documentation for a software project.

Installation
------------

Install the package using pip:

.. code-block:: bash

   pip install example-package

Or from source:

.. code-block:: bash

   git clone https://github.com/example/example-package.git
   cd example-package
   pip install -e .

Quick Start
-----------

Here's how to get started quickly:

.. code-block:: python

   from example_package import Calculator
   
   calc = Calculator()
   result = calc.add(5, 3)
   print(f"Result: {result}")  # Output: Result: 8

Configuration
-------------

Create a configuration file:

.. code-block:: yaml

   # config.yaml
   calculator:
     precision: 2
     mode: scientific

Load it in your code:

.. code-block:: python

   from example_package import Calculator
   
   calc = Calculator.from_config('config.yaml')

Features
--------

The package includes:

* **Basic Operations**: Add, subtract, multiply, divide
* **Advanced Functions**: Power, square root, logarithm
* **Scientific Mode**: Trigonometric functions
* **History**: Track calculation history

Basic Operations
~~~~~~~~~~~~~~~~

.. code-block:: python

   calc = Calculator()
   
   # Addition
   calc.add(10, 5)        # Returns: 15
   
   # Subtraction
   calc.subtract(10, 5)   # Returns: 5
   
   # Multiplication
   calc.multiply(10, 5)   # Returns: 50
   
   # Division
   calc.divide(10, 5)     # Returns: 2.0

Advanced Functions
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import math
   
   # Power
   calc.power(2, 3)       # Returns: 8
   
   # Square root
   calc.sqrt(16)          # Returns: 4.0
   
   # Logarithm
   calc.log(100, 10)      # Returns: 2.0

API Reference
-------------

Calculator Class
~~~~~~~~~~~~~~~~

.. code-block:: python

   class Calculator:
       """A simple calculator class.
       
       Provides basic and advanced mathematical operations.
       """
       
       def add(self, a, b):
           """Add two numbers.
           
           Args:
               a (float): First number
               b (float): Second number
               
           Returns:
               float: Sum of a and b
           """
           return a + b

See Also
--------

* :doc:`api-docs-example` - Full API documentation example
* :doc:`jupyter-example` - Jupyter notebook integration
