Sphinx GraphQL Tutorial
=======================

.. note::

   **Package Resources:**

   - `PyPI Package <https://pypi.org/project/sphinx-graphql/>`_
   - `API Documentation <../../pdoc/sphinx_graphql/index.html>`_
   - `Manual <https://dls-controls.github.io/sphinx-graphql>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial covers sphinx-graphql, a Sphinx extension for documenting GraphQL APIs.

What is Sphinx GraphQL?
----------------------
Sphinx GraphQL provides directives for rendering GraphQL schemas and GraphiQL views inside Sphinx documentation.

Installation
------------

Install via pip:

.. code-block:: bash

   pip install sphinx-graphql

Configuration
-------------

Enable the extension in ``conf.py``:

.. code-block:: python

   extensions = [
       "sphinx_graphql",
   ]

Basic Usage
-----------

Embed a GraphiQL view (example):

.. code-block:: restructuredtext

   .. graphiql::
      :endpoint: https://api.example.com/graphql

Advanced Features
-----------------

- Render schema documentation alongside GraphiQL.
- Configure endpoints per environment.

Examples
--------

Schema + GraphiQL layout (example structure):

.. code-block:: restructuredtext

   .. rubric:: GraphQL Playground

   .. graphiql::
      :endpoint: https://api.example.com/graphql

Additional Resources
--------------------

- `Manual <https://dls-controls.github.io/sphinx-graphql>`_
- `PyPI <https://pypi.org/project/sphinx-graphql/>`_
- `API Documentation <../../pdoc/sphinx_graphql/index.html>`_
