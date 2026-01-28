Sphinx-Autodoc-TOML Example
===========================

This page demonstrates the **sphinx-autodoc-toml** extension for documenting Python projects configured with pyproject.toml.

.. contents:: Contents
   :local:
   :depth: 2


Basic Usage
-----------

Project Metadata
~~~~~~~~~~~~~~~~

.. toml-autodoc:: pyproject.toml
   :section: project

This documents the [project] section including name, version, description, and dependencies.

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_autodoc_toml',
   ]
   
   toml_autodoc_file = 'pyproject.toml'

Options
~~~~~~~

.. code-block:: python

   toml_autodoc_sections = ['project', 'build-system', 'tool.pytest']

Examples
--------

Dependencies
~~~~~~~~~~~~

.. toml-autodoc:: pyproject.toml
   :section: project.dependencies

Build System
~~~~~~~~~~~~

.. toml-autodoc:: pyproject.toml
   :section: build-system

See Also
--------

- :doc:`../tutorials/packages/sphinx-autodoc-toml` - Complete tutorial
- pyproject.toml: https://peps.python.org/pep-0621/
- GitHub repository: https://github.com/sphinx-contrib/autodoc-toml
