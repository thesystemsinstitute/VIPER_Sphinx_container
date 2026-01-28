Sphinx-Favicon Example
======================

This page demonstrates the **sphinx-favicon** extension for adding favicon support to Sphinx documentation with multiple formats and sizes.

.. contents:: Contents
   :local:
   :depth: 2


Basic Favicon
-------------

Single ICO File
~~~~~~~~~~~~~~~

Simplest configuration with one .ico file:

.. code-block:: python

   # conf.py
   favicons = [
       "favicon.ico",
   ]

Single PNG File
~~~~~~~~~~~~~~~

Modern PNG favicon:

.. code-block:: python

   favicons = [
       "favicon.png",
   ]

Multiple Sizes
--------------

Standard Sizes
~~~~~~~~~~~~~~

Provide multiple sizes for different contexts:

.. code-block:: python

   favicons = [
       {
           "rel": "icon",
           "sizes": "16x16",
           "href": "favicon-16x16.png",
       },
       {
           "rel": "icon",
           "sizes": "32x32",
           "href": "favicon-32x32.png",
       },
       {
           "rel": "icon",
           "sizes": "48x48",
           "href": "favicon-48x48.png",
       },
   ]

High-Resolution Icons
~~~~~~~~~~~~~~~~~~~~~

Support for retina displays:

.. code-block:: python

   favicons = [
       {
           "rel": "icon",
           "sizes": "192x192",
           "href": "favicon-192x192.png",
       },
       {
           "rel": "icon",
           "sizes": "512x512",
           "href": "favicon-512x512.png",
       },
   ]

Platform-Specific Icons
-----------------------

Apple Touch Icons
~~~~~~~~~~~~~~~~~

iOS home screen icons:

.. code-block:: python

   favicons = [
       {
           "rel": "apple-touch-icon",
           "sizes": "180x180",
           "href": "apple-touch-icon.png",
       },
       {
           "rel": "apple-touch-icon",
           "sizes": "152x152",
           "href": "apple-touch-icon-152x152.png",
       },
       {
           "rel": "apple-touch-icon",
           "sizes": "120x120",
           "href": "apple-touch-icon-120x120.png",
       },
   ]

Android Chrome
~~~~~~~~~~~~~~

Android home screen icons:

.. code-block:: python

   favicons = [
       {
           "rel": "icon",
           "type": "image/png",
           "sizes": "192x192",
           "href": "android-chrome-192x192.png",
       },
       {
           "rel": "icon",
           "type": "image/png",
           "sizes": "512x512",
           "href": "android-chrome-512x512.png",
       },
   ]

Microsoft Tiles
~~~~~~~~~~~~~~~

Windows tile icons:

.. code-block:: python

   favicons = [
       {
           "rel": "mask-icon",
           "href": "safari-pinned-tab.svg",
           "color": "#5bbad5",
       },
       {
           "rel": "msapplication-TileImage",
           "href": "mstile-150x150.png",
       },
   ]

Advanced Configuration
----------------------

Complete Setup
~~~~~~~~~~~~~~

Full favicon configuration with all platforms:

.. code-block:: python

   favicons = [
       # Standard favicons
       {
           "rel": "icon",
           "type": "image/x-icon",
           "href": "favicon.ico",
       },
       {
           "rel": "icon",
           "type": "image/png",
           "sizes": "16x16",
           "href": "favicon-16x16.png",
       },
       {
           "rel": "icon",
           "type": "image/png",
           "sizes": "32x32",
           "href": "favicon-32x32.png",
       },
       
       # Apple
       {
           "rel": "apple-touch-icon",
           "sizes": "180x180",
           "href": "apple-touch-icon.png",
       },
       
       # Android
       {
           "rel": "manifest",
           "href": "site.webmanifest",
       },
       
       # Safari
       {
           "rel": "mask-icon",
           "href": "safari-pinned-tab.svg",
           "color": "#5bbad5",
       },
       
       # MS
       {
           "name": "msapplication-TileColor",
           "content": "#da532c",
       },
       {
           "name": "theme-color",
           "content": "#ffffff",
       },
   ]

SVG Favicons
~~~~~~~~~~~~

Modern SVG favicon support:

.. code-block:: python

   favicons = [
       {
           "rel": "icon",
           "type": "image/svg+xml",
           "href": "favicon.svg",
       },
       # Fallback for older browsers
       {
           "rel": "icon",
           "type": "image/png",
           "href": "favicon.png",
       },
   ]

Dynamic Favicons
~~~~~~~~~~~~~~~~

Different favicons for different sections:

.. code-block:: python

   # Use in conf.py or per-page configuration
   favicons = [
       {
           "rel": "icon",
           "href": "favicon-api.png",
           "static-only": True,
       },
   ]

File Organization
-----------------

Directory Structure
~~~~~~~~~~~~~~~~~~~

Recommended file organization:

.. code-block:: text

   docs/
   ├── _static/
   │   ├── favicons/
   │   │   ├── favicon.ico
   │   │   ├── favicon-16x16.png
   │   │   ├── favicon-32x32.png
   │   │   ├── favicon.svg
   │   │   ├── apple-touch-icon.png
   │   │   ├── android-chrome-192x192.png
   │   │   ├── android-chrome-512x512.png
   │   │   ├── safari-pinned-tab.svg
   │   │   └── site.webmanifest
   │   └── ...
   └── conf.py

Path Configuration
~~~~~~~~~~~~~~~~~~

Using subdirectory for favicons:

.. code-block:: python

   favicons = [
       {
           "rel": "icon",
           "href": "favicons/favicon.ico",
       },
       {
           "rel": "icon",
           "sizes": "16x16",
           "href": "favicons/favicon-16x16.png",
       },
   ]

Manifest File
-------------

Web App Manifest
~~~~~~~~~~~~~~~~

Create ``site.webmanifest``:

.. code-block:: json

   {
       "name": "My Documentation",
       "short_name": "MyDocs",
       "icons": [
           {
               "src": "/android-chrome-192x192.png",
               "sizes": "192x192",
               "type": "image/png"
           },
           {
               "src": "/android-chrome-512x512.png",
               "sizes": "512x512",
               "type": "image/png"
           }
       ],
       "theme_color": "#ffffff",
       "background_color": "#ffffff",
       "display": "standalone"
   }

Browser Config
~~~~~~~~~~~~~~

Create ``browserconfig.xml`` for IE/Edge:

.. code-block:: xml

   <?xml version="1.0" encoding="utf-8"?>
   <browserconfig>
       <msapplication>
           <tile>
               <square150x150logo src="/mstile-150x150.png"/>
               <TileColor>#da532c</TileColor>
           </tile>
       </msapplication>
   </browserconfig>

Practical Examples
------------------

Simple Project
~~~~~~~~~~~~~~

Minimal favicon setup:

.. code-block:: python

   # conf.py
   extensions = [
       'sphinx_favicon',
   ]
   
   favicons = [
       "favicon.ico",
   ]

Multi-Platform Support
~~~~~~~~~~~~~~~~~~~~~~

Cross-platform favicon configuration:

.. code-block:: python

   extensions = [
       'sphinx_favicon',
   ]
   
   favicons = [
       # ICO for legacy browsers
       "favicon.ico",
       
       # PNG for modern browsers
       {"rel": "icon", "sizes": "32x32", "href": "favicon-32x32.png"},
       
       # Apple devices
       {"rel": "apple-touch-icon", "href": "apple-touch-icon.png"},
       
       # Android devices
       {"rel": "manifest", "href": "site.webmanifest"},
   ]

Theme Integration
~~~~~~~~~~~~~~~~~

Matching theme colors:

.. code-block:: python

   # conf.py
   html_theme = "sphinx_rtd_theme"
   
   favicons = [
       {
           "rel": "icon",
           "sizes": "32x32",
           "href": "favicon-32x32.png",
       },
       {
           "name": "theme-color",
           "content": "#343131",  # RTD theme color
       },
   ]

Testing Favicons
----------------

Browser Testing
~~~~~~~~~~~~~~~

Check favicon display in different browsers:

1. Chrome: DevTools → Application → Manifest
2. Firefox: Inspector → Network → Filter images
3. Safari: Develop → Show Page Resources
4. Edge: F12 Tools → Network

Online Tools
~~~~~~~~~~~~

Use favicon generators and validators:

- https://realfavicongenerator.net/
- https://www.favicon-generator.org/
- https://favicon.io/

Common Issues
-------------

Cache Problems
~~~~~~~~~~~~~~

Force favicon refresh:

.. code-block:: python

   # Add version parameter
   favicons = [
       {
           "rel": "icon",
           "href": "favicon.png?v=2",
       },
   ]

Path Issues
~~~~~~~~~~~

Ensure correct static paths:

.. code-block:: python

   # conf.py
   html_static_path = ['_static']
   
   favicons = [
       "favicon.ico",  # Located in _static/favicon.ico
   ]

See Also
--------

- :doc:`../tutorials/packages/sphinx-favicon` - Complete tutorial
- GitHub repository: https://github.com/tcmetzger/sphinx-favicon
- RealFaviconGenerator: https://realfavicongenerator.net/
