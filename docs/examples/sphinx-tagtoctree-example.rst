Sphinx-TagTocTree Example
=========================

This page demonstrates the **sphinx-tagtoctree** extension which allows organizing documentation using tags instead of traditional hierarchical structure.


Configuration
-------------

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_tagtoctree',
       # ... other extensions
   ]
   
   # Tag configuration
   tagtoctree_tag_index_name = 'tags'
   tagtoctree_generate_tag_pages = True

Basic Usage
-----------

Tagging Documents
~~~~~~~~~~~~~~~~~

Add tags to document metadata:

.. code-block:: rst

   Authentication Guide
   ====================
   
   :tags: security, api, beginner
   
   This guide covers authentication mechanisms...

.. code-block:: rst

   Database Optimization
   =====================
   
   :tags: performance, database, advanced
   
   Learn how to optimize database queries...

Creating Tagged ToC Trees
~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the ``tagtoctree`` directive:

.. code-block:: rst

   Security Documentation
   ======================
   
   All security-related guides:
   
   .. tagtoctree::
      :tag: security
      :maxdepth: 2
   
   This will include all documents tagged with "security"

Advanced Examples
-----------------

Multiple Tag Filters
~~~~~~~~~~~~~~~~~~~~

Filter by multiple tags:

.. code-block:: rst

   Beginner API Guides
   ===================
   
   .. tagtoctree::
      :tags: api, beginner
      :operator: and
      :maxdepth: 1
   
   Shows only documents with BOTH "api" AND "beginner" tags

OR Operator
~~~~~~~~~~~

.. code-block:: rst

   Quick Reference
   ===============
   
   .. tagtoctree::
      :tags: cheatsheet, reference
      :operator: or
   
   Shows documents with EITHER "cheatsheet" OR "reference"

Exclude Tags
~~~~~~~~~~~~

.. code-block:: rst

   Non-Advanced Documentation
   ==========================
   
   .. tagtoctree::
      :tag: tutorial
      :exclude-tags: advanced, expert
      :maxdepth: 2
   
   Shows tutorials excluding advanced content

Real-World Example
------------------

Project Structure
~~~~~~~~~~~~~~~~~

**File**: ``docs/guides/authentication.rst``

.. code-block:: rst

   User Authentication
   ===================
   
   :tags: security, api, oauth, beginner
   
   Learn how to implement OAuth 2.0 authentication...

**File**: ``docs/guides/rate-limiting.rst``

.. code-block:: rst

   Rate Limiting
   =============
   
   :tags: security, api, performance, intermediate
   
   Implement rate limiting to protect your API...

**File**: ``docs/guides/caching.rst``

.. code-block:: rst

   Caching Strategies
   ==================
   
   :tags: performance, optimization, advanced
   
   Advanced caching techniques for high-traffic applications...

**File**: ``docs/tutorials/quickstart.rst``

.. code-block:: rst

   Quick Start Guide
   =================
   
   :tags: tutorial, beginner, getting-started
   
   Get up and running in 5 minutes...

Organized Documentation
~~~~~~~~~~~~~~~~~~~~~~~

**File**: ``docs/by-topic.rst``

.. code-block:: rst

   Documentation by Topic
   ======================
   
   Security
   --------
   
   .. tagtoctree::
      :tag: security
      :maxdepth: 1
   
   Performance
   -----------
   
   .. tagtoctree::
      :tag: performance
      :maxdepth: 1
   
   API Documentation
   -----------------
   
   .. tagtoctree::
      :tag: api
      :maxdepth: 1

**File**: ``docs/by-difficulty.rst``

.. code-block:: rst

   Documentation by Difficulty
   ===========================
   
   Beginner
   --------
   
   .. tagtoctree::
      :tag: beginner
      :maxdepth: 2
   
   Intermediate
   ------------
   
   .. tagtoctree::
      :tag: intermediate
      :maxdepth: 2
   
   Advanced
   --------
   
   .. tagtoctree::
      :tag: advanced
      :maxdepth: 2

Tag Index Page
~~~~~~~~~~~~~~

**File**: ``docs/tags.rst``

.. code-block:: rst

   All Tags
   ========
   
   .. tagindex::
      :columns: 3
   
   This automatically generates a tag cloud with:
   - security (4 documents)
   - api (2 documents)
   - performance (2 documents)
   - beginner (2 documents)
   - etc.

Dynamic Navigation
------------------

Context-Aware Navigation
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Related Security Topics
   =======================
   
   This page is tagged with: :tags: security, encryption
   
   Other Security Resources
   ------------------------
   
   .. tagtoctree::
      :tag: security
      :exclude-current: true
      :maxdepth: 1
   
   Excludes the current page from the list

Combined Organization
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Complete Python Guide
   =====================
   
   Tutorials
   ---------
   
   .. tagtoctree::
      :tags: python, tutorial
      :operator: and
   
   API Reference
   -------------
   
   .. tagtoctree::
      :tags: python, api-reference
      :operator: and
   
   Advanced Topics
   ---------------
   
   .. tagtoctree::
      :tags: python, advanced
      :operator: and

Configuration Options
---------------------

Directive Options
~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Option
     - Type
     - Description
   * - :tag:
     - string
     - Single tag to filter by
   * - :tags:
     - list
     - Multiple tags (comma-separated)
   * - :operator:
     - and/or
     - How to combine multiple tags
   * - :exclude-tags:
     - list
     - Tags to exclude
   * - :maxdepth:
     - int
     - Maximum depth of toctree
   * - :exclude-current:
     - flag
     - Exclude current document
   * - :numbered:
     - flag
     - Number entries
   * - :titlesonly:
     - flag
     - Show only titles

Global Configuration
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   
   # Automatically generate tag index
   tagtoctree_generate_tag_pages = True
   
   # Tag index file name
   tagtoctree_tag_index_name = 'tags'
   
   # Tag cloud minimum size
   tagtoctree_min_tag_size = 10
   
   # Tag cloud maximum size
   tagtoctree_max_tag_size = 30
   
   # Show document count
   tagtoctree_show_tag_count = True

Use Cases
---------

1. **Large Documentation Sets**
   
   - Multiple categorization schemes
   - Cross-cutting concerns
   - Flexible navigation

2. **Multi-Audience Documentation**
   
   - Role-based views (developer, admin, user)
   - Skill-level filtering
   - Topic-based organization

3. **Evolving Documentation**
   
   - Easy reorganization
   - No folder restructuring needed
   - Maintain multiple views

Benefits
--------

- **Flexibility**: One document, many categories
- **No Duplication**: Single source, multiple views
- **Maintainability**: Change tags, not folder structure
- **Discovery**: Related content automatically linked
- **Evolution**: Easy to reorganize over time

Learn More
----------

For complete documentation and advanced features, see:

- :doc:`../tutorials/packages/sphinx-tagtoctree` - Full tutorial
- `sphinx-tagtoctree Documentation <https://sphinx-tagtoctree.readthedocs.io/>`_ - Official docs
- `Sphinx ToC Tree <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-toctree>`_ - Standard toctree
