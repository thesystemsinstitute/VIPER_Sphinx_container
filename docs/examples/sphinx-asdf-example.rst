Sphinx Asdf Example
===================

.. note::

   **Package**: sphinx-asdf  
   **Purpose**: ASDF schema documentation  
   **Tutorial**: See :doc:`../tutorials/packages/sphinx-asdf` for complete tutorial

This page demonstrates **sphinx-asdf** - ASDF schema documentation.

.. contents:: Contents
   :local:
   :depth: 3

Overview
--------


Key Features
~~~~~~~~~~~~

- **Schema Documentation**: Automatic documentation of ASDF schemas
- **Validation Examples**: Include schema validation examples
- **Schema Trees**: Generate schema reference trees
- **Custom Paths**: Flexible schema path configuration

Installation
------------

Using pip
~~~~~~~~~

Install the extension:

.. code-block:: bash

   pip install sphinx-asdf

Or add to your ``requirements.txt``:

.. code-block:: text

   sphinx-asdf
   sphinx>=5.0.0
   asdf>=2.8.0

Configuration
-------------

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_asdf',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

Complete configuration with all features:

.. code-block:: python

   extensions = ['sphinx_asdf']
   
   # Package-specific configuration
   asdf_schema_path = '_schemas'
   asdf_schema_standard_prefix = 'http://stsci.edu/schemas/asdf/'
   asdf_schema_reference_mapping = []
   
   # Extension configuration
   asdf_extensions = []

Basic Usage
-----------

Example 1: Basic Schema Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here's a basic example:

.. code-block:: rst

   .. asdf-schema::
      :schema: config-schema.yaml
      :title: Configuration Schema

Example 2: Auto-generate Schemas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Automatically document all schemas:

.. code-block:: rst

   .. asdf-autoschemas::
      :schema-root: schemas/
      :standard-prefix: http://example.com/schemas/

Real-World Examples
-------------------

Example: Astronomical Data Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A practical astronomy data format documentation:

.. code-block:: rst

   FITS Data Schema
   ================
   
   .. asdf-schema::
      :schema: fits-schema.yaml
      :examples:
   
   Example Data File
   -----------------
   
   .. asdf-example::
      :schema: fits-schema.yaml
      :example-file: examples/observation.asdf
   
   Schema Tree
   -----------
   
   .. asdf-schema-tree::
      :schema: fits-schema.yaml
      :max-depth: 4

Best Practices
--------------

Recommendations
~~~~~~~~~~~~~~~

- Use clear schema descriptions
- Provide validation examples
- Keep schemas versioned
- Test schema documentation builds

Common Patterns
~~~~~~~~~~~~~~~

Standard patterns for using sphinx-asdf:

1. **Schema Documentation**: Document individual schemas with examples
2. **Schema Trees**: Show schema hierarchy and references
3. **Validation**: Include validation examples

Integration Tips
----------------

Working with Other Extensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

sphinx-asdf integrates well with:

- sphinx-jsonschema for JSON schema documentation
- Standard Sphinx extensions
- Custom documentation tools

Additional Resources
--------------------

- :doc:`Complete Tutorial <../tutorials/packages/sphinx-asdf>`
- `PyPI Package <https://pypi.org/project/sphinx-asdf/>`_
- :ref:`Package API Documentation <pdoc-sphinx-asdf>`

Next Steps
----------

- Explore the :doc:`tutorial <../tutorials/packages/sphinx-asdf>`
- Check the official documentation
- Try the examples in your own projects
- Customize for your specific needs
