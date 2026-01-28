Sphinx-Version-Warning Tutorial
================================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-version-warning/>`_
   - `Official Documentation <https://sphinx-version-warning.readthedocs.io/>`_
   - :doc:`See Working Example <../../examples/sphinx-version-warning-example>`


This tutorial demonstrates how to use sphinx-version-warning to display version warnings in your documentation.

What is Sphinx-Version-Warning?
--------------------------------

sphinx-version-warning is a Sphinx extension that provides:

- Version warning banners
- Latest version notifications
- Outdated documentation alerts
- Custom warning messages
- Automatic version detection
- Configurable styling
- Multiple version support
- Read the Docs integration
- User-friendly alerts
- Version comparison

This helps users know when they're viewing outdated documentation and directs them to the latest version.

Installation
------------

sphinx-version-warning is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import versionwarning.extension; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'versionwarning.extension',
   ]
   
   # Version warning configuration
   versionwarning_admonition_type = 'warning'
   versionwarning_banner_title = 'Outdated Documentation'
   versionwarning_messages = {
       'latest': 'You are reading the latest version.',
       'stable': 'This is the stable version.',
   }

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['versionwarning.extension']
   
   # Project version
   version = '1.2'
   release = '1.2.3'
   
   # Warning configuration
   versionwarning_admonition_type = 'warning'  # note, warning, tip, etc.
   versionwarning_banner_title = 'Documentation Version'
   
   # Custom messages per version
   versionwarning_messages = {
       'latest': 'This is the latest development version.',
       'stable': 'This is the latest stable release.',
       '1.x': 'This is an older version. Please upgrade to 2.x.',
       'dev': 'This is unreleased development documentation.',
   }
   
   # Message for unknown versions
   versionwarning_message_placeholder = (
       'You are viewing documentation for version {version}. '
       'The latest version is {latest}.'
   )
   
   # Body text
   versionwarning_body_selector = 'div.body'
   
   # API endpoint for latest version
   versionwarning_api_url = 'https://api.example.com/latest-version'
   
   # Project URLs
   versionwarning_project_slug = 'myproject'
   versionwarning_project_version = version

Basic Usage
-----------

Automatic Warning Display
~~~~~~~~~~~~~~~~~~~~~~~~~~

Once configured, warnings appear automatically on all pages when viewing older versions.

The warning looks like:

.. code-block:: text

   ⚠ Documentation Version
   
   You are viewing documentation for version 1.0.
   The latest version is 2.0.
   
   [View Latest Documentation]

Practical Examples
------------------

Example 1: Simple Version Warning
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/conf.py``:

.. code-block:: python

   extensions = ['versionwarning.extension']
   
   # Project version
   version = '1.0'
   release = '1.0.5'
   
   # Simple warning
   versionwarning_admonition_type = 'warning'
   versionwarning_banner_title = 'Outdated Version'
   versionwarning_messages = {
       'latest': (
           'You are viewing the latest documentation. '
           'Everything here is current!'
       ),
       '1.x': (
           'This is version 1.x documentation. '
           'Version 2.x is now available with many improvements.'
       ),
   }

Example 2: Comprehensive Version System
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/conf.py``:

.. code-block:: python

   import os
   
   extensions = ['versionwarning.extension']
   
   # Detect version from environment or file
   version = os.environ.get('DOC_VERSION', '2.1')
   release = version
   
   # Detailed version warnings
   versionwarning_admonition_type = 'tip'
   versionwarning_banner_title = 'Documentation Version Notice'
   
   versionwarning_messages = {
       'latest': (
           '✅ <strong>Latest Version</strong><br>'
           'You are viewing the most recent documentation. '
           'This includes all the newest features and updates.'
       ),
       'stable': (
           '✅ <strong>Stable Release</strong><br>'
           'This is the latest stable version recommended for production use.'
       ),
       '2.x': (
           '📌 <strong>Version 2.x</strong><br>'
           'You are viewing documentation for version 2.x. '
           'This is a stable release branch.'
       ),
       '1.x': (
           '⚠️ <strong>Legacy Version</strong><br>'
           'This is version 1.x documentation. While still supported, '
           'we recommend upgrading to version 2.x for new features and improvements. '
           '<a href="/en/stable/">View latest stable docs</a>'
       ),
       'dev': (
           '🚧 <strong>Development Version</strong><br>'
           'This documentation is for unreleased features. '
           'Content may change without notice. '
           'Use at your own risk!'
       ),
   }
   
   # Placeholder for versions not explicitly defined
   versionwarning_message_placeholder = (
       '📖 You are viewing documentation for version <strong>{version}</strong>. '
       'The latest stable version is <strong>{latest}</strong>. '
       '<a href="/en/{latest}/">Switch to latest</a>'
   )

Example 3: Read the Docs Integration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/conf.py``:

.. code-block:: python

   import os
   
   extensions = ['versionwarning.extension']
   
   # Read the Docs environment
   on_rtd = os.environ.get('READTHEDOCS') == 'True'
   rtd_version = os.environ.get('READTHEDOCS_VERSION', 'latest')
   
   if on_rtd:
       version = rtd_version
       release = rtd_version
   else:
       version = '2.0'
       release = '2.0.0'
   
   # Configure warnings
   versionwarning_admonition_type = 'warning'
   versionwarning_banner_title = 'Version Notice'
   
   versionwarning_messages = {
       'latest': 'You are reading the latest development version.',
       'stable': 'You are reading the stable documentation.',
   }
   
   # For Read the Docs
   versionwarning_project_slug = 'myproject'
   versionwarning_project_version = rtd_version

Example 4: Custom Styled Banner
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/conf.py``:

.. code-block:: python

   versionwarning_admonition_type = 'note'
   versionwarning_banner_title = ''  # No title, custom HTML
   
   versionwarning_messages = {
       'latest': '''
           <div class="version-banner version-latest">
               <span class="version-icon">✨</span>
               <div class="version-content">
                   <h3>Latest Development Version</h3>
                   <p>You're viewing cutting-edge documentation. Features may change.</p>
               </div>
           </div>
       ''',
       'stable': '''
           <div class="version-banner version-stable">
               <span class="version-icon">✅</span>
               <div class="version-content">
                   <h3>Stable Release</h3>
                   <p>Recommended for production use.</p>
               </div>
           </div>
       ''',
   }

``docs/_static/version-banner.css``:

.. code-block:: css

   .version-banner {
       display: flex;
       align-items: center;
       padding: 15px 20px;
       border-radius: 8px;
       margin: 20px 0;
       gap: 15px;
   }
   
   .version-banner.version-latest {
       background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
       color: white;
   }
   
   .version-banner.version-stable {
       background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
       color: white;
   }
   
   .version-icon {
       font-size: 32px;
   }
   
   .version-content h3 {
       margin: 0 0 5px 0;
       font-size: 18px;
       font-weight: bold;
   }
   
   .version-content p {
       margin: 0;
       font-size: 14px;
       opacity: 0.9;
   }

``docs/conf.py``:

.. code-block:: python

   html_css_files = ['version-banner.css']

Advanced Features
-----------------

Dynamic Version Detection
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import subprocess
   
   def get_git_version():
       """Get version from git tags."""
       try:
           tag = subprocess.check_output(
               ['git', 'describe', '--tags', '--abbrev=0'],
               stderr=subprocess.DEVNULL
           ).decode().strip()
           return tag
       except:
           return 'dev'
   
   version = get_git_version()

API-Based Latest Version
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import requests
   
   def get_latest_version():
       """Fetch latest version from API."""
       try:
           resp = requests.get('https://api.github.com/repos/user/repo/releases/latest')
           return resp.json()['tag_name']
       except:
           return 'unknown'
   
   latest_version = get_latest_version()
   
   versionwarning_message_placeholder = (
       f'Current: {{version}} | Latest: {latest_version}'
   )

Conditional Warnings
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Only show warning for old versions
   from packaging import version as pkg_version
   
   if pkg_version.parse(version) < pkg_version.parse('2.0'):
       versionwarning_admonition_type = 'danger'
   else:
       versionwarning_admonition_type = 'tip'

Docker Integration
------------------

Build with Version Warning
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     -e DOC_VERSION=1.0 \
     kensai-sphinx:latest \
     sphinx-build -b html /project/docs /project/docs/_build/html

Multi-Version Build
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   #!/bin/bash
   
   versions=("1.0" "2.0" "latest")
   
   for ver in "${versions[@]}"; do
     docker run --rm \
       -v $(pwd):/project \
       -e DOC_VERSION=$ver \
       kensai-sphinx:latest \
       sphinx-build -b html /project/docs /project/docs/_build/html/$ver
   done

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Build Versioned Docs
   
   on:
     push:
       tags:
         - 'v*'
   
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Get Version
           id: version
           run: echo "VERSION=${GITHUB_REF#refs/tags/v}" >> $GITHUB_OUTPUT
         
         - name: Build Documentation
           env:
             DOC_VERSION: ${{ steps.version.outputs.VERSION }}
           run: |
             docker run --rm \
               -v $(pwd):/project \
               -e DOC_VERSION=$DOC_VERSION \
               kensai-sphinx:latest \
               sphinx-build -b html /project/docs /project/docs/_build/html
         
         - name: Deploy
           uses: peaceiris/actions-gh-pages@v3
           with:
             github_token: ${{ secrets.GITHUB_TOKEN }}
             publish_dir: ./docs/_build/html
             destination_dir: ${{ steps.version.outputs.VERSION }}

Best Practices
--------------

1. **Clear Messages**
   
   Make version status obvious

2. **Provide Links**
   
   Direct users to latest docs

3. **Use Appropriate Types**
   
   danger for old, tip for latest

4. **Test All Versions**
   
   Verify warnings display correctly

5. **Keep Updated**
   
   Update messages when releasing

6. **Consider Users**
   
   Balance helpfulness vs annoyance

Troubleshooting
---------------

Warning Not Showing
~~~~~~~~~~~~~~~~~~~

**Solution:**

Check extension is loaded:

.. code-block:: python

   extensions = ['versionwarning.extension']

Verify version is set:

.. code-block:: python

   print(f"Building version: {version}")

Wrong Message Displayed
~~~~~~~~~~~~~~~~~~~~~~~~

**Solution:**

Check version matching:

.. code-block:: python

   # Version '2.0.5' matches pattern '2.x'
   versionwarning_messages = {
       '2.x': 'Version 2 message',
   }

Styling Issues
~~~~~~~~~~~~~~

**Solution:**

Override CSS:

.. code-block:: css

   .versionwarning {
       background-color: #fff3cd !important;
   }

Multiple Warnings
~~~~~~~~~~~~~~~~~

**Solution:**

Use more specific version patterns:

.. code-block:: python

   versionwarning_messages = {
       '2.1': 'Specific message for 2.1',
       '2.x': 'General message for 2.x',
   }

Next Steps
----------

1. Configure version detection
2. Set up warning messages
3. Test different versions
4. Style the warnings
5. Deploy versioned docs

Additional Resources
--------------------

- :doc:`sphinx-notfound-page` - Custom 404 pages
- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `sphinx-version-warning Documentation <https://github.com/humitos/sphinx-version-warning>`_
- `Read the Docs Versioning <https://docs.readthedocs.io/en/stable/versions.html>`_
