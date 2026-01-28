nbsphinx Example
================

This page demonstrates the **nbsphinx** extension for including Jupyter notebooks directly in Sphinx documentation.

.. contents:: Contents
   :local:
   :depth: 2

Overview
--------

The nbsphinx extension allows you to use Jupyter notebooks (``.ipynb`` files) as source files for Sphinx documentation, with automatic rendering of code cells, outputs, and markdown cells.

Basic Setup
-----------

Configuration
~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   extensions = [
       'nbsphinx',
   ]
   
   # Source file patterns
   source_suffix = {
       '.rst': 'restructuredtext',
       '.ipynb': 'nbsphinx',
   }

Exclude Patterns
~~~~~~~~~~~~~~~~

.. code-block:: python

   # Don't include checkpoint files
   exclude_patterns = [
       '_build',
       '**.ipynb_checkpoints',
   ]

Including Notebooks
-------------------

In Toctree
~~~~~~~~~~

.. code-block:: rst

   .. toctree::
      :maxdepth: 2
   
      introduction.rst
      tutorial.ipynb
      examples.ipynb
      api_reference.rst

Direct Include
~~~~~~~~~~~~~~

.. code-block:: rst

   .. include:: notebook.ipynb

Notebook Structure
------------------

Markdown Cells
~~~~~~~~~~~~~~

Notebooks can contain markdown cells:

.. code-block:: markdown

   # Main Title
   
   This is a **Jupyter notebook** rendered in Sphinx.
   
   ## Subsection
   
   - Item 1
   - Item 2
   - Item 3

Code Cells
~~~~~~~~~~

Python code cells with output:

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   
   x = np.linspace(0, 10, 100)
   y = np.sin(x)
   
   plt.plot(x, y)
   plt.title('Sine Wave')
   plt.xlabel('x')
   plt.ylabel('sin(x)')
   plt.show()

Raw Cells
~~~~~~~~~

Raw cells for Sphinx directives:

.. code-block:: rst

   .. note::
      This is a Sphinx directive in a raw cell.

Execution Control
-----------------

Execute on Build
~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   # Execute notebooks during build
   nbsphinx_execute = 'auto'  # 'always', 'never', 'auto'

Per-Notebook Control
~~~~~~~~~~~~~~~~~~~~

Add to notebook metadata:

.. code-block:: json

   {
     "nbsphinx": {
       "execute": "never"
     }
   }

Timeout Configuration
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Set execution timeout (seconds)
   nbsphinx_timeout = 60  # -1 for no timeout

Kernel Selection
~~~~~~~~~~~~~~~~

.. code-block:: python

   # Specify kernel
   nbsphinx_kernel_name = 'python3'

Code Cell Options
-----------------

Hide Input
~~~~~~~~~~

Add cell metadata:

.. code-block:: json

   {
     "nbsphinx": "hidden"
   }

Or use cell tag ``nbsphinx-hidden``.

Hide Output
~~~~~~~~~~~

.. code-block:: json

   {
     "nbsphinx": {
       "output-hidden": true
     }
   }

Custom Cell Tags
~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   nbsphinx_custom_formats = {
       '.py': ['jupytext.reads', {'fmt': 'py:percent'}],
   }

Output Formatting
-----------------

Figure Captions
~~~~~~~~~~~~~~~

Add caption to figures:

.. code-block:: python

   # Code cell with caption in metadata
   plt.plot([1, 2, 3], [1, 4, 9])

Cell metadata:

.. code-block:: json

   {
     "nbsphinx": {
       "caption": "This is a figure caption"
     }
   }

Image Scaling
~~~~~~~~~~~~~

.. code-block:: json

   {
     "nbsphinx": {
       "thumbnail": {
         "width": "200px"
       }
     }
   }

Table Formatting
~~~~~~~~~~~~~~~~

DataFrames are automatically formatted:

.. code-block:: python

   import pandas as pd
   
   df = pd.DataFrame({
       'A': [1, 2, 3],
       'B': [4, 5, 6]
   })
   df

Links and References
--------------------

Cross-References
~~~~~~~~~~~~~~~~

In markdown cells:

.. code-block:: markdown

   See the [API Reference](api.rst) for details.
   
   Jump to {ref}`section-label`.

Internal Links
~~~~~~~~~~~~~~

.. code-block:: markdown

   [Link to another notebook](other_notebook.ipynb)

External Links
~~~~~~~~~~~~~~

.. code-block:: markdown

   Visit [NumPy documentation](https://numpy.org/doc/)

Math Support
------------

Inline Math
~~~~~~~~~~~

.. code-block:: markdown

   Einstein's equation: $E = mc^2$

Display Math
~~~~~~~~~~~~

.. code-block:: markdown

   $$
   \int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
   $$

LaTeX Equations
~~~~~~~~~~~~~~~

.. code-block:: markdown

   \\begin{equation}
   x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
   \\end{equation}

Advanced Configuration
----------------------

Custom CSS
~~~~~~~~~~

.. code-block:: python

   # conf.py
   html_static_path = ['_static']
   html_css_files = ['custom_notebook.css']

Prompt Format
~~~~~~~~~~~~~

.. code-block:: python

   # Customize input/output prompts
   nbsphinx_prompt_width = '0'  # Hide prompts
   
   # Or custom format
   nbsphinx_input_prompt = 'In [%s]:'
   nbsphinx_output_prompt = 'Out[%s]:'

Code Highlighting
~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Pygments style
   pygments_style = 'sphinx'
   
   # Or custom theme
   pygments_style = 'monokai'

Thumbnails
~~~~~~~~~~

.. code-block:: python

   # Generate thumbnails for gallery
   nbsphinx_thumbnails = {
       'notebooks/example': '_static/thumb.png',
   }

Error Handling
--------------

Allow Errors
~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   nbsphinx_allow_errors = True

Per-Cell Control
~~~~~~~~~~~~~~~~

Cell metadata:

.. code-block:: json

   {
     "nbsphinx": {
       "allow_errors": true
     }
   }

Execution Environment
---------------------

Custom Environment
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   nbsphinx_execute_arguments = [
       "--InlineBackend.figure_formats={'svg', 'pdf'}",
       "--InlineBackend.rc={'figure.dpi': 96}",
   ]

Working Directory
~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Execute in notebook directory
   nbsphinx_execute_in_temp_directory = False

Prolog and Epilog
-----------------

Add Code Before
~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   nbsphinx_prolog = r"""
   {% set docname = env.doc2path(env.docname, base=None) %}
   
   .. note::
      This notebook is located at ``{{ docname }}``.
   """

Add Code After
~~~~~~~~~~~~~~

.. code-block:: python

   nbsphinx_epilog = r"""
   .. note::
      End of notebook.
   """

Practical Examples
------------------

Tutorial Notebook
~~~~~~~~~~~~~~~~~

Structure:

.. code-block:: markdown

   # Tutorial: Data Analysis with Pandas
   
   ## Introduction
   
   This tutorial covers basic data analysis operations.
   
   ## Setup

.. code-block:: python

   import pandas as pd
   import numpy as np
   
   # Load data
   df = pd.read_csv('data.csv')
   df.head()

.. code-block:: markdown

   ## Analysis
   
   Let's analyze the data:

.. code-block:: python

   # Basic statistics
   df.describe()

Documentation with Code
~~~~~~~~~~~~~~~~~~~~~~~

Mix narrative and code:

.. code-block:: markdown

   # API Example
   
   The `process_data` function accepts a DataFrame:

.. code-block:: python

   from mypackage import process_data
   
   result = process_data(df)
   print(result)

Gallery
~~~~~~~

Create example gallery:

.. code-block:: rst

   Examples Gallery
   ================
   
   .. toctree::
      :maxdepth: 1
   
      examples/plot_basic
      examples/plot_advanced
      examples/plot_custom

Integration Tips
----------------

With Read the Docs
~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

   # .readthedocs.yaml
   build:
     os: ubuntu-22.04
     tools:
       python: "3.11"
   
   python:
     install:
       - requirements: requirements.txt

Requirements
~~~~~~~~~~~~

.. code-block:: text

   # requirements.txt
   nbsphinx
   jupyter
   ipykernel
   matplotlib
   pandas
   numpy

Version Control
~~~~~~~~~~~~~~~

.. code-block:: gitignore

   # .gitignore
   **/.ipynb_checkpoints/
   docs/_build/
   docs/**/_build/

Clean Notebooks
~~~~~~~~~~~~~~~

.. code-block:: bash

   # Clear outputs before committing
   jupyter nbconvert --clear-output --inplace notebook.ipynb

Best Practices
--------------

Notebook Organization
~~~~~~~~~~~~~~~~~~~~~

1. One concept per notebook
2. Clear section headings
3. Explanatory markdown cells
4. Clean, commented code
5. Hide unnecessary cells

Performance
~~~~~~~~~~~

1. Set appropriate timeouts
2. Use ``nbsphinx_execute = 'never'`` for expensive notebooks
3. Cache execution results
4. Minimize notebook size

Documentation
~~~~~~~~~~~~~

1. Mix with RST files for structure
2. Use notebooks for examples/tutorials
3. Keep API docs in RST
4. Cross-reference between formats

See Also
--------

- :doc:`../tutorials/packages/nbsphinx` - Complete tutorial
- GitHub repository: https://github.com/spatialaudio/nbsphinx
- Jupyter documentation: https://jupyter.org/documentation
