Sphinx-Autopackagesummary Tutorial
===================================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-autopackagesummary/>`_
   - `Manual <https://github.com/sphinx-contrib/autopackagesummary>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinx-autopackagesummary to automatically generate package summaries and API documentation.

What is Sphinx-Autopackagesummary?
-----------------------------------
sphinx-autopackagesummary is a Sphinx extension that provides:

- Automatic package summaries
- Module listing
- Class/function tables
- Hierarchical documentation
- Recursive package traversal
- Customizable templates
- Toctree generation
- Cross-referencing
- Organized API docs
- Multi-package support

This automates the creation of comprehensive package documentation structure.

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

sphinx-autopackagesummary is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinx_autopackagesummary; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``docs/conf.py``:

.. code-block:: python

   extensions = [
       'sphinx.ext.autodoc',
       'sphinx.ext.autosummary',
       'sphinx_autopackagesummary',
   ]
   
   # Auto-generate summaries
   autosummary_generate = True

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = [
       'sphinx.ext.autodoc',
       'sphinx.ext.autosummary',
       'sphinx_autopackagesummary',
   ]
   
   # Summary generation
   autosummary_generate = True
   autosummary_generate_overwrite = False
   
   # Package summary options
   autopackagesummary_autodoc_default_options = {
       'members': True,
       'undoc-members': True,
       'show-inheritance': True,
   }
   
   # Template directory
   templates_path = ['_templates']
   
   # Recursion depth
   autopackagesummary_max_depth = 3


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

Basic Usage
-----------

Generate Package Summary
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. autopackagesummary:: mypackage

This creates a summary of ``mypackage`` with all modules and members.

Recursive Documentation
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. autopackagesummary:: mypackage
      :recursive:

Custom Depth
~~~~~~~~~~~~

.. code-block:: rst

   .. autopackagesummary:: mypackage
      :recursive:
      :maxdepth: 2

   API Reference
   =============
   
   .. autopackagesummary:: mypackage
      :toctree: generated
      :recursive:

This generates:

- ``generated/mypackage.rst`` - Package overview
- ``generated/mypackage.core.rst`` - Core module
- ``generated/mypackage.utils.rst`` - Utils module
- ``generated/mypackage.config.rst`` - Config module

Example 2: Multi-Level Package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Project structure:

.. code-block:: text

   myproject/
   ├── __init__.py
   ├── core/
   │   ├── __init__.py
   │   ├── engine.py
   │   └── processor.py
   ├── api/
   │   ├── __init__.py
   │   ├── client.py
   │   └── server.py
   └── utils/
       ├── __init__.py
       ├── helpers.py
       └── validators.py

``docs/api/reference.rst``:

.. code-block:: rst

   Complete API Reference
   ======================
   
   This page provides complete documentation for all packages and modules.
   
   .. autopackagesummary:: myproject
      :toctree: _autosummary
      :recursive:
      :maxdepth: 3
   
   Package Structure
   -----------------
   
   - :mod:`myproject.core` - Core functionality
   - :mod:`myproject.api` - API components
   - :mod:`myproject.utils` - Utility functions

Example 3: Customized Member Display
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/conf.py``:

.. code-block:: python

   autopackagesummary_autodoc_default_options = {
       'members': True,
       'member-order': 'bysource',
       'special-members': '__init__',
       'undoc-members': True,
       'exclude-members': '__weakref__',
       'show-inheritance': True,
   }

``docs/api/detailed.rst``:

.. code-block:: rst

   Detailed API Documentation
   ==========================
   
   .. autopackagesummary:: mypackage
      :toctree: api
      :recursive:
      :template: custom-package.rst

Example 4: Separate Package Sections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/api/core.rst``:

.. code-block:: rst

   Core Package
   ============
   
   Core functionality and base classes.
   
   .. autopackagesummary:: myproject.core
      :toctree: _generated/core
      :recursive:

``docs/api/api.rst``:

.. code-block:: rst

   API Package
   ===========
   
   Client and server API implementations.
   
   .. autopackagesummary:: myproject.api
      :toctree: _generated/api
      :recursive:

``docs/api/utils.rst``:

.. code-block:: rst

   Utilities Package
   =================
   
   Helper functions and validators.
   
   .. autopackagesummary:: myproject.utils
      :toctree: _generated/utils
      :recursive:

``docs/api/index.rst``:

.. code-block:: rst

   API Documentation
   =================
   
   .. toctree::
      :maxdepth: 2
      
      core
      api
      utils

Example 5: Summary Tables
~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/api/summary.rst``:

.. code-block:: rst

   API Summary
   ===========
   
   Classes
   -------
   
   .. autosummary::
      :toctree: _generated
      :template: class.rst
      
      mypackage.core.Processor
      mypackage.core.Engine
      mypackage.api.Client
      mypackage.api.Server
   
   Functions
   ---------
   
   .. autosummary::
      :toctree: _generated
      :template: function.rst
      
      mypackage.utils.validate
      mypackage.utils.format_data
      mypackage.utils.parse_config
   
   Complete Package Documentation
   ------------------------------
   
   .. autopackagesummary:: mypackage
      :toctree: _generated
      :recursive:

Advanced Features
-----------------

Custom Templates
~~~~~~~~~~~~~~~~

``docs/_templates/custom-package.rst``:

.. code-block:: rst

   {{ fullname }}
   {{ "=" * (fullname | length) }}
   
   .. automodule:: {{ fullname }}
      :members:
      :undoc-members:
      :show-inheritance:
   
   {% block modules %}
   {% if modules %}
   Submodules
   ----------
   
   .. autosummary::
      :toctree:
      :recursive:
   {% for item in modules %}
      {{ item }}
   {%- endfor %}
   {% endif %}
   {% endblock %}

Filtering Packages
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   def skip_private_packages(app, what, name, obj, skip, options):
       """Skip private packages/modules."""
       if name.startswith('_') and name != '__init__':
           return True
       return skip
   
   def setup(app):
       app.connect('autodoc-skip-member', skip_private_packages)

Grouping by Category
~~~~~~~~~~~~~~~~~~~~

``docs/api/by-category.rst``:

.. code-block:: rst

   API by Category
   ===============
   
   Data Processing
   ---------------
   
   .. autopackagesummary:: mypackage.processing
      :toctree: _generated/processing
   
   Network Operations
   ------------------
   
   .. autopackagesummary:: mypackage.network
      :toctree: _generated/network
   
   File I/O
   --------
   
   .. autopackagesummary:: mypackage.io
      :toctree: _generated/io

Docker Integration
------------------

Build with Package Summaries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     kensai-sphinx:latest \
     sphinx-build -b html /project/docs /project/docs/_build/html

Auto-generate Summaries
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Generate summaries only
   docker run --rm \
     -v $(pwd):/project \
     kensai-sphinx:latest \
     sphinx-autogen docs/api/index.rst

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Build API Documentation
   
   on: [push]
   
   jobs:
     docs:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Install Package
           run: pip install -e .
         
         - name: Build Documentation
           run: |
             docker run --rm \
               -v $(pwd):/project \
               kensai-sphinx:latest \
               sphinx-build -b html /project/docs /project/docs/_build/html
         
         - name: Verify Generated Files
           run: |
             # Check that autosummary generated files
             if [ ! -d docs/_autosummary ]; then
               echo "Autosummary files not generated!"
               exit 1
             fi
         
         - name: Deploy
           uses: peaceiris/actions-gh-pages@v3
           with:
             github_token: ${{ secrets.GITHUB_TOKEN }}
             publish_dir: ./docs/_build/html

Best Practices
--------------

1. **Clear Structure**
   
   Organize packages logically

2. **Use Templates**
   
   Customize appearance

3. **Filter Private**
   
   Hide internal modules

4. **Add Context**
   
   Include package descriptions

5. **Test Generated Docs**
   
   Verify completeness

6. **Keep Updated**
   
   Regenerate on code changes

Troubleshooting
---------------

No Files Generated
~~~~~~~~~~~~~~~~~~

**Solution:**

Enable autosummary:

.. code-block:: python

   autosummary_generate = True

Verify package is importable:

.. code-block:: bash

   python -c "import mypackage"

Missing Modules
~~~~~~~~~~~~~~~

**Solution:**

Check maxdepth:

.. code-block:: rst

   .. autopackagesummary:: mypackage
      :maxdepth: 5

Import Errors
~~~~~~~~~~~~~

**Solution:**

Add package to path:

.. code-block:: python

   import sys
   sys.path.insert(0, os.path.abspath('../'))

Wrong Output Location
~~~~~~~~~~~~~~~~~~~~~

**Solution:**

Specify toctree directory:

.. code-block:: rst

   .. autopackagesummary:: mypackage
      :toctree: _generated

Template Not Found
~~~~~~~~~~~~~~~~~~

**Solution:**

Check templates path:

.. code-block:: python

   templates_path = ['_templates']

Verify template file exists.

Next Steps
----------

1. Configure autopackagesummary
2. Create API documentation pages
3. Customize templates
4. Build and review
5. Deploy documentation


Practical Examples
------------------

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


Practical Examples
------------------

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


Practical Examples
------------------

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

Additional Resources
--------------------
- :doc:`sphinx-autoapi` - Alternative API documentation
- :doc:`sphinx-autoindex` - Automatic indexing
- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `autosummary Extension <https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html>`_
Related Extensions
~~~~~~~~~~~~~~~~~~
- :doc:`sphinx-autodoc-example` - Automatic documentation
- :doc:`sphinx-autosummary-example` - Summary tables
- :doc:`sphinx-autoapi-example` - API documentation
- :doc:`sphinx-autoindex-example` - Index generation
External Resources
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

