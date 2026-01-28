nbsphinx-link Example
=====================

This page demonstrates the **nbsphinx-link** extension for linking to notebooks outside the Sphinx source directory.

.. contents:: Contents
   :local:
   :depth: 2

Overview
--------

The nbsphinx-link extension allows you to include Jupyter notebooks that are stored outside your documentation source directory, which is useful for keeping examples with source code while including them in documentation.

Basic Usage
-----------

Configuration
~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   extensions = [
       'nbsphinx',
       'nbsphinx_link',
   ]

Link File Format
~~~~~~~~~~~~~~~~

Create a ``.nblink`` file pointing to an external notebook:

.. code-block:: json

   {
       "path": "../examples/example.ipynb"
   }

Save as ``docs/notebooks/example.nblink``.

File Paths
----------

Relative Paths
~~~~~~~~~~~~~~

Link to file relative to ``.nblink`` location:

.. code-block:: json

   {
       "path": "../../src/examples/tutorial.ipynb"
   }

Absolute Paths
~~~~~~~~~~~~~~

Use absolute paths (less portable):

.. code-block:: json

   {
       "path": "/home/user/project/notebooks/demo.ipynb"
   }

Repository Structure
~~~~~~~~~~~~~~~~~~~~

Recommended structure:

.. code-block:: text

   project/
   ├── docs/
   │   ├── conf.py
   │   ├── index.rst
   │   └── notebooks/
   │       ├── tutorial.nblink
   │       └── examples.nblink
   ├── src/
   │   └── mypackage/
   │       └── __init__.py
   └── examples/
       ├── tutorial.ipynb
       └── examples.ipynb

Including Linked Notebooks
---------------------------

In Toctree
~~~~~~~~~~

.. code-block:: rst

   .. toctree::
      :maxdepth: 2
   
      intro.rst
      notebooks/tutorial.nblink
      notebooks/examples.nblink
      api.rst

Direct Reference
~~~~~~~~~~~~~~~~

.. code-block:: rst

   See the tutorial: :doc:`notebooks/tutorial.nblink`

Advanced Configuration
----------------------

Custom Extra Files
~~~~~~~~~~~~~~~~~~

Copy additional files when building:

.. code-block:: json

   {
       "path": "../../examples/tutorial.ipynb",
       "extra-media": [
           "../../examples/data/image.png",
           "../../examples/data/dataset.csv"
       ]
   }

Environment Variables
~~~~~~~~~~~~~~~~~~~~~

Use environment variables in paths:

.. code-block:: json

   {
       "path": "${PROJECT_ROOT}/examples/notebook.ipynb"
   }

Multiple Links
--------------

Create Multiple .nblink Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text

   docs/notebooks/
   ├── getting_started.nblink
   ├── advanced_usage.nblink
   ├── api_examples.nblink
   └── custom_examples.nblink

Getting Started Link
^^^^^^^^^^^^^^^^^^^^

.. code-block:: json

   {
       "path": "../../examples/getting_started.ipynb"
   }

Advanced Usage Link
^^^^^^^^^^^^^^^^^^^

.. code-block:: json

   {
       "path": "../../examples/advanced_usage.ipynb"
   }

Practical Examples
------------------

Package Documentation
~~~~~~~~~~~~~~~~~~~~~

Structure for documenting a package:

.. code-block:: text

   mypackage/
   ├── mypackage/
   │   ├── __init__.py
   │   └── core.py
   ├── examples/
   │   ├── basic_usage.ipynb
   │   ├── advanced_features.ipynb
   │   └── data/
   │       └── sample.csv
   └── docs/
       ├── conf.py
       ├── index.rst
       └── examples/
           ├── basic.nblink
           └── advanced.nblink

Basic Example Link
^^^^^^^^^^^^^^^^^^

``docs/examples/basic.nblink``:

.. code-block:: json

   {
       "path": "../../examples/basic_usage.ipynb"
   }

Advanced Example Link
^^^^^^^^^^^^^^^^^^^^^

``docs/examples/advanced.nblink``:

.. code-block:: json

   {
       "path": "../../examples/advanced_features.ipynb",
       "extra-media": [
           "../../examples/data/sample.csv"
       ]
   }

Documentation Index
^^^^^^^^^^^^^^^^^^^

``docs/index.rst``:

.. code-block:: rst

   Welcome to MyPackage
   ====================
   
   .. toctree::
      :maxdepth: 2
      :caption: Examples
   
      examples/basic.nblink
      examples/advanced.nblink

Integration with Source Code
-----------------------------

Keep Examples with Code
~~~~~~~~~~~~~~~~~~~~~~~~

Store notebooks alongside source:

.. code-block:: text

   src/
   ├── mypackage/
   │   ├── __init__.py
   │   ├── module1/
   │   │   ├── __init__.py
   │   │   ├── core.py
   │   │   └── examples/
   │   │       └── module1_demo.ipynb
   │   └── module2/
   │       ├── __init__.py
   │       ├── api.py
   │       └── examples/
   │           └── module2_demo.ipynb
   └── docs/
       └── examples/
           ├── module1.nblink
           └── module2.nblink

Link Configuration
~~~~~~~~~~~~~~~~~~

``docs/examples/module1.nblink``:

.. code-block:: json

   {
       "path": "../../src/mypackage/module1/examples/module1_demo.ipynb"
   }

Automated Link Generation
--------------------------

Python Script
~~~~~~~~~~~~~

Generate ``.nblink`` files automatically:

.. code-block:: python

   # generate_links.py
   import json
   from pathlib import Path

   def create_nblink(notebook_path, link_path):
       """Create an nblink file."""
       link_data = {
           "path": str(notebook_path)
       }
       
       with open(link_path, 'w') as f:
           json.dump(link_data, f, indent=2)

   # Find all notebooks in examples/
   examples_dir = Path('../examples')
   docs_dir = Path('docs/notebooks')
   docs_dir.mkdir(exist_ok=True)

   for nb in examples_dir.glob('**/*.ipynb'):
       if '.ipynb_checkpoints' not in str(nb):
           rel_path = nb.relative_to(Path.cwd())
           link_name = nb.stem + '.nblink'
           link_path = docs_dir / link_name
           create_nblink(f'../../{rel_path}', link_path)
           print(f'Created: {link_path}')

Make Task
~~~~~~~~~

Add to ``Makefile``:

.. code-block:: makefile

   .PHONY: generate-links
   generate-links:
       python generate_links.py

   html: generate-links
       sphinx-build -b html docs docs/_build/html

Version Control
---------------

Git Configuration
~~~~~~~~~~~~~~~~~

.. code-block:: gitignore

   # .gitignore
   
   # Include nblink files
   !*.nblink
   
   # But exclude notebook checkpoints
   **/.ipynb_checkpoints/

Track Links
~~~~~~~~~~~

Keep ``.nblink`` files in version control:

.. code-block:: bash

   git add docs/examples/*.nblink
   git commit -m "Add notebook links"

External Notebooks
~~~~~~~~~~~~~~~~~~

``.gitignore`` for local development:

.. code-block:: gitignore

   # Development notebooks (not tracked)
   dev_notebooks/
   
   # But keep the links
   !docs/dev/*.nblink

Build Integration
-----------------

Read the Docs
~~~~~~~~~~~~~

.. code-block:: yaml

   # .readthedocs.yaml
   version: 2
   
   build:
     os: ubuntu-22.04
     tools:
       python: "3.11"
   
   sphinx:
     configuration: docs/conf.py
   
   python:
     install:
       - requirements: docs/requirements.txt

Requirements File
~~~~~~~~~~~~~~~~~

.. code-block:: text

   # docs/requirements.txt
   nbsphinx>=0.8.0
   nbsphinx-link>=1.3.0
   jupyter
   ipykernel

CI/CD Pipeline
~~~~~~~~~~~~~~

.. code-block:: yaml

   # .github/workflows/docs.yml
   name: Documentation
   
   on: [push, pull_request]
   
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v2
         
         - name: Set up Python
           uses: actions/setup-python@v2
           with:
             python-version: '3.11'
         
         - name: Install dependencies
           run: |
             pip install -r docs/requirements.txt
         
         - name: Generate links
           run: |
             python generate_links.py
         
         - name: Build docs
           run: |
             cd docs
             make html

Troubleshooting
---------------

Path Issues
~~~~~~~~~~~

Debug path resolution:

.. code-block:: python

   # Add to conf.py
   import os
   print(f"Current dir: {os.getcwd()}")
   
   # Verify paths in .nblink files
   import json
   from pathlib import Path
   
   link_file = Path('notebooks/example.nblink')
   if link_file.exists():
       with open(link_file) as f:
           data = json.load(f)
           nb_path = Path(link_file.parent) / data['path']
           print(f"Notebook path: {nb_path.resolve()}")
           print(f"Exists: {nb_path.exists()}")

Missing Notebooks
~~~~~~~~~~~~~~~~~

Check for missing files during build:

.. code-block:: python

   # In conf.py
   def check_nblinks(app, env, docnames):
       """Check all nblink files."""
       from pathlib import Path
       import json
       
       for docname in docnames:
           if docname.endswith('.nblink'):
               link_file = Path(env.srcdir) / f'{docname}'
               with open(link_file) as f:
                   data = json.load(f)
                   nb_path = link_file.parent / data['path']
                   if not nb_path.exists():
                       print(f"WARNING: {nb_path} not found")

   def setup(app):
       app.connect('env-before-read-docs', check_nblinks)

Best Practices
--------------

Organization
~~~~~~~~~~~~

1. Keep notebooks with relevant code
2. Use consistent naming for ``.nblink`` files
3. Document path structure in README
4. Automate link generation when possible

Maintenance
~~~~~~~~~~~

1. Verify links during builds
2. Update paths when refactoring
3. Keep notebook outputs cleared in version control
4. Use relative paths for portability

Documentation
~~~~~~~~~~~~~

1. Explain external notebook locations
2. Document how to regenerate links
3. Provide examples of link usage
4. Include troubleshooting guide

See Also
--------

- :doc:`../tutorials/packages/nbsphinx-link` - Complete tutorial
- :doc:`nbsphinx-example` - nbsphinx extension
- GitHub repository: https://github.com/vidartf/nbsphinx-link
