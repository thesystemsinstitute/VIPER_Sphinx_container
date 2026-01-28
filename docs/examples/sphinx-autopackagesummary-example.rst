Sphinx-Autopackagesummary Example
==================================

.. note::

   **Package**: sphinx-autopackagesummary  
   **Purpose**: Automatically generate package summaries and module overviews  
   **Tutorial**: See :doc:`../tutorials/packages/sphinx-autopackagesummary` for complete tutorial

This page demonstrates the **sphinx-autopackagesummary** extension for automatically generating comprehensive package and module summaries.

.. contents:: Contents
   :local:
   :depth: 3

Overview
--------

What is sphinx-autopackagesummary?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

sphinx-autopackagesummary extends Sphinx's autosummary to provide enhanced package documentation with:

- Automatic package structure documentation
- Module summary generation
- Hierarchical package trees
- Subpackage discovery
- API overview generation

Key Features
~~~~~~~~~~~~

- **Automatic Discovery**: Recursively discover packages and modules
- **Hierarchical Views**: Show package structure as trees
- **Rich Summaries**: Generate detailed package overviews
- **Customizable Output**: Control what gets documented
- **Cross-References**: Automatic linking between packages
- **Multi-Level**: Support deeply nested package structures
- **Filtering**: Include/exclude patterns for packages
- **Templates**: Customizable summary templates

Installation
------------

Using pip
~~~~~~~~~

Install the extension:

.. code-block:: bash

   pip install sphinx-autopackagesummary

Or add to your ``requirements.txt``:

.. code-block:: text

   sphinx-autopackagesummary>=0.3.0
   sphinx>=4.0.0

Configuration
-------------

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx.ext.autodoc',
       'sphinx.ext.autosummary',
       'sphinx_autopackagesummary',
       # ... other extensions
   ]
   
   # Enable autosummary
   autosummary_generate = True
   
   # Package summary settings
   autopackagesummary_generate = True

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

Complete configuration with all options:

.. code-block:: python

   # Package Discovery
   autopackagesummary_generate = True
   autopackagesummary_root_package = 'mypackage'
   autopackagesummary_max_depth = None  # Unlimited depth
   
   # Include/Exclude
   autopackagesummary_include_patterns = ['*']
   autopackagesummary_exclude_patterns = ['*.tests', '*.test_*', '*._*']
   
   # Content Options
   autopackagesummary_show_modules = True
   autopackagesummary_show_classes = True
   autopackagesummary_show_functions = True
   autopackagesummary_show_attributes = False
   autopackagesummary_show_private = False
   
   # Formatting
   autopackagesummary_format = 'hierarchical'  # 'hierarchical', 'flat', 'tree'
   autopackagesummary_show_docstrings = True
   autopackagesummary_short_docstrings = True  # First line only
   
   # Output Control
   autopackagesummary_toctree_dir = 'api'
   autopackagesummary_template_dir = '_templates'
   autopackagesummary_output_format = 'rst'  # 'rst', 'md'
   
   # Cross-References
   autopackagesummary_generate_links = True
   autopackagesummary_import_prefix = ''
   
   # Advanced Options
   autopackagesummary_recursive = True
   autopackagesummary_show_inheritance = True
   autopackagesummary_imported_members = False

Directives
----------

autopackagesummary Directive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Generate package summary:

.. code-block:: rst

   .. autopackagesummary:: mypackage
      :toctree: api
      :recursive:
      
      Complete package documentation.

With Options
~~~~~~~~~~~~

.. code-block:: rst

   .. autopackagesummary:: mypackage.utils
      :toctree: api/utils
      :recursive:
      :max-depth: 2
      :show-modules: true
      :show-classes: true
      :show-functions: true
      :exclude: mypackage.utils.internal
      
      Utilities package summary.

autopackagetree Directive
~~~~~~~~~~~~~~~~~~~~~~~~~~

Display package structure as tree:

.. code-block:: rst

   .. autopackagetree:: mypackage
      :max-depth: 3
      :show-files: true
      
      Package structure tree.

automodulesummary Directive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Summarize modules in a package:

.. code-block:: rst

   .. automodulesummary::
      :toctree: api/modules
      
      mypackage.core
      mypackage.utils
      mypackage.models

autopackageoverview Directive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Generate package overview:

.. code-block:: rst

   .. autopackageoverview:: mypackage
      :show-stats: true
      :show-dependencies: true
      
      High-level package overview.

Practical Examples
------------------

Complete Package Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**File**: ``api/index.rst``

.. code-block:: rst

   API Reference
   =============
   
   This page provides a complete reference for all packages and modules.
   
   Package Overview
   ----------------
   
   .. autopackageoverview:: mypackage
      :show-stats: true
      :show-dependencies: true
   
   Package Structure
   -----------------
   
   .. autopackagetree:: mypackage
      :max-depth: 3
   
   Complete API
   ------------
   
   .. autopackagesummary:: mypackage
      :toctree: generated
      :recursive:
      :max-depth: 3

Single Package Summary
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Core Package
   ============
   
   .. autopackagesummary:: mypackage.core
      :toctree: generated/core
      :recursive:
      :max-depth: 2
      :show-modules: true
      :show-classes: true
      :show-functions: true
      
      The core package provides fundamental functionality.

Hierarchical Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Package Hierarchy
   =================
   
   Root Package
   ------------
   
   .. autopackagesummary:: mypackage
      :toctree: api
      :max-depth: 1
      
      Top-level package overview.
   
   Subpackages
   -----------
   
   Core
   ~~~~
   
   .. autopackagesummary:: mypackage.core
      :toctree: api/core
      :max-depth: 2
   
   Utilities
   ~~~~~~~~~
   
   .. autopackagesummary:: mypackage.utils
      :toctree: api/utils
      :max-depth: 2
   
   Models
   ~~~~~~
   
   .. autopackagesummary:: mypackage.models
      :toctree: api/models
      :max-depth: 2

Module Summaries
~~~~~~~~~~~~~~~~

.. code-block:: rst

   Module Reference
   ================
   
   .. automodulesummary::
      :toctree: modules
      :template: custom_module.rst
      
      mypackage.core.base
      mypackage.core.exceptions
      mypackage.core.config
      mypackage.utils.helpers
      mypackage.utils.validators

Package Tree View
~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Package Structure
   =================
   
   .. autopackagetree:: mypackage
      :max-depth: 4
      :show-files: true
      :show-private: false
      
   The package structure shows the organization of modules and subpackages.

Sample Package Structure
------------------------

Example Package Layout
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text

   mypackage/
   ├── __init__.py
   ├── core/
   │   ├── __init__.py
   │   ├── base.py
   │   ├── exceptions.py
   │   └── config.py
   ├── utils/
   │   ├── __init__.py
   │   ├── helpers.py
   │   ├── validators.py
   │   └── formatters.py
   ├── models/
   │   ├── __init__.py
   │   ├── user.py
   │   ├── product.py
   │   └── order.py
   ├── api/
   │   ├── __init__.py
   │   ├── endpoints.py
   │   └── schemas.py
   └── cli/
       ├── __init__.py
       └── commands.py

Package __init__.py
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   """MyPackage - A comprehensive Python package.
   
   This package provides various utilities and tools for
   building applications.
   
   Subpackages
   -----------
   core
       Core functionality and base classes
   utils
       Utility functions and helpers
   models
       Data models and ORM classes
   api
       API endpoints and schemas
   cli
       Command-line interface
   """
   
   __version__ = '1.0.0'
   __author__ = 'Your Name'
   
   from mypackage.core import *
   from mypackage.utils import *

Subpackage __init__.py
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   """Core package for MyPackage.
   
   This subpackage contains the core functionality including:
   
   - Base classes
   - Exception definitions
   - Configuration management
   
   Classes
   -------
   BaseClass
       Foundation class for all components
   Config
       Configuration manager
   
   Exceptions
   ----------
   PackageError
       Base exception class
   ConfigError
       Configuration-related errors
   """
   
   from mypackage.core.base import BaseClass
   from mypackage.core.exceptions import PackageError, ConfigError
   from mypackage.core.config import Config
   
   __all__ = ['BaseClass', 'Config', 'PackageError', 'ConfigError']

Advanced Features
-----------------

Custom Templates
~~~~~~~~~~~~~~~~

Create custom package summary templates:

**File**: ``_templates/autopackagesummary/package.rst``

.. code-block:: rst

   {{ fullname }}
   {{ underline }}
   
   .. automodule:: {{ fullname }}
      :no-index:
   
   {% if subpackages %}
   Subpackages
   -----------
   
   .. autosummary::
      :toctree:
      :recursive:
   
   {% for item in subpackages %}
      {{ item }}
   {% endfor %}
   {% endif %}
   
   {% if modules %}
   Modules
   -------
   
   .. autosummary::
      :toctree:
   
   {% for item in modules %}
      {{ item }}
   {% endfor %}
   {% endif %}
   
   {% if classes %}
   Classes
   -------
   
   .. autosummary::
      :toctree:
      :template: custom_class.rst
   
   {% for item in classes %}
      {{ fullname }}.{{ item }}
   {% endfor %}
   {% endif %}

Custom Module Template
~~~~~~~~~~~~~~~~~~~~~~

**File**: ``_templates/autopackagesummary/module.rst``

.. code-block:: rst

   {{ fullname }}
   {{ underline }}
   
   .. automodule:: {{ fullname }}
   
   {% if all_classes %}
   Classes
   -------
   
   .. autosummary::
      :toctree:
      :nosignatures:
   
   {% for cls in all_classes %}
      {{ fullname }}.{{ cls }}
   {% endfor %}
   
   {% for cls in all_classes %}
   
   {{ cls }}
   {{ "~" * cls|length }}
   
   .. autoclass:: {{ fullname }}.{{ cls }}
      :members:
      :undoc-members:
      :show-inheritance:
   
   {% endfor %}
   {% endif %}
   
   {% if all_functions %}
   Functions
   ---------
   
   .. autosummary::
      :nosignatures:
   
   {% for func in all_functions %}
      {{ fullname }}.{{ func }}
   {% endfor %}
   
   {% for func in all_functions %}
   
   .. autofunction:: {{ fullname }}.{{ func }}
   
   {% endfor %}
   {% endif %}

Filtering and Selection
~~~~~~~~~~~~~~~~~~~~~~~

Control what gets documented:

.. code-block:: rst

   .. autopackagesummary:: mypackage
      :include: mypackage.core.*, mypackage.utils.*
      :exclude: *.tests, *._internal
      :show-private: false
      :imported-members: false

Package Statistics
~~~~~~~~~~~~~~~~~~

Show package metrics:

.. code-block:: rst

   Package Statistics
   ==================
   
   .. autopackageoverview:: mypackage
      :show-stats: true
      :metrics:
         - modules
         - classes
         - functions
         - lines-of-code
         - test-coverage

Best Practices
--------------

Documentation Organization
~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Logical Structure**: Organize by package hierarchy
2. **Clear Navigation**: Provide multiple entry points
3. **Consistent Formatting**: Use same templates throughout
4. **Helpful Summaries**: Write clear package docstrings

Example structure:

.. code-block:: text

   docs/
   ├── index.rst
   ├── api/
   │   ├── index.rst                 # Main API index
   │   ├── overview.rst              # Package overview
   │   ├── core/
   │   │   ├── index.rst             # Core package
   │   │   ├── base.rst              # Base module
   │   │   └── exceptions.rst        # Exceptions module
   │   ├── utils/
   │   │   └── index.rst             # Utils package
   │   └── models/
   │       └── index.rst             # Models package
   └── conf.py

Package Docstrings
~~~~~~~~~~~~~~~~~~

Write comprehensive package docstrings:

.. code-block:: python

   """Package one-line summary.
   
   Longer description explaining the purpose and scope
   of this package.
   
   Subpackages
   -----------
   subpkg1
       Description of subpackage
   subpkg2
       Description of another subpackage
   
   Modules
   -------
   module1
       Description of module
   module2
       Description of another module
   
   Examples
   --------
   >>> from mypackage import MyClass
   >>> obj = MyClass()
   >>> obj.method()
   
   See Also
   --------
   related_package : Related functionality
   """

Module Organization
~~~~~~~~~~~~~~~~~~~

Keep __all__ updated for clean summaries:

.. code-block:: python

   # mypackage/utils/__init__.py
   
   from mypackage.utils.helpers import *
   from mypackage.utils.validators import *
   
   __all__ = [
       # Helpers
       'format_string',
       'parse_config',
       'load_data',
       # Validators
       'validate_email',
       'validate_url',
       'validate_phone',
   ]

Troubleshooting
---------------

Modules Not Found
~~~~~~~~~~~~~~~~~

**Problem**: Packages not appearing in summary

**Solution**:

.. code-block:: python

   # Ensure package is importable
   import sys
   import os
   sys.path.insert(0, os.path.abspath('..'))
   
   # Check include patterns
   autopackagesummary_include_patterns = ['*']
   
   # Clear exclude patterns
   autopackagesummary_exclude_patterns = []

Empty Summaries
~~~~~~~~~~~~~~~

**Problem**: Summaries generated but empty

**Solution**:

.. code-block:: python

   # Enable content display
   autopackagesummary_show_modules = True
   autopackagesummary_show_classes = True
   autopackagesummary_show_functions = True
   
   # Check __all__ in __init__.py
   # Ensure docstrings exist

Template Errors
~~~~~~~~~~~~~~~

**Problem**: Template rendering fails

**Solution**:

.. code-block:: python

   # Check template path
   autopackagesummary_template_dir = '_templates'
   
   # Verify template syntax
   # Use default templates first
   autopackagesummary_template_dir = None

Slow Generation
~~~~~~~~~~~~~~~

**Problem**: Summary generation is slow

**Solution**:

.. code-block:: python

   # Limit depth
   autopackagesummary_max_depth = 2
   
   # Exclude large subpackages
   autopackagesummary_exclude_patterns = [
       '*.tests',
       '*.vendor',
       '*.migrations',
   ]
   
   # Disable imported members
   autopackagesummary_imported_members = False

Integration Examples
--------------------

With Sphinx-Autodoc
~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Package Documentation
   =====================
   
   Package Summary
   ---------------
   
   .. autopackagesummary:: mypackage
      :toctree: api
      :recursive:
   
   Detailed Documentation
   ----------------------
   
   .. automodule:: mypackage
      :members:
      :undoc-members:
      :show-inheritance:

With Napoleon
~~~~~~~~~~~~~

Use Google/NumPy style docstrings:

.. code-block:: python

   """Package for data processing.
   
   This package provides tools for processing and analyzing data.
   
   Attributes:
       VERSION (str): Current package version
       DEFAULT_CONFIG (dict): Default configuration settings
   
   Examples:
       Basic usage::
   
           >>> from mypackage import DataProcessor
           >>> processor = DataProcessor()
           >>> result = processor.process(data)
   
   Note:
       This package requires numpy and pandas.
   """

With Intersphinx
~~~~~~~~~~~~~~~~

Link to external packages:

.. code-block:: python

   # conf.py
   intersphinx_mapping = {
       'python': ('https://docs.python.org/3', None),
       'numpy': ('https://numpy.org/doc/stable/', None),
       'pandas': ('https://pandas.pydata.org/docs/', None),
   }

.. code-block:: rst

   Dependencies
   ------------
   
   This package depends on:
   
   - :mod:`numpy` - Numerical computations
   - :mod:`pandas` - Data manipulation
   - :mod:`requests` - HTTP requests

With ReadTheDocs
~~~~~~~~~~~~~~~~

Configure for ReadTheDocs:

.. code-block:: python

   # conf.py
   import os
   
   on_rtd = os.environ.get('READTHEDOCS') == 'True'
   
   if on_rtd:
       # Install package in RTD environment
       import subprocess
       subprocess.call(['pip', 'install', '-e', '..'])

Advanced Usage
--------------

Multi-Package Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Document multiple packages:

.. code-block:: rst

   Project Documentation
   =====================
   
   Main Package
   ------------
   
   .. autopackagesummary:: mainpkg
      :toctree: api/main
      :recursive:
   
   Plugin Packages
   ---------------
   
   .. autopackagesummary:: mainpkg.plugins.plugin1
      :toctree: api/plugins/plugin1
   
   .. autopackagesummary:: mainpkg.plugins.plugin2
      :toctree: api/plugins/plugin2

Conditional Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~

Document based on conditions:

.. code-block:: python

   # conf.py
   import os
   
   if os.environ.get('FULL_DOCS'):
       autopackagesummary_show_private = True
       autopackagesummary_max_depth = None
   else:
       autopackagesummary_show_private = False
       autopackagesummary_max_depth = 2

Dynamic Package Discovery
~~~~~~~~~~~~~~~~~~~~~~~~~

Discover packages dynamically:

.. code-block:: python

   # conf.py
   import pkgutil
   import importlib
   
   def find_packages(package_name):
       """Find all subpackages."""
       package = importlib.import_module(package_name)
       packages = []
       for importer, modname, ispkg in pkgutil.walk_packages(
           path=package.__path__,
           prefix=package.__name__ + '.',
       ):
           if ispkg:
               packages.append(modname)
       return packages
   
   # Use in documentation
   discovered_packages = find_packages('mypackage')

See Also
--------

Related Extensions
~~~~~~~~~~~~~~~~~~

- :doc:`sphinx-autodoc-example` - Automatic documentation
- :doc:`sphinx-autosummary-example` - Summary tables
- :doc:`sphinx-autoapi-example` - API documentation
- :doc:`sphinx-autoindex-example` - Index generation

External Resources
~~~~~~~~~~~~~~~~~~

- Sphinx Autosummary: https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html
- Python Packages: https://docs.python.org/3/tutorial/modules.html#packages

Summary
-------

sphinx-autopackagesummary provides comprehensive package documentation:

- **Automatic Discovery**: Recursively find packages and modules
- **Hierarchical Views**: Show package structure clearly
- **Rich Summaries**: Detailed package overviews
- **Customizable**: Templates and formatting options
- **Integration**: Works with autodoc, autosummary, Napoleon
- **Flexible**: Include/exclude patterns, depth control
- **Organized**: Clean, navigable documentation structure

Perfect for documenting large Python projects with complex package hierarchies.
