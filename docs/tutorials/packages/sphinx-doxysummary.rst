Sphinx Doxysummary Tutorial
===========================

.. note::

   **Package Resources:**

   - `PyPI Package <https://pypi.org/project/sphinx-doxysummary/>`_
   - `API Documentation <../../pdoc/sphinx_doxysummary/index.html>`_
   - `Manual <https://doxysummary.readthedocs.io/en/latest/>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial explains sphinx-doxysummary, a Sphinx extension that builds autosummary tables from Doxygen XML.

What is Sphinx Doxysummary?
---------------------------
Sphinx Doxysummary integrates Doxygen XML with Sphinx autosummary-style tables.

Installation
------------

Install via pip:

.. code-block:: bash

   pip install sphinx-doxysummary

Configuration
-------------

Enable the extension and set XML paths in ``conf.py``:

.. code-block:: python

   extensions = [
       "sphinx_doxysummary",
   ]

   doxygen_xml = ["./xml"]

Basic Usage
-----------

Add a ``doxysummary`` directive:

.. code-block:: restructuredtext

   .. doxysummary::
      :toctree: generated
      :template: cppclass.rst

      MyNamespace::MyClass

Advanced Features
-----------------

- Use ``:scope:`` to set a namespace or class scope.
- Alias entries with quoted display names.

Examples
--------

.. code-block:: restructuredtext

   .. doxysummary::
      :toctree: generated
      :scope: api

      Widget
      Gizmo

Additional Resources
--------------------

- `Manual <https://doxysummary.readthedocs.io/en/latest/>`_
- `PyPI <https://pypi.org/project/sphinx-doxysummary/>`_
- `API Documentation <../../pdoc/sphinx_doxysummary/index.html>`_
