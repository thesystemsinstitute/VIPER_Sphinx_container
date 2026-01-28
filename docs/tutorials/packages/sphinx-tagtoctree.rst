Sphinx-Tagtoctree Tutorial
===========================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-tagtoctree/>`_
   - :doc:`See Working Example <../../examples/sphinx-tagtoctree-example>`


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

Practical Examples
------------------

Example 1: Multi-Level Learning Path
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create ``docs/index.rst``:

.. code-block:: rst

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

Additional Resources
--------------------

- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- :doc:`../extensions` - Other useful extensions
- `Sphinx Documentation <https://www.sphinx-doc.org/>`_
