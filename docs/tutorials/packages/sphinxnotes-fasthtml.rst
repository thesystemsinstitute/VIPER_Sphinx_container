Sphinxnotes-FastHTML Tutorial
=============================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinxnotes-fasthtml/>`_
   - `API Documentation <../../pdoc/sphinxnotes_fasthtml/index.html>`_
   - `Manual <https://github.com/sphinx-notes/fasthtml>`_
   - :doc:`Working Example <../../examples/sphinxnotes-fasthtml-example>`


.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinxnotes-fasthtml to generate fast, lightweight HTML output with minimal JavaScript and optimized performance.

What is Sphinxnotes-FastHTML?
------------------------------
sphinxnotes-fasthtml is a Sphinx extension that provides optimized HTML output:

- Minimal JavaScript footprint
- Fast page load times
- Lightweight CSS
- Progressive enhancement
- Static site optimization
- Reduced bundle size
- Better performance metrics
- Mobile-optimized output
- Accessibility improvements
- SEO-friendly markup

This is ideal for documentation that prioritizes speed, accessibility, and works well on low-bandwidth connections.

The sphinxnotes-fasthtml extension provides a streamlined approach to HTML generation with sensible defaults and rapid build times.


Installation
------------

sphinxnotes-fasthtml is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinxnotes.fasthtml; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinxnotes.fasthtml',
   ]
   
   html_theme = 'fasthtml'

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinxnotes.fasthtml']
   
   html_theme = 'fasthtml'
   
   # FastHTML configuration
   fasthtml_minify = True
   fasthtml_inline_css = True
   fasthtml_inline_scripts = False
   fasthtml_defer_scripts = True
   
   # Performance options
   fasthtml_optimize_images = True
   fasthtml_lazy_loading = True
   fasthtml_preconnect = ['https://fonts.googleapis.com']
   fasthtml_dns_prefetch = ['https://cdn.example.com']
   
   # JavaScript control
   fasthtml_disable_search_js = False
   fasthtml_minimal_js = True
   fasthtml_no_jquery = True
   
   # CSS optimization
   fasthtml_critical_css = True
   fasthtml_purge_css = True
   fasthtml_css_variables = True
   
   # Accessibility
   fasthtml_skip_links = True
   fasthtml_aria_labels = True
   fasthtml_focus_indicators = True
   
   # SEO
   fasthtml_semantic_html = True
   fasthtml_structured_data = True
   fasthtml_meta_tags = True


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Basic Setup
~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinxnotes.fasthtml',
   ]
   
   # FastHTML settings
   fasthtml_theme = 'clean'
   fasthtml_minify = True

Custom Themes
~~~~~~~~~~~~~

.. code-block:: python

   fasthtml_custom_css = '''
   body {
       font-family: Arial, sans-serif;
       line-height: 1.6;
   }
   '''

Basic Usage
-----------

Enable FastHTML Theme
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   html_theme = 'fasthtml'

Minimal JavaScript Mode
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   fasthtml_minimal_js = True
   fasthtml_no_jquery = True

Inline Critical CSS
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   fasthtml_critical_css = True
   fasthtml_inline_css = True

Lazy Load Images
~~~~~~~~~~~~~~~~

.. code-block:: python

   fasthtml_lazy_loading = True
   fasthtml_optimize_images = True

   Welcome to FastDoc
   ==================
   
   This documentation is optimized for speed and accessibility.
   
   .. toctree::
      :maxdepth: 2
      :caption: Contents:
      
      quickstart
      api/index
      guides/index
   
   Features
   --------
   
   - ⚡ Lightning-fast page loads
   - 📱 Mobile-optimized
   - ♿ Accessibility-first
   - 🔍 SEO-friendly
   - 🌐 Works offline
   
   Getting Started
   ---------------
   
   .. code-block:: bash
   
      pip install fastdoc
   
   Quick Example
   ~~~~~~~~~~~~~
   
   .. code-block:: python
   
      from fastdoc import Client
      
      client = Client()
      result = client.process()

Example 2: Mobile-First API Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``conf.py``:

.. code-block:: python

   project = 'Mobile API Docs'
   extensions = [
       'sphinxnotes.fasthtml',
       'sphinx.ext.autodoc',
       'sphinx.ext.napoleon',
   ]
   
   html_theme = 'fasthtml'
   
   # Mobile optimization
   fasthtml_viewport_meta = 'width=device-width, initial-scale=1'
   fasthtml_touch_icons = True
   fasthtml_mobile_nav = True
   
   # Performance for mobile networks
   fasthtml_lazy_loading = True
   fasthtml_optimize_images = True
   fasthtml_inline_css = True
   fasthtml_minify = True
   
   # Reduce data usage
   fasthtml_no_fonts = False  # Use system fonts
   fasthtml_minimal_js = True
   
   # Progressive Web App features
   fasthtml_service_worker = True
   fasthtml_manifest = {
       'name': 'Mobile API Docs',
       'short_name': 'API',
       'start_url': '/index.html',
       'display': 'standalone',
       'theme_color': '#007bff',
       'background_color': '#ffffff',
   }

``docs/api/client.rst``:

.. code-block:: rst

   API Client
   ==========
   
   .. autoclass:: myapi.Client
      :members:
      :undoc-members:
   
   Quick Start
   -----------
   
   .. code-block:: python
   
      from myapi import Client
      
      # Initialize client
      client = Client(api_key='your-key')
      
      # Make request
      response = client.get('/users')
   
   Authentication
   --------------
   
   .. code-block:: python
   
      client = Client(
          api_key='your-key',
          timeout=30
      )
   
   Rate Limiting
   -------------
   
   The API enforces rate limits:
   
   - **Free tier:** 100 requests/hour
   - **Pro tier:** 10,000 requests/hour
   
   Error Handling
   --------------
   
   .. code-block:: python
   
      from myapi import Client, APIError
      
      client = Client(api_key='key')
      
      try:
          response = client.get('/users')
      except APIError as e:
          print(f"Error: {e}")

Example 3: Offline-Capable Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``conf.py``:

.. code-block:: python

   project = 'Offline Docs'
   extensions = [
       'sphinxnotes.fasthtml',
   ]
   
   html_theme = 'fasthtml'
   
   # Offline support
   fasthtml_service_worker = True
   fasthtml_offline_fallback = True
   fasthtml_cache_strategy = 'cache-first'
   
   # No external dependencies
   fasthtml_no_cdn = True
   fasthtml_inline_css = True
   fasthtml_inline_scripts = True
   fasthtml_embed_images = True
   
   # Local search
   fasthtml_local_search = True
   fasthtml_search_index = 'embedded'
   
   # Manifest for PWA
   fasthtml_manifest = {
       'name': 'Offline Documentation',
       'short_name': 'Docs',
       'start_url': '/',
       'display': 'standalone',
       'orientation': 'any',
   }

Create ``_static/sw.js`` (Service Worker):

.. code-block:: javascript

   const CACHE_NAME = 'docs-v1';
   const urlsToCache = [
       '/',
       '/index.html',
       '/search.html',
       '/_static/styles.css',
       '/_static/scripts.js'
   ];
   
   self.addEventListener('install', event => {
       event.waitUntil(
           caches.open(CACHE_NAME)
               .then(cache => cache.addAll(urlsToCache))
       );
   });
   
   self.addEventListener('fetch', event => {
       event.respondWith(
           caches.match(event.request)
               .then(response => response || fetch(event.request))
       );
   });

Advanced Features
-----------------

Critical CSS Extraction
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   fasthtml_critical_css = True
   fasthtml_critical_css_rules = [
       'body', 'header', 'nav', '.content', 'h1', 'h2', 'p'
   ]
   
   # Rest of CSS is loaded asynchronously
   fasthtml_async_css = True

Resource Hints
~~~~~~~~~~~~~~

.. code-block:: python

   # Preconnect to external domains
   fasthtml_preconnect = [
       'https://fonts.googleapis.com',
       'https://api.example.com',
   ]
   
   # DNS prefetch
   fasthtml_dns_prefetch = [
       'https://cdn.jsdelivr.net',
   ]
   
   # Preload critical resources
   fasthtml_preload = [
       {'href': '/_static/logo.png', 'as': 'image'},
       {'href': '/_static/main.css', 'as': 'style'},
   ]

Image Optimization
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   fasthtml_optimize_images = True
   fasthtml_image_formats = ['webp', 'jpg']
   fasthtml_image_sizes = [320, 640, 1024, 1920]
   fasthtml_lazy_loading = True
   
   # Generate responsive images
   fasthtml_responsive_images = True

In RST:

.. code-block:: rst

   .. image:: screenshot.png
      :alt: Application screenshot
      :loading: lazy
      :sizes: (max-width: 600px) 100vw, 50vw

Custom Fonts Optimization
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Use system fonts for better performance
   fasthtml_font_stack = [
       '-apple-system',
       'BlinkMacSystemFont',
       '"Segoe UI"',
       'Roboto',
       'sans-serif'
   ]
   
   # Or load web fonts optimally
   fasthtml_web_fonts = {
       'display': 'swap',
       'families': ['Roboto:400,700']
   }

Accessibility Features
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Skip links for keyboard navigation
   fasthtml_skip_links = True
   
   # ARIA landmarks
   fasthtml_aria_labels = True
   
   # Focus indicators
   fasthtml_focus_indicators = True
   
   # Color contrast checking
   fasthtml_check_contrast = True
   fasthtml_min_contrast_ratio = 4.5

Docker Integration
------------------

Build Optimized Docs
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     kensai-sphinx:latest \
     sphinx-build -b html /project/docs /project/docs/_build/html

Analyze Performance
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Build and analyze
   docker run --rm \
     -v $(pwd):/project \
     kensai-sphinx:latest \
     sh -c "sphinx-build -b html /project/docs /project/docs/_build/html && \
            du -sh /project/docs/_build/html"

CI/CD Integration
-----------------

GitHub Actions with Performance Testing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Build and Test Performance
   
   on: [push]
   
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Build Documentation
           run: |
             docker run --rm -v $(pwd):/project \
               kensai-sphinx:latest \
               sphinx-build -b html /project/docs /project/docs/_build/html
         
         - name: Check Bundle Size
           run: |
             SIZE=$(du -sb docs/_build/html | cut -f1)
             echo "Bundle size: $SIZE bytes"
             if [ $SIZE -gt 10485760 ]; then
               echo "Bundle too large (>10MB)"
               exit 1
             fi
         
         - name: Lighthouse CI
           uses: treosh/lighthouse-ci-action@v9
           with:
             urls: |
               file://${{ github.workspace }}/docs/_build/html/index.html
             budgetPath: ./budget.json
         
         - name: Deploy
           uses: peaceiris/actions-gh-pages@v3
           with:
             github_token: ${{ secrets.GITHUB_TOKEN }}
             publish_dir: ./docs/_build/html

``budget.json``:

.. code-block:: json

   [
     {
       "path": "/*",
       "resourceSizes": [
         {
           "resourceType": "document",
           "budget": 50
         },
         {
           "resourceType": "script",
           "budget": 100
         },
         {
           "resourceType": "stylesheet",
           "budget": 50
         },
         {
           "resourceType": "image",
           "budget": 200
         }
       ],
       "resourceCounts": [
         {
           "resourceType": "third-party",
           "budget": 5
         }
       ]
     }
   ]

Best Practices
--------------

1. **Measure Performance**
   
   Use Lighthouse and WebPageTest:
   
   .. code-block:: bash
   
      lighthouse http://localhost:8000 --view

2. **Optimize Images**
   
   - Use appropriate formats (WebP, AVIF)
   - Provide responsive sizes
   - Enable lazy loading

3. **Minimize JavaScript**
   
   - Use only necessary features
   - Defer non-critical scripts
   - Inline critical scripts

4. **Critical CSS**
   
   - Inline above-the-fold CSS
   - Async load remaining styles

5. **Reduce HTTP Requests**
   
   - Combine files
   - Inline small resources
   - Use HTTP/2 when possible

6. **Enable Caching**
   
   - Set appropriate cache headers
   - Use service workers
   - Implement cache busting

Performance Metrics
-------------------

Target Metrics
~~~~~~~~~~~~~~

.. code-block:: python

   # Set performance budgets
   fasthtml_performance_budgets = {
       'FCP': 1.8,  # First Contentful Paint (seconds)
       'LCP': 2.5,  # Largest Contentful Paint
       'TTI': 3.8,  # Time to Interactive
       'TBT': 200,  # Total Blocking Time (ms)
       'CLS': 0.1,  # Cumulative Layout Shift
   }

Troubleshooting
---------------

Styles Not Loading
~~~~~~~~~~~~~~~~~~

**Solution:**

Check CSS inlining:

.. code-block:: python

   fasthtml_inline_css = True
   # OR
   fasthtml_async_css = True

JavaScript Errors
~~~~~~~~~~~~~~~~~

**Solution:**

Ensure compatibility:

.. code-block:: python

   fasthtml_es6_modules = False  # Use ES5 for compatibility
   fasthtml_polyfills = True

Large Bundle Size
~~~~~~~~~~~~~~~~~

**Solution:**

Enable purging:

.. code-block:: python

   fasthtml_purge_css = True
   fasthtml_tree_shaking = True
   fasthtml_minify = True

Slow Build Times
~~~~~~~~~~~~~~~~

**Solution:**

Disable expensive optimizations during development:

.. code-block:: python

   import os
   
   IS_PRODUCTION = os.getenv('CI') is not None
   
   fasthtml_optimize_images = IS_PRODUCTION
   fasthtml_minify = IS_PRODUCTION

Next Steps
----------

1. Configure FastHTML theme
2. Enable performance optimizations
3. Test on mobile devices
4. Run Lighthouse audits
5. Implement service workers for offline support
6. Monitor Core Web Vitals

Additional Resources
--------------------

- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `Web.dev Performance <https://web.dev/performance/>`_
- `Lighthouse Documentation <https://developers.google.com/web/tools/lighthouse>`_
- `MDN Web Performance <https://developer.mozilla.org/en-US/docs/Web/Performance>`_
