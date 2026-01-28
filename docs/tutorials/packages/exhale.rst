Exhale Tutorial
===============

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/exhale/>`_
   - `API Documentation <../../pdoc/exhale/index.html>`_
   - `Manual <https://exhale.readthedocs.io/en/latest/>`_
   - :doc:`Working Example <../../examples/exhale-example>`


.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use Exhale to automatically generate C++ API documentation from Doxygen output.

What is Exhale?
---------------

Exhale is a Sphinx extension that provides:

- Automatic API page generation
- Doxygen integration
- Hierarchical documentation
- Class hierarchy trees
- File hierarchy trees
- Namespace documentation
- Index pages
- Cross-referencing
- Breathe integration
- Customizable layouts

Exhale automates the creation of comprehensive C++ API documentation, eliminating manual page creation.


Exhale analyzes Doxygen XML output and automatically creates a comprehensive documentation structure with class hierarchies, file listings, and namespace organization.

Installation
------------

Exhale is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import exhale; print('Installed')"

Prerequisites
-------------

Exhale requires:

1. Doxygen (to generate XML)
2. Breathe (to parse Doxygen XML)
3. Graphviz (optional, for diagrams)

Configuration
-------------

Basic Setup
~~~~~~~~~~~

``docs/conf.py``:

.. code-block:: python

   extensions = [
       'breathe',
       'exhale',
   ]
   
   # Breathe configuration
   breathe_projects = {
       "myproject": "./doxygen/xml"
   }
   breathe_default_project = "myproject"
   
   # Exhale configuration
   exhale_args = {
       "containmentFolder": "./api",
       "rootFileName": "library_root.rst",
       "rootFileTitle": "Library API",
       "doxygenStripFromPath": "..",
       "createTreeView": True,
       "exhaleExecutesDoxygen": True,
       "exhaleDoxygenStdin": "INPUT = ../include"
   }

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['breathe', 'exhale']
   
   # Breathe configuration
   breathe_projects = {"myproject": "./doxygen/xml"}
   breathe_default_project = "myproject"
   
   # Exhale configuration
   exhale_args = {
       # Required arguments
       "containmentFolder": "./api",
       "rootFileName": "library_root.rst",
       "rootFileTitle": "C++ API Reference",
       "doxygenStripFromPath": "..",
       
       # Doxygen execution
       "exhaleExecutesDoxygen": True,
       "exhaleDoxygenStdin": """
           INPUT = ../include ../src
           EXCLUDE_PATTERNS = */test/* */internal/*
           RECURSIVE = YES
           GENERATE_XML = YES
       """,
       
       # Tree view
       "createTreeView": True,
       "exhaleUseDoxyfile": False,
       
       # Styling
       "minifyTreeView": True,
       "treeViewIsBootstrap": True,
       
       # Listings
       "listingExclude": [r'.*Test.*', r'.*Internal.*'],
       
       # Page layout
       "fullToctreeMaxDepth": 2,
       "unabridgedOrphanKinds": {'file', 'namespace'},
       
       # Linking
       "kindsWithContentsDirectives": ['class', 'struct', 'namespace'],
   }


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   # Enable required extensions
   extensions = [
       'breathe',
       'exhale'
   ]
   
   # Breathe configuration
   breathe_projects = {
       "MyProject": "./doxyxml/"
   }
   breathe_default_project = "MyProject"
   
   # Exhale configuration
   exhale_args = {
       # Required arguments
       "containmentFolder": "./api",
       "rootFileName": "library_root.rst",
       "rootFileTitle": "Library API",
       "doxygenStripFromPath": "..",
       
       # Doxygen configuration
       "createTreeView": True,
       "exhaleExecutesDoxygen": True,
       "exhaleDoxygenStdin": "INPUT = ../include"
   }

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py - Advanced exhale settings
   exhale_args = {
       # Output configuration
       "containmentFolder": "./api",
       "rootFileName": "library_root.rst",
       "rootFileTitle": "Complete API Reference",
       
       # Doxygen integration
       "exhaleExecutesDoxygen": True,
       "exhaleDoxygenStdin": """
           INPUT            = ../include ../src
           EXCLUDE_PATTERNS = */internal/* */test/*
           EXCLUDE_SYMBOLS  = *_internal *_impl
       """,
       
       # Tree view settings
       "createTreeView": True,
       "exhaleUseDoxyfile": False,
       
       # Listing configuration
       "fullToctreeMaxDepth": 3,
       "listingExclude": [r'.*_p\.h$'],  # Exclude private headers
       
       # Page generation
       "unabridgedOrphanKinds": {"class", "struct"},
       
       # Path handling
       "doxygenStripFromPath": "..",
       
       # Custom CSS
       "customSpecificationsMapping": {
           "class": "custom-class",
           "function": "custom-function"
       }
   }

Using Existing Doxyfile
~~~~~~~~~~~~~~~~~~~~~~~

If you have an existing Doxyfile:

.. code-block:: python

   # conf.py
   exhale_args = {
       "containmentFolder": "./api",
       "rootFileName": "library_root.rst",
       "rootFileTitle": "API",
       
       # Use existing Doxyfile
       "exhaleExecutesDoxygen": True,
       "exhaleUseDoxyfile": True,
       "exhaleDoxygenStdin": "INPUT = ../include"  # Override INPUT only
   }

Basic Usage
-----------

Generate API Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Configure Exhale in ``conf.py``
2. Build documentation:

.. code-block:: bash

   sphinx-build -b html docs docs/_build/html

Exhale automatically:

- Runs Doxygen
- Generates RST files for all classes, functions, etc.
- Creates index pages
- Builds hierarchies

Include in Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/index.rst``:

.. code-block:: rst

   .. toctree::
      :maxdepth: 2
      
      introduction
      api/library_root
      examples

   MyLib Documentation
   ===================
   
   Welcome to MyLib!
   
   .. toctree::
      :maxdepth: 2
      :caption: Contents:
      
      introduction
      api/library_root
      examples

Result: Exhale generates:

- ``docs/api/library_root.rst`` - Main API index
- ``docs/api/namespace_mylib.rst`` - Namespace page
- ``docs/api/class_mylib_Processor.rst`` - Class page
- ``docs/api/function_*.rst`` - Function pages
- Hierarchy trees and indexes

Example 2: Multi-Module Project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``include/core/engine.hpp``:

.. code-block:: cpp

   namespace core {
   
   /**
    * @brief Main engine class
    */
   class Engine {
   public:
       void start();
       void stop();
   };
   
   } // namespace core

``include/plugins/plugin.hpp``:

.. code-block:: cpp

   namespace plugins {
   
   /**
    * @brief Plugin interface
    */
   class Plugin {
   public:
       virtual void load() = 0;
       virtual void unload() = 0;
   };
   
   } // namespace plugins

``docs/conf.py``:

.. code-block:: python

   exhale_args = {
       "containmentFolder": "./api",
       "rootFileName": "api_root.rst",
       "rootFileTitle": "Complete API Reference",
       "doxygenStripFromPath": "..",
       "createTreeView": True,
       "exhaleExecutesDoxygen": True,
       "exhaleDoxygenStdin": """
           INPUT = ../include/core ../include/plugins
           RECURSIVE = YES
           FILE_PATTERNS = *.hpp *.h
           EXCLUDE_PATTERNS = */test/*
       """,
       "fullToctreeMaxDepth": 3,
   }

Example 3: Custom Page Layout
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/conf.py``:

.. code-block:: python

   exhale_args = {
       "containmentFolder": "./api",
       "rootFileName": "api_index.rst",
       "rootFileTitle": "API Documentation",
       "doxygenStripFromPath": "..",
       
       # Custom layout
       "createTreeView": True,
       "minifyTreeView": False,
       "treeViewIsBootstrap": True,
       
       # Page organization
       "fullToctreeMaxDepth": 2,
       "unabridgedOrphanKinds": {'file', 'namespace', 'enum'},
       
       # Contents directives
       "kindsWithContentsDirectives": [
           'class', 'struct', 'namespace', 'file'
       ],
       
       # Custom page titles
       "afterTitleDescription": """
           This API reference is automatically generated from source code.
       """,
       
       # Exclude patterns
       "listingExclude": [
           r'.*_internal\.hpp',
           r'.*test.*',
       ],
       
       # Doxygen
       "exhaleExecutesDoxygen": True,
       "exhaleDoxygenStdin": """
           INPUT = ../include
           RECURSIVE = YES
           EXTRACT_ALL = YES
           EXTRACT_PRIVATE = YES
           EXTRACT_STATIC = YES
           GENERATE_XML = YES
       """,
   }

Example 4: Integration with Custom Pages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/api_guide.rst``:

.. code-block:: rst

   API Guide
   =========
   
   This guide explains how to use the MyLib API.
   
   Core Concepts
   -------------
   
   The library is organized into several namespaces:
   
   - :doc:`core <api/namespace_core>` - Core functionality
   - :doc:`utils <api/namespace_utils>` - Utility functions
   - :doc:`plugins <api/namespace_plugins>` - Plugin system
   
   Quick Start
   -----------
   
   1. Create an :cpp:class:`core::Engine` instance
   2. Initialize with :cpp:func:`core::Engine::start`
   3. Process data
   
   Complete Reference
   ------------------
   
   See the :doc:`full API reference <api/library_root>` for all classes and functions.

Advanced Features
-----------------

Custom Doxygen Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   exhale_args = {
       # Use existing Doxyfile
       "exhaleExecutesDoxygen": True,
       "exhaleUseDoxyfile": True,
       "exhaleDoxygenStdin": "INPUT = ../include",
   }

Or use separate Doxyfile:

.. code-block:: python

   exhale_args = {
       "exhaleExecutesDoxygen": False,  # Run Doxygen manually
       # ... other settings
   }

Exclude Specific Items
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   exhale_args = {
       "listingExclude": [
           r'.*Internal.*',
           r'.*_impl\.hpp',
           r'test_.*',
       ],
   }

Custom Tree View
~~~~~~~~~~~~~~~~

.. code-block:: python

   exhale_args = {
       "createTreeView": True,
       "minifyTreeView": True,  # Compact view
       "treeViewIsBootstrap": True,  # Bootstrap styling
   }

Orphan Pages
~~~~~~~~~~~~

.. code-block:: python

   exhale_args = {
       # Kinds that should have full pages even if orphaned
       "unabridgedOrphanKinds": {'file', 'namespace', 'enum'},
   }

Docker Integration
------------------

Complete Build Setup
~~~~~~~~~~~~~~~~~~~~~

``Dockerfile.docs``:

.. code-block:: dockerfile

   FROM kensai-sphinx:latest
   
   # Install dependencies
   RUN apk add --no-cache doxygen graphviz
   
   WORKDIR /project
   
   CMD ["sphinx-build", "-b", "html", "docs", "docs/_build/html"]

Build:

.. code-block:: bash

   docker build -f Dockerfile.docs -t myproject-docs .
   docker run --rm -v $(pwd):/project myproject-docs

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Build C++ API Docs
   
   on: [push]
   
   jobs:
     docs:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Install Dependencies
           run: |
             sudo apt-get update
             sudo apt-get install -y doxygen graphviz
         
         - name: Build Documentation
           run: |
             docker run --rm -v $(pwd):/project \
               kensai-sphinx:latest \
               sphinx-build -b html /project/docs /project/docs/_build/html
         
         - name: Verify API Generated
           run: |
             # Check that Exhale generated API files
             if [ ! -f docs/api/library_root.rst ]; then
               echo "API documentation not generated!"
               exit 1
             fi
         
         - name: Deploy
           uses: peaceiris/actions-gh-pages@v3
           with:
             github_token: ${{ secrets.GITHUB_TOKEN }}
             publish_dir: ./docs/_build/html

Best Practices
--------------

1. **Document Source Code**
   
   Use Doxygen comments consistently

2. **Organize Namespaces**
   
   Group related functionality

3. **Exclude Test Code**
   
   Keep API docs clean

4. **Use Tree View**
   
   Easier navigation for large APIs

5. **Cross-Reference**
   
   Link to API from guides

6. **Keep Updated**
   
   Regenerate on code changes

Troubleshooting
---------------

Exhale Not Generating Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Solution:**

Check Doxygen execution:

.. code-block:: python

   exhale_args = {
       "exhaleExecutesDoxygen": True,
       "exhaleDoxygenStdin": "INPUT = ../include",
   }

Verify Doxygen XML exists after build.

Missing Classes
~~~~~~~~~~~~~~~

**Solution:**

Check Doxygen input paths:

.. code-block:: python

   exhale_args = {
       "exhaleDoxygenStdin": """
           INPUT = ../include
           RECURSIVE = YES
       """,
   }

Tree View Not Showing
~~~~~~~~~~~~~~~~~~~~~

**Solution:**

Enable tree view:

.. code-block:: python

   exhale_args = {
       "createTreeView": True,
   }

Duplicate Pages
~~~~~~~~~~~~~~~

**Solution:**

Check for conflicts with manual RST files. Exhale generates automatically.

Build Errors
~~~~~~~~~~~~

**Solution:**

Check Sphinx output for Exhale warnings. Verify paths in configuration.

Next Steps
----------

1. Install Doxygen and Breathe
2. Configure Exhale
3. Build and review API docs
4. Customize layout
5. Integrate with CI/CD

Additional Resources
--------------------

- :doc:`breathe` - Doxygen integration
- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `Exhale Documentation <https://exhale.readthedocs.io/>`_
- `Doxygen Documentation <https://www.doxygen.nl/manual/>`_
