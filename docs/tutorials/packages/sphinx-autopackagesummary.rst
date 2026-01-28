Sphinx-Autopackagesummary Tutorial
===================================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-autopackagesummary/>`_
   - `Manual <https://github.com/sphinx-contrib/autopackagesummary>`_
   - :doc:`Working Example <../../examples/sphinx-autopackagesummary-example>`


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

Additional Resources
--------------------

- :doc:`sphinx-autoapi` - Alternative API documentation
- :doc:`sphinx-autoindex` - Automatic indexing
- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `autosummary Extension <https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html>`_
