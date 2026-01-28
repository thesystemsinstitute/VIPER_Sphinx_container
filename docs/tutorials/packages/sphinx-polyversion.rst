Sphinx Polyversion Tutorial
===========================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-polyversion/>`_
   - :doc:`See Working Example <../../examples/sphinx-polyversion-example>`
   - `Official Documentation <https://sphinx-polyversion.readthedocs.io/>`_

This tutorial demonstrates how to use sphinx-polyversion in your Sphinx documentation.

What is Sphinx Polyversion?
----------------------------

sphinx-polyversion is a Sphinx extension that provides:

- Multi-version documentation
- Easy integration with Sphinx
- Comprehensive configuration options
- Professional documentation output

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

Additional Resources
--------------------

- :doc:`Working Example <../../examples/sphinx-polyversion-example>`
- `PyPI Package <https://pypi.org/project/sphinx-polyversion/>`_
- `Official Documentation <https://sphinx-polyversion.readthedocs.io/>`_
