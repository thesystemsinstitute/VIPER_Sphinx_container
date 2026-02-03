Sphinx Gherkindoc Tutorial
==========================

.. note::

   **Package Resources:**

   - `PyPI Package <https://pypi.org/project/sphinx-gherkindoc/>`_
   - `API Documentation <../../pdoc/sphinx_gherkindoc/index.html>`_
   - `Manual <https://jolly-good-toolbelt.github.io/sphinx_gherkindoc/>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial covers sphinx-gherkindoc, a tool that converts Gherkin feature files into Sphinx-ready reStructuredText.

What is Sphinx Gherkindoc?
--------------------------
Sphinx Gherkindoc scans a directory of ``.feature`` files and generates rST files you can include in your Sphinx build.

Installation
------------

Install via pip:

.. code-block:: bash

   pip install sphinx-gherkindoc

Configuration
-------------

Choose a source directory for your features and an output directory for generated rST.

Basic Usage
-----------

Generate rST files from Gherkin features:

.. code-block:: bash

   sphinx-gherkindoc features docs/_docs

Advanced Features
-----------------

- Generate a step glossary with ``-G``.
- Exclude directories with ``--exclude`` patterns.

Examples
--------

Generate a step glossary:

.. code-block:: bash

   sphinx-gherkindoc -G step_glossary features docs/_docs

Additional Resources
--------------------

- `Manual <https://jolly-good-toolbelt.github.io/sphinx_gherkindoc/>`_
- `PyPI <https://pypi.org/project/sphinx-gherkindoc/>`_
- `API Documentation <../../pdoc/sphinx_gherkindoc/index.html>`_
