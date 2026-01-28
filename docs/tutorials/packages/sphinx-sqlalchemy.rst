Sphinx Sqlalchemy Tutorial
==========================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-sqlalchemy/>`_
   - :doc:`See Working Example <../../examples/sphinx-sqlalchemy-example>`

This tutorial demonstrates how to use sphinx-sqlalchemy in your Sphinx documentation.

What is Sphinx Sqlalchemy?
---------------------------
sphinx-sqlalchemy is a Sphinx extension that provides:

- SQLAlchemy model documentation
- Easy integration with Sphinx
- Comprehensive configuration options
- Professional documentation output

sphinx-sqlalchemy provides:

- SQLAlchemy model documentation
- Integration with Sphinx documentation
- Flexible configuration options
- Professional output formatting

Key Features
~~~~~~~~~~~~

- **Model Documentation**: Automatic documentation of SQLAlchemy models
- **Schema Generation**: Complete database schema documentation
- **Relationship Mapping**: Document model relationships and foreign keys
- **ER Diagrams**: Generate entity-relationship diagrams


Installation
------------

sphinx-sqlalchemy is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinx_sqlalchemy; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``docs/conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_sqlalchemy',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinx_sqlalchemy']
   
   # Configuration options
   sqlalchemy_autodoc_models = True
   sqlalchemy_table_options = {
       'show_columns': True,
       'show_relationships': True,
   }


Complete configuration with all features:

.. code-block:: python

   extensions = ['sphinx_sqlalchemy']
   
   # Package-specific configuration
   sqlalchemy_autodoc_models = True
   sqlalchemy_table_options = {
       'show_columns': True,
       'show_relationships': True,
       'show_primary_keys': True,
       'show_foreign_keys': True,
       'show_indexes': True,
   }
   
   # ER diagram options
   sqlalchemy_erd_format = 'svg'
   sqlalchemy_erd_options = {
       'show_datatypes': True,
       'show_indexes': True,
   }

Basic Usage
-----------

Getting Started
~~~~~~~~~~~~~~~

Here's a basic example of using sphinx-sqlalchemy:

.. code-block:: rst

   .. sqlalchemy-model:: myapp.models.User
      :members:
      :show-inheritance:

Documenting Models
~~~~~~~~~~~~~~~~~~

Document SQLAlchemy models automatically:

.. code-block:: rst

   .. automodel:: User
      :members:
      :show-relationships:

Common Use Cases
----------------

Database Schema Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Generate complete database schema documentation:

.. code-block:: rst

   .. sqlalchemy-schema::
      :module: myapp.models
      :include-all-tables:

Model Relationships
~~~~~~~~~~~~~~~~~~~

Document model relationships and foreign keys:

.. code-block:: rst

   .. sqlalchemy-relationships:: User
      :show-backref:
      :show-foreign-keys:

Advanced Features
-----------------

Custom Formatting
~~~~~~~~~~~~~~~~~

Customize the output format:

.. code-block:: python

   # In conf.py
   sqlalchemy_model_options = {
       'show_primary_keys': True,
       'show_indexes': True,
       'show_constraints': True,
   }

ER Diagram Generation
~~~~~~~~~~~~~~~~~~~~~

Generate entity-relationship diagrams:

.. code-block:: rst

   .. sqlalchemy-erd::
      :module: myapp.models
      :format: svg

Best Practices
--------------

Tips and Guidelines
~~~~~~~~~~~~~~~~~~~

- Document all model relationships clearly
- Include column descriptions in docstrings
- Use appropriate type hints
- Keep database schema documentation updated
- Test documentation builds after model changes

Troubleshooting
---------------

Common Issues
~~~~~~~~~~~~~

**Issue**: Models not found

**Solution**: Ensure the module path is correct and models are importable.

**Issue**: Relationships not showing

**Solution**: Enable relationship display in configuration.

Additional Resources
--------------------

- :doc:`Working Example <../../examples/sphinx-sqlalchemy-example>`
- `PyPI Package <https://pypi.org/project/sphinx-sqlalchemy/>`_
