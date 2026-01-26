Jupyter Notebook Example
========================

This example shows how to include Jupyter notebooks in your Sphinx documentation.

Setup
-----

The container includes ``nbsphinx`` for Jupyter notebook integration.

Configuration
~~~~~~~~~~~~~

In ``conf.py``:

.. code-block:: python

   extensions = [
       'nbsphinx',
       'sphinx.ext.mathjax',
   ]
   
   # Execute notebooks before conversion
   nbsphinx_execute = 'never'  # or 'always', 'auto'
   
   # Timeout for notebook execution (seconds)
   nbsphinx_timeout = 60
   
   # Allow errors during execution
   nbsphinx_allow_errors = False

Including Notebooks
-------------------

Add notebooks to your toctree:

.. code-block:: rst

   .. toctree::
      :maxdepth: 2
      
      tutorial.ipynb
      examples/data_analysis.ipynb
      examples/visualization.ipynb

Example Notebook
----------------

Create ``tutorial.ipynb``:

**Cell 1 (Markdown):**

.. code-block:: markdown

   # Data Analysis Tutorial
   
   This notebook demonstrates data analysis with pandas.

**Cell 2 (Code):**

.. code-block:: python

   import pandas as pd
   import numpy as np
   import matplotlib.pyplot as plt
   
   # Create sample data
   dates = pd.date_range('2024-01-01', periods=100)
   data = pd.DataFrame({
       'date': dates,
       'value': np.random.randn(100).cumsum()
   })
   
   print(data.head())

**Cell 3 (Markdown):**

.. code-block:: markdown

   ## Visualization
   
   Let's plot the data:

**Cell 4 (Code):**

.. code-block:: python

   plt.figure(figsize=(10, 6))
   plt.plot(data['date'], data['value'])
   plt.title('Random Walk')
   plt.xlabel('Date')
   plt.ylabel('Value')
   plt.grid(True)
   plt.show()

Advanced Features
-----------------

Custom CSS for Notebooks
~~~~~~~~~~~~~~~~~~~~~~~~~

Add custom styling:

.. code-block:: python

   nbsphinx_prolog = """
   {% set docname = env.doc2path(env.docname, base=None) %}
   
   .. note::
      This page was generated from a Jupyter notebook.
      Download: :download:`{{ docname }}`
   """

Hide Input Cells
~~~~~~~~~~~~~~~~

Use cell tags to hide input:

.. code-block:: python

   # In Jupyter, add tag "hide-input" to cell metadata
   nbsphinx_execute = 'never'

In the notebook cell metadata:

.. code-block:: json

   {
     "tags": ["hide-input"]
   }

Execute on Build
~~~~~~~~~~~~~~~~

.. code-block:: python

   nbsphinx_execute = 'always'
   nbsphinx_kernel_name = 'python3'

Mathematical Equations
~~~~~~~~~~~~~~~~~~~~~~

Notebooks support LaTeX math:

**Markdown Cell:**

.. code-block:: markdown

   The quadratic formula is:
   
   $$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

Interactive Widgets
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from ipywidgets import interact, FloatSlider
   import numpy as np
   import matplotlib.pyplot as plt
   
   @interact(freq=FloatSlider(min=1, max=10, step=0.1, value=1))
   def plot_sine(freq):
       x = np.linspace(0, 2*np.pi, 100)
       y = np.sin(freq * x)
       plt.figure(figsize=(10, 4))
       plt.plot(x, y)
       plt.title(f'sin({freq}x)')
       plt.grid(True)
       plt.show()

Best Practices
--------------

1. **Keep Notebooks Focused**: One topic per notebook
2. **Clear Outputs**: Clear outputs before committing to git
3. **Execution**: Decide whether to execute during build
4. **Size**: Keep notebooks reasonably sized (< 1MB)
5. **Dependencies**: Document required packages

Example: Data Analysis Workflow
--------------------------------

.. code-block:: rst

   Data Analysis Guide
   ===================
   
   This guide walks through a complete data analysis workflow.
   
   .. toctree::
      :maxdepth: 1
      
      notebooks/01_data_loading
      notebooks/02_cleaning
      notebooks/03_exploration
      notebooks/04_visualization
      notebooks/05_modeling

Linking Between Documents
--------------------------

From notebook to RST:

.. code-block:: markdown

   See the [API Reference](api-reference.rst) for details.

From RST to notebook:

.. code-block:: rst

   See :doc:`tutorial` for a hands-on example.

Troubleshooting
---------------

Kernel Not Found
~~~~~~~~~~~~~~~~

.. code-block:: python

   nbsphinx_kernel_name = 'python3'

Execution Timeout
~~~~~~~~~~~~~~~~~

.. code-block:: python

   nbsphinx_timeout = 600  # 10 minutes

Missing Dependencies
~~~~~~~~~~~~~~~~~~~~

Install required packages in the container:

.. code-block:: dockerfile

   RUN pip install jupyter pandas numpy matplotlib

Resources
---------

* `nbsphinx Documentation <https://nbsphinx.readthedocs.io/>`_
* `Jupyter Documentation <https://jupyter.org/documentation>`_
