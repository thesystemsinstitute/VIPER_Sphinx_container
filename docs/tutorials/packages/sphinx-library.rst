Sphinx-Library Tutorial
=======================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-library/>`_
   - `API Documentation <../../pdoc/sphinx_library/index.html>`_
   - `Manual <https://github.com/sphinx-contrib/sphinx-library>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinx-library to document software libraries and create comprehensive API documentation with automatic organization and cross-referencing.

What is Sphinx-Library?
------------------------
sphinx-library is a Sphinx extension that provides enhanced tools for documenting software libraries. It offers:

- Automatic library structure organization
- Enhanced API documentation layouts
- Cross-referencing between library components
- Version tracking for library APIs
- Deprecation warnings and migration guides
- Automatic index generation for library modules
- Enhanced code examples with library context

sphinx-library enhances Sphinx with specialized features for documenting software libraries, providing better structure, organization, and presentation of library APIs.


Installation
------------

sphinx-library is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm viper-sphinx:latest python -c "import sphinx_library; print(sphinx_library.__version__)"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   # Enable the extension
   extensions = [
       'sphinx_library',
   ]

   # Basic configuration
   library_name = 'MyLibrary'
   library_version = '1.0.0'
   library_logo = '_static/logo.png'

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Full configuration options
   extensions = [
       'sphinx_library',
   ]

   # Library metadata
   library_name = 'MyAwesomeLib'
   library_version = '2.1.0'
   library_description = 'A comprehensive library for data processing'
   library_author = 'Your Name'
   library_logo = '_static/library_logo.png'
   
   # API documentation settings
   library_api_autodoc = True
   library_api_index = True
   library_api_show_private = False
   library_api_show_inherited = True
   
   # Module organization
   library_modules = {
       'Core': ['mylib.core', 'mylib.base'],
       'Utilities': ['mylib.utils', 'mylib.helpers'],
       'Extensions': ['mylib.ext'],
   }
   
   # Version management
   library_versions = {
       '2.1.0': 'current',
       '2.0.0': 'stable',
       '1.0.0': 'legacy',
   }
   
   # Deprecation tracking
   library_track_deprecations = True
   library_deprecation_warnings = True

Basic Usage
-----------

Library Directive
~~~~~~~~~~~~~~~~~

Document library components:

.. code-block:: rst

   .. library:: MyLibrary
      :version: 1.0.0
      :author: John Doe
      
      This is a comprehensive library for data processing.
      
      Key Features:
      
      - Fast data processing
      - Multiple format support
      - Extensible architecture

Module Documentation
~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. library-module:: mylib.core
      :category: Core
      :status: stable
      
      Core functionality for the library.
      
      Classes
      -------
      
      .. autoclass:: mylib.core.DataProcessor
         :members:

API Reference
~~~~~~~~~~~~~

.. code-block:: rst

   .. library-api::
      
      Complete API reference for MyLibrary.
      
      .. toctree::
         :maxdepth: 2
         
         api/core
         api/utils
         api/extensions

   MyLibrary Documentation
   =======================
   
   .. library:: MyLibrary
      :version: 1.0.0
      :homepage: https://github.com/user/mylib
      
      MyLibrary is a powerful data processing library.
   
   Quick Start
   -----------
   
   Installation::
   
       pip install mylib
   
   Basic usage:
   
   .. code-block:: python
   
      from mylib import DataProcessor
      
      processor = DataProcessor()
      result = processor.process(data)
   
   Contents
   --------
   
   .. toctree::
      :maxdepth: 2
      
      installation
      quickstart
      api/index
      examples

Example 2: Multi-Module Library
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``conf.py``:

.. code-block:: python

   library_modules = {
       'Core Components': [
           'mylib.core.processor',
           'mylib.core.validator',
           'mylib.core.transformer',
       ],
       'Data Formats': [
           'mylib.formats.json',
           'mylib.formats.xml',
           'mylib.formats.csv',
       ],
       'Utilities': [
           'mylib.utils.logging',
           'mylib.utils.config',
       ],
   }

``docs/api/index.rst``:

.. code-block:: rst

   API Reference
   =============
   
   .. library-api::
      :organize-by: category
      
      Complete API documentation organized by module category.
   
   Core Components
   ---------------
   
   .. library-module-group:: Core Components
      :auto-index:

Example 3: Version-Aware Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Track multiple versions:

.. code-block:: rst

   .. library:: MyLibrary
      :version: 2.0.0
      
      .. versionadded:: 2.0.0
         New async processing support.
      
      .. versionchanged:: 2.0.0
         Improved performance by 50%.
      
      .. deprecated:: 2.0.0
         The ``old_process()`` method is deprecated.
         Use ``process_async()`` instead.

Example 4: Class Library Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Data Processing Classes
   =======================
   
   .. library-class:: DataProcessor
      :module: mylib.core
      :category: Core
      
      Main class for data processing operations.
      
      .. library-method:: process
         :signature: process(data, options=None)
         :returns: ProcessedData
         
         Process input data with optional configuration.
         
         Parameters
         ----------
         data : dict or list
             Input data to process
         options : dict, optional
             Processing options
         
         Returns
         -------
         ProcessedData
             Processed result object
         
   Utility Functions
   =================
   
   .. library-function:: validate_input
      :module: mylib.utils
      :category: Validation
      
      Validate input data structure.
      
      .. code-block:: python
      
         from mylib.utils import validate_input
         
         is_valid = validate_input(data, schema)

Advanced Features
-----------------

Automatic Index Generation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. library-index::
      :by-category:
      :show-private: False
      
      Automatically generated index of all library components.

Cross-Referencing
~~~~~~~~~~~~~~~~~

Link between library components:

.. code-block:: rst

   The :library-class:`DataProcessor` uses :library-func:`validate_input`
   for input validation. See :library-mod:`mylib.core` for details.

Deprecation Warnings
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. library-deprecated:: 2.0.0
      :removed-in: 3.0.0
      :replacement: new_function
      
      This function is deprecated and will be removed in version 3.0.0.
      Use :func:`new_function` instead.

Migration Guides
~~~~~~~~~~~~~~~~

.. code-block:: rst

   Migration Guide: 1.x to 2.x
   ===========================
   
   .. library-migration::
      :from-version: 1.0
      :to-version: 2.0
      
      API Changes
      -----------
      
      - ``old_process()`` → ``process_async()``
      - ``Validator`` → ``DataValidator``
      
Docker Integration
------------------

Build Documentation
~~~~~~~~~~~~~~~~~~~

This container automatically builds library documentation:

.. code-block:: bash

   # Build the container (includes library docs)
   docker build -t viper-sphinx:latest .
   
   # View generated documentation
   docker run -d -p 8080:8080 --name sphinx-docs viper-sphinx:latest
   
   # Access at http://localhost:8080

Mount Your Library Source
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd)/mylib:/project/mylib \
     -v $(pwd)/docs:/project/docs \
     viper-sphinx:latest \
     sphinx-build -b html /project/docs /project/docs/_build/html

With Auto-Documentation
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     -e LIBRARY_NAME="MyLibrary" \
     -e LIBRARY_VERSION="1.0.0" \
     viper-sphinx:latest \
     sphinx-apidoc -o /project/docs/api /project/mylib

Complete Library Documentation Example
---------------------------------------

Project Structure
~~~~~~~~~~~~~~~~~

.. code-block:: text

   myproject/
   ├── mylib/
   │   ├── __init__.py
   │   ├── core/
   │   │   ├── __init__.py
   │   │   └── processor.py
   │   └── utils/
   │       ├── __init__.py
   │       └── helpers.py
   ├── docs/
   │   ├── conf.py
   │   ├── index.rst
   │   ├── installation.rst
   │   ├── quickstart.rst
   │   ├── api/
   │   │   ├── index.rst
   │   │   ├── core.rst
   │   │   └── utils.rst
   │   └── examples/
   │       └── basic.rst
   └── setup.py

conf.py Configuration
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import os
   import sys
   sys.path.insert(0, os.path.abspath('..'))
   
   project = 'MyLibrary'
   version = '1.0.0'
   
   extensions = [
       'sphinx.ext.autodoc',
       'sphinx.ext.napoleon',
       'sphinx_library',
   ]
   
   library_name = 'MyLibrary'
   library_version = version
   library_description = 'A powerful data processing library'
   
   library_modules = {
       'Core': ['mylib.core.processor'],
       'Utilities': ['mylib.utils.helpers'],
   }
   
   library_api_autodoc = True
   library_api_index = True

index.rst
~~~~~~~~~

.. code-block:: rst

   MyLibrary Documentation
   =======================
   
   .. library:: MyLibrary
      :version: 1.0.0
      :author: Your Name
      :homepage: https://github.com/you/mylib
      :license: MIT
      
      MyLibrary provides powerful data processing capabilities
      with an easy-to-use API.
   
   Features
   --------
   
   - **Fast**: Optimized for performance
   - **Flexible**: Supports multiple data formats
   - **Extensible**: Plugin architecture
   - **Well-tested**: Comprehensive test suite
   
   Quick Example
   -------------
   
   .. code-block:: python
   
      from mylib import DataProcessor
      
      processor = DataProcessor()
      result = processor.process({'data': [1, 2, 3]})
   
   Contents
   --------
   
   .. toctree::
      :maxdepth: 2
      
      installation
      quickstart
      api/index
      examples/basic

api/index.rst
~~~~~~~~~~~~~

.. code-block:: rst

   API Reference
   =============
   
   .. library-api::
      :organize-by: category
      
      Complete API documentation for MyLibrary.
   
   .. library-index::
      :by-category:
   
   Core Module
   -----------
   
   .. automodule:: mylib.core.processor
      :members:
      :undoc-members:
      :show-inheritance:
   
   Utilities Module
   ----------------
   
   .. automodule:: mylib.utils.helpers
      :members:
      :undoc-members:

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

``.github/workflows/docs.yml``:

.. code-block:: yaml

   name: Build Library Documentation
   
   on:
     push:
       branches: [main]
     pull_request:
   
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Build Documentation
           run: |
             docker run --rm \
               -v $(pwd):/project \
               -e LIBRARY_NAME="${{ github.event.repository.name }}" \
               -e LIBRARY_VERSION="${{ github.ref_name }}" \
               viper-sphinx:latest \
               sphinx-build -b html /project/docs /project/docs/_build/html
         
         - name: Deploy to GitHub Pages
           if: github.ref == 'refs/heads/main'
           uses: peaceiris/actions-gh-pages@v3
           with:
             github_token: ${{ secrets.GITHUB_TOKEN }}
             publish_dir: ./docs/_build/html

Common Patterns
---------------

Organizing Large Libraries
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   library_modules = {
       'Core Components': [
           'mylib.core.base',
           'mylib.core.processor',
           'mylib.core.validator',
       ],
       'Data Formats': [
           'mylib.formats.json',
           'mylib.formats.xml',
           'mylib.formats.yaml',
           'mylib.formats.csv',
       ],
       'Network': [
           'mylib.net.client',
           'mylib.net.server',
           'mylib.net.protocol',
       ],
       'Utilities': [
           'mylib.utils.logging',
           'mylib.utils.config',
           'mylib.utils.cache',
       ],
   }

Documenting Plugin Systems
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Plugin Development
   ==================
   
   .. library-plugin-api::
      
      Create custom plugins for MyLibrary.
   
   Base Plugin Class
   -----------------
   
   .. library-class:: BasePlugin
      :abstract:
      
      All plugins must inherit from BasePlugin.
      
      .. library-method:: process
         :abstract:
         
         Override this method to implement plugin logic.

API Stability Indicators
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. library-api-stability::
      
      ✅ **Stable** - Core API (mylib.core)
      ⚠️ **Beta** - Network API (mylib.net)
      🔬 **Experimental** - ML Extensions (mylib.ml)

Troubleshooting
---------------

Missing Library Module
~~~~~~~~~~~~~~~~~~~~~~

**Error:** "No module named 'sphinx_library'"

**Solution:**

Verify installation:

.. code-block:: bash

   docker run --rm viper-sphinx:latest pip list | grep sphinx-library

Import Errors in Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Error:** "ImportError: cannot import name 'MyClass'"

**Solution:**

Check ``sys.path`` in ``conf.py``:

.. code-block:: python

   import os
   import sys
   sys.path.insert(0, os.path.abspath('../mylib'))

Cross-Reference Not Found
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Error:** "undefined label: 'library-class'"

**Solution:**

Ensure extension is enabled:

.. code-block:: python

   extensions = ['sphinx_library']  # Add to conf.py

Best Practices
--------------

1. **Organize by Feature**
   
   Group modules by functionality, not file structure

2. **Provide Examples**
   
   Every API should have at least one usage example

3. **Document Versions**
   
   Track changes across versions with clear migration guides

4. **Use Semantic Versioning**
   
   Follow semver principles for version numbering

5. **Automate Documentation**
   
   Generate API docs automatically from docstrings

6. **Keep It Updated**
   
   Update documentation with every code change

7. **Test Examples**
   
   Ensure code examples in documentation actually work

Next Steps
----------

1. Configure sphinx-library for your project
2. Organize your library modules by category
3. Set up automatic API documentation
4. Create comprehensive examples
5. Integrate documentation builds into CI/CD
6. Consider :doc:`sphinx-autoapi` for automatic API generation


Practical Examples
------------------

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

Additional Resources
--------------------

- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- :doc:`sphinx-autoapi` - Automatic API documentation
- :doc:`../extensions` - Other useful extensions
- `Sphinx Documentation <https://www.sphinx-doc.org/>`_
