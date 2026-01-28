Sphinx Polyversion Tutorial
===========================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-polyversion/>`_
   - `API Documentation <../../pdoc/sphinx_polyversion/index.html>`_
   - `Manual <https://github.com/Holzhaus/sphinx-polyversion>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinx-polyversion in your Sphinx documentation.

What is Sphinx Polyversion?
----------------------------
sphinx-polyversion is a Sphinx extension that provides:

- Multi-version documentation
- Easy integration with Sphinx
- Comprehensive configuration options
- Professional documentation output

sphinx-polyversion provides:

- Multi-version documentation
- Integration with Sphinx documentation
- Flexible configuration options
- Professional output formatting

Key Features
~~~~~~~~~~~~

- **Version Management**: Build documentation for multiple versions
- **Git Integration**: Automatic version detection from Git tags
- **Version Selector**: Add version switcher to documentation
- **Flexible Sources**: Support multiple version sources


Installation
------------

sphinx-polyversion is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinx_polyversion; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``docs/conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_polyversion',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinx_polyversion']
   
   # Configuration options
   polyversion_default_version = 'latest'
   polyversion_version_sources = {
       'git': 'git describe --tags --always',
   }
   polyversion_template_vars = {
       'current_version': lambda: 'latest',
   }


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_polyversion',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

Complete configuration with all features:

.. code-block:: python

   extensions = ['sphinx_polyversion']
   
   # Package-specific configuration
   polyversion_default_version = 'latest'
   
   # Version detection
   polyversion_version_sources = {
       'git': 'git describe --tags --always',
       'env': 'DOCS_VERSION',
   }
   
   # Template variables
   polyversion_template_vars = {
       'current_version': lambda: 'latest',
       'all_versions': lambda: ['v1.0', 'v2.0', 'latest'],
   }
   
   # Version filtering
   polyversion_version_filter = lambda v: not v.endswith('-dev')
   
   # Output configuration
   polyversion_output_format = '{version}'

Basic Usage
-----------

Getting Started
~~~~~~~~~~~~~~~

Build multiple versions:

.. code-block:: bash

   sphinx-polyversion docs docs/_build/html

Version Configuration
~~~~~~~~~~~~~~~~~~~~~

Configure version sources:

.. code-block:: python

   # In conf.py
   polyversion_version_sources = {
       'git': 'git describe --tags',
       'env': 'VERSION',
   }

Common Use Cases
----------------

Multi-version Builds
~~~~~~~~~~~~~~~~~~~~

Build all versions from Git tags:

.. code-block:: bash

   sphinx-polyversion --all docs docs/_build/html

Version Selector
~~~~~~~~~~~~~~~~

Add version selector to template:

.. code-block:: html

   <div class="version-selector">
       {% for version in versions %}
       <a href="/{{ version }}/">{{ version }}</a>
       {% endfor %}
   </div>

Advanced Features
-----------------

Custom Version Detection
~~~~~~~~~~~~~~~~~~~~~~~~

Custom version detection logic:

.. code-block:: python

   def get_version():
       import subprocess
       return subprocess.check_output(['git', 'describe', '--tags']).decode().strip()
   
   polyversion_template_vars = {
       'version': get_version,
   }

Version Filtering
~~~~~~~~~~~~~~~~~

Filter which versions to build:

.. code-block:: python

   polyversion_version_filter = lambda v: v.startswith('v')

Best Practices
--------------

Tips and Guidelines
~~~~~~~~~~~~~~~~~~~

- Use semantic versioning
- Keep version documentation organized
- Test version builds regularly
- Use appropriate version selectors
- Maintain version compatibility

Troubleshooting
---------------

Common Issues
~~~~~~~~~~~~~

**Issue**: Version not detected

**Solution**: Check Git tags and version source configuration.

**Issue**: Build failures for old versions

**Solution**: Use version-specific configuration or filters.


Practical Examples
------------------

Overview
--------


Key Features
~~~~~~~~~~~~

- **Version Management**: Build documentation for multiple versions
- **Git Integration**: Automatic version detection from Git tags
- **Version Selector**: Add version switcher to documentation
- **Flexible Sources**: Support multiple version sources

Installation
------------

Using pip
~~~~~~~~~

Install the extension:

.. code-block:: bash

   pip install sphinx-polyversion

Or add to your ``requirements.txt``:

.. code-block:: text

   sphinx-polyversion
   sphinx>=5.0.0

Configuration
-------------

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_polyversion',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

Complete configuration with all features:

.. code-block:: python

   extensions = ['sphinx_polyversion']
   
   # Package-specific configuration
   polyversion_default_version = 'latest'
   
   # Version detection
   polyversion_version_sources = {
       'git': 'git describe --tags --always',
       'env': 'DOCS_VERSION',
   }
   
   # Template variables
   polyversion_template_vars = {
       'current_version': lambda: 'latest',
       'all_versions': lambda: ['v1.0', 'v2.0', 'latest'],
   }
   
   # Version filtering
   polyversion_version_filter = lambda v: not v.endswith('-dev')
   
   # Output configuration
   polyversion_output_format = '{version}'

Basic Usage
-----------

Example 1: Build All Versions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Build documentation for all Git tags:

.. code-block:: bash

   # Build all versions
   sphinx-polyversion docs docs/_build/html
   
   # Build specific versions
   sphinx-polyversion --versions v1.0,v2.0,latest docs docs/_build/html

Example 2: Version Selector Template
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add version selector to your theme:

.. code-block:: html

   {# In your theme template #}
   <div class="version-selector">
       <select onchange="window.location.href=this.value">
           {% for version in versions %}
           <option value="/{{ version }}/" 
                   {% if version == current_version %}selected{% endif %}>
               {{ version }}
           </option>
           {% endfor %}
       </select>
   </div>

Real-World Examples
-------------------

Example: Complete Multi-version Setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Full configuration for multi-version docs:

.. code-block:: python

   # docs/conf.py
   import subprocess
   
   extensions = ['sphinx_polyversion']
   
   def get_git_versions():
       """Get all git tags."""
       result = subprocess.run(
           ['git', 'tag', '-l'],
           capture_output=True,
           text=True
       )
       versions = result.stdout.strip().split('\n')
       # Filter and sort versions
       versions = [v for v in versions if v.startswith('v')]
       versions.sort(reverse=True)
       return versions
   
   polyversion_default_version = 'latest'
   polyversion_version_sources = {
       'git': 'git describe --tags --always',
   }
   
   polyversion_template_vars = {
       'current_version': lambda: 'latest',
       'all_versions': get_git_versions,
   }

Example: CI/CD Integration
~~~~~~~~~~~~~~~~~~~~~~~~~~

GitHub Actions workflow for multi-version docs:

.. code-block:: yaml

   name: Build Multi-version Docs
   
   on:
     push:
       tags:
         - 'v*'
     workflow_dispatch:
   
   jobs:
     build-docs:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
           with:
             fetch-depth: 0  # Fetch all history for all tags
         
         - name: Set up Python
           uses: actions/setup-python@v4
           with:
             python-version: '3.11'
         
         - name: Install dependencies
           run: |
             pip install sphinx sphinx-polyversion
         
         - name: Build all versions
           run: |
             sphinx-polyversion docs docs/_build/html
         
         - name: Deploy to GitHub Pages
           uses: peaceiris/actions-gh-pages@v3
           with:
             github_token: ${{ secrets.GITHUB_TOKEN }}
             publish_dir: ./docs/_build/html

Example: Makefile Integration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add to ``Makefile``:

.. code-block:: makefile

   .PHONY: multiversion
   multiversion:
   	sphinx-polyversion $(SOURCEDIR) $(BUILDDIR)/html
   
   .PHONY: multiversion-latest
   multiversion-latest:
   	sphinx-polyversion --versions latest $(SOURCEDIR) $(BUILDDIR)/html

Best Practices
--------------

Recommendations
~~~~~~~~~~~~~~~

- Use semantic versioning for tags
- Keep version documentation consistent
- Test builds for all supported versions
- Use version filtering for development tags
- Provide clear version navigation

Common Patterns
~~~~~~~~~~~~~~~

Standard patterns for using sphinx-polyversion:

1. **Git Tags**: Use Git tags as version source
2. **Version Selector**: Add dropdown for version switching
3. **Latest Alias**: Maintain 'latest' pointing to newest version

Integration Tips
----------------

Working with Other Extensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

sphinx-polyversion integrates well with:

- sphinx-multiversion for alternative approach
- sphinx-versions for version management
- Standard Sphinx themes with custom templates

Additional Resources
--------------------

- `PyPI Package <https://pypi.org/project/sphinx-polyversion/>`_
- `Official Documentation <https://sphinx-polyversion.readthedocs.io/>`_
- :doc:`Complete Tutorial <../tutorials/packages/sphinx-polyversion>`
- :ref:`Package API Documentation <pdoc-sphinx-polyversion>`
Next Steps
----------
- Explore the :doc:`tutorial <../tutorials/packages/sphinx-polyversion>`
- Check the official documentation
- Try the examples in your own projects
- Customize for your specific needs

