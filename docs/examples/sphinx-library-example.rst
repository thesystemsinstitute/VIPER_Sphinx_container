Sphinx-Library Example
======================

This page demonstrates **sphinx-library**, showing how to create organized, professional library documentation with automatic API organization and enhanced features.


Example Library Documentation
------------------------------

Project Structure
~~~~~~~~~~~~~~~~~

A typical library project using sphinx-library:

.. code-block:: text

   myawesomelib/
   ├── myawesomelib/
   │   ├── __init__.py
   │   ├── core.py
   │   ├── utils.py
   │   ├── models/
   │   │   ├── __init__.py
   │   │   ├── base.py
   │   │   └── user.py
   │   └── api/
   │       ├── __init__.py
   │       ├── client.py
   │       └── exceptions.py
   ├── docs/
   │   ├── conf.py
   │   ├── index.rst
   │   ├── installation.rst
   │   ├── quickstart.rst
   │   ├── api/
   │   │   └── index.rst
   │   └── examples/
   │       └── basic.rst
   └── tests/

Configuration Example
~~~~~~~~~~~~~~~~~~~~~

Complete ``docs/conf.py`` setup:

.. code-block:: python

   # Project information
   project = 'MyAwesomeLib'
   copyright = '2026, Library Authors'
   author = 'Library Authors'
   version = '2.1'
   release = '2.1.0'
   
   # Extensions
   extensions = [
       'sphinx_library',
       'sphinx.ext.autodoc',
       'sphinx.ext.napoleon',
       'sphinx.ext.intersphinx',
       'sphinx.ext.viewcode',
   ]
   
   # Sphinx-library configuration
   library_name = 'MyAwesomeLib'
   library_version = '2.1.0'
   library_description = 'A comprehensive data processing library'
   library_author = 'Library Authors'
   library_license = 'MIT'
   library_logo = '_static/logo.png'
   
   # API documentation settings
   library_api_autodoc = True
   library_api_index = True
   library_api_show_private = False
   library_api_show_inherited = True
   
   # Module organization
   library_modules = {
       'Core': [
           'myawesomelib.core',
           'myawesomelib.utils',
       ],
       'Models': [
           'myawesomelib.models.base',
           'myawesomelib.models.user',
       ],
       'API Client': [
           'myawesomelib.api.client',
           'myawesomelib.api.exceptions',
       ],
   }
   
   # Version tracking
   library_versions = {
       '2.1.0': 'current',
       '2.0.0': 'stable',
       '1.5.0': 'legacy',
   }
   
   # Deprecation warnings
   library_show_deprecations = True
   library_deprecation_format = 'admonition'
   
   # Example code settings
   library_example_path = 'examples/'
   library_example_highlight = True
   
   # Theme customization
   html_theme = 'sphinx_rtd_theme'
   library_theme_options = {
       'logo_only': True,
       'display_version': True,
       'prev_next_buttons_location': 'bottom',
   }

Main Documentation Page
------------------------

**File:** ``docs/index.rst``

.. code-block:: rst

   MyAwesomeLib Documentation
   ==========================
   
   .. library-header::
      :version: 2.1.0
      :status: stable
      :license: MIT
      :python-versions: 3.8, 3.9, 3.10, 3.11, 3.12
   
   MyAwesomeLib is a comprehensive data processing library that provides
   powerful tools for data manipulation, analysis, and transformation.
   
   Quick Example
   -------------
   
   .. library-example::
      :name: basic-usage
      :category: quickstart
   
      from myawesomelib import DataProcessor
      
      # Create a processor
      processor = DataProcessor()
      
      # Process your data
      result = processor.process(data)
      print(result)
   
   Features
   --------
   
   .. library-features::
   
      * **High Performance**: Optimized for large datasets
      * **Easy to Use**: Simple, intuitive API
      * **Well Tested**: 95%+ code coverage
      * **Fully Typed**: Complete type annotations
      * **Extensible**: Plugin architecture
   
   Getting Started
   ---------------
   
   .. toctree::
      :maxdepth: 2
   
      installation
      quickstart
      user-guide/index
      api/index
      examples/index
   
   .. library-version-warning::
      :version: 2.1.0
      :message: This is the latest stable release.

API Documentation
-----------------

**File:** ``docs/api/index.rst``

.. code-block:: rst

   API Reference
   =============
   
   Complete API documentation for MyAwesomeLib.
   
   .. library-api-index::
      :organize-by: category
      :show-module-summary: true
   
   Core Modules
   ------------
   
   .. library-module-group:: Core
      :description: Core functionality and utilities
   
   .. automodule:: myawesomelib.core
      :members:
      :undoc-members:
      :show-inheritance:
      :library-enhanced: true
   
   Data Models
   -----------
   
   .. library-module-group:: Models
      :description: Data models and structures
   
   .. autoclass:: myawesomelib.models.base.BaseModel
      :members:
      :library-enhanced: true
      :show-examples: true
   
   .. autoclass:: myawesomelib.models.user.User
      :members:
      :inherited-members:
      :library-enhanced: true
   
   API Client
   ----------
   
   .. library-module-group:: API Client
      :description: HTTP client for API interactions
   
   .. autoclass:: myawesomelib.api.client.APIClient
      :members:
      :library-enhanced: true
      :show-examples: true
   
   Exceptions
   ~~~~~~~~~~
   
   .. autoexception:: myawesomelib.api.exceptions.APIError
      :library-enhanced: true
   
   .. autoexception:: myawesomelib.api.exceptions.AuthenticationError
      :library-enhanced: true

Enhanced API Display Features
------------------------------

Class Documentation
~~~~~~~~~~~~~~~~~~~

When documenting a class with library enhancements:

.. code-block:: python

   class DataProcessor:
       """Process and transform data.
       
       The DataProcessor provides efficient data transformation
       capabilities with support for various formats.
       
       .. library-meta::
          :added: 1.0.0
          :category: core
          :thread-safe: yes
       
       Args:
           config (dict): Configuration options
           strict (bool): Enable strict mode validation
       
       Example:
           Basic usage::
           
               processor = DataProcessor(strict=True)
               result = processor.process(data)
       
       See Also:
           - :class:`DataValidator` - Validate data
           - :class:`DataTransformer` - Transform data
       """

Rendered Output Features:

- **Version Badge**: Shows when class was added (v1.0.0)
- **Category Tag**: Groups by category (Core)
- **Thread-Safety Indicator**: Visual indicator for thread-safe classes
- **Enhanced Examples**: Syntax-highlighted code with copy button
- **Smart Cross-References**: Automatic linking to related classes
- **Parameter Tables**: Formatted parameter documentation

Method Documentation
~~~~~~~~~~~~~~~~~~~~

Enhanced method display:

.. code-block:: python

   def process(self, data, format='json'):
       """Process input data.
       
       .. library-meta::
          :complexity: O(n)
          :performance: optimized
          :added: 1.0.0
          :modified: 2.1.0
       
       Args:
           data (Any): Input data to process
           format (str): Output format ('json', 'xml', 'csv')
       
       Returns:
           dict: Processed data dictionary
       
       Raises:
           ValueError: If format is unsupported
           ProcessingError: If processing fails
       
       Example:
           >>> processor = DataProcessor()
           >>> result = processor.process({'key': 'value'})
           >>> print(result)
           {'processed': True, 'key': 'value'}
       
       .. library-performance::
          Typical execution: 0.5ms for 1000 records
       """

Rendered Features:

- **Complexity Badge**: Big-O notation display
- **Performance Indicators**: Speed/memory annotations
- **Version History**: Added/Modified version tags
- **Interactive Examples**: Runnable code snippets
- **Exception Documentation**: Clear error documentation

Deprecation Warnings
~~~~~~~~~~~~~~~~~~~~

Automatic deprecation notices:

.. code-block:: python

   def old_method(self, data):
       """Legacy processing method.
       
       .. deprecated:: 2.0.0
          Use :meth:`process` instead. This method will be
          removed in version 3.0.0.
       
       .. library-migration::
          :from: old_method(data)
          :to: process(data, format='json')
       """

Rendered as a prominent warning box with migration guide.

Module Organization Example
----------------------------

The library automatically generates organized API index:

**Rendered Output:**

.. code-block:: text

   API Reference
   =============
   
   ┌─────────────────────────────────────────────────────┐
   │ MyAwesomeLib v2.1.0                                 │
   │ Complete API Reference                              │
   │ Python 3.8+ │ MIT License │ 95% Coverage           │
   └─────────────────────────────────────────────────────┘
   
   📦 Core Modules
   ──────────────────────────────────────────────────────
   
   myawesomelib.core
      Core processing functionality
      Classes: DataProcessor, ConfigManager
      Functions: initialize, configure
      
   myawesomelib.utils
      Utility functions and helpers
      Functions: validate, transform, serialize
   
   📦 Data Models
   ──────────────────────────────────────────────────────
   
   myawesomelib.models.base
      Base model classes and mixins
      Classes: BaseModel, ModelMixin
      
   myawesomelib.models.user
      User-related data models
      Classes: User, UserProfile, UserSettings
   
   📦 API Client
   ──────────────────────────────────────────────────────
   
   myawesomelib.api.client
      HTTP API client
      Classes: APIClient, AsyncAPIClient
      
   myawesomelib.api.exceptions
      API-related exceptions
      Exceptions: APIError, AuthenticationError,
                  RateLimitError, ValidationError

Version Documentation
---------------------

Multiple version support:

.. code-block:: rst

   Version 2.1.0 (Current)
   -----------------------
   
   .. library-version-info::
      :version: 2.1.0
      :status: stable
      :released: 2026-01-15
      :python: 3.8+
   
   What's New
   ~~~~~~~~~~
   
   .. library-changelog::
      :version: 2.1.0
   
      **Added**
      
      - New async API client
      - Enhanced error handling
      - Performance improvements
      
      **Changed**
      
      - Updated dependency versions
      - Improved documentation
      
      **Deprecated**
      
      - ``old_method()`` - Use ``process()`` instead
      
      **Fixed**
      
      - Memory leak in batch processing
      - Edge case in data validation
   
   Migration Guide
   ~~~~~~~~~~~~~~~
   
   .. library-migration-guide::
      :from: 2.0.0
      :to: 2.1.0
   
      1. Update import statements::
      
         # Old
         from myawesomelib.legacy import Processor
         
         # New
         from myawesomelib.core import DataProcessor
      
      2. Replace deprecated methods::
      
         # Old
         result = processor.old_method(data)
         
         # New
         result = processor.process(data, format='json')

Examples Section
----------------

**File:** ``docs/examples/basic.rst``

.. code-block:: rst

   Basic Examples
   ==============
   
   Installation
   ------------
   
   .. library-install::
      :package: myawesomelib
      :extras: all
   
      pip install myawesomelib[all]
   
   Quick Start
   -----------
   
   .. library-example::
      :name: quickstart
      :category: basic
      :python-version: 3.8+
   
      from myawesomelib import DataProcessor
      
      # Initialize processor
      processor = DataProcessor(
          strict=True,
          validate=True
      )
      
      # Process data
      data = {'name': 'John', 'age': 30}
      result = processor.process(data)
      
      print(result)
      # Output: {'processed': True, 'name': 'John', 'age': 30}
   
   Advanced Usage
   --------------
   
   .. library-example::
      :name: advanced
      :category: advanced
      :requires: myawesomelib >= 2.1.0
   
      from myawesomelib import DataProcessor, Config
      
      # Custom configuration
      config = Config(
          format='json',
          validate=True,
          strict_mode=True
      )
      
      processor = DataProcessor(config)
      
      # Batch processing
      batch_data = [
          {'id': 1, 'value': 'A'},
          {'id': 2, 'value': 'B'},
          {'id': 3, 'value': 'C'},
      ]
      
      results = processor.process_batch(batch_data)
      
      for result in results:
          print(f"ID {result['id']}: {result['status']}")

Feature Showcase
----------------

Library Header
~~~~~~~~~~~~~~

Displays key library information:

.. code-block:: rst

   .. library-header::
      :version: 2.1.0
      :status: stable
      :license: MIT
      :python-versions: 3.8, 3.9, 3.10, 3.11, 3.12
      :platforms: Linux, macOS, Windows

Renders as a professional info card with badges.

Module Summary Cards
~~~~~~~~~~~~~~~~~~~~

Visual module summaries:

.. code-block:: rst

   .. library-module-card::
      :module: myawesomelib.core
      :category: Core
      :stability: stable
      :coverage: 98%

Interactive API Index
~~~~~~~~~~~~~~~~~~~~~

Searchable, filterable API reference:

.. code-block:: rst

   .. library-api-index::
      :organize-by: category
      :show-module-summary: true
      :enable-search: true
      :show-coverage: true

Installation Guide
~~~~~~~~~~~~~~~~~~

Enhanced installation documentation:

.. code-block:: rst

   .. library-install::
      :package: myawesomelib
      :extras: all, dev, docs
      :python: 3.8+
   
      # Basic installation
      pip install myawesomelib
      
      # With all extras
      pip install myawesomelib[all]
      
      # Development installation
      pip install myawesomelib[dev]

Best Practices Example
-----------------------

Complete documentation workflow:

1. **Setup**

   .. code-block:: bash
   
      # Initialize documentation
      sphinx-quickstart docs
      
      # Install sphinx-library
      pip install sphinx-library

2. **Configure**

   Add to ``docs/conf.py``:
   
   .. code-block:: python
   
      extensions = ['sphinx_library']
      library_name = 'MyLib'
      library_version = '1.0.0'

3. **Document**

   Write clear API documentation with examples:
   
   .. code-block:: python
   
      """Module documentation.
      
      .. library-meta::
         :category: core
         :added: 1.0.0
      """

4. **Build**

   .. code-block:: bash
   
      sphinx-build -b html docs/ docs/_build/html

Learn More
----------

For complete documentation and advanced features, see:

- :doc:`../tutorials/packages/sphinx-library` - Complete tutorial
- `Sphinx-library Documentation <https://sphinx-library.readthedocs.io/>`_
- `Library Documentation Best Practices <https://documentation.divio.com/>`_
