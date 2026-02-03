rst-pypi-ref Tutorial
======================

.. note::

   **Package Resources:**

   - `PyPI Package <https://pypi.org/project/rst-pypi-ref/>`_
   - `API Documentation <../../pdoc/rst_pypi_ref/index.html>`_
   - `Manual <https://github.com/attakei-lab/rst-pypi-ref>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial introduces rst-pypi-ref, a reStructuredText role for linking to PyPI projects.

What is rst-pypi-ref?
---------------------
rst-pypi-ref provides a ``:pypi:`` role (and Sphinx integration) for fast links to PyPI packages.

Installation
------------

Install via pip:

.. code-block:: bash

   pip install rst-pypi-ref

Configuration
-------------

Enable the extension in ``conf.py``:

.. code-block:: python

   extensions = [
       "rst_pypi_ref.sphinx",
   ]

Basic Usage
-----------

Use the role in reStructuredText:

.. code-block:: restructuredtext

   See :pypi:`sphinx-readme` for details.

Advanced Features
-----------------

- Pin versions: ``:pypi:`package==1.2.3```.
- Customize link text: ``:pypi:`PyPI <package>```.

Examples
--------

.. code-block:: restructuredtext

   Dependency: :pypi:`sphinx-graphql`.

Additional Resources
--------------------

- `Manual <https://github.com/attakei-lab/rst-pypi-ref>`_
- `PyPI <https://pypi.org/project/rst-pypi-ref/>`_
- `API Documentation <../../pdoc/rst_pypi_ref/index.html>`_
