Sphinx-Notfound-Page Example
============================

This page demonstrates the **sphinx-notfound-page** extension for creating custom 404 error pages in Sphinx documentation.

.. contents:: Contents
   :local:
   :depth: 2

Overview
--------

The sphinx-notfound-page extension generates a custom 404 error page for your Sphinx documentation that matches your theme and provides helpful navigation options.

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

See Also
--------

- :doc:`../tutorials/packages/sphinx-notfound-page` - Complete tutorial
- GitHub repository: https://github.com/readthedocs/sphinx-notfound-page
