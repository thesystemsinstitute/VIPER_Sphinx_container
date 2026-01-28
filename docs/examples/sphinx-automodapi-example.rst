Sphinx-Automodapi Example
=========================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-automodapi/>`_
   - `API Documentation <../pdoc/sphinx_automodapi/index.html>`_
   - `Manual <https://sphinx-automodapi.readthedocs.io/en/latest/>`_
   - :doc:`Tutorial <../tutorials/packages/sphinx-automodapi>`

This page demonstrates the **sphinx-automodapi** extension for automatically documenting entire Python modules and packages.

.. contents:: Contents
   :local:
   :depth: 2

Basic Usage
-----------

Simple Module
~~~~~~~~~~~~~

.. code-block:: rst

   .. automodapi:: mypackage.mymodule

This automatically documents all public classes and functions in the module.

With Options
~~~~~~~~~~~~

.. code-block:: rst

   .. automodapi:: mypackage.core
      :no-inheritance-diagram:
      :skip: internal_function

Examples
--------

Full Package
~~~~~~~~~~~~

.. code-block:: rst

   .. automodapi:: mypackage
      :no-main-docstring:
      :headings: ^=

Filtered Documentation
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. automodapi:: mypackage.utils
      :allowed-package-names: mypackage
      :skip: _internal_helper

Example 1: Data Processing Package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``sphinx_automodapi_mylib/__init__.py``:

.. literalinclude:: sphinx_automodapi_mylib/__init__.py
   :language: python

``sphinx_automodapi_mylib/readers.py``:

.. literalinclude:: sphinx_automodapi_mylib/readers.py
   :language: python

``mylib/processors.py``:

.. literalinclude:: sphinx_automodapi_mylib/processors.py
   :language: python

``sphinx_automodapi_mylib/writers.py``:

.. literalinclude:: sphinx_automodapi_mylib/writers.py
   :language: python

``sphinx_automodapi_mylib/api.rst``:

.. literalinclude:: sphinx_automodapi_mylib/api.rst
   :language: rst

**Generated Output:**

View the actual generated API documentation: :doc:`sphinx_automodapi_mylib/api`

The automodapi directives in the file above automatically generate:

- Complete class documentation for all public classes (BaseReader, CSVReader, JSONReader, XMLReader, DataProcessor, FilterProcessor, TransformProcessor, BaseWriter, CSVWriter, JSONWriter, XMLWriter)
- Method documentation with parameters, return types, and examples  
- Inheritance diagrams showing class hierarchies (e.g., BaseReader → CSVReader, JSONReader, XMLReader)
- Cross-references between related classes and functions
- Organized sections for each module with proper headings

**Explanation:**

As you can see above, the automodapi directive automatically generated:

- Complete class documentation for all public classes
- Method signatures with parameters and return types
- Inheritance diagrams (unless disabled with ``:no-inheritance-diagram:``)
- Cross-references between related classes and functions
- Organized sections for each module with proper headings

      
See Also
--------

- :doc:`../tutorials/packages/sphinx-automodapi` - Complete tutorial
- GitHub repository: https://github.com/astropy/sphinx-automodapi