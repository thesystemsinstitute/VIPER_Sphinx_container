Sphinx-Theme Tutorial
=====================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-theme/>`_
   - `API Documentation <../../pdoc/sphinx_theme/index.html>`_
   - `Manual <https://github.com/sphinx-contrib/sphinx-theme>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinx-theme to create and customize Sphinx documentation themes, enabling you to build beautiful, branded documentation sites.

What is Sphinx-Theme?
----------------------
sphinx-theme is a base package and framework for creating custom Sphinx themes. It provides:

- Theme scaffolding and templates
- CSS/JS asset management
- Theme configuration system
- Responsive design utilities
- Color scheme customization
- Layout templates and components
- Theme inheritance mechanism
- Asset bundling and optimization

While Sphinx comes with built-in themes, sphinx-theme helps you create professional custom themes for your documentation.

sphinx-theme provides tools and utilities for building custom Sphinx themes:

- Theme development framework
- Customizable components
- Modern CSS/JavaScript integration
- Responsive design support
- Theme configuration helpers


Installation
------------

sphinx-theme is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm viper-sphinx:latest python -c "import sphinx_theme; print('Installed')"

Available Themes
----------------

Popular themes available in this container:

- **sphinx-rtd-theme** - Read the Docs theme
- **sphinx-book-theme** - Book-style theme
- **pydata-sphinx-theme** - PyData theme
- **furo** - Modern, clean theme
- **sphinx-material** - Material Design theme
- **sphinx-immaterial** - Material Design with extras
- **sphinxawesome-theme** - Awesome theme
- **karma-sphinx-theme** - Karma theme
- **piccolo-theme** - Minimal theme
- **sphinx-press-theme** - Press/blog theme

Configuration
-------------

Basic Theme Selection
~~~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   # Use a built-in theme
   html_theme = 'alabaster'
   
   # Or use an installed theme
   html_theme = 'sphinx_rtd_theme'

Custom Theme Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Theme selection
   html_theme = 'sphinx_rtd_theme'
   
   # Theme options
   html_theme_options = {
       'logo_only': False,
       'display_version': True,
       'prev_next_buttons_location': 'bottom',
       'style_external_links': False,
       'collapse_navigation': True,
       'sticky_navigation': True,
       'navigation_depth': 4,
       'includehidden': True,
       'titles_only': False
   }
   
   # Custom CSS/JS
   html_static_path = ['_static']
   html_css_files = ['custom.css']
   html_js_files = ['custom.js']
   
   # Logo and favicon
   html_logo = '_static/logo.png'
   html_favicon = '_static/favicon.ico'

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import sphinx_theme
   
   # Use sphinx-theme path
   html_theme = 'custom_theme'
   html_theme_path = [sphinx_theme.get_html_theme_path()]
   
   # Theme options
   html_theme_options = {
       # Colors
       'primary_color': '#2196F3',
       'accent_color': '#FF5722',
       'text_color': '#212121',
       'background_color': '#FFFFFF',
       
       # Layout
       'sidebar_width': '280px',
       'body_max_width': '1200px',
       'content_padding': '20px',
       
       # Navigation
       'show_navbar': True,
       'show_sidebar': True,
       'show_toc': True,
       'toc_depth': 3,
       
       # Features
       'search_bar': True,
       'dark_mode': True,
       'code_theme': 'monokai',
       'font_family': 'Roboto, sans-serif',
   }
   
   # Sidebar templates
   html_sidebars = {
       '**': [
           'globaltoc.html',
           'relations.html',
           'sourcelink.html',
           'searchbox.html',
       ]
   }

Theme Customization
-------------------

Custom CSS
~~~~~~~~~~

Create ``docs/_static/custom.css``:

.. code-block:: css

   /* Custom color scheme */
   :root {
       --primary-color: #2196F3;
       --secondary-color: #FF5722;
       --text-color: #333333;
       --background-color: #FFFFFF;
       --code-background: #F5F5F5;
   }
   
   /* Custom navigation bar */
   .navbar {
       background-color: var(--primary-color);
       padding: 1rem;
   }
   
   /* Custom headings */
   h1, h2, h3 {
       color: var(--primary-color);
       font-family: 'Roboto', sans-serif;
   }
   
   /* Custom code blocks */
   pre {
       background-color: var(--code-background);
       border-left: 3px solid var(--primary-color);
       padding: 1rem;
       border-radius: 4px;
   }
   
   /* Custom admonitions */
   .admonition {
       border-left: 4px solid var(--primary-color);
       padding: 1rem;
       margin: 1rem 0;
       background-color: #F0F8FF;
   }
   
   /* Responsive design */
   @media (max-width: 768px) {
       .sidebar {
           display: none;
       }
       .content {
           max-width: 100%;
       }
   }

Custom JavaScript
~~~~~~~~~~~~~~~~~

Create ``docs/_static/custom.js``:

.. code-block:: javascript

   // Add custom behavior
   document.addEventListener('DOMContentLoaded', function() {
       // Add smooth scrolling
       document.querySelectorAll('a[href^="#"]').forEach(anchor => {
           anchor.addEventListener('click', function (e) {
               e.preventDefault();
               const target = document.querySelector(this.getAttribute('href'));
               if (target) {
                   target.scrollIntoView({
                       behavior: 'smooth'
                   });
               }
           });
       });
       
       // Add copy button to code blocks
       document.querySelectorAll('pre').forEach(block => {
           const button = document.createElement('button');
           button.className = 'copy-button';
           button.textContent = 'Copy';
           button.onclick = function() {
               navigator.clipboard.writeText(block.textContent);
               button.textContent = 'Copied!';
               setTimeout(() => button.textContent = 'Copy', 2000);
           };
           block.parentNode.insertBefore(button, block);
       });
       
       // Add dark mode toggle
       const toggle = document.createElement('button');
       toggle.id = 'dark-mode-toggle';
       toggle.textContent = '🌙';
       toggle.onclick = function() {
           document.body.classList.toggle('dark-mode');
           toggle.textContent = document.body.classList.contains('dark-mode') ? '☀️' : '🌙';
       };
       document.body.appendChild(toggle);
   });

Creating Custom Theme
---------------------

Theme Structure
~~~~~~~~~~~~~~~

.. code-block:: text

   my_theme/
   ├── theme.conf
   ├── layout.html
   ├── static/
   │   ├── css/
   │   │   └── theme.css
   │   └── js/
   │       └── theme.js
   └── templates/
       ├── page.html
       ├── searchbox.html
       └── sidebar.html

theme.conf
~~~~~~~~~~

.. code-block:: ini

   [theme]
   inherit = basic
   stylesheet = theme.css
   pygments_style = monokai
   
   [options]
   show_navbar = true
   show_sidebar = true
   sidebar_width = 280px
   primary_color = #2196F3
   accent_color = #FF5722
   font_family = Roboto, sans-serif

layout.html
~~~~~~~~~~~

.. code-block:: html

   {% extends "basic/layout.html" %}
   
   {% block header %}
   <header class="navbar">
       <div class="container">
           <a href="{{ pathto(master_doc) }}" class="logo">
               {% if logo %}
               <img src="{{ pathto('_static/' + logo, 1) }}" alt="Logo">
               {% endif %}
               {{ project }}
           </a>
           <nav class="navigation">
               {% block navigation %}
               {{ toctree(maxdepth=2, collapse=False) }}
               {% endblock %}
           </nav>
       </div>
   </header>
   {% endblock %}
   
   {% block content %}
   <div class="container">
       <div class="row">
           {% if theme_show_sidebar %}
           <aside class="sidebar col-md-3">
               {% block sidebar %}
               {{ toctree(maxdepth=theme_toc_depth|default(3)) }}
               {% endblock %}
           </aside>
           {% endif %}
           
           <main class="content col-md-9">
               {% block body %}{% endblock %}
           </main>
       </div>
   </div>
   {% endblock %}
   
   {% block footer %}
   <footer class="footer">
       <div class="container">
           <p>&copy; {{ copyright }}</p>
       </div>
   </footer>
   {% endblock %}

Using Custom Theme
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   import os
   
   html_theme = 'my_theme'
   html_theme_path = [os.path.abspath('_themes')]

Theme Comparison
----------------

Read the Docs Theme
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   html_theme = 'sphinx_rtd_theme'
   html_theme_options = {
       'collapse_navigation': False,
       'sticky_navigation': True,
       'navigation_depth': 4,
   }

**Best for:** Traditional documentation, API references

Book Theme
~~~~~~~~~~

.. code-block:: python

   html_theme = 'sphinx_book_theme'
   html_theme_options = {
       'repository_url': 'https://github.com/user/repo',
       'use_repository_button': True,
   }

**Best for:** Books, tutorials, courses

Furo Theme
~~~~~~~~~~

.. code-block:: python

   html_theme = 'furo'
   html_theme_options = {
       'light_css_variables': {
           'color-brand-primary': '#2196F3',
           'color-brand-content': '#FF5722',
       },
   }

**Best for:** Modern, clean documentation

Docker Integration
------------------

Build with Custom Theme
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     viper-sphinx:latest \
     sphinx-build -b html /project/docs /project/docs/_build/html

Test Different Themes
~~~~~~~~~~~~~~~~~~~~~~

Create ``test_themes.sh``:

.. code-block:: bash

   #!/bin/bash
   
   THEMES=("sphinx_rtd_theme" "sphinx_book_theme" "furo" "alabaster")
   
   for theme in "${THEMES[@]}"; do
       echo "Building with $theme..."
       
       docker run --rm \
         -v $(pwd):/project \
         -e SPHINX_THEME="$theme" \
         viper-sphinx:latest \
         sh -c "
           sed -i \"s/html_theme = .*/html_theme = '$theme'/\" /project/docs/conf.py
           sphinx-build -b html /project/docs /project/docs/_build/$theme
         "
   done
   
   echo "All themes built!"

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Build Documentation with Custom Theme
   
   on:
     push:
       paths:
         - 'docs/**'
         - '_themes/**'
   
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Build Docs
           run: |
             docker run --rm \
               -v $(pwd):/project \
               viper-sphinx:latest \
               sphinx-build -b html /project/docs /project/docs/_build/html
         
         - name: Deploy
           uses: peaceiris/actions-gh-pages@v3
           with:
             github_token: ${{ secrets.GITHUB_TOKEN }}
             publish_dir: ./docs/_build/html

Best Practices
--------------

1. **Start with Existing Theme**
   
   Extend rather than create from scratch:
   
   .. code-block:: ini
   
      [theme]
      inherit = sphinx_rtd_theme

2. **Keep It Simple**
   
   Don't over-customize - maintain readability

3. **Test Responsiveness**
   
   Ensure theme works on all devices

4. **Use CSS Variables**
   
   Make theming flexible:
   
   .. code-block:: css
   
      :root {
          --primary-color: #2196F3;
      }

5. **Version Your Theme**
   
   Track theme changes in version control

6. **Document Theme Options**
   
   Create a theme configuration guide

7. **Test Accessibility**
   
   Ensure proper contrast, keyboard navigation

Common Customizations
---------------------

Custom Sidebar
~~~~~~~~~~~~~~

.. code-block:: python

   html_sidebars = {
       '**': [
           'about.html',
           'navigation.html',
           'relations.html',
           'searchbox.html',
           'donate.html',
       ]
   }

Custom Footer
~~~~~~~~~~~~~

.. code-block:: html

   {# _templates/footer.html #}
   <footer>
       <p>&copy; 2026 My Company. All rights reserved.</p>
       <p>
           <a href="privacy.html">Privacy</a> |
           <a href="terms.html">Terms</a>
       </p>
   </footer>

Custom Search
~~~~~~~~~~~~~

.. code-block:: python

   html_search_language = 'en'
   html_search_options = {
       'type': 'default',
       'minSuffixLength': 2,
   }

Troubleshooting
---------------

Theme Not Found
~~~~~~~~~~~~~~~

**Solution:**

Check theme is installed:

.. code-block:: bash

   docker run --rm viper-sphinx:latest pip list | grep sphinx-theme

Custom CSS Not Loading
~~~~~~~~~~~~~~~~~~~~~~~

**Solution:**

Verify paths in ``conf.py``:

.. code-block:: python

   html_static_path = ['_static']
   html_css_files = ['custom.css']

Theme Options Not Applied
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Solution:**

Check theme supports the options:

.. code-block:: bash

   # View theme options
   docker run --rm viper-sphinx:latest \
     python -c "import sphinx_rtd_theme; help(sphinx_rtd_theme)"

Next Steps
----------

1. Choose a base theme for your documentation
2. Customize colors and branding
3. Add custom CSS/JS if needed
4. Test on different devices and browsers
5. Consider creating a reusable custom theme


Practical Examples
------------------

This page demonstrates **sphinx-theme** - a framework for creating custom Sphinx themes with modern design and enhanced features.


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

Additional Resources
--------------------

- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `Sphinx Theming Guide <https://www.sphinx-doc.org/en/master/development/theming.html>`_
- `sphinx-rtd-theme docs <https://sphinx-rtd-theme.readthedocs.io/>`_
- `Furo documentation <https://pradyunsg.me/furo/>`_
