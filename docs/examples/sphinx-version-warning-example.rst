Sphinx-Version-Warning Example
===============================

This page demonstrates the **sphinx-version-warning** extension for showing version warnings in documentation.

.. contents:: Contents
   :local:
   :depth: 2

Overview
--------

The sphinx-version-warning extension displays a banner warning users when they're viewing outdated documentation versions.

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

See Also
--------

- :doc:`../tutorials/packages/sphinx-version-warning` - Complete tutorial
- GitHub repository: https://github.com/sphinx-contrib/versionwarning
