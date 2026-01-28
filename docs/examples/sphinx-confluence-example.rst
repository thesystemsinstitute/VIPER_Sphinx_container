Sphinx-Confluence Example
=========================

This page demonstrates example output and configuration for **sphinx-confluence**, showing how Sphinx documentation can be published to Atlassian Confluence.

Overview
--------

When you use sphinx-confluence to publish documentation to Confluence, your reStructuredText files are converted into Confluence's storage format (XHTML). This example shows what various Sphinx elements look like when published.

Example Configuration
---------------------

Here's a complete ``conf.py`` setup for publishing to Confluence Cloud:

.. code-block:: python

   # Project information
   project = 'Product Documentation'
   copyright = '2026, Your Company'
   author = 'Documentation Team'
   version = '1.0'
   release = '1.0.0'
   
   # Extensions
   extensions = [
       'sphinxcontrib.confluencebuilder',
       'sphinx.ext.autodoc',
       'sphinx.ext.intersphinx',
   ]
   
   # Confluence Configuration
   confluence_publish = True
   confluence_space_name = 'DOCS'
   confluence_server_url = 'https://yourcompany.atlassian.net/wiki'
   confluence_parent_page = 'Product Documentation Home'
   
   # Authentication (use environment variables for security)
   import os
   confluence_server_user = os.getenv('CONFLUENCE_USER')
   confluence_server_pass = os.getenv('CONFLUENCE_API_TOKEN')
   
   # Publishing options
   confluence_page_hierarchy = True
   confluence_publish_prefix = 'v1.0'
   confluence_publish_postfix = ''
   confluence_ask_user = False
   confluence_ask_password = False
   
   # Content options
   confluence_max_doc_depth = 2
   confluence_root_homepage = True
   confluence_title_overrides = {
       'index': 'Product Documentation v1.0',
   }

Example Documentation Structure
--------------------------------

When published to Confluence, this documentation structure:

.. code-block:: text

   docs/
   ├── index.rst              → Home page in Confluence
   ├── installation.rst       → Installation Guide (child page)
   ├── user-guide/
   │   ├── index.rst         → User Guide (child page)
   │   ├── getting-started.rst → Getting Started (grandchild)
   │   └── advanced.rst      → Advanced Features (grandchild)
   └── api/
       ├── index.rst         → API Reference (child page)
       └── modules.rst       → Modules (grandchild)

Becomes this Confluence hierarchy:

.. code-block:: text

   📄 Product Documentation v1.0 (Home)
   ├── 📄 Installation Guide
   ├── 📁 User Guide
   │   ├── 📄 Getting Started
   │   └── 📄 Advanced Features
   └── 📁 API Reference
       └── 📄 Modules

Example: Publishing a Page
---------------------------

Source RST
~~~~~~~~~~

Here's what a typical documentation page looks like in reStructuredText:

.. code-block:: rst

   Installation Guide
   ==================
   
   This guide covers installing the Product SDK.
   
   Prerequisites
   -------------
   
   Before you begin, ensure you have:
   
   * Python 3.8 or later
   * pip package manager
   * Virtual environment (recommended)
   
   Quick Install
   -------------
   
   Install using pip:
   
   .. code-block:: bash
   
      pip install product-sdk
   
   Verify Installation
   -------------------
   
   Test your installation:
   
   .. code-block:: python
   
      import product_sdk
      print(product_sdk.__version__)
   
   Expected output::
   
      1.0.0
   
   .. note::
   
      If you encounter issues, see :doc:`troubleshooting`.
   
   Next Steps
   ----------
   
   Continue to the :doc:`user-guide/getting-started` guide.

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
   docker run --rm -v $(pwd):/project kensai-sphinx:latest \
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
       kensai-sphinx:latest \
       sphinx-build -b confluence /project/docs /project/build/confluence

Dry Run
~~~~~~~

Test without actually publishing:

.. code-block:: bash

   docker run --rm -v $(pwd):/project kensai-sphinx:latest \
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
