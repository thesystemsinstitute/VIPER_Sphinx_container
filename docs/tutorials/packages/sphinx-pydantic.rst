Sphinx Pydantic Tutorial
========================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-pydantic/>`_
   - `API Documentation <../../pdoc/sphinx_pydantic/index.html>`_
   - `Manual <https://autodoc-pydantic.readthedocs.io/>`_
   - :doc:`Working Example <../../examples/sphinx-pydantic-example>`


.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinx-pydantic in your Sphinx documentation.

What is Sphinx Pydantic?
-------------------------
sphinx-pydantic is a Sphinx extension that provides:

- Enhanced Pydantic documentation
- Easy integration with Sphinx
- Comprehensive configuration options
- Professional documentation output

sphinx-pydantic provides:

- Enhanced Pydantic documentation
- Integration with Sphinx documentation
- Flexible configuration options
- Professional output formatting

Key Features
~~~~~~~~~~~~

- **Enhanced Documentation**: Rich Pydantic model documentation
- **Field Summary**: Tabular field information
- **JSON Schema**: Display JSON/YAML schemas
- **Validators**: Document custom validators


Installation
------------

sphinx-pydantic is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinx_pydantic; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``docs/conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_pydantic',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinx_pydantic']
   
   # Configuration options
   pydantic_show_json = True
   pydantic_show_field_summary = True


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_pydantic',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

Complete configuration with all features:

.. code-block:: python

   extensions = ['sphinx_pydantic']
   
   # Package-specific configuration
   pydantic_show_json = True
   pydantic_show_field_summary = True
   pydantic_show_validators = True
   pydantic_show_config_summary = True
   pydantic_show_schema = True

Basic Usage
-----------

Getting Started
~~~~~~~~~~~~~~~

Document Pydantic models:

.. code-block:: rst

   .. pydantic:: myapp.models.User

Show Field Details
~~~~~~~~~~~~~~~~~~

Display field information:

.. code-block:: rst

   .. pydantic:: myapp.models.User
      :show-fields:
      :show-json:

Common Use Cases
----------------

Model Documentation
~~~~~~~~~~~~~~~~~~~

Document data models:

.. code-block:: rst

   .. pydantic:: myapp.models.User
      :show-fields:
      :show-validators:
      :show-config:

API Models
~~~~~~~~~~

Document API models:

.. code-block:: rst

   .. pydantic:: myapp.api.UserRequest
      :show-json-schema:

Advanced Features
-----------------

Field Summary
~~~~~~~~~~~~~

Show field summary table:

.. code-block:: rst

   .. pydantic:: myapp.models.User
      :field-summary:

JSON Schema
~~~~~~~~~~~

Display JSON schema:

.. code-block:: rst

   .. pydantic:: myapp.models.User
      :show-json-schema:
      :schema-format: yaml

Best Practices
--------------

Tips and Guidelines
~~~~~~~~~~~~~~~~~~~

- Add field descriptions
- Document validators
- Show JSON examples
- Include config options
- Keep documentation updated

Troubleshooting
---------------

Common Issues
~~~~~~~~~~~~~

**Issue**: Model not rendering

**Solution**: Check model path and ensure Pydantic is installed.

**Issue**: Fields missing

**Solution**: Verify field definitions and configuration.

Additional Resources
--------------------

- :doc:`Working Example <../../examples/sphinx-pydantic-example>`
- `PyPI Package <https://pypi.org/project/sphinx-pydantic/>`_
- `Official Documentation <https://sphinx-pydantic.readthedocs.io/>`_
