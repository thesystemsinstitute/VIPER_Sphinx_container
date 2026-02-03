Sphinx-Notfound-Page Tutorial
==============================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-notfound-page/>`_
   - `API Documentation <../../pdoc/sphinx_notfound_page/index.html>`_
   - `Manual <https://sphinx-notfound-page.readthedocs.io/>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinx-notfound-page to create custom 404 error pages for your Sphinx documentation.

What is Sphinx-Notfound-Page?
------------------------------
sphinx-notfound-page is a Sphinx extension that provides:

- Custom 404 error pages
- Branded error pages
- Search suggestions
- Navigation on 404 pages
- Customizable content
- Multiple theme support
- URL suggestions
- Link checking hints
- Professional error handling
- GitHub Pages compatible

This creates a user-friendly experience when visitors land on non-existent documentation pages.

The sphinx-notfound-page extension generates a custom 404 error page for your Sphinx documentation that matches your theme and provides helpful navigation options.


Installation
------------

sphinx-notfound-page is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm viper-sphinx:latest python -c "import notfound.extension; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'notfound.extension',
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['notfound.extension']
   
   # 404 page configuration
   notfound_pagename = '404'
   notfound_template = '404.html'
   
   # Context for template
   notfound_context = {
       'title': 'Page Not Found',
       'body': '<h1>404 - Page Not Found</h1><p>Sorry, the page you are looking for does not exist.</p>',
   }
   
   # URLs to exclude from 404 handling
   notfound_urls_prefix = '/en/latest/'
   
   # Default 404 page for all versions
   notfound_default_language = 'en'
   notfound_default_version = 'latest'

Basic Usage
-----------

Create Custom 404 Page
~~~~~~~~~~~~~~~~~~~~~~~

Create ``docs/404.rst``:

.. code-block:: rst

   Page Not Found
   ==============
   
   Oops! The page you're looking for doesn't exist.
   
   Here are some helpful links:
   
   * :doc:`index` - Home page
   * :doc:`installation` - Installation guide
   * :doc:`usage` - Usage documentation
   * :ref:`search` - Search the documentation
   
   Common Issues
   -------------
   
   * **Outdated link?** We may have reorganized our documentation.
   * **Typo in URL?** Check the address carefully.
   * **Old bookmark?** Update your bookmarks to the latest version.
   
   Need Help?
   ----------
   
   * Check our `GitHub Issues <https://github.com/user/project/issues>`_
   * Join our `Community Forum <https://forum.example.com>`_
   * Email us at support@example.com

Build and Test
~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     viper-sphinx:latest \
     sphinx-build -b html /project/docs /project/docs/_build/html

The 404 page is automatically created as ``404.html``.

.. code-block:: rst

    404 - Page Not Found
    ====================
   
    .. image:: _static/404-illustration.svg
        :alt: Page not found illustration
        :width: 400px
        :align: center
   
    The page you're looking for doesn't exist or has been moved.
   
    Quick Links
    -----------
   
    .. grid:: 2
        :gutter: 3
      
        .. grid-item-card:: 🏠 Home
            :link: index
            :link-type: doc
         
            Return to the home page
      
        .. grid-item-card:: 📖 Documentation
            :link: getting-started
            :link-type: doc
         
            Start with our guides
      
        .. grid-item-card:: 🔍 Search
            :link: search
            :link-type: ref
         
            Search the documentation
      
        .. grid-item-card:: 📋 API Reference
            :link: api/index
            :link-type: doc
         
            Browse the API docs
   
    What Happened?
    --------------
   
    There are a few reasons you might see this page:
   
    * The page has been moved or deleted
    * You followed an outdated link
    * There's a typo in the URL
    * You're looking for documentation from an older version
   
    What to Do
    ----------
   
    1. **Check the URL** - Make sure the address is correct
    2. **Use Search** - Try :ref:`searching <search>` for what you need
    3. **Browse Topics** - Start from the :doc:`table of contents <index>`
    4. **Report Issue** - If you think this is a broken link, `report it <https://github.com/user/project/issues>`_
   
    Popular Pages
    -------------
   
    * :doc:`installation` - How to install
    * :doc:`quickstart` - Quick start guide
    * :doc:`tutorials/index` - Tutorials
    * :doc:`api/index` - API reference
    * :doc:`faq` - Frequently asked questions
   
    Need Help?
    ----------
   
    If you can't find what you're looking for:
   
    .. list-table::
        :widths: 20 80
      
        * - 💬 Community
          - Join our `Discord server <https://discord.gg/example>`_
        * - 🐛 Bug Reports
          - `Open an issue on GitHub <https://github.com/user/project/issues>`_
        * - 📧 Email
          - Contact us at support@example.com
        * - 📚 Stack Overflow
          - Tag your questions with ``myproject``

Example 2: Simple 404 with Custom Styling
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/404.rst``:

.. code-block:: rst

   .. raw:: html
      
      <div class="not-found-container">
        <h1 class="not-found-title">404</h1>
        <p class="not-found-message">Page Not Found</p>
      </div>
   
   The page you requested could not be found.
   
   :doc:`← Back to Home <index>`

``docs/_static/custom-404.css``:

.. code-block:: css

   .not-found-container {
       text-align: center;
       padding: 60px 20px;
   }
   
   .not-found-title {
       font-size: 120px;
       color: #e74c3c;
       margin: 0;
       font-weight: bold;
   }
   
   .not-found-message {
       font-size: 24px;
       color: #666;
       margin-top: 20px;
   }

``docs/conf.py``:

.. code-block:: python

   html_css_files = ['custom-404.css']

Example 3: Dynamic 404 with Suggestions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/_templates/404.html``:

.. code-block:: html

   {% extends "!page.html" %}
   
   {% block body %}
   <div class="notfound">
     <h1>404 - Page Not Found</h1>
     
     <p>The page <code id="missing-url"></code> does not exist.</p>
     
     <h2>Did you mean?</h2>
     <ul id="suggestions"></ul>
     
     <h2>Popular Pages</h2>
     <ul>
       <li><a href="{{ pathto('index') }}">Home</a></li>
       <li><a href="{{ pathto('installation') }}">Installation</a></li>
       <li><a href="{{ pathto('api/index') }}">API Reference</a></li>
     </ul>
   </div>
   
   <script>
     // Show the requested URL
     document.getElementById('missing-url').textContent = window.location.pathname;
     
     // Simple suggestion logic
     const suggestions = document.getElementById('suggestions');
     const path = window.location.pathname;
     
     // Map common mistakes to correct pages
     const corrections = {
       '/install': '/installation.html',
       '/api': '/api/index.html',
       '/docs': '/index.html',
     };
     
     Object.keys(corrections).forEach(wrong => {
       if (path.includes(wrong)) {
         const li = document.createElement('li');
         const a = document.createElement('a');
         a.href = corrections[wrong];
         a.textContent = 'Try ' + corrections[wrong];
         li.appendChild(a);
         suggestions.appendChild(li);
       }
     });
   </script>
   {% endblock %}

``docs/conf.py``:

.. code-block:: python

   notfound_template = '404.html'

Example 4: Multilingual 404
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/404.rst``:

.. code-block:: rst

   Page Not Found / Página no encontrada
   ======================================
   
   .. container:: lang-en
      
      **English:**
      
      The page you're looking for doesn't exist.
      
      * :doc:`Home <index>`
      * :ref:`Search <search>`
   
   .. container:: lang-es
      
      **Español:**
      
      La página que buscas no existe.
      
      * :doc:`Inicio <index>`
      * :ref:`Buscar <search>`

Advanced Features
-----------------

Custom Template Variables
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   notfound_context = {
       'title': 'Page Not Found',
       'body': 'Custom 404 message',
       'project_name': project,
       'support_email': 'support@example.com',
   }

URL Prefix Handling
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # For Read the Docs or versioned docs
   notfound_urls_prefix = '/en/latest/'
   notfound_default_language = 'en'
   notfound_default_version = 'latest'

Custom Page Name
~~~~~~~~~~~~~~~~

.. code-block:: python

   # Use different filename
   notfound_pagename = 'not-found'
   # Results in not-found.html

Read the Docs Integration
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   
   # Detect Read the Docs environment
   import os
   
   on_rtd = os.environ.get('READTHEDOCS') == 'True'
   
   if on_rtd:
       notfound_urls_prefix = '/en/latest/'

Docker Integration
------------------

Build with 404 Page
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     viper-sphinx:latest \
     sphinx-build -b html /project/docs /project/docs/_build/html

Test 404 Page Locally
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Serve built docs
   docker run --rm \
     -v $(pwd):/project \
     -p 8000:8000 \
     viper-sphinx:latest \
     sh -c "cd /project/docs/_build/html && python -m http.server 8000"
   
   # Visit http://localhost:8000/nonexistent to see 404 page

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Build Docs with 404 Page
   
   on: [push]
   
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Build Documentation
           run: |
             docker run --rm -v $(pwd):/project \
               viper-sphinx:latest \
               sphinx-build -b html /project/docs /project/docs/_build/html
         
         - name: Verify 404 Page
           run: |
             if [ ! -f docs/_build/html/404.html ]; then
               echo "404.html not found!"
               exit 1
             fi
         
         - name: Deploy
           uses: peaceiris/actions-gh-pages@v3
           with:
             github_token: ${{ secrets.GITHUB_TOKEN }}
             publish_dir: ./docs/_build/html

GitHub Pages Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The 404.html file is automatically used by GitHub Pages for missing pages.

Best Practices
--------------

1. **Keep It Simple**
   
   Clear message and navigation

2. **Provide Navigation**
   
   Links to key pages

3. **Include Search**
   
   Help users find content

4. **Be Helpful**
   
   Suggest common pages

5. **Match Theme**
   
   Consistent styling

6. **Test Thoroughly**
   
   Verify 404 page works

Troubleshooting
---------------

404 Page Not Created
~~~~~~~~~~~~~~~~~~~~

**Solution:**

Check extension is loaded:

.. code-block:: python

   extensions = ['notfound.extension']

Verify build output for 404.html.

Wrong Template Used
~~~~~~~~~~~~~~~~~~~

**Solution:**

Specify template:

.. code-block:: python

   notfound_template = '404.html'

Links Broken on 404 Page
~~~~~~~~~~~~~~~~~~~~~~~~~

**Solution:**

Use absolute URLs or pathto():

.. code-block:: html

   <a href="{{ pathto('index') }}">Home</a>

Styling Not Applied
~~~~~~~~~~~~~~~~~~~

**Solution:**

Ensure CSS is loaded:

.. code-block:: python

   html_css_files = ['custom-404.css']

Read the Docs 404 Issues
~~~~~~~~~~~~~~~~~~~~~~~~~

**Solution:**

Configure URL prefix:

.. code-block:: python

   notfound_urls_prefix = '/en/latest/'

Next Steps
----------

1. Create 404.rst page
2. Customize content
3. Add navigation links
4. Style the page
5. Test on hosting platform


Practical Examples
------------------

Basic Configuration
-------------------

Setup
~~~~~

.. code-block:: python

   # conf.py
   extensions = [
       'notfound.extension',
   ]

Default Behavior
~~~~~~~~~~~~~~~~

The extension automatically creates a 404 page using your theme with:

- Site title
- Search box
- Navigation links
- Return to homepage link

Custom Content
--------------

Custom Message
~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   notfound_context = {
       'title': 'Page Not Found',
       'body': '''
           <h1>404 - Page Not Found</h1>
           <p>Sorry, the page you're looking for doesn't exist.</p>
           <p>Try using the search box or navigation menu.</p>
       ''',
   }

Template Variables
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   notfound_context = {
       'title': 'Not Found',
       'body': '''
           <h1>Oops!</h1>
           <p>We couldn't find: {{ pagename }}</p>
           <p><a href="{{ pathto(master_doc) }}">Return home</a></p>
       ''',
   }

URLs Configuration
------------------

URL Prefix
~~~~~~~~~~

For sites hosted in subdirectories:

.. code-block:: python

   # conf.py
   notfound_urls_prefix = '/docs/'

This ensures links work correctly when docs are at ``example.com/docs/``.

External URLs
~~~~~~~~~~~~~

.. code-block:: python

   # For docs hosted on different domain
   notfound_urls_prefix = 'https://docs.example.com/'

No Prefix
~~~~~~~~~

.. code-block:: python

   # For root-level hosting
   notfound_urls_prefix = '/'

Template Customization
----------------------

Custom Template
~~~~~~~~~~~~~~~

Create ``_templates/404.html``:

.. code-block:: html

   {% extends "!404.html" %}
   
   {% block body %}
   <div class="notfound-page">
       <h1>404 - Page Not Found</h1>
       
       <p class="error-message">
           The page <code>{{ pagename }}</code> could not be found.
       </p>
       
       <div class="suggestions">
           <h2>What would you like to do?</h2>
           <ul>
               <li><a href="{{ pathto(master_doc) }}">Go to homepage</a></li>
               <li><a href="{{ pathto('search') }}">Search documentation</a></li>
               <li><a href="{{ pathto('genindex') }}">View index</a></li>
           </ul>
       </div>
   </div>
   {% endblock %}

Specify Template
~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   notfound_template = '404.html'
   
   templates_path = ['_templates']

Advanced Templates
------------------

With Search
~~~~~~~~~~~

.. code-block:: html

   {% extends "!404.html" %}
   
   {% block body %}
   <div class="notfound-container">
       <h1>Page Not Found</h1>
       
       <p>Try searching for what you need:</p>
       
       {{ search }}
       
       <p>Or browse these sections:</p>
       <ul>
           <li><a href="{{ pathto('getting-started') }}">Getting Started</a></li>
           <li><a href="{{ pathto('api/index') }}">API Reference</a></li>
           <li><a href="{{ pathto('tutorials/index') }}">Tutorials</a></li>
       </ul>
   </div>
   {% endblock %}

With Theme Integration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: html

   {% extends "!404.html" %}
   
   {% block extrahead %}
   {{ super() }}
   <style>
       .notfound-page {
           max-width: 800px;
           margin: 50px auto;
           padding: 20px;
           text-align: center;
       }
       .error-code {
           font-size: 120px;
           color: #e74c3c;
           font-weight: bold;
       }
       .suggestions {
           margin-top: 30px;
       }
       .search-box {
           margin: 20px 0;
       }
   </style>
   {% endblock %}
   
   {% block body %}
   <div class="notfound-page">
       <div class="error-code">404</div>
       <h1>Oops! Page Not Found</h1>
       
       <div class="search-box">
           {{ search }}
       </div>
       
       <div class="suggestions">
           <a href="{{ pathto(master_doc) }}" class="btn btn-primary">
               Return to Homepage
           </a>
       </div>
   </div>
   {% endblock %}

Hosting Platforms
-----------------

Read the Docs
~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   # Read the Docs hosts at /en/latest/ by default
   import os
   
   if os.environ.get('READTHEDOCS') == 'True':
       notfound_urls_prefix = '/en/latest/'

GitHub Pages
~~~~~~~~~~~~

.. code-block:: python

   # For https://username.github.io/project/
   html_baseurl = 'https://username.github.io/project/'
   notfound_urls_prefix = '/project/'

GitLab Pages
~~~~~~~~~~~~

.. code-block:: python

   # For https://username.gitlab.io/project/
   notfound_urls_prefix = '/project/'

Custom Server
~~~~~~~~~~~~~

Configure web server to serve 404.html:

**Apache** (``.htaccess``):

.. code-block:: apache

   ErrorDocument 404 /404.html

**Nginx**:

.. code-block:: nginx

   error_page 404 /404.html;
   location = /404.html {
       internal;
   }

Practical Examples
------------------

Simple 404
~~~~~~~~~~

.. code-block:: python

   # conf.py
   extensions = ['notfound.extension']
   
   notfound_context = {
       'body': '''
           <h1>Page Not Found</h1>
           <p>The requested page could not be found.</p>
           <p><a href="/">Return to homepage</a></p>
       ''',
   }

Branded 404
~~~~~~~~~~~

.. code-block:: python

   notfound_context = {
       'title': 'MyProject - 404',
       'body': '''
           <div style="text-align: center;">
               <img src="_static/logo.png" alt="MyProject" width="200">
               <h1>Page Not Found</h1>
               <p>We couldn't find what you're looking for.</p>
               <p><a href="{{ pathto(master_doc) }}">Go Home</a></p>
           </div>
       ''',
   }

Multi-Language Support
----------------------

Language Detection
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   language = 'en'
   locale_dirs = ['locale/']
   
   notfound_context = {
       'body': '''
           <h1>{{ _('Page Not Found') }}</h1>
           <p>{{ _('The page you requested does not exist.') }}</p>
           <p><a href="{{ pathto(master_doc) }}">{{ _('Return home') }}</a></p>
       ''',
   }

Multiple Languages
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # English version
   if language == 'en':
       notfound_urls_prefix = '/en/'
   # Spanish version
   elif language == 'es':
       notfound_urls_prefix = '/es/'

Testing
-------

Local Testing
~~~~~~~~~~~~~

.. code-block:: bash

   # Build docs
   sphinx-build docs docs/_build/html
   
   # Serve locally
   python -m http.server -d docs/_build/html 8000
   
   # Test 404 page
   # Visit: http://localhost:8000/nonexistent

Check Generated Page
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Verify 404.html exists
   ls docs/_build/html/404.html
   
   # View content
   cat docs/_build/html/404.html

Integration Testing
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # test_404.py
   import requests
   
   def test_404_page():
       """Test custom 404 page."""
       response = requests.get('http://localhost:8000/nonexistent')
       assert response.status_code == 404
       assert 'Page Not Found' in response.text
       assert 'Return home' in response.text

Analytics Integration
---------------------

Google Analytics
~~~~~~~~~~~~~~~~

.. code-block:: html

   {% extends "!404.html" %}
   
   {% block extrahead %}
   {{ super() }}
   <!-- Google Analytics -->
   <script>
       // Track 404 errors
       if (typeof ga !== 'undefined') {
           ga('send', 'event', 'Error', '404', document.location.pathname);
       }
   </script>
   {% endblock %}

Custom Tracking
~~~~~~~~~~~~~~~

.. code-block:: html

   {% block extrahead %}
   {{ super() }}
   <script>
       // Log 404 to your service
       fetch('/api/log-404', {
           method: 'POST',
           body: JSON.stringify({
               path: window.location.pathname,
               referrer: document.referrer,
               timestamp: new Date().toISOString()
           })
       });
   </script>
   {% endblock %}

Best Practices
--------------

Content Guidelines
~~~~~~~~~~~~~~~~~~

1. Keep the message friendly and helpful
2. Provide clear navigation options
3. Include search functionality
4. Match your site's branding
5. Show suggested pages

Technical Tips
~~~~~~~~~~~~~~

1. Test on all hosting platforms
2. Verify URL prefixes are correct
3. Ensure assets (CSS/JS) load
4. Check mobile responsiveness
5. Monitor 404 occurrences

Accessibility
~~~~~~~~~~~~~

.. code-block:: html

   <div role="alert" aria-live="polite">
       <h1>Page Not Found</h1>
       <p>
           The page you requested at
           <code aria-label="Requested URL">{{ pagename }}</code>
           could not be found.
       </p>
   </div>

Troubleshooting
---------------

404 Page Not Generated
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Ensure extension is loaded
   extensions = ['notfound.extension']
   
   # Check build output
   # Should see: "writing additional pages... 404"

Links Don't Work
~~~~~~~~~~~~~~~~

.. code-block:: python

   # Check URL prefix
   notfound_urls_prefix = '/correct/path/'
   
   # Verify in 404.html
   # Links should have correct base path

Theme Issues
~~~~~~~~~~~~

.. code-block:: python

   # Ensure theme compatibility
   html_theme = 'sphinx_rtd_theme'
   
   # May need custom template for some themes
   notfound_template = 'custom_404.html'


Practical Examples
------------------

Basic Configuration
-------------------

Setup
~~~~~

.. code-block:: python

   # conf.py
   extensions = [
       'notfound.extension',
   ]

Default Behavior
~~~~~~~~~~~~~~~~

The extension automatically creates a 404 page using your theme with:

- Site title
- Search box
- Navigation links
- Return to homepage link

Custom Content
--------------

Custom Message
~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   notfound_context = {
       'title': 'Page Not Found',
       'body': '''
           <h1>404 - Page Not Found</h1>
           <p>Sorry, the page you're looking for doesn't exist.</p>
           <p>Try using the search box or navigation menu.</p>
       ''',
   }

Template Variables
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   notfound_context = {
       'title': 'Not Found',
       'body': '''
           <h1>Oops!</h1>
           <p>We couldn't find: {{ pagename }}</p>
           <p><a href="{{ pathto(master_doc) }}">Return home</a></p>
       ''',
   }

URLs Configuration
------------------

URL Prefix
~~~~~~~~~~

For sites hosted in subdirectories:

.. code-block:: python

   # conf.py
   notfound_urls_prefix = '/docs/'

This ensures links work correctly when docs are at ``example.com/docs/``.

External URLs
~~~~~~~~~~~~~

.. code-block:: python

   # For docs hosted on different domain
   notfound_urls_prefix = 'https://docs.example.com/'

No Prefix
~~~~~~~~~

.. code-block:: python

   # For root-level hosting
   notfound_urls_prefix = '/'

Template Customization
----------------------

Custom Template
~~~~~~~~~~~~~~~

Create ``_templates/404.html``:

.. code-block:: html

   {% extends "!404.html" %}
   
   {% block body %}
   <div class="notfound-page">
       <h1>404 - Page Not Found</h1>
       
       <p class="error-message">
           The page <code>{{ pagename }}</code> could not be found.
       </p>
       
       <div class="suggestions">
           <h2>What would you like to do?</h2>
           <ul>
               <li><a href="{{ pathto(master_doc) }}">Go to homepage</a></li>
               <li><a href="{{ pathto('search') }}">Search documentation</a></li>
               <li><a href="{{ pathto('genindex') }}">View index</a></li>
           </ul>
       </div>
   </div>
   {% endblock %}

Specify Template
~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   notfound_template = '404.html'
   
   templates_path = ['_templates']

Advanced Templates
------------------

With Search
~~~~~~~~~~~

.. code-block:: html

   {% extends "!404.html" %}
   
   {% block body %}
   <div class="notfound-container">
       <h1>Page Not Found</h1>
       
       <p>Try searching for what you need:</p>
       
       {{ search }}
       
       <p>Or browse these sections:</p>
       <ul>
           <li><a href="{{ pathto('getting-started') }}">Getting Started</a></li>
           <li><a href="{{ pathto('api/index') }}">API Reference</a></li>
           <li><a href="{{ pathto('tutorials/index') }}">Tutorials</a></li>
       </ul>
   </div>
   {% endblock %}

With Theme Integration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: html

   {% extends "!404.html" %}
   
   {% block extrahead %}
   {{ super() }}
   <style>
       .notfound-page {
           max-width: 800px;
           margin: 50px auto;
           padding: 20px;
           text-align: center;
       }
       .error-code {
           font-size: 120px;
           color: #e74c3c;
           font-weight: bold;
       }
       .suggestions {
           margin-top: 30px;
       }
       .search-box {
           margin: 20px 0;
       }
   </style>
   {% endblock %}
   
   {% block body %}
   <div class="notfound-page">
       <div class="error-code">404</div>
       <h1>Oops! Page Not Found</h1>
       
       <div class="search-box">
           {{ search }}
       </div>
       
       <div class="suggestions">
           <a href="{{ pathto(master_doc) }}" class="btn btn-primary">
               Return to Homepage
           </a>
       </div>
   </div>
   {% endblock %}

Hosting Platforms
-----------------

Read the Docs
~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   # Read the Docs hosts at /en/latest/ by default
   import os
   
   if os.environ.get('READTHEDOCS') == 'True':
       notfound_urls_prefix = '/en/latest/'

GitHub Pages
~~~~~~~~~~~~

.. code-block:: python

   # For https://username.github.io/project/
   html_baseurl = 'https://username.github.io/project/'
   notfound_urls_prefix = '/project/'

GitLab Pages
~~~~~~~~~~~~

.. code-block:: python

   # For https://username.gitlab.io/project/
   notfound_urls_prefix = '/project/'

Custom Server
~~~~~~~~~~~~~

Configure web server to serve 404.html:

**Apache** (``.htaccess``):

.. code-block:: apache

   ErrorDocument 404 /404.html

**Nginx**:

.. code-block:: nginx

   error_page 404 /404.html;
   location = /404.html {
       internal;
   }

Practical Examples
------------------

Simple 404
~~~~~~~~~~

.. code-block:: python

   # conf.py
   extensions = ['notfound.extension']
   
   notfound_context = {
       'body': '''
           <h1>Page Not Found</h1>
           <p>The requested page could not be found.</p>
           <p><a href="/">Return to homepage</a></p>
       ''',
   }

Branded 404
~~~~~~~~~~~

.. code-block:: python

   notfound_context = {
       'title': 'MyProject - 404',
       'body': '''
           <div style="text-align: center;">
               <img src="_static/logo.png" alt="MyProject" width="200">
               <h1>Page Not Found</h1>
               <p>We couldn't find what you're looking for.</p>
               <p><a href="{{ pathto(master_doc) }}">Go Home</a></p>
           </div>
       ''',
   }

Multi-Language Support
----------------------

Language Detection
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   language = 'en'
   locale_dirs = ['locale/']
   
   notfound_context = {
       'body': '''
           <h1>{{ _('Page Not Found') }}</h1>
           <p>{{ _('The page you requested does not exist.') }}</p>
           <p><a href="{{ pathto(master_doc) }}">{{ _('Return home') }}</a></p>
       ''',
   }

Multiple Languages
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # English version
   if language == 'en':
       notfound_urls_prefix = '/en/'
   # Spanish version
   elif language == 'es':
       notfound_urls_prefix = '/es/'

Testing
-------

Local Testing
~~~~~~~~~~~~~

.. code-block:: bash

   # Build docs
   sphinx-build docs docs/_build/html
   
   # Serve locally
   python -m http.server -d docs/_build/html 8000
   
   # Test 404 page
   # Visit: http://localhost:8000/nonexistent

Check Generated Page
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Verify 404.html exists
   ls docs/_build/html/404.html
   
   # View content
   cat docs/_build/html/404.html

Integration Testing
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # test_404.py
   import requests
   
   def test_404_page():
       """Test custom 404 page."""
       response = requests.get('http://localhost:8000/nonexistent')
       assert response.status_code == 404
       assert 'Page Not Found' in response.text
       assert 'Return home' in response.text

Analytics Integration
---------------------

Google Analytics
~~~~~~~~~~~~~~~~

.. code-block:: html

   {% extends "!404.html" %}
   
   {% block extrahead %}
   {{ super() }}
   <!-- Google Analytics -->
   <script>
       // Track 404 errors
       if (typeof ga !== 'undefined') {
           ga('send', 'event', 'Error', '404', document.location.pathname);
       }
   </script>
   {% endblock %}

Custom Tracking
~~~~~~~~~~~~~~~

.. code-block:: html

   {% block extrahead %}
   {{ super() }}
   <script>
       // Log 404 to your service
       fetch('/api/log-404', {
           method: 'POST',
           body: JSON.stringify({
               path: window.location.pathname,
               referrer: document.referrer,
               timestamp: new Date().toISOString()
           })
       });
   </script>
   {% endblock %}

Best Practices
--------------

Content Guidelines
~~~~~~~~~~~~~~~~~~

1. Keep the message friendly and helpful
2. Provide clear navigation options
3. Include search functionality
4. Match your site's branding
5. Show suggested pages

Technical Tips
~~~~~~~~~~~~~~

1. Test on all hosting platforms
2. Verify URL prefixes are correct
3. Ensure assets (CSS/JS) load
4. Check mobile responsiveness
5. Monitor 404 occurrences

Accessibility
~~~~~~~~~~~~~

.. code-block:: html

   <div role="alert" aria-live="polite">
       <h1>Page Not Found</h1>
       <p>
           The page you requested at
           <code aria-label="Requested URL">{{ pagename }}</code>
           could not be found.
       </p>
   </div>

Troubleshooting
---------------

404 Page Not Generated
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Ensure extension is loaded
   extensions = ['notfound.extension']
   
   # Check build output
   # Should see: "writing additional pages... 404"

Links Don't Work
~~~~~~~~~~~~~~~~

.. code-block:: python

   # Check URL prefix
   notfound_urls_prefix = '/correct/path/'
   
   # Verify in 404.html
   # Links should have correct base path

Theme Issues
~~~~~~~~~~~~

.. code-block:: python

   # Ensure theme compatibility
   html_theme = 'sphinx_rtd_theme'
   
   # May need custom template for some themes
   notfound_template = 'custom_404.html'


Practical Examples
------------------

Basic Configuration
-------------------

Setup
~~~~~

.. code-block:: python

   # conf.py
   extensions = [
       'notfound.extension',
   ]

Default Behavior
~~~~~~~~~~~~~~~~

The extension automatically creates a 404 page using your theme with:

- Site title
- Search box
- Navigation links
- Return to homepage link

Custom Content
--------------

Custom Message
~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   notfound_context = {
       'title': 'Page Not Found',
       'body': '''
           <h1>404 - Page Not Found</h1>
           <p>Sorry, the page you're looking for doesn't exist.</p>
           <p>Try using the search box or navigation menu.</p>
       ''',
   }

Template Variables
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   notfound_context = {
       'title': 'Not Found',
       'body': '''
           <h1>Oops!</h1>
           <p>We couldn't find: {{ pagename }}</p>
           <p><a href="{{ pathto(master_doc) }}">Return home</a></p>
       ''',
   }

URLs Configuration
------------------

URL Prefix
~~~~~~~~~~

For sites hosted in subdirectories:

.. code-block:: python

   # conf.py
   notfound_urls_prefix = '/docs/'

This ensures links work correctly when docs are at ``example.com/docs/``.

External URLs
~~~~~~~~~~~~~

.. code-block:: python

   # For docs hosted on different domain
   notfound_urls_prefix = 'https://docs.example.com/'

No Prefix
~~~~~~~~~

.. code-block:: python

   # For root-level hosting
   notfound_urls_prefix = '/'

Template Customization
----------------------

Custom Template
~~~~~~~~~~~~~~~

Create ``_templates/404.html``:

.. code-block:: html

   {% extends "!404.html" %}
   
   {% block body %}
   <div class="notfound-page">
       <h1>404 - Page Not Found</h1>
       
       <p class="error-message">
           The page <code>{{ pagename }}</code> could not be found.
       </p>
       
       <div class="suggestions">
           <h2>What would you like to do?</h2>
           <ul>
               <li><a href="{{ pathto(master_doc) }}">Go to homepage</a></li>
               <li><a href="{{ pathto('search') }}">Search documentation</a></li>
               <li><a href="{{ pathto('genindex') }}">View index</a></li>
           </ul>
       </div>
   </div>
   {% endblock %}

Specify Template
~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   notfound_template = '404.html'
   
   templates_path = ['_templates']

Advanced Templates
------------------

With Search
~~~~~~~~~~~

.. code-block:: html

   {% extends "!404.html" %}
   
   {% block body %}
   <div class="notfound-container">
       <h1>Page Not Found</h1>
       
       <p>Try searching for what you need:</p>
       
       {{ search }}
       
       <p>Or browse these sections:</p>
       <ul>
           <li><a href="{{ pathto('getting-started') }}">Getting Started</a></li>
           <li><a href="{{ pathto('api/index') }}">API Reference</a></li>
           <li><a href="{{ pathto('tutorials/index') }}">Tutorials</a></li>
       </ul>
   </div>
   {% endblock %}

With Theme Integration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: html

   {% extends "!404.html" %}
   
   {% block extrahead %}
   {{ super() }}
   <style>
       .notfound-page {
           max-width: 800px;
           margin: 50px auto;
           padding: 20px;
           text-align: center;
       }
       .error-code {
           font-size: 120px;
           color: #e74c3c;
           font-weight: bold;
       }
       .suggestions {
           margin-top: 30px;
       }
       .search-box {
           margin: 20px 0;
       }
   </style>
   {% endblock %}
   
   {% block body %}
   <div class="notfound-page">
       <div class="error-code">404</div>
       <h1>Oops! Page Not Found</h1>
       
       <div class="search-box">
           {{ search }}
       </div>
       
       <div class="suggestions">
           <a href="{{ pathto(master_doc) }}" class="btn btn-primary">
               Return to Homepage
           </a>
       </div>
   </div>
   {% endblock %}

Hosting Platforms
-----------------

Read the Docs
~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   # Read the Docs hosts at /en/latest/ by default
   import os
   
   if os.environ.get('READTHEDOCS') == 'True':
       notfound_urls_prefix = '/en/latest/'

GitHub Pages
~~~~~~~~~~~~

.. code-block:: python

   # For https://username.github.io/project/
   html_baseurl = 'https://username.github.io/project/'
   notfound_urls_prefix = '/project/'

GitLab Pages
~~~~~~~~~~~~

.. code-block:: python

   # For https://username.gitlab.io/project/
   notfound_urls_prefix = '/project/'

Custom Server
~~~~~~~~~~~~~

Configure web server to serve 404.html:

**Apache** (``.htaccess``):

.. code-block:: apache

   ErrorDocument 404 /404.html

**Nginx**:

.. code-block:: nginx

   error_page 404 /404.html;
   location = /404.html {
       internal;
   }

Practical Examples
------------------

Simple 404
~~~~~~~~~~

.. code-block:: python

   # conf.py
   extensions = ['notfound.extension']
   
   notfound_context = {
       'body': '''
           <h1>Page Not Found</h1>
           <p>The requested page could not be found.</p>
           <p><a href="/">Return to homepage</a></p>
       ''',
   }

Branded 404
~~~~~~~~~~~

.. code-block:: python

   notfound_context = {
       'title': 'MyProject - 404',
       'body': '''
           <div style="text-align: center;">
               <img src="_static/logo.png" alt="MyProject" width="200">
               <h1>Page Not Found</h1>
               <p>We couldn't find what you're looking for.</p>
               <p><a href="{{ pathto(master_doc) }}">Go Home</a></p>
           </div>
       ''',
   }

Multi-Language Support
----------------------

Language Detection
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   language = 'en'
   locale_dirs = ['locale/']
   
   notfound_context = {
       'body': '''
           <h1>{{ _('Page Not Found') }}</h1>
           <p>{{ _('The page you requested does not exist.') }}</p>
           <p><a href="{{ pathto(master_doc) }}">{{ _('Return home') }}</a></p>
       ''',
   }

Multiple Languages
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # English version
   if language == 'en':
       notfound_urls_prefix = '/en/'
   # Spanish version
   elif language == 'es':
       notfound_urls_prefix = '/es/'

Testing
-------

Local Testing
~~~~~~~~~~~~~

.. code-block:: bash

   # Build docs
   sphinx-build docs docs/_build/html
   
   # Serve locally
   python -m http.server -d docs/_build/html 8000
   
   # Test 404 page
   # Visit: http://localhost:8000/nonexistent

Check Generated Page
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Verify 404.html exists
   ls docs/_build/html/404.html
   
   # View content
   cat docs/_build/html/404.html

Integration Testing
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # test_404.py
   import requests
   
   def test_404_page():
       """Test custom 404 page."""
       response = requests.get('http://localhost:8000/nonexistent')
       assert response.status_code == 404
       assert 'Page Not Found' in response.text
       assert 'Return home' in response.text

Analytics Integration
---------------------

Google Analytics
~~~~~~~~~~~~~~~~

.. code-block:: html

   {% extends "!404.html" %}
   
   {% block extrahead %}
   {{ super() }}
   <!-- Google Analytics -->
   <script>
       // Track 404 errors
       if (typeof ga !== 'undefined') {
           ga('send', 'event', 'Error', '404', document.location.pathname);
       }
   </script>
   {% endblock %}

Custom Tracking
~~~~~~~~~~~~~~~

.. code-block:: html

   {% block extrahead %}
   {{ super() }}
   <script>
       // Log 404 to your service
       fetch('/api/log-404', {
           method: 'POST',
           body: JSON.stringify({
               path: window.location.pathname,
               referrer: document.referrer,
               timestamp: new Date().toISOString()
           })
       });
   </script>
   {% endblock %}

Best Practices
--------------

Content Guidelines
~~~~~~~~~~~~~~~~~~

1. Keep the message friendly and helpful
2. Provide clear navigation options
3. Include search functionality
4. Match your site's branding
5. Show suggested pages

Technical Tips
~~~~~~~~~~~~~~

1. Test on all hosting platforms
2. Verify URL prefixes are correct
3. Ensure assets (CSS/JS) load
4. Check mobile responsiveness
5. Monitor 404 occurrences

Accessibility
~~~~~~~~~~~~~

.. code-block:: html

   <div role="alert" aria-live="polite">
       <h1>Page Not Found</h1>
       <p>
           The page you requested at
           <code aria-label="Requested URL">{{ pagename }}</code>
           could not be found.
       </p>
   </div>

Troubleshooting
---------------

404 Page Not Generated
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Ensure extension is loaded
   extensions = ['notfound.extension']
   
   # Check build output
   # Should see: "writing additional pages... 404"

Links Don't Work
~~~~~~~~~~~~~~~~

.. code-block:: python

   # Check URL prefix
   notfound_urls_prefix = '/correct/path/'
   
   # Verify in 404.html
   # Links should have correct base path

Theme Issues
~~~~~~~~~~~~

.. code-block:: python

   # Ensure theme compatibility
   html_theme = 'sphinx_rtd_theme'
   
   # May need custom template for some themes
   notfound_template = 'custom_404.html'

Additional Resources
--------------------
- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `sphinx-notfound-page Documentation <https://sphinx-notfound-page.readthedocs.io/>`_
- `GitHub Pages 404 <https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-custom-404-page-for-your-github-pages-site>`_
- GitHub repository: https://github.com/readthedocs/sphinx-notfound-page

