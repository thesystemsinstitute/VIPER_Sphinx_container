nbsphinx Tutorial
=================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/nbsphinx/>`_
   - `API Documentation <../../pdoc/nbsphinx/index.html>`_
   - `Manual <https://nbsphinx.readthedocs.io/>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use nbsphinx to include Jupyter Notebooks in your Sphinx documentation.

What is nbsphinx?
-----------------
nbsphinx is a Sphinx extension that provides:

- Jupyter Notebook integration
- Execute notebooks during build
- Display notebook outputs
- Syntax highlighting
- Interactive widgets
- Math rendering
- Markdown cells
- Code cell execution
- Image embedding
- Custom CSS styling
- nbconvert integration

This allows you to include executable code examples and tutorials directly from Jupyter Notebooks.

The nbsphinx extension allows you to use Jupyter notebooks (``.ipynb`` files) as source files for Sphinx documentation, with automatic rendering of code cells, outputs, and markdown cells.


Installation
------------

nbsphinx is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm viper-sphinx:latest python -c "import nbsphinx; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'nbsphinx',
   ]
   
   # Source file suffixes
   source_suffix = {
       '.rst': 'restructuredtext',
       '.ipynb': 'nbsphinx',
       '.md': 'markdown',
   }

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = [
       'nbsphinx',
       'sphinx.ext.mathjax',
       'IPython.sphinxext.ipython_console_highlighting',
   ]
   
   source_suffix = {
       '.rst': 'restructuredtext',
       '.ipynb': 'nbsphinx',
   }
   
   # Execution configuration
   nbsphinx_execute = 'auto'  # auto, always, never
   nbsphinx_execute_arguments = [
       "--InlineBackend.figure_formats={'svg', 'pdf'}",
       "--InlineBackend.rc={'figure.dpi': 96}",
   ]
   
   # Timeout for notebook execution (seconds)
   nbsphinx_timeout = 60
   
   # Kernel name
   nbsphinx_kernel_name = 'python3'
   
   # Allow errors during execution
   nbsphinx_allow_errors = False
   
   # Thumbnail for notebooks
   nbsphinx_thumbnails = {
       'examples/tutorial': '_static/tutorial-thumb.png',
   }
   
   # Custom CSS
   nbsphinx_custom_formats = {
       '.mysuffix': lambda s: s,
   }
   
   # Prolog/epilog for all notebooks
   nbsphinx_prolog = """
   .. note::
      This page was generated from a Jupyter notebook.
   """

Basic Usage
-----------

Include Notebook in Toctree
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/index.rst``:

.. code-block:: rst

   .. toctree::
      :maxdepth: 2
      
      installation
      tutorials/getting-started.ipynb
      tutorials/advanced.ipynb
      api/reference

The ``.ipynb`` files are automatically rendered!

Create Tutorial Notebook
~~~~~~~~~~~~~~~~~~~~~~~~~

Create ``docs/tutorials/getting-started.ipynb``:

.. code-block:: python

   # First cell (Markdown)
   # Getting Started
   
   This tutorial shows basic usage.
   
   ## Installation
   
   Install the package:
   
   ```bash
   pip install mypackage
   ```
   
   # Second cell (Code)
   import mypackage
   print(mypackage.__version__)
   
   # Third cell (Code with output)
   import numpy as np
   import matplotlib.pyplot as plt
   
   x = np.linspace(0, 2*np.pi, 100)
   y = np.sin(x)
   
   plt.plot(x, y)
   plt.title('Sine Wave')
   plt.show()

Advanced Features
-----------------

Control Notebook Execution
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add metadata to notebook cells:

.. code-block:: json

   {
     "nbsphinx": "hidden",
     "tags": ["remove-cell"]
   }

Or in conf.py:

.. code-block:: python

   nbsphinx_execute = 'never'  # Don't execute notebooks

Hide Code Cells
~~~~~~~~~~~~~~~

Add to cell metadata:

.. code-block:: json

   {
     "nbsphinx": "hidden"
   }

Or use tags:

.. code-block:: json

   {
     "tags": ["hide-input", "hide-output"]
   }

Custom Thumbnails
~~~~~~~~~~~~~~~~~

.. code-block:: python

   nbsphinx_thumbnails = {
       'examples/tutorial': '_static/tutorial-thumb.png',
       'examples/advanced': '_static/advanced-thumb.png',
   }

Prolog and Epilog
~~~~~~~~~~~~~~~~~

.. code-block:: python

   nbsphinx_prolog = """
   .. note::
      
      This page was generated from a Jupyter notebook.
      
      :download:`Download notebook <{{ env.docname }}.ipynb>`
   """
   
   nbsphinx_epilog = """
   .. seealso::
      
      :doc:`/api/reference` - API documentation
   """

Custom Formats
~~~~~~~~~~~~~~

.. code-block:: python

   import nbformat
   
   def custom_converter(text):
       nb = nbformat.reads(text, as_version=4)
       # Modify notebook
       return nb
   
   nbsphinx_custom_formats = {
       '.custom': custom_converter,
   }

Docker Integration
------------------

Build Notebook Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     viper-sphinx:latest \
     sphinx-build -b html /project/docs /project/docs/_build/html

With Jupyter Kernel
~~~~~~~~~~~~~~~~~~~

.. code-block:: dockerfile

   FROM viper-sphinx:latest
   
   # Install notebook dependencies
   RUN pip install jupyter ipykernel pandas matplotlib seaborn scikit-learn
   
   # Register kernel
   RUN python -m ipykernel install --name python3

Build:

.. code-block:: bash

   docker build -t sphinx-jupyter .
   docker run --rm -v $(pwd):/project \
     sphinx-jupyter \
     sphinx-build -b html /project/docs /project/docs/_build/html

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Build Notebook Docs
   
   on:
     push:
       paths:
         - 'docs/**/*.ipynb'
         - 'docs/**/*.rst'
   
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Setup Python
           uses: actions/setup-python@v4
           with:
             python-version: '3.11'
         
         - name: Install Dependencies
           run: |
             pip install sphinx nbsphinx ipykernel
             pip install -r requirements.txt
         
         - name: Build Documentation
           run: |
             sphinx-build -b html docs docs/_build/html
         
         - name: Deploy
           uses: peaceiris/actions-gh-pages@v3
           with:
             github_token: ${{ secrets.GITHUB_TOKEN }}
             publish_dir: ./docs/_build/html

Best Practices
--------------

1. **Keep Notebooks Simple**
   
   Focus on one concept per notebook

2. **Add Explanatory Text**
   
   Use Markdown cells liberally

3. **Control Execution**
   
   Set appropriate timeouts

4. **Version Control**
   
   Clear outputs before committing

5. **Handle Dependencies**
   
   Document required packages

6. **Test Execution**
   
   Ensure notebooks run cleanly

Troubleshooting
---------------

Kernel Not Found
~~~~~~~~~~~~~~~~

**Solution:**

Install and register kernel:

.. code-block:: bash

   pip install ipykernel
   python -m ipykernel install --user --name python3

Execution Timeout
~~~~~~~~~~~~~~~~~

**Solution:**

Increase timeout:

.. code-block:: python

   nbsphinx_timeout = 120  # seconds

Missing Outputs
~~~~~~~~~~~~~~~

**Solution:**

Execute notebooks:

.. code-block:: python

   nbsphinx_execute = 'always'

Or execute manually:

.. code-block:: bash

   jupyter nbconvert --execute --inplace notebook.ipynb

Import Errors
~~~~~~~~~~~~~

**Solution:**

Install dependencies:

.. code-block:: bash

   pip install -r requirements.txt

Images Not Showing
~~~~~~~~~~~~~~~~~~

**Solution:**

Use relative paths or embedded images:

.. code-block:: python

   from IPython.display import Image
   Image('path/to/image.png')

Next Steps
----------

1. Create Jupyter notebooks
2. Add to toctree
3. Configure execution
4. Test builds
5. Deploy documentation


Practical Examples
------------------

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


Practical Examples
------------------

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


Practical Examples
------------------

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

Additional Resources
--------------------
- :doc:`nbsphinx-link` - Link to external notebooks
- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `nbsphinx Documentation <https://nbsphinx.readthedocs.io/>`_
- `Jupyter Notebook <https://jupyter.org/>`_
- :doc:`../tutorials/packages/nbsphinx` - Complete tutorial
- GitHub repository: https://github.com/spatialaudio/nbsphinx
- Jupyter documentation: https://jupyter.org/documentation

