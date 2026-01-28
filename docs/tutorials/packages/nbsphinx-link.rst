nbsphinx-link Tutorial
======================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/nbsphinx-link/>`_
   - :doc:`See Working Example <../../examples/nbsphinx-link-example>`


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

Practical Examples
------------------

Example 1: Project with Examples Directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Project structure:

.. code-block:: text

   myproject/
   ├── mypackage/
   │   ├── __init__.py
   │   └── core.py
   ├── examples/
   │   ├── basic_usage.ipynb
   │   ├── advanced.ipynb
   │   └── data_processing.ipynb
   └── docs/
       ├── conf.py
       ├── index.rst
       └── examples/
           ├── basic_usage.nblink
           ├── advanced.nblink
           └── data_processing.nblink

``docs/examples/basic_usage.nblink``:

.. code-block:: json

   {
       "path": "../../examples/basic_usage.ipynb"
   }

``docs/examples/advanced.nblink``:

.. code-block:: json

   {
       "path": "../../examples/advanced.ipynb"
   }

``docs/index.rst``:

.. code-block:: rst

   Examples
   ========
   
   .. toctree::
      :maxdepth: 1
      
      examples/basic_usage.nblink
      examples/advanced.nblink
      examples/data_processing.nblink

Example 2: Multiple Source Locations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/tutorials/getting-started.nblink``:

.. code-block:: json

   {
       "path": "../../notebooks/tutorials/getting-started.ipynb"
   }

``docs/tutorials/api-usage.nblink``:

.. code-block:: json

   {
       "path": "../../examples/api/usage.ipynb"
   }

``docs/case-studies/analysis.nblink``:

.. code-block:: json

   {
       "path": "../../../case-studies/analysis.ipynb"
   }

Example 3: Automated Link Generation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``generate_nblinks.py``:

.. code-block:: python

   """Generate .nblink files for all notebooks in examples/."""
   
   import json
   import os
   from pathlib import Path
   
   def generate_nblinks(
       source_dir: str = "examples",
       output_dir: str = "docs/examples",
       relative_path: str = "../../examples"
   ):
       """
       Generate .nblink files.
       
       Parameters
       ----------
       source_dir : str
           Directory containing notebooks
       output_dir : str
           Directory for .nblink files
       relative_path : str
           Relative path from output_dir to source_dir
       """
       source_path = Path(source_dir)
       output_path = Path(output_dir)
       output_path.mkdir(parents=True, exist_ok=True)
       
       # Find all notebooks
       notebooks = list(source_path.glob("**/*.ipynb"))
       
       for notebook in notebooks:
           # Skip checkpoints
           if ".ipynb_checkpoints" in str(notebook):
               continue
           
           # Calculate relative path
           rel_notebook = notebook.relative_to(source_path)
           nblink_path = output_path / rel_notebook.with_suffix('.nblink')
           
           # Create parent directories
           nblink_path.parent.mkdir(parents=True, exist_ok=True)
           
           # Generate link
           link_target = f"{relative_path}/{rel_notebook}"
           nblink_content = {
               "path": link_target
           }
           
           # Write .nblink file
           with open(nblink_path, 'w') as f:
               json.dump(nblink_content, f, indent=4)
           
           print(f"Created {nblink_path} -> {link_target}")
   
   if __name__ == '__main__':
       generate_nblinks()

Run to generate links:

.. code-block:: bash

   python generate_nblinks.py

Example 4: Organization by Category
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Project structure:

.. code-block:: text

   project/
   ├── notebooks/
   │   ├── tutorials/
   │   │   ├── beginner.ipynb
   │   │   └── advanced.ipynb
   │   ├── howtos/
   │   │   ├── visualization.ipynb
   │   │   └── optimization.ipynb
   │   └── examples/
   │       ├── example1.ipynb
   │       └── example2.ipynb
   └── docs/
       ├── conf.py
       └── notebooks/
           ├── tutorials/
           │   ├── beginner.nblink
           │   └── advanced.nblink
           ├── howtos/
           │   ├── visualization.nblink
           │   └── optimization.nblink
           └── examples/
               ├── example1.nblink
               └── example2.nblink

``docs/index.rst``:

.. code-block:: rst

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
   
   Examples
   --------
   
   .. toctree::
      :maxdepth: 1
      
      notebooks/examples/example1.nblink
      notebooks/examples/example2.nblink

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
