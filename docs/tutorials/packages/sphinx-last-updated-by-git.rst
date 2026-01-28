Sphinx-Last-Updated-By-Git Tutorial
====================================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-last-updated-by-git/>`_
   - :doc:`See Working Example <../../examples/sphinx-last-updated-by-git-example>`


This tutorial demonstrates how to use sphinx-last-updated-by-git to automatically add last-modified dates from Git history.

What is Sphinx-Last-Updated-By-Git?
------------------------------------

sphinx-last-updated-by-git is a Sphinx extension that provides:

- Automatic last-updated timestamps
- Git commit history integration
- Per-page modification dates
- No manual date maintenance
- Accurate update tracking
- Commit author information
- Timezone support
- Customizable date formats
- CI/CD friendly
- Multi-language support

This eliminates manual date tracking and ensures documentation always shows accurate last-modified information.

Installation
------------

sphinx-last-updated-by-git is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinx_last_updated_by_git; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_last_updated_by_git',
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinx_last_updated_by_git']
   
   # HTML last updated format
   html_last_updated_fmt = '%b %d, %Y'
   
   # Git options
   git_last_updated_timezone = 'America/New_York'
   git_last_updated_metatags = True
   
   # Include uncommitted changes
   git_untracked_check_dependencies = False
   git_untracked_show_sourcelink = False

Basic Usage
-----------

Automatic Date Display
~~~~~~~~~~~~~~~~~~~~~~

Once configured, Sphinx automatically adds last-updated information to each page based on Git history.

The date appears in the page footer (theme-dependent):

.. code-block:: text

   Last updated on Dec 15, 2023

Accessing in Templates
~~~~~~~~~~~~~~~~~~~~~~

Use in custom templates:

.. code-block:: html

   {% if last_updated %}
   <div class="last-updated">
     Last modified: {{ last_updated }}
   </div>
   {% endif %}

Practical Examples
------------------

Example 1: Basic Date Display
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/conf.py``:

.. code-block:: python

   extensions = ['sphinx_last_updated_by_git']
   
   # Simple date format
   html_last_updated_fmt = '%Y-%m-%d'

Result in footer:

.. code-block:: text

   Last updated on 2023-12-15

Example 2: Detailed Timestamp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/conf.py``:

.. code-block:: python

   extensions = ['sphinx_last_updated_by_git']
   
   # Detailed timestamp
   html_last_updated_fmt = '%B %d, %Y at %I:%M %p %Z'
   
   # Timezone configuration
   git_last_updated_timezone = 'UTC'

Result:

.. code-block:: text

   Last updated on December 15, 2023 at 02:30 PM UTC

Example 3: Custom Template with Author
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/_templates/page.html``:

.. code-block:: html

   {% extends "!page.html" %}
   
   {% block footer %}
   {{ super() }}
   
   <div class="git-info">
     {% if last_updated %}
     <p class="last-updated">
       <strong>Last Updated:</strong> {{ last_updated }}
     </p>
     {% endif %}
     
     {% if git_author %}
     <p class="last-author">
       <strong>Last Modified By:</strong> {{ git_author }}
     </p>
     {% endif %}
   </div>
   {% endblock %}

``docs/conf.py``:

.. code-block:: python

   extensions = ['sphinx_last_updated_by_git']
   
   html_last_updated_fmt = '%b %d, %Y'
   
   # Enable author information
   git_last_updated_author = True

``docs/_static/git-info.css``:

.. code-block:: css

   .git-info {
       margin-top: 20px;
       padding: 15px;
       background-color: #f8f9fa;
       border-left: 4px solid #3498db;
       font-size: 14px;
   }
   
   .git-info p {
       margin: 5px 0;
   }
   
   .git-info strong {
       color: #2c3e50;
   }

Example 4: Per-Page Modification Table
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/_templates/page.html``:

.. code-block:: html

   {% extends "!page.html" %}
   
   {% block body %}
   {{ super() }}
   
   <div class="document-metadata">
     <h4>Document Information</h4>
     <table class="metadata-table">
       <tr>
         <th>Last Modified</th>
         <td>{{ last_updated or 'Unknown' }}</td>
       </tr>
       <tr>
         <th>Git Commit</th>
         <td><code>{{ git_commit_hash[:8] if git_commit_hash else 'N/A' }}</code></td>
       </tr>
       <tr>
         <th>Author</th>
         <td>{{ git_author or 'Unknown' }}</td>
       </tr>
       <tr>
         <th>File Path</th>
         <td><code>{{ pagename }}.rst</code></td>
       </tr>
     </table>
   </div>
   {% endblock %}

``docs/_static/metadata.css``:

.. code-block:: css

   .document-metadata {
       margin: 30px 0;
       padding: 20px;
       background: #f5f5f5;
       border-radius: 8px;
   }
   
   .document-metadata h4 {
       margin-top: 0;
       color: #2c3e50;
   }
   
   .metadata-table {
       width: 100%;
       border-collapse: collapse;
   }
   
   .metadata-table th {
       text-align: left;
       padding: 8px 12px;
       background-color: #e0e0e0;
       font-weight: 600;
       width: 30%;
   }
   
   .metadata-table td {
       padding: 8px 12px;
       border-bottom: 1px solid #ddd;
   }
   
   .metadata-table code {
       background-color: #fff;
       padding: 2px 6px;
       border-radius: 3px;
   }

Example 5: Multilingual Date Formats
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/conf.py``:

.. code-block:: python

   import locale
   
   extensions = ['sphinx_last_updated_by_git']
   
   # Set locale for date formatting
   try:
       locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')  # Spanish
       html_last_updated_fmt = '%d de %B de %Y'
   except:
       html_last_updated_fmt = '%B %d, %Y'

Advanced Features
-----------------

Timezone Handling
~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Display in specific timezone
   git_last_updated_timezone = 'Europe/London'
   
   # Or use UTC
   git_last_updated_timezone = 'UTC'
   
   # Format with timezone
   html_last_updated_fmt = '%Y-%m-%d %H:%M %Z'

Meta Tags for SEO
~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Add meta tags with modification date
   git_last_updated_metatags = True

This adds to HTML:

.. code-block:: html

   <meta name="last-modified" content="2023-12-15T14:30:00+00:00">

Uncommitted Changes
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Check uncommitted files
   git_untracked_check_dependencies = True
   
   # Show warning for uncommitted changes
   git_untracked_show_sourcelink = True

Custom Date Processing
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   def setup(app):
       def process_git_date(app, pagename, templatename, context, doctree):
           # Custom processing
           if 'last_updated' in context:
               date = context['last_updated']
               # Add custom formatting
               context['last_updated_custom'] = f"Updated: {date}"
       
       app.connect('html-page-context', process_git_date)

Docker Integration
------------------

Build with Git History
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Ensure .git directory is available
   docker run --rm \
     -v $(pwd):/project \
     kensai-sphinx:latest \
     sphinx-build -b html /project/docs /project/docs/_build/html

Important: The ``.git`` directory must be mounted for the extension to access Git history.

Dockerfile with Git
~~~~~~~~~~~~~~~~~~~

.. code-block:: dockerfile

   FROM kensai-sphinx:latest
   
   # Install git if not present
   RUN apk add --no-cache git
   
   WORKDIR /project
   
   # Build documentation
   CMD ["sphinx-build", "-b", "html", "docs", "docs/_build/html"]

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Build Docs with Git Dates
   
   on: [push]
   
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
           with:
             fetch-depth: 0  # Full history for accurate dates
         
         - name: Build Documentation
           run: |
             docker run --rm -v $(pwd):/project \
               kensai-sphinx:latest \
               sphinx-build -b html /project/docs /project/docs/_build/html
         
         - name: Verify Last Updated
           run: |
             # Check that dates are present
             if ! grep -q "Last updated" docs/_build/html/index.html; then
               echo "Last updated info not found!"
               exit 1
             fi
         
         - name: Deploy
           uses: peaceiris/actions-gh-pages@v3
           with:
             github_token: ${{ secrets.GITHUB_TOKEN }}
             publish_dir: ./docs/_build/html

GitLab CI
~~~~~~~~~

.. code-block:: yaml

   build-docs:
     image: kensai-sphinx:latest
     script:
       - git fetch --unshallow  # Get full history
       - sphinx-build -b html docs docs/_build/html
     artifacts:
       paths:
         - docs/_build/html
     variables:
       GIT_DEPTH: 0  # Full clone

Best Practices
--------------

1. **Full Git History**
   
   Use ``fetch-depth: 0`` in CI/CD for accurate dates

2. **Consistent Format**
   
   Choose readable date format

3. **Timezone Awareness**
   
   Set appropriate timezone

4. **Test Locally**
   
   Verify dates before deploying

5. **Handle Edge Cases**
   
   New files, uncommitted changes

6. **Performance**
   
   Consider caching for large repos

Troubleshooting
---------------

No Dates Showing
~~~~~~~~~~~~~~~~

**Solution:**

Check Git repository exists:

.. code-block:: bash

   ls -la .git

Ensure extension is loaded:

.. code-block:: python

   extensions = ['sphinx_last_updated_by_git']

Wrong Dates
~~~~~~~~~~~

**Solution:**

Fetch full Git history:

.. code-block:: bash

   git fetch --unshallow

Timezone Issues
~~~~~~~~~~~~~~~

**Solution:**

Explicitly set timezone:

.. code-block:: python

   git_last_updated_timezone = 'UTC'

Docker Git Not Found
~~~~~~~~~~~~~~~~~~~~

**Solution:**

Install Git in container:

.. code-block:: dockerfile

   RUN apk add --no-cache git

Shallow Clone Issues
~~~~~~~~~~~~~~~~~~~~

**Solution:**

In CI/CD, use full clone:

.. code-block:: yaml

   - uses: actions/checkout@v3
     with:
       fetch-depth: 0

Next Steps
----------

1. Add extension to conf.py
2. Configure date format
3. Test with git history
4. Customize template display
5. Deploy with CI/CD

Additional Resources
--------------------

- :doc:`sphinx-git` - More Git integration features
- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `sphinx-last-updated-by-git Documentation <https://github.com/mgeier/sphinx-last-updated-by-git>`_
- `Git Documentation <https://git-scm.com/doc>`_
