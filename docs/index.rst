KENSAI Sphinx Documentation Container
======================================

.. image:: https://img.shields.io/badge/Python-3.13-blue.svg
   :target: https://www.python.org/downloads/
   :alt: Python Version

.. image:: https://img.shields.io/badge/Sphinx-Documentation-green.svg
   :target: https://www.sphinx-doc.org/
   :alt: Sphinx Documentation

Welcome to the KENSAI Sphinx Container documentation! This container provides a comprehensive, 
ready-to-use environment for generating beautiful documentation using Sphinx and related tools.

Purpose
-------

This Docker container is designed to:

* Provide a complete Sphinx documentation generation environment
* Include a wide range of Sphinx extensions and themes
* Support multiple documentation formats (HTML, PDF, ePub, etc.)
* Include Graphviz for diagram generation
* Offer a portable, consistent documentation environment across platforms
* Serve generated documentation via built-in web server

The container is built on Python 3.13 Alpine Linux for minimal footprint while maintaining 
full functionality.

Sphinx Documentation
--------------------

Sphinx is a powerful documentation generator that makes it easy to create intelligent and 
beautiful documentation. Learn more:

* `Official Sphinx Documentation <https://www.sphinx-doc.org/>`_
* `Sphinx Tutorial <https://www.sphinx-doc.org/en/master/tutorial/>`_
* `reStructuredText Primer <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_

How to Use This Container
--------------------------

From Your Project
~~~~~~~~~~~~~~~~~

**Option 1: Using Docker Run**

.. code-block:: bash

   # Build the container
   docker build -t kensai-sphinx .

   # Run to generate documentation from your project
   docker run -v /path/to/your/project:/project kensai-sphinx \
       sphinx-build /project/docs /project/docs/_build/html

   # Serve the documentation
   docker run -p 8080:8080 -v /path/to/your/project:/project kensai-sphinx

**Option 2: Using Docker Compose**

Create a ``docker-compose.yml`` in your project:

.. code-block:: yaml

   version: '3.8'
   services:
     sphinx:
       image: kensai-sphinx
       ports:
         - "8080:8080"
       volumes:
         - ./docs:/project/docs
         - ./docs/_build:/project/docs/_build

Then run:

.. code-block:: bash

   docker-compose up

**Option 3: Using the Build Scripts**

For Windows:

.. code-block:: batch

   build.bat

For Linux/Mac:

.. code-block:: bash

   ./build.sh

Accessing the Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once the container is running, open your browser and navigate to:

.. code-block:: text

   http://localhost:8080

Installed Tools
---------------

This container includes:

**System Tools:**

* **Graphviz** - Graph visualization software for creating diagrams
* **pyan3** - Python call graph generator

**Python Documentation Tools:**

* **Sphinx** - Main documentation generator
* **pdoc3** - Auto-generate API documentation
* 80+ Sphinx extensions and themes (see :doc:`sphinx-packages`)

**Supported Formats:**

* HTML (with multiple themes)
* PDF (via LaTeX)
* ePub
* Man pages
* Texinfo

Quick Start Tutorial
--------------------

1. **Create a new Sphinx project:**

   .. code-block:: bash

      docker run -v $(pwd):/project kensai-sphinx \
          sphinx-quickstart /project/docs

2. **Write your documentation** in reStructuredText or Markdown

3. **Build the documentation:**

   .. code-block:: bash

      docker run -v $(pwd):/project kensai-sphinx \
          sphinx-build /project/docs /project/docs/_build/html

4. **View the results** by opening ``docs/_build/html/index.html``

Documentation Sections
----------------------

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   quick-reference
   sphinx-packages

.. toctree::
   :maxdepth: 2
   :caption: Tutorials and Examples:

   tutorials/sphinx-basics
   tutorials/themes
   tutorials/extensions
   tutorials/package-tutorials
   examples/package-examples
   tutorials/doxygen-usage
   tutorials/doxygen-breathe-exhale

Indices and Tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
