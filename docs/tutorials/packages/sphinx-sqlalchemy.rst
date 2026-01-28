Sphinx Sqlalchemy Tutorial
==========================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-sqlalchemy/>`_

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


Practical Examples
------------------

Overview
--------


Key Features
~~~~~~~~~~~~

- **Model Documentation**: Automatic documentation of SQLAlchemy models
- **Schema Generation**: Complete database schema documentation
- **Relationship Mapping**: Document model relationships and foreign keys
- **ER Diagrams**: Generate entity-relationship diagrams

Installation
------------

Using pip
~~~~~~~~~

Install the extension:

.. code-block:: bash

   pip install sphinx-sqlalchemy

Or add to your ``requirements.txt``:

.. code-block:: text

   sphinx-sqlalchemy
   sphinx>=5.0.0
   sqlalchemy>=1.4.0

Configuration
-------------

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_sqlalchemy',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

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

Example 1: Document a Model
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here's a basic example:

.. code-block:: rst

   .. sqlalchemy-model:: myapp.models.User
      :members:
      :show-inheritance:
      :show-relationships:

Example 2: Database Schema
~~~~~~~~~~~~~~~~~~~~~~~~~~

Document complete database schema:

.. code-block:: rst

   .. sqlalchemy-schema::
      :module: myapp.models
      :include-all-tables:
      :show-relationships:

Real-World Examples
-------------------

Example: E-commerce Models
~~~~~~~~~~~~~~~~~~~~~~~~~~

A practical e-commerce database documentation:

.. code-block:: rst

   Database Schema
   ===============
   
   .. sqlalchemy-schema::
      :module: ecommerce.models
      :include-all-tables:
   
   User Model
   ----------
   
   .. sqlalchemy-model:: ecommerce.models.User
      :members:
      :show-relationships:
   
   Product Model
   -------------
   
   .. sqlalchemy-model:: ecommerce.models.Product
      :members:
      :show-relationships:
   
   Order Model
   -----------
   
   .. sqlalchemy-model:: ecommerce.models.Order
      :members:
      :show-relationships:

Best Practices
--------------

Recommendations
~~~~~~~~~~~~~~~

- Use clear model docstrings
- Document all relationships
- Include column descriptions
- Keep schema documentation synchronized with code

Common Patterns
~~~~~~~~~~~~~~~

Standard patterns for using sphinx-sqlalchemy:

1. **Model Documentation**: Use automodel for individual models
2. **Schema Overview**: Generate complete schema documentation
3. **ER Diagrams**: Include visual representations

Integration Tips
----------------

Working with Other Extensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

sphinx-sqlalchemy integrates well with:

- sphinx-autoapi for API documentation
- sphinx-autodoc for automatic documentation
- eralchemy2 for additional ER diagram generation

Additional Resources
--------------------

- `PyPI Package <https://pypi.org/project/sphinx-sqlalchemy/>`_
- :doc:`Complete Tutorial <../tutorials/packages/sphinx-sqlalchemy>`
- :ref:`Package API Documentation <pdoc-sphinx-sqlalchemy>`
Next Steps
----------
- Explore the :doc:`tutorial <../tutorials/packages/sphinx-sqlalchemy>`
- Check the official documentation
- Try the examples in your own projects
- Customize for your specific needs

