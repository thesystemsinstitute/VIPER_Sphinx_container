Sphinx-Tagtoctree Tutorial
===========================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-tagtoctree/>`_
   - `API Documentation <../../pdoc/sphinx_tagtoctree/index.html>`_
   - `Manual <https://github.com/sphinx-contrib/tagtoctree>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinx-tagtoctree to organize documentation with tags, creating dynamic table of contents based on document metadata.

What is Sphinx-Tagtoctree?
---------------------------
sphinx-tagtoctree is a Sphinx extension that enables tag-based document organization. It allows you to:

- Tag documents with custom metadata
- Generate dynamic table of contents based on tags
- Filter and organize content by categories
- Create multiple views of the same content
- Build tag-based navigation systems
- Auto-generate tag indexes and listings

This is especially useful for large documentation projects where content can be organized in multiple ways (by topic, difficulty, version, etc.).

sphinx-tagtoctree enables tag-based organization of documentation, allowing:

- Documents to appear in multiple categories
- Flexible organization without folder structure constraints
- Dynamic table of contents based on tags
- Cross-cutting documentation themes


Installation
------------

sphinx-tagtoctree is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinx_tagtoctree; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_tagtoctree',
   ]
   
   # Enable tag-based navigation
   tagtoctree_enabled = True

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinx_tagtoctree']
   
   # Tag configuration
   tagtoctree_enabled = True
   tagtoctree_default_tag = 'general'
   tagtoctree_tag_field = 'tags'
   tagtoctree_show_untagged = True
   
   # Tag display options
   tagtoctree_tag_prefix = '🏷️ '
   tagtoctree_show_tag_count = True
   tagtoctree_sort_tags = True
   
   # Available tags (optional)
   tagtoctree_tags = {
       'beginner': {
           'title': 'Beginner Tutorials',
           'icon': '🌱',
       },
       'advanced': {
           'title': 'Advanced Topics',
           'icon': '🚀',
       },
       'api': {
           'title': 'API Reference',
           'icon': '📚',
       },
   }


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

   .. tags:: tutorial, beginner, python
   
   Getting Started with Python
   ===========================
   
   This is a beginner-friendly Python tutorial.

Alternative syntax:

.. code-block:: rst

   :tags: advanced, performance, optimization
   
   Performance Optimization Guide
   ==============================

Creating Tag-Based TOC
~~~~~~~~~~~~~~~~~~~~~~

Use the ``tagtoctree`` directive:

.. code-block:: rst

   .. tagtoctree::
      :tags: tutorial
      
      Tutorials matching the 'tutorial' tag will appear here.

Multiple Tags
~~~~~~~~~~~~~

.. code-block:: rst

   .. tagtoctree::
      :tags: python, beginner
      :operator: and
      
      Documents with BOTH 'python' AND 'beginner' tags.

.. code-block:: rst

   .. tagtoctree::
      :tags: python, javascript
      :operator: or
      
      Documents with 'python' OR 'javascript' tags.

   Documentation
   =============
   
   Choose your learning path:
   
   Beginner Path
   -------------
   
   .. tagtoctree::
      :tags: beginner
      :maxdepth: 1
      
   Intermediate Path
   -----------------
   
   .. tagtoctree::
      :tags: intermediate
      :maxdepth: 1
      
   Advanced Path
   -------------
   
   .. tagtoctree::
      :tags: advanced
      :maxdepth: 1

Tag individual documents:

``docs/intro.rst``:

.. code-block:: rst

   .. tags:: beginner, tutorial
   
   Introduction
   ============

``docs/async-programming.rst``:

.. code-block:: rst

   .. tags:: advanced, python
   
   Async Programming
   =================

Example 2: Topic-Based Organization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Topics
   ======
   
   Python Development
   ------------------
   
   .. tagtoctree::
      :tags: python
      :maxdepth: 2
   
   JavaScript Development
   ----------------------
   
   .. tagtoctree::
      :tags: javascript
      :maxdepth: 2
   
   Database Topics
   ---------------
   
   .. tagtoctree::
      :tags: database
      :maxdepth: 2
   
   DevOps & Deployment
   -------------------
   
   .. tagtoctree::
      :tags: devops, deployment
      :operator: or
      :maxdepth: 2

Example 3: Tag Index Page
~~~~~~~~~~~~~~~~~~~~~~~~~~

Create ``docs/tags.rst``:

.. code-block:: rst

   Browse by Tag
   =============
   
   All available tags in this documentation.
   
   .. tagindex::
      :sort: alphabetical
      :show-count: true
   
   Documents by Tag
   ----------------
   
   Tutorials
   ~~~~~~~~~
   
   .. tagtoctree::
      :tags: tutorial
      :maxdepth: 1
   
   API Documentation
   ~~~~~~~~~~~~~~~~~
   
   .. tagtoctree::
      :tags: api
      :maxdepth: 1
   
   Examples
   ~~~~~~~~
   
   .. tagtoctree::
      :tags: example
      :maxdepth: 1

Example 4: Version-Specific Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Version 2.0 Documentation
   =========================
   
   New in Version 2.0
   ------------------
   
   .. tagtoctree::
      :tags: v2.0, new
      :operator: and
   
   Updated in Version 2.0
   ----------------------
   
   .. tagtoctree::
      :tags: v2.0, updated
      :operator: and
   
   Legacy (v1.x) Documentation
   ---------------------------
   
   .. tagtoctree::
      :tags: v1.x
      :exclude-tags: deprecated

Tag documents:

.. code-block:: rst

   .. tags:: v2.0, new, async
   
   Async Processing
   ================

Example 5: Complex Multi-Tag Organization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Learning Resources
   ==================
   
   Beginner Python Tutorials
   --------------------------
   
   .. tagtoctree::
      :tags: python, beginner, tutorial
      :operator: and
      :maxdepth: 1
   
   Advanced Python Examples
   ------------------------
   
   .. tagtoctree::
      :tags: python, advanced, example
      :operator: and
      :maxdepth: 1
   
   Web Development
   ---------------
   
   .. tagtoctree::
      :tags: web
      :exclude-tags: deprecated
      :maxdepth: 2

Advanced Features
-----------------

Tag Exclusion
~~~~~~~~~~~~~

Exclude certain tags:

.. code-block:: rst

   .. tagtoctree::
      :tags: python
      :exclude-tags: deprecated, experimental
      
      Show Python docs except deprecated and experimental ones.

Tag Sorting
~~~~~~~~~~~

.. code-block:: rst

   .. tagtoctree::
      :tags: tutorial
      :sort: alphabetical
      
   .. tagtoctree::
      :tags: api
      :sort: creation-date

Custom Tag Display
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. tagtoctree::
      :tags: python
      :show-tags: true
      :tag-format: badge
      
      Documents will show their tags as badges.

Tag Count Display
~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Available Topics
   ================
   
   .. taglist::
      :show-count: true
      :format: table
      
      ==================  =====
      Tag                 Count
      ==================  =====
      python              15
      javascript          12
      tutorial            25
      ==================  =====

Nested Tags
~~~~~~~~~~~

.. code-block:: rst

   .. tags:: python, tutorial, beginner
   .. tags:: web, backend
   
   Python Web Development for Beginners
   =====================================

Tag Inheritance
~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   tagtoctree_tag_inheritance = {
       'python': ['programming'],
       'javascript': ['programming'],
       'tutorial': ['learning'],
   }

Now documents tagged with ``python`` automatically get ``programming`` tag.

Docker Integration
------------------

Build Tagged Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     kensai-sphinx:latest \
     sphinx-build -b html /project/docs /project/docs/_build/html

Generate Tag Report
~~~~~~~~~~~~~~~~~~~

Create ``generate_tag_report.py``:

.. code-block:: python

   import os
   import re
   from pathlib import Path
   
   def extract_tags(file_path):
       with open(file_path, 'r') as f:
           content = f.read()
           match = re.search(r'\.\. tags:: (.+)', content)
           if match:
               return match.group(1).split(', ')
       return []
   
   docs_dir = Path('docs')
   tag_map = {}
   
   for rst_file in docs_dir.rglob('*.rst'):
       tags = extract_tags(rst_file)
       for tag in tags:
           if tag not in tag_map:
               tag_map[tag] = []
           tag_map[tag].append(str(rst_file))
   
   print("Tag Report")
   print("=" * 50)
   for tag, files in sorted(tag_map.items()):
       print(f"\n{tag} ({len(files)} documents):")
       for file in files:
           print(f"  - {file}")

Run:

.. code-block:: bash

   docker run --rm -v $(pwd):/project \
     kensai-sphinx:latest \
     python /project/generate_tag_report.py

Complete Project Example
-------------------------

Project Structure
~~~~~~~~~~~~~~~~~

.. code-block:: text

   myproject/
   ├── docs/
   │   ├── conf.py
   │   ├── index.rst
   │   ├── tags.rst
   │   ├── tutorials/
   │   │   ├── beginner/
   │   │   │   ├── intro.rst         # tags: beginner, tutorial
   │   │   │   └── basics.rst        # tags: beginner, tutorial
   │   │   ├── intermediate/
   │   │   │   ├── classes.rst       # tags: intermediate, tutorial
   │   │   │   └── modules.rst       # tags: intermediate, tutorial
   │   │   └── advanced/
   │   │       ├── metaclasses.rst   # tags: advanced, tutorial
   │   │       └── decorators.rst    # tags: advanced, tutorial
   │   ├── api/
   │   │   ├── core.rst              # tags: api, reference
   │   │   └── utils.rst             # tags: api, reference
   │   └── examples/
   │       ├── web.rst               # tags: example, web
   │       └── cli.rst               # tags: example, cli

conf.py
~~~~~~~

.. code-block:: python

   extensions = ['sphinx_tagtoctree']
   
   tagtoctree_enabled = True
   tagtoctree_show_tag_count = True
   
   tagtoctree_tags = {
       'beginner': {'title': 'Beginner', 'icon': '🌱'},
       'intermediate': {'title': 'Intermediate', 'icon': '📈'},
       'advanced': {'title': 'Advanced', 'icon': '🚀'},
       'tutorial': {'title': 'Tutorial', 'icon': '📖'},
       'api': {'title': 'API', 'icon': '⚙️'},
       'example': {'title': 'Example', 'icon': '💡'},
   }

index.rst
~~~~~~~~~

.. code-block:: rst

   Welcome
   =======
   
   Browse by Difficulty
   --------------------
   
   .. tagtoctree::
      :tags: beginner
      :caption: Beginner
      :maxdepth: 1
   
   .. tagtoctree::
      :tags: intermediate
      :caption: Intermediate
      :maxdepth: 1
   
   .. tagtoctree::
      :tags: advanced
      :caption: Advanced
      :maxdepth: 1
   
   Browse by Type
   --------------
   
   .. tagtoctree::
      :tags: tutorial
      :caption: Tutorials
   
   .. tagtoctree::
      :tags: api
      :caption: API Reference
   
   .. tagtoctree::
      :tags: example
      :caption: Examples

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Build Tagged Documentation
   
   on:
     push:
       paths:
         - 'docs/**'
   
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Build Docs
           run: |
             docker run --rm -v $(pwd):/project \
               kensai-sphinx:latest \
               sphinx-build -b html docs/ docs/_build/html
         
         - name: Generate Tag Report
           run: |
             docker run --rm -v $(pwd):/project \
               kensai-sphinx:latest \
               python generate_tag_report.py > tag_report.txt
         
         - name: Upload Report
           uses: actions/upload-artifact@v3
           with:
             name: tag-report
             path: tag_report.txt


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

Best Practices
--------------

1. **Use Consistent Tag Names**
   
   Define standard tags for your project:
   
   .. code-block:: python
   
      # conf.py - Define all available tags
      tagtoctree_tags = {
          'beginner': {...},
          'intermediate': {...},
          'advanced': {...},
      }

2. **Tag Hierarchies**
   
   Use tag inheritance for related concepts:
   
   .. code-block:: python
   
      tagtoctree_tag_inheritance = {
          'python3': ['python'],
          'django': ['python', 'web'],
      }

3. **Multiple Views**
   
   Create different views of the same content:
   
   .. code-block:: rst
   
      # By difficulty
      .. tagtoctree::
         :tags: beginner
      
      # By topic
      .. tagtoctree::
         :tags: python

4. **Document Tag Meanings**
   
   Create a tags page explaining each tag:
   
   .. code-block:: rst
   
      Tag Glossary
      ============
      
      - **beginner**: No prior knowledge required
      - **advanced**: Requires solid understanding
      - **api**: API documentation

5. **Use Tag Exclusion**
   
   Hide deprecated or experimental content:
   
   .. code-block:: rst
   
      .. tagtoctree::
         :exclude-tags: deprecated, experimental

6. **Combine with Other Features**
   
   Mix tags with traditional toctree:
   
   .. code-block:: rst
   
      .. toctree::
         :maxdepth: 2
         
         introduction
         
      .. tagtoctree::
         :tags: tutorial
         :maxdepth: 1

Common Patterns
---------------

Learning Path
~~~~~~~~~~~~~

.. code-block:: rst

   Learning Path
   =============
   
   Step 1: Basics
   
   .. tagtoctree::
      :tags: beginner, step1
      :operator: and
   
   Step 2: Fundamentals
   
   .. tagtoctree::
      :tags: beginner, step2
      :operator: and
   
   Step 3: Practice
   
   .. tagtoctree::
      :tags: beginner, practice
      :operator: and

Feature Matrix
~~~~~~~~~~~~~~

.. code-block:: rst

   Feature Documentation
   =====================
   
   Stable Features
   
   .. tagtoctree::
      :tags: feature, stable
      :operator: and
   
   Beta Features
   
   .. tagtoctree::
      :tags: feature, beta
      :operator: and
   
   Experimental Features
   
   .. tagtoctree::
      :tags: feature, experimental
      :operator: and

Troubleshooting
---------------

Tags Not Working
~~~~~~~~~~~~~~~~

**Issue:** Tags don't appear in TOC

**Solution:**

1. Check extension is enabled:

   .. code-block:: python
   
      extensions = ['sphinx_tagtoctree']

2. Verify tag syntax:

   .. code-block:: rst
   
      .. tags:: tag1, tag2

3. Rebuild docs:

   .. code-block:: bash
   
      docker run --rm -v $(pwd):/project kensai-sphinx:latest \
        sphinx-build -b html docs/ docs/_build/html

Empty Tag TOC
~~~~~~~~~~~~~

**Issue:** Tag toctree is empty

**Solution:**

Check if documents are actually tagged:

.. code-block:: bash

   grep -r ".. tags::" docs/

Documents Not Appearing
~~~~~~~~~~~~~~~~~~~~~~~~

**Issue:** Tagged document doesn't show up

**Solution:**

Verify tag operator:

.. code-block:: rst

   # Wrong - requires BOTH tags
   .. tagtoctree::
      :tags: python, advanced
      :operator: and
   
   # Correct - requires EITHER tag
   .. tagtoctree::
      :tags: python, advanced
      :operator: or

Next Steps
----------

1. Plan your tagging strategy
2. Tag existing documentation
3. Create tag-based navigation
4. Build a tag index page
5. Integrate into your documentation workflow


Practical Examples
------------------

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

Additional Resources
--------------------

- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- :doc:`../extensions` - Other useful extensions
- `Sphinx Documentation <https://www.sphinx-doc.org/>`_
