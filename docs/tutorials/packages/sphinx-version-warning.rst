Sphinx-Version-Warning Tutorial
================================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-version-warning/>`_
   - `API Documentation <../../pdoc/sphinx_version_warning/index.html>`_
   - `Manual <https://github.com/humitos/sphinx-version-warning>`_

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


Practical Examples
------------------

Basic Configuration
-------------------

Setup
~~~~~

.. code-block:: python

   # conf.py
   extensions = [
       'versionwarning.extension',
   ]
   
   # Current version
   version = '2.0'
   release = '2.0.1'

Version Warning Message
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   versionwarning_messages = {
       'latest': 'This is the development version!',
       'stable': '',  # No warning for stable
   }

Banner Configuration
--------------------

Message Types
~~~~~~~~~~~~~

.. code-block:: python

   versionwarning_messages = {
       # Development version warning
       'latest': '''
           You are viewing the <strong>development</strong> version.
           <a href="/en/stable/">Switch to stable version</a>
       ''',
       
       # Specific version warnings
       '1.0': '''
           This version is outdated.
           <a href="/en/latest/">View latest</a>
       ''',
       
       # No warning for current stable
       '2.0': '',
   }

Default Message
~~~~~~~~~~~~~~~

.. code-block:: python

   # Message for versions not explicitly defined
   versionwarning_default_message = '''
       This is an old version of the documentation.
       <a href="/en/stable/">Go to latest stable</a>
   '''

Banner Styling
--------------

Custom Colors
~~~~~~~~~~~~~

.. code-block:: python

   versionwarning_banner_html = '''
       <div class="version-warning" style="
           background-color: #ffeb3b;
           color: #000;
           padding: 10px;
           text-align: center;
           border-bottom: 2px solid #ffc107;
       ">
           {message}
       </div>
   '''

Theme Integration
~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Use theme colors
   versionwarning_banner_html = '''
       <div class="admonition warning version-warning">
           <p class="admonition-title">Version Warning</p>
           <p>{message}</p>
       </div>
   '''

Custom CSS
~~~~~~~~~~

.. code-block:: css

   /* custom.css */
   .version-warning {
       background: linear-gradient(to right, #ff6b6b, #feca57);
       color: white;
       padding: 15px;
       text-align: center;
       font-weight: bold;
       border-left: 5px solid #ee5a24;
   }
   
   .version-warning a {
       color: white;
       text-decoration: underline;
   }

Version Detection
-----------------

Read the Docs Integration
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   import os
   
   # Detect RTD environment
   on_rtd = os.environ.get('READTHEDOCS') == 'True'
   
   if on_rtd:
       rtd_version = os.environ.get('READTHEDOCS_VERSION', 'unknown')
       
       versionwarning_messages = {
           'latest': 'Development version - may be unstable',
           'stable': '',
       }
       
       # Set message based on RTD version
       if rtd_version not in ['stable', 'latest']:
           versionwarning_default_message = f'''
               You are viewing documentation for version {rtd_version}.
               <a href="/en/stable/">View stable version</a>
           '''

GitHub Pages
~~~~~~~~~~~~

.. code-block:: python

   # Detect from build context
   import subprocess
   
   try:
       git_branch = subprocess.check_output(
           ['git', 'rev-parse', '--abbrev-ref', 'HEAD']
       ).decode().strip()
       
       if git_branch == 'develop':
           versionwarning_messages['latest'] = 'Development branch'
   except:
       pass

Version Comparison
------------------

Semantic Versioning
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from packaging import version
   
   current_version = version.parse(release)
   latest_version = version.parse('2.1.0')
   
   if current_version < latest_version:
       versionwarning_default_message = f'''
           This is version {release}.
           Version {latest_version} is available.
       '''

Custom Logic
~~~~~~~~~~~~

.. code-block:: python

   def get_version_message(current_ver):
       """Generate version warning based on age."""
       if current_ver.startswith('0.'):
           return 'Pre-release version'
       elif current_ver.startswith('1.'):
           return 'Version 1.x is deprecated. Upgrade to 2.x'
       return ''
   
   versionwarning_default_message = get_version_message(version)

Multi-Version Setup
-------------------

Version Switcher
~~~~~~~~~~~~~~~~

.. code-block:: python

   versionwarning_banner_html = '''
       <div class="version-banner">
           <span>{message}</span>
           <select onchange="location.href=this.value">
               <option value="/en/stable/">Stable (2.0)</option>
               <option value="/en/latest/">Latest (dev)</option>
               <option value="/en/1.9/">1.9</option>
               <option value="/en/1.8/">1.8</option>
           </select>
       </div>
   '''

Version Links
~~~~~~~~~~~~~

.. code-block:: python

   versionwarning_messages = {
       'latest': '''
           Development version.
           <a href="/en/stable/">Stable</a> |
           <a href="/en/2.0/">2.0</a> |
           <a href="/en/1.9/">1.9</a>
       ''',
   }

Conditional Warnings
--------------------

By Page Type
~~~~~~~~~~~~

.. code-block:: python

   # In conf.py or custom extension
   def add_version_warning(app, pagename, templatename, context, doctree):
       """Add version warning based on page type."""
       if pagename.startswith('api/'):
           context['versionwarning_message'] = 'API may change!'
   
   def setup(app):
       app.connect('html-page-context', add_version_warning)

By Section
~~~~~~~~~~

.. code-block:: python

   versionwarning_messages = {
       'latest': {
           'default': 'Development version',
           'api': 'API is unstable',
           'tutorials': 'Tutorials may be incomplete',
       }
   }

Practical Examples
------------------

Simple Warning
~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   extensions = ['versionwarning.extension']
   
   version = '1.5'
   
   versionwarning_messages = {
       '1.5': '''
           This version is deprecated.
           <a href="/en/latest/">View latest documentation</a>
       ''',
   }

Development Branch
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import os
   
   on_develop = os.environ.get('BRANCH') == 'develop'
   
   if on_develop:
       versionwarning_messages = {
           'latest': '''
               <strong>⚠️ Development Version</strong><br>
               This documentation may contain unreleased features.
               <a href="/en/stable/">View stable version</a>
           '''
       }

EOL Warning
~~~~~~~~~~~

.. code-block:: python

   # End-of-life version
   from datetime import datetime
   
   eol_date = datetime(2024, 12, 31)
   
   if datetime.now() > eol_date:
       versionwarning_default_message = '''
           <strong>⚠️ End of Life</strong><br>
           This version is no longer supported.
           Please upgrade to a supported version.
       '''

Beta Warning
~~~~~~~~~~~~

.. code-block:: python

   if 'beta' in release.lower():
       versionwarning_messages['latest'] = '''
           <strong>🚧 Beta Version</strong><br>
           This is a pre-release version. Use with caution.
           <a href="/en/stable/">Stable version</a>
       '''

Advanced Features
-----------------

JavaScript Integration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: html

   <script>
   // Auto-redirect old versions
   (function() {
       const version = '1.5';
       const currentVersion = '2.0';
       
       if (version !== currentVersion) {
           const redirect = confirm(
               'This documentation is outdated. ' +
               'Would you like to view the latest version?'
           );
           if (redirect) {
               window.location.href = '/en/latest/';
           }
       }
   })();
   </script>

Cookie-Based Dismissal
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: html

   <div id="version-warning" class="version-warning">
       {message}
       <button onclick="dismissWarning()">×</button>
   </div>
   
   <script>
   function dismissWarning() {
       document.cookie = 'version_warning_dismissed=1;max-age=86400';
       document.getElementById('version-warning').style.display = 'none';
   }
   
   if (document.cookie.includes('version_warning_dismissed=1')) {
       document.getElementById('version-warning').style.display = 'none';
   }
   </script>

Testing
-------

Local Testing
~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   # Force version for testing
   version = '1.0'  # Old version
   
   versionwarning_messages = {
       '1.0': 'This should show a warning',
       '2.0': '',  # Current, no warning
   }

Build Validation
~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Build docs for different versions
   VERSION=1.0 sphinx-build docs docs/_build/v1.0
   VERSION=2.0 sphinx-build docs docs/_build/v2.0
   
   # Check for warning banner
   grep "version-warning" docs/_build/v1.0/index.html

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Build Docs
   
   on:
     push:
       branches: [main, develop]
       tags: ['v*']
   
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v2
         
         - name: Determine version
           id: version
           run: |
             if [[ "$GITHUB_REF" == refs/tags/* ]]; then
               echo "VERSION=${GITHUB_REF#refs/tags/v}" >> $GITHUB_OUTPUT
             else
               echo "VERSION=latest" >> $GITHUB_OUTPUT
             fi
         
         - name: Build docs
           run: |
             sphinx-build -D version=${{ steps.version.outputs.VERSION }} \
                          docs docs/_build

Best Practices
--------------

Message Content
~~~~~~~~~~~~~~~

1. Be clear and concise
2. Provide actionable links
3. Use appropriate urgency
4. Match your brand voice
5. Consider translations

Version Strategy
~~~~~~~~~~~~~~~~

1. Maintain multiple versions
2. Clear stable/dev distinction
3. Document version policy
4. Deprecation warnings
5. Migration guides

User Experience
~~~~~~~~~~~~~~~

1. Don't be too intrusive
2. Allow dismissal option
3. Provide version switcher
4. Mobile-friendly design
5. Accessible markup


Practical Examples
------------------

Basic Configuration
-------------------

Setup
~~~~~

.. code-block:: python

   # conf.py
   extensions = [
       'versionwarning.extension',
   ]
   
   # Current version
   version = '2.0'
   release = '2.0.1'

Version Warning Message
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   versionwarning_messages = {
       'latest': 'This is the development version!',
       'stable': '',  # No warning for stable
   }

Banner Configuration
--------------------

Message Types
~~~~~~~~~~~~~

.. code-block:: python

   versionwarning_messages = {
       # Development version warning
       'latest': '''
           You are viewing the <strong>development</strong> version.
           <a href="/en/stable/">Switch to stable version</a>
       ''',
       
       # Specific version warnings
       '1.0': '''
           This version is outdated.
           <a href="/en/latest/">View latest</a>
       ''',
       
       # No warning for current stable
       '2.0': '',
   }

Default Message
~~~~~~~~~~~~~~~

.. code-block:: python

   # Message for versions not explicitly defined
   versionwarning_default_message = '''
       This is an old version of the documentation.
       <a href="/en/stable/">Go to latest stable</a>
   '''

Banner Styling
--------------

Custom Colors
~~~~~~~~~~~~~

.. code-block:: python

   versionwarning_banner_html = '''
       <div class="version-warning" style="
           background-color: #ffeb3b;
           color: #000;
           padding: 10px;
           text-align: center;
           border-bottom: 2px solid #ffc107;
       ">
           {message}
       </div>
   '''

Theme Integration
~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Use theme colors
   versionwarning_banner_html = '''
       <div class="admonition warning version-warning">
           <p class="admonition-title">Version Warning</p>
           <p>{message}</p>
       </div>
   '''

Custom CSS
~~~~~~~~~~

.. code-block:: css

   /* custom.css */
   .version-warning {
       background: linear-gradient(to right, #ff6b6b, #feca57);
       color: white;
       padding: 15px;
       text-align: center;
       font-weight: bold;
       border-left: 5px solid #ee5a24;
   }
   
   .version-warning a {
       color: white;
       text-decoration: underline;
   }

Version Detection
-----------------

Read the Docs Integration
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   import os
   
   # Detect RTD environment
   on_rtd = os.environ.get('READTHEDOCS') == 'True'
   
   if on_rtd:
       rtd_version = os.environ.get('READTHEDOCS_VERSION', 'unknown')
       
       versionwarning_messages = {
           'latest': 'Development version - may be unstable',
           'stable': '',
       }
       
       # Set message based on RTD version
       if rtd_version not in ['stable', 'latest']:
           versionwarning_default_message = f'''
               You are viewing documentation for version {rtd_version}.
               <a href="/en/stable/">View stable version</a>
           '''

GitHub Pages
~~~~~~~~~~~~

.. code-block:: python

   # Detect from build context
   import subprocess
   
   try:
       git_branch = subprocess.check_output(
           ['git', 'rev-parse', '--abbrev-ref', 'HEAD']
       ).decode().strip()
       
       if git_branch == 'develop':
           versionwarning_messages['latest'] = 'Development branch'
   except:
       pass

Version Comparison
------------------

Semantic Versioning
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from packaging import version
   
   current_version = version.parse(release)
   latest_version = version.parse('2.1.0')
   
   if current_version < latest_version:
       versionwarning_default_message = f'''
           This is version {release}.
           Version {latest_version} is available.
       '''

Custom Logic
~~~~~~~~~~~~

.. code-block:: python

   def get_version_message(current_ver):
       """Generate version warning based on age."""
       if current_ver.startswith('0.'):
           return 'Pre-release version'
       elif current_ver.startswith('1.'):
           return 'Version 1.x is deprecated. Upgrade to 2.x'
       return ''
   
   versionwarning_default_message = get_version_message(version)

Multi-Version Setup
-------------------

Version Switcher
~~~~~~~~~~~~~~~~

.. code-block:: python

   versionwarning_banner_html = '''
       <div class="version-banner">
           <span>{message}</span>
           <select onchange="location.href=this.value">
               <option value="/en/stable/">Stable (2.0)</option>
               <option value="/en/latest/">Latest (dev)</option>
               <option value="/en/1.9/">1.9</option>
               <option value="/en/1.8/">1.8</option>
           </select>
       </div>
   '''

Version Links
~~~~~~~~~~~~~

.. code-block:: python

   versionwarning_messages = {
       'latest': '''
           Development version.
           <a href="/en/stable/">Stable</a> |
           <a href="/en/2.0/">2.0</a> |
           <a href="/en/1.9/">1.9</a>
       ''',
   }

Conditional Warnings
--------------------

By Page Type
~~~~~~~~~~~~

.. code-block:: python

   # In conf.py or custom extension
   def add_version_warning(app, pagename, templatename, context, doctree):
       """Add version warning based on page type."""
       if pagename.startswith('api/'):
           context['versionwarning_message'] = 'API may change!'
   
   def setup(app):
       app.connect('html-page-context', add_version_warning)

By Section
~~~~~~~~~~

.. code-block:: python

   versionwarning_messages = {
       'latest': {
           'default': 'Development version',
           'api': 'API is unstable',
           'tutorials': 'Tutorials may be incomplete',
       }
   }

Practical Examples
------------------

Simple Warning
~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   extensions = ['versionwarning.extension']
   
   version = '1.5'
   
   versionwarning_messages = {
       '1.5': '''
           This version is deprecated.
           <a href="/en/latest/">View latest documentation</a>
       ''',
   }

Development Branch
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import os
   
   on_develop = os.environ.get('BRANCH') == 'develop'
   
   if on_develop:
       versionwarning_messages = {
           'latest': '''
               <strong>⚠️ Development Version</strong><br>
               This documentation may contain unreleased features.
               <a href="/en/stable/">View stable version</a>
           '''
       }

EOL Warning
~~~~~~~~~~~

.. code-block:: python

   # End-of-life version
   from datetime import datetime
   
   eol_date = datetime(2024, 12, 31)
   
   if datetime.now() > eol_date:
       versionwarning_default_message = '''
           <strong>⚠️ End of Life</strong><br>
           This version is no longer supported.
           Please upgrade to a supported version.
       '''

Beta Warning
~~~~~~~~~~~~

.. code-block:: python

   if 'beta' in release.lower():
       versionwarning_messages['latest'] = '''
           <strong>🚧 Beta Version</strong><br>
           This is a pre-release version. Use with caution.
           <a href="/en/stable/">Stable version</a>
       '''

Advanced Features
-----------------

JavaScript Integration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: html

   <script>
   // Auto-redirect old versions
   (function() {
       const version = '1.5';
       const currentVersion = '2.0';
       
       if (version !== currentVersion) {
           const redirect = confirm(
               'This documentation is outdated. ' +
               'Would you like to view the latest version?'
           );
           if (redirect) {
               window.location.href = '/en/latest/';
           }
       }
   })();
   </script>

Cookie-Based Dismissal
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: html

   <div id="version-warning" class="version-warning">
       {message}
       <button onclick="dismissWarning()">×</button>
   </div>
   
   <script>
   function dismissWarning() {
       document.cookie = 'version_warning_dismissed=1;max-age=86400';
       document.getElementById('version-warning').style.display = 'none';
   }
   
   if (document.cookie.includes('version_warning_dismissed=1')) {
       document.getElementById('version-warning').style.display = 'none';
   }
   </script>

Testing
-------

Local Testing
~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   # Force version for testing
   version = '1.0'  # Old version
   
   versionwarning_messages = {
       '1.0': 'This should show a warning',
       '2.0': '',  # Current, no warning
   }

Build Validation
~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Build docs for different versions
   VERSION=1.0 sphinx-build docs docs/_build/v1.0
   VERSION=2.0 sphinx-build docs docs/_build/v2.0
   
   # Check for warning banner
   grep "version-warning" docs/_build/v1.0/index.html

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Build Docs
   
   on:
     push:
       branches: [main, develop]
       tags: ['v*']
   
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v2
         
         - name: Determine version
           id: version
           run: |
             if [[ "$GITHUB_REF" == refs/tags/* ]]; then
               echo "VERSION=${GITHUB_REF#refs/tags/v}" >> $GITHUB_OUTPUT
             else
               echo "VERSION=latest" >> $GITHUB_OUTPUT
             fi
         
         - name: Build docs
           run: |
             sphinx-build -D version=${{ steps.version.outputs.VERSION }} \
                          docs docs/_build

Best Practices
--------------

Message Content
~~~~~~~~~~~~~~~

1. Be clear and concise
2. Provide actionable links
3. Use appropriate urgency
4. Match your brand voice
5. Consider translations

Version Strategy
~~~~~~~~~~~~~~~~

1. Maintain multiple versions
2. Clear stable/dev distinction
3. Document version policy
4. Deprecation warnings
5. Migration guides

User Experience
~~~~~~~~~~~~~~~

1. Don't be too intrusive
2. Allow dismissal option
3. Provide version switcher
4. Mobile-friendly design
5. Accessible markup


Practical Examples
------------------

Basic Configuration
-------------------

Setup
~~~~~

.. code-block:: python

   # conf.py
   extensions = [
       'versionwarning.extension',
   ]
   
   # Current version
   version = '2.0'
   release = '2.0.1'

Version Warning Message
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   versionwarning_messages = {
       'latest': 'This is the development version!',
       'stable': '',  # No warning for stable
   }

Banner Configuration
--------------------

Message Types
~~~~~~~~~~~~~

.. code-block:: python

   versionwarning_messages = {
       # Development version warning
       'latest': '''
           You are viewing the <strong>development</strong> version.
           <a href="/en/stable/">Switch to stable version</a>
       ''',
       
       # Specific version warnings
       '1.0': '''
           This version is outdated.
           <a href="/en/latest/">View latest</a>
       ''',
       
       # No warning for current stable
       '2.0': '',
   }

Default Message
~~~~~~~~~~~~~~~

.. code-block:: python

   # Message for versions not explicitly defined
   versionwarning_default_message = '''
       This is an old version of the documentation.
       <a href="/en/stable/">Go to latest stable</a>
   '''

Banner Styling
--------------

Custom Colors
~~~~~~~~~~~~~

.. code-block:: python

   versionwarning_banner_html = '''
       <div class="version-warning" style="
           background-color: #ffeb3b;
           color: #000;
           padding: 10px;
           text-align: center;
           border-bottom: 2px solid #ffc107;
       ">
           {message}
       </div>
   '''

Theme Integration
~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Use theme colors
   versionwarning_banner_html = '''
       <div class="admonition warning version-warning">
           <p class="admonition-title">Version Warning</p>
           <p>{message}</p>
       </div>
   '''

Custom CSS
~~~~~~~~~~

.. code-block:: css

   /* custom.css */
   .version-warning {
       background: linear-gradient(to right, #ff6b6b, #feca57);
       color: white;
       padding: 15px;
       text-align: center;
       font-weight: bold;
       border-left: 5px solid #ee5a24;
   }
   
   .version-warning a {
       color: white;
       text-decoration: underline;
   }

Version Detection
-----------------

Read the Docs Integration
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   import os
   
   # Detect RTD environment
   on_rtd = os.environ.get('READTHEDOCS') == 'True'
   
   if on_rtd:
       rtd_version = os.environ.get('READTHEDOCS_VERSION', 'unknown')
       
       versionwarning_messages = {
           'latest': 'Development version - may be unstable',
           'stable': '',
       }
       
       # Set message based on RTD version
       if rtd_version not in ['stable', 'latest']:
           versionwarning_default_message = f'''
               You are viewing documentation for version {rtd_version}.
               <a href="/en/stable/">View stable version</a>
           '''

GitHub Pages
~~~~~~~~~~~~

.. code-block:: python

   # Detect from build context
   import subprocess
   
   try:
       git_branch = subprocess.check_output(
           ['git', 'rev-parse', '--abbrev-ref', 'HEAD']
       ).decode().strip()
       
       if git_branch == 'develop':
           versionwarning_messages['latest'] = 'Development branch'
   except:
       pass

Version Comparison
------------------

Semantic Versioning
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from packaging import version
   
   current_version = version.parse(release)
   latest_version = version.parse('2.1.0')
   
   if current_version < latest_version:
       versionwarning_default_message = f'''
           This is version {release}.
           Version {latest_version} is available.
       '''

Custom Logic
~~~~~~~~~~~~

.. code-block:: python

   def get_version_message(current_ver):
       """Generate version warning based on age."""
       if current_ver.startswith('0.'):
           return 'Pre-release version'
       elif current_ver.startswith('1.'):
           return 'Version 1.x is deprecated. Upgrade to 2.x'
       return ''
   
   versionwarning_default_message = get_version_message(version)

Multi-Version Setup
-------------------

Version Switcher
~~~~~~~~~~~~~~~~

.. code-block:: python

   versionwarning_banner_html = '''
       <div class="version-banner">
           <span>{message}</span>
           <select onchange="location.href=this.value">
               <option value="/en/stable/">Stable (2.0)</option>
               <option value="/en/latest/">Latest (dev)</option>
               <option value="/en/1.9/">1.9</option>
               <option value="/en/1.8/">1.8</option>
           </select>
       </div>
   '''

Version Links
~~~~~~~~~~~~~

.. code-block:: python

   versionwarning_messages = {
       'latest': '''
           Development version.
           <a href="/en/stable/">Stable</a> |
           <a href="/en/2.0/">2.0</a> |
           <a href="/en/1.9/">1.9</a>
       ''',
   }

Conditional Warnings
--------------------

By Page Type
~~~~~~~~~~~~

.. code-block:: python

   # In conf.py or custom extension
   def add_version_warning(app, pagename, templatename, context, doctree):
       """Add version warning based on page type."""
       if pagename.startswith('api/'):
           context['versionwarning_message'] = 'API may change!'
   
   def setup(app):
       app.connect('html-page-context', add_version_warning)

By Section
~~~~~~~~~~

.. code-block:: python

   versionwarning_messages = {
       'latest': {
           'default': 'Development version',
           'api': 'API is unstable',
           'tutorials': 'Tutorials may be incomplete',
       }
   }

Practical Examples
------------------

Simple Warning
~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   extensions = ['versionwarning.extension']
   
   version = '1.5'
   
   versionwarning_messages = {
       '1.5': '''
           This version is deprecated.
           <a href="/en/latest/">View latest documentation</a>
       ''',
   }

Development Branch
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import os
   
   on_develop = os.environ.get('BRANCH') == 'develop'
   
   if on_develop:
       versionwarning_messages = {
           'latest': '''
               <strong>⚠️ Development Version</strong><br>
               This documentation may contain unreleased features.
               <a href="/en/stable/">View stable version</a>
           '''
       }

EOL Warning
~~~~~~~~~~~

.. code-block:: python

   # End-of-life version
   from datetime import datetime
   
   eol_date = datetime(2024, 12, 31)
   
   if datetime.now() > eol_date:
       versionwarning_default_message = '''
           <strong>⚠️ End of Life</strong><br>
           This version is no longer supported.
           Please upgrade to a supported version.
       '''

Beta Warning
~~~~~~~~~~~~

.. code-block:: python

   if 'beta' in release.lower():
       versionwarning_messages['latest'] = '''
           <strong>🚧 Beta Version</strong><br>
           This is a pre-release version. Use with caution.
           <a href="/en/stable/">Stable version</a>
       '''

Advanced Features
-----------------

JavaScript Integration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: html

   <script>
   // Auto-redirect old versions
   (function() {
       const version = '1.5';
       const currentVersion = '2.0';
       
       if (version !== currentVersion) {
           const redirect = confirm(
               'This documentation is outdated. ' +
               'Would you like to view the latest version?'
           );
           if (redirect) {
               window.location.href = '/en/latest/';
           }
       }
   })();
   </script>

Cookie-Based Dismissal
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: html

   <div id="version-warning" class="version-warning">
       {message}
       <button onclick="dismissWarning()">×</button>
   </div>
   
   <script>
   function dismissWarning() {
       document.cookie = 'version_warning_dismissed=1;max-age=86400';
       document.getElementById('version-warning').style.display = 'none';
   }
   
   if (document.cookie.includes('version_warning_dismissed=1')) {
       document.getElementById('version-warning').style.display = 'none';
   }
   </script>

Testing
-------

Local Testing
~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   # Force version for testing
   version = '1.0'  # Old version
   
   versionwarning_messages = {
       '1.0': 'This should show a warning',
       '2.0': '',  # Current, no warning
   }

Build Validation
~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Build docs for different versions
   VERSION=1.0 sphinx-build docs docs/_build/v1.0
   VERSION=2.0 sphinx-build docs docs/_build/v2.0
   
   # Check for warning banner
   grep "version-warning" docs/_build/v1.0/index.html

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Build Docs
   
   on:
     push:
       branches: [main, develop]
       tags: ['v*']
   
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v2
         
         - name: Determine version
           id: version
           run: |
             if [[ "$GITHUB_REF" == refs/tags/* ]]; then
               echo "VERSION=${GITHUB_REF#refs/tags/v}" >> $GITHUB_OUTPUT
             else
               echo "VERSION=latest" >> $GITHUB_OUTPUT
             fi
         
         - name: Build docs
           run: |
             sphinx-build -D version=${{ steps.version.outputs.VERSION }} \
                          docs docs/_build

Best Practices
--------------

Message Content
~~~~~~~~~~~~~~~

1. Be clear and concise
2. Provide actionable links
3. Use appropriate urgency
4. Match your brand voice
5. Consider translations

Version Strategy
~~~~~~~~~~~~~~~~

1. Maintain multiple versions
2. Clear stable/dev distinction
3. Document version policy
4. Deprecation warnings
5. Migration guides

User Experience
~~~~~~~~~~~~~~~

1. Don't be too intrusive
2. Allow dismissal option
3. Provide version switcher
4. Mobile-friendly design
5. Accessible markup

Additional Resources
--------------------
- :doc:`sphinx-notfound-page` - Custom 404 pages
- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `sphinx-version-warning Documentation <https://github.com/humitos/sphinx-version-warning>`_
- `Read the Docs Versioning <https://docs.readthedocs.io/en/stable/versions.html>`_
- :doc:`../tutorials/packages/sphinx-version-warning` - Complete tutorial
- GitHub repository: https://github.com/sphinx-contrib/versionwarning

