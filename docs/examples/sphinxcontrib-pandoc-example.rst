Sphinxcontrib Pandoc Example
============================

.. note::

   **Package**: sphinxcontrib-pandoc  
   **Purpose**: Pandoc integration for Sphinx  
   **Tutorial**: See :doc:`../tutorials/packages/sphinxcontrib-pandoc` for complete tutorial

This page demonstrates **sphinxcontrib-pandoc** - Pandoc integration for Sphinx.

.. contents:: Contents
   :local:
   :depth: 3

Overview
--------


Key Features
~~~~~~~~~~~~

- **Format Conversion**: Convert to multiple formats
- **Pandoc Power**: Leverage Pandoc's conversion capabilities
- **Custom Templates**: Use custom Pandoc templates
- **Flexible Options**: Configure Pandoc behavior

Installation
------------

Using pip
~~~~~~~~~

Install the extension:

.. code-block:: bash

   pip install sphinxcontrib-pandoc
   # Also install Pandoc system-wide
   sudo apt-get install pandoc

Or add to your ``requirements.txt``:

.. code-block:: text

   sphinxcontrib-pandoc
   sphinx>=5.0.0

Configuration
-------------

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinxcontrib.pandoc',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

Complete configuration with all features:

.. code-block:: python

   extensions = ['sphinxcontrib.pandoc']
   
   # Package-specific configuration
   pandoc_builder_name = 'pandoc'
   pandoc_format = 'markdown'
   
   # Pandoc options
   pandoc_options = [
       '--standalone',
       '--toc',
       '--toc-depth=3',
       '--markdown-headings=atx',
   ]
   
   # Template
   pandoc_template = None

Basic Usage
-----------

Example 1: Convert to Markdown
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Export documentation to Markdown:

.. code-block:: bash

   # Build Markdown
   sphinx-build -b pandoc docs docs/_build/markdown
   
   # With specific options
   sphinx-build -b pandoc \
       -D pandoc_format=markdown \
       -D pandoc_options="--standalone --toc" \
       docs docs/_build/markdown

Example 2: Generate DOCX
~~~~~~~~~~~~~~~~~~~~~~~~

Create Word documents:

.. code-block:: bash

   # Generate DOCX
   sphinx-build -b pandoc \
       -D pandoc_format=docx \
       -D pandoc_options="--reference-doc=template.docx" \
       docs docs/_build/docx

Real-World Examples
-------------------

Example: Multi-format Export
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Build script for multiple formats:

.. code-block:: python

   #!/usr/bin/env python3
   """Build documentation in multiple formats."""
   import subprocess
   from pathlib import Path
   
   SOURCE_DIR = Path('docs')
   BUILD_DIR = Path('docs/_build')
   
   FORMATS = {
       'markdown': {
           'format': 'markdown',
           'options': ['--standalone', '--toc', '--markdown-headings=atx'],
       },
       'docx': {
           'format': 'docx',
           'options': ['--reference-doc=template.docx'],
       },
       'epub': {
           'format': 'epub',
           'options': ['--epub-cover-image=cover.jpg'],
       },
       'latex': {
           'format': 'latex',
           'options': ['--standalone'],
       },
   }
   
   for name, config in FORMATS.items():
       output_dir = BUILD_DIR / name
       output_dir.mkdir(parents=True, exist_ok=True)
       
       cmd = [
           'sphinx-build',
           '-b', 'pandoc',
           '-D', f'pandoc_format={config["format"]}',
           '-D', f'pandoc_options={" ".join(config["options"])}',
           str(SOURCE_DIR),
           str(output_dir),
       ]
       
       print(f"Building {name}...")
       subprocess.run(cmd, check=True)

Example: CI/CD Integration
~~~~~~~~~~~~~~~~~~~~~~~~~~

GitHub Actions workflow:

.. code-block:: yaml

   name: Build Multi-format Docs
   
   on: [push]
   
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Install Pandoc
           run: |
             sudo apt-get update
             sudo apt-get install -y pandoc
         
         - name: Set up Python
           uses: actions/setup-python@v4
           with:
             python-version: '3.11'
         
         - name: Install dependencies
           run: |
             pip install sphinx sphinxcontrib-pandoc
         
         - name: Build Markdown
           run: |
             sphinx-build -b pandoc -D pandoc_format=markdown docs docs/_build/markdown
         
         - name: Build DOCX
           run: |
             sphinx-build -b pandoc -D pandoc_format=docx docs docs/_build/docx
         
         - name: Upload artifacts
           uses: actions/upload-artifact@v3
           with:
             name: documentation
             path: docs/_build/

Example: Custom Template
~~~~~~~~~~~~~~~~~~~~~~~~

Use custom Pandoc template:

.. code-block:: python

   # In conf.py
   pandoc_format = 'latex'
   pandoc_options = [
       '--template=custom-template.latex',
       '--standalone',
       '--toc',
       '--variable=documentclass:report',
       '--variable=geometry:margin=1in',
   ]

Best Practices
--------------

Recommendations
~~~~~~~~~~~~~~~

- Install compatible Pandoc version
- Test conversions for all target formats
- Use format-specific templates
- Review converted output quality
- Maintain conversion scripts

Common Patterns
~~~~~~~~~~~~~~~

Standard patterns for using sphinxcontrib-pandoc:

1. **Markdown Export**: Export for GitHub/GitLab
2. **DOCX Generation**: Create Word documents for review
3. **Multi-format**: Build all formats in CI/CD

Integration Tips
----------------

Working with Other Extensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

sphinxcontrib-pandoc integrates well with:

- Standard Sphinx extensions
- Custom export workflows
- Documentation build pipelines

Additional Resources
--------------------

- :doc:`Complete Tutorial <../tutorials/packages/sphinxcontrib-pandoc>`
- `PyPI Package <https://pypi.org/project/sphinxcontrib-pandoc/>`_
- `Pandoc Documentation <https://pandoc.org/>`_
- :ref:`Package API Documentation <pdoc-sphinxcontrib-pandoc>`

Next Steps
----------

- Explore the :doc:`tutorial <../tutorials/packages/sphinxcontrib-pandoc>`
- Check the official documentation
- Try the examples in your own projects
- Customize for your specific needs
