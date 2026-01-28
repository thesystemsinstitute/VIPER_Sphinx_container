Sphinx-Analytics Tutorial
=========================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-analytics/>`_
   - `API Documentation <../../pdoc/sphinx_analytics/index.html>`_
   - `Manual <https://github.com/sphinx-contrib/analytics>`_
   - :doc:`Working Example <../../examples/sphinx-analytics-example>`


.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinx-analytics to add web analytics tracking to your Sphinx documentation.

What is Sphinx-Analytics?
--------------------------

sphinx-analytics is a Sphinx extension that provides:

- Google Analytics integration
- Plausible Analytics support
- Fathom Analytics support
- Matomo/Piwik support
- Custom analytics providers
- Privacy-friendly tracking
- GDPR compliance options
- Multiple tracker support
- Event tracking
- Custom dimensions

This enables you to understand how users interact with your documentation.


sphinx-analytics simplifies adding analytics tracking to Sphinx documentation by automatically injecting tracking scripts into generated HTML pages.

Installation
------------

sphinx-analytics is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinx_analytics; print('Installed')"

Configuration
-------------

Basic Setup (Google Analytics)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add to your ``docs/conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_analytics',
   ]
   
   # Google Analytics
   analytics_id = 'G-XXXXXXXXXX'

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinx_analytics']
   
   # Google Analytics 4
   analytics_id = 'G-XXXXXXXXXX'
   analytics_anonymize_ip = True
   
   # Multiple trackers
   analytics_trackers = [
       {
           'type': 'google',
           'id': 'G-XXXXXXXXXX',
       },
       {
           'type': 'plausible',
           'domain': 'docs.example.com',
       },
   ]

Alternative Providers
~~~~~~~~~~~~~~~~~~~~~

**Plausible Analytics:**

.. code-block:: python

   analytics_trackers = [
       {
           'type': 'plausible',
           'domain': 'docs.example.com',
           'src': 'https://plausible.io/js/script.js',
       },
   ]

**Fathom Analytics:**

.. code-block:: python

   analytics_trackers = [
       {
           'type': 'fathom',
           'site_id': 'ABCDEFGH',
       },
   ]

**Matomo/Piwik:**

.. code-block:: python

   analytics_trackers = [
       {
           'type': 'matomo',
           'url': 'https://analytics.example.com/',
           'site_id': 1,
       },
   ]


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Google Analytics 4
~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   # Enable the extension
   extensions = [
       'sphinx_analytics',
   ]
   
   # Google Analytics 4 configuration
   analytics = {
       'google_analytics_id': 'G-XXXXXXXXXX',
   }

Google Universal Analytics (Legacy)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   extensions = ['sphinx_analytics']
   
   # Universal Analytics (legacy)
   analytics = {
       'google_analytics_id': 'UA-XXXXXXXXX-X',
   }

Plausible Analytics
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   extensions = ['sphinx_analytics']
   
   # Plausible Analytics
   analytics = {
       'plausible_domain': 'docs.example.com',
       'plausible_url': 'https://plausible.io/js/script.js',  # Optional
   }

Matomo (Piwik)
~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   extensions = ['sphinx_analytics']
   
   # Matomo configuration
   analytics = {
       'matomo_url': 'https://analytics.example.com/',
       'matomo_site_id': '1',
   }

Multiple Providers
~~~~~~~~~~~~~~~~~~

Track with multiple analytics platforms:

.. code-block:: python

   # conf.py
   extensions = ['sphinx_analytics']
   
   # Multiple analytics providers
   analytics = {
       'google_analytics_id': 'G-XXXXXXXXXX',
       'plausible_domain': 'docs.example.com',
       'matomo_url': 'https://analytics.example.com/',
       'matomo_site_id': '1',
   }

Basic Usage
-----------

Automatic Tracking
~~~~~~~~~~~~~~~~~~

Once configured, analytics tracking is automatically added to all pages:

.. code-block:: html

   <!-- Google Analytics -->
   <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
   <script>
     window.dataLayer = window.dataLayer || [];
     function gtag(){dataLayer.push(arguments);}
     gtag('js', new Date());
     gtag('config', 'G-XXXXXXXXXX');
   </script>

Custom Events
~~~~~~~~~~~~~

Track custom events in documentation:

.. code-block:: html

   <button onclick="gtag('event', 'download', {'event_category': 'engagement'});">
     Download
   </button>

Advanced Features
-----------------

Custom Dimensions
~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   analytics_custom_dimensions = {
       'dimension1': 'Documentation Version',
       'dimension2': 'User Type',
   }

.. code-block:: html

   <script>
     gtag('config', 'G-XXXXXXXXXX', {
       'custom_map': {
         'dimension1': 'doc_version',
         'dimension2': 'user_type'
       }
     });
     
     gtag('event', 'page_view', {
       'doc_version': '2.0',
       'user_type': 'developer'
     });
   </script>

Content Grouping
~~~~~~~~~~~~~~~~

.. code-block:: html

   <script>
     gtag('config', 'G-XXXXXXXXXX', {
       'content_group': '{{ pagename.split('/')[0] if '/' in pagename else 'root' }}'
     });
   </script>

User ID Tracking
~~~~~~~~~~~~~~~~

.. code-block:: html

   <script>
     // If user is logged in
     var userId = getUserId();  // Your function
     if (userId) {
       gtag('config', 'G-XXXXXXXXXX', {
         'user_id': userId
       });
     }
   </script>

Docker Integration
------------------

Build with Analytics
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     -e ANALYTICS_ID=G-XXXXXXXXXX \
     kensai-sphinx:latest \
     sphinx-build -b html /project/docs /project/docs/_build/html

Dynamic Configuration
~~~~~~~~~~~~~~~~~~~~~

``docs/conf.py``:

.. code-block:: python

   import os
   
   # Get analytics ID from environment
   analytics_id = os.environ.get('ANALYTICS_ID', '')

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Build Docs with Analytics
   
   on:
     push:
       branches: [main]
   
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Build Documentation
           env:
             ANALYTICS_ID: ${{ secrets.GOOGLE_ANALYTICS_ID }}
           run: |
             docker run --rm \
               -v $(pwd):/project \
               -e ANALYTICS_ID=$ANALYTICS_ID \
               kensai-sphinx:latest \
               sphinx-build -b html /project/docs /project/docs/_build/html
         
         - name: Verify Analytics Code
           run: |
             if grep -q "G-XXXXXXXXXX" docs/_build/html/index.html; then
               echo "✓ Analytics code found"
             else
               echo "⚠ Analytics code not found"
             fi
         
         - name: Deploy
           uses: peaceiris/actions-gh-pages@v3
           with:
             github_token: ${{ secrets.GITHUB_TOKEN }}
             publish_dir: ./docs/_build/html

Environment-Specific Analytics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

   # Different IDs for staging/production
   - name: Build Documentation
     env:
       ANALYTICS_ID: ${{ github.ref == 'refs/heads/main' && secrets.PROD_ANALYTICS_ID || secrets.STAGING_ANALYTICS_ID }}
     run: invoke docs-build

Best Practices
--------------

1. **Privacy First**
   
   Use anonymized IP and privacy-friendly trackers

2. **Conditional Loading**
   
   Disable in development/testing

3. **Track Meaningful Events**
   
   Downloads, searches, external links

4. **GDPR Compliance**
   
   Add cookie consent if needed

5. **Performance**
   
   Use async loading

6. **Test Tracking**
   
   Verify events in analytics dashboard

Troubleshooting
---------------

Analytics Not Loading
~~~~~~~~~~~~~~~~~~~~~

**Solution:**

Check tracking ID is set:

.. code-block:: python

   print(f"Analytics ID: {analytics_id}")

Verify in HTML output:

.. code-block:: bash

   grep -r "gtag" docs/_build/html/

Wrong Data Tracked
~~~~~~~~~~~~~~~~~~

**Solution:**

Use debug mode:

.. code-block:: python

   analytics_debug = True

Check browser console for tracking events.

Ad Blockers
~~~~~~~~~~~

**Solution:**

Ad blockers may block tracking. Consider privacy-focused alternatives like Plausible.

GDPR Compliance
~~~~~~~~~~~~~~~

**Solution:**

1. Anonymize IP:

.. code-block:: python

   analytics_anonymize_ip = True

2. Add cookie consent banner
3. Update privacy policy

Testing Locally
~~~~~~~~~~~~~~~

**Solution:**

Analytics typically don't work on localhost. Use:

.. code-block:: python

   analytics_debug = True

Or test on deployed site.

Next Steps
----------

1. Choose analytics provider
2. Get tracking ID
3. Configure in conf.py
4. Add custom events
5. Monitor analytics dashboard

Additional Resources
--------------------

- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `Google Analytics 4 <https://analytics.google.com/>`_
- `Plausible Analytics <https://plausible.io/>`_
- `Fathom Analytics <https://usefathom.com/>`_
- `GDPR Compliance Guide <https://gdpr.eu/>`_
