Sphinx-Hoverxref Example
========================

This page demonstrates the **sphinx-hoverxref** extension for showing tooltips and modal windows when hovering over cross-references.

.. contents:: Contents
   :local:
   :depth: 2

Overview
--------

The sphinx-hoverxref extension adds interactive tooltips that display the content of cross-referenced sections, allowing readers to preview content without navigating away from the current page.

Basic Configuration
-------------------

Setup
~~~~~

.. code-block:: python

   # conf.py
   extensions = [
       'hoverxref.extension',
   ]
   
   # Basic hoverxref configuration
   hoverxref_auto_ref = True

Intersphinx Support
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = [
       'sphinx.ext.intersphinx',
       'hoverxref.extension',
   ]
   
   # Enable for intersphinx
   hoverxref_intersphinx = [
       'python',
       'sphinx',
       'readthedocs',
   ]

Reference Types
---------------

Auto References
~~~~~~~~~~~~~~~

Automatically enable for all reference types:

.. code-block:: python

   hoverxref_auto_ref = True

The extension works with standard Sphinx cross-references:

.. code-block:: rst

   See :ref:`installation` for setup instructions.
   
   Check the :doc:`api-reference` for details.
   
   Use :py:func:`myfunction` for processing.

Selective References
~~~~~~~~~~~~~~~~~~~~

Enable for specific roles only:

.. code-block:: python

   hoverxref_auto_ref = False
   
   hoverxref_roles = [
       'ref',
       'doc',
       'class',
       'func',
   ]

Custom Role
~~~~~~~~~~~

.. code-block:: python

   hoverxref_role_types = {
       'ref': 'tooltip',
       'doc': 'modal',
       'class': 'tooltip',
       'func': 'tooltip',
   }

Tooltip vs Modal
----------------

Tooltip Display
~~~~~~~~~~~~~~~

.. code-block:: python

   # Default: show as tooltip
   hoverxref_role_types = {
       'ref': 'tooltip',
       'confval': 'tooltip',
   }

Usage in reStructuredText:

.. code-block:: rst

   Hover over :ref:`this reference <target-label>` to see a tooltip.

Modal Display
~~~~~~~~~~~~~

.. code-block:: python

   # Show in modal window
   hoverxref_role_types = {
       'doc': 'modal',
       'class': 'modal',
   }

Usage:

.. code-block:: rst

   Click :doc:`this document <page>` to see it in a modal.

Mixed Types
~~~~~~~~~~~

.. code-block:: python

   hoverxref_role_types = {
       # Quick previews
       'ref': 'tooltip',
       'term': 'tooltip',
       
       # Detailed content
       'doc': 'modal',
       'class': 'modal',
       'mod': 'modal',
   }

Appearance Configuration
------------------------

Tooltip Settings
~~~~~~~~~~~~~~~~

.. code-block:: python

   hoverxref_tooltip_theme = [
       ('light', {
           'theme': 'light',
           'animation': 'fade',
           'animateFill': False,
       }),
   ]

Tooltip Styling
~~~~~~~~~~~~~~~

.. code-block:: python

   hoverxref_tooltip_maxwidth = 600  # pixels
   
   hoverxref_tooltip_content = 'function(reference) { return reference.getAttribute("data-title"); }'

Modal Settings
~~~~~~~~~~~~~~

.. code-block:: python

   hoverxref_modal_hover_delay = 500  # milliseconds
   
   hoverxref_modal_class = 'custom-modal'

Custom CSS
----------

Tooltip Styling
~~~~~~~~~~~~~~~

.. code-block:: css

   /* custom.css */
   .hoverxref-tooltip {
       background-color: #f8f9fa;
       border: 1px solid #dee2e6;
       border-radius: 4px;
       box-shadow: 0 2px 8px rgba(0,0,0,0.15);
       padding: 10px;
       max-width: 400px;
   }
   
   .hoverxref-tooltip code {
       background-color: #e9ecef;
       padding: 2px 4px;
       border-radius: 3px;
   }

Modal Styling
~~~~~~~~~~~~~

.. code-block:: css

   .hoverxref-modal-content {
       background: white;
       border-radius: 8px;
       padding: 20px;
       max-width: 800px;
       margin: 50px auto;
   }
   
   .hoverxref-modal-overlay {
       background-color: rgba(0, 0, 0, 0.5);
   }

Theme Integration
~~~~~~~~~~~~~~~~~

.. code-block:: css

   /* Match RTD theme */
   .hoverxref-tooltip {
       background-color: #fcfcfc;
       color: #404040;
       font-family: "Lato", "proxima-nova", "Helvetica Neue", Arial, sans-serif;
   }

Domain-Specific Configuration
------------------------------

Python Domain
~~~~~~~~~~~~~

.. code-block:: python

   hoverxref_domains = ['py']
   
   hoverxref_role_types = {
       'py:class': 'tooltip',
       'py:func': 'tooltip',
       'py:meth': 'tooltip',
       'py:attr': 'tooltip',
       'py:mod': 'modal',
   }

C/C++ Domain
~~~~~~~~~~~~

.. code-block:: python

   hoverxref_domains = ['c', 'cpp']
   
   hoverxref_role_types = {
       'c:func': 'tooltip',
       'cpp:class': 'modal',
   }

JavaScript Domain
~~~~~~~~~~~~~~~~~

.. code-block:: python

   hoverxref_domains = ['js']
   
   hoverxref_role_types = {
       'js:func': 'tooltip',
       'js:class': 'tooltip',
   }

Practical Examples
------------------

API Documentation
~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   extensions = [
       'sphinx.ext.autodoc',
       'hoverxref.extension',
   ]
   
   hoverxref_auto_ref = True
   hoverxref_domains = ['py']
   
   hoverxref_role_types = {
       'ref': 'tooltip',
       'py:class': 'tooltip',
       'py:func': 'tooltip',
       'py:meth': 'tooltip',
   }

Usage in docs:

.. code-block:: rst

   The :py:class:`MyClass` provides functionality for processing.
   
   Use :py:func:`process_data` to transform input.
   
   See :ref:`advanced-usage` for more details.

Tutorial Documentation
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   hoverxref_role_types = {
       'ref': 'tooltip',     # Quick previews
       'term': 'tooltip',    # Glossary terms
       'doc': 'modal',       # Full documents
   }

Usage:

.. code-block:: rst

   First, review the :term:`API key` concept.
   
   Then check :ref:`configuration` settings.
   
   For complete details, see :doc:`full-guide`.

Advanced Features
-----------------

Intersphinx Integration
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   intersphinx_mapping = {
       'python': ('https://docs.python.org/3', None),
       'sphinx': ('https://www.sphinx-doc.org/', None),
   }
   
   hoverxref_intersphinx = ['python', 'sphinx']
   
   hoverxref_intersphinx_types = {
       'python': {
           'py:class': 'tooltip',
           'py:func': 'tooltip',
       },
       'sphinx': {
           'ref': 'modal',
       },
   }

Usage:

.. code-block:: rst

   Use Python's :py:func:`python:open` function.
   
   See Sphinx's :ref:`sphinx:invocation`.

Custom Content
~~~~~~~~~~~~~~

.. code-block:: python

   def get_hoverxref_content(app, domain, reftype, target):
       """Custom content for tooltips."""
       if reftype == 'term':
           return f"Definition of {target}"
       return None
   
   def setup(app):
       app.connect('hoverxref-tooltip-content', get_hoverxref_content)

Lazy Loading
~~~~~~~~~~~~

.. code-block:: python

   # Load content on demand
   hoverxref_lazy_load = True
   
   # API endpoint for content
   hoverxref_api_host = 'https://docs.example.com'

Performance Optimization
------------------------

Caching
~~~~~~~

.. code-block:: python

   # Cache tooltip content
   hoverxref_cache_timeout = 3600  # seconds

Selective Loading
~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Only load for certain pages
   def should_load_hoverxref(pagename):
       return pagename.startswith('api/')
   
   hoverxref_exclude = lambda pagename: not should_load_hoverxref(pagename)

Minification
~~~~~~~~~~~~

.. code-block:: python

   # Minify JavaScript
   html_js_files = [
       ('hoverxref.min.js', {'defer': 'defer'}),
   ]

Accessibility
-------------

Keyboard Navigation
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Enable keyboard shortcuts
   hoverxref_keyboard_navigation = True

ARIA Labels
~~~~~~~~~~~

.. code-block:: python

   hoverxref_tooltip_aria_label = 'Tooltip: {title}'

Screen Readers
~~~~~~~~~~~~~~

.. code-block:: html

   <span class="hoverxref"
         role="tooltip"
         aria-label="Preview available">
       Reference text
   </span>

Mobile Support
--------------

Touch Behavior
~~~~~~~~~~~~~~

.. code-block:: python

   # Configure for touch devices
   hoverxref_tooltip_interactive = True
   
   hoverxref_touch_delay = 200  # ms

Responsive Design
~~~~~~~~~~~~~~~~~

.. code-block:: css

   @media (max-width: 768px) {
       .hoverxref-tooltip {
           max-width: 90vw;
           font-size: 14px;
       }
       
       .hoverxref-modal-content {
           margin: 20px;
           padding: 15px;
       }
   }

Testing
-------

Visual Testing
~~~~~~~~~~~~~~

.. code-block:: python

   # Test configuration
   hoverxref_auto_ref = True
   hoverxref_role_types = {
       'ref': 'tooltip',
       'doc': 'modal',
   }

Check in browser:

1. Hover over references
2. Verify tooltip appears
3. Check modal opens on click
4. Test keyboard navigation

Integration Testing
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # test_hoverxref.py
   from selenium import webdriver
   
   def test_tooltip_appears():
       driver = webdriver.Firefox()
       driver.get('http://localhost:8000/docs/')
       
       # Hover over reference
       elem = driver.find_element_by_css_selector('.reference.internal')
       ActionChains(driver).move_to_element(elem).perform()
       
       # Check tooltip
       tooltip = driver.find_element_by_css_selector('.hoverxref-tooltip')
       assert tooltip.is_displayed()

Best Practices
--------------

When to Use
~~~~~~~~~~~

**Good for:**

- API references
- Glossary terms
- Short definitions
- Quick previews

**Not ideal for:**

- Long documents
- Complex layouts
- Critical content
- Mobile-first sites

Configuration Tips
~~~~~~~~~~~~~~~~~~

1. Start with tooltips for most references
2. Use modals for detailed content
3. Test on different devices
4. Consider page load time
5. Match theme styling

Content Guidelines
~~~~~~~~~~~~~~~~~~

1. Keep tooltip content concise
2. Ensure meaningful summaries
3. Test with screen readers
4. Provide fallback navigation
5. Don't hide important information

See Also
--------

- :doc:`../tutorials/packages/sphinx-hoverxref` - Complete tutorial
- GitHub repository: https://github.com/readthedocs/sphinx-hoverxref
