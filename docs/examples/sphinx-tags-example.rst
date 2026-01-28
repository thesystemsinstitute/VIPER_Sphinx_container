Sphinx Tags Example
===================

.. note::

   **Package**: sphinx-tags  
   **Purpose**: Tag-based organization  
   **Tutorial**: See :doc:`../tutorials/packages/sphinx-tags` for complete tutorial

This page demonstrates **sphinx-tags** - Tag-based organization.

.. contents:: Contents
   :local:
   :depth: 3

Overview
--------


Key Features
~~~~~~~~~~~~

- **Tagging System**: Add tags to documentation pages
- **Tag Pages**: Automatic tag index pages
- **Tag Cloud**: Visual tag cloud representation
- **Cross-referencing**: Link to tagged content

Installation
------------

Using pip
~~~~~~~~~

Install the extension:

.. code-block:: bash

   pip install sphinx-tags

Or add to your ``requirements.txt``:

.. code-block:: text

   sphinx-tags
   sphinx>=5.0.0

Configuration
-------------

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_tags',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

Complete configuration with all features:

.. code-block:: python

   extensions = ['sphinx_tags']
   
   # Package-specific configuration
   tags_create_tags = True
   tags_output_dir = '_tags'
   tags_overview_title = 'Tags'
   tags_extension = ['rst']
   tags_page_title = 'Tag: '
   tags_create_badges = True

Basic Usage
-----------

Example 1: Tag Documents
~~~~~~~~~~~~~~~~~~~~~~~~

Add tags to documentation pages:

.. code-block:: rst

   Python Tutorial
   ===============
   
   .. tags:: python, tutorial, beginner
   
   This tutorial introduces Python programming...

Example 2: Reference Tags
~~~~~~~~~~~~~~~~~~~~~~~~~

Link to tag pages:

.. code-block:: rst

   See all :tag:`python` tutorials.
   
   Browse :tag:`advanced` topics.

Real-World Examples
-------------------

Example: Blog-style Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Organize blog posts with tags:

.. code-block:: rst

   Getting Started with Docker
   ===========================
   
   .. tags:: docker, containers, tutorial, beginner
   
   :Author: John Doe
   :Date: 2026-01-27
   
   Introduction
   ------------
   
   This post covers Docker basics...
   
   Related Topics
   --------------
   
   - See all :tag:`docker` posts
   - Browse :tag:`containers` content
   - Check out :tag:`tutorial` series

Example: Tutorial Series
~~~~~~~~~~~~~~~~~~~~~~~~

Organize tutorials by difficulty and topic:

.. code-block:: rst

   Advanced Async Programming
   ==========================
   
   .. tags:: python, async, advanced, concurrency
   
   Prerequisites
   -------------
   
   Before starting, review:
   
   - :tag:`python` basics
   - :tag:`beginner` tutorials
   
   Content
   -------
   
   This advanced tutorial covers...

Example: Tag Index Page
~~~~~~~~~~~~~~~~~~~~~~~

Create a comprehensive tag index:

.. code-block:: rst

   Documentation Tags
   ==================
   
   Browse documentation by tags:
   
   Tag Cloud
   ---------
   
   .. tagcloud::
      :minsize: 80%
      :maxsize: 200%
   
   All Tags
   --------
   
   .. tagindex::
   
   Popular Tags
   ------------
   
   - :tag:`python` - Python programming
   - :tag:`tutorial` - Step-by-step guides
   - :tag:`advanced` - Advanced topics
   - :tag:`api` - API documentation

Example: Multi-level Tagging
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use hierarchical tags:

.. code-block:: rst

   Flask Web Application Tutorial
   ===============================
   
   .. tags:: python, web, flask, tutorial, beginner, web-frameworks
   
   This tutorial covers building web applications with Flask.
   
   Navigation
   ----------
   
   By Category:
   
   - :tag:`python` - All Python content
   - :tag:`web` - Web development
   - :tag:`web-frameworks` - Web frameworks specifically
   
   By Level:
   
   - :tag:`beginner` - Beginner content
   - :tag:`tutorial` - Tutorial format

Example: Configuration with Custom Template
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Customize tag pages:

.. code-block:: python

   # In conf.py
   extensions = ['sphinx_tags']
   
   tags_create_tags = True
   tags_output_dir = '_tags'
   tags_extension = ['rst']
   tags_create_badges = True
   tags_badge_colors = {
       'python': '#3776ab',
       'javascript': '#f7df1e',
       'tutorial': '#28a745',
       'advanced': '#dc3545',
   }
   
   # Custom template
   tags_page_title = 'Tagged: {tag}'
   tags_overview_title = 'Browse by Tag'

Example: Tag Statistics
~~~~~~~~~~~~~~~~~~~~~~~

Create tag statistics page:

.. code-block:: rst

   Tag Statistics
   ==============
   
   Most Popular Tags
   -----------------
   
   .. taglist::
      :sort: count
      :limit: 10
   
   All Tags (Alphabetical)
   -----------------------
   
   .. taglist::
      :sort: name

Best Practices
--------------

Recommendations
~~~~~~~~~~~~~~~

- Use consistent tag naming conventions
- Create a tag taxonomy/hierarchy
- Don't over-tag (5-10 tags per page max)
- Link related content through tags
- Maintain a tag index page

Common Patterns
~~~~~~~~~~~~~~~

Standard patterns for using sphinx-tags:

1. **Topic Tags**: Main subject areas (python, javascript)
2. **Type Tags**: Content type (tutorial, reference, guide)
3. **Level Tags**: Difficulty level (beginner, advanced)

Integration Tips
----------------

Working with Other Extensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

sphinx-tags integrates well with:

- Blog extensions for post organization
- Search extensions for tag-based search
- Navigation extensions for tag browsing

Additional Resources
--------------------

- :doc:`Complete Tutorial <../tutorials/packages/sphinx-tags>`
- `PyPI Package <https://pypi.org/project/sphinx-tags/>`_
- `Official Documentation <https://sphinx-tags.readthedocs.io/>`_
- :ref:`Package API Documentation <pdoc-sphinx-tags>`

Next Steps
----------

- Explore the :doc:`tutorial <../tutorials/packages/sphinx-tags>`
- Check the official documentation
- Try the examples in your own projects
- Customize for your specific needs
