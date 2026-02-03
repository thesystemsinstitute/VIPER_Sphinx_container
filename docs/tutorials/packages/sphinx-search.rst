Sphinx Search Tutorial
======================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-search/>`_

This tutorial demonstrates how to use sphinx-search in your Sphinx documentation.

What is Sphinx Search?
----------------------
sphinx-search is a Sphinx extension that provides:

- Enhanced search functionality
- Easy integration with Sphinx
- Comprehensive configuration options
- Professional documentation output

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

sphinx-search is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm viper-sphinx:latest python -c "import sphinx_search; print('Installed')"

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


Practical Examples
------------------

Overview
--------


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

- `PyPI Package <https://pypi.org/project/sphinx-search/>`_
- :doc:`Complete Tutorial <../tutorials/packages/sphinx-search>`
- :ref:`Package API Documentation <pdoc-sphinx-search>`
Next Steps
----------
- Explore the :doc:`tutorial <../tutorials/packages/sphinx-search>`
- Check the official documentation
- Try the examples in your own projects
- Customize for your specific needs

