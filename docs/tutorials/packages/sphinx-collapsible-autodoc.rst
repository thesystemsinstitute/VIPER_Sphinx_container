Sphinx-Collapsible-Autodoc Tutorial
====================================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-collapsible-autodoc/>`_
   - `API Documentation <../../pdoc/sphinx_collapsible_autodoc/index.html>`_
   - `Manual <https://github.com/tzing/sphinx-collapse>`_
   - :doc:`Working Example <../../examples/sphinx-collapsible-autodoc-example>`


.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinx-collapsible-autodoc to create collapsible sections in your API documentation for better readability.

What is Sphinx-Collapsible-Autodoc?
------------------------------------

sphinx-collapsible-autodoc is a Sphinx extension that provides:

- Collapsible function/method documentation
- Expandable class members
- Cleaner API documentation layout
- Customizable collapse behavior
- Better mobile experience
- JavaScript-based interaction
- Configurable initial state
- Selective collapse control
- Improved navigation
- Reduced page length

This makes large API documentation more manageable by allowing users to expand only what they need.


The sphinx-collapsible-autodoc extension adds collapsible sections to autodoc documentation, improving readability for large APIs.

Installation
------------

sphinx-collapsible-autodoc is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinx_collapsible_autodoc; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx.ext.autodoc',
       'sphinx_collapsible_autodoc',
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = [
       'sphinx.ext.autodoc',
       'sphinx_collapsible_autodoc',
   ]
   
   # Collapsible autodoc configuration
   collapsible_autodoc_default_state = 'collapsed'  # collapsed, expanded
   collapsible_autodoc_animate = True
   collapsible_autodoc_animation_duration = 300  # milliseconds
   
   # Control what gets collapsed
   collapsible_autodoc_collapse_methods = True
   collapsible_autodoc_collapse_functions = True
   collapsible_autodoc_collapse_classes = False
   collapsible_autodoc_collapse_attributes = True
   
   # Icons and styling
   collapsible_autodoc_expand_icon = '▶'
   collapsible_autodoc_collapse_icon = '▼'
   collapsible_autodoc_icon_position = 'left'  # left, right
   
   # Behavior
   collapsible_autodoc_remember_state = True  # Use localStorage
   collapsible_autodoc_expand_all_button = True
   collapsible_autodoc_collapse_all_button = True


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Basic Setup
~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx.ext.autodoc',
       'sphinx_collapsible_autodoc',
   ]

Options
~~~~~~~

.. code-block:: python

   collapsible_autodoc_default = 'collapsed'  # or 'expanded'
   collapsible_autodoc_sections = ['methods', 'attributes']

Basic Usage
-----------

Auto-Collapsible Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Simply enable the extension and all autodoc content becomes collapsible:

.. code-block:: rst

   .. autoclass:: mylib.Client
      :members:
      :undoc-members:

All methods will be collapsible by default.

Control Per-Item Collapse
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. autoclass:: mylib.Client
      :members:
      :collapsible: methods
      :default-state: collapsed

Disable Collapsing
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. autofunction:: mylib.important_function
      :no-collapse:

   Utility Functions
   =================
   
   Collection of utility functions for common tasks.
   
   .. automodule:: mylib.utils
      :members:
      :collapsible: functions
      :default-state: collapsed
   
   .. tip::
      
      Use the expand all button to view all function documentation at once.

Example 3: Grouped Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/api/complete.rst``:

.. code-block:: rst

   Complete API Reference
   ======================
   
   Core Components
   ---------------
   
   Main client class (always expanded):
   
   .. autoclass:: mylib.Client
      :members: __init__, connect, disconnect
      :no-collapse:
   
   Request Methods
   ---------------
   
   HTTP request methods (collapsed by default):
   
   .. autoclass:: mylib.Client
      :members: get, post, put, delete, patch
      :collapsible: methods
      :default-state: collapsed
      :noindex:
   
   Advanced Features
   -----------------
   
   Advanced methods (collapsed):
   
   .. autoclass:: mylib.Client
      :members: batch_request, stream, upload_file
      :collapsible: methods
      :default-state: collapsed
      :noindex:

Advanced Features
-----------------

Custom Icons
~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   collapsible_autodoc_expand_icon = '➕'
   collapsible_autodoc_collapse_icon = '➖'

Group Behavior
~~~~~~~~~~~~~~

.. code-block:: rst

   .. collapsible-group:: user-methods
      
      .. automethod:: mylib.Client.get_user
      .. automethod:: mylib.Client.create_user
      .. automethod:: mylib.Client.update_user

Expand/Collapse All Buttons
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Add buttons to page
   collapsible_autodoc_expand_all_button = True
   collapsible_autodoc_collapse_all_button = True
   collapsible_autodoc_button_position = 'top'  # top, bottom, both

Remember State
~~~~~~~~~~~~~~

.. code-block:: python

   # Save state in browser localStorage
   collapsible_autodoc_remember_state = True

Custom CSS
~~~~~~~~~~

Create ``_static/collapsible-custom.css``:

.. code-block:: css

   /* Custom styling for collapsible sections */
   .collapsible-autodoc {
       border-left: 3px solid #007bff;
       padding-left: 10px;
       margin: 10px 0;
   }
   
   .collapsible-autodoc-header {
       cursor: pointer;
       background-color: #f8f9fa;
       padding: 8px 12px;
       border-radius: 4px;
       transition: background-color 0.2s;
   }
   
   .collapsible-autodoc-header:hover {
       background-color: #e9ecef;
   }
   
   .collapsible-autodoc-content {
       padding: 10px 0;
   }
   
   .collapsible-autodoc-icon {
       color: #007bff;
       font-weight: bold;
       margin-right: 8px;
   }

Add to ``conf.py``:

.. code-block:: python

   html_static_path = ['_static']
   html_css_files = ['collapsible-custom.css']

JavaScript Customization
~~~~~~~~~~~~~~~~~~~~~~~~

Create ``_static/collapsible-custom.js``:

.. code-block:: javascript

   // Custom collapse/expand behavior
   document.addEventListener('DOMContentLoaded', function() {
       // Expand all on Ctrl+E
       document.addEventListener('keydown', function(e) {
           if (e.ctrlKey && e.key === 'e') {
               document.querySelectorAll('.collapsible-autodoc')
                   .forEach(el => el.classList.add('expanded'));
           }
       });
       
       // Collapse all on Ctrl+C
       document.addEventListener('keydown', function(e) {
           if (e.ctrlKey && e.key === 'c') {
               document.querySelectorAll('.collapsible-autodoc')
                   .forEach(el => el.classList.remove('expanded'));
           }
       });
   });

Add to ``conf.py``:

.. code-block:: python

   html_js_files = ['collapsible-custom.js']

Docker Integration
------------------

Build Documentation
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     kensai-sphinx:latest \
     sphinx-build -b html /project/docs /project/docs/_build/html

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Build Collapsible Docs
   
   on: [push]
   
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Build Documentation
           run: |
             docker run --rm -v $(pwd):/project \
               kensai-sphinx:latest \
               sphinx-build -b html /project/docs /project/docs/_build/html

Best Practices
--------------

1. **Collapse Long Sections**
   
   Use for classes with many methods

2. **Keep Important Items Expanded**
   
   Don't collapse __init__ or main functions

3. **Group Related Items**
   
   Use collapsible groups for organization

4. **Provide Navigation**
   
   Add expand/collapse all buttons

5. **Test Mobile View**
   
   Ensure collapsible works on touch devices

6. **Use Meaningful Icons**
   
   Choose clear expand/collapse indicators

Troubleshooting
---------------

Collapsing Not Working
~~~~~~~~~~~~~~~~~~~~~~

**Solution:**

Check JavaScript is enabled:

.. code-block:: python

   html_theme_options = {
       'javascript_enabled': True
   }

Icons Not Showing
~~~~~~~~~~~~~~~~~

**Solution:**

Check icon configuration:

.. code-block:: python

   collapsible_autodoc_expand_icon = '▶'
   collapsible_autodoc_collapse_icon = '▼'

State Not Remembered
~~~~~~~~~~~~~~~~~~~~

**Solution:**

Enable localStorage:

.. code-block:: python

   collapsible_autodoc_remember_state = True

Animation Issues
~~~~~~~~~~~~~~~~

**Solution:**

Adjust animation duration:

.. code-block:: python

   collapsible_autodoc_animation_duration = 200

Next Steps
----------

1. Enable collapsible autodoc
2. Configure default state
3. Customize styling
4. Add expand/collapse all buttons
5. Test on different devices

Additional Resources
--------------------

- :doc:`sphinx-autodoc-defaultargs` - Show default values
- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `Sphinx Autodoc <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_
