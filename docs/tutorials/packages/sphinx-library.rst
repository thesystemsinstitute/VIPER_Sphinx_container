Sphinx-Library Tutorial
=======================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-library/>`_
   - `API Documentation <../../pdoc/sphinx_library/index.html>`_
   - `Manual <https://github.com/sphinx-contrib/sphinx-library>`_
   - :doc:`Working Example <../../examples/sphinx-library-example>`


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

   docker run --rm kensai-sphinx:latest python -c "import sphinx_library; print(sphinx_library.__version__)"

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
   docker build -t kensai-sphinx:latest .
   
   # View generated documentation
   docker run -d -p 8080:8080 --name sphinx-docs kensai-sphinx:latest
   
   # Access at http://localhost:8080

Mount Your Library Source
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd)/mylib:/project/mylib \
     -v $(pwd)/docs:/project/docs \
     kensai-sphinx:latest \
     sphinx-build -b html /project/docs /project/docs/_build/html

With Auto-Documentation
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     -e LIBRARY_NAME="MyLibrary" \
     -e LIBRARY_VERSION="1.0.0" \
     kensai-sphinx:latest \
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
               kensai-sphinx:latest \
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

   docker run --rm kensai-sphinx:latest pip list | grep sphinx-library

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

Additional Resources
--------------------

- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- :doc:`sphinx-autoapi` - Automatic API documentation
- :doc:`../extensions` - Other useful extensions
- `Sphinx Documentation <https://www.sphinx-doc.org/>`_
