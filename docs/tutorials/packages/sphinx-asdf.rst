Sphinx Asdf Tutorial
====================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-asdf/>`_
   - `API Documentation <../../pdoc/sphinx_asdf/index.html>`_
   - `Manual <https://github.com/ska-telescope/ska-sdp-cip-developer-docs>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinx-asdf in your Sphinx documentation.

What is Sphinx Asdf?
--------------------
sphinx-asdf is a Sphinx extension that provides:

- ASDF schema documentation
- Easy integration with Sphinx
- Comprehensive configuration options
- Professional documentation output

sphinx-asdf provides:

- ASDF schema documentation
- Integration with Sphinx documentation
- Flexible configuration options
- Professional output formatting

Key Features
~~~~~~~~~~~~

- **Schema Documentation**: Automatic documentation of ASDF schemas
- **Validation Examples**: Include schema validation examples
- **Schema Trees**: Generate schema reference trees
- **Custom Paths**: Flexible schema path configuration


Installation
------------

sphinx-asdf is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinx_asdf; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``docs/conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_asdf',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinx_asdf']
   
   # Configuration options
   asdf_schema_path = '_schemas'
   asdf_schema_standard_prefix = 'http://stsci.edu/schemas/asdf/'


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

Getting Started
~~~~~~~~~~~~~~~

Here's a basic example of using sphinx-asdf:

.. code-block:: rst

   .. asdf-schema::
      :schema: myschema.yaml
      :title: My Schema

Document Schemas
~~~~~~~~~~~~~~~~

Document ASDF schemas automatically:

.. code-block:: rst

   .. asdf-autoschemas::
      :schema-root: schemas/
      :standard-prefix: http://example.com/schemas/

Common Use Cases
----------------

Schema Documentation
~~~~~~~~~~~~~~~~~~~~

Generate schema documentation:

.. code-block:: rst

   .. asdf-schema::
      :schema: config-schema.yaml
      :examples:
      :schema-path: _schemas/

Schema Validation Examples
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Include schema validation examples:

.. code-block:: rst

   .. asdf-example::
      :schema: config-schema.yaml
      :example-file: examples/config.yaml

Advanced Features
-----------------

Custom Schema Paths
~~~~~~~~~~~~~~~~~~~

Configure custom schema paths:

.. code-block:: python

   # In conf.py
   asdf_schema_path = 'custom/schemas'
   asdf_extensions = ['myext.schemas']

Schema References
~~~~~~~~~~~~~~~~~

Document schema references:

.. code-block:: rst

   .. asdf-schema-tree::
      :schema: root-schema.yaml
      :max-depth: 3

Best Practices
--------------

Tips and Guidelines
~~~~~~~~~~~~~~~~~~~

- Keep schemas well-documented
- Provide clear examples
- Test schema validation
- Use appropriate schema versions
- Keep documentation in sync with schemas

Troubleshooting
---------------

Common Issues
~~~~~~~~~~~~~

**Issue**: Schema not found

**Solution**: Check the schema path configuration and file location.

**Issue**: Validation errors

**Solution**: Ensure your example files match the schema definition.


Practical Examples
------------------

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

- `PyPI Package <https://pypi.org/project/sphinx-asdf/>`_
- :doc:`Complete Tutorial <../tutorials/packages/sphinx-asdf>`
- :ref:`Package API Documentation <pdoc-sphinx-asdf>`
Next Steps
----------
- Explore the :doc:`tutorial <../tutorials/packages/sphinx-asdf>`
- Check the official documentation
- Try the examples in your own projects
- Customize for your specific needs

