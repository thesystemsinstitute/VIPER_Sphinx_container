Sphinx Icontract Tutorial
=========================

.. note::

   **Package Resources:**

   - `PyPI Package <https://pypi.org/project/sphinx-icontract/>`_
   - `API Documentation <../../pdoc/sphinx_icontract/index.html>`_
   - `Manual <https://github.com/Parquery/sphinx-icontract>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial covers sphinx-icontract, a Sphinx extension that documents icontracts on functions and classes.

What is Sphinx Icontract?
-------------------------
Sphinx Icontract extends ``sphinx.ext.autodoc`` so contract conditions (preconditions, postconditions, invariants) are shown in generated documentation.

Installation
------------

Install via pip:

.. code-block:: bash

   pip install sphinx-icontract

Configuration
-------------

Enable the extension in ``conf.py`` alongside autodoc:

.. code-block:: python

   extensions = [
       "sphinx.ext.autodoc",
       "sphinx_icontract",
   ]

Basic Usage
-----------

Document a module with autodoc; contracts appear in the output automatically.

Advanced Features
-----------------

- Render implications from logical expressions (e.g., ``not A or B`` as $A \Rightarrow B$).
- Include custom error messages in contract descriptions.

Examples
--------

A simple contract example:

.. code-block:: python

   import icontract

   @icontract.require(lambda x: x > 0)
   def square(x: int) -> int:
       return x * x

Additional Resources
--------------------

- `Manual <https://github.com/Parquery/sphinx-icontract>`_
- `PyPI <https://pypi.org/project/sphinx-icontract/>`_
- `API Documentation <../../pdoc/sphinx_icontract/index.html>`_
