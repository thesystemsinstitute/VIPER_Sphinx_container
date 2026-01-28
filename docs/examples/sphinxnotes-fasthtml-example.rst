Sphinxnotes-Fasthtml Example
============================

This page demonstrates the **sphinxnotes-fasthtml** extension for quickly generating HTML documentation with minimal configuration.

.. contents:: Contents
   :local:
   :depth: 2

Overview
--------

The sphinxnotes-fasthtml extension provides a streamlined approach to HTML generation with sensible defaults and rapid build times.

Basic Usage
-----------

Simple Page
~~~~~~~~~~~

.. fasthtml::

   # Quick Start
   
   This is a fast HTML page with automatic formatting.
   
   - Bullet points work
   - Lists are automatic
   - **Bold** and *italic* supported

Inline Styles
~~~~~~~~~~~~~

.. fasthtml::
   :style: clean
   
   ## Clean Style
   
   Minimal styling for professional documentation.

Code Blocks
~~~~~~~~~~~

.. fasthtml::
   
   ## Code Example
   
   ```python
   def hello():
       print("Hello, FastHTML!")
   ```

Quick Formatting
----------------

Headers
~~~~~~~

.. fasthtml::

   # H1 Header
   ## H2 Header
   ### H3 Header
   #### H4 Header

Lists
~~~~~

.. fasthtml::

   **Ordered List:**
   1. First item
   2. Second item
   3. Third item
   
   **Unordered List:**
   - Item A
   - Item B
   - Item C

Tables
~~~~~~

.. fasthtml::

   | Column 1 | Column 2 | Column 3 |
   |----------|----------|----------|
   | Data 1   | Data 2   | Data 3   |
   | Value A  | Value B  | Value C  |

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinxnotes.fasthtml',
   ]
   
   # FastHTML settings
   fasthtml_theme = 'clean'
   fasthtml_minify = True

Custom Themes
~~~~~~~~~~~~~

.. code-block:: python

   fasthtml_custom_css = '''
   body {
       font-family: Arial, sans-serif;
       line-height: 1.6;
   }
   '''

Quick Templates
---------------

Blog Post
~~~~~~~~~

.. fasthtml::
   :template: blog
   
   # My Blog Post
   *Published: January 2024*
   
   This is a quick blog post using FastHTML.

API Documentation
~~~~~~~~~~~~~~~~~

.. fasthtml::
   :template: api
   
   ## function_name(param1, param2)
   
   **Parameters:**
   - param1: Description
   - param2: Description
   
   **Returns:** Result description

See Also
--------

- :doc:`../tutorials/packages/sphinxnotes-fasthtml` - Complete tutorial
- GitHub repository: https://github.com/sphinx-notes/fasthtml
