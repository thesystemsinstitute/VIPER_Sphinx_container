Sphinx-Automodapi Example
=========================

This page demonstrates the **sphinx-automodapi** extension for automatically documenting entire Python modules and packages.

.. contents:: Contents
   :local:
   :depth: 2

Overview
--------

The sphinx-automodapi extension simplifies documenting entire modules by automatically generating API documentation for all classes, functions, and submodules.

Basic Usage
-----------

Simple Module
~~~~~~~~~~~~~

.. automodapi:: mypackage.mymodule

This automatically documents all public classes and functions in the module.

With Options
~~~~~~~~~~~~

.. automodapi:: mypackage.core
   :no-inheritance-diagram:
   :skip: internal_function

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx.ext.autodoc',
       'sphinx_automodapi.automodapi',
   ]

Options
~~~~~~~

.. code-block:: python

   automodapi_toctreedirnm = 'api'
   automodapi_writereprocessed = False

Examples
--------

Full Package
~~~~~~~~~~~~

.. automodapi:: mypackage
   :no-main-docstring:
   :headings: ^=

Filtered Documentation
~~~~~~~~~~~~~~~~~~~~~~

.. automodapi:: mypackage.utils
   :allowed-package-names: mypackage
   :skip: _internal_helper

See Also
--------

- :doc:`../tutorials/packages/sphinx-automodapi` - Complete tutorial
- GitHub repository: https://github.com/astropy/sphinx-automodapi
