Sphinx-Wagtail-Theme Tutorial
=============================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-wagtail-theme/>`_
   - `API Documentation <../../pdoc/sphinx_wagtail_theme/index.html>`_
   - `Manual <https://github.com/wagtail/sphinx_wagtail_theme>`_

This tutorial demonstrates how to use sphinx-wagtail-theme, a modern, clean documentation theme inspired by Wagtail CMS documentation.

What is Sphinx-Wagtail-Theme?
------------------------------
sphinx-wagtail-theme is a Sphinx theme that provides:

- Clean, modern design
- Responsive mobile layout
- Dark mode support
- Customizable color schemes
- Clear typography
- Easy navigation
- Code syntax highlighting
- Search functionality
- Sidebar navigation
- Breadcrumb trails
- Professional appearance
- Accessible design

Based on the Wagtail CMS documentation style, it's perfect for creating professional, user-friendly documentation.

The sphinx-wagtail-theme brings the clean, modern design of Wagtail CMS to Sphinx documentation with responsive layouts and elegant typography.

Theme Features
--------------

Clean Design
~~~~~~~~~~~~

The Wagtail theme features:

- Modern, minimal interface
- Responsive grid layout
- Mobile-friendly navigation
- Clean typography
- Accessible color scheme

Navigation
~~~~~~~~~~

Sidebar navigation with:

- Collapsible sections
- Breadcrumb trails
- Quick search
- Table of contents

Content Display
~~~~~~~~~~~~~~~

Optimized content presentation:

- Wide reading column
- Syntax-highlighted code blocks
- Formatted tables
- Image galleries


Installation
------------

sphinx-wagtail-theme is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinx_wagtail_theme; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   import sphinx_wagtail_theme
   
   html_theme = 'sphinx_wagtail_theme'
   html_theme_path = [sphinx_wagtail_theme.get_html_theme_path()]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import sphinx_wagtail_theme
   
   html_theme = 'sphinx_wagtail_theme'
   html_theme_path = [sphinx_wagtail_theme.get_html_theme_path()]
   
   # Theme options
   html_theme_options = {
       'project_name': 'My Project',
       'github_url': 'https://github.com/myorg/myproject',
       'logo': 'images/logo.png',
       'logo_alt': 'Project Logo',
       'footer_links': True,

       # Logo
       'logo': 'logo.png',
       'logo_alt': 'Project Logo',
       'logo_height': 59,
       'logo_url': '/',
       'logo_width': 45,
       
       # Colors
       'primary_color': '#007d7e',
       'secondary_color': '#43b1b0',
       'accent_color': '#f37e77',
       
       # Navigation
       'sidebar_width': '270px',
       'page_width': '1200px',
       
       # Features
       'github_url': 'https://github.com/user/repo',
       'github_button': True,
       'github_type': 'star',
       'github_count': True,
       
       # Footer
       'footer_show_prev_next': True,
       'footer_text': '© 2026 Your Company',
       
       # Misc
       'analytics_id': 'G-XXXXXXXXXX',
       'show_sidebar': True,
       'canonical_url': 'https://docs.example.com',
   }
   
   # Sidebar templates
   html_sidebars = {
       '**': [
           'searchbox.html',
           'globaltoc.html',
           'relations.html',
       ]
   }


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Basic Setup
~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   import sphinx_wagtail_theme
   
   html_theme = 'sphinx_wagtail_theme'
   html_theme_path = [sphinx_wagtail_theme.get_html_theme_path()]

Theme Options
~~~~~~~~~~~~~

.. code-block:: python

   html_theme_options = {
       'project_name': 'My Project',
       'github_url': 'https://github.com/myorg/myproject',
       'logo': 'images/logo.png',
       'logo_alt': 'Project Logo',
       'footer_links': True,
   }

Color Customization
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   html_theme_options = {
       'primary_color': '#43b1b0',
       'secondary_color': '#262626',
       'accent_color': '#e74c3c',
   }

Layout Options
--------------

Sidebar Configuration
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   html_theme_options = {
       'navigation_depth': 4,
       'collapse_navigation': False,
       'display_version': True,
       'sticky_navigation': True,
   }

Header Customization
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   html_theme_options = {
       'header_links': [
           ('Home', '/'),
           ('Docs', '/docs/'),
           ('API', '/api/'),
       ],
   }

Basic Usage
-----------

Enable Theme
~~~~~~~~~~~~

.. code-block:: python

   import sphinx_wagtail_theme
   
   html_theme = 'sphinx_wagtail_theme'
   html_theme_path = [sphinx_wagtail_theme.get_html_theme_path()]

Add Logo
~~~~~~~~

.. code-block:: python

   html_theme_options = {
       'logo': 'logo.png',
       'logo_alt': 'Company Logo',
   }

Set Colors
~~~~~~~~~~

.. code-block:: python

   html_theme_options = {
       'primary_color': '#007d7e',
       'secondary_color': '#43b1b0',
   }

Add GitHub Link
~~~~~~~~~~~~~~~

.. code-block:: python

   html_theme_options = {
       'github_url': 'https://github.com/user/repo',
       'github_button': True,
   }

   MyProduct Documentation
   =======================
   
   Welcome to MyProduct - the best solution for your needs.
   
   .. toctree::
      :maxdepth: 2
      :caption: Getting Started
      
      quickstart
      installation
      tutorial
   
   .. toctree::
      :maxdepth: 2
      :caption: User Guide
      
      guides/basic-usage
      guides/advanced-features
      guides/best-practices
   
   .. toctree::
      :maxdepth: 2
      :caption: API Reference
      
      api/client
      api/models
      api/exceptions
   
   Features
   --------
   
   .. grid:: 3
   
       .. grid-item-card:: Easy to Use
           
           Simple API with great defaults
           
       .. grid-item-card:: Fast
           
           Optimized for performance
           
       .. grid-item-card:: Extensible
           
           Plugin architecture

Example 2: API Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``conf.py``:

.. code-block:: python

   import sphinx_wagtail_theme
   
   project = 'API Documentation'
   
   extensions = [
       'sphinx.ext.autodoc',
       'sphinx.ext.napoleon',
       'sphinx.ext.intersphinx',
       'sphinx.ext.viewcode',
       'sphinxcontrib.httpdomain',
   ]
   
   html_theme = 'sphinx_wagtail_theme'
   html_theme_path = [sphinx_wagtail_theme.get_html_theme_path()]
   
   html_theme_options = {
       'logo': '_static/api-logo.png',
       'primary_color': '#10b981',
       'secondary_color': '#059669',
       
       'github_url': 'https://github.com/company/api',
       'github_button': True,
       
       'footer_text': 'API v2.0 | © 2026 Company',
   }
   
   # Sidebar with search and TOC
   html_sidebars = {
       '**': [
           'searchbox.html',
           'globaltoc.html',
           'sourcelink.html',
       ]
   }

``docs/api/rest.rst``:

.. code-block:: rst

   REST API
   ========
   
   Authentication
   --------------
   
   All API requests require authentication.
   
   .. http:get:: /api/v2/users
      
      Get list of users.
      
      **Example request**:
      
      .. sourcecode:: http
      
         GET /api/v2/users HTTP/1.1
         Host: api.example.com
         Authorization: Bearer TOKEN
      
      **Example response**:
      
      .. sourcecode:: http
      
         HTTP/1.1 200 OK
         Content-Type: application/json
         
         {
           "users": [
             {"id": 1, "name": "Alice"},
             {"id": 2, "name": "Bob"}
           ]
         }
      
      :reqheader Authorization: Bearer token
      :statuscode 200: Success
      :statuscode 401: Unauthorized
      :statuscode 500: Server error
   
   .. http:post:: /api/v2/users
      
      Create a new user.
      
      **Example request**:
      
      .. sourcecode:: http
      
         POST /api/v2/users HTTP/1.1
         Host: api.example.com
         Content-Type: application/json
         
         {
           "name": "Charlie",
           "email": "charlie@example.com"
         }
      
      :jsonparam string name: User's name
      :jsonparam string email: User's email
      :statuscode 201: Created
      :statuscode 400: Bad request

Example 3: Internal Wiki
~~~~~~~~~~~~~~~~~~~~~~~~~

``conf.py``:

.. code-block:: python

   import sphinx_wagtail_theme
   
   project = 'Engineering Wiki'
   
   extensions = [
       'sphinx.ext.autosectionlabel',
       'sphinx.ext.todo',
       'myst_parser',
   ]
   
   html_theme = 'sphinx_wagtail_theme'
   html_theme_path = [sphinx_wagtail_theme.get_html_theme_path()]
   
   html_theme_options = {
       'logo': '_static/company-logo.png',
       'primary_color': '#6366f1',
       'secondary_color': '#818cf8',
       
       'footer_text': 'Internal Documentation - Confidential',
       'show_sidebar': True,
   }
   
   # Enable todo extension
   todo_include_todos = True
   
   # Markdown support
   source_suffix = {
       '.rst': 'restructuredtext',
       '.md': 'markdown',
   }

``docs/engineering/deployment.rst``:

.. code-block:: rst

   Deployment Guide
   ================
   
   This guide covers deploying our applications.
   
   .. contents:: Table of Contents
      :local:
      :depth: 2
   
   Prerequisites
   -------------
   
   .. important::
      
      Ensure you have access to:
      
      - AWS Console
      - GitHub repository
      - Slack deployment channel
   
   Staging Deployment
   ------------------
   
   .. code-block:: bash
   
      # Deploy to staging
      ./deploy.sh staging
   
   .. warning::
      
      Always test in staging before production!
   
   Production Deployment
   ---------------------
   
   .. code-block:: bash
   
      # Production deployment
      ./deploy.sh production
   
   Post-Deployment
   ---------------
   
   .. todo::
      
      Add monitoring dashboard link
   
   Checklist:
   
   - [ ] Verify health endpoints
   - [ ] Check error rates
   - [ ] Monitor performance metrics
   - [ ] Update changelog

Advanced Features
-----------------

Custom Color Scheme
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   html_theme_options = {
       # Main colors
       'primary_color': '#1e40af',
       'secondary_color': '#3b82f6',
       'accent_color': '#f59e0b',
       
       # Additional colors
       'text_color': '#1f2937',
       'link_color': '#2563eb',
       'border_color': '#e5e7eb',
   }

Multiple Sidebars
~~~~~~~~~~~~~~~~~

.. code-block:: python

   html_sidebars = {
       '**': [
           'searchbox.html',
           'globaltoc.html',
           'relations.html',
           'sourcelink.html',
           'custom-sidebar.html',
       ]
   }

Custom Templates
~~~~~~~~~~~~~~~~

Create ``_templates/custom-sidebar.html``:

.. code-block:: html

   <div class="sidebar-block">
       <h3>Quick Links</h3>
       <ul>
           <li><a href="/quickstart.html">Quick Start</a></li>
           <li><a href="/api/">API Reference</a></li>
           <li><a href="/faq.html">FAQ</a></li>
       </ul>
   </div>

Code Highlighting
~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Use Pygments style
   pygments_style = 'monokai'
   
   # Or define custom
   html_theme_options = {
       'code_font': '"Source Code Pro", monospace',
       'code_bg_color': '#f8f9fa',
   }

Navigation Depth
~~~~~~~~~~~~~~~~

.. code-block:: python

   html_theme_options = {
       'navigation_depth': 4,
       'collapse_navigation': False,
       'sticky_navigation': True,
   }

Docker Integration
------------------

Build with Theme
~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     kensai-sphinx:latest \
     sphinx-build -b html /project/docs /project/docs/_build/html

Preview Locally
~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm -p 8000:8000 \
     -v $(pwd):/project \
     kensai-sphinx:latest \
     python -m http.server 8000 -d /project/docs/_build/html

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Build Documentation
   
   on:
     push:
       paths:
         - 'docs/**'
   
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Build Docs
           run: |
             docker run --rm -v $(pwd):/project \
               kensai-sphinx:latest \
               sphinx-build -b html /project/docs /project/docs/_build/html
         
         - name: Deploy to GitHub Pages
           uses: peaceiris/actions-gh-pages@v3
           with:
             github_token: ${{ secrets.GITHUB_TOKEN }}
             publish_dir: ./docs/_build/html

Best Practices
--------------

1. **Use Consistent Colors**
   
   Match your brand colors:
   
   .. code-block:: python
   
      html_theme_options = {
          'primary_color': '#brand-color',
      }

2. **Optimize Logo**
   
   Use SVG for scalability or optimize PNG:
   
   .. code-block:: bash
   
      # Optimize with pngquant
      pngquant logo.png --output logo-optimized.png

3. **Organize Sidebars**
   
   Keep navigation simple and focused

4. **Add Search**
   
   Always include searchbox.html

5. **Test Responsive**
   
   Check on mobile devices

6. **Custom CSS Last**
   
   Override theme styles with custom.css

Common Patterns
---------------

Documentation Structure
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   html_sidebars = {
       '**': ['searchbox.html', 'globaltoc.html'],
       'index': ['searchbox.html'],
   }

.. code-block:: rst

   # index.rst
   .. toctree::
      :maxdepth: 2
      :caption: Contents:
      
      getting-started/index
      user-guide/index
      api/index
      contributing

Troubleshooting
---------------

Theme Not Loading
~~~~~~~~~~~~~~~~~

**Solution:**

Check theme path:

.. code-block:: python

   import sphinx_wagtail_theme
   
   html_theme = 'sphinx_wagtail_theme'
   html_theme_path = [sphinx_wagtail_theme.get_html_theme_path()]

Colors Not Changing
~~~~~~~~~~~~~~~~~~~

**Solution:**

Clear build directory:

.. code-block:: bash

   rm -rf docs/_build
   sphinx-build -b html docs docs/_build/html

Logo Not Displaying
~~~~~~~~~~~~~~~~~~~

**Solution:**

Check path relative to _static:

.. code-block:: python

   html_static_path = ['_static']
   html_theme_options = {
       'logo': 'logo.png',  # Must be in _static/logo.png
   }

Sidebar Missing
~~~~~~~~~~~~~~~

**Solution:**

Define html_sidebars:

.. code-block:: python

   html_sidebars = {
       '**': ['searchbox.html', 'globaltoc.html']
   }

Next Steps
----------

1. Configure theme with your branding
2. Customize colors to match brand
3. Add logo and favicon
4. Organize sidebar navigation
5. Test responsive design
6. Deploy documentation


Practical Examples
------------------

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   import sphinx_wagtail_theme
   
   html_theme = 'sphinx_wagtail_theme'
   html_theme_path = [sphinx_wagtail_theme.get_html_theme_path()]


Content Examples
----------------

Code Blocks
~~~~~~~~~~~

Python code with syntax highlighting:

.. code-block:: python

   def calculate_total(items):
       """Calculate total price of items."""
       return sum(item.price for item in items)

Admonitions
~~~~~~~~~~~

.. code-block:: rst

   .. note::
      Wagtail theme styles admonitions beautifully.

   .. warning::
      Important information stands out clearly.

   .. tip::
      Helpful tips are easy to spot.

.. note::
   Wagtail theme styles admonitions beautifully.

.. warning::
   Important information stands out clearly.

.. tip::
   Helpful tips are easy to spot.

Tables
~~~~~~

.. code-block:: rst

   .. list-table:: Feature Comparison
      :header-rows: 1
      
      * - Feature
      - Supported
      - Notes
      * - Responsive
      - ✓
      - Mobile-first design
      * - Search
      - ✓
      - Full-text search
      * - Themes
      - ✓
      - Light/dark modes

.. list-table:: Feature Comparison
   :header-rows: 1
   
   * - Feature
     - Supported
     - Notes
   * - Responsive
     - ✓
     - Mobile-first design
   * - Search
     - ✓
     - Full-text search
   * - Themes
     - ✓
     - Light/dark modes

Advanced Features
-----------------

Add to ``conf.py``:

Search Integration
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   html_theme_options = {
       'search_placeholder': 'Search documentation...',
       'search_button_text': 'Search',
   }

Version Selector
~~~~~~~~~~~~~~~~

.. code-block:: python

   html_theme_options = {
       'version_selector': True,
       'versions': [
           ('latest', '/latest/'),
           ('v2.0', '/v2.0/'),
           ('v1.0', '/v1.0/'),
       ],
   }

Custom CSS
~~~~~~~~~~

.. code-block:: python

   html_static_path = ['_static']
   html_css_files = ['custom.css']


Practical Examples
------------------

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   import sphinx_wagtail_theme
   
   html_theme = 'sphinx_wagtail_theme'
   html_theme_path = [sphinx_wagtail_theme.get_html_theme_path()]


Content Examples
----------------

Code Blocks
~~~~~~~~~~~

Python code with syntax highlighting:

.. code-block:: python

   def calculate_total(items):
       """Calculate total price of items."""
       return sum(item.price for item in items)

Admonitions
~~~~~~~~~~~

.. code-block:: rst

   .. note::
      Wagtail theme styles admonitions beautifully.

   .. warning::
      Important information stands out clearly.

   .. tip::
      Helpful tips are easy to spot.

.. note::
   Wagtail theme styles admonitions beautifully.

.. warning::
   Important information stands out clearly.

.. tip::
   Helpful tips are easy to spot.

Tables
~~~~~~

.. code-block:: rst

   .. list-table:: Feature Comparison
      :header-rows: 1
      
      * - Feature
      - Supported
      - Notes
      * - Responsive
      - ✓
      - Mobile-first design
      * - Search
      - ✓
      - Full-text search
      * - Themes
      - ✓
      - Light/dark modes

.. list-table:: Feature Comparison
   :header-rows: 1
   
   * - Feature
     - Supported
     - Notes
   * - Responsive
     - ✓
     - Mobile-first design
   * - Search
     - ✓
     - Full-text search
   * - Themes
     - ✓
     - Light/dark modes

Advanced Features
-----------------

Add to ``conf.py``:

Search Integration
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   html_theme_options = {
       'search_placeholder': 'Search documentation...',
       'search_button_text': 'Search',
   }

Version Selector
~~~~~~~~~~~~~~~~

.. code-block:: python

   html_theme_options = {
       'version_selector': True,
       'versions': [
           ('latest', '/latest/'),
           ('v2.0', '/v2.0/'),
           ('v1.0', '/v1.0/'),
       ],
   }

Custom CSS
~~~~~~~~~~

.. code-block:: python

   html_static_path = ['_static']
   html_css_files = ['custom.css']


Practical Examples
------------------

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   import sphinx_wagtail_theme
   
   html_theme = 'sphinx_wagtail_theme'
   html_theme_path = [sphinx_wagtail_theme.get_html_theme_path()]


Content Examples
----------------

Code Blocks
~~~~~~~~~~~

Python code with syntax highlighting:

.. code-block:: python

   def calculate_total(items):
       """Calculate total price of items."""
       return sum(item.price for item in items)

Admonitions
~~~~~~~~~~~

.. code-block:: rst

   .. note::
      Wagtail theme styles admonitions beautifully.

   .. warning::
      Important information stands out clearly.

   .. tip::
      Helpful tips are easy to spot.

.. note::
   Wagtail theme styles admonitions beautifully.

.. warning::
   Important information stands out clearly.

.. tip::
   Helpful tips are easy to spot.

Tables
~~~~~~

.. code-block:: rst

   .. list-table:: Feature Comparison
      :header-rows: 1
      
      * - Feature
      - Supported
      - Notes
      * - Responsive
      - ✓
      - Mobile-first design
      * - Search
      - ✓
      - Full-text search
      * - Themes
      - ✓
      - Light/dark modes

.. list-table:: Feature Comparison
   :header-rows: 1
   
   * - Feature
     - Supported
     - Notes
   * - Responsive
     - ✓
     - Mobile-first design
   * - Search
     - ✓
     - Full-text search
   * - Themes
     - ✓
     - Light/dark modes

Advanced Features
-----------------

Add to ``conf.py``:

Search Integration
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   html_theme_options = {
       'search_placeholder': 'Search documentation...',
       'search_button_text': 'Search',
   }

Version Selector
~~~~~~~~~~~~~~~~

.. code-block:: python

   html_theme_options = {
       'version_selector': True,
       'versions': [
           ('latest', '/latest/'),
           ('v2.0', '/v2.0/'),
           ('v1.0', '/v1.0/'),
       ],
   }

Custom CSS
~~~~~~~~~~

.. code-block:: python

   html_static_path = ['_static']
   html_css_files = ['custom.css']

Additional Resources
--------------------
- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- :doc:`sphinx-rtd-theme` - Read the Docs theme
- :doc:`sphinx-book-theme` - Book theme
- `Wagtail Documentation <https://docs.wagtail.org/>`_
- :doc:`../tutorials/packages/sphinx-wagtail-theme` - Complete tutorial
- Wagtail CMS: https://wagtail.org/
- GitHub repository: https://github.com/wagtail/sphinx_wagtail_theme

