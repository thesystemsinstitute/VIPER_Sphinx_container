Sphinx-Autodoc2-Fern Example
============================

This page demonstrates the **sphinx-autodoc2-fern** extension for generating API documentation with Fern-style layouts.

.. contents:: Contents
   :local:
   :depth: 2

Overview
--------

The sphinx-autodoc2-fern extension provides modern, Fern-inspired API documentation layouts with enhanced navigation and presentation.

Basic Usage
-----------

API Documentation
~~~~~~~~~~~~~~~~~

.. code-block:: python

   class UserAPI:
       """User management API."""
       
       def get_user(self, user_id: int) -> dict:
           """Retrieve user by ID."""
           pass
       
       def create_user(self, data: dict) -> dict:
           """Create new user."""
           pass

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_autodoc2_fern',
   ]
   
   autodoc2_fern_layout = 'modern'

Options
~~~~~~~

.. code-block:: python

   autodoc2_fern_options = {
       'sidebar_navigation': True,
       'code_examples': True,
       'response_samples': True,
   }

Examples
--------

Endpoint Documentation
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   def list_users(page: int = 1, limit: int = 10) -> List[User]:
       """List all users with pagination.
       
       :param page: Page number
       :param limit: Items per page
       :return: List of users
       """
       pass

See Also
--------

- :doc:`../tutorials/packages/sphinx-autodoc2-fern` - Complete tutorial
- Fern documentation: https://buildwithfern.com/
- GitHub repository: https://github.com/sphinx-contrib/autodoc2-fern
