Hatch Sphinx Tutorial
======================

.. note::

   **Package Resources:**

   - `PyPI Package <https://pypi.org/project/hatch-sphinx/>`_
   - `API Documentation <../../pdoc/hatch_sphinx/index.html>`_
   - `Manual <https://github.com/llimeht/hatch-sphinx#readme>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial covers hatch-sphinx, a Hatch build hook for running Sphinx during package builds.

What is Hatch Sphinx?
---------------------
Hatch Sphinx is a Hatchling plugin that runs Sphinx (and optional tooling) as part of your build pipeline.

Installation
------------

Install via pip:

.. code-block:: bash

   pip install hatch-sphinx

Configuration
-------------

Add the hook to your ``pyproject.toml``:

.. code-block:: toml

   [build-system]
   requires = ["hatchling", "hatch-sphinx"]
   build-backend = "hatchling.build"

   [[tool.hatch.build.targets.wheel.hooks.sphinx.tools]]
   tool = "build"
   doc_dir = "docs"
   out_dir = "_build"
   format = "html"

Basic Usage
-----------

Build your wheel and let Hatch run Sphinx automatically:

.. code-block:: bash

   hatch build

This runs the configured Sphinx tools as part of the wheel build process.

Advanced Features
-----------------

- Chain multiple tools (e.g., ``apidoc`` then ``build``).
- Use custom commands for pre/post processing.
- Support for multiple output formats.
- Integration with hatch environments.
- Conditional documentation builds.

Configuration Options
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: toml

   # pyproject.toml - Full configuration options

   [build-system]
   requires = ["hatchling", "hatch-sphinx"]
   build-backend = "hatchling.build"

   [tool.hatch.build.targets.wheel.hooks.sphinx]
   # Enable/disable the hook
   enable = true

   # Run Sphinx tools in sequence
   [[tool.hatch.build.targets.wheel.hooks.sphinx.tools]]
   tool = "apidoc"              # sphinx-apidoc
   source = "src/mypackage"     # Source code directory
   out_dir = "docs/api"         # Output directory for .rst files
   exclude = ["**/tests/*"]     # Patterns to exclude
   module_first = true          # Put module documentation first
   separate = true              # Separate pages for each module
   force = true                 # Overwrite existing files

   [[tool.hatch.build.targets.wheel.hooks.sphinx.tools]]
   tool = "build"               # sphinx-build
   doc_dir = "docs"             # Documentation source directory
   out_dir = "docs/_build"      # Build output directory
   format = "html"              # Output format (html, latex, epub, etc.)
   jobs = "auto"                # Parallel build jobs

Examples
--------

Basic Documentation Build
~~~~~~~~~~~~~~~~~~~~~~~~~

Minimal configuration for HTML documentation:

.. code-block:: toml

   # pyproject.toml

   [build-system]
   requires = ["hatchling", "hatch-sphinx"]
   build-backend = "hatchling.build"

   [[tool.hatch.build.targets.wheel.hooks.sphinx.tools]]
   tool = "build"
   doc_dir = "docs"
   out_dir = "docs/_build/html"
   format = "html"

API Documentation Generation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Generate API docs from source code, then build HTML:

.. code-block:: toml

   # pyproject.toml

   [build-system]
   requires = ["hatchling", "hatch-sphinx"]
   build-backend = "hatchling.build"

   # First, generate API documentation
   [[tool.hatch.build.targets.wheel.hooks.sphinx.tools]]
   tool = "apidoc"
   source = "src/mypackage"
   out_dir = "docs/api"
   exclude = ["**/tests/*", "**/conftest.py"]
   module_first = true
   separate = true
   force = true
   implicit_namespaces = true

   # Then, build the documentation
   [[tool.hatch.build.targets.wheel.hooks.sphinx.tools]]
   tool = "build"
   doc_dir = "docs"
   out_dir = "docs/_build/html"
   format = "html"
   jobs = "auto"

Multi-Format Builds
~~~~~~~~~~~~~~~~~~~

Build multiple output formats:

.. code-block:: toml

   # pyproject.toml

   [build-system]
   requires = ["hatchling", "hatch-sphinx"]
   build-backend = "hatchling.build"

   # Generate API docs first
   [[tool.hatch.build.targets.wheel.hooks.sphinx.tools]]
   tool = "apidoc"
   source = "src/mypackage"
   out_dir = "docs/api"

   # Build HTML documentation
   [[tool.hatch.build.targets.wheel.hooks.sphinx.tools]]
   tool = "build"
   doc_dir = "docs"
   out_dir = "docs/_build/html"
   format = "html"

   # Build PDF documentation
   [[tool.hatch.build.targets.wheel.hooks.sphinx.tools]]
   tool = "build"
   doc_dir = "docs"
   out_dir = "docs/_build/latex"
   format = "latexpdf"

   # Build EPUB
   [[tool.hatch.build.targets.wheel.hooks.sphinx.tools]]
   tool = "build"
   doc_dir = "docs"
   out_dir = "docs/_build/epub"
   format = "epub"

Custom Pre-Build Commands
~~~~~~~~~~~~~~~~~~~~~~~~~

Run custom commands before the build:

.. code-block:: toml

   # pyproject.toml

   [build-system]
   requires = ["hatchling", "hatch-sphinx"]
   build-backend = "hatchling.build"

   # Run custom pre-processing
   [[tool.hatch.build.targets.wheel.hooks.sphinx.tools]]
   tool = "command"
   command = "python scripts/generate_changelog.py"

   # Generate API diagrams
   [[tool.hatch.build.targets.wheel.hooks.sphinx.tools]]
   tool = "command"
   command = "pyreverse -o svg -p mypackage src/mypackage -d docs/_static"

   # Generate API docs
   [[tool.hatch.build.targets.wheel.hooks.sphinx.tools]]
   tool = "apidoc"
   source = "src/mypackage"
   out_dir = "docs/api"

   # Build HTML
   [[tool.hatch.build.targets.wheel.hooks.sphinx.tools]]
   tool = "build"
   doc_dir = "docs"
   out_dir = "docs/_build/html"
   format = "html"

Conditional Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~

Only build docs in certain environments:

.. code-block:: toml

   # pyproject.toml

   [build-system]
   requires = ["hatchling", "hatch-sphinx"]
   build-backend = "hatchling.build"

   # Only enable for wheel builds, not sdist
   [tool.hatch.build.targets.wheel.hooks.sphinx]
   enable = true

   [tool.hatch.build.targets.sdist.hooks.sphinx]
   enable = false

   [[tool.hatch.build.targets.wheel.hooks.sphinx.tools]]
   tool = "build"
   doc_dir = "docs"
   out_dir = "docs/_build/html"
   format = "html"

Complete Project Example
~~~~~~~~~~~~~~~~~~~~~~~~

Full project structure with hatch-sphinx:

.. code-block:: text

   mypackage/
   ├── pyproject.toml
   ├── README.md
   ├── src/
   │   └── mypackage/
   │       ├── __init__.py
   │       ├── core.py
   │       └── utils.py
   ├── docs/
   │   ├── conf.py
   │   ├── index.rst
   │   ├── getting-started.rst
   │   └── api/
   │       └── (generated by sphinx-apidoc)
   └── tests/
       └── test_core.py

Complete ``pyproject.toml``:

.. code-block:: toml

   [build-system]
   requires = ["hatchling", "hatch-sphinx", "sphinx", "sphinx-rtd-theme"]
   build-backend = "hatchling.build"

   [project]
   name = "mypackage"
   version = "1.0.0"
   description = "My awesome package"
   readme = "README.md"
   requires-python = ">=3.8"
   authors = [
       { name = "Your Name", email = "you@example.com" }
   ]

   [tool.hatch.build.targets.wheel]
   packages = ["src/mypackage"]

   [[tool.hatch.build.targets.wheel.hooks.sphinx.tools]]
   tool = "apidoc"
   source = "src/mypackage"
   out_dir = "docs/api"
   module_first = true
   separate = true
   force = true

   [[tool.hatch.build.targets.wheel.hooks.sphinx.tools]]
   tool = "build"
   doc_dir = "docs"
   out_dir = "docs/_build/html"
   format = "html"
   jobs = "auto"

   [tool.hatch.envs.docs]
   dependencies = [
       "sphinx",
       "sphinx-rtd-theme",
       "myst-parser",
   ]

   [tool.hatch.envs.docs.scripts]
   build = "sphinx-build -b html docs docs/_build/html"
   serve = "python -m http.server -d docs/_build/html"
   clean = "rm -rf docs/_build docs/api"

Build and verify:

.. code-block:: bash

   # Build wheel with documentation
   hatch build

   # Or use the docs environment
   hatch run docs:build
   hatch run docs:serve

CI/CD Integration
~~~~~~~~~~~~~~~~~

GitHub Actions workflow:

.. code-block:: yaml

   # .github/workflows/build.yml
   name: Build Package

   on:
     push:
       tags: ['v*']

   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v4

         - name: Set up Python
           uses: actions/setup-python@v5
           with:
             python-version: '3.11'

         - name: Install hatch
           run: pip install hatch

         - name: Build package with docs
           run: hatch build

         - name: Upload wheel
           uses: actions/upload-artifact@v4
           with:
             name: wheel
             path: dist/*.whl

Additional Resources
--------------------

- `Manual <https://github.com/llimeht/hatch-sphinx#readme>`_
- `PyPI <https://pypi.org/project/hatch-sphinx/>`_
- `API Documentation <../../pdoc/hatch_sphinx/index.html>`_
