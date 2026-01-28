Sphinx-Version-Warning Tutorial
================================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-version-warning/>`_
   - `API Documentation <../../pdoc/sphinx_version_warning/index.html>`_
   - `Manual <https://github.com/humitos/sphinx-version-warning>`_
   - :doc:`Working Example <../../examples/sphinx-version-warning-example>`


.. contents:: Table of Contents
   :local:
   :depth: 2

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

The sphinx-version-warning extension displays a banner warning users when they're viewing outdated documentation versions.


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
