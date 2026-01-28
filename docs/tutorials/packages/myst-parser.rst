myst-parser Tutorial
====================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/myst-parser/>`_
   - `API Documentation <../../pdoc/myst_parser/index.html>`_
   - `Manual <https://myst-parser.readthedocs.io/>`_
   - :doc:`Working Example <../../examples/myst-parser-example>`


.. contents:: Table of Contents
   :local:
   :depth: 2

The MyST (Markedly Structured Text) parser allows you to write Sphinx documentation in 
Markdown instead of reStructuredText.

What is MyST?
-------------
MyST is a rich and extensible flavor of Markdown designed for technical documentation. 
It's fully compatible with CommonMark and adds powerful features like:

- Roles and directives (similar to RST)
- Extensible syntax
- Cross-references
- Math equations
- Admonitions
- And much more!

The myst-parser extension enables rich Markdown support in Sphinx, combining Markdown's simplicity with the power of reStructuredText through the MyST (Markedly Structured Text) syntax.


Installation
------------

Already included in this container!

For your own environment:

.. code-block:: bash

   pip install myst-parser

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = ['myst_parser']
   
   # Enable both .rst and .md files
   source_suffix = {
       '.rst': 'restructuredtext',
       '.md': 'markdown',
   }

Enable MyST Extensions
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   myst_enable_extensions = [
       "amsmath",          # LaTeX math
       "colon_fence",      # ::: fences
       "deflist",          # Definition lists
       "dollarmath",       # $...$ and $$...$$ math
       "fieldlist",        # Field lists
       "html_admonition",  # HTML admonitions
       "html_image",       # HTML images
       "linkify",          # Auto-detect URLs
       "replacements",     # Text replacements
       "smartquotes",      # Smart quotes
       "strikethrough",    # ~~text~~
       "substitution",     # {{ variable }}
       "tasklist",         # - [ ] Task lists
   ]


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

Basic Markdown Syntax
---------------------

Create a file ``page.md``:

.. code-block:: markdown

   # My Page Title
   
   This is a paragraph with **bold** and *italic* text.
   
   ## Section Heading
   
   - Bullet point 1
   - Bullet point 2
   - Bullet point 3
   
   1. Numbered item
   2. Another item
   
   ### Code Example
   
   ```python
   def hello():
       print("Hello from Markdown!")
   ```
   
   ## Links
   
   [External link](https://sphinx-doc.org)
   
   Internal link to {doc}`other-page`

MyST-Specific Features
----------------------

Directives
~~~~~~~~~~

Use `:::` or ` ```{directive}`:

.. code-block:: markdown

   :::{note}
   This is a note using MyST syntax!
   :::
   
   ```{warning}
   This is a warning!
   ```
   
   ```{code-block} python
   :linenos:
   :emphasize-lines: 2,3
   
   def calculate(x, y):
       result = x + y  # Line 2 (highlighted)
       return result   # Line 3 (highlighted)
   ```

Roles
~~~~~

.. code-block:: markdown

   Reference a class: {class}`MyClass`
   
   Reference a function: {func}`my_function`
   
   Reference a module: {mod}`my_module`
   
   External link: {external:ref}`python:list`
   
   Math inline: {math}`x^2 + y^2 = z^2`

Cross-References
~~~~~~~~~~~~~~~~

.. code-block:: markdown

   # My Section
   
   (my-target)=
   ## Target Section
   
   Content here.
   
   ## Another Section
   
   Link to {ref}`my-target` above.
   
   Link to another document: {doc}`../other-page`

Admonitions
~~~~~~~~~~~

.. code-block:: markdown

   :::{note}
   This is a note.
   :::
   
   :::{warning}
   Be careful!
   :::
   
   :::{tip}
   Pro tip here!
   :::
   
   :::{admonition} Custom Title
   :class: important
   
   Custom admonition with a title.
   :::

Math Equations
~~~~~~~~~~~~~~

Inline math:

.. code-block:: markdown

   The equation $E = mc^2$ is famous.
   
   Or using role: {math}`E = mc^2`

Block math:

.. code-block:: markdown

   $$
   \int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
   $$
   
   Or using directive:
   
   ```{math}
   :label: my-equation
   
   e^{i\pi} + 1 = 0
   ```
   
   Reference equation {eq}`my-equation`.

Tables
~~~~~~

.. code-block:: markdown

   | Header 1 | Header 2 | Header 3 |
   |----------|----------|----------|
   | Cell 1   | Cell 2   | Cell 3   |
   | Cell 4   | Cell 5   | Cell 6   |
   
   Or use list-table directive:
   
   ```{list-table} My Table
   :header-rows: 1
   :widths: 20 30 50
   
   * - Column 1
     - Column 2
     - Column 3
   * - Data
     - More data
     - Even more data
   ```

Images and Figures
~~~~~~~~~~~~~~~~~~

.. code-block:: markdown

   ![Alt text](path/to/image.png)
   
   Or with directive:
   
   ```{image} path/to/image.png
   :alt: Alternative text
   :width: 400px
   :align: center
   ```
   
   For figures with captions:
   
   ```{figure} path/to/diagram.png
   :name: my-figure
   :width: 500px
   
   This is the figure caption.
   ```
   
   Reference: {numref}`my-figure`

Task Lists
~~~~~~~~~~

.. code-block:: markdown

   - [x] Completed task
   - [ ] Incomplete task
   - [ ] Another task

Definition Lists
~~~~~~~~~~~~~~~~

.. code-block:: markdown

   Term 1
   : Definition of term 1
   
   Term 2
   : Definition of term 2
   : Second definition of term 2

Substitutions
~~~~~~~~~~~~~

In ``conf.py``:

.. code-block:: python

   myst_substitutions = {
       "project_name": "My Project",
       "version": "1.0.0",
   }

In Markdown:

.. code-block:: markdown

   Welcome to {{ project_name }} version {{ version }}!

Advanced Features
-----------------

Field Lists
~~~~~~~~~~~

.. code-block:: markdown

   :author: John Doe
   :date: 2026-01-25
   :version: 1.0

HTML in Markdown
~~~~~~~~~~~~~~~~

.. code-block:: markdown

   <div class="custom-class">
   
   This is **Markdown** inside HTML!
   
   </div>

Comments
~~~~~~~~

.. code-block:: markdown

   % This is a comment (won't appear in output)
   
   (comment)=
   This is also a comment using a target.

Auto-generated ToC
~~~~~~~~~~~~~~~~~~

.. code-block:: markdown

   ```{contents}
   :depth: 2
   :local:
   ```

Complete Example
----------------

Full Markdown document:

.. code-block:: markdown

   ---
   title: My Document
   author: John Doe
   date: 2026-01-25
   ---
   
   # Introduction
   
   Welcome to {{ project_name }}!
   
   :::{note}
   This is built with MyST Parser.
   :::
   
   ## Features
   
   - **Bold** and *italic* text
   - Code blocks with syntax highlighting
   - Math equations: $E = mc^2$
   - Cross-references
   
   ## Code Example
   
   ```{code-block} python
   :caption: hello.py
   :linenos:
   
   def greet(name: str) -> str:
       """Greet someone."""
       return f"Hello, {name}!"
   
   print(greet("World"))
   ```
   
   ## See Also
   
   - {doc}`../tutorials/sphinx-basics`
   - [Sphinx Docs](https://sphinx-doc.org)
   
   ## Tasks
   
   - [x] Write documentation
   - [ ] Add examples
   - [ ] Review content

Mixing RST and Markdown
------------------------

You can use both in the same project:

.. code-block:: rst

   .. toctree::
      :maxdepth: 2
      
      intro.md
      guide.rst
      api.md
      examples.rst

Configuration Examples
----------------------

Minimal
~~~~~~~

.. code-block:: python

   extensions = ['myst_parser']

Full Featured
~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['myst_parser']
   
   source_suffix = {
       '.rst': 'restructuredtext',
       '.md': 'markdown',
   }
   
   myst_enable_extensions = [
       "amsmath",
       "colon_fence",
       "deflist",
       "dollarmath",
       "fieldlist",
       "html_admonition",
       "html_image",
       "linkify",
       "replacements",
       "smartquotes",
       "strikethrough",
       "substitution",
       "tasklist",
   ]
   
   myst_heading_anchors = 3  # Auto-generate anchors for h1-h3
   
   myst_substitutions = {
       "project": "My Project",
       "version": "1.0.0",
   }
   
   myst_url_schemes = ["http", "https", "mailto", "ftp"]

Best Practices
--------------

1. **Consistency**: Choose Markdown or RST for each project
2. **Extensions**: Only enable needed extensions
3. **Syntax**: Use MyST syntax for advanced features
4. **Testing**: Test cross-references and directives
5. **Documentation**: Comment complex MyST usage

Troubleshooting
---------------

Directive Not Recognized
~~~~~~~~~~~~~~~~~~~~~~~~~

Check extension is enabled:

.. code-block:: python

   myst_enable_extensions = ["colon_fence"]

Cross-Reference Not Working
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use proper syntax:

.. code-block:: markdown

   {doc}`page-name`    # For documents
   {ref}`target-name`  # For targets

Math Not Rendering
~~~~~~~~~~~~~~~~~~

Enable math extension:

.. code-block:: python

   myst_enable_extensions = ["dollarmath"]
   extensions = ['myst_parser', 'sphinx.ext.mathjax']

Resources
---------

* `MyST Parser Documentation <https://myst-parser.readthedocs.io/>`_
* `MyST Syntax Guide <https://myst-parser.readthedocs.io/en/latest/syntax/syntax.html>`_
* `GitHub Repository <https://github.com/executablebooks/MyST-Parser>`_

Video Tutorial
--------------

.. raw:: html

   <iframe width="560" height="315" 
   src="https://www.youtube.com/embed/qRSb299awB0" 
   title="MyST Markdown Tutorial" 
   frameborder="0" 
   allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
   allowfullscreen></iframe>
