Sphinx-Favicon Tutorial
========================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-favicon/>`_
   - `API Documentation <../../pdoc/sphinx_favicon/index.html>`_
   - `Manual <https://github.com/tcmetzger/sphinx-favicon>`_
   - :doc:`Working Example <../../examples/sphinx-favicon-example>`


.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinx-favicon to add custom favicons to your Sphinx documentation.

What is Sphinx-Favicon?
------------------------

sphinx-favicon is a Sphinx extension that provides:

- Custom favicon support
- Multiple favicon formats
- Device-specific icons
- Web app manifest integration
- Apple touch icons
- Windows tile icons
- Android Chrome icons
- SVG favicon support
- Automatic format generation
- Theme integration

This ensures your documentation has professional branding across all devices and platforms.


The sphinx-favicon extension allows you to easily add favicons to your Sphinx documentation with support for multiple formats, sizes, and platform-specific icons.

Installation
------------

sphinx-favicon is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinx_favicon; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_favicon',
   ]
   
   # Basic favicon
   html_favicon = '_static/favicon.ico'

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinx_favicon']
   
   # Multiple favicon formats
   favicons = [
       {
           "rel": "icon",
           "sizes": "16x16",
           "href": "favicon-16x16.png",
           "type": "image/png",
       },
       {
           "rel": "icon",
           "sizes": "32x32",
           "href": "favicon-32x32.png",
           "type": "image/png",
       },
       {
           "rel": "apple-touch-icon",
           "sizes": "180x180",
           "href": "apple-touch-icon.png",
       },
       {
           "rel": "icon",
           "type": "image/svg+xml",
           "href": "favicon.svg",
       },
       {
           "rel": "manifest",
           "href": "site.webmanifest",
       },
   ]
   
   html_static_path = ['_static']

Basic Usage
-----------

Single Favicon
~~~~~~~~~~~~~~

Place ``favicon.ico`` in ``docs/_static/`` and configure:

.. code-block:: python

   html_favicon = '_static/favicon.ico'

Multiple Formats
~~~~~~~~~~~~~~~~

.. code-block:: python

   favicons = [
       {"rel": "icon", "href": "favicon.ico"},
       {"rel": "icon", "sizes": "32x32", "href": "favicon-32x32.png"},
   ]

Advanced Features
-----------------

Conditional Favicons
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import os
   
   favicons = [
       {"rel": "icon", "href": "favicon.ico"},
   ]
   
   # Add development-specific favicon
   if os.environ.get('SPHINX_ENV') == 'development':
       favicons.append({
           "rel": "icon",
           "href": "favicon-dev.ico",
       })

Custom Meta Tags
~~~~~~~~~~~~~~~~

.. code-block:: python

   favicons = [
       {"rel": "icon", "href": "favicon.ico"},
       # Windows tile color
       {
           "name": "msapplication-TileColor",
           "content": "#2196F3",
       },
       # Theme color
       {
           "name": "theme-color",
           "content": "#2196F3",
       },
   ]

Favicon with Color Modes
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   favicons = [
       # Light mode favicon
       {
           "rel": "icon",
           "href": "favicon-light.svg",
           "media": "(prefers-color-scheme: light)",
       },
       # Dark mode favicon
       {
           "rel": "icon",
           "href": "favicon-dark.svg",
           "media": "(prefers-color-scheme: dark)",
       },
   ]

Docker Integration
------------------

Build with Favicons
~~~~~~~~~~~~~~~~~~~

``Dockerfile``:

.. code-block:: dockerfile

   FROM python:3.11-alpine
   
   # Install dependencies
   RUN pip install sphinx sphinx-favicon pillow
   
   # Copy documentation
   COPY docs/ /docs/
   
   # Generate favicons
   COPY generate_favicons.py /
   RUN python /generate_favicons.py
   
   # Build documentation
   WORKDIR /docs
   RUN sphinx-build -b html . _build/html

Build and Run
~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     kensai-sphinx:latest \
     sphinx-build -b html /project/docs /project/docs/_build/html

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Build Docs with Favicon
   
   on: [push]
   
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Generate Favicons
           run: |
             pip install pillow
             python generate_favicons.py
         
         - name: Build Documentation
           run: |
             docker run --rm -v $(pwd):/project \
               kensai-sphinx:latest \
               sphinx-build -b html /project/docs /project/docs/_build/html
         
         - name: Deploy
           uses: peaceiris/actions-gh-pages@v3
           with:
             github_token: ${{ secrets.GITHUB_TOKEN }}
             publish_dir: ./docs/_build/html

Best Practices
--------------

1. **Provide Multiple Formats**
   
   Support ICO, PNG, and SVG

2. **Use Appropriate Sizes**
   
   Common sizes: 16x16, 32x32, 180x180, 192x192, 512x512

3. **Include Web Manifest**
   
   For PWA support

4. **Optimize File Sizes**
   
   Compress PNG files

5. **Test on Devices**
   
   Check iOS, Android, Windows

6. **Version Control Icons**
   
   Commit generated icons to git

Troubleshooting
---------------

Favicon Not Showing
~~~~~~~~~~~~~~~~~~~

**Solution:**

Clear browser cache:

.. code-block:: bash

   # Chrome DevTools: Right-click refresh > Empty Cache and Hard Reload

Check path in conf.py:

.. code-block:: python

   html_static_path = ['_static']
   favicons = [{"rel": "icon", "href": "favicon.ico"}]

Wrong Icon Displayed
~~~~~~~~~~~~~~~~~~~~

**Solution:**

Ensure file exists:

.. code-block:: bash

   ls docs/_static/favicon.ico

Check browser DevTools Network tab for 404 errors.

SVG Not Supported
~~~~~~~~~~~~~~~~~

**Solution:**

Provide PNG fallback:

.. code-block:: python

   favicons = [
       {"rel": "icon", "type": "image/svg+xml", "href": "favicon.svg"},
       {"rel": "icon", "type": "image/png", "href": "favicon-32x32.png"},
   ]

Mobile Icon Issues
~~~~~~~~~~~~~~~~~~

**Solution:**

Add apple-touch-icon:

.. code-block:: python

   favicons = [
       {
           "rel": "apple-touch-icon",
           "sizes": "180x180",
           "href": "apple-touch-icon.png",
       },
   ]

Next Steps
----------

1. Create favicon source image
2. Generate multiple sizes
3. Configure sphinx-favicon
4. Test on different devices
5. Add web app manifest

Additional Resources
--------------------

- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `RealFaviconGenerator <https://realfavicongenerator.net/>`_
- `Favicon Cheat Sheet <https://github.com/audreyfeldroy/favicon-cheat-sheet>`_
- `Web App Manifest <https://developer.mozilla.org/en-US/docs/Web/Manifest>`_
