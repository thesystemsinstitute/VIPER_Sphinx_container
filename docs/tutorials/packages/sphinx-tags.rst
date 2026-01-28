Sphinx Tags Tutorial
====================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-tags/>`_
   - `API Documentation <../../pdoc/sphinx_tags/index.html>`_
   - `Manual <https://sphinx-tags.readthedocs.io/>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinx-tags in your Sphinx documentation.

What is Sphinx Tags?
--------------------
sphinx-tags is a Sphinx extension that provides:

- Tag-based organization
- Easy integration with Sphinx
- Comprehensive configuration options
- Professional documentation output

sphinx-tags provides:

- Tag-based organization
- Integration with Sphinx documentation
- Flexible configuration options
- Professional output formatting

Key Features
~~~~~~~~~~~~

- **Tagging System**: Add tags to documentation pages
- **Tag Pages**: Automatic tag index pages
- **Tag Cloud**: Visual tag cloud representation
- **Cross-referencing**: Link to tagged content


Installation
------------

sphinx-tags is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinx_tags; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``docs/conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_tags',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinx_tags']
   
   # Configuration options
   tags_create_tags = True
   tags_output_dir = '_tags'
   tags_overview_title = 'Tags'


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

Getting Started
~~~~~~~~~~~~~~~

Add tags to documents:

.. code-block:: rst

   .. tags:: python, tutorial, beginner

Tag Pages
~~~~~~~~~

Reference tag pages:

.. code-block:: rst

   See all :tag:`python` articles.

Common Use Cases
----------------

Blog-style Documentation
~~~~~~~~~~~~~~~~~~~~~~~~

Organize blog posts with tags:

.. code-block:: rst

   My Blog Post
   ============
   
   .. tags:: python, web development, flask
   
   Content here...

Tutorial Organization
~~~~~~~~~~~~~~~~~~~~~

Tag tutorials by topic:

.. code-block:: rst

   Advanced Python Tutorial
   ========================
   
   .. tags:: python, advanced, async

Advanced Features
-----------------

Tag Cloud
~~~~~~~~~

Generate tag cloud:

.. code-block:: rst

   .. tagcloud::

Tag Index
~~~~~~~~~

Create tag index page:

.. code-block:: rst

   .. tagindex::

Best Practices
--------------

Tips and Guidelines
~~~~~~~~~~~~~~~~~~~

- Use consistent tag naming
- Don't over-tag content
- Create tag taxonomy
- Link related tagged content
- Maintain tag index

Troubleshooting
---------------

Common Issues
~~~~~~~~~~~~~

**Issue**: Tags not showing

**Solution**: Ensure tags directive is properly formatted and extension is enabled.

**Issue**: Tag pages not generating

**Solution**: Check tags_create_tags is set to True.


Practical Examples
------------------

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

- `PyPI Package <https://pypi.org/project/sphinx-tags/>`_
- `Official Documentation <https://sphinx-tags.readthedocs.io/>`_
- :doc:`Complete Tutorial <../tutorials/packages/sphinx-tags>`
- :ref:`Package API Documentation <pdoc-sphinx-tags>`
Next Steps
----------
- Explore the :doc:`tutorial <../tutorials/packages/sphinx-tags>`
- Check the official documentation
- Try the examples in your own projects
- Customize for your specific needs

