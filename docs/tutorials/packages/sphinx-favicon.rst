Sphinx-Favicon Tutorial
========================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-favicon/>`_
   - `Official Documentation <https://sphinx-favicon.readthedocs.io/>`_
   - :doc:`See Working Example <../../examples/sphinx-favicon-example>`


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

Practical Examples
------------------

Example 1: Complete Favicon Set
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create ``docs/_static/`` directory structure:

.. code-block:: text

   docs/
   └── _static/
       ├── favicon.ico
       ├── favicon-16x16.png
       ├── favicon-32x32.png
       ├── apple-touch-icon.png
       ├── android-chrome-192x192.png
       ├── android-chrome-512x512.png
       ├── favicon.svg
       └── site.webmanifest

``docs/conf.py``:

.. code-block:: python

   extensions = ['sphinx_favicon']
   
   html_static_path = ['_static']
   
   favicons = [
       # Standard favicon
       {
           "rel": "icon",
           "href": "favicon.ico",
       },
       # PNG favicons for different sizes
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
       # Apple Touch Icon
       {
           "rel": "apple-touch-icon",
           "sizes": "180x180",
           "href": "apple-touch-icon.png",
       },
       # Android Chrome icons
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
       # SVG favicon (modern browsers)
       {
           "rel": "icon",
           "type": "image/svg+xml",
           "href": "favicon.svg",
       },
       # Web app manifest
       {
           "rel": "manifest",
           "href": "site.webmanifest",
       },
   ]

Example 2: SVG Favicon with Theme Support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/_static/favicon.svg``:

.. code-block:: xml

   <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
     <style>
       /* Light mode */
       circle { fill: #2196F3; }
       text { fill: white; }
       
       /* Dark mode */
       @media (prefers-color-scheme: dark) {
         circle { fill: #64B5F6; }
         text { fill: #121212; }
       }
     </style>
     <circle cx="50" cy="50" r="45"/>
     <text x="50" y="65" font-size="50" font-weight="bold" 
           text-anchor="middle" font-family="Arial">S</text>
   </svg>

``docs/conf.py``:

.. code-block:: python

   favicons = [
       {
           "rel": "icon",
           "type": "image/svg+xml",
           "href": "favicon.svg",
       },
       # Fallback for browsers without SVG support
       {
           "rel": "icon",
           "type": "image/png",
           "sizes": "32x32",
           "href": "favicon-32x32.png",
       },
   ]

Example 3: Web App Manifest
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/_static/site.webmanifest``:

.. code-block:: json

   {
     "name": "My Documentation",
     "short_name": "MyDocs",
     "description": "Comprehensive documentation for MyProject",
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
     "theme_color": "#2196F3",
     "background_color": "#ffffff",
     "display": "standalone",
     "start_url": "/"
   }

``docs/conf.py``:

.. code-block:: python

   favicons = [
       {
           "rel": "manifest",
           "href": "site.webmanifest",
       },
       {
           "rel": "icon",
           "sizes": "192x192",
           "href": "android-chrome-192x192.png",
       },
       {
           "rel": "icon",
           "sizes": "512x512",
           "href": "android-chrome-512x512.png",
       },
   ]

Example 4: Programmatic Favicon Generation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``generate_favicons.py``:

.. code-block:: python

   """Generate favicons from source image."""
   
   from PIL import Image, ImageDraw, ImageFont
   import os
   
   def create_favicon(text, output_dir, color="#2196F3"):
       """
       Create favicon set from text.
       
       Parameters
       ----------
       text : str
           Text to display in favicon (1-2 characters)
       output_dir : str
           Output directory for favicons
       color : str
           Background color (hex)
       """
       os.makedirs(output_dir, exist_ok=True)
       
       sizes = {
           'favicon-16x16.png': 16,
           'favicon-32x32.png': 32,
           'apple-touch-icon.png': 180,
           'android-chrome-192x192.png': 192,
           'android-chrome-512x512.png': 512,
       }
       
       for filename, size in sizes.items():
           # Create image
           img = Image.new('RGB', (size, size), color)
           draw = ImageDraw.Draw(img)
           
           # Add text
           font_size = int(size * 0.6)
           try:
               font = ImageFont.truetype("arial.ttf", font_size)
           except:
               font = ImageFont.load_default()
           
           # Center text
           bbox = draw.textbbox((0, 0), text, font=font)
           text_width = bbox[2] - bbox[0]
           text_height = bbox[3] - bbox[1]
           position = ((size - text_width) // 2, (size - text_height) // 2)
           
           draw.text(position, text, fill='white', font=font)
           
           # Save
           img.save(os.path.join(output_dir, filename))
       
       # Create ICO file
       ico_img = Image.new('RGB', (32, 32), color)
       draw = ImageDraw.Draw(ico_img)
       try:
           font = ImageFont.truetype("arial.ttf", 20)
       except:
           font = ImageFont.load_default()
       bbox = draw.textbbox((0, 0), text, font=font)
       text_width = bbox[2] - bbox[0]
       text_height = bbox[3] - bbox[1]
       position = ((32 - text_width) // 2, (32 - text_height) // 2)
       draw.text(position, text, fill='white', font=font)
       ico_img.save(os.path.join(output_dir, 'favicon.ico'))
       
       print(f"Favicons generated in {output_dir}")
   
   if __name__ == '__main__':
       create_favicon('MD', 'docs/_static', '#2196F3')

Run generation:

.. code-block:: bash

   python generate_favicons.py

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
