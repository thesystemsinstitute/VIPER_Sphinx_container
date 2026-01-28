Sphinx Asdf Tutorial
====================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-asdf/>`_
   - `API Documentation <../../pdoc/sphinx_asdf/index.html>`_
   - `Manual <https://github.com/ska-telescope/ska-sdp-cip-developer-docs>`_
   - :doc:`Working Example <../../examples/sphinx-asdf-example>`


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

Additional Resources
--------------------

- :doc:`Working Example <../../examples/sphinx-asdf-example>`
- `PyPI Package <https://pypi.org/project/sphinx-asdf/>`_
