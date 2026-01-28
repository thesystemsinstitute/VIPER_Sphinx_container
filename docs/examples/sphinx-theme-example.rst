Sphinx-Theme Example
====================

This page demonstrates **sphinx-theme** - a framework for creating custom Sphinx themes with modern design and enhanced features.

What is sphinx-theme?
----------------------

sphinx-theme provides tools and utilities for building custom Sphinx themes:

- Theme development framework
- Customizable components
- Modern CSS/JavaScript integration
- Responsive design support
- Theme configuration helpers

Installation & Configuration
-----------------------------

Add to your ``conf.py``:

.. code-block:: python

   import sphinx_theme
   
   extensions = [
       'sphinx_theme',
       # ... other extensions
   ]
   
   # Use custom theme
   html_theme = 'custom_theme'
   html_theme_path = [sphinx_theme.get_theme_path()]
   
   # Theme options
   html_theme_options = {
       'color_scheme': 'light',
       'sidebar_position': 'left',
       'show_breadcrumbs': True
   }

Theme Structure
---------------

Basic Theme Layout
~~~~~~~~~~~~~~~~~~

.. code-block:: text

   my_theme/
   ├── theme.conf           # Theme configuration
   ├── layout.html          # Base layout template
   ├── static/
   │   ├── css/
   │   │   ├── theme.css    # Main stylesheet
   │   │   └── custom.css   # Customizations
   │   └── js/
   │       └── theme.js     # JavaScript
   └── components/
       ├── header.html      # Header component
       ├── sidebar.html     # Sidebar component
       └── footer.html      # Footer component

``theme.conf`` Example
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: ini

   [theme]
   inherit = basic
   stylesheet = theme.css
   pygments_style = friendly
   
   [options]
   # Color scheme: light, dark, auto
   color_scheme = light
   
   # Sidebar position: left, right
   sidebar_position = left
   
   # Navigation depth
   navigation_depth = 4
   
   # Show breadcrumbs
   show_breadcrumbs = true
   
   # Custom logo
   logo = _static/logo.png
   
   # Custom CSS files
   extra_css = custom.css, highlight.css

Layout Templates
----------------

Base Layout
~~~~~~~~~~~

**File**: ``layout.html``

.. code-block:: html+jinja

   <!DOCTYPE html>
   <html lang="{{ language }}" data-theme="{{ theme_color_scheme }}">
   <head>
     <meta charset="utf-8">
     <meta name="viewport" content="width=device-width, initial-scale=1">
     <title>{{ title|striptags|e }}{{ titlesuffix }}</title>
     
     {%- for css in css_files %}
     <link rel="stylesheet" href="{{ pathto(css, 1) }}">
     {%- endfor %}
     
     {%- block extrahead %} {% endblock %}
   </head>
   
   <body>
     {%- include "header.html" %}
     
     <div class="page-wrapper">
       {%- if theme_sidebar_position == 'left' %}
         {%- include "sidebar.html" %}
       {%- endif %}
       
       <main class="content">
         {%- if theme_show_breadcrumbs %}
           {%- include "breadcrumbs.html" %}
         {%- endif %}
         
         {%- block body %} {% endblock %}
       </main>
       
       {%- if theme_sidebar_position == 'right' %}
         {%- include "sidebar.html" %}
       {%- endif %}
     </div>
     
     {%- include "footer.html" %}
     
     {%- for js in script_files %}
     <script src="{{ pathto(js, 1) }}"></script>
     {%- endfor %}
   </body>
   </html>

Header Component
~~~~~~~~~~~~~~~~

**File**: ``components/header.html``

.. code-block:: html+jinja

   <header class="site-header">
     <div class="header-container">
       {%- if logo %}
       <div class="logo">
         <a href="{{ pathto(master_doc) }}">
           <img src="{{ pathto('_static/' + logo, 1) }}" alt="{{ project }}">
         </a>
       </div>
       {%- endif %}
       
       <div class="site-title">
         <a href="{{ pathto(master_doc) }}">{{ project }}</a>
       </div>
       
       <nav class="header-nav">
         {%- for nav_item in theme_nav_links %}
         <a href="{{ nav_item.url }}">{{ nav_item.title }}</a>
         {%- endfor %}
       </nav>
       
       <div class="header-tools">
         <button id="theme-toggle" aria-label="Toggle theme">
           <span class="icon-sun"></span>
           <span class="icon-moon"></span>
         </button>
         <button id="search-toggle" aria-label="Search">
           <span class="icon-search"></span>
         </button>
       </div>
     </div>
   </header>

Sidebar Component
~~~~~~~~~~~~~~~~~

**File**: ``components/sidebar.html``

.. code-block:: html+jinja

   <aside class="sidebar">
     {%- if display_toc %}
     <nav class="sidebar-nav">
       <h3>{{ _('Table of Contents') }}</h3>
       {{ toc }}
     </nav>
     {%- endif %}
     
     {%- if theme_show_related %}
     <div class="sidebar-section">
       <h3>{{ _('Related Pages') }}</h3>
       <ul>
         {%- if prev %}
         <li><a href="{{ prev.link }}">← {{ prev.title }}</a></li>
         {%- endif %}
         {%- if next %}
         <li><a href="{{ next.link }}">{{ next.title }} →</a></li>
         {%- endif %}
       </ul>
     </div>
     {%- endif %}
     
     {%- block sidebarsearch %}
     <div class="sidebar-search">
       <form action="{{ pathto('search') }}" method="get">
         <input type="text" name="q" placeholder="{{ _('Search...') }}">
         <button type="submit">{{ _('Go') }}</button>
       </form>
     </div>
     {%- endblock %}
   </aside>

Styling
-------

CSS Variables
~~~~~~~~~~~~~

.. code-block:: css

   :root {
     /* Colors */
     --color-primary: #2c3e50;
     --color-secondary: #3498db;
     --color-background: #ffffff;
     --color-text: #2c3e50;
     --color-border: #e1e4e8;
     
     /* Typography */
     --font-family: 'Inter', system-ui, sans-serif;
     --font-size-base: 16px;
     --line-height-base: 1.6;
     
     /* Spacing */
     --spacing-xs: 0.25rem;
     --spacing-sm: 0.5rem;
     --spacing-md: 1rem;
     --spacing-lg: 2rem;
     --spacing-xl: 4rem;
     
     /* Layout */
     --sidebar-width: 280px;
     --content-max-width: 1200px;
   }
   
   [data-theme="dark"] {
     --color-background: #1e1e1e;
     --color-text: #e1e4e8;
     --color-border: #30363d;
   }

Responsive Design
~~~~~~~~~~~~~~~~~

.. code-block:: css

   .page-wrapper {
     display: grid;
     grid-template-columns: var(--sidebar-width) 1fr;
     gap: var(--spacing-lg);
     max-width: var(--content-max-width);
     margin: 0 auto;
   }
   
   @media (max-width: 768px) {
     .page-wrapper {
       grid-template-columns: 1fr;
     }
     
     .sidebar {
       display: none;
     }
     
     .sidebar.mobile-open {
       display: block;
       position: fixed;
       top: 0;
       left: 0;
       width: 100%;
       height: 100%;
       z-index: 1000;
     }
   }

JavaScript Features
-------------------

Theme Toggle
~~~~~~~~~~~~

.. code-block:: javascript

   // theme.js
   
   function initTheme() {
     const toggle = document.getElementById('theme-toggle');
     const prefersDark = window.matchMedia('(prefers-color-scheme: dark)');
     
     // Get saved preference or system preference
     const theme = localStorage.getItem('theme') || 
                   (prefersDark.matches ? 'dark' : 'light');
     
     document.documentElement.setAttribute('data-theme', theme);
     
     toggle.addEventListener('click', () => {
       const current = document.documentElement.getAttribute('data-theme');
       const next = current === 'dark' ? 'light' : 'dark';
       
       document.documentElement.setAttribute('data-theme', next);
       localStorage.setItem('theme', next);
     });
   }
   
   // Initialize on load
   document.addEventListener('DOMContentLoaded', initTheme);

Search Enhancement
~~~~~~~~~~~~~~~~~~

.. code-block:: javascript

   function initSearch() {
     const searchToggle = document.getElementById('search-toggle');
     const searchOverlay = document.getElementById('search-overlay');
     
     searchToggle.addEventListener('click', () => {
       searchOverlay.classList.toggle('active');
       document.querySelector('#search-input').focus();
     });
     
     // Close on escape key
     document.addEventListener('keydown', (e) => {
       if (e.key === 'Escape' && searchOverlay.classList.contains('active')) {
         searchOverlay.classList.remove('active');
       }
     });
   }

Configuration Options
---------------------

Theme Options Reference
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   html_theme_options = {
       # Appearance
       'color_scheme': 'light',        # light, dark, auto
       'accent_color': '#3498db',      # Hex color
       
       # Layout
       'sidebar_position': 'left',     # left, right
       'sidebar_width': '280px',
       'content_max_width': '1200px',
       
       # Navigation
       'navigation_depth': 4,
       'show_breadcrumbs': True,
       'show_nav_prev_next': True,
       'collapse_navigation': False,
       
       # Header
       'logo': '_static/logo.png',
       'logo_alt': 'Project Logo',
       'show_project_name': True,
       'nav_links': [
           {'title': 'Home', 'url': '/'},
           {'title': 'Docs', 'url': '/docs'},
           {'title': 'API', 'url': '/api'}
       ],
       
       # Footer
       'footer_text': '© 2026 Project Name',
       'show_footer_version': True,
       'footer_links': [
           {'title': 'GitHub', 'url': 'https://github.com/user/repo'},
           {'title': 'License', 'url': '/license'}
       ],
       
       # Features
       'enable_search': True,
       'enable_theme_toggle': True,
       'enable_code_copy': True,
       'enable_toc_scroll': True,
       
       # Code highlighting
       'pygments_light_style': 'friendly',
       'pygments_dark_style': 'monokai',
       
       # Fonts
       'font_family': '"Inter", system-ui, sans-serif',
       'code_font_family': '"Fira Code", monospace'
   }

Custom CSS
~~~~~~~~~~

.. code-block:: python

   html_css_files = [
       'custom.css',
       'https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700'
   ]

Custom JavaScript
~~~~~~~~~~~~~~~~~

.. code-block:: python

   html_js_files = [
       'custom.js',
       ('analytics.js', {'async': 'async'})
   ]

Example Themes
--------------

Minimal Theme
~~~~~~~~~~~~~

.. code-block:: python

   html_theme_options = {
       'color_scheme': 'light',
       'sidebar_position': 'left',
       'navigation_depth': 2,
       'show_breadcrumbs': False,
       'accent_color': '#2c3e50'
   }

Modern Documentation Theme
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   html_theme_options = {
       'color_scheme': 'auto',
       'sidebar_position': 'left',
       'sidebar_width': '320px',
       'navigation_depth': 4,
       'show_breadcrumbs': True,
       'enable_search': True,
       'enable_theme_toggle': True,
       'accent_color': '#3498db',
       'pygments_light_style': 'friendly',
       'pygments_dark_style': 'monokai'
   }

Learn More
----------

For complete theme development documentation, see:

- :doc:`../tutorials/packages/sphinx-theme` - Full tutorial
- `Sphinx Theming Guide <https://www.sphinx-doc.org/en/master/development/theming.html>`_ - Official guide
- `Jinja2 Documentation <https://jinja.palletsprojects.com/>`_ - Template engine
