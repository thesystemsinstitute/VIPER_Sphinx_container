nbsphinx-link Tutorial
======================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/nbsphinx-link/>`_
   - `API Documentation <../../pdoc/nbsphinx_link/index.html>`_
   - `Manual <https://nbsphinx-link.readthedocs.io/>`_

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

   docker run --rm viper-sphinx:latest python -c "import nbsphinx_link; print('Installed')"

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
     viper-sphinx:latest \
     sh -c "python /project/generate_nblinks.py && \
            sphinx-build -b html /project/docs /project/docs/_build/html"

``docker-compose.yml``:

.. code-block:: yaml

   version: '3.8'
   
   services:
     docs:
       image: viper-sphinx:latest
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
               viper-sphinx:latest \
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


Practical Examples
------------------

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

.. code-block:: text

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

.. code-block:: text

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


Practical Examples
------------------

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

.. code-block:: text

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

.. code-block:: text

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


Practical Examples
------------------

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

.. code-block:: text

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

.. code-block:: text

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

Additional Resources
--------------------
- :doc:`nbsphinx` - Jupyter Notebook integration
- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `nbsphinx-link Repository <https://github.com/vidartf/nbsphinx-link>`_
- `nbsphinx Documentation <https://nbsphinx.readthedocs.io/>`_
- GitHub repository: https://github.com/vidartf/nbsphinx-link

