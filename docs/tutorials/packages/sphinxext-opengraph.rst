Sphinxext-Opengraph Tutorial
============================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinxext-opengraph/>`_
   - `Official Documentation <https://sphinxext-opengraph.readthedocs.io/>`_
   - :doc:`See Working Example <../../examples/sphinxext-opengraph-example>`


This tutorial demonstrates how to use sphinxext-opengraph to add Open Graph metadata for better social media sharing.

What is Sphinxext-Opengraph?
-----------------------------
sphinxext-opengraph is a Sphinx extension that provides:

- Open Graph meta tags
- Twitter Card support
- Social media previews
- Rich link previews
- Custom images per page
- Automatic metadata generation
- Facebook sharing optimization
- LinkedIn preview support
- Discord embed cards
- SEO improvements

This ensures your documentation looks professional when shared on social media platforms.

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

sphinxext-opengraph is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinxext.opengraph; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinxext.opengraph',
   ]
   
   # Basic Open Graph configuration
   ogp_site_url = "https://docs.example.com/"
   ogp_site_name = "MyProject Documentation"

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinxext.opengraph']
   
   # Site information
   ogp_site_url = "https://docs.example.com/"
   ogp_site_name = "MyProject Documentation"
   
   # Default image
   ogp_image = "https://docs.example.com/_static/logo.png"
   ogp_image_alt = "MyProject Logo"
   
   # Social media
   ogp_social_cards = {
       "enable": True,
       "image": "_static/social-card.png",
   }
   
   # Twitter specific
   ogp_twitter_site = "@myproject"
   ogp_twitter_card = "summary_large_image"
   
   # Description
   ogp_description_length = 200
   ogp_use_first_image = True
   
   # Custom types
   ogp_type = "website"
   
   # Additional metadata
   ogp_custom_meta_tags = [
       '<meta property="og:locale" content="en_US" />',
       '<meta property="fb:app_id" content="123456789" />',
   ]


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

Basic Usage
-----------

Automatic Metadata
~~~~~~~~~~~~~~~~~~

Once configured, Open Graph tags are automatically added to all pages:

.. code-block:: html

   <meta property="og:title" content="Page Title" />
   <meta property="og:type" content="website" />
   <meta property="og:url" content="https://docs.example.com/page.html" />
   <meta property="og:image" content="https://docs.example.com/_static/logo.png" />
   <meta property="og:description" content="Page description..." />

Per-Page Metadata
~~~~~~~~~~~~~~~~~

Override metadata for specific pages:

.. code-block:: rst

   .. meta::
      :description: Custom description for this page
      :og:title: Custom Social Media Title
      :og:image: https://example.com/custom-image.png

   Welcome to MyProject
   ====================
   
   MyProject is a powerful library for data processing and analysis.
   
   Features
   --------
   
   - Fast data processing
   - Easy to use API
   - Comprehensive documentation

Result when shared:

.. code-block:: html

   <meta property="og:title" content="Welcome to MyProject" />
   <meta property="og:description" content="MyProject is a powerful library..." />
   <meta property="og:image" content="https://myproject.readthedocs.io/_static/logo.png" />

Example 2: Custom Images Per Page
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/tutorials/getting-started.rst``:

.. code-block:: rst

   .. meta::
      :og:image: https://docs.example.com/_static/tutorial-preview.png
      :og:image:alt: Getting Started Tutorial
   
   Getting Started Tutorial
   ========================
   
   Learn how to use MyProject in 5 minutes.

``docs/api/reference.rst``:

.. code-block:: rst

   .. meta::
      :og:image: https://docs.example.com/_static/api-preview.png
      :og:image:alt: API Reference
      :og:description: Complete API reference for MyProject
   
   API Reference
   =============
   
   Detailed API documentation.

Example 3: Twitter Card Optimization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/conf.py``:

.. code-block:: python

   extensions = ['sphinxext.opengraph']
   
   # Site info
   ogp_site_url = 'https://myproject.dev/'
   ogp_site_name = 'MyProject'
   
   # Twitter configuration
   ogp_twitter_site = '@myproject'
   ogp_twitter_card = 'summary_large_image'
   ogp_image = 'https://myproject.dev/_static/twitter-card.png'
   
   # Large image for better Twitter preview
   ogp_image_width = 1200
   ogp_image_height = 630

Creates Twitter Card:

.. code-block:: html

   <meta name="twitter:card" content="summary_large_image" />
   <meta name="twitter:site" content="@myproject" />
   <meta name="twitter:title" content="Page Title" />
   <meta name="twitter:description" content="Description..." />
   <meta name="twitter:image" content="https://myproject.dev/_static/twitter-card.png" />

Example 4: Multiple Social Platforms
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/conf.py``:

.. code-block:: python

   extensions = ['sphinxext.opengraph']
   
   # Base configuration
   ogp_site_url = 'https://docs.example.com/'
   ogp_site_name = 'Example Docs'
   ogp_type = 'website'
   
   # Default image (1200x630 for best compatibility)
   ogp_image = 'https://docs.example.com/_static/social-preview.png'
   ogp_image_width = 1200
   ogp_image_height = 630
   ogp_image_alt = 'Example Project Documentation'
   
   # Twitter
   ogp_twitter_site = '@exampleproject'
   ogp_twitter_card = 'summary_large_image'
   
   # Custom metadata for other platforms
   ogp_custom_meta_tags = [
       '<meta property="og:locale" content="en_US" />',
       '<meta property="article:publisher" content="https://facebook.com/example" />',
   ]

Example 5: Dynamic Social Cards
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/conf.py``:

.. code-block:: python

   import os
   
   extensions = ['sphinxext.opengraph']
   
   # Generate social cards dynamically
   def create_social_card(app, pagename, templatename, context, doctree):
       """Generate custom social card for each page."""
       if pagename == 'index':
           context['ogp_image'] = 'https://example.com/_static/home-card.png'
       elif pagename.startswith('api/'):
           context['ogp_image'] = 'https://example.com/_static/api-card.png'
       elif pagename.startswith('tutorials/'):
           context['ogp_image'] = 'https://example.com/_static/tutorial-card.png'
       else:
           context['ogp_image'] = 'https://example.com/_static/default-card.png'
   
   def setup(app):
       app.connect('html-page-context', create_social_card)
   
   # Base configuration
   ogp_site_url = 'https://example.com/'
   ogp_site_name = 'Example Documentation'

Advanced Features
-----------------

Automatic First Image
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Use first image in document as og:image
   ogp_use_first_image = True

This automatically selects the first image from the page content.

Custom Description Length
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Limit description length (characters)
   ogp_description_length = 200

Custom Meta Tags
~~~~~~~~~~~~~~~~

.. code-block:: python

   ogp_custom_meta_tags = [
       '<meta property="og:video" content="https://example.com/video.mp4" />',
       '<meta property="og:locale:alternate" content="fr_FR" />',
       '<meta name="author" content="MyProject Team" />',
   ]

Content Type Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Different types for different pages
   def setup(app):
       def set_content_type(app, pagename, templatename, context, doctree):
           if pagename.startswith('blog/'):
               context['ogp_type'] = 'article'
           else:
               context['ogp_type'] = 'website'
       
       app.connect('html-page-context', set_content_type)

Read the Docs Integration
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import os
   
   # Detect Read the Docs
   on_rtd = os.environ.get('READTHEDOCS') == 'True'
   
   if on_rtd:
       rtd_version = os.environ.get('READTHEDOCS_VERSION', 'latest')
       ogp_site_url = f'https://myproject.readthedocs.io/en/{rtd_version}/'
   else:
       ogp_site_url = 'https://myproject.readthedocs.io/'

Docker Integration
------------------

Build with Open Graph
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     kensai-sphinx:latest \
     sphinx-build -b html /project/docs /project/docs/_build/html

Verify Metadata
~~~~~~~~~~~~~~~

.. code-block:: bash

   # Check Open Graph tags
   docker run --rm \
     -v $(pwd):/project \
     kensai-sphinx:latest \
     sh -c "grep -A 5 'og:title' /project/docs/_build/html/index.html"

CI/CD Integration
-----------------

GitHub Actions with Testing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Build Docs with Open Graph
   
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
         
         - name: Verify Open Graph Tags
           run: |
             # Check that Open Graph tags are present
             if ! grep -q 'og:title' docs/_build/html/index.html; then
               echo "Open Graph tags not found!"
               exit 1
             fi
             
             # Verify image URL
             if ! grep -q 'og:image' docs/_build/html/index.html; then
               echo "Open Graph image not set!"
               exit 1
             fi
         
         - name: Test Social Preview
           run: |
             # Validate image URLs are accessible
             IMAGE_URL=$(grep 'og:image' docs/_build/html/index.html | \
                         sed -n 's/.*content="\([^"]*\)".*/\1/p')
             echo "Image URL: $IMAGE_URL"
         
         - name: Deploy
           uses: peaceiris/actions-gh-pages@v3
           with:
             github_token: ${{ secrets.GITHUB_TOKEN }}
             publish_dir: ./docs/_build/html

Best Practices
--------------

1. **Optimize Images**
   
   Use 1200x630px for best compatibility

2. **Keep Descriptions Short**
   
   160-200 characters for optimal display

3. **Test Previews**
   
   Use Facebook Sharing Debugger, Twitter Card Validator

4. **Unique Images**
   
   Different images for major sections

5. **Accurate Metadata**
   
   Ensure titles and descriptions match content

6. **Performance**
   
   Optimize social card images for fast loading

Troubleshooting
---------------

Tags Not Generated
~~~~~~~~~~~~~~~~~~

**Solution:**

Check extension loaded:

.. code-block:: python

   extensions = ['sphinxext.opengraph']

Verify site URL is set:

.. code-block:: python

   ogp_site_url = "https://example.com/"

Image Not Showing
~~~~~~~~~~~~~~~~~

**Solution:**

Use absolute URLs:

.. code-block:: python

   ogp_image = "https://example.com/_static/logo.png"

Verify image exists and is accessible.

Wrong Preview
~~~~~~~~~~~~~

**Solution:**

Clear social media cache:

- Facebook: https://developers.facebook.com/tools/debug/
- Twitter: https://cards-dev.twitter.com/validator
- LinkedIn: Use post inspector

Description Too Long
~~~~~~~~~~~~~~~~~~~~

**Solution:**

Set maximum length:

.. code-block:: python

   ogp_description_length = 160

Testing Previews
~~~~~~~~~~~~~~~~

**Tools:**

- `Facebook Sharing Debugger <https://developers.facebook.com/tools/debug/>`_
- `Twitter Card Validator <https://cards-dev.twitter.com/validator>`_
- `LinkedIn Post Inspector <https://www.linkedin.com/post-inspector/>`_
- `OpenGraph.xyz <https://www.opengraph.xyz/>`_

Next Steps
----------

1. Configure basic Open Graph settings
2. Create social media images
3. Test with validators
4. Add per-page customization
5. Deploy and share

Additional Resources
--------------------

- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `sphinxext-opengraph Documentation <https://sphinxext-opengraph.readthedocs.io/>`_
- `Open Graph Protocol <https://ogp.me/>`_
- `Twitter Cards Guide <https://developer.twitter.com/en/docs/twitter-for-websites/cards/overview/abouts-cards>`_
