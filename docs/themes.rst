Sphinx Themes Guide
===================

Sphinx themes control the visual appearance of your documentation. This container 
includes several popular themes and access to many more from the community.

Included Themes
---------------

Read the Docs Theme
~~~~~~~~~~~~~~~~~~~

The most popular Sphinx theme, used by Read the Docs.

**Installation:** Already included

**Configuration:**

.. code-block:: python

   html_theme = 'sphinx_rtd_theme'
   
   html_theme_options = {
       'logo_only': False,
       'display_version': True,
       'prev_next_buttons_location': 'bottom',
       'style_external_links': False,
       'collapse_navigation': False,
       'sticky_navigation': True,
       'navigation_depth': 4,
       'includehidden': True,
       'titles_only': False
   }

**Features:**

* Mobile-responsive design
* Integrated search
* Navigation sidebar
* Version selector support
* GitHub/GitLab integration

**Links:**

* `Documentation <https://sphinx-rtd-theme.readthedocs.io/>`_
* `Demo <https://sphinx-rtd-theme.readthedocs.io/>`_

Furo
~~~~

A clean, customizable theme with a modern design.

**Configuration:**

.. code-block:: python

   html_theme = 'furo'
   
   html_theme_options = {
       "light_css_variables": {
           "color-brand-primary": "#336790",
           "color-brand-content": "#336790",
       },
       "dark_css_variables": {
           "color-brand-primary": "#E5B62F",
           "color-brand-content": "#E5B62F",
       },
   }

**Features:**

* Light and dark mode
* Customizable colors
* Clean, modern design
* Mobile-responsive
* Fast and lightweight

**Links:**

* `Documentation <https://pradyunsg.me/furo/>`_
* `Customization Guide <https://pradyunsg.me/furo/customisation/>`_

Book Theme
~~~~~~~~~~

A modern, book-like theme from the Executable Books project.

**Configuration:**

.. code-block:: python

   html_theme = 'sphinx_book_theme'
   
   html_theme_options = {
       "repository_url": "https://github.com/your-org/your-repo",
       "use_repository_button": True,
       "use_issues_button": True,
       "use_edit_page_button": True,
       "path_to_docs": "docs",
       "home_page_in_toc": True,
       "show_navbar_depth": 2,
   }

**Features:**

* Left sidebar with table of contents
* GitHub integration buttons
* Full-width content option
* Built-in dark mode
* Print to PDF support

**Links:**

* `Documentation <https://sphinx-book-theme.readthedocs.io/>`_
* `Gallery <https://sphinx-book-theme.readthedocs.io/en/latest/reference/demo.html>`_

PyData Theme
~~~~~~~~~~~~

Used by NumPy, Pandas, and other PyData projects.

**Configuration:**

.. code-block:: python

   html_theme = 'pydata_sphinx_theme'
   
   html_theme_options = {
       "icon_links": [
           {
               "name": "GitHub",
               "url": "https://github.com/your-org/your-repo",
               "icon": "fab fa-github-square",
           },
       ],
       "navbar_end": ["navbar-icon-links", "search-field.html"],
       "show_prev_next": True,
   }

**Features:**

* Bootstrap-based design
* Icon links in navigation
* Flexible layout
* Search integration
* Responsive design

**Links:**

* `Documentation <https://pydata-sphinx-theme.readthedocs.io/>`_

Material Theme
~~~~~~~~~~~~~~

Material Design-inspired theme for Sphinx.

**Configuration:**

.. code-block:: python

   html_theme = 'sphinx_material'
   
   html_theme_options = {
       'nav_title': 'My Project',
       'color_primary': 'blue',
       'color_accent': 'light-blue',
       'repo_url': 'https://github.com/your-org/your-repo',
       'repo_name': 'Your Project',
       'globaltoc_depth': 2,
       'globaltoc_collapse': False,
       'globaltoc_includehidden': False,
   }

**Features:**

* Material Design
* Multiple color schemes
* Mobile-responsive
* Search highlighting
* Version dropdown

**Links:**

* `Documentation <https://bashtage.github.io/sphinx-material/>`_

Choosing a Theme
----------------

Consider these factors:

1. **Audience**: Technical docs vs. user guides
2. **Brand**: Does it match your brand colors?
3. **Features**: Navigation, search, version support
4. **Mobile**: Mobile responsiveness
5. **Customization**: How much can you customize?
6. **Maintenance**: Is it actively maintained?

Comparison Table
~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 15 15 15 15 20

   * - Theme
     - Difficulty
     - Mobile
     - Dark Mode
     - Customization
     - Best For
   * - RTD Theme
     - Easy
     - Yes
     - No
     - Medium
     - API docs, technical
   * - Furo
     - Easy
     - Yes
     - Yes
     - High
     - Modern projects
   * - Book Theme
     - Medium
     - Yes
     - Yes
     - High
     - Tutorials, books
   * - PyData
     - Medium
     - Yes
     - Yes
     - High
     - Data science
   * - Material
     - Medium
     - Yes
     - Yes
     - High
     - General purpose

Customizing Themes
------------------

Custom CSS
~~~~~~~~~~

1. Create ``_static/custom.css``:

.. code-block:: css

   /* Custom styles */
   .wy-nav-content {
       max-width: 1200px;
   }
   
   h1 {
       color: #336790;
   }

2. Reference in ``conf.py``:

.. code-block:: python

   html_static_path = ['_static']
   html_css_files = ['custom.css']

Custom Templates
~~~~~~~~~~~~~~~~

1. Create ``_templates/layout.html``:

.. code-block:: html

   {% extends "!layout.html" %}
   
   {% block extrahead %}
   <link rel="stylesheet" href="{{ pathto('_static/custom.css', 1) }}">
   {% endblock %}

2. Configure in ``conf.py``:

.. code-block:: python

   templates_path = ['_templates']

Logo and Favicon
~~~~~~~~~~~~~~~~

.. code-block:: python

   html_logo = '_static/logo.png'
   html_favicon = '_static/favicon.ico'

Theme Options
~~~~~~~~~~~~~

Most themes support various options:

.. code-block:: python

   html_theme_options = {
       'navigation_depth': 4,
       'collapse_navigation': False,
       'titles_only': False,
       # Theme-specific options
   }

Exploring More Themes
---------------------

Sphinx Themes Gallery
~~~~~~~~~~~~~~~~~~~~~

Visit `sphinx-themes.org <https://sphinx-themes.org/>`_ to browse hundreds of themes 
with live previews.

Popular themes include:

* **sphinx-immaterial**: Material Design theme
* **piccolo-theme**: Lightweight, modern theme
* **sphinx-press-theme**: Magazine-style theme
* **karma-sphinx-theme**: Clean, minimalist theme
* **sphinxawesome-theme**: Feature-rich theme

Installing Additional Themes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Themes can be added to the container by modifying ``requirements.txt``:

.. code-block:: text

   sphinx-immaterial
   piccolo-theme
   karma-sphinx-theme

Then rebuild the container:

.. code-block:: bash

   docker build -t kensai-sphinx .

Example Configurations
----------------------

Minimal Configuration
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   html_theme = 'furo'

Professional Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   html_theme = 'sphinx_rtd_theme'
   html_logo = '_static/logo.png'
   html_favicon = '_static/favicon.ico'
   
   html_theme_options = {
       'logo_only': True,
       'display_version': True,
       'style_external_links': True,
   }
   
   html_css_files = ['custom.css']

Open Source Project
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   html_theme = 'sphinx_book_theme'
   
   html_theme_options = {
       "repository_url": "https://github.com/myorg/myproject",
       "use_repository_button": True,
       "use_issues_button": True,
       "use_download_button": True,
       "use_fullscreen_button": True,
   }

Testing Themes
--------------

Switch themes easily to test:

.. code-block:: bash

   # Edit conf.py to change html_theme
   # Rebuild
   docker run -v $(pwd):/project kensai-sphinx \
       sphinx-build -b html /project/docs /project/docs/_build/html

Resources
---------

* `Sphinx Themes Gallery <https://sphinx-themes.org/>`_
* `Theme Development Guide <https://www.sphinx-doc.org/en/master/development/theming.html>`_
* `HTML Theme Configuration <https://www.sphinx-doc.org/en/master/usage/theming.html>`_

Video Tutorial
--------------

.. raw:: html

   <iframe width="560" height="315" 
   src="https://www.youtube.com/embed/gWrc4xzm45Y" 
   title="Sphinx Themes Tutorial" 
   frameborder="0" 
   allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
   allowfullscreen></iframe>
