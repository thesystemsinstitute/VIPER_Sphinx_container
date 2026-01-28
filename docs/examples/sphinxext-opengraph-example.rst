sphinxext-opengraph - Working Example
======================================

This page demonstrates the capabilities of **sphinxext-opengraph**, a Sphinx extension that adds Open Graph meta tags to your documentation for better social media integration and link previews.

.. note::

   **About sphinxext-opengraph**
   
   sphinxext-opengraph automatically generates Open Graph protocol meta tags that control how your documentation appears when shared on social media platforms like Facebook, Twitter, LinkedIn, and Slack.
   
   - **Package**: sphinxext-opengraph
   - **Purpose**: Social media meta tags and link previews
   - **Use Case**: Improve documentation sharing on social platforms
   - **Tutorial**: :doc:`../tutorials/packages/sphinxext-opengraph`

Overview
--------

Open Graph protocol is a standard for providing metadata about web pages that social media platforms use to create rich previews when URLs are shared.

Key Features
~~~~~~~~~~~~

**Social Media Integration**

- Automatic Open Graph meta tag generation
- Twitter Card support
- LinkedIn preview optimization
- Facebook sharing enhancements

**Customization Options**

- Per-page configuration
- Default values for all pages
- Image, title, and description control
- Site name and URL configuration

**Platform Support**

- Facebook Open Graph
- Twitter Cards (summary and large image)
- LinkedIn rich previews
- Slack unfurling
- Discord embeds

Installation
------------

Basic Installation
~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   pip install sphinxext-opengraph

The extension is already installed in this environment:

.. code-block:: python

   import sphinxext.opengraph
   print(f"Version: {sphinxext.opengraph.__version__}")

Configuration
-------------

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   # Enable the extension
   extensions = [
       'sphinxext.opengraph',
   ]
   
   # Basic Open Graph settings
   ogp_site_url = "https://docs.example.com/"
   ogp_site_name = "My Documentation"

Default Image Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Set a default image for all pages:

.. code-block:: python

   # Default OG image
   ogp_image = "https://docs.example.com/_static/og-image.png"
   
   # Or use a local image (relative to _static)
   ogp_image = "_static/logo.png"
   
   # Image dimensions (recommended: 1200x630)
   ogp_image_width = 1200
   ogp_image_height = 630

Social Media Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure for different platforms:

.. code-block:: python

   # Enable Twitter Card support
   ogp_enable_meta_description = True
   
   # Twitter-specific configuration
   ogp_social_cards = {
       "site": "@yourusername",
       "creator": "@yourusername",
   }
   
   # Default card type (summary or summary_large_image)
   ogp_type = "article"

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Custom meta tags
   ogp_custom_meta_tags = [
       '<meta property="og:locale" content="en_US" />',
       '<meta property="article:author" content="Your Name" />',
   ]
   
   # Use absolute URLs for images
   ogp_use_first_image = True
   
   # Exclude specific pages
   ogp_exclude = [
       "genindex",
       "search",
   ]

Per-Page Configuration
-----------------------

Using Page Metadata
~~~~~~~~~~~~~~~~~~~

Configure Open Graph tags for individual pages using metadata:

.. code-block:: rst

   .. meta::
      :og:title: Custom Page Title
      :og:description: A custom description for this specific page
      :og:image: https://example.com/custom-image.png
   
   Page Title
   ==========
   
   Your content here...

Title Override Example
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. meta::
      :og:title: Complete Guide to Python Decorators
      :og:description: Learn everything about Python decorators with examples
   
   Python Decorators Guide
   ========================

Description Override
~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. meta::
      :description: API reference for the authentication module
      :og:description: Complete API documentation for user authentication
   
   Authentication API
   ==================

Image Override
~~~~~~~~~~~~~~

.. code-block:: rst

   .. meta::
      :og:image: https://docs.example.com/_images/tutorial-banner.png
      :og:image:width: 1200
      :og:image:height: 630
   
   Tutorial: Getting Started
   =========================

Open Graph Tag Examples
------------------------

Basic Article Tags
~~~~~~~~~~~~~~~~~~

For documentation pages (article type):

.. code-block:: html

   <meta property="og:type" content="article" />
   <meta property="og:title" content="Installation Guide" />
   <meta property="og:description" content="Complete installation instructions" />
   <meta property="og:url" content="https://docs.example.com/install.html" />
   <meta property="og:image" content="https://docs.example.com/_static/og-image.png" />
   <meta property="og:site_name" content="My Documentation" />

Twitter Card Tags
~~~~~~~~~~~~~~~~~

Twitter-specific metadata:

.. code-block:: html

   <meta name="twitter:card" content="summary_large_image" />
   <meta name="twitter:site" content="@yourusername" />
   <meta name="twitter:creator" content="@author" />
   <meta name="twitter:title" content="Installation Guide" />
   <meta name="twitter:description" content="Complete installation instructions" />
   <meta name="twitter:image" content="https://docs.example.com/_static/og-image.png" />

LinkedIn Tags
~~~~~~~~~~~~~

LinkedIn uses standard Open Graph tags:

.. code-block:: html

   <meta property="og:type" content="website" />
   <meta property="og:title" content="API Documentation" />
   <meta property="og:description" content="Complete API reference" />
   <meta property="og:image" content="https://docs.example.com/_static/api-preview.png" />

Practical Examples
-------------------

Documentation Project Setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Complete configuration for a documentation project:

.. code-block:: python

   # conf.py
   extensions = ['sphinxext.opengraph']
   
   # Site configuration
   ogp_site_url = "https://myproject.readthedocs.io/"
   ogp_site_name = "MyProject Documentation"
   
   # Default image
   ogp_image = "_static/social-preview.png"
   ogp_image_width = 1200
   ogp_image_height = 630
   
   # Twitter integration
   ogp_social_cards = {
       "site": "@myproject",
   }
   
   # Enable meta description
   ogp_enable_meta_description = True
   
   # Exclude internal pages
   ogp_exclude = ["genindex", "search", "py-modindex"]

API Documentation Setup
~~~~~~~~~~~~~~~~~~~~~~~

For API documentation with custom previews:

.. code-block:: python

   # conf.py
   ogp_site_url = "https://api-docs.example.com/"
   ogp_site_name = "Example API"
   ogp_type = "website"
   
   # API-specific image
   ogp_image = "https://api-docs.example.com/_static/api-og.png"
   
   # Custom tags for API docs
   ogp_custom_meta_tags = [
       '<meta property="og:locale" content="en_US" />',
       '<meta property="article:section" content="API Reference" />',
   ]

Tutorial Site Setup
~~~~~~~~~~~~~~~~~~~

For tutorial-focused documentation:

.. code-block:: python

   # conf.py
   ogp_site_url = "https://tutorials.example.com/"
   ogp_site_name = "Example Tutorials"
   ogp_type = "article"
   
   # Use first image from each page
   ogp_use_first_image = True
   
   # Author information
   ogp_custom_meta_tags = [
       '<meta property="article:author" content="Tutorial Team" />',
       '<meta property="article:section" content="Tutorials" />',
   ]

Social Media Previews
---------------------

Facebook Preview
~~~~~~~~~~~~~~~~

What users see when sharing on Facebook:

.. code-block:: text

   ┌──────────────────────────────────────┐
   │  [Image: 1200x630 preview image]     │
   ├──────────────────────────────────────┤
   │  MY DOCUMENTATION                    │
   │  Installation Guide                  │
   │  Complete installation instructions  │
   │  docs.example.com                    │
   └──────────────────────────────────────┘

Twitter Preview
~~~~~~~~~~~~~~~

Large image card preview:

.. code-block:: text

   ┌──────────────────────────────────────┐
   │  [Image: Large preview image]        │
   ├──────────────────────────────────────┤
   │  Installation Guide                  │
   │  Complete installation instructions  │
   │  🔗 docs.example.com                 │
   └──────────────────────────────────────┘

LinkedIn Preview
~~~~~~~~~~~~~~~~

Professional preview format:

.. code-block:: text

   ┌──────────────────────────────────────┐
   │  [Image: Preview image]              │
   ├──────────────────────────────────────┤
   │  Installation Guide                  │
   │  Complete installation instructions  │
   │  My Documentation                    │
   │  docs.example.com                    │
   └──────────────────────────────────────┘

Slack/Discord Unfurling
~~~~~~~~~~~~~~~~~~~~~~~

Rich preview in chat applications:

.. code-block:: text

   My Documentation
   Installation Guide
   Complete installation instructions
   [Image preview]
   docs.example.com

Testing and Validation
-----------------------

Test Your Open Graph Tags
~~~~~~~~~~~~~~~~~~~~~~~~~~

Use these tools to validate your OG tags:

**Facebook Sharing Debugger**:

.. code-block:: bash

   # URL
   https://developers.facebook.com/tools/debug/
   
   # Enter your page URL to see preview

**Twitter Card Validator**:

.. code-block:: bash

   # URL
   https://cards-dev.twitter.com/validator
   
   # Enter your page URL to test Twitter card

**LinkedIn Post Inspector**:

.. code-block:: bash

   # URL
   https://www.linkedin.com/post-inspector/
   
   # Test LinkedIn preview

View Page Source
~~~~~~~~~~~~~~~~

Check generated meta tags:

.. code-block:: bash

   # View HTML source
   curl https://docs.example.com/page.html | grep "og:"
   
   # Expected output:
   # <meta property="og:title" content="Page Title" />
   # <meta property="og:description" content="Description" />
   # <meta property="og:image" content="https://..." />

Common Patterns
---------------

Multi-Language Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Support for multiple languages:

.. code-block:: python

   # conf.py
   language = 'en'
   
   ogp_custom_meta_tags = [
       f'<meta property="og:locale" content="{language}_US" />',
   ]
   
   # Add alternate locales
   if language == 'en':
       ogp_custom_meta_tags.append(
           '<meta property="og:locale:alternate" content="es_ES" />'
       )

Version-Specific Images
~~~~~~~~~~~~~~~~~~~~~~~

Different images for different versions:

.. code-block:: python

   # conf.py
   import os
   
   version = "2.0"
   
   if version.startswith("2."):
       ogp_image = "_static/og-v2.png"
   else:
       ogp_image = "_static/og-v1.png"

Dynamic Site URL
~~~~~~~~~~~~~~~~

Adapt to different environments:

.. code-block:: python

   # conf.py
   import os
   
   # Use environment variable or default
   ogp_site_url = os.environ.get(
       'DOCS_URL',
       'https://docs.example.com/'
   )

Best Practices
--------------

Image Guidelines
~~~~~~~~~~~~~~~~

**Recommended Dimensions**:

- Facebook: 1200×630 pixels (1.91:1 ratio)
- Twitter: 1200×628 pixels (summary_large_image)
- LinkedIn: 1200×627 pixels

**Image Requirements**:

.. code-block:: python

   # Optimal image configuration
   ogp_image_width = 1200
   ogp_image_height = 630
   
   # Minimum size: 600x315
   # Maximum size: 8MB
   # Formats: JPG, PNG, GIF

Title Best Practices
~~~~~~~~~~~~~~~~~~~~

**Length Recommendations**:

- Facebook: 60-90 characters
- Twitter: 70 characters
- LinkedIn: 100 characters

.. code-block:: python

   # Good title (short and descriptive)
   ogp_title = "Quick Start Guide - MyProject"
   
   # Too long (will be truncated)
   ogp_title = "The Complete Comprehensive Guide to Getting Started..."

Description Guidelines
~~~~~~~~~~~~~~~~~~~~~~

**Length Recommendations**:

- Facebook: 200 characters
- Twitter: 200 characters
- LinkedIn: 160 characters

.. code-block:: rst

   .. meta::
      :og:description: Learn how to install and configure MyProject in 5 minutes
   
   # Good: Clear, concise, under 200 chars

Troubleshooting
---------------

Tags Not Appearing
~~~~~~~~~~~~~~~~~~

Check configuration:

.. code-block:: python

   # Verify extension is loaded
   extensions = ['sphinxext.opengraph']
   
   # Verify site URL is set
   ogp_site_url = "https://docs.example.com/"
   
   # Rebuild documentation
   # make clean && make html

Images Not Loading
~~~~~~~~~~~~~~~~~~

Verify image paths:

.. code-block:: python

   # Use absolute URLs for images
   ogp_image = "https://docs.example.com/_static/og-image.png"
   
   # Not: ogp_image = "_static/og-image.png"
   # (relative paths may not work on all platforms)

Cache Issues
~~~~~~~~~~~~

Social media platforms cache previews:

.. code-block:: bash

   # Clear Facebook cache
   https://developers.facebook.com/tools/debug/
   # Click "Scrape Again"
   
   # Clear LinkedIn cache
   https://www.linkedin.com/post-inspector/
   # Re-inspect URL

Integration Examples
--------------------

Read the Docs Integration
~~~~~~~~~~~~~~~~~~~~~~~~~~

Configuration for RTD:

.. code-block:: python

   # conf.py
   import os
   
   # Detect RTD environment
   on_rtd = os.environ.get('READTHEDOCS') == 'True'
   
   if on_rtd:
       ogp_site_url = f"https://{os.environ['READTHEDOCS_PROJECT']}.readthedocs.io/"
       ogp_image = f"{ogp_site_url}en/latest/_static/og-image.png"

GitHub Pages Integration
~~~~~~~~~~~~~~~~~~~~~~~~~

Configuration for GitHub Pages:

.. code-block:: python

   # conf.py
   project = "myproject"
   github_user = "username"
   
   ogp_site_url = f"https://{github_user}.github.io/{project}/"
   ogp_image = f"{ogp_site_url}_static/social-preview.png"

Custom Domain Setup
~~~~~~~~~~~~~~~~~~~

With custom domain:

.. code-block:: python

   # conf.py
   ogp_site_url = "https://docs.customdomain.com/"
   ogp_site_name = "Custom Documentation"
   
   # Ensure DNS is configured
   # Add CNAME record pointing to hosting provider

See Also
--------

**Related Extensions**:

- :doc:`sphinx-analytics-example` - Analytics tracking
- :doc:`sphinx-rtd-theme-example` - Read the Docs theme
- :doc:`sphinx-book-theme-example` - Book theme

**External Resources**:

- `Open Graph Protocol <https://ogp.me/>`_
- `Twitter Cards <https://developer.twitter.com/en/docs/twitter-for-websites/cards>`_
- `Facebook Sharing <https://developers.facebook.com/docs/sharing/webmasters>`_

**Testing Tools**:

- Facebook Sharing Debugger
- Twitter Card Validator
- LinkedIn Post Inspector
- Open Graph Check

Summary
-------

sphinxext-opengraph provides automatic social media integration for Sphinx documentation:

**Key Capabilities**:

✅ Automatic Open Graph meta tag generation
✅ Twitter Card support
✅ Per-page customization
✅ Image, title, description control
✅ Multi-platform optimization

**Common Use Cases**:

- Documentation site social sharing
- API documentation previews
- Tutorial link previews
- Blog post social cards
- Project documentation marketing

The extension makes documentation more shareable and professional-looking when posted on social media platforms.
