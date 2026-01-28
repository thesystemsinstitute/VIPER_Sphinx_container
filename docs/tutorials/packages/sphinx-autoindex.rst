Sphinx-Autoindex Tutorial
=========================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-autoindex/>`_
   - :doc:`See Working Example <../../examples/sphinx-autoindex-example>`


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

Installation
------------

sphinx-autoindex is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinx_autoindex; print('Installed')"

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

Practical Examples
------------------

Example 1: Complete Package Index
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Project structure:

.. code-block:: text

   mypackage/
   ├── __init__.py
   ├── core.py
   ├── utils.py
   └── api/
       ├── __init__.py
       ├── client.py
       └── server.py

``docs/api/index.rst``:

.. code-block:: rst

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
     kensai-sphinx:latest \
     sphinx-build -b html /project/docs /project/docs/_build/html

Generate Index Only
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Generate index without full build
   docker run --rm \
     -v $(pwd):/project \
     kensai-sphinx:latest \
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
               kensai-sphinx:latest \
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

Additional Resources
--------------------

- :doc:`sphinx-autoapi` - Automatic API docs
- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `Sphinx autodoc <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_
