MyST-Parser Example
===================

This page demonstrates the **myst-parser** extension for using Markdown (MyST - Markedly Structured Text) in Sphinx documentation.

.. contents:: Contents
   :local:
   :depth: 2

Overview
--------

The myst-parser extension enables rich Markdown support in Sphinx, combining Markdown's simplicity with the power of reStructuredText through the MyST (Markedly Structured Text) syntax.

Basic Markdown
--------------

Text Formatting
~~~~~~~~~~~~~~~

Create a ``.md`` file with basic Markdown:

.. code-block:: markdown

   # Heading 1
   ## Heading 2
   ### Heading 3
   
   **Bold text** and *italic text*
   
   `inline code` and ~~strikethrough~~
   
   [Link text](https://example.com)

Lists
~~~~~

.. code-block:: markdown

   - Unordered list
   - Second item
     - Nested item
   
   1. Ordered list
   2. Second item
      1. Nested numbered item

Code Blocks
~~~~~~~~~~~

.. code-block:: markdown

   ```python
   def hello():
       print("Hello, World!")
   ```
   
   ```{code-block} python
   :linenos:
   :caption: example.py
   
   def advanced():
       pass
   ```

MyST Extensions
---------------

Directives
~~~~~~~~~~

MyST-style directives in Markdown:

.. code-block:: markdown

   ```{note}
   This is a note directive in MyST syntax.
   ```
   
   ```{warning}
   This is a warning!
   ```
   
   ```{admonition} Custom Title
   Custom admonition content.
   ```

Roles
~~~~~

Inline roles:

.. code-block:: markdown

   Reference {ref}`section-label` or {doc}`other-file`.
   
   Code reference: {py:func}`myfunction`
   
   Math: {math}`E = mc^2`

Cross-References
----------------

Internal Links
~~~~~~~~~~~~~~

.. code-block:: markdown

   (target-label)=
   ## Section Title
   
   Link to [section](target-label) or {ref}`target-label`.

Document Links
~~~~~~~~~~~~~~

.. code-block:: markdown

   See {doc}`other-document` or {doc}`path/to/document`.
   
   Download {download}`file.pdf`

Auto-Labels
~~~~~~~~~~~

.. code-block:: markdown

   ## My Section
   
   Link to [My Section](#my-section)

Math Support
------------

Inline Math
~~~~~~~~~~~

.. code-block:: markdown

   Einstein's equation is $E = mc^2$.
   
   Or using role: {math}`E = mc^2`

Block Math
~~~~~~~~~~

.. code-block:: markdown

   ```{math}
   :label: my-equation
   
   \int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
   ```
   
   Reference equation {eq}`my-equation`.

Tables
------

Basic Tables
~~~~~~~~~~~~

.. code-block:: markdown

   | Header 1 | Header 2 | Header 3 |
   |----------|----------|----------|
   | Cell 1   | Cell 2   | Cell 3   |
   | Cell 4   | Cell 5   | Cell 6   |

Advanced Tables
~~~~~~~~~~~~~~~

.. code-block:: markdown

   ```{list-table} Table Title
   :header-rows: 1
   :widths: 20 30 50
   
   * - Column 1
     - Column 2
     - Column 3
   * - Data 1
     - Data 2
     - Data 3
   ```

Figures and Images
------------------

Basic Images
~~~~~~~~~~~~

.. code-block:: markdown

   ![Alt text](image.png)
   
   ![Alt text](image.png "Image title")

Advanced Figures
~~~~~~~~~~~~~~~~

.. code-block:: markdown

   ```{figure} image.png
   :alt: Alternative text
   :width: 400px
   :align: center
   
   Figure caption goes here.
   ```

Configuration
-------------

Basic Setup
~~~~~~~~~~~

.. code-block:: python

   # conf.py
   extensions = [
       'myst_parser',
   ]
   
   # Source file suffixes
   source_suffix = {
       '.rst': 'restructuredtext',
       '.md': 'markdown',
   }

Enable Extensions
~~~~~~~~~~~~~~~~~

.. code-block:: python

   myst_enable_extensions = [
       "amsmath",          # Math support
       "colon_fence",      # ::: fences
       "deflist",          # Definition lists
       "dollarmath",       # $ and $$ for math
       "fieldlist",        # Field lists
       "html_admonition",  # HTML-style admonitions
       "html_image",       # HTML images
       "linkify",          # Auto-link URLs
       "replacements",     # Character replacements
       "smartquotes",      # Smart quotes
       "strikethrough",    # ~~text~~
       "substitution",     # Substitutions
       "tasklist",         # Task lists
   ]

Advanced Features
-----------------

Task Lists
~~~~~~~~~~

.. code-block:: markdown

   - [x] Completed task
   - [ ] Pending task
   - [ ] Another task

Definition Lists
~~~~~~~~~~~~~~~~

.. code-block:: markdown

   Term 1
   : Definition of term 1
   
   Term 2
   : Definition of term 2
   : Second definition

Field Lists
~~~~~~~~~~~

.. code-block:: markdown

   :Author: John Doe
   :Version: 1.0
   :Date: 2024-01-26

Substitutions
~~~~~~~~~~~~~

.. code-block:: markdown

   {{ version }}
   
   {{ author }}

Colon Fence
~~~~~~~~~~~

.. code-block:: markdown

   :::note
   Using colon fence instead of backticks.
   :::

Mixed Content
-------------

reStructuredText in Markdown
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: markdown

   ```{eval-rst}
   .. note::
      This is RST content in a Markdown file.
   
   .. code-block:: python
   
      def example():
          pass
   ```

Markdown in reStructuredText
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. md::
   
      # Markdown content
      
      This is **Markdown** in an RST file.

Front Matter
------------

YAML Front Matter
~~~~~~~~~~~~~~~~~

.. code-block:: markdown

   ---
   title: My Page Title
   author: John Doe
   date: 2024-01-26
   ---
   
   # Page Content

Sphinx Metadata
~~~~~~~~~~~~~~~

.. code-block:: markdown

   ---
   orphan: true
   nosearch: true
   ---

Practical Examples
------------------

Documentation Page
~~~~~~~~~~~~~~~~~~

Complete Markdown documentation page:

.. code-block:: markdown

   ---
   title: API Reference
   ---
   
   # API Reference
   
   ## Overview
   
   This API provides access to our service.
   
   ```{note}
   Authentication required for all endpoints.
   ```
   
   ## Endpoints
   
   ### GET /users
   
   Returns list of users.
   
   **Parameters:**
   
   - `limit` (int): Maximum number of results
   - `offset` (int): Pagination offset
   
   **Example:**
   
   ```python
   import requests
   
   response = requests.get("https://api.example.com/users")
   ```

Tutorial
~~~~~~~~

.. code-block:: markdown

   # Getting Started
   
   ## Installation
   
   ```bash
   pip install mypackage
   ```
   
   ## Quick Start
   
   1. Import the package:
   
      ```python
      import mypackage
      ```
   
   2. Create a client:
   
      ```python
      client = mypackage.Client()
      ```
   
   3. Use the API:
   
      ```python
   result = client.process()
      ```
   
   ```{tip}
   Check the {doc}`api-reference` for more details.
   ```

Best Practices
--------------

When to Use MyST
~~~~~~~~~~~~~~~~

**Advantages:**

- Familiar Markdown syntax
- Easier for contributors
- Good for simple documentation
- Compatible with GitHub README

**Use RST When:**

- Complex cross-references needed
- Advanced Sphinx directives
- Existing RST codebase
- Need all Sphinx features

File Organization
~~~~~~~~~~~~~~~~~

.. code-block:: text

   docs/
   ├── index.rst          # Main index (RST)
   ├── api/
   │   ├── index.rst      # API index (RST)
   │   └── reference.md   # API ref (Markdown)
   ├── tutorials/
   │   ├── intro.md       # Tutorials in MD
   │   └── advanced.md
   └── conf.py

See Also
--------

- :doc:`../tutorials/packages/myst-parser` - Complete tutorial
- GitHub repository: https://github.com/executablebooks/MyST-Parser
- MyST syntax guide: https://myst-parser.readthedocs.io/
