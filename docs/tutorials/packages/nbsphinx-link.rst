nbsphinx-link Tutorial
======================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/nbsphinx-link/>`_
   - `API Documentation <../../pdoc/nbsphinx_link/index.html>`_
   - `Manual <https://nbsphinx-link.readthedocs.io/>`_
   - :doc:`Working Example <../../examples/nbsphinx-link-example>`


.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use nbsphinx-link to reference Jupyter Notebooks from outside your documentation directory.

What is nbsphinx-link?
-----------------------
nbsphinx-link is a Sphinx extension that provides:

- Link to external notebooks
- Reference notebooks outside docs
- Avoid notebook duplication
- Keep notebooks in source tree
- Maintain single source
- Symlink alternative
- Cross-platform compatible
- Simple .nblink files
- Version control friendly
- No file copying needed

This is perfect for including example notebooks that live alongside your source code.

The nbsphinx-link extension allows you to include Jupyter notebooks that are stored outside your documentation source directory, which is useful for keeping examples with source code while including them in documentation.


Installation
------------

nbsphinx-link is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import nbsphinx_link; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'nbsphinx',
       'nbsphinx_link',
   ]
   
   source_suffix = {
       '.rst': 'restructuredtext',
       '.ipynb': 'nbsphinx',
       '.nblink': 'nbsphinx-link',
   }

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = [
       'nbsphinx',
       'nbsphinx_link',
   ]
   
   source_suffix = {
       '.rst': 'restructuredtext',
       '.ipynb': 'nbsphinx',
       '.nblink': 'nbsphinx-link',
   }
   
   # nbsphinx configuration
   nbsphinx_execute = 'auto'
   nbsphinx_timeout = 60
   nbsphinx_allow_errors = False

Basic Usage
-----------

Create Link File
~~~~~~~~~~~~~~~~

Create ``docs/examples/tutorial.nblink``:

.. code-block:: json

   {
       "path": "../../examples/tutorial.ipynb"
   }

This links to ``examples/tutorial.ipynb`` which is outside the docs directory.

Include in Toctree
~~~~~~~~~~~~~~~~~~

``docs/index.rst``:

.. code-block:: rst

   .. toctree::
      :maxdepth: 2
      
      installation
      examples/tutorial.nblink
      api/reference

The linked notebook is rendered as if it were in the docs directory!

   Documentation
   =============
   
   Tutorials
   ---------
   
   .. toctree::
      :maxdepth: 1
      
      notebooks/tutorials/beginner.nblink
      notebooks/tutorials/advanced.nblink
   
   How-To Guides
   -------------
   
   .. toctree::
      :maxdepth: 1
      
      notebooks/howtos/visualization.nblink
      notebooks/howtos/optimization.nblink
   
Advanced Features
-----------------

Relative Path Resolution
~~~~~~~~~~~~~~~~~~~~~~~~

Paths in .nblink files are relative to the .nblink file location:

.. code-block:: json

   {
       "path": "../../examples/notebook.ipynb"
   }

Absolute Paths
~~~~~~~~~~~~~~

You can use absolute paths (not recommended):

.. code-block:: json

   {
       "path": "/absolute/path/to/notebook.ipynb"
   }

Build-Time Generation
~~~~~~~~~~~~~~~~~~~~~~

``docs/conf.py``:

.. code-block:: python

   import subprocess
   
   def setup(app):
       """Generate nblink files before build."""
       subprocess.run(['python', 'generate_nblinks.py'], check=True)

Git Integration
~~~~~~~~~~~~~~~

``.gitignore``:

.. code-block:: text

   # Don't commit generated nblink files
   docs/examples/*.nblink
   
   # But do commit the generator
   !generate_nblinks.py

Then generate during build.

Docker Integration
------------------

Build with Linked Notebooks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     kensai-sphinx:latest \
     sh -c "python /project/generate_nblinks.py && \
            sphinx-build -b html /project/docs /project/docs/_build/html"

``docker-compose.yml``:

.. code-block:: yaml

   version: '3.8'
   
   services:
     docs:
       image: kensai-sphinx:latest
       volumes:
         - .:/project
       working_dir: /project
       command: >
         sh -c "python generate_nblinks.py &&
                sphinx-build -b html docs docs/_build/html"

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Build Docs with Linked Notebooks
   
   on:
     push:
       paths:
         - 'examples/**/*.ipynb'
         - 'docs/**'
   
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Generate nblink files
           run: python generate_nblinks.py
         
         - name: Build Documentation
           run: |
             docker run --rm -v $(pwd):/project \
               kensai-sphinx:latest \
               sphinx-build -b html /project/docs /project/docs/_build/html
         
         - name: Deploy
           uses: peaceiris/actions-gh-pages@v3
           with:
             github_token: ${{ secrets.GITHUB_TOKEN }}
             publish_dir: ./docs/_build/html

Best Practices
--------------

1. **Keep Notebooks with Code**
   
   Store examples near source code

2. **Automate Link Generation**
   
   Don't manually create .nblink files

3. **Use Relative Paths**
   
   More portable than absolute paths

4. **Version Control**
   
   Commit notebooks, optionally commit .nblink

5. **Test Links**
   
   Ensure paths are correct

6. **Organize by Category**
   
   Mirror notebook structure in docs

Troubleshooting
---------------

Notebook Not Found
~~~~~~~~~~~~~~~~~~

**Solution:**

Check path in .nblink file:

.. code-block:: bash

   # From docs/examples/tutorial.nblink location
   ls ../../examples/tutorial.ipynb

File Not Rendered
~~~~~~~~~~~~~~~~~

**Solution:**

Ensure .nblink extension is configured:

.. code-block:: python

   source_suffix = {
       '.nblink': 'nbsphinx-link',
   }

Path Resolution Error
~~~~~~~~~~~~~~~~~~~~~

**Solution:**

Use path relative to .nblink file, not to conf.py:

.. code-block:: json

   {
       "path": "../../examples/notebook.ipynb"
   }

Links Not Generated
~~~~~~~~~~~~~~~~~~~

**Solution:**

Run generator before build:

.. code-block:: bash

   python generate_nblinks.py
   sphinx-build -b html docs docs/_build/html

Next Steps
----------

1. Organize notebooks outside docs
2. Create .nblink files
3. Add to toctree
4. Automate link generation
5. Test documentation build

Additional Resources
--------------------

- :doc:`nbsphinx` - Jupyter Notebook integration
- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `nbsphinx-link Repository <https://github.com/vidartf/nbsphinx-link>`_
- `nbsphinx Documentation <https://nbsphinx.readthedocs.io/>`_
