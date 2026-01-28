Sphinx-Collapsible-Autodoc Example
===================================

This page demonstrates the **sphinx-collapsible-autodoc** extension for creating collapsible sections in autodoc output.

.. contents:: Contents
   :local:
   :depth: 2


Basic Usage
-----------

Collapsible Methods
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   class DataProcessor:
       """Data processing class with many methods."""
       
       def process(self, data):
           """Process data."""
           pass
       
       def validate(self, data):
           """Validate data."""
           pass
       
       def transform(self, data):
           """Transform data."""
           pass

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx.ext.autodoc',
       'sphinx_collapsible_autodoc',
   ]

Options
~~~~~~~

.. code-block:: python

   collapsible_autodoc_default = 'collapsed'  # or 'expanded'
   collapsible_autodoc_sections = ['methods', 'attributes']

Examples
--------

Collapsible Sections
~~~~~~~~~~~~~~~~~~~~

Methods are grouped in collapsible sections for easy navigation.

See Also
--------

- :doc:`../tutorials/packages/sphinx-collapsible-autodoc` - Complete tutorial
- GitHub repository: https://github.com/sphinx-contrib/collapsible-autodoc
