sphinx-analytics - Working Example
====================================

This page demonstrates the capabilities of **sphinx-analytics**, a Sphinx extension for integrating analytics tracking (Google Analytics, Plausible, Matomo, etc.) into your documentation.

.. note::

   **About sphinx-analytics**
   
   sphinx-analytics provides a simple way to add analytics tracking code to your Sphinx documentation, supporting multiple analytics providers with minimal configuration.
   
   - **Package**: sphinx-analytics
   - **Purpose**: Analytics integration for Sphinx docs
   - **Use Case**: Track documentation usage and behavior
   - **Tutorial**: :doc:`../tutorials/packages/sphinx-analytics`


Installation
------------

Basic Installation
~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   pip install sphinx-analytics

The extension is already installed in this environment:

.. code-block:: python

   import sphinx_analytics
   print("sphinx-analytics available")

Configuration
-------------

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

Advanced Configuration
----------------------

Privacy Settings
~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   analytics = {
       'google_analytics_id': 'G-XXXXXXXXXX',
       
       # Privacy options
       'anonymize_ip': True,
       'respect_dnt': True,  # Respect Do Not Track
       'cookie_consent': True,
   }

Custom Configuration
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   analytics = {
       'google_analytics_id': 'G-XXXXXXXXXX',
       
       # Custom GA4 config
       'ga_config': {
           'send_page_view': True,
           'cookie_domain': 'auto',
           'cookie_expires': 63072000,  # 2 years
       }
   }

Conditional Loading
~~~~~~~~~~~~~~~~~~~

Load analytics only in production:

.. code-block:: python

   # conf.py
   import os
   
   extensions = ['sphinx_analytics']
   
   # Only enable in production
   if os.environ.get('READTHEDOCS', False):
       analytics = {
           'google_analytics_id': 'G-XXXXXXXXXX',
       }
   else:
       analytics = {}

Environment-Based Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   import os
   
   extensions = ['sphinx_analytics']
   
   # Different tracking IDs per environment
   env = os.environ.get('DOCS_ENV', 'dev')
   
   analytics_ids = {
       'dev': 'G-DEV1234567',
       'staging': 'G-STAGE123456',
       'production': 'G-PROD123456',
   }
   
   analytics = {
       'google_analytics_id': analytics_ids.get(env, ''),
   }

Event Tracking
--------------

Custom Events
~~~~~~~~~~~~~

Track custom events in your documentation:

.. code-block:: rst

   .. raw:: html
   
      <button onclick="gtag('event', 'download', {
        'event_category': 'engagement',
        'event_label': 'user_guide.pdf'
      });">
        Download User Guide
      </button>

Link Tracking
~~~~~~~~~~~~~

Track external link clicks:

.. code-block:: rst

   .. raw:: html
   
      <a href="https://github.com/myproject" 
         onclick="gtag('event', 'click', {
           'event_category': 'outbound',
           'event_label': 'github'
         });">
        View on GitHub
      </a>

Search Tracking
~~~~~~~~~~~~~~~

Track search queries:

.. code-block:: javascript

   // Custom JavaScript for search tracking
   document.querySelector('#search-form').addEventListener('submit', function(e) {
       gtag('event', 'search', {
           'search_term': document.querySelector('#search-input').value
       });
   });

Download Tracking
~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. raw:: html
   
      <script>
      document.querySelectorAll('a[href$=".pdf"]').forEach(function(link) {
          link.addEventListener('click', function() {
              gtag('event', 'file_download', {
                  'file_name': this.getAttribute('href')
              });
          });
      });
      </script>

Integration Examples
--------------------

Read the Docs
~~~~~~~~~~~~~

Configuration for Read the Docs:

.. code-block:: python

   # conf.py
   import os
   
   extensions = ['sphinx_analytics']
   
   # Enable only on Read the Docs
   on_rtd = os.environ.get('READTHEDOCS') == 'True'
   
   if on_rtd:
       analytics = {
           'google_analytics_id': 'G-XXXXXXXXXX',
       }

GitHub Pages
~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   extensions = ['sphinx_analytics']
   
   # GitHub Pages configuration
   analytics = {
       'google_analytics_id': 'G-XXXXXXXXXX',
   }
   
   html_baseurl = 'https://username.github.io/project/'

Custom Domain
~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   extensions = ['sphinx_analytics']
   
   analytics = {
       'google_analytics_id': 'G-XXXXXXXXXX',
   }
   
   # Ensure canonical URLs
   html_baseurl = 'https://docs.customdomain.com/'

Practical Examples
------------------

Documentation Portal
~~~~~~~~~~~~~~~~~~~~

Track multiple documentation projects:

.. code-block:: python

   # conf.py - Main docs
   project = 'MyProject'
   
   extensions = ['sphinx_analytics']
   
   analytics = {
       'google_analytics_id': 'G-XXXXXXXXXX',
       'ga_config': {
           'custom_map': {
               'dimension1': 'project_name'
           }
       }
   }
   
   # Add custom dimension
   html_theme_options = {
       'analytics_custom_js': '''
           gtag('set', {'project_name': 'MyProject'});
       '''
   }

API Documentation
~~~~~~~~~~~~~~~~~

Track API reference usage:

.. code-block:: python

   # conf.py
   extensions = ['sphinx_analytics']
   
   analytics = {
       'google_analytics_id': 'G-XXXXXXXXXX',
   }

Add event tracking to API pages:

.. code-block:: rst

   .. raw:: html
   
      <script>
      // Track API method views
      gtag('event', 'page_view', {
          'page_title': 'API: ' + document.title,
          'page_location': window.location.href
      });
      </script>

Tutorial Series
~~~~~~~~~~~~~~~

Track tutorial progress:

.. code-block:: rst

   Tutorial: Getting Started
   =========================
   
   .. raw:: html
   
      <script>
      gtag('event', 'tutorial_begin', {
          'tutorial_name': 'Getting Started'
      });
      </script>
   
   Tutorial content here...
   
   .. raw:: html
   
      <script>
      gtag('event', 'tutorial_complete', {
          'tutorial_name': 'Getting Started'
      });
      </script>

GDPR Compliance
---------------

Cookie Consent Banner
~~~~~~~~~~~~~~~~~~~~~

Add cookie consent:

.. code-block:: python

   # conf.py
   extensions = ['sphinx_analytics']
   
   analytics = {
       'google_analytics_id': 'G-XXXXXXXXXX',
       'cookie_consent': True,
   }
   
   html_theme_options = {
       'analytics_cookie_consent_template': '''
           <div id="cookie-consent">
               <p>We use cookies to analyze site usage.</p>
               <button onclick="acceptCookies()">Accept</button>
               <button onclick="rejectCookies()">Reject</button>
           </div>
       '''
   }

Conditional Loading
~~~~~~~~~~~~~~~~~~~

Load analytics only with consent:

.. code-block:: html

   <script>
   function acceptCookies() {
       localStorage.setItem('cookieConsent', 'accepted');
       loadAnalytics();
       document.getElementById('cookie-consent').style.display = 'none';
   }
   
   function rejectCookies() {
       localStorage.setItem('cookieConsent', 'rejected');
       document.getElementById('cookie-consent').style.display = 'none';
   }
   
   function loadAnalytics() {
       if (localStorage.getItem('cookieConsent') === 'accepted') {
           // Load GA4
           var script = document.createElement('script');
           script.src = 'https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX';
           document.head.appendChild(script);
       }
   }
   
   window.addEventListener('load', function() {
       if (!localStorage.getItem('cookieConsent')) {
           document.getElementById('cookie-consent').style.display = 'block';
       } else if (localStorage.getItem('cookieConsent') === 'accepted') {
           loadAnalytics();
       }
   });
   </script>

Privacy Policy Integration
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Privacy Policy
   ==============
   
   This documentation uses Google Analytics to understand how
   visitors use our documentation. Analytics data is:
   
   - Anonymized (IP addresses are masked)
   - Used only for improving documentation
   - Not shared with third parties
   - Respects Do Not Track settings
   
   You can opt out by:
   
   1. Enabling Do Not Track in your browser
   2. Using the `Google Analytics Opt-out Browser Add-on <https://tools.google.com/dlpage/gaoptout>`_
   3. Blocking analytics scripts with an ad blocker

Analytics Dashboards
--------------------

Key Metrics to Track
~~~~~~~~~~~~~~~~~~~~

**Page Views**:

- Most visited pages
- Documentation sections
- Entry pages
- Exit pages

**User Behavior**:

- Time on page
- Bounce rate
- Navigation paths
- Search queries

**Engagement**:

- Downloads
- External link clicks
- Tutorial completions
- Code snippet copies

Custom Reports
~~~~~~~~~~~~~~

Create custom GA4 reports:

.. code-block:: python

   # conf.py
   analytics = {
       'google_analytics_id': 'G-XXXXXXXXXX',
       'ga_config': {
           'custom_map': {
               'dimension1': 'doc_version',
               'dimension2': 'doc_section',
               'dimension3': 'user_role'
           }
       }
   }

Plausible Dashboard
~~~~~~~~~~~~~~~~~~~

Plausible provides a simpler, privacy-focused dashboard:

- Real-time visitors
- Top pages
- Referrer sources
- Countries
- Devices

No personal data collected or cookies required.

Best Practices
--------------

Performance Impact
~~~~~~~~~~~~~~~~~~

Minimize analytics performance impact:

.. code-block:: python

   # conf.py
   analytics = {
       'google_analytics_id': 'G-XXXXXXXXXX',
       'async_loading': True,  # Load asynchronously
   }

Testing Analytics
~~~~~~~~~~~~~~~~~

Test in development:

.. code-block:: python

   # conf.py
   import os
   
   DEBUG = os.environ.get('DEBUG', 'False') == 'True'
   
   extensions = ['sphinx_analytics']
   
   if DEBUG:
       # Use debug mode
       analytics = {
           'google_analytics_id': 'G-XXXXXXXXXX',
           'debug_mode': True,
       }

Data Retention
~~~~~~~~~~~~~~

Configure data retention in GA4:

1. Go to Admin → Data Settings → Data Retention
2. Set event data retention (2 months recommended)
3. Enable "Reset user data on new activity"

Troubleshooting
---------------

Analytics Not Loading
~~~~~~~~~~~~~~~~~~~~~

Check browser console:

.. code-block:: javascript

   // Verify gtag is loaded
   if (typeof gtag === 'undefined') {
       console.error('Google Analytics not loaded');
   } else {
       console.log('GA loaded successfully');
   }

Verify Configuration
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   print(f"Analytics config: {analytics}")

Check generated HTML:

.. code-block:: bash

   # Search for analytics code in built HTML
   grep -r "gtag" _build/html/

Ad Blockers
~~~~~~~~~~~

Many users block analytics:

- Accept that not all traffic will be tracked
- Consider server-side analytics as alternative
- Use privacy-focused analytics (Plausible)

See Also
--------

**Related Extensions**:

- :doc:`sphinxext-opengraph-example` - Social media integration
- :doc:`sphinx-notfound-page-example` - Custom 404 pages
- :doc:`sphinx-rtd-theme-example` - Read the Docs theme

**External Resources**:

- `Google Analytics 4 <https://analytics.google.com/>`_
- `Plausible Analytics <https://plausible.io/>`_
- `Matomo Analytics <https://matomo.org/>`_
- `GDPR Compliance Guide <https://gdpr.eu/>`_

Summary
-------

sphinx-analytics provides analytics integration:

**Key Capabilities**:

✅ Multiple analytics provider support
✅ Simple configuration
✅ Privacy-focused options
✅ Custom event tracking
✅ GDPR compliance features

**Common Use Cases**:

- Documentation usage tracking
- User behavior analysis
- Content optimization
- Tutorial effectiveness measurement
- Search query analysis

Essential for understanding how users interact with your Sphinx documentation.
