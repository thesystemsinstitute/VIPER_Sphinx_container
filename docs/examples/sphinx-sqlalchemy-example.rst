Sphinx Sqlalchemy Example
=========================

.. note::

   **Package**: sphinx-sqlalchemy  
   **Purpose**: SQLAlchemy model documentation  
   **Tutorial**: See :doc:`../tutorials/packages/sphinx-sqlalchemy` for complete tutorial

This page demonstrates **sphinx-sqlalchemy** - SQLAlchemy model documentation.

.. contents:: Contents
   :local:
   :depth: 3

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

- :doc:`Complete Tutorial <../tutorials/packages/sphinx-sqlalchemy>`
- `PyPI Package <https://pypi.org/project/sphinx-sqlalchemy/>`_
- :ref:`Package API Documentation <pdoc-sphinx-sqlalchemy>`

Next Steps
----------

- Explore the :doc:`tutorial <../tutorials/packages/sphinx-sqlalchemy>`
- Check the official documentation
- Try the examples in your own projects
- Customize for your specific needs
