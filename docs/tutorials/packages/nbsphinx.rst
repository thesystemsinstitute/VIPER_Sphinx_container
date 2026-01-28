nbsphinx Tutorial
=================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/nbsphinx/>`_
   - `API Documentation <../../pdoc/nbsphinx/index.html>`_
   - `Manual <https://nbsphinx.readthedocs.io/>`_
   - :doc:`Working Example <../../examples/nbsphinx-example>`


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

   docker run --rm kensai-sphinx:latest python -c "import nbsphinx; print('Installed')"

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
     kensai-sphinx:latest \
     sphinx-build -b html /project/docs /project/docs/_build/html

With Jupyter Kernel
~~~~~~~~~~~~~~~~~~~

.. code-block:: dockerfile

   FROM kensai-sphinx:latest
   
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

Additional Resources
--------------------

- :doc:`nbsphinx-link` - Link to external notebooks
- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `nbsphinx Documentation <https://nbsphinx.readthedocs.io/>`_
- `Jupyter Notebook <https://jupyter.org/>`_
