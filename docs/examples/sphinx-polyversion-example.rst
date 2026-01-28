Sphinx Polyversion Example
==========================

.. note::

   **Package**: sphinx-polyversion  
   **Purpose**: Multi-version documentation  
   **Tutorial**: See :doc:`../tutorials/packages/sphinx-polyversion` for complete tutorial

This page demonstrates **sphinx-polyversion** - Multi-version documentation.

.. contents:: Contents
   :local:
   :depth: 3

Overview
--------

What is sphinx-polyversion?
---------------------------

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

- :doc:`Complete Tutorial <../tutorials/packages/sphinx-polyversion>`
- `PyPI Package <https://pypi.org/project/sphinx-polyversion/>`_
- `Official Documentation <https://sphinx-polyversion.readthedocs.io/>`_
- :ref:`Package API Documentation <pdoc-sphinx-polyversion>`

Next Steps
----------

- Explore the :doc:`tutorial <../tutorials/packages/sphinx-polyversion>`
- Check the official documentation
- Try the examples in your own projects
- Customize for your specific needs
