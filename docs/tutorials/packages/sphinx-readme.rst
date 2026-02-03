Sphinx README Tutorial
======================

.. note::

   **Package Resources:**

   - `PyPI Package <https://pypi.org/project/sphinx-readme/>`_
   - `API Documentation <../../pdoc/sphinx_readme/index.html>`_
   - `Manual <https://sphinx-readme.readthedocs.io/en/latest/>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial explains how to use sphinx-readme to generate a rich ``README.rst`` from Sphinx sources.

What is Sphinx README?
----------------------
Sphinx README parses Sphinx source files and emits a ``README.rst`` that renders well on PyPI and code hosts.

Installation
------------

Install via pip:

.. code-block:: bash

   pip install sphinx-readme

Configuration
-------------

Enable the extension and configure the output in ``conf.py``:

.. code-block:: python

   extensions = [
       "sphinx_readme",
   ]

   readme_src_files = "index.rst"
   readme_out_dir = "."

Basic Usage
-----------

Build the README:

.. code-block:: bash

   sphinx-build -b readme docs docs/_build/readme

This generates a ``README.rst`` file that renders well on PyPI and GitHub.

Advanced Features
-----------------

- Configure ``readme_docs_url_type`` to link to HTML or source.
- Control which files are converted with ``readme_src_files``.
- Automatic badge generation.
- Cross-reference resolution for PyPI.
- Image path conversion.
- Code block preservation.

Configuration Options
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py

   extensions = [
       "sphinx_readme",
   ]

   # README source and output configuration
   readme_src_files = "index.rst"           # Source file(s) to convert
   readme_out_dir = "."                     # Output directory for README.rst

   # URL configuration for links
   readme_docs_url_type = "html"            # 'html', 'code', or 'raw'
   readme_docs_url = "https://myproject.readthedocs.io/en/latest/"

   # Badge configuration
   readme_badges = [
       {
           "image": "https://img.shields.io/pypi/v/myproject.svg",
           "target": "https://pypi.org/project/myproject/",
           "alt": "PyPI version",
       },
       {
           "image": "https://readthedocs.org/projects/myproject/badge/?version=latest",
           "target": "https://myproject.readthedocs.io/en/latest/",
           "alt": "Documentation Status",
       },
   ]

   # Content options
   readme_include_toc = False               # Include table of contents
   readme_raw_directive = "raw-readme"      # Directive for README-only content

Examples
--------

Basic README Generation
~~~~~~~~~~~~~~~~~~~~~~~

Minimal configuration:

.. code-block:: python

   # conf.py

   extensions = ["sphinx_readme"]

   readme_src_files = "index.rst"
   readme_out_dir = ".."  # Project root

Build:

.. code-block:: bash

   sphinx-build -b readme docs docs/_build/readme

   # README.rst is created in project root

Multi-File README
~~~~~~~~~~~~~~~~~

Combine multiple source files:

.. code-block:: python

   # conf.py

   extensions = ["sphinx_readme"]

   readme_src_files = [
       "index.rst",
       "installation.rst",
       "quickstart.rst",
   ]
   readme_out_dir = ".."

The files are concatenated in order to create a comprehensive README.

Documentation Links
~~~~~~~~~~~~~~~~~~~

Configure how links are generated:

.. code-block:: python

   # conf.py

   extensions = ["sphinx_readme"]

   readme_src_files = "index.rst"
   readme_out_dir = ".."

   # Link to hosted HTML documentation
   readme_docs_url_type = "html"
   readme_docs_url = "https://myproject.readthedocs.io/en/latest/"

   # Or link to source files on GitHub
   # readme_docs_url_type = "code"
   # readme_docs_url = "https://github.com/user/myproject/blob/main/docs/"

Links in the source RST:

.. code-block:: restructuredtext

   See the :doc:`installation` guide for details.

   Check :ref:`advanced-configuration` for more options.

Are converted to:

.. code-block:: restructuredtext

   See the `installation <https://myproject.readthedocs.io/en/latest/installation.html>`_ guide for details.

   Check `advanced-configuration <https://myproject.readthedocs.io/en/latest/configuration.html#advanced-configuration>`_ for more options.

Adding Badges
~~~~~~~~~~~~~

Add status badges to your README:

.. code-block:: python

   # conf.py

   extensions = ["sphinx_readme"]

   readme_src_files = "index.rst"
   readme_out_dir = ".."

   readme_badges = [
       # PyPI version
       {
           "image": "https://img.shields.io/pypi/v/myproject.svg",
           "target": "https://pypi.org/project/myproject/",
           "alt": "PyPI version",
       },
       # Build status
       {
           "image": "https://github.com/user/myproject/actions/workflows/test.yml/badge.svg",
           "target": "https://github.com/user/myproject/actions/workflows/test.yml",
           "alt": "Build Status",
       },
       # Documentation
       {
           "image": "https://readthedocs.org/projects/myproject/badge/?version=latest",
           "target": "https://myproject.readthedocs.io/",
           "alt": "Documentation Status",
       },
       # License
       {
           "image": "https://img.shields.io/pypi/l/myproject.svg",
           "target": "https://github.com/user/myproject/blob/main/LICENSE",
           "alt": "License",
       },
       # Python versions
       {
           "image": "https://img.shields.io/pypi/pyversions/myproject.svg",
           "target": "https://pypi.org/project/myproject/",
           "alt": "Python Versions",
       },
   ]

README-Only Content
~~~~~~~~~~~~~~~~~~~

Include content only in the README:

.. code-block:: restructuredtext

   Welcome to MyProject
   ====================

   .. raw-readme::

      .. note::

         This note appears only in the README, not in the HTML docs.

         **Quick Install:**

         .. code-block:: bash

            pip install myproject

   Introduction
   ------------

   MyProject is a powerful tool for...

Content Exclusion
~~~~~~~~~~~~~~~~~

Exclude content from the README:

.. code-block:: restructuredtext

   API Reference
   =============

   .. only:: not readme

      .. toctree::
         :maxdepth: 2

         api/module1
         api/module2
         api/module3

   .. only:: readme

      For detailed API documentation, see the
      `online documentation <https://myproject.readthedocs.io/en/latest/api/>`_.

Complete Project Setup
~~~~~~~~~~~~~~~~~~~~~~

**Project structure:**

.. code-block:: text

   myproject/
   ├── pyproject.toml
   ├── README.rst          # Generated by sphinx-readme
   ├── src/
   │   └── myproject/
   │       └── __init__.py
   └── docs/
       ├── conf.py
       ├── index.rst        # Source for README
       ├── installation.rst
       ├── quickstart.rst
       └── api/
           └── index.rst

**docs/conf.py:**

.. code-block:: python

   project = "MyProject"
   author = "Your Name"
   release = "1.0.0"

   extensions = [
       "sphinx.ext.autodoc",
       "sphinx.ext.napoleon",
       "sphinx_readme",
   ]

   # README configuration
   readme_src_files = ["index.rst", "installation.rst"]
   readme_out_dir = ".."
   readme_docs_url_type = "html"
   readme_docs_url = "https://myproject.readthedocs.io/en/latest/"

   readme_badges = [
       {
           "image": "https://img.shields.io/pypi/v/myproject.svg",
           "target": "https://pypi.org/project/myproject/",
           "alt": "PyPI version",
       },
       {
           "image": "https://readthedocs.org/projects/myproject/badge/",
           "target": "https://myproject.readthedocs.io/",
           "alt": "Documentation",
       },
   ]

**docs/index.rst:**

.. code-block:: restructuredtext

   MyProject
   =========

   .. raw-readme::

      |pypi| |docs| |license|

      .. |pypi| image:: https://img.shields.io/pypi/v/myproject.svg
         :target: https://pypi.org/project/myproject/
      .. |docs| image:: https://readthedocs.org/projects/myproject/badge/
         :target: https://myproject.readthedocs.io/
      .. |license| image:: https://img.shields.io/pypi/l/myproject.svg
         :target: https://github.com/user/myproject/blob/main/LICENSE

   MyProject is a Python library for doing amazing things.

   Features
   --------

   - Feature one with great benefits
   - Feature two for power users
   - Feature three for automation

   Quick Start
   -----------

   Install with pip:

   .. code-block:: bash

      pip install myproject

   Basic usage:

   .. code-block:: python

      from myproject import amazing_function

      result = amazing_function("input")
      print(result)

   .. only:: not readme

      .. toctree::
         :maxdepth: 2

         installation
         quickstart
         api/index

   .. only:: readme

      Documentation
      -------------

      Full documentation is available at https://myproject.readthedocs.io/

Makefile Integration
~~~~~~~~~~~~~~~~~~~~

.. code-block:: makefile

   # Makefile

   .PHONY: readme html clean

   readme:
   	sphinx-build -b readme docs docs/_build/readme

   html:
   	sphinx-build -b html docs docs/_build/html

   # Build README before publishing
   publish: readme
   	python -m build
   	twine upload dist/*

   clean:
   	rm -rf docs/_build

CI/CD Integration
~~~~~~~~~~~~~~~~~

Keep README in sync with documentation:

.. code-block:: yaml

   # .github/workflows/readme.yml
   name: Update README

   on:
     push:
       branches: [main]
       paths:
         - 'docs/**'

   jobs:
     update-readme:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v4

         - name: Set up Python
           uses: actions/setup-python@v5
           with:
             python-version: '3.11'

         - name: Install dependencies
           run: pip install sphinx sphinx-readme

         - name: Generate README
           run: sphinx-build -b readme docs docs/_build/readme

         - name: Commit README
           run: |
             git config user.name "GitHub Actions"
             git config user.email "actions@github.com"
             git add README.rst
             git diff --cached --quiet || git commit -m "Update README from docs"
             git push

Additional Resources
--------------------

- `Manual <https://sphinx-readme.readthedocs.io/en/latest/>`_
- `PyPI <https://pypi.org/project/sphinx-readme/>`_
- `API Documentation <../../pdoc/sphinx_readme/index.html>`_
