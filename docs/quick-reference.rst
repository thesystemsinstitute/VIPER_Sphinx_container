Quick Reference Guide
=====================

This is a quick reference for common tasks with the KENSAI Sphinx Container.

Quick Start
-----------

**Build Container:**

.. code-block:: bash

   # Windows
   build.bat
   
   # Linux/Mac
   ./build.sh

**Run Container:**

.. code-block:: bash

   docker run -p 8080:8080 kensai-sphinx:latest

**Access Documentation:**

Open browser to: http://localhost:8080

Common Commands
---------------

Container Management
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Build image
   docker build -t kensai-sphinx:latest .
   
   # Run container
   docker run -d -p 8080:8080 --name sphinx-docs kensai-sphinx:latest
   
   # Stop container
   docker stop sphinx-docs
   
   # Remove container
   docker rm sphinx-docs
   
   # View logs
   docker logs -f sphinx-docs
   
   # Open shell
   docker exec -it sphinx-docs /bin/sh

Documentation Generation
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Generate HTML docs
   docker run -v $(pwd):/project kensai-sphinx \
     sphinx-build /project/docs /project/docs/_build/html
   
   # Generate PDF
   docker run -v $(pwd):/project kensai-sphinx \
     sphinx-build -b latex /project/docs /project/docs/_build/latex
   
   # Check for broken links
   docker run -v $(pwd):/project kensai-sphinx \
     sphinx-build -b linkcheck /project/docs /project/docs/_build/linkcheck

Development Workflow
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Auto-rebuild on changes
   docker run -p 8000:8000 -v $(pwd):/project kensai-sphinx \
     sphinx-autobuild /project/docs /project/docs/_build/html \
     --host 0.0.0.0 --port 8000

Docker Compose
~~~~~~~~~~~~~~

.. code-block:: bash

   # Start services
   docker-compose up -d
   
   # Stop services
   docker-compose down
   
   # View logs
   docker-compose logs -f
   
   # Start dev mode
   docker-compose --profile dev up -d

Helper Scripts
--------------

Windows
~~~~~~~

.. code-block:: batch

   sphinx-helper.bat build    # Build image
   sphinx-helper.bat run      # Run server
   sphinx-helper.bat dev      # Dev mode
   sphinx-helper.bat stop     # Stop containers
   sphinx-helper.bat clean    # Clean build

Linux/Mac
~~~~~~~~~

.. code-block:: bash

   ./sphinx-helper.sh build   # Build image
   ./sphinx-helper.sh run     # Run server
   ./sphinx-helper.sh dev     # Dev mode
   ./sphinx-helper.sh stop    # Stop containers
   ./sphinx-helper.sh clean   # Clean build

Configuration Snippets
----------------------

Change Theme
~~~~~~~~~~~~

Edit ``docs/conf.py``:

.. code-block:: python

   html_theme = 'furo'
   # Options: 'sphinx_rtd_theme', 'sphinx_book_theme', 
   #          'pydata_sphinx_theme', 'sphinx_material'

Enable Extensions
~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = [
       'sphinx.ext.autodoc',
       'sphinx.ext.napoleon',
       'sphinx_copybutton',
       'myst_parser',
   ]

Add Logo
~~~~~~~~

.. code-block:: python

   html_logo = '_static/logo.png'
   html_favicon = '_static/favicon.ico'

Troubleshooting
---------------

Port Already in Use
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Use different port
   docker run -p 9090:8080 kensai-sphinx:latest

Permission Errors
~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Linux: run as current user
   docker run --user $(id -u):$(id -g) -v $(pwd):/project kensai-sphinx

Build Fails
~~~~~~~~~~~

.. code-block:: bash

   # Clean build
   docker build --no-cache -t kensai-sphinx:latest .

Container Won't Start
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Check logs
   docker logs kensai-sphinx-docs
   
   # Run interactively
   docker run -it --rm kensai-sphinx:latest /bin/sh

File Permissions
----------------

Linux/Mac
~~~~~~~~~

.. code-block:: bash

   # Make scripts executable
   chmod +x build.sh
   chmod +x sphinx-helper.sh

Ports Reference
---------------

- **8080** - Main documentation server
- **8000** - Development server (auto-rebuild)

File Structure
--------------

.. code-block:: text

   project/
   ├── docs/
   │   ├── conf.py          # Configuration
   │   ├── index.rst        # Main page
   │   ├── _static/         # Images, CSS
   │   ├── _templates/      # Custom templates
   │   └── _build/          # Generated output
   ├── Dockerfile
   ├── docker-compose.yml
   ├── requirements.txt
   └── README.md

Environment Variables
---------------------

.. code-block:: bash

   # Change server port
   docker run -e DOCS_PORT=9000 -p 9000:9000 kensai-sphinx:latest

Sphinx Commands
---------------

.. code-block:: bash

   # Initialize new project
   sphinx-quickstart
   
   # Build HTML
   sphinx-build -b html source build/html
   
   # Build PDF
   sphinx-build -b latex source build/latex
   
   # Check links
   sphinx-build -b linkcheck source build/linkcheck
   
   # Generate API docs
   sphinx-apidoc -o docs/api src/

reStructuredText Quick Reference
---------------------------------

**Headers:**

.. code-block:: rst

   Title
   =====
   
   Section
   -------
   
   Subsection
   ~~~~~~~~~~

**Formatting:**

.. code-block:: rst

   **bold**
   *italic*
   ``code``

**Lists:**

.. code-block:: rst

   * Bullet
   * Items
   
   1. Numbered
   2. Items

**Links:**

.. code-block:: rst

   `Link text <https://example.com>`_
   :doc:`other-page`
   :ref:`section-label`

**Code:**

.. code-block:: rst

   .. code-block:: python
   
      def hello():
          print("Hello!")

**Images:**

.. code-block:: rst

   .. image:: path/to/image.png
      :width: 400px

**Admonitions:**

.. code-block:: rst

   .. note::
      Important info
   
   .. warning::
      Be careful!

Resources
---------

- Container docs: http://localhost:8080 (when running)
- Sphinx docs: https://www.sphinx-doc.org/
- Themes: https://sphinx-themes.org/
- Extensions: https://www.sphinx-doc.org/en/master/usage/extensions/

Getting Help
------------

1. Check container documentation at http://localhost:8080
2. View logs: ``docker logs kensai-sphinx-docs``
3. Open shell: ``docker exec -it kensai-sphinx-docs /bin/sh``
4. Check Sphinx documentation
5. Review this quick reference

Tips
----

- Use ``sphinx-autobuild`` for live preview during development
- Keep documentation with your code in version control
- Use ``sphinx-copybutton`` for better UX
- Enable only needed extensions for faster builds
- Test documentation builds in CI/CD pipeline
- Use cross-references to link related sections
- Include examples and code snippets
- Keep generated ``_build/`` out of version control
