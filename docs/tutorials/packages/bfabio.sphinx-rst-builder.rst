bfabio.sphinx-rst-builder Tutorial
=====================================

.. note::

   **Package Resources:**

   - `PyPI Package <https://pypi.org/project/bfabio.sphinx-rst-builder/>`_
   - `API Documentation <../../pdoc/bfabio_sphinx_rst_builder/index.html>`_
   - `Manual <https://github.com/bfabio/sphinx-rst-builder>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial explains the reStructuredText builder extension for Sphinx.

What is bfabio.sphinx-rst-builder?
---------------------------------
This package provides a Sphinx builder that outputs reStructuredText files.

Installation
------------

Install via pip:

.. code-block:: bash

   pip install bfabio.sphinx-rst-builder

Configuration
-------------

Enable the extension in ``conf.py``:

.. code-block:: python

   extensions = [
       "sphinx_rst_builder",
   ]

Basic Usage
-----------

Build the ``rst`` output:

.. code-block:: bash

   sphinx-build -b rst docs docs/_build/rst

Advanced Features
-----------------

- Customize output suffixes with ``rst_file_suffix``.
- Adjust link suffixes with ``rst_link_suffix``.

Examples
--------

.. code-block:: python

   rst_file_suffix = ".rst"
   rst_link_suffix = ".rst"

Additional Resources
--------------------

- `Manual <https://github.com/bfabio/sphinx-rst-builder>`_
- `PyPI <https://pypi.org/project/bfabio.sphinx-rst-builder/>`_
- `API Documentation <../../pdoc/bfabio_sphinx_rst_builder/index.html>`_
