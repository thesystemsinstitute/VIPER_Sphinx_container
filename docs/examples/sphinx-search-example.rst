Sphinx Search Example
=====================

.. note::

   **Package**: sphinx-search  
   **Purpose**: Enhanced search functionality  
   **Tutorial**: See :doc:`../tutorials/packages/sphinx-search` for complete tutorial

This page demonstrates **sphinx-search** - Enhanced search functionality.

.. contents:: Contents
   :local:
   :depth: 3

Overview
--------

What is sphinx-search?
----------------------

sphinx-search provides:

- Enhanced search functionality
- Integration with Sphinx documentation
- Flexible configuration options
- Professional output formatting

Key Features
~~~~~~~~~~~~

- **Advanced Search**: Enhanced search capabilities
- **Fuzzy Matching**: Find results even with typos
- **Code Search**: Search within code blocks
- **Search Analytics**: Track search queries

Installation
------------

Using pip
~~~~~~~~~

Install the extension:

.. code-block:: bash

   pip install sphinx-search

Or add to your ``requirements.txt``:

.. code-block:: text

   sphinx-search
   sphinx>=5.0.0

Configuration
-------------

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_search',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

Complete configuration with all features:

.. code-block:: python

   extensions = ['sphinx_search']
   
   # Package-specific configuration
   search_language = 'en'
   search_stemming = True
   search_stopwords = ['the', 'a', 'an']
   
   # Search options
   search_options = {
       'types': ['text', 'code', 'docstring'],
       'min_length': 3,
       'fuzzy_matching': True,
       'boost_title': 2.0,
       'boost_h1': 1.5,
       'boost_code': 0.8,
   }
   
   # Index configuration
   search_index_format = 'json'
   search_exclude = ['_build', '_templates', '_static']
   search_include_patterns = ['*.rst', '*.md']

Basic Usage
-----------

Example 1: Basic Search Enhancement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The extension automatically enhances the default Sphinx search:

.. code-block:: python

   # In conf.py
   extensions = ['sphinx_search']
   
   # Customization
   search_language = 'en'
   search_stemming = True

Example 2: Advanced Search Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure advanced features:

.. code-block:: python

   search_options = {
       'types': ['text', 'code', 'docstring'],
       'fuzzy_matching': True,
       'boost_title': 2.0,  # Boost title matches
       'boost_h1': 1.5,     # Boost H1 matches
       'max_results': 50,
   }

Real-World Examples
-------------------

Example: Documentation Site Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Complete search setup for documentation site:

.. code-block:: python

   # docs/conf.py
   extensions = [
       'sphinx_search',
       'sphinx.ext.autodoc',
   ]
   
   # Search configuration
   search_language = 'en'
   search_stemming = True
   search_stopwords = ['the', 'a', 'an', 'and', 'or', 'but']
   
   # Enhanced options
   search_options = {
       'types': ['text', 'code', 'docstring', 'title'],
       'min_length': 2,
       'fuzzy_matching': True,
       'fuzzy_distance': 2,
       'boost_title': 3.0,
       'boost_h1': 2.0,
       'boost_h2': 1.5,
       'boost_code': 1.0,
       'boost_docstring': 1.2,
   }
   
   # Exclusions
   search_exclude = [
       '_build/**',
       '_templates/**',
       '_static/**',
   ]

Example: Multi-language Search
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Support multiple languages:

.. code-block:: python

   # In conf.py
   language = 'en'  # Default language
   
   # Search configuration
   search_language = language
   search_languages = {
       'en': {
           'stemming': True,
           'stopwords': ['the', 'a', 'an'],
       },
       'es': {
           'stemming': True,
           'stopwords': ['el', 'la', 'un'],
       },
   }

Example: Code-heavy Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Optimize for code search:

.. code-block:: python

   search_options = {
       'types': ['code', 'docstring', 'text'],
       'boost_code': 2.0,        # Prioritize code
       'boost_docstring': 1.8,    # Then docstrings
       'boost_text': 1.0,         # Then regular text
       'min_length': 2,           # Shorter minimum for code
       'fuzzy_matching': False,   # Disable for code (exact match)
   }

Example: Custom Search Page
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a custom search results page:

.. code-block:: rst

   Search
   ======
   
   .. raw:: html
   
      <div id="custom-search">
          <input type="text" id="search-input" placeholder="Search documentation...">
          <div id="search-results"></div>
      </div>
      
      <script>
      // Custom search implementation
      document.getElementById('search-input').addEventListener('input', function(e) {
          // Use enhanced search API
          const query = e.target.value;
          if (query.length >= 3) {
              // Perform search
              performSearch(query);
          }
      });
      </script>

Best Practices
--------------

Recommendations
~~~~~~~~~~~~~~~

- Configure language-specific settings
- Use appropriate boosting for content types
- Set minimum search length to reduce noise
- Exclude build and template directories
- Test search with common queries

Common Patterns
~~~~~~~~~~~~~~~

Standard patterns for using sphinx-search:

1. **Content Boost**: Boost important content types
2. **Fuzzy Search**: Enable for user-friendly searches
3. **Code Search**: Optimize for code-heavy docs

Integration Tips
----------------

Working with Other Extensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

sphinx-search integrates well with:

- sphinx.ext.autodoc for API documentation search
- sphinx-sitemap for search engine optimization
- Custom themes with search widgets

Additional Resources
--------------------

- :doc:`Complete Tutorial <../tutorials/packages/sphinx-search>`
- `PyPI Package <https://pypi.org/project/sphinx-search/>`_
- :ref:`Package API Documentation <pdoc-sphinx-search>`

Next Steps
----------

- Explore the :doc:`tutorial <../tutorials/packages/sphinx-search>`
- Check the official documentation
- Try the examples in your own projects
- Customize for your specific needs
