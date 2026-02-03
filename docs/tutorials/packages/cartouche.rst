Cartouche Tutorial
==================

.. note::

   **Package Resources:**

   - `PyPI Package <https://pypi.org/project/cartouche/>`_
   - `API Documentation <../../pdoc/cartouche/index.html>`_
   - `Manual <https://github.com/rob-smallshire/cartouche>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial covers cartouche, a Sphinx extension that converts lightweight docstring formats into reStructuredText.

What is Cartouche?
------------------
Cartouche transforms readable docstrings into Sphinx-friendly markup, keeping docstrings IDE-friendly while still rich in Sphinx.

Installation
------------

Install via pip:

.. code-block:: bash

   pip install cartouche

Configuration
-------------

Enable the extension in ``conf.py``:

.. code-block:: python

   extensions = [
       "cartouche",
   ]

Basic Usage
-----------

Write concise docstrings and let Cartouche render them during the Sphinx build.

Advanced Features
-----------------

- Keep docstrings readable for introspection tools.
- Use standard Sphinx directives after transformation.

Examples
--------

Docstring example (source before Sphinx rendering):

.. code-block:: python

   def example(a, b):
       """Summary line.

       Args:
           a: First value.
           b: Second value.
       """
       return a + b

Additional Resources
--------------------

- `Manual <https://github.com/rob-smallshire/cartouche>`_
- `PyPI <https://pypi.org/project/cartouche/>`_
- `API Documentation <../../pdoc/cartouche/index.html>`_
