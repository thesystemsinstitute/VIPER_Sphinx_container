Sphinx-Wagtail-Theme Example
============================

This page demonstrates the **sphinx-wagtail-theme** extension, which provides a Wagtail CMS-inspired theme for Sphinx documentation.

.. contents:: Contents
   :local:
   :depth: 2


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

See Also
--------

- :doc:`../tutorials/packages/sphinx-wagtail-theme` - Complete tutorial
- Wagtail CMS: https://wagtail.org/
- GitHub repository: https://github.com/wagtail/sphinx_wagtail_theme
