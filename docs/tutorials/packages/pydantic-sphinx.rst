Pydantic Sphinx Tutorial
========================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/pydantic-sphinx/>`_
   - :doc:`See Working Example <../../examples/pydantic-sphinx-example>`

This tutorial demonstrates how to use pydantic-sphinx in your Sphinx documentation.

What is Pydantic Sphinx?
-------------------------
pydantic-sphinx is a Sphinx extension that provides:

- Pydantic model documentation
- Easy integration with Sphinx
- Comprehensive configuration options
- Professional documentation output

pydantic-sphinx provides:

- Pydantic model documentation
- Integration with Sphinx documentation
- Flexible configuration options
- Professional output formatting

Key Features
~~~~~~~~~~~~

- **Model Documentation**: Auto-document Pydantic models
- **JSON Schema**: Display JSON schema
- **Validators**: Document custom validators
- **Configuration**: Show model configuration


Installation
------------

pydantic-sphinx is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import pydantic_sphinx; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``docs/conf.py``:

.. code-block:: python

   extensions = [
       'pydantic_sphinx',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['pydantic_sphinx']
   
   # Configuration options
   autodoc_pydantic_model_show_json = True
   autodoc_pydantic_model_show_config = True


Complete configuration with all features:

.. code-block:: python

   extensions = ['pydantic_sphinx', 'sphinx.ext.autodoc']
   
   # Package-specific configuration
   autodoc_pydantic_model_show_json = True
   autodoc_pydantic_model_show_config = True
   autodoc_pydantic_model_show_validator_members = True
   autodoc_pydantic_settings_show_json = True
   autodoc_pydantic_field_list_validators = True

Basic Usage
-----------

Getting Started
~~~~~~~~~~~~~~~

Document Pydantic models:

.. code-block:: rst

   .. autopydantic_model:: myapp.models.User

Document Fields
~~~~~~~~~~~~~~~

Show model fields:

.. code-block:: rst

   .. autopydantic_model:: myapp.models.User
      :members:
      :member-order: bysource

Common Use Cases
----------------

Model Documentation
~~~~~~~~~~~~~~~~~~~

Document data models:

.. code-block:: rst

   .. autopydantic_model:: myapp.models.User
      :members:
      :show-json:
      :show-config:

Settings Documentation
~~~~~~~~~~~~~~~~~~~~~~

Document settings classes:

.. code-block:: rst

   .. autopydantic_settings:: myapp.config.Settings
      :members:

Advanced Features
-----------------

JSON Schema
~~~~~~~~~~~

Show JSON schema:

.. code-block:: rst

   .. autopydantic_model:: myapp.models.User
      :show-json-schema:

Validators
~~~~~~~~~~

Document validators:

.. code-block:: rst

   .. autopydantic_model:: myapp.models.User
      :members:
      :show-validators:

Best Practices
--------------

Tips and Guidelines
~~~~~~~~~~~~~~~~~~~

- Add field descriptions in Field()
- Document validators
- Show JSON examples
- Include configuration
- Keep models well-documented

Troubleshooting
---------------

Common Issues
~~~~~~~~~~~~~

**Issue**: Model not found

**Solution**: Ensure the module path is correct and Pydantic is installed.

**Issue**: Fields not showing

**Solution**: Check autodoc configuration and model definition.

Additional Resources
--------------------

- :doc:`Working Example <../../examples/pydantic-sphinx-example>`
- `PyPI Package <https://pypi.org/project/pydantic-sphinx/>`_
