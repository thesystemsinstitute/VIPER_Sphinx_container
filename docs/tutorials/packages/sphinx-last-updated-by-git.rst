Sphinx-Last-Updated-By-Git Tutorial
====================================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-last-updated-by-git/>`_
   - `Manual <https://github.com/mgeier/sphinx-last-updated-by-git>`_
   - :doc:`Working Example <../../examples/sphinx-last-updated-by-git-example>`


.. contents:: Table of Contents
   :local:
   :depth: 2

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

The sphinx-last-updated-by-git extension automatically retrieves the last modification date from Git history and adds it to each documentation page.


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
