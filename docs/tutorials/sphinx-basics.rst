Sphinx Basics Tutorial
======================

This tutorial covers the fundamentals of using Sphinx to create beautiful documentation.

What is Sphinx?
---------------

Sphinx is a documentation generator that converts reStructuredText (and Markdown) files 
into various output formats including HTML, PDF, ePub, and more. It was originally created 
for the Python documentation but is now used across many programming languages.

Key Features
~~~~~~~~~~~~

* **Output formats**: HTML, LaTeX (for PDF), ePub, Texinfo, manual pages, plain text
* **Extensive cross-references**: Semantic markup and automatic links
* **Hierarchical structure**: Easy definition of document tree
* **Automatic indices**: General index and module index
* **Code highlighting**: Automatic highlighting using Pygments
* **Extensions**: Many extensions available via the Sphinx Contrib project

Creating Your First Project
----------------------------

Step 1: Initialize a New Sphinx Project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the container to create a new Sphinx project:

.. code-block:: bash

   docker run -v $(pwd):/project kensai-sphinx \
       sphinx-quickstart /project/docs

This will ask you several questions:

* **Separate source and build directories?** Usually "yes" (y)
* **Project name:** Your project name
* **Author name:** Your name
* **Project release:** Version number (e.g., 1.0)
* **Project language:** en (English) or your language code

Directory Structure
~~~~~~~~~~~~~~~~~~~

After initialization, you'll have:

.. code-block:: text

   docs/
   ├── _build/          # Generated documentation
   ├── _static/         # Static files (CSS, images)
   ├── _templates/      # Custom templates
   ├── conf.py          # Configuration file
   ├── index.rst        # Main document
   └── Makefile         # Build automation

Step 2: Understanding conf.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``conf.py`` file is the configuration heart of your Sphinx project. Key sections:

**Project Information**

.. code-block:: python

   project = 'My Project'
   copyright = '2026, My Name'
   author = 'My Name'
   release = '1.0'

**Extensions**

.. code-block:: python

   extensions = [
       'sphinx.ext.autodoc',      # Auto-document from docstrings
       'sphinx.ext.napoleon',     # Google/NumPy style docstrings
       'sphinx.ext.viewcode',     # Add links to source code
       'myst_parser',             # Markdown support
   ]

**HTML Theme**

.. code-block:: python

   html_theme = 'sphinx_rtd_theme'  # Read the Docs theme

Step 3: Writing Content
~~~~~~~~~~~~~~~~~~~~~~~

reStructuredText Basics
^^^^^^^^^^^^^^^^^^^^^^^^

Create a new file ``docs/getting-started.rst``:

.. code-block:: rst

   Getting Started
   ===============

   This is a paragraph with **bold** and *italic* text.

   Section
   -------

   Subsection
   ~~~~~~~~~~

   * Bullet list item 1
   * Bullet list item 2

   1. Numbered list
   2. Another item

   Code Examples
   -------------

   Python code::

       def hello():
           print("Hello, World!")

   Or with syntax highlighting:

   .. code-block:: python

       def greet(name):
           return f"Hello, {name}!"

Cross-References
^^^^^^^^^^^^^^^^

Link to other documents:

.. code-block:: rst

   See :doc:`getting-started` for more info.

   Or with custom text: :doc:`Get started <getting-started>`

External links:

.. code-block:: rst

   Visit `Python <https://www.python.org/>`_ website.

Step 4: Building Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using the Container
^^^^^^^^^^^^^^^^^^^

Build HTML documentation:

.. code-block:: bash

   docker run -v $(pwd):/project kensai-sphinx \
       sphinx-build -b html /project/docs /project/docs/_build/html

Build PDF (LaTeX):

.. code-block:: bash

   docker run -v $(pwd):/project kensai-sphinx \
       sphinx-build -b latex /project/docs /project/docs/_build/latex

Auto-rebuild on Changes
^^^^^^^^^^^^^^^^^^^^^^^^

Use ``sphinx-autobuild`` for live preview:

.. code-block:: bash

   docker run -p 8000:8000 -v $(pwd):/project kensai-sphinx \
       sphinx-autobuild /project/docs /project/docs/_build/html \
       --host 0.0.0.0 --port 8000

Visit ``http://localhost:8000`` and see changes update automatically!

Advanced Features
-----------------

Table of Contents Tree
~~~~~~~~~~~~~~~~~~~~~~~

Create a documentation structure in ``index.rst``:

.. code-block:: rst

   .. toctree::
      :maxdepth: 2
      :caption: Contents:

      getting-started
      user-guide
      api-reference
      faq

This creates a navigation tree with your documents.

Admonitions
~~~~~~~~~~~

Create attention-grabbing boxes:

.. note::
   This is a note admonition.

.. warning::
   This is a warning!

.. tip::
   Here's a helpful tip.

.. code-block:: rst

   .. note::
      This is a note admonition.

   .. warning::
      This is a warning!

   .. tip::
      Here's a helpful tip.

Images and Figures
~~~~~~~~~~~~~~~~~~

Add images:

.. code-block:: rst

   .. image:: _static/logo.png
      :width: 200px
      :alt: Logo

   .. figure:: _static/diagram.png
      :width: 400px

      This is the figure caption.

Tables
~~~~~~

Simple tables:

.. code-block:: rst

   ===== ===== =====
   Col1  Col2  Col3
   ===== ===== =====
   A     B     C
   D     E     F
   ===== ===== =====

Or list-tables (easier for complex tables):

.. code-block:: rst

   .. list-table:: My Table
      :header-rows: 1
      :widths: 20 30 50

      * - Header 1
        - Header 2
        - Header 3
      * - Row 1
        - Data
        - More data
      * - Row 2
        - Data
        - More data

Documenting Code
----------------

Python Docstrings
~~~~~~~~~~~~~~~~~

Write docstrings in your Python code:

.. code-block:: python

   def calculate_area(width, height):
       """Calculate the area of a rectangle.

       Args:
           width (float): The width of the rectangle.
           height (float): The height of the rectangle.

       Returns:
           float: The calculated area.

       Example:
           >>> calculate_area(5, 10)
           50.0
       """
       return width * height

Then document it in Sphinx:

.. code-block:: rst

   .. autofunction:: mymodule.calculate_area

Markdown Support
~~~~~~~~~~~~~~~~

With MyST Parser, you can also write in Markdown:

.. code-block:: markdown

   # My Page

   This is a paragraph with **bold** and *italic*.

   ## Code Example

   ```python
   def hello():
       print("Hello!")
   ```

   See {doc}`other-page` for more info.

Best Practices
--------------

1. **Consistent Structure**: Keep a logical hierarchy in your documentation
2. **Cross-reference**: Link between related sections
3. **Code Examples**: Include practical examples
4. **Keep it Updated**: Update docs with code changes
5. **Use Extensions**: Leverage Sphinx extensions for specific needs
6. **Version Control**: Keep your docs in git with your code
7. **Automated Builds**: Use CI/CD to build and deploy docs

Example Project Structure
--------------------------

.. code-block:: text

   myproject/
   ├── docs/
   │   ├── _static/
   │   ├── _templates/
   │   ├── api/
   │   │   └── index.rst
   │   ├── tutorials/
   │   │   ├── index.rst
   │   │   ├── getting-started.rst
   │   │   └── advanced.rst
   │   ├── conf.py
   │   └── index.rst
   ├── src/
   │   └── myproject/
   │       └── __init__.py
   └── README.md

Next Steps
----------

* Learn about :doc:`themes` to customize your documentation appearance
* Explore :doc:`extensions` to add functionality
* Check out :doc:`../examples/index` for real-world examples

Video Tutorial
--------------

.. raw:: html

   <iframe width="560" height="315" 
   src="https://www.youtube.com/embed/oJsUvBQyHBs" 
   title="Sphinx Tutorial" 
   frameborder="0" 
   allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
   allowfullscreen></iframe>

Resources
---------

* `Sphinx Documentation <https://www.sphinx-doc.org/>`_
* `reStructuredText Primer <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_
* `Sphinx Tutorial <https://www.sphinx-doc.org/en/master/tutorial/>`_
