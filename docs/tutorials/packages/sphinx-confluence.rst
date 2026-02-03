Sphinx-Confluence Tutorial
==========================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-confluence/>`_
   - `API Documentation <../../pdoc/sphinx_confluence/index.html>`_
   - `Manual <https://sphinxcontrib-confluencebuilder.readthedocs.io/>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinx-confluence (sphinxcontrib-confluencebuilder) to publish your Sphinx documentation directly to Atlassian Confluence.

What is Sphinx-Confluence?
---------------------------
sphinx-confluence (also known as sphinxcontrib-confluencebuilder) is a Sphinx extension that enables you to build and publish your documentation to Confluence Wiki. This allows you to:

- Maintain documentation in reStructuredText or Markdown
- Build for both HTML and Confluence targets
- Automatically sync documentation to Confluence
- Leverage Sphinx's powerful features while using Confluence as a platform
- Keep documentation in version control while publishing to a wiki

When you use sphinx-confluence to publish documentation to Confluence, your reStructuredText files are converted into Confluence's storage format (XHTML). This example shows what various Sphinx elements look like when published.


Installation
------------

sphinx-confluence is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm viper-sphinx:latest pip show sphinx-confluence

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   # Add to extensions
   extensions = [
       'sphinxcontrib.confluencebuilder',
       # ... other extensions
   ]
   
   # Confluence configuration
   confluence_publish = True
   confluence_space_name = 'YOUR_SPACE'
   confluence_server_url = 'https://your-domain.atlassian.net/wiki'
   confluence_server_user = 'your-email@example.com'
   confluence_server_pass = 'your-api-token'

Authentication Options
~~~~~~~~~~~~~~~~~~~~~~

**API Token (Recommended for Confluence Cloud):**

.. code-block:: python

   confluence_server_user = 'your-email@example.com'
   confluence_server_pass = 'your-api-token'  # Generate in Confluence settings

**Personal Access Token:**

.. code-block:: python

   confluence_publish_token = 'your-personal-access-token'

**Environment Variables (More Secure):**

.. code-block:: python

   import os
   
   confluence_server_user = os.getenv('CONFLUENCE_USER')
   confluence_server_pass = os.getenv('CONFLUENCE_API_TOKEN')

Then run:

.. code-block:: bash

   docker run --rm \
       -e CONFLUENCE_USER=your-email@example.com \
       -e CONFLUENCE_API_TOKEN=your-token \
       -v $(pwd):/project \
       viper-sphinx:latest \
       sphinx-build -b confluence /project/docs /project/docs/_build/confluence

Essential Configuration Options
--------------------------------

Publishing Options
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Enable/disable publishing
   confluence_publish = True  # Set to False to only build locally
   
   # Parent page (optional - where to publish docs)
   confluence_parent_page = 'Documentation'
   
   # Page prefix (helps organize docs)
   confluence_page_prefix = 'MyProject - '
   
   # Cleanup old pages
   confluence_purge = False  # Set to True to remove obsolete pages
   confluence_purge_from_master = True  # Only purge pages not in current build

Content Options
~~~~~~~~~~~~~~~

.. code-block:: python

   # Max width for images
   confluence_max_image_width = 800
   
   # File types to publish
   confluence_publish_dryrun = False  # Set True to test without publishing
   
   # Code block theme
   confluence_code_block_theme = 'midnight'  # or 'default', 'django', etc.
   
   # Remove title from pages
   confluence_remove_title = False
   
   # Header/Footer
   confluence_header_file = 'header.tpl'
   confluence_footer_file = 'footer.tpl'

Advanced Options
~~~~~~~~~~~~~~~~

.. code-block:: python

   # Asset handling
   confluence_asset_override = True  # Always update images/attachments
   
   # SSL verification
   confluence_disable_ssl_validation = False  # Only for testing!
   
   # Proxy settings
   confluence_proxy = 'http://proxy.example.com:8080'
   
   # Timeout
   confluence_timeout = 30  # seconds
   
   # Page hierarchy
   confluence_page_hierarchy = True  # Maintain doc structure
   
   # Verbose output
   confluence_publish_debug = True

Building for Confluence
------------------------

Local Build (No Publishing)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Build Confluence-formatted pages locally:

.. code-block:: bash

   # Set confluence_publish = False in conf.py
   docker run --rm -v $(pwd):/project viper-sphinx:latest \
       sphinx-build -b confluence /project/docs /project/docs/_build/confluence

This creates Confluence Storage Format files without publishing.

Publish to Confluence
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
       -e CONFLUENCE_USER=your-email@example.com \
       -e CONFLUENCE_API_TOKEN=your-token \
       -v $(pwd):/project \
       viper-sphinx:latest \
       sphinx-build -b confluence /project/docs /project/docs/_build/confluence

Dry Run (Test Before Publishing)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # In conf.py
   confluence_publish_dryrun = True

This shows what would be published without actually doing it.

Organizing Documentation
-------------------------

Page Hierarchy
~~~~~~~~~~~~~~

Maintain your document structure in Confluence:

.. code-block:: python

   confluence_page_hierarchy = True

Your Sphinx toctree structure will be reflected in Confluence:

.. code-block:: rst

   .. toctree::
      :maxdepth: 2
      
      introduction
      installation
      api/index
      tutorials/index

Creates:

::

   Parent Page
   ├── Introduction
   ├── Installation
   ├── API
   │   ├── Module A
   │   └── Module B
   └── Tutorials
       ├── Tutorial 1
       └── Tutorial 2

Page Prefixes
~~~~~~~~~~~~~

Add prefixes to avoid naming conflicts:

.. code-block:: python

   confluence_page_prefix = 'MyProject v2.0 - '

Results in page names like:
- "MyProject v2.0 - Introduction"
- "MyProject v2.0 - Installation"

Custom Parent Page
~~~~~~~~~~~~~~~~~~

Publish under a specific parent:

.. code-block:: python

   confluence_parent_page = 'Engineering Documentation'

Content Features
----------------

Supported Elements
~~~~~~~~~~~~~~~~~~

sphinx-confluence supports most Sphinx/reST features:

✅ **Supported:**
- Headings and text formatting
- Lists (ordered, unordered, definition)
- Tables (including complex tables)
- Code blocks with syntax highlighting
- Images and figures
- Links (internal and external)
- Admonitions (note, warning, tip, etc.)
- Literal blocks
- Line blocks
- Block quotes

⚠️ **Limited Support:**
- Custom directives (may need conversion)
- Some Sphinx domains
- Complex cross-references

❌ **Not Supported:**
- Dynamic content (requires JavaScript)
- Some complex Sphinx extensions

Code Blocks
~~~~~~~~~~~

Code blocks are automatically syntax-highlighted:

.. code-block:: rst

   .. code-block:: python
   
      def hello_world():
          print("Hello, Confluence!")

Set the theme in conf.py:

.. code-block:: python

   confluence_code_block_theme = 'midnight'  # Dark theme
   # Options: default, django, midnight, vibrant ink, etc.

Images and Figures
~~~~~~~~~~~~~~~~~~

Images are uploaded as attachments:

.. code-block:: rst

   .. figure:: images/architecture.png
      :width: 600
      :alt: System Architecture
      
      System architecture diagram

Configure max width:

.. code-block:: python

   confluence_max_image_width = 800

Admonitions
~~~~~~~~~~~

Standard Sphinx admonitions convert to Confluence info/warning panels:

.. code-block:: rst

   .. note::
      This is an informational note.
   
   .. warning::
      This is a warning message.
   
   .. tip::
      This is a helpful tip.

Tables
~~~~~~

Both simple and complex tables work:

.. code-block:: rst

   .. list-table:: API Endpoints
      :header-rows: 1
      :widths: 20 40 40
      
      * - Method
        - Endpoint
        - Description
      * - GET
        - /api/users
        - List all users
      * - POST
        - /api/users
        - Create new user

Workflow Example
----------------

Complete Publishing Workflow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Setup Configuration**

Create ``docs/conf.py``:

.. code-block:: python

   import os
   
   project = 'My Project'
   extensions = ['sphinxcontrib.confluencebuilder']
   
   # Confluence settings
   confluence_publish = True
   confluence_space_name = 'MYSPACE'
   confluence_server_url = 'https://mycompany.atlassian.net/wiki'
   confluence_server_user = os.getenv('CONFLUENCE_USER')
   confluence_server_pass = os.getenv('CONFLUENCE_API_TOKEN')
   confluence_parent_page = 'Project Documentation'
   confluence_page_prefix = 'MyProject - '
   confluence_page_hierarchy = True
   confluence_purge = True
   confluence_purge_from_master = True

2. **Write Documentation**

Create ``docs/index.rst``:

.. code-block:: rst

   My Project Documentation
   =========================
   
   .. toctree::
      :maxdepth: 2
      
      overview
      installation
      usage
      api

3. **Test Locally**

.. code-block:: bash

   # Build HTML first to verify
   docker run --rm -v $(pwd):/project viper-sphinx:latest \
       sphinx-build -b html /project/docs /project/docs/_build/html

4. **Dry Run**

.. code-block:: python

   # Temporarily set in conf.py
   confluence_publish_dryrun = True

.. code-block:: bash

   docker run --rm \
       -e CONFLUENCE_USER=me@example.com \
       -e CONFLUENCE_API_TOKEN=mytoken \
       -v $(pwd):/project \
       viper-sphinx:latest \
       sphinx-build -b confluence /project/docs /project/docs/_build/confluence

5. **Publish**

.. code-block:: python

   # Set in conf.py
   confluence_publish_dryrun = False

.. code-block:: bash

   docker run --rm \
       -e CONFLUENCE_USER=me@example.com \
       -e CONFLUENCE_API_TOKEN=mytoken \
       -v $(pwd):/project \
       viper-sphinx:latest \
       sphinx-build -b confluence /project/docs /project/docs/_build/confluence

Docker Compose Setup
--------------------

Create ``docker-compose.yml``:

.. code-block:: yaml

   version: '3.8'
   
   services:
     confluence-publish:
       image: viper-sphinx:latest
       volumes:
         - ./:/project
       working_dir: /project/docs
       environment:
         - CONFLUENCE_USER=${CONFLUENCE_USER}
         - CONFLUENCE_API_TOKEN=${CONFLUENCE_API_TOKEN}
       command: sphinx-build -b confluence . _build/confluence

Create ``.env`` file:

.. code-block:: text

   CONFLUENCE_USER=your-email@example.com
   CONFLUENCE_API_TOKEN=your-api-token

Run:

.. code-block:: bash

   docker-compose run --rm confluence-publish

CI/CD Integration
-----------------

GitHub Actions Example
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Publish to Confluence
   
   on:
     push:
       branches: [main]
   
   jobs:
     publish:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Build and Publish
           run: |
             docker run --rm \
               -e CONFLUENCE_USER=${{ secrets.CONFLUENCE_USER }} \
               -e CONFLUENCE_API_TOKEN=${{ secrets.CONFLUENCE_TOKEN }} \
               -v $(pwd):/project \
               viper-sphinx:latest \
               sphinx-build -b confluence /project/docs /project/docs/_build/confluence

GitLab CI Example
~~~~~~~~~~~~~~~~~

.. code-block:: yaml

   publish-confluence:
     image: viper-sphinx:latest
     script:
       - sphinx-build -b confluence docs docs/_build/confluence
     variables:
       CONFLUENCE_USER: $CONFLUENCE_USER
       CONFLUENCE_API_TOKEN: $CONFLUENCE_API_TOKEN
     only:
       - main

Best Practices
--------------

1. **Use Environment Variables** for credentials, never commit them
2. **Test with Dry Run** before publishing to production
3. **Use Page Prefixes** to organize and version documentation
4. **Enable Purging** to remove outdated pages automatically
5. **Maintain Hierarchy** to reflect your documentation structure
6. **Version Control** - keep Confluence in sync with your repo
7. **Review Permissions** - ensure correct access in Confluence space

Troubleshooting
---------------

Authentication Fails
~~~~~~~~~~~~~~~~~~~~

.. code-block:: text

   Error: 401 Unauthorized

**Solutions:**
- Verify API token is correct
- Check username matches token owner
- Ensure user has space permissions
- For Confluence Cloud, use email as username

Pages Not Updating
~~~~~~~~~~~~~~~~~~

.. code-block:: text

   Pages exist but don't update

**Solutions:**
- Set ``confluence_asset_override = True``
- Enable ``confluence_purge = True``
- Check page permissions in Confluence

SSL Certificate Errors
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text

   SSL verification failed

**Solutions:**
- For testing only: ``confluence_disable_ssl_validation = True``
- Better: Install proper certificates
- Check corporate proxy settings

Missing Images
~~~~~~~~~~~~~~

**Solutions:**
- Verify image paths are correct
- Check ``confluence_asset_override = True``
- Ensure images are in accessible location
- Set appropriate ``confluence_max_image_width``

Common Configuration
--------------------

Complete Example
~~~~~~~~~~~~~~~~

.. code-block:: python

   # docs/conf.py
   import os
   from datetime import datetime
   
   # Project information
   project = 'My Project'
   copyright = f'{datetime.now().year}, My Company'
   version = '2.0'
   
   # Extensions
   extensions = [
       'sphinxcontrib.confluencebuilder',
       'sphinx.ext.autodoc',
       'sphinx.ext.intersphinx',
   ]
   
   # Confluence configuration
   confluence_publish = True
   confluence_space_name = 'PROJ'
   confluence_server_url = 'https://company.atlassian.net/wiki'
   confluence_server_user = os.getenv('CONFLUENCE_USER')
   confluence_server_pass = os.getenv('CONFLUENCE_API_TOKEN')
   
   # Publishing options
   confluence_parent_page = 'Product Documentation'
   confluence_page_prefix = f'{project} {version} - '
   confluence_page_hierarchy = True
   confluence_purge = True
   confluence_purge_from_master = True
   
   # Content options
   confluence_max_image_width = 800
   confluence_code_block_theme = 'midnight'
   confluence_remove_title = False
   
   # Debug
   confluence_publish_debug = False
   confluence_publish_dryrun = False


Practical Examples
------------------

Confluence Output
~~~~~~~~~~~~~~~~~

When published to Confluence, this page appears with:

- **Styled Headers**: Each heading level properly formatted
- **Lists**: Bullet points and numbered lists preserved
- **Code Blocks**: Syntax-highlighted code with proper formatting
- **Admonitions**: Note/Warning/Tip boxes styled as Confluence panels
- **Cross-References**: Links to other documentation pages
- **Navigation**: Automatic breadcrumbs and child page links

Example: Code Documentation
----------------------------

Source RST with API Docs
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   API Reference
   =============
   
   Core Module
   -----------
   
   .. automodule:: product_sdk.core
      :members:
      :undoc-members:
      :show-inheritance:
   
   Example Usage
   ~~~~~~~~~~~~~
   
   Here's how to use the core functionality:
   
   .. code-block:: python
   
      from product_sdk import Client
      
      # Initialize client
      client = Client(api_key='your-key')
      
      # Fetch data
      data = client.get_data(id=123)
      print(data)
   
   Parameters
   ~~~~~~~~~~
   
   .. list-table::
      :header-rows: 1
      :widths: 20 20 60
   
      * - Parameter
        - Type
        - Description
      * - api_key
        - string
        - Your API authentication key
      * - timeout
        - int
        - Request timeout in seconds (default: 30)
      * - retry
        - bool
        - Enable automatic retry (default: True)

Confluence Rendering
~~~~~~~~~~~~~~~~~~~~

The published Confluence page includes:

- **API Documentation**: Class and method signatures with descriptions
- **Code Examples**: Syntax-highlighted Python code blocks
- **Tables**: Properly formatted parameter tables
- **Type Information**: Parameter types and return types
- **Links**: Cross-references to related API elements

Example: Build and Publish Commands
------------------------------------

Local Testing
~~~~~~~~~~~~~

Build Confluence output locally without publishing:

.. code-block:: bash

   # Build to see what will be published
   docker run --rm -v $(pwd):/project viper-sphinx:latest \
       sphinx-build -b confluence /project/docs /project/build/confluence

This creates Confluence storage format files in ``build/confluence/`` for review.

Publishing to Confluence
~~~~~~~~~~~~~~~~~~~~~~~~

Publish documentation to Confluence server:

.. code-block:: bash

   # Set authentication
   export CONFLUENCE_USER="your-email@example.com"
   export CONFLUENCE_API_TOKEN="your-api-token"
   
   # Build and publish
   docker run --rm \
       -e CONFLUENCE_USER \
       -e CONFLUENCE_API_TOKEN \
       -v $(pwd):/project \
       viper-sphinx:latest \
       sphinx-build -b confluence /project/docs /project/build/confluence

Dry Run
~~~~~~~

Test without actually publishing:

.. code-block:: bash

   docker run --rm -v $(pwd):/project viper-sphinx:latest \
       sphinx-build -b confluence -D confluence_publish=False \
       /project/docs /project/build/confluence

Example: Advanced Features
---------------------------

Including Attachments
~~~~~~~~~~~~~~~~~~~~~

Images and files are automatically uploaded as attachments:

.. code-block:: rst

   Architecture Diagram
   --------------------
   
   .. image:: _static/architecture.png
      :width: 600px
      :alt: System Architecture
   
   Download the :download:`configuration template <_static/config.yaml>`.

The image and YAML file are uploaded to Confluence and linked automatically.

Confluence Macros
~~~~~~~~~~~~~~~~~

Insert native Confluence macros:

.. code-block:: rst

   .. confluence_macro::
      :name: info
      :title: Important Information
   
      This content appears in a Confluence info panel.
   
   .. confluence_macro::
      :name: toc
      :maxLevel: 3

Page Metadata
~~~~~~~~~~~~~

Control page-specific settings:

.. code-block:: rst

   .. confluence_metadata::
      :labels: api, reference, v1.0
      :editor: v2
   
   API Reference
   =============
   
   This page has custom labels and uses the Confluence v2 editor.

Example Output Features
-----------------------

When your documentation is published to Confluence, users see:

✅ **Professional Formatting**
   - Clean, consistent styling
   - Proper heading hierarchy
   - Readable code blocks with syntax highlighting

✅ **Interactive Elements**
   - Expandable sections
   - Tabbed content
   - Interactive tables of contents

✅ **Collaborative Features**
   - Comments on pages
   - Page ratings
   - Watch notifications
   - Version history

✅ **Search Integration**
   - Full-text search across documentation
   - Confluence's powerful search filters
   - Quick access from anywhere in Confluence

✅ **Access Control**
   - Leverage Confluence's permission system
   - Space-level and page-level restrictions
   - Integration with corporate SSO

Publishing Workflow
-------------------

A typical publishing workflow:

.. code-block:: bash

   #!/bin/bash
   # publish-docs.sh
   
   set -e
   
   echo "Building documentation..."
   sphinx-build -b confluence docs/ build/confluence
   
   echo "Running pre-publish checks..."
   # Validate links, images, etc.
   
   echo "Publishing to Confluence..."
   # Authentication via environment variables
   sphinx-build -b confluence \
       -D confluence_publish=True \
       docs/ build/confluence
   
   echo "✅ Documentation published successfully!"
   echo "View at: https://yourcompany.atlassian.net/wiki/spaces/DOCS"

Learn More
----------

For detailed configuration and usage instructions, see:

- :doc:`../tutorials/packages/sphinx-confluence` - Complete tutorial
- `Confluence Builder Documentation <https://sphinxcontrib-confluencebuilder.readthedocs.io/>`_
- `Atlassian Confluence API <https://developer.atlassian.com/cloud/confluence/rest/>`_

Additional Resources
--------------------

- `Confluence Builder Documentation <https://sphinxcontrib-confluencebuilder.readthedocs.io/>`_
- `Confluence REST API <https://developer.atlassian.com/cloud/confluence/rest/>`_
- `Generating API Tokens <https://id.atlassian.com/manage-profile/security/api-tokens>`_
- :doc:`../sphinx-basics` - Learn more about Sphinx
- :doc:`../extensions` - Other useful extensions

Next Steps
----------

1. Set up your Confluence space and get API credentials
2. Configure ``conf.py`` with your Confluence settings
3. Do a dry run to verify the output
4. Publish your first documentation set
5. Integrate into your CI/CD pipeline
