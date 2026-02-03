Sphinx-Autoindex Tutorial
=========================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-autoindex/>`_
   - `API Documentation <../../pdoc/sphinx_autoindex/index.html>`_
   - `Manual <https://github.com/sphinx-contrib/autoindex>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinx-autoindex to automatically generate index pages for your documentation.

What is Sphinx-Autoindex?
--------------------------
sphinx-autoindex is a Sphinx extension that provides:

- Automatic index generation
- Module indexing
- Package indexing
- Class/function indexes
- Alphabetical sorting
- Grouped indexes
- Custom index templates
- Cross-referencing
- Search integration
- Multi-level indexing

This creates comprehensive indexes without manual maintenance.

What is sphinx-autoindex?
~~~~~~~~~~~~~~~~~~~~~~~~~~

sphinx-autoindex automatically generates various types of index pages and maintains cross-reference indexes throughout your documentation:

- Module and package indexes
- Symbol indexes (functions, classes, methods)
- Topic indexes
- Glossary generation
- Automatic cross-referencing

Key Features
~~~~~~~~~~~~

- **Automatic Index Generation**: Create comprehensive indexes automatically
- **Multiple Index Types**: Modules, symbols, topics, glossaries
- **Smart Cross-Referencing**: Automatic link generation
- **Hierarchical Organization**: Nested index structures
- **Customizable Formatting**: Control index appearance
- **Search Integration**: Enhanced search capabilities
- **Multi-language Support**: Internationalization support
- **Incremental Updates**: Efficient index rebuilding


Installation
------------

sphinx-autoindex is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm viper-sphinx:latest python -c "import sphinx_autoindex; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``docs/conf.py``:

.. code-block:: python

   extensions = [
       'sphinx.ext.autodoc',
       'sphinx_autoindex',
   ]
   
   # Auto-index configuration
   autoindex_generate = True

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinx.ext.autodoc', 'sphinx_autoindex']
   
   # Index generation
   autoindex_generate = True
   autoindex_modules = ['mypackage']
   
   # Index organization
   autoindex_group_by = 'module'  # or 'alpha', 'type'
   autoindex_ignore_patterns = ['test_*', '*_internal']
   
   # Display options
   autoindex_show_descriptions = True
   autoindex_show_signatures = True
   autoindex_compact = False


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx.ext.autodoc',
       'sphinx_autoindex',
       # ... other extensions
   ]
   
   # Enable auto-indexing
   autoindex_generate = True

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

Complete configuration with all options:

.. code-block:: python

   # Auto-indexing Configuration
   autoindex_generate = True
   autoindex_ignore = ['_build', 'venv', '*.pyc']
   
   # Index Types
   autoindex_modules = True
   autoindex_classes = True
   autoindex_functions = True
   autoindex_methods = True
   autoindex_attributes = True
   autoindex_data = True
   
   # Index Organization
   autoindex_group_by = 'module'  # 'module', 'type', 'alphabet'
   autoindex_sort_by = 'name'     # 'name', 'type', 'module'
   autoindex_hierarchical = True
   
   # Display Options
   autoindex_show_private = False
   autoindex_show_inherited = True
   autoindex_show_undocumented = False
   autoindex_format = 'detailed'  # 'detailed', 'compact', 'table'
   
   # Cross-References
   autoindex_generate_refs = True
   autoindex_ref_prefix = 'ref-'
   autoindex_ref_format = 'short'  # 'short', 'full', 'module.name'
   
   # Template Options
   autoindex_template = 'autoindex.html'
   autoindex_custom_sections = ['Examples', 'See Also']
   
   # Search Integration
   autoindex_enhance_search = True
   autoindex_search_boost = 1.5
   
   # Performance
   autoindex_cache_enabled = True
   autoindex_parallel_build = True

Basic Usage
-----------

Generate Module Index
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. autoindex:: mypackage

This creates an index of all modules in ``mypackage``.

Generate Class Index
~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. autoindex:: mypackage
      :type: class

Generate Function Index
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. autoindex:: mypackage
      :type: function

   API Reference
   =============
   
   Complete Module Index
   ----------------------
   
   .. autoindex:: mypackage
      :recursive: true
   
   Classes
   -------
   
   .. autoindex:: mypackage
      :type: class
      :recursive: true
   
   Functions
   ---------
   
   .. autoindex:: mypackage
      :type: function
      :recursive: true
   
   Exceptions
   ----------
   
   .. autoindex:: mypackage
      :type: exception
      :recursive: true

Example 2: Alphabetical Index
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/api/alphabetical.rst``:

.. code-block:: rst

   Alphabetical Index
   ==================
   
   A
   -
   
   .. autoindex:: mypackage
      :filter: ^[Aa]
   
   B
   -
   
   .. autoindex:: mypackage
      :filter: ^[Bb]
   
   C
   -
   
   .. autoindex:: mypackage
      :filter: ^[Cc]

Example 3: Grouped by Module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/api/by-module.rst``:

.. code-block:: rst

   Index by Module
   ===============
   
   Core Module
   -----------
   
   .. autoindex:: mypackage.core
   
   Utilities
   ---------
   
   .. autoindex:: mypackage.utils
   
   API Client
   ----------
   
   .. autoindex:: mypackage.api.client
   
   API Server
   ----------
   
   .. autoindex:: mypackage.api.server

Example 4: Custom Index with Descriptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/conf.py``:

.. code-block:: python

   autoindex_show_descriptions = True
   autoindex_description_length = 100

``docs/api/detailed-index.rst``:

.. code-block:: rst

   Detailed API Index
   ==================
   
   This index includes descriptions for all components.
   
   .. autoindex:: mypackage
      :recursive: true
      :show-descriptions: true
      :sort: name

Result:

.. code-block:: text

   mypackage.core.Processor
       Main data processing class for handling input transformations
   
   mypackage.core.process_data(data, options=None)
       Process data with optional configuration options
   
   mypackage.utils.validate(obj)
       Validate object against schema

Example 5: Multi-Package Index
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/api/packages.rst``:

.. code-block:: rst

   Package Index
   =============
   
   Core Package
   ------------
   
   .. autoindex:: myproject.core
      :maxdepth: 2
   
   Extensions Package
   ------------------
   
   .. autoindex:: myproject.extensions
      :maxdepth: 2
   
   Plugins Package
   ---------------
   
   .. autoindex:: myproject.plugins
      :maxdepth: 2

Example 6: Filtered Index
~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/api/public-api.rst``:

.. code-block:: rst

   Public API
   ==========
   
   This index shows only public (non-underscore) members.
   
   .. autoindex:: mypackage
      :recursive: true
      :ignore-patterns: _*

Advanced Features
-----------------

Custom Grouping
~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   def custom_grouper(name, obj):
       """Group items by custom logic."""
       if hasattr(obj, '__module__'):
           return obj.__module__.split('.')[1]
       return 'Other'
   
   autoindex_grouper = custom_grouper

Custom Sorting
~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   def custom_sorter(items):
       """Custom sort function."""
       # Sort by importance, then name
       def sort_key(item):
           name, obj = item
           priority = getattr(obj, '__priority__', 999)
           return (priority, name)
       
       return sorted(items, key=sort_key)
   
   autoindex_sorter = custom_sorter

Template Customization
~~~~~~~~~~~~~~~~~~~~~~

``docs/_templates/autoindex.html``:

.. code-block:: html

   <div class="autoindex">
     {% for group, items in index_data.items() %}
     <section class="index-group">
       <h3>{{ group }}</h3>
       <ul class="index-list">
         {% for name, info in items %}
         <li class="index-item">
           <a href="{{ info.url }}">{{ name }}</a>
           {% if info.signature %}
           <span class="signature">{{ info.signature }}</span>
           {% endif %}
           {% if info.description %}
           <p class="description">{{ info.description }}</p>
           {% endif %}
         </li>
         {% endfor %}
       </ul>
     </section>
     {% endfor %}
   </div>

Cross-Reference Integration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   See :ref:`autoindex-mypackage` for complete module listing.
   
   .. _autoindex-mypackage:
   
   .. autoindex:: mypackage

Docker Integration
------------------

Build with Auto-Index
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     viper-sphinx:latest \
     sphinx-build -b html /project/docs /project/docs/_build/html

Generate Index Only
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Generate index without full build
   docker run --rm \
     -v $(pwd):/project \
     viper-sphinx:latest \
     python -c "from sphinx_autoindex import generate_index; generate_index('mypackage')"

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Build Documentation with Index
   
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
               viper-sphinx:latest \
               sphinx-build -b html /project/docs /project/docs/_build/html
         
         - name: Verify Index Generated
           run: |
             # Check that index pages exist
             if [ ! -f docs/_build/html/api/index.html ]; then
               echo "Index not generated!"
               exit 1
             fi
         
         - name: Deploy
           uses: peaceiris/actions-gh-pages@v3
           with:
             github_token: ${{ secrets.GITHUB_TOKEN }}
             publish_dir: ./docs/_build/html

Best Practices
--------------

1. **Organize by Module**
   
   Group related items together

2. **Include Descriptions**
   
   Help users understand items

3. **Filter Appropriately**
   
   Hide internal/private members

4. **Keep Updated**
   
   Auto-index regenerates automatically

5. **Cross-Reference**
   
   Link from guides to index

6. **Test Thoroughly**
   
   Verify all items appear

Troubleshooting
---------------

Index Not Generated
~~~~~~~~~~~~~~~~~~~

**Solution:**

Check extension loaded:

.. code-block:: python

   extensions = ['sphinx_autoindex']

Verify package is importable:

.. code-block:: bash

   python -c "import mypackage"

Missing Items
~~~~~~~~~~~~~

**Solution:**

Check ignore patterns:

.. code-block:: python

   autoindex_ignore_patterns = []

Verify items are documented.

Import Errors
~~~~~~~~~~~~~

**Solution:**

Ensure package is installed:

.. code-block:: bash

   pip install -e .

Add to Python path:

.. code-block:: python

   import sys
   sys.path.insert(0, os.path.abspath('../'))

Duplicate Entries
~~~~~~~~~~~~~~~~~

**Solution:**

Check for name conflicts:

.. code-block:: python

   autoindex_deduplicate = True

Wrong Organization
~~~~~~~~~~~~~~~~~~

**Solution:**

Adjust grouping:

.. code-block:: python

   autoindex_group_by = 'module'  # or 'alpha', 'type'

Next Steps
----------

1. Configure autoindex
2. Create index pages
3. Customize grouping/sorting
4. Add to navigation
5. Deploy documentation


Practical Examples
------------------

Installation
------------

Using pip
~~~~~~~~~

Install the extension:

.. code-block:: bash

   pip install sphinx-autoindex

Or add to your ``requirements.txt``:

.. code-block:: text

   sphinx-autoindex>=1.3.0

Configuration
-------------

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx.ext.autodoc',
       'sphinx_autoindex',
       # ... other extensions
   ]
   
   # Enable auto-indexing
   autoindex_generate = True

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

Complete configuration with all options:

.. code-block:: python

   # Auto-indexing Configuration
   autoindex_generate = True
   autoindex_ignore = ['_build', 'venv', '*.pyc']
   
   # Index Types
   autoindex_modules = True
   autoindex_classes = True
   autoindex_functions = True
   autoindex_methods = True
   autoindex_attributes = True
   autoindex_data = True
   
   # Index Organization
   autoindex_group_by = 'module'  # 'module', 'type', 'alphabet'
   autoindex_sort_by = 'name'     # 'name', 'type', 'module'
   autoindex_hierarchical = True
   
   # Display Options
   autoindex_show_private = False
   autoindex_show_inherited = True
   autoindex_show_undocumented = False
   autoindex_format = 'detailed'  # 'detailed', 'compact', 'table'
   
   # Cross-References
   autoindex_generate_refs = True
   autoindex_ref_prefix = 'ref-'
   autoindex_ref_format = 'short'  # 'short', 'full', 'module.name'
   
   # Template Options
   autoindex_template = 'autoindex.html'
   autoindex_custom_sections = ['Examples', 'See Also']
   
   # Search Integration
   autoindex_enhance_search = True
   autoindex_search_boost = 1.5
   
   # Performance
   autoindex_cache_enabled = True
   autoindex_parallel_build = True

Directives
----------

autoindex Directive
~~~~~~~~~~~~~~~~~~~

Generate automatic index:

.. code-block:: rst

   .. autoindex::
      
      Automatically generated index of all symbols.

With Options
~~~~~~~~~~~~

.. code-block:: rst

   .. autoindex::
      :types: module, class, function
      :group-by: module
      :format: detailed
      :show-private: false
      
      Filtered and organized index.

automodindex Directive
~~~~~~~~~~~~~~~~~~~~~~

Generate module index:

.. code-block:: rst

   .. automodindex::
      :modules: mypackage.*
      :exclude: mypackage.internal
      :hierarchical: true
      
      Index of all modules in mypackage.

autoclassindex Directive
~~~~~~~~~~~~~~~~~~~~~~~~

Generate class index:

.. code-block:: rst

   .. autoclassindex::
      :modules: mypackage
      :show-bases: true
      :show-members: true
      :group-by: module

autofuncindex Directive
~~~~~~~~~~~~~~~~~~~~~~~

Generate function index:

.. code-block:: rst

   .. autofuncindex::
      :modules: mypackage.utils
      :include-methods: true
      :show-signatures: true

autoattribindex Directive
~~~~~~~~~~~~~~~~~~~~~~~~~

Generate attribute index:

.. code-block:: rst

   .. autoattribindex::
      :modules: mypackage.models
      :show-values: true
      :group-by: class

Roles
-----

Index References
~~~~~~~~~~~~~~~~

.. code-block:: rst

   See the :autoindex:`MyClass` documentation.
   
   Use :autofunc:`calculate_total` for totals.
   
   The :automod:`mypackage.utils` module provides utilities.

Practical Examples
------------------

Complete Module Index
~~~~~~~~~~~~~~~~~~~~~

**File**: ``api/index.rst``

.. code-block:: rst

   API Index
   =========
   
   Complete index of all modules, classes, and functions.
   
   .. autoindex::
      :types: module, class, function, method
      :group-by: module
      :format: detailed
      :show-inherited: true
      
      This index is automatically generated from the codebase.

Module-Specific Index
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Utils Module Index
   ==================
   
   .. automodindex::
      :modules: mypackage.utils
      :hierarchical: true
      :show-submodules: true
      
      Index of utility modules and functions.
   
   Functions
   ---------
   
   .. autofuncindex::
      :modules: mypackage.utils
      :show-signatures: true
      :sort-by: name

Class Hierarchy Index
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Class Hierarchy
   ===============
   
   .. autoclassindex::
      :modules: mypackage
      :hierarchical: true
      :show-bases: true
      :show-inheritance: true
      
      Class hierarchy for the entire package.
   
   Base Classes
   ------------
   
   .. autoclassindex::
      :modules: mypackage.base
      :filter: is_base_class
      :show-subclasses: true

Custom Grouped Index
~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Grouped API Reference
   =====================
   
   Core Components
   ---------------
   
   .. autoindex::
      :modules: mypackage.core
      :types: class, function
      :format: table
   
   Utilities
   ---------
   
   .. autoindex::
      :modules: mypackage.utils
      :types: function
      :format: compact
   
   Models
   ------
   
   .. autoindex::
      :modules: mypackage.models
      :types: class
      :show-members: true

Alphabetical Index
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Alphabetical Index
   ==================
   
   .. autoindex::
      :group-by: alphabet
      :format: table
      :columns: 3
      
   A
   -
   
   .. autoindex::
      :filter: name.startswith('a')
      :format: compact
   
   B
   -
   
   .. autoindex::
      :filter: name.startswith('b')
      :format: compact

Advanced Features
-----------------

Custom Filtering
~~~~~~~~~~~~~~~~

Filter index entries with Python expressions:

.. code-block:: rst

   .. autoindex::
      :filter: not name.startswith('_') and is_public
      :modules: mypackage
      
      Public symbols only.

Custom Grouping
~~~~~~~~~~~~~~~

Define custom grouping logic:

.. code-block:: python

   # conf.py
   def custom_grouper(obj):
       """Group by custom criteria."""
       if hasattr(obj, 'category'):
           return obj.category
       return 'Other'
   
   autoindex_custom_grouper = custom_grouper

Custom Formatting
~~~~~~~~~~~~~~~~~

Create custom index templates:

**File**: ``_templates/autoindex.html``

.. code-block:: html+jinja

   {% extends "layout.html" %}
   
   {% block body %}
   <div class="autoindex">
     <h1>{{ title }}</h1>
     
     {% for group, items in index_groups %}
     <div class="index-group">
       <h2>{{ group }}</h2>
       
       <table class="index-table">
         <thead>
           <tr>
             <th>Name</th>
             <th>Type</th>
             <th>Module</th>
             <th>Description</th>
           </tr>
         </thead>
         <tbody>
           {% for item in items %}
           <tr>
             <td><a href="{{ item.url }}">{{ item.name }}</a></td>
             <td>{{ item.type }}</td>
             <td>{{ item.module }}</td>
             <td>{{ item.summary }}</td>
           </tr>
           {% endfor %}
         </tbody>
       </table>
     </div>
     {% endfor %}
   </div>
   {% endblock %}

Multi-Level Indexes
~~~~~~~~~~~~~~~~~~~

Create hierarchical index structure:

.. code-block:: rst

   API Reference
   =============
   
   .. toctree::
      :maxdepth: 2
      
      api/modules
      api/classes
      api/functions
   
   **File**: ``api/modules.rst``
   
   Module Index
   ============
   
   .. automodindex::
      :hierarchical: true
      :depth: 3
      
      Complete module hierarchy.
   
   **File**: ``api/classes.rst``
   
   Class Index
   ===========
   
   .. autoclassindex::
      :group-by: module
      :show-bases: true
   
   **File**: ``api/functions.rst``
   
   Function Index
   ==============
   
   .. autofuncindex::
      :group-by: module
      :show-signatures: true

Customization
-------------

Index Styling
~~~~~~~~~~~~~~

**File**: ``_static/autoindex.css``

.. code-block:: css

   .autoindex {
       margin: 2em 0;
   }
   
   .index-group {
       margin: 2em 0;
       padding: 1em;
       background-color: #f9f9f9;
       border-left: 3px solid #3498db;
   }
   
   .index-group h2 {
       margin-top: 0;
       color: #2c3e50;
   }
   
   .index-table {
       width: 100%;
       border-collapse: collapse;
       margin-top: 1em;
   }
   
   .index-table th {
       background-color: #34495e;
       color: white;
       padding: 0.75em;
       text-align: left;
       font-weight: bold;
   }
   
   .index-table td {
       padding: 0.5em 0.75em;
       border-bottom: 1px solid #ddd;
   }
   
   .index-table tr:hover {
       background-color: #ecf0f1;
   }
   
   .index-table a {
       color: #3498db;
       text-decoration: none;
   }
   
   .index-table a:hover {
       text-decoration: underline;
   }
   
   .index-compact {
       columns: 3;
       column-gap: 2em;
   }
   
   .index-compact li {
       break-inside: avoid;
       margin-bottom: 0.5em;
   }

Custom Index Builders
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   from sphinx_autoindex import IndexBuilder
   
   class CustomIndexBuilder(IndexBuilder):
       """Custom index builder."""
       
       def filter_entries(self, entries):
           """Filter index entries."""
           return [e for e in entries if self.should_include(e)]
       
       def should_include(self, entry):
           """Determine if entry should be included."""
           # Custom logic
           if entry.name.startswith('_'):
               return False
           if not entry.docstring:
               return False
           return True
       
       def group_entries(self, entries):
           """Group entries by custom criteria."""
           groups = {}
           for entry in entries:
               key = self.get_group_key(entry)
               if key not in groups:
                   groups[key] = []
               groups[key].append(entry)
           return groups
       
       def get_group_key(self, entry):
           """Get grouping key for entry."""
           if hasattr(entry, 'category'):
               return entry.category
           return entry.type
   
   autoindex_builder_class = CustomIndexBuilder

Best Practices
--------------

Index Organization
~~~~~~~~~~~~~~~~~~

1. **Logical Structure**: Organize indexes by module, type, or purpose
2. **Hierarchical Navigation**: Use multi-level indexes for large projects
3. **Consistent Formatting**: Use same format across related indexes
4. **Clear Headings**: Provide descriptive titles and context

Example structure:

.. code-block:: text

   docs/
   ├── index.rst
   ├── api/
   │   ├── index.rst          # Main API index
   │   ├── modules.rst        # Module index
   │   ├── classes.rst        # Class index
   │   ├── functions.rst      # Function index
   │   └── by-topic/
   │       ├── core.rst       # Core API index
   │       ├── utils.rst      # Utilities index
   │       └── models.rst     # Models index
   └── conf.py

Performance Optimization
~~~~~~~~~~~~~~~~~~~~~~~~

For large codebases:

.. code-block:: python

   # Enable caching
   autoindex_cache_enabled = True
   autoindex_cache_dir = '.autoindex_cache'
   
   # Parallel processing
   autoindex_parallel_build = True
   
   # Limit scope
   autoindex_modules = ['mypackage.*']
   autoindex_ignore = ['*.tests', '*.test_*']

Index Maintenance
~~~~~~~~~~~~~~~~~

Keep indexes current:

.. code-block:: python

   # Automatically update on changes
   autoindex_auto_update = True
   
   # Validate index entries
   autoindex_validate_refs = True
   
   # Warn on missing entries
   autoindex_warn_missing = True

Integration Patterns
~~~~~~~~~~~~~~~~~~~~

Combine with other extensions:

.. code-block:: rst

   API Documentation
   =================
   
   Quick Index
   -----------
   
   .. autoindex::
      :format: compact
      :types: class, function
   
   Detailed Documentation
   ----------------------
   
   .. autosummary::
      :toctree: generated
      :recursive:
      
      mypackage

Troubleshooting
---------------

Missing Index Entries
~~~~~~~~~~~~~~~~~~~~~

**Problem**: Some symbols not appearing in index

**Solution**:

.. code-block:: python

   # Check ignore patterns
   autoindex_ignore = []  # Clear to see all
   
   # Include private members
   autoindex_show_private = True
   
   # Include undocumented
   autoindex_show_undocumented = True
   
   # Debug mode
   autoindex_debug = True

Slow Index Generation
~~~~~~~~~~~~~~~~~~~~~

**Problem**: Index generation takes too long

**Solution**:

.. code-block:: python

   # Enable caching
   autoindex_cache_enabled = True
   
   # Limit scope
   autoindex_modules = ['mypackage.core']  # Specific modules
   
   # Disable expensive features
   autoindex_show_inherited = False
   autoindex_generate_refs = False

Broken Cross-References
~~~~~~~~~~~~~~~~~~~~~~~~

**Problem**: Index references not linking correctly

**Solution**:

.. code-block:: python

   # Validate references
   autoindex_validate_refs = True
   
   # Use full paths
   autoindex_ref_format = 'full'
   
   # Check autodoc configuration
   autodoc_default_options = {
       'members': True,
       'undoc-members': True,
   }

Formatting Issues
~~~~~~~~~~~~~~~~~

**Problem**: Index not displaying correctly

**Solution**:

.. code-block:: python

   # Try different formats
   autoindex_format = 'table'  # or 'compact', 'detailed'
   
   # Check custom CSS
   html_static_path = ['_static']
   html_css_files = ['autoindex.css']
   
   # Validate template
   autoindex_template = 'autoindex.html'

Integration Examples
--------------------

With Sphinx-Autodoc
~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Module Documentation
   ====================
   
   .. automodule:: mypackage.core
      :members:
      :undoc-members:
   
   Module Index
   ------------
   
   .. automodindex::
      :modules: mypackage.core
      :hierarchical: true

With Sphinx-Autosummary
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   API Summary
   ===========
   
   .. autosummary::
      :toctree: generated
      
      mypackage.utils
      mypackage.models
   
   Complete Index
   --------------
   
   .. autoindex::
      :modules: mypackage
      :format: detailed

With Intersphinx
~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   extensions = [
       'sphinx_autoindex',
       'sphinx.ext.intersphinx',
   ]
   
   intersphinx_mapping = {
       'python': ('https://docs.python.org/3', None),
       'numpy': ('https://numpy.org/doc/stable/', None),
   }
   
   # Include external references in index
   autoindex_include_external = True

With Search Extension
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Enhanced search with autoindex
   autoindex_enhance_search = True
   autoindex_search_boost = 1.5
   
   # Custom search priority
   autoindex_search_priority = {
       'class': 1.5,
       'function': 1.2,
       'module': 1.0,
   }

Advanced Usage
--------------

Dynamic Index Generation
~~~~~~~~~~~~~~~~~~~~~~~~

Generate indexes programmatically:

.. code-block:: python

   # conf.py
   def generate_custom_index(app):
       """Generate custom index during build."""
       from sphinx_autoindex import IndexGenerator
       
       generator = IndexGenerator(app)
       index = generator.generate(
           modules=['mypackage'],
           types=['class', 'function'],
           group_by='category'
       )
       
       # Write to file
       output_path = app.outdir / 'custom-index.html'
       generator.write_index(index, output_path)
   
   def setup(app):
       app.connect('build-finished', generate_custom_index)

Multi-Language Indexes
~~~~~~~~~~~~~~~~~~~~~~

Support internationalization:

.. code-block:: python

   # conf.py
   language = 'en'
   locale_dirs = ['locale/']
   
   autoindex_i18n = True
   autoindex_translations = {
       'en': {
           'Module Index': 'Module Index',
           'Class Index': 'Class Index',
       },
       'es': {
           'Module Index': 'Índice de Módulos',
           'Class Index': 'Índice de Clases',
       }
   }

Conditional Indexing
~~~~~~~~~~~~~~~~~~~~

Generate different indexes based on conditions:

.. code-block:: python

   # conf.py
   import os
   
   if os.environ.get('BUILD_TYPE') == 'api':
       autoindex_types = ['class', 'function', 'method']
   else:
       autoindex_types = ['module']


Practical Examples
------------------

Installation
------------

Using pip
~~~~~~~~~

Install the extension:

.. code-block:: bash

   pip install sphinx-autoindex

Or add to your ``requirements.txt``:

.. code-block:: text

   sphinx-autoindex>=1.3.0

Configuration
-------------

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx.ext.autodoc',
       'sphinx_autoindex',
       # ... other extensions
   ]
   
   # Enable auto-indexing
   autoindex_generate = True

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

Complete configuration with all options:

.. code-block:: python

   # Auto-indexing Configuration
   autoindex_generate = True
   autoindex_ignore = ['_build', 'venv', '*.pyc']
   
   # Index Types
   autoindex_modules = True
   autoindex_classes = True
   autoindex_functions = True
   autoindex_methods = True
   autoindex_attributes = True
   autoindex_data = True
   
   # Index Organization
   autoindex_group_by = 'module'  # 'module', 'type', 'alphabet'
   autoindex_sort_by = 'name'     # 'name', 'type', 'module'
   autoindex_hierarchical = True
   
   # Display Options
   autoindex_show_private = False
   autoindex_show_inherited = True
   autoindex_show_undocumented = False
   autoindex_format = 'detailed'  # 'detailed', 'compact', 'table'
   
   # Cross-References
   autoindex_generate_refs = True
   autoindex_ref_prefix = 'ref-'
   autoindex_ref_format = 'short'  # 'short', 'full', 'module.name'
   
   # Template Options
   autoindex_template = 'autoindex.html'
   autoindex_custom_sections = ['Examples', 'See Also']
   
   # Search Integration
   autoindex_enhance_search = True
   autoindex_search_boost = 1.5
   
   # Performance
   autoindex_cache_enabled = True
   autoindex_parallel_build = True

Directives
----------

autoindex Directive
~~~~~~~~~~~~~~~~~~~

Generate automatic index:

.. code-block:: rst

   .. autoindex::
      
      Automatically generated index of all symbols.

With Options
~~~~~~~~~~~~

.. code-block:: rst

   .. autoindex::
      :types: module, class, function
      :group-by: module
      :format: detailed
      :show-private: false
      
      Filtered and organized index.

automodindex Directive
~~~~~~~~~~~~~~~~~~~~~~

Generate module index:

.. code-block:: rst

   .. automodindex::
      :modules: mypackage.*
      :exclude: mypackage.internal
      :hierarchical: true
      
      Index of all modules in mypackage.

autoclassindex Directive
~~~~~~~~~~~~~~~~~~~~~~~~

Generate class index:

.. code-block:: rst

   .. autoclassindex::
      :modules: mypackage
      :show-bases: true
      :show-members: true
      :group-by: module

autofuncindex Directive
~~~~~~~~~~~~~~~~~~~~~~~

Generate function index:

.. code-block:: rst

   .. autofuncindex::
      :modules: mypackage.utils
      :include-methods: true
      :show-signatures: true

autoattribindex Directive
~~~~~~~~~~~~~~~~~~~~~~~~~

Generate attribute index:

.. code-block:: rst

   .. autoattribindex::
      :modules: mypackage.models
      :show-values: true
      :group-by: class

Roles
-----

Index References
~~~~~~~~~~~~~~~~

.. code-block:: rst

   See the :autoindex:`MyClass` documentation.
   
   Use :autofunc:`calculate_total` for totals.
   
   The :automod:`mypackage.utils` module provides utilities.

Practical Examples
------------------

Complete Module Index
~~~~~~~~~~~~~~~~~~~~~

**File**: ``api/index.rst``

.. code-block:: rst

   API Index
   =========
   
   Complete index of all modules, classes, and functions.
   
   .. autoindex::
      :types: module, class, function, method
      :group-by: module
      :format: detailed
      :show-inherited: true
      
      This index is automatically generated from the codebase.

Module-Specific Index
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Utils Module Index
   ==================
   
   .. automodindex::
      :modules: mypackage.utils
      :hierarchical: true
      :show-submodules: true
      
      Index of utility modules and functions.
   
   Functions
   ---------
   
   .. autofuncindex::
      :modules: mypackage.utils
      :show-signatures: true
      :sort-by: name

Class Hierarchy Index
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Class Hierarchy
   ===============
   
   .. autoclassindex::
      :modules: mypackage
      :hierarchical: true
      :show-bases: true
      :show-inheritance: true
      
      Class hierarchy for the entire package.
   
   Base Classes
   ------------
   
   .. autoclassindex::
      :modules: mypackage.base
      :filter: is_base_class
      :show-subclasses: true

Custom Grouped Index
~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Grouped API Reference
   =====================
   
   Core Components
   ---------------
   
   .. autoindex::
      :modules: mypackage.core
      :types: class, function
      :format: table
   
   Utilities
   ---------
   
   .. autoindex::
      :modules: mypackage.utils
      :types: function
      :format: compact
   
   Models
   ------
   
   .. autoindex::
      :modules: mypackage.models
      :types: class
      :show-members: true

Alphabetical Index
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Alphabetical Index
   ==================
   
   .. autoindex::
      :group-by: alphabet
      :format: table
      :columns: 3
      
   A
   -
   
   .. autoindex::
      :filter: name.startswith('a')
      :format: compact
   
   B
   -
   
   .. autoindex::
      :filter: name.startswith('b')
      :format: compact

Advanced Features
-----------------

Custom Filtering
~~~~~~~~~~~~~~~~

Filter index entries with Python expressions:

.. code-block:: rst

   .. autoindex::
      :filter: not name.startswith('_') and is_public
      :modules: mypackage
      
      Public symbols only.

Custom Grouping
~~~~~~~~~~~~~~~

Define custom grouping logic:

.. code-block:: python

   # conf.py
   def custom_grouper(obj):
       """Group by custom criteria."""
       if hasattr(obj, 'category'):
           return obj.category
       return 'Other'
   
   autoindex_custom_grouper = custom_grouper

Custom Formatting
~~~~~~~~~~~~~~~~~

Create custom index templates:

**File**: ``_templates/autoindex.html``

.. code-block:: html+jinja

   {% extends "layout.html" %}
   
   {% block body %}
   <div class="autoindex">
     <h1>{{ title }}</h1>
     
     {% for group, items in index_groups %}
     <div class="index-group">
       <h2>{{ group }}</h2>
       
       <table class="index-table">
         <thead>
           <tr>
             <th>Name</th>
             <th>Type</th>
             <th>Module</th>
             <th>Description</th>
           </tr>
         </thead>
         <tbody>
           {% for item in items %}
           <tr>
             <td><a href="{{ item.url }}">{{ item.name }}</a></td>
             <td>{{ item.type }}</td>
             <td>{{ item.module }}</td>
             <td>{{ item.summary }}</td>
           </tr>
           {% endfor %}
         </tbody>
       </table>
     </div>
     {% endfor %}
   </div>
   {% endblock %}

Multi-Level Indexes
~~~~~~~~~~~~~~~~~~~

Create hierarchical index structure:

.. code-block:: rst

   API Reference
   =============
   
   .. toctree::
      :maxdepth: 2
      
      api/modules
      api/classes
      api/functions
   
   **File**: ``api/modules.rst``
   
   Module Index
   ============
   
   .. automodindex::
      :hierarchical: true
      :depth: 3
      
      Complete module hierarchy.
   
   **File**: ``api/classes.rst``
   
   Class Index
   ===========
   
   .. autoclassindex::
      :group-by: module
      :show-bases: true
   
   **File**: ``api/functions.rst``
   
   Function Index
   ==============
   
   .. autofuncindex::
      :group-by: module
      :show-signatures: true

Customization
-------------

Index Styling
~~~~~~~~~~~~~~

**File**: ``_static/autoindex.css``

.. code-block:: css

   .autoindex {
       margin: 2em 0;
   }
   
   .index-group {
       margin: 2em 0;
       padding: 1em;
       background-color: #f9f9f9;
       border-left: 3px solid #3498db;
   }
   
   .index-group h2 {
       margin-top: 0;
       color: #2c3e50;
   }
   
   .index-table {
       width: 100%;
       border-collapse: collapse;
       margin-top: 1em;
   }
   
   .index-table th {
       background-color: #34495e;
       color: white;
       padding: 0.75em;
       text-align: left;
       font-weight: bold;
   }
   
   .index-table td {
       padding: 0.5em 0.75em;
       border-bottom: 1px solid #ddd;
   }
   
   .index-table tr:hover {
       background-color: #ecf0f1;
   }
   
   .index-table a {
       color: #3498db;
       text-decoration: none;
   }
   
   .index-table a:hover {
       text-decoration: underline;
   }
   
   .index-compact {
       columns: 3;
       column-gap: 2em;
   }
   
   .index-compact li {
       break-inside: avoid;
       margin-bottom: 0.5em;
   }

Custom Index Builders
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   from sphinx_autoindex import IndexBuilder
   
   class CustomIndexBuilder(IndexBuilder):
       """Custom index builder."""
       
       def filter_entries(self, entries):
           """Filter index entries."""
           return [e for e in entries if self.should_include(e)]
       
       def should_include(self, entry):
           """Determine if entry should be included."""
           # Custom logic
           if entry.name.startswith('_'):
               return False
           if not entry.docstring:
               return False
           return True
       
       def group_entries(self, entries):
           """Group entries by custom criteria."""
           groups = {}
           for entry in entries:
               key = self.get_group_key(entry)
               if key not in groups:
                   groups[key] = []
               groups[key].append(entry)
           return groups
       
       def get_group_key(self, entry):
           """Get grouping key for entry."""
           if hasattr(entry, 'category'):
               return entry.category
           return entry.type
   
   autoindex_builder_class = CustomIndexBuilder

Best Practices
--------------

Index Organization
~~~~~~~~~~~~~~~~~~

1. **Logical Structure**: Organize indexes by module, type, or purpose
2. **Hierarchical Navigation**: Use multi-level indexes for large projects
3. **Consistent Formatting**: Use same format across related indexes
4. **Clear Headings**: Provide descriptive titles and context

Example structure:

.. code-block:: text

   docs/
   ├── index.rst
   ├── api/
   │   ├── index.rst          # Main API index
   │   ├── modules.rst        # Module index
   │   ├── classes.rst        # Class index
   │   ├── functions.rst      # Function index
   │   └── by-topic/
   │       ├── core.rst       # Core API index
   │       ├── utils.rst      # Utilities index
   │       └── models.rst     # Models index
   └── conf.py

Performance Optimization
~~~~~~~~~~~~~~~~~~~~~~~~

For large codebases:

.. code-block:: python

   # Enable caching
   autoindex_cache_enabled = True
   autoindex_cache_dir = '.autoindex_cache'
   
   # Parallel processing
   autoindex_parallel_build = True
   
   # Limit scope
   autoindex_modules = ['mypackage.*']
   autoindex_ignore = ['*.tests', '*.test_*']

Index Maintenance
~~~~~~~~~~~~~~~~~

Keep indexes current:

.. code-block:: python

   # Automatically update on changes
   autoindex_auto_update = True
   
   # Validate index entries
   autoindex_validate_refs = True
   
   # Warn on missing entries
   autoindex_warn_missing = True

Integration Patterns
~~~~~~~~~~~~~~~~~~~~

Combine with other extensions:

.. code-block:: rst

   API Documentation
   =================
   
   Quick Index
   -----------
   
   .. autoindex::
      :format: compact
      :types: class, function
   
   Detailed Documentation
   ----------------------
   
   .. autosummary::
      :toctree: generated
      :recursive:
      
      mypackage

Troubleshooting
---------------

Missing Index Entries
~~~~~~~~~~~~~~~~~~~~~

**Problem**: Some symbols not appearing in index

**Solution**:

.. code-block:: python

   # Check ignore patterns
   autoindex_ignore = []  # Clear to see all
   
   # Include private members
   autoindex_show_private = True
   
   # Include undocumented
   autoindex_show_undocumented = True
   
   # Debug mode
   autoindex_debug = True

Slow Index Generation
~~~~~~~~~~~~~~~~~~~~~

**Problem**: Index generation takes too long

**Solution**:

.. code-block:: python

   # Enable caching
   autoindex_cache_enabled = True
   
   # Limit scope
   autoindex_modules = ['mypackage.core']  # Specific modules
   
   # Disable expensive features
   autoindex_show_inherited = False
   autoindex_generate_refs = False

Broken Cross-References
~~~~~~~~~~~~~~~~~~~~~~~~

**Problem**: Index references not linking correctly

**Solution**:

.. code-block:: python

   # Validate references
   autoindex_validate_refs = True
   
   # Use full paths
   autoindex_ref_format = 'full'
   
   # Check autodoc configuration
   autodoc_default_options = {
       'members': True,
       'undoc-members': True,
   }

Formatting Issues
~~~~~~~~~~~~~~~~~

**Problem**: Index not displaying correctly

**Solution**:

.. code-block:: python

   # Try different formats
   autoindex_format = 'table'  # or 'compact', 'detailed'
   
   # Check custom CSS
   html_static_path = ['_static']
   html_css_files = ['autoindex.css']
   
   # Validate template
   autoindex_template = 'autoindex.html'

Integration Examples
--------------------

With Sphinx-Autodoc
~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Module Documentation
   ====================
   
   .. automodule:: mypackage.core
      :members:
      :undoc-members:
   
   Module Index
   ------------
   
   .. automodindex::
      :modules: mypackage.core
      :hierarchical: true

With Sphinx-Autosummary
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   API Summary
   ===========
   
   .. autosummary::
      :toctree: generated
      
      mypackage.utils
      mypackage.models
   
   Complete Index
   --------------
   
   .. autoindex::
      :modules: mypackage
      :format: detailed

With Intersphinx
~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   extensions = [
       'sphinx_autoindex',
       'sphinx.ext.intersphinx',
   ]
   
   intersphinx_mapping = {
       'python': ('https://docs.python.org/3', None),
       'numpy': ('https://numpy.org/doc/stable/', None),
   }
   
   # Include external references in index
   autoindex_include_external = True

With Search Extension
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Enhanced search with autoindex
   autoindex_enhance_search = True
   autoindex_search_boost = 1.5
   
   # Custom search priority
   autoindex_search_priority = {
       'class': 1.5,
       'function': 1.2,
       'module': 1.0,
   }

Advanced Usage
--------------

Dynamic Index Generation
~~~~~~~~~~~~~~~~~~~~~~~~

Generate indexes programmatically:

.. code-block:: python

   # conf.py
   def generate_custom_index(app):
       """Generate custom index during build."""
       from sphinx_autoindex import IndexGenerator
       
       generator = IndexGenerator(app)
       index = generator.generate(
           modules=['mypackage'],
           types=['class', 'function'],
           group_by='category'
       )
       
       # Write to file
       output_path = app.outdir / 'custom-index.html'
       generator.write_index(index, output_path)
   
   def setup(app):
       app.connect('build-finished', generate_custom_index)

Multi-Language Indexes
~~~~~~~~~~~~~~~~~~~~~~

Support internationalization:

.. code-block:: python

   # conf.py
   language = 'en'
   locale_dirs = ['locale/']
   
   autoindex_i18n = True
   autoindex_translations = {
       'en': {
           'Module Index': 'Module Index',
           'Class Index': 'Class Index',
       },
       'es': {
           'Module Index': 'Índice de Módulos',
           'Class Index': 'Índice de Clases',
       }
   }

Conditional Indexing
~~~~~~~~~~~~~~~~~~~~

Generate different indexes based on conditions:

.. code-block:: python

   # conf.py
   import os
   
   if os.environ.get('BUILD_TYPE') == 'api':
       autoindex_types = ['class', 'function', 'method']
   else:
       autoindex_types = ['module']


Practical Examples
------------------

Installation
------------

Using pip
~~~~~~~~~

Install the extension:

.. code-block:: bash

   pip install sphinx-autoindex

Or add to your ``requirements.txt``:

.. code-block:: text

   sphinx-autoindex>=1.3.0

Configuration
-------------

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx.ext.autodoc',
       'sphinx_autoindex',
       # ... other extensions
   ]
   
   # Enable auto-indexing
   autoindex_generate = True

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

Complete configuration with all options:

.. code-block:: python

   # Auto-indexing Configuration
   autoindex_generate = True
   autoindex_ignore = ['_build', 'venv', '*.pyc']
   
   # Index Types
   autoindex_modules = True
   autoindex_classes = True
   autoindex_functions = True
   autoindex_methods = True
   autoindex_attributes = True
   autoindex_data = True
   
   # Index Organization
   autoindex_group_by = 'module'  # 'module', 'type', 'alphabet'
   autoindex_sort_by = 'name'     # 'name', 'type', 'module'
   autoindex_hierarchical = True
   
   # Display Options
   autoindex_show_private = False
   autoindex_show_inherited = True
   autoindex_show_undocumented = False
   autoindex_format = 'detailed'  # 'detailed', 'compact', 'table'
   
   # Cross-References
   autoindex_generate_refs = True
   autoindex_ref_prefix = 'ref-'
   autoindex_ref_format = 'short'  # 'short', 'full', 'module.name'
   
   # Template Options
   autoindex_template = 'autoindex.html'
   autoindex_custom_sections = ['Examples', 'See Also']
   
   # Search Integration
   autoindex_enhance_search = True
   autoindex_search_boost = 1.5
   
   # Performance
   autoindex_cache_enabled = True
   autoindex_parallel_build = True

Directives
----------

autoindex Directive
~~~~~~~~~~~~~~~~~~~

Generate automatic index:

.. code-block:: rst

   .. autoindex::
      
      Automatically generated index of all symbols.

With Options
~~~~~~~~~~~~

.. code-block:: rst

   .. autoindex::
      :types: module, class, function
      :group-by: module
      :format: detailed
      :show-private: false
      
      Filtered and organized index.

automodindex Directive
~~~~~~~~~~~~~~~~~~~~~~

Generate module index:

.. code-block:: rst

   .. automodindex::
      :modules: mypackage.*
      :exclude: mypackage.internal
      :hierarchical: true
      
      Index of all modules in mypackage.

autoclassindex Directive
~~~~~~~~~~~~~~~~~~~~~~~~

Generate class index:

.. code-block:: rst

   .. autoclassindex::
      :modules: mypackage
      :show-bases: true
      :show-members: true
      :group-by: module

autofuncindex Directive
~~~~~~~~~~~~~~~~~~~~~~~

Generate function index:

.. code-block:: rst

   .. autofuncindex::
      :modules: mypackage.utils
      :include-methods: true
      :show-signatures: true

autoattribindex Directive
~~~~~~~~~~~~~~~~~~~~~~~~~

Generate attribute index:

.. code-block:: rst

   .. autoattribindex::
      :modules: mypackage.models
      :show-values: true
      :group-by: class

Roles
-----

Index References
~~~~~~~~~~~~~~~~

.. code-block:: rst

   See the :autoindex:`MyClass` documentation.
   
   Use :autofunc:`calculate_total` for totals.
   
   The :automod:`mypackage.utils` module provides utilities.

Practical Examples
------------------

Complete Module Index
~~~~~~~~~~~~~~~~~~~~~

**File**: ``api/index.rst``

.. code-block:: rst

   API Index
   =========
   
   Complete index of all modules, classes, and functions.
   
   .. autoindex::
      :types: module, class, function, method
      :group-by: module
      :format: detailed
      :show-inherited: true
      
      This index is automatically generated from the codebase.

Module-Specific Index
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Utils Module Index
   ==================
   
   .. automodindex::
      :modules: mypackage.utils
      :hierarchical: true
      :show-submodules: true
      
      Index of utility modules and functions.
   
   Functions
   ---------
   
   .. autofuncindex::
      :modules: mypackage.utils
      :show-signatures: true
      :sort-by: name

Class Hierarchy Index
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Class Hierarchy
   ===============
   
   .. autoclassindex::
      :modules: mypackage
      :hierarchical: true
      :show-bases: true
      :show-inheritance: true
      
      Class hierarchy for the entire package.
   
   Base Classes
   ------------
   
   .. autoclassindex::
      :modules: mypackage.base
      :filter: is_base_class
      :show-subclasses: true

Custom Grouped Index
~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Grouped API Reference
   =====================
   
   Core Components
   ---------------
   
   .. autoindex::
      :modules: mypackage.core
      :types: class, function
      :format: table
   
   Utilities
   ---------
   
   .. autoindex::
      :modules: mypackage.utils
      :types: function
      :format: compact
   
   Models
   ------
   
   .. autoindex::
      :modules: mypackage.models
      :types: class
      :show-members: true

Alphabetical Index
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Alphabetical Index
   ==================
   
   .. autoindex::
      :group-by: alphabet
      :format: table
      :columns: 3
      
   A
   -
   
   .. autoindex::
      :filter: name.startswith('a')
      :format: compact
   
   B
   -
   
   .. autoindex::
      :filter: name.startswith('b')
      :format: compact

Advanced Features
-----------------

Custom Filtering
~~~~~~~~~~~~~~~~

Filter index entries with Python expressions:

.. code-block:: rst

   .. autoindex::
      :filter: not name.startswith('_') and is_public
      :modules: mypackage
      
      Public symbols only.

Custom Grouping
~~~~~~~~~~~~~~~

Define custom grouping logic:

.. code-block:: python

   # conf.py
   def custom_grouper(obj):
       """Group by custom criteria."""
       if hasattr(obj, 'category'):
           return obj.category
       return 'Other'
   
   autoindex_custom_grouper = custom_grouper

Custom Formatting
~~~~~~~~~~~~~~~~~

Create custom index templates:

**File**: ``_templates/autoindex.html``

.. code-block:: html+jinja

   {% extends "layout.html" %}
   
   {% block body %}
   <div class="autoindex">
     <h1>{{ title }}</h1>
     
     {% for group, items in index_groups %}
     <div class="index-group">
       <h2>{{ group }}</h2>
       
       <table class="index-table">
         <thead>
           <tr>
             <th>Name</th>
             <th>Type</th>
             <th>Module</th>
             <th>Description</th>
           </tr>
         </thead>
         <tbody>
           {% for item in items %}
           <tr>
             <td><a href="{{ item.url }}">{{ item.name }}</a></td>
             <td>{{ item.type }}</td>
             <td>{{ item.module }}</td>
             <td>{{ item.summary }}</td>
           </tr>
           {% endfor %}
         </tbody>
       </table>
     </div>
     {% endfor %}
   </div>
   {% endblock %}

Multi-Level Indexes
~~~~~~~~~~~~~~~~~~~

Create hierarchical index structure:

.. code-block:: rst

   API Reference
   =============
   
   .. toctree::
      :maxdepth: 2
      
      api/modules
      api/classes
      api/functions
   
   **File**: ``api/modules.rst``
   
   Module Index
   ============
   
   .. automodindex::
      :hierarchical: true
      :depth: 3
      
      Complete module hierarchy.
   
   **File**: ``api/classes.rst``
   
   Class Index
   ===========
   
   .. autoclassindex::
      :group-by: module
      :show-bases: true
   
   **File**: ``api/functions.rst``
   
   Function Index
   ==============
   
   .. autofuncindex::
      :group-by: module
      :show-signatures: true

Customization
-------------

Index Styling
~~~~~~~~~~~~~~

**File**: ``_static/autoindex.css``

.. code-block:: css

   .autoindex {
       margin: 2em 0;
   }
   
   .index-group {
       margin: 2em 0;
       padding: 1em;
       background-color: #f9f9f9;
       border-left: 3px solid #3498db;
   }
   
   .index-group h2 {
       margin-top: 0;
       color: #2c3e50;
   }
   
   .index-table {
       width: 100%;
       border-collapse: collapse;
       margin-top: 1em;
   }
   
   .index-table th {
       background-color: #34495e;
       color: white;
       padding: 0.75em;
       text-align: left;
       font-weight: bold;
   }
   
   .index-table td {
       padding: 0.5em 0.75em;
       border-bottom: 1px solid #ddd;
   }
   
   .index-table tr:hover {
       background-color: #ecf0f1;
   }
   
   .index-table a {
       color: #3498db;
       text-decoration: none;
   }
   
   .index-table a:hover {
       text-decoration: underline;
   }
   
   .index-compact {
       columns: 3;
       column-gap: 2em;
   }
   
   .index-compact li {
       break-inside: avoid;
       margin-bottom: 0.5em;
   }

Custom Index Builders
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   from sphinx_autoindex import IndexBuilder
   
   class CustomIndexBuilder(IndexBuilder):
       """Custom index builder."""
       
       def filter_entries(self, entries):
           """Filter index entries."""
           return [e for e in entries if self.should_include(e)]
       
       def should_include(self, entry):
           """Determine if entry should be included."""
           # Custom logic
           if entry.name.startswith('_'):
               return False
           if not entry.docstring:
               return False
           return True
       
       def group_entries(self, entries):
           """Group entries by custom criteria."""
           groups = {}
           for entry in entries:
               key = self.get_group_key(entry)
               if key not in groups:
                   groups[key] = []
               groups[key].append(entry)
           return groups
       
       def get_group_key(self, entry):
           """Get grouping key for entry."""
           if hasattr(entry, 'category'):
               return entry.category
           return entry.type
   
   autoindex_builder_class = CustomIndexBuilder

Best Practices
--------------

Index Organization
~~~~~~~~~~~~~~~~~~

1. **Logical Structure**: Organize indexes by module, type, or purpose
2. **Hierarchical Navigation**: Use multi-level indexes for large projects
3. **Consistent Formatting**: Use same format across related indexes
4. **Clear Headings**: Provide descriptive titles and context

Example structure:

.. code-block:: text

   docs/
   ├── index.rst
   ├── api/
   │   ├── index.rst          # Main API index
   │   ├── modules.rst        # Module index
   │   ├── classes.rst        # Class index
   │   ├── functions.rst      # Function index
   │   └── by-topic/
   │       ├── core.rst       # Core API index
   │       ├── utils.rst      # Utilities index
   │       └── models.rst     # Models index
   └── conf.py

Performance Optimization
~~~~~~~~~~~~~~~~~~~~~~~~

For large codebases:

.. code-block:: python

   # Enable caching
   autoindex_cache_enabled = True
   autoindex_cache_dir = '.autoindex_cache'
   
   # Parallel processing
   autoindex_parallel_build = True
   
   # Limit scope
   autoindex_modules = ['mypackage.*']
   autoindex_ignore = ['*.tests', '*.test_*']

Index Maintenance
~~~~~~~~~~~~~~~~~

Keep indexes current:

.. code-block:: python

   # Automatically update on changes
   autoindex_auto_update = True
   
   # Validate index entries
   autoindex_validate_refs = True
   
   # Warn on missing entries
   autoindex_warn_missing = True

Integration Patterns
~~~~~~~~~~~~~~~~~~~~

Combine with other extensions:

.. code-block:: rst

   API Documentation
   =================
   
   Quick Index
   -----------
   
   .. autoindex::
      :format: compact
      :types: class, function
   
   Detailed Documentation
   ----------------------
   
   .. autosummary::
      :toctree: generated
      :recursive:
      
      mypackage

Troubleshooting
---------------

Missing Index Entries
~~~~~~~~~~~~~~~~~~~~~

**Problem**: Some symbols not appearing in index

**Solution**:

.. code-block:: python

   # Check ignore patterns
   autoindex_ignore = []  # Clear to see all
   
   # Include private members
   autoindex_show_private = True
   
   # Include undocumented
   autoindex_show_undocumented = True
   
   # Debug mode
   autoindex_debug = True

Slow Index Generation
~~~~~~~~~~~~~~~~~~~~~

**Problem**: Index generation takes too long

**Solution**:

.. code-block:: python

   # Enable caching
   autoindex_cache_enabled = True
   
   # Limit scope
   autoindex_modules = ['mypackage.core']  # Specific modules
   
   # Disable expensive features
   autoindex_show_inherited = False
   autoindex_generate_refs = False

Broken Cross-References
~~~~~~~~~~~~~~~~~~~~~~~~

**Problem**: Index references not linking correctly

**Solution**:

.. code-block:: python

   # Validate references
   autoindex_validate_refs = True
   
   # Use full paths
   autoindex_ref_format = 'full'
   
   # Check autodoc configuration
   autodoc_default_options = {
       'members': True,
       'undoc-members': True,
   }

Formatting Issues
~~~~~~~~~~~~~~~~~

**Problem**: Index not displaying correctly

**Solution**:

.. code-block:: python

   # Try different formats
   autoindex_format = 'table'  # or 'compact', 'detailed'
   
   # Check custom CSS
   html_static_path = ['_static']
   html_css_files = ['autoindex.css']
   
   # Validate template
   autoindex_template = 'autoindex.html'

Integration Examples
--------------------

With Sphinx-Autodoc
~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Module Documentation
   ====================
   
   .. automodule:: mypackage.core
      :members:
      :undoc-members:
   
   Module Index
   ------------
   
   .. automodindex::
      :modules: mypackage.core
      :hierarchical: true

With Sphinx-Autosummary
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   API Summary
   ===========
   
   .. autosummary::
      :toctree: generated
      
      mypackage.utils
      mypackage.models
   
   Complete Index
   --------------
   
   .. autoindex::
      :modules: mypackage
      :format: detailed

With Intersphinx
~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   extensions = [
       'sphinx_autoindex',
       'sphinx.ext.intersphinx',
   ]
   
   intersphinx_mapping = {
       'python': ('https://docs.python.org/3', None),
       'numpy': ('https://numpy.org/doc/stable/', None),
   }
   
   # Include external references in index
   autoindex_include_external = True

With Search Extension
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Enhanced search with autoindex
   autoindex_enhance_search = True
   autoindex_search_boost = 1.5
   
   # Custom search priority
   autoindex_search_priority = {
       'class': 1.5,
       'function': 1.2,
       'module': 1.0,
   }

Advanced Usage
--------------

Dynamic Index Generation
~~~~~~~~~~~~~~~~~~~~~~~~

Generate indexes programmatically:

.. code-block:: python

   # conf.py
   def generate_custom_index(app):
       """Generate custom index during build."""
       from sphinx_autoindex import IndexGenerator
       
       generator = IndexGenerator(app)
       index = generator.generate(
           modules=['mypackage'],
           types=['class', 'function'],
           group_by='category'
       )
       
       # Write to file
       output_path = app.outdir / 'custom-index.html'
       generator.write_index(index, output_path)
   
   def setup(app):
       app.connect('build-finished', generate_custom_index)

Multi-Language Indexes
~~~~~~~~~~~~~~~~~~~~~~

Support internationalization:

.. code-block:: python

   # conf.py
   language = 'en'
   locale_dirs = ['locale/']
   
   autoindex_i18n = True
   autoindex_translations = {
       'en': {
           'Module Index': 'Module Index',
           'Class Index': 'Class Index',
       },
       'es': {
           'Module Index': 'Índice de Módulos',
           'Class Index': 'Índice de Clases',
       }
   }

Conditional Indexing
~~~~~~~~~~~~~~~~~~~~

Generate different indexes based on conditions:

.. code-block:: python

   # conf.py
   import os
   
   if os.environ.get('BUILD_TYPE') == 'api':
       autoindex_types = ['class', 'function', 'method']
   else:
       autoindex_types = ['module']

Additional Resources
--------------------
- :doc:`sphinx-autoapi` - Automatic API docs
- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `Sphinx autodoc <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_
Related Extensions
~~~~~~~~~~~~~~~~~~
- :doc:`sphinx-autodoc-example` - Automatic Python documentation
- :doc:`sphinx-autosummary-example` - Summary generation
- :doc:`sphinx-autoapi-example` - API documentation generator
- :doc:`sphinx-autopackagesummary-example` - Package summaries
External Resources
- Sphinx Indexing: https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#index-generating-markup
- Python Module Index: https://docs.python.org/3/py-modindex.html
Summary
-------
sphinx-autoindex provides powerful automatic index generation:
- **Comprehensive Indexing**: Modules, classes, functions, attributes
- **Flexible Organization**: Group by module, type, alphabet
- **Multiple Formats**: Detailed, compact, table formats
- **Smart Cross-Referencing**: Automatic link generation
- **Customizable**: Templates, styling, filtering
- **Performance**: Caching and parallel processing
- **Integration**: Works with autodoc, autosummary, intersphinx
Perfect for maintaining comprehensive API indexes in large documentation projects.


Summary
-------
sphinx-autoindex provides powerful automatic index generation:
- **Comprehensive Indexing**: Modules, classes, functions, attributes
- **Flexible Organization**: Group by module, type, alphabet
- **Multiple Formats**: Detailed, compact, table formats
- **Smart Cross-Referencing**: Automatic link generation
- **Customizable**: Templates, styling, filtering
- **Performance**: Caching and parallel processing
- **Integration**: Works with autodoc, autosummary, intersphinx
Perfect for maintaining comprehensive API indexes in large documentation projects.


Summary
-------
sphinx-autoindex provides powerful automatic index generation:
- **Comprehensive Indexing**: Modules, classes, functions, attributes
- **Flexible Organization**: Group by module, type, alphabet
- **Multiple Formats**: Detailed, compact, table formats
- **Smart Cross-Referencing**: Automatic link generation
- **Customizable**: Templates, styling, filtering
- **Performance**: Caching and parallel processing
- **Integration**: Works with autodoc, autosummary, intersphinx
Perfect for maintaining comprehensive API indexes in large documentation projects.

