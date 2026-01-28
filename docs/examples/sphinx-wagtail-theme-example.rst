Sphinx-Wagtail-Theme Example
============================

This page demonstrates the **sphinx-wagtail-theme** extension, which provides a Wagtail CMS-inspired theme for Sphinx documentation.

.. contents:: Contents
   :local:
   :depth: 2

Overview
--------

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

Configuration
-------------

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

.. note::
   Wagtail theme styles admonitions beautifully.

.. warning::
   Important information stands out clearly.

.. tip::
   Helpful tips are easy to spot.

Tables
~~~~~~

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

See Also
--------

- :doc:`../tutorials/packages/sphinx-wagtail-theme` - Complete tutorial
- Wagtail CMS: https://wagtail.org/
- GitHub repository: https://github.com/wagtail/sphinx_wagtail_theme
