Sphinx-Last-Updated-By-Git Example
===================================

This page demonstrates the **sphinx-last-updated-by-git** extension for automatically adding "last updated" information from Git commit history.

.. contents:: Contents
   :local:
   :depth: 2

Overview
--------

The sphinx-last-updated-by-git extension automatically retrieves the last modification date from Git history and adds it to each documentation page.

Basic Configuration
-------------------

Setup
~~~~~

.. code-block:: python

   # conf.py
   extensions = [
       'sphinx_last_updated_by_git',
   ]

The extension automatically enables ``html_last_updated_fmt`` using Git.

Default Behavior
~~~~~~~~~~~~~~~~

By default, the extension:

1. Checks Git history for each source file
2. Finds the last commit that modified the file
3. Displays the commit date in the page footer

Date Format
-----------

Custom Format
~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   html_last_updated_fmt = '%b %d, %Y'

Examples:

- ``'%Y-%m-%d'`` → 2024-01-26
- ``'%B %d, %Y'`` → January 26, 2024
- ``'%d/%m/%Y'`` → 26/01/2024
- ``'%c'`` → Full date and time

Locale-Specific
~~~~~~~~~~~~~~~

.. code-block:: python

   import locale
   
   # Set locale for date formatting
   try:
       locale.setlocale(locale.LC_TIME, 'en_US.UTF-8')
   except:
       pass
   
   html_last_updated_fmt = '%B %d, %Y at %H:%M'

Advanced Configuration
----------------------

Branch Selection
~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   # Use specific branch
   import subprocess
   
   def get_git_branch():
       try:
           return subprocess.check_output(
               ['git', 'rev-parse', '--abbrev-ref', 'HEAD']
           ).decode().strip()
       except:
           return 'main'
   
   current_branch = get_git_branch()

Custom Commit Information
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Show commit hash and author
   html_context = {
       'display_github': True,
       'github_user': 'username',
       'github_repo': 'repository',
       'github_version': 'main',
   }

Template Customization
----------------------

Custom Template
~~~~~~~~~~~~~~~

Create ``_templates/footer.html``:

.. code-block:: html

   {% extends "!footer.html" %}
   
   {% block extrafooter %}
   <div class="last-updated">
       Last updated: {{ last_updated }}
   </div>
   {% if show_source %}
   <div class="git-info">
       <a href="{{ github_url }}">View source on GitHub</a>
   </div>
   {% endif %}
   {% endblock %}

Advanced Template
~~~~~~~~~~~~~~~~~

.. code-block:: html

   {% extends "!footer.html" %}
   
   {% block extrafooter %}
   <div class="git-metadata">
       <div class="last-modified">
           <i class="fa fa-clock-o"></i>
           Last modified: {{ last_updated }}
       </div>
       {% if commit_hash %}
       <div class="commit-info">
           <i class="fa fa-git"></i>
           Commit: <code>{{ commit_hash[:7] }}</code>
       </div>
       {% endif %}
       {% if commit_author %}
       <div class="author-info">
           <i class="fa fa-user"></i>
           By: {{ commit_author }}
       </div>
       {% endif %}
   </div>
   {% endblock %}

Styling
-------

CSS Customization
~~~~~~~~~~~~~~~~~

.. code-block:: css

   /* custom.css */
   .last-updated {
       text-align: center;
       padding: 10px;
       font-size: 0.9em;
       color: #666;
       border-top: 1px solid #e1e4e5;
       margin-top: 20px;
   }
   
   .git-metadata {
       display: flex;
       justify-content: space-between;
       padding: 10px 0;
       font-size: 0.85em;
       color: #888;
   }
   
   .git-metadata code {
       background-color: #f6f8fa;
       padding: 2px 6px;
       border-radius: 3px;
   }

Theme Integration
~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   html_static_path = ['_static']
   html_css_files = ['custom.css']

Git Information Extraction
---------------------------

Get Commit Details
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   import subprocess
   from datetime import datetime
   
   def get_git_info(filepath):
       """Get Git information for a file."""
       try:
           # Last commit date
           date_str = subprocess.check_output([
               'git', 'log', '-1',
               '--format=%ci',
               filepath
           ]).decode().strip()
           
           # Commit hash
           commit_hash = subprocess.check_output([
               'git', 'log', '-1',
               '--format=%H',
               filepath
           ]).decode().strip()
           
           # Author
           author = subprocess.check_output([
               'git', 'log', '-1',
               '--format=%an',
               filepath
           ]).decode().strip()
           
           return {
               'date': date_str,
               'hash': commit_hash,
               'author': author
           }
       except:
           return None

Multiple Authors
~~~~~~~~~~~~~~~~

.. code-block:: python

   def get_all_contributors(filepath):
       """Get all contributors to a file."""
       try:
           authors = subprocess.check_output([
               'git', 'log',
               '--format=%an',
               filepath
           ]).decode().strip().split('\n')
           
           # Remove duplicates, preserve order
           seen = set()
           unique_authors = []
           for author in authors:
               if author not in seen:
                   seen.add(author)
                   unique_authors.append(author)
           
           return unique_authors
       except:
           return []

Integration with Hosting
-------------------------

GitHub Integration
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   html_context = {
       'display_github': True,
       'github_user': 'yourusername',
       'github_repo': 'yourrepo',
       'github_version': 'main',
       'conf_py_path': '/docs/',
   }

GitLab Integration
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   html_context = {
       'display_gitlab': True,
       'gitlab_user': 'yourusername',
       'gitlab_repo': 'yourrepo',
       'gitlab_version': 'main',
       'conf_py_path': '/docs/',
   }

Bitbucket Integration
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   html_context = {
       'display_bitbucket': True,
       'bitbucket_user': 'yourusername',
       'bitbucket_repo': 'yourrepo',
       'bitbucket_version': 'main',
   }

Practical Examples
------------------

Simple Footer
~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   extensions = ['sphinx_last_updated_by_git']
   html_last_updated_fmt = '%Y-%m-%d'

Result: "Last updated: 2024-01-26"

Detailed Footer
~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinx_last_updated_by_git']
   html_last_updated_fmt = '%B %d, %Y at %H:%M'

Template ``_templates/footer.html``:

.. code-block:: html

   {% extends "!footer.html" %}
   {% block extrafooter %}
   <div class="metadata">
       Last updated: {{ last_updated }}<br>
       <a href="{{ pathto('genindex') }}">Index</a> |
       <a href="{{ pathto('search') }}">Search</a>
   </div>
   {% endblock %}

With Version Control Links
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   import subprocess
   
   # Get current commit
   try:
       commit_hash = subprocess.check_output(
           ['git', 'rev-parse', 'HEAD']
       ).decode().strip()
   except:
       commit_hash = 'unknown'
   
   html_context = {
       'commit_hash': commit_hash,
       'github_url': f'https://github.com/user/repo/commit/{commit_hash}',
   }

Template:

.. code-block:: html

   <div class="version-info">
       Last updated: {{ last_updated }}<br>
       Build from commit:
       <a href="{{ github_url }}">{{ commit_hash[:7] }}</a>
   </div>

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Build Docs
   
   on:
     push:
       branches: [main]
   
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v2
           with:
             fetch-depth: 0  # Full history for git dates
         
         - name: Build docs
           run: |
             pip install sphinx sphinx-last-updated-by-git
             sphinx-build docs docs/_build/html

GitLab CI
~~~~~~~~~

.. code-block:: yaml

   pages:
     image: python:3.11
     script:
       - pip install sphinx sphinx-last-updated-by-git
       - git fetch --unshallow  # Get full history
       - sphinx-build docs public
     artifacts:
       paths:
         - public

Read the Docs
~~~~~~~~~~~~~

.. code-block:: yaml

   # .readthedocs.yaml
   version: 2
   
   build:
     os: ubuntu-22.04
     tools:
       python: "3.11"
   
   python:
     install:
       - requirements: docs/requirements.txt

``docs/requirements.txt``:

.. code-block:: text

   sphinx>=4.0
   sphinx-last-updated-by-git

Fallback Handling
-----------------

No Git Repository
~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   import os
   from datetime import datetime
   
   # Fallback if not in Git repo
   if not os.path.exists('.git'):
       html_last_updated_fmt = False
       # Or use current date
       # html_last_updated_fmt = datetime.now().strftime('%Y-%m-%d')

Missing Files
~~~~~~~~~~~~~

.. code-block:: python

   def safe_get_git_date(filepath):
       """Get git date with fallback."""
       try:
           date_str = subprocess.check_output([
               'git', 'log', '-1', '--format=%ci', filepath
           ]).decode().strip()
           return date_str
       except:
           # File not in git history
           return datetime.now().strftime('%Y-%m-%d')

Best Practices
--------------

Git Configuration
~~~~~~~~~~~~~~~~~

1. Ensure full Git history in CI
2. Use ``fetch-depth: 0`` in GitHub Actions
3. Configure Git user for automated commits
4. Don't ignore ``.git`` in build

Date Formatting
~~~~~~~~~~~~~~~

1. Use consistent format across site
2. Consider internationalization
3. Show timezone if relevant
4. Match theme style

Performance
~~~~~~~~~~~

1. Cache Git queries when possible
2. Batch git log commands
3. Consider build-time vs runtime
4. Don't query for every page request

Troubleshooting
---------------

Dates Not Showing
~~~~~~~~~~~~~~~~~

Check:

1. Extension is in ``extensions`` list
2. Git repository exists
3. Files are tracked in Git
4. CI has full Git history

Wrong Dates
~~~~~~~~~~~

.. code-block:: bash

   # Verify git log
   git log -1 --format=%ci docs/index.rst
   
   # Check git config
   git config --list | grep date

Build Warnings
~~~~~~~~~~~~~~

.. code-block:: python

   # Suppress warnings if desired
   import warnings
   warnings.filterwarnings('ignore', category=UserWarning, module='sphinx_last_updated_by_git')

See Also
--------

- :doc:`../tutorials/packages/sphinx-last-updated-by-git` - Complete tutorial
- GitHub repository: https://github.com/mgeier/sphinx-last-updated-by-git
