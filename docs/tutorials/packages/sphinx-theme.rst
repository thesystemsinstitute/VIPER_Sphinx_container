Sphinx-Theme Tutorial
=====================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-theme/>`_
   - `API Documentation <../../pdoc/sphinx_theme/index.html>`_
   - `Manual <https://github.com/sphinx-contrib/sphinx-theme>`_
   - :doc:`Working Example <../../examples/sphinx-theme-example>`


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

   docker run --rm kensai-sphinx:latest python -c "import sphinx_theme; print('Installed')"

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
     kensai-sphinx:latest \
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
         kensai-sphinx:latest \
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
               kensai-sphinx:latest \
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

   docker run --rm kensai-sphinx:latest pip list | grep sphinx-theme

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
   docker run --rm kensai-sphinx:latest \
     python -c "import sphinx_rtd_theme; help(sphinx_rtd_theme)"

Next Steps
----------

1. Choose a base theme for your documentation
2. Customize colors and branding
3. Add custom CSS/JS if needed
4. Test on different devices and browsers
5. Consider creating a reusable custom theme

Additional Resources
--------------------

- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `Sphinx Theming Guide <https://www.sphinx-doc.org/en/master/development/theming.html>`_
- `sphinx-rtd-theme docs <https://sphinx-rtd-theme.readthedocs.io/>`_
- `Furo documentation <https://pradyunsg.me/furo/>`_
