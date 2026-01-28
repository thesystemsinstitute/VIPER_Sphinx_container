Sphinx Tags Tutorial
====================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-tags/>`_
   - `API Documentation <../../pdoc/sphinx_tags/index.html>`_
   - `Manual <https://sphinx-tags.readthedocs.io/>`_
   - :doc:`Working Example <../../examples/sphinx-tags-example>`


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

Additional Resources
--------------------

- :doc:`Working Example <../../examples/sphinx-tags-example>`
- `PyPI Package <https://pypi.org/project/sphinx-tags/>`_
- `Official Documentation <https://sphinx-tags.readthedocs.io/>`_
