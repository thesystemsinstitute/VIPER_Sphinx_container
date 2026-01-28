Sphinx Search Tutorial
======================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-search/>`_
   - :doc:`See Working Example <../../examples/sphinx-search-example>`

This tutorial demonstrates how to use sphinx-search in your Sphinx documentation.

What is Sphinx Search?
----------------------

sphinx-search is a Sphinx extension that provides:

- Enhanced search functionality
- Easy integration with Sphinx
- Comprehensive configuration options
- Professional documentation output

Installation
------------

sphinx-search is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinx_search; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``docs/conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_search',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinx_search']
   
   # Configuration options
   search_language = 'en'
   search_options = {
       'types': ['text', 'code'],
       'min_length': 3,
   }

Basic Usage
-----------

Getting Started
~~~~~~~~~~~~~~~

The extension automatically enhances search functionality.

Search Configuration
~~~~~~~~~~~~~~~~~~~~

Configure search behavior:

.. code-block:: python

   # In conf.py
   search_index_format = 'json'
   search_stemming = True

Common Use Cases
----------------

Code Search
~~~~~~~~~~~

Enable code search:

.. code-block:: python

   search_options = {
       'types': ['text', 'code', 'docstring'],
   }

Advanced Search
~~~~~~~~~~~~~~~

Configure advanced search features:

.. code-block:: python

   search_options = {
       'fuzzy_matching': True,
       'boost_title': 2.0,
   }

Advanced Features
-----------------

Custom Indexing
~~~~~~~~~~~~~~~

Customize what gets indexed:

.. code-block:: python

   search_exclude = ['_build', '_templates']
   search_include_patterns = ['*.rst', '*.md']

Search Analytics
~~~~~~~~~~~~~~~~

Track search queries:

.. code-block:: python

   search_analytics = True
   search_analytics_backend = 'google'

Best Practices
--------------

Tips and Guidelines
~~~~~~~~~~~~~~~~~~~

- Configure appropriate search languages
- Test search functionality
- Optimize index size
- Use search analytics
- Keep search index updated

Troubleshooting
---------------

Common Issues
~~~~~~~~~~~~~

**Issue**: Search not working

**Solution**: Check search index is built and JavaScript is loading.

**Issue**: Poor search results

**Solution**: Adjust search options and stemming configuration.

Additional Resources
--------------------

- :doc:`Working Example <../../examples/sphinx-search-example>`
- `PyPI Package <https://pypi.org/project/sphinx-search/>`_
