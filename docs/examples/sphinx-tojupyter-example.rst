Sphinx-ToJupyter Example
========================

This page demonstrates the **sphinx-tojupyter** extension for converting Sphinx documentation to Jupyter notebooks.

.. contents:: Contents
   :local:
   :depth: 2

Overview
--------

The sphinx-tojupyter extension converts RST documentation into executable Jupyter notebooks, preserving code blocks, narrative text, and formatting.

Basic Conversion
----------------

Code Block Conversion
~~~~~~~~~~~~~~~~~~~~~

Python code blocks are converted to code cells:

.. code-block:: python

   # This becomes a code cell
   import numpy as np
   x = np.linspace(0, 10, 100)
   y = np.sin(x)

Markdown Conversion
~~~~~~~~~~~~~~~~~~~

Regular text is converted to markdown cells:

This paragraph will appear as markdown in the notebook.

- Lists are preserved
- **Bold** and *italic* formatting maintained
- Links remain functional

Notebook Features
-----------------

Executable Cells
~~~~~~~~~~~~~~~~

.. code-block:: python

   # Executable code
   def calculate(a, b):
       return a + b
   
   result = calculate(5, 3)
   print(f"Result: {result}")

Plotting Examples
~~~~~~~~~~~~~~~~~

.. code-block:: python

   import matplotlib.pyplot as plt
   
   plt.plot(x, y)
   plt.xlabel('X axis')
   plt.ylabel('Y axis')
   plt.title('Sine Wave')
   plt.show()

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_tojupyter',
   ]
   
   jupyter_conversion_mode = 'all'  # 'all', 'code', or 'markdown'
   jupyter_output_dir = '_jupyter'

Advanced Options
~~~~~~~~~~~~~~~~

.. code-block:: python

   jupyter_kernels = {
       'python3': {
           'kernelspec': {
               'display_name': "Python 3",
               'language': "python",
               'name': "python3"
           }
       }
   }
   
   jupyter_execute_notebooks = True
   jupyter_allow_errors = False

Cell Metadata
~~~~~~~~~~~~~

.. code-block:: python

   jupyter_cell_metadata = {
       'tags': ['remove-cell', 'hide-input'],
       'slideshow': {'slide_type': 'slide'},
   }

Practical Examples
------------------

Tutorial Notebook
~~~~~~~~~~~~~~~~~

Create step-by-step tutorials:

.. code-block:: python

   # Step 1: Import libraries
   import pandas as pd
   
   # Step 2: Load data
   df = pd.read_csv('data.csv')
   
   # Step 3: Analyze
   print(df.describe())

Data Analysis
~~~~~~~~~~~~~

.. code-block:: python

   # Load and process data
   data = [1, 2, 3, 4, 5]
   mean = sum(data) / len(data)
   print(f"Mean: {mean}")

See Also
--------

- :doc:`../tutorials/packages/sphinx-tojupyter` - Complete tutorial
- Jupyter documentation: https://jupyter.org/
- GitHub repository: https://github.com/QuantEcon/sphinxcontrib-jupyter
