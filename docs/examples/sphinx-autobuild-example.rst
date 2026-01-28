Sphinx-Autobuild Example
========================

This page demonstrates the **sphinx-autobuild** extension for automatically rebuilding Sphinx documentation when files change.

.. contents:: Contents
   :local:
   :depth: 2


Basic Usage
-----------

Command Line
~~~~~~~~~~~~

Start the auto-build server:

.. code-block:: bash

   sphinx-autobuild docs docs/_build/html

With specific host and port:

.. code-block:: bash

   sphinx-autobuild docs docs/_build/html --host 0.0.0.0 --port 8080

Open in Browser
~~~~~~~~~~~~~~~

.. code-block:: bash

   # Auto-open browser
   sphinx-autobuild docs docs/_build/html --open-browser

Watch Options
-------------

Ignore Patterns
~~~~~~~~~~~~~~~

Ignore specific files or directories:

.. code-block:: bash

   sphinx-autobuild docs docs/_build/html \
       --ignore "*.swp" \
       --ignore "*.tmp" \
       --ignore "*~"

Watch Additional Files
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Watch additional directories
   sphinx-autobuild docs docs/_build/html \
       --watch ../src \
       --watch ../README.md

Re-read Patterns
~~~~~~~~~~~~~~~~

Force rebuild when specific files change:

.. code-block:: bash

   sphinx-autobuild docs docs/_build/html \
       --re-ignore ".*\.git.*" \
       --re-ignore ".*\.tox.*"

Build Options
-------------

Custom Builder
~~~~~~~~~~~~~~

Use different Sphinx builders:

.. code-block:: bash

   # HTML builder (default)
   sphinx-autobuild docs docs/_build/html

   # LaTeX builder
   sphinx-autobuild docs docs/_build/latex -b latex

   # Dirhtml builder
   sphinx-autobuild docs docs/_build/dirhtml -b dirhtml

Parallel Builds
~~~~~~~~~~~~~~~

.. code-block:: bash

   # Use multiple processes
   sphinx-autobuild docs docs/_build/html -j 4

Clean Build
~~~~~~~~~~~

.. code-block:: bash

   # Clean before building
   sphinx-autobuild docs docs/_build/html --clean

Server Configuration
--------------------

Custom Host and Port
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Bind to specific interface
   sphinx-autobuild docs docs/_build/html \
       --host 127.0.0.1 \
       --port 8000

Network Access
~~~~~~~~~~~~~~

.. code-block:: bash

   # Allow network access
   sphinx-autobuild docs docs/_build/html \
       --host 0.0.0.0 \
       --port 8080

Custom Paths
~~~~~~~~~~~~

.. code-block:: bash

   # Serve from subdirectory
   sphinx-autobuild docs docs/_build/html \
       --url-prefix /docs/

Delay and Debouncing
--------------------

Build Delay
~~~~~~~~~~~

.. code-block:: bash

   # Wait before rebuilding (milliseconds)
   sphinx-autobuild docs docs/_build/html --delay 2000

Debounce
~~~~~~~~

.. code-block:: bash

   # Debounce file changes
   sphinx-autobuild docs docs/_build/html --debounce 1000

Advanced Features
-----------------

Pre-build Commands
~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Run command before build
   sphinx-autobuild docs docs/_build/html \
       --pre-build "echo 'Starting build...'"

Multiple Watch Directories
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   sphinx-autobuild docs docs/_build/html \
       --watch docs \
       --watch ../source_code \
       --watch ../config.yaml

Ignore Build Directory
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Prevent watching build output
   sphinx-autobuild docs docs/_build/html \
       --ignore "docs/_build/*"

Development Workflow
--------------------

Basic Workflow
~~~~~~~~~~~~~~

.. code-block:: bash

   # Start development server
   sphinx-autobuild docs docs/_build/html
   
   # Edit files in docs/
   # Browser auto-refreshes on save

With Editor
~~~~~~~~~~~

Configure your editor to work with autobuild:

.. code-block:: bash

   # VS Code: Save on focus change
   # Sublime Text: Save on deactivated
   
   sphinx-autobuild docs docs/_build/html --delay 500

Multi-Language
~~~~~~~~~~~~~~

.. code-block:: bash

   # Watch translation files
   sphinx-autobuild docs docs/_build/html \
       --watch docs/locale/

Integration Examples
--------------------

Make Task
~~~~~~~~~

Add to ``Makefile``:

.. code-block:: makefile

   .PHONY: livehtml
   livehtml:
       sphinx-autobuild "$(SOURCEDIR)" "$(BUILDDIR)/html" \
           --port 8000 \
           --open-browser

npm Script
~~~~~~~~~~

Add to ``package.json``:

.. code-block:: json

   {
       "scripts": {
           "docs:dev": "sphinx-autobuild docs docs/_build/html",
           "docs:serve": "sphinx-autobuild docs docs/_build/html --port 8080 --open-browser"
       }
   }

Python Script
~~~~~~~~~~~~~

.. code-block:: python

   # build_docs.py
   import subprocess
   import sys

   def watch_docs():
       """Start sphinx-autobuild server."""
       cmd = [
           "sphinx-autobuild",
           "docs",
           "docs/_build/html",
           "--port", "8000",
           "--open-browser",
       ]
       subprocess.run(cmd, check=True)

   if __name__ == "__main__":
       watch_docs()

Docker Integration
------------------

Dockerfile
~~~~~~~~~~

.. code-block:: dockerfile

   FROM python:3.11-slim
   
   WORKDIR /docs
   
   RUN pip install sphinx sphinx-autobuild sphinx-rtd-theme
   
   EXPOSE 8000
   
   CMD ["sphinx-autobuild", ".", "_build/html", \
        "--host", "0.0.0.0", "--port", "8000"]

Docker Compose
~~~~~~~~~~~~~~

.. code-block:: yaml

   version: '3.8'
   
   services:
     sphinx:
       build: .
       ports:
         - "8000:8000"
       volumes:
         - ./docs:/docs
       command: >
         sphinx-autobuild docs docs/_build/html
         --host 0.0.0.0
         --port 8000
         --watch docs

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Documentation
   
   on:
     push:
       paths:
         - 'docs/**'
   
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
             pip install sphinx sphinx-autobuild
         
         - name: Build docs
           run: |
             sphinx-build docs docs/_build/html

GitLab CI
~~~~~~~~~

.. code-block:: yaml

   docs:
     image: python:3.11
     script:
       - pip install sphinx sphinx-autobuild
       - sphinx-build docs docs/_build/html
     artifacts:
       paths:
         - docs/_build/html

Troubleshooting
---------------

Port Already in Use
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Use different port
   sphinx-autobuild docs docs/_build/html --port 8001

Build Loops
~~~~~~~~~~~

.. code-block:: bash

   # Ignore build directory
   sphinx-autobuild docs docs/_build/html \
       --ignore "docs/_build/*" \
       --ignore "*.pyc"

Slow Rebuilds
~~~~~~~~~~~~~

.. code-block:: bash

   # Use parallel builds
   sphinx-autobuild docs docs/_build/html -j auto
   
   # Increase delay
   sphinx-autobuild docs docs/_build/html --delay 2000

Configuration File
------------------

pyproject.toml
~~~~~~~~~~~~~~

.. code-block:: toml

   [tool.sphinx-autobuild]
   port = 8000
   host = "127.0.0.1"
   open-browser = true
   delay = 1000
   ignore = [
       "*.swp",
       "*.tmp",
       "*~",
   ]

Command-line Override
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Override config file settings
   sphinx-autobuild docs docs/_build/html \
       --port 9000 \
       --no-open-browser

Best Practices
--------------

Development Setup
~~~~~~~~~~~~~~~~~

1. Use ``--delay`` to avoid excessive rebuilds
2. Ignore temporary files (swp, tmp, pyc)
3. Watch source code for autodoc changes
4. Use ``--open-browser`` for convenience

Production Build
~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Development
   sphinx-autobuild docs docs/_build/html
   
   # Production
   sphinx-build docs docs/_build/html

Performance Tips
~~~~~~~~~~~~~~~~

1. Use parallel builds (``-j auto``)
2. Ignore unnecessary directories
3. Increase debounce time for large projects
4. Use incremental builds when possible

Practical Examples
------------------

Simple Project
~~~~~~~~~~~~~~

.. code-block:: bash

   # Basic auto-build
   sphinx-autobuild docs docs/_build/html

Large Project
~~~~~~~~~~~~~

.. code-block:: bash

   # Optimized for large project
   sphinx-autobuild docs docs/_build/html \
       -j auto \
       --delay 1000 \
       --ignore "*.tmp" \
       --ignore "*.swp" \
       --watch ../src

Multi-Language Project
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Watch translations
   sphinx-autobuild docs docs/_build/html/en \
       --watch docs/locale/ \
       --watch docs/_templates/

API Documentation
~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Watch source code for autodoc
   sphinx-autobuild docs docs/_build/html \
       --watch ../mypackage \
       --pre-build "echo 'Checking API changes...'"

See Also
--------

- :doc:`../tutorials/packages/sphinx-autobuild` - Complete tutorial
- GitHub repository: https://github.com/executablebooks/sphinx-autobuild
