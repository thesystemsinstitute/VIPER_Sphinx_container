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

Advanced Features
-----------------

- Configure ``readme_docs_url_type`` to link to HTML or source.
- Control which files are converted with ``readme_src_files``.

Examples
--------

Generate a ``README.rst`` at the project root:

.. code-block:: python

   readme_src_files = ["index.rst", "quick-reference.rst"]
   readme_out_dir = ".."

Additional Resources
--------------------

- `Manual <https://sphinx-readme.readthedocs.io/en/latest/>`_
- `PyPI <https://pypi.org/project/sphinx-readme/>`_
- `API Documentation <../../pdoc/sphinx_readme/index.html>`_
