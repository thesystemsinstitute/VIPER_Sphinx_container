Sphinx-Collapsible-Autodoc Tutorial
====================================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-collapsible-autodoc/>`_
   - :doc:`See Working Example <../../examples/sphinx-collapsible-autodoc-example>`


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

Practical Examples
------------------

Example 1: Large API Class
~~~~~~~~~~~~~~~~~~~~~~~~~~~

``mylib/api.py``:

.. code-block:: python

   """API client with many methods."""
   
   class APIClient:
       """
       Comprehensive API client.
       
       This class provides access to all API endpoints with
       dozens of methods organized by category.
       """
       
       def __init__(self, api_key: str, base_url: str = "https://api.example.com"):
           """Initialize API client."""
           self.api_key = api_key
           self.base_url = base_url
       
       # User management methods (10+ methods)
       def get_user(self, user_id: int):
           """Get user by ID."""
           pass
       
       def create_user(self, name: str, email: str):
           """Create new user."""
           pass
       
       def update_user(self, user_id: int, **kwargs):
           """Update user fields."""
           pass
       
       def delete_user(self, user_id: int):
           """Delete user."""
           pass
       
       def list_users(self, page: int = 1, per_page: int = 10):
           """List users with pagination."""
           pass
       
       # Post management methods (10+ methods)
       def get_post(self, post_id: int):
           """Get post by ID."""
           pass
       
       def create_post(self, title: str, content: str):
           """Create new post."""
           pass
       
       def update_post(self, post_id: int, **kwargs):
           """Update post."""
           pass
       
       def delete_post(self, post_id: int):
           """Delete post."""
           pass
       
       def list_posts(self, user_id: int = None):
           """List posts."""
           pass
       
       # Comment management methods (10+ methods)
       def get_comment(self, comment_id: int):
           """Get comment by ID."""
           pass
       
       def create_comment(self, post_id: int, text: str):
           """Create new comment."""
           pass
       
       def update_comment(self, comment_id: int, text: str):
           """Update comment."""
           pass
       
       def delete_comment(self, comment_id: int):
           """Delete comment."""
           pass
       
       def list_comments(self, post_id: int):
           """List comments for post."""
           pass

``docs/api/client.rst``:

.. code-block:: rst

   API Client
   ==========
   
   .. autoclass:: mylib.api.APIClient
      :members:
      :member-order: groupwise
      :collapsible: methods
      :default-state: collapsed
   
   The API client provides comprehensive access to all endpoints.
   Click on method names to expand documentation.
   
   User Management
   ---------------
   
   Methods for managing users:
   
   - :meth:`~mylib.api.APIClient.get_user`
   - :meth:`~mylib.api.APIClient.create_user`
   - :meth:`~mylib.api.APIClient.update_user`
   - :meth:`~mylib.api.APIClient.delete_user`
   - :meth:`~mylib.api.APIClient.list_users`

Example 2: Module with Many Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``mylib/utils.py``:

.. code-block:: python

   """Utility functions."""
   
   def format_date(date, format='%Y-%m-%d'):
       """Format date to string."""
       pass
   
   def parse_date(date_string, format='%Y-%m-%d'):
       """Parse date from string."""
       pass
   
   def format_currency(amount, currency='USD'):
       """Format amount as currency."""
       pass
   
   def parse_currency(currency_string):
       """Parse currency string to amount."""
       pass
   
   def format_phone(phone, country='US'):
       """Format phone number."""
       pass
   
   def validate_email(email):
       """Validate email address."""
       pass
   
   def sanitize_html(html):
       """Sanitize HTML content."""
       pass
   
   def slugify(text):
       """Convert text to URL slug."""
       pass
   
   def truncate(text, max_length=100):
       """Truncate text to max length."""
       pass
   
   def highlight(text, query):
       """Highlight search query in text."""
       pass

``docs/api/utils.rst``:

.. code-block:: rst

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
