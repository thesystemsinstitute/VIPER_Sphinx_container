bfabio.sphinx-rst-builder Tutorial
=====================================

.. note::

   **Package Resources:**

   - `PyPI Package <https://pypi.org/project/bfabio.sphinx-rst-builder/>`_
   - `API Documentation <../../pdoc/bfabio_sphinx_rst_builder/index.html>`_
   - `Manual <https://github.com/bfabio/sphinx-rst-builder>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial explains the reStructuredText builder extension for Sphinx.

What is bfabio.sphinx-rst-builder?
---------------------------------
This package provides a Sphinx builder that outputs reStructuredText files.

Installation
------------

Install via pip:

.. code-block:: bash

   pip install bfabio.sphinx-rst-builder

Configuration
-------------

Enable the extension in ``conf.py``:

.. code-block:: python

   extensions = [
       "sphinx_rst_builder",
   ]

Basic Usage
-----------

Build the ``rst`` output:

.. code-block:: bash

   sphinx-build -b rst docs docs/_build/rst

This generates reStructuredText files from your Sphinx source documents.

Advanced Features
-----------------

- Customize output suffixes with ``rst_file_suffix``.
- Adjust link suffixes with ``rst_link_suffix``.
- Preserve cross-references between documents.
- Convert processed RST back to source format.
- Useful for documentation migration and export.

Configuration Options
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py

   extensions = [
       "sphinx_rst_builder",
   ]

   # RST builder configuration
   rst_file_suffix = ".rst"        # Output file extension
   rst_link_suffix = ".rst"        # Link suffix in references
   rst_file_transform = None       # Custom file path transformer
   rst_link_transform = None       # Custom link transformer

Examples
--------

Basic RST Export
~~~~~~~~~~~~~~~~

Export your Sphinx documentation as plain RST files:

.. code-block:: bash

   # Build RST output
   sphinx-build -b rst docs docs/_build/rst

   # View generated files
   ls docs/_build/rst/
   # index.rst
   # getting-started.rst
   # api/
   #   index.rst
   #   module1.rst
   #   module2.rst

The output preserves your document structure but resolves includes and references.

Different Output Suffixes
~~~~~~~~~~~~~~~~~~~~~~~~~

Use different file extensions for output:

.. code-block:: python

   # conf.py

   extensions = ["sphinx_rst_builder"]

   # Use .txt extension for output files
   rst_file_suffix = ".txt"
   rst_link_suffix = ".txt"

Build:

.. code-block:: bash

   sphinx-build -b rst docs docs/_build/txt

Documentation Migration
~~~~~~~~~~~~~~~~~~~~~~~

Migrate documentation between projects:

1. **Export from source project:**

   .. code-block:: bash

      # In source project
      cd source-project
      sphinx-build -b rst docs exported_docs

2. **Copy to target project:**

   .. code-block:: bash

      # Copy exported RST files
      cp -r source-project/exported_docs/* target-project/docs/imported/

3. **Include in target project's toctree:**

   .. code-block:: restructuredtext

      .. toctree::
         :maxdepth: 2
         :caption: Imported Documentation

         imported/index

Converting Processed Content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The RST builder processes your source files, so substitutions, includes, and conditionals are resolved:

**Source (with includes and substitutions):**

.. code-block:: restructuredtext

   .. |project| replace:: MyProject

   Welcome to |project|
   ====================

   .. include:: _includes/intro.rst

   .. only:: html

      This is HTML-only content.

**Output (after RST build):**

.. code-block:: restructuredtext

   Welcome to MyProject
   ====================

   This is the introduction text from the included file.

   This is HTML-only content.

Custom Transformations
~~~~~~~~~~~~~~~~~~~~~~

Apply custom transformations to file paths and links:

.. code-block:: python

   # conf.py

   extensions = ["sphinx_rst_builder"]

   def custom_file_transform(docname):
       """Transform document names for output files."""
       # Add prefix to all output files
       return f"exported_{docname}"

   def custom_link_transform(docname):
       """Transform document names in cross-references."""
       return f"exported_{docname}"

   rst_file_transform = custom_file_transform
   rst_link_transform = custom_link_transform

Makefile Integration
~~~~~~~~~~~~~~~~~~~~

Add to your Makefile:

.. code-block:: makefile

   # Makefile

   SPHINXBUILD   = sphinx-build
   SOURCEDIR     = docs
   BUILDDIR      = docs/_build

   .PHONY: rst html clean export

   rst:
   	$(SPHINXBUILD) -b rst "$(SOURCEDIR)" "$(BUILDDIR)/rst"

   html:
   	$(SPHINXBUILD) -b html "$(SOURCEDIR)" "$(BUILDDIR)/html"

   export: rst
   	@echo "RST files exported to $(BUILDDIR)/rst"
   	tar -czf docs-export.tar.gz -C "$(BUILDDIR)" rst

   clean:
   	rm -rf "$(BUILDDIR)"

Creating Standalone Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Export documentation for distribution without Sphinx:

.. code-block:: bash

   # Build RST files
   sphinx-build -b rst docs docs/_build/rst

   # Create distribution package
   mkdir -p dist/docs
   cp -r docs/_build/rst/* dist/docs/

   # Add a simple README
   cat > dist/docs/README.md << 'EOF'
   # Documentation

   This documentation is in reStructuredText format.

   To view as HTML, use docutils:
       rst2html index.rst index.html

   Or install Sphinx and rebuild:
       pip install sphinx
       sphinx-build -b html . _build/html
   EOF

   # Package
   zip -r documentation.zip dist/docs/

CI/CD Export Pipeline
~~~~~~~~~~~~~~~~~~~~~

Export documentation in CI:

.. code-block:: yaml

   # .github/workflows/export-docs.yml
   name: Export Documentation

   on:
     release:
       types: [published]

   jobs:
     export:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v4

         - name: Set up Python
           uses: actions/setup-python@v5
           with:
             python-version: '3.11'

         - name: Install dependencies
           run: |
             pip install sphinx bfabio.sphinx-rst-builder

         - name: Export RST files
           run: |
             sphinx-build -b rst docs docs/_build/rst

         - name: Create archive
           run: |
             cd docs/_build
             tar -czf rst-docs.tar.gz rst/

         - name: Upload to release
           uses: actions/upload-release-asset@v1
           env:
             GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
           with:
             upload_url: ${{ github.event.release.upload_url }}
             asset_path: docs/_build/rst-docs.tar.gz
             asset_name: documentation-rst.tar.gz
             asset_content_type: application/gzip

Use Cases
~~~~~~~~~

**1. Documentation Backup:**
   Export processed RST as a backup before major changes.

**2. External Publishing:**
   Prepare RST files for publishing platforms that don't support Sphinx.

**3. Version Snapshots:**
   Create versioned snapshots of documentation in pure RST format.

**4. Migration:**
   Move documentation between Sphinx projects or to other documentation systems.

**5. Offline Distribution:**
   Distribute documentation that can be rebuilt without all original dependencies.

Additional Resources
--------------------

- `Manual <https://github.com/bfabio/sphinx-rst-builder>`_
- `PyPI <https://pypi.org/project/bfabio.sphinx-rst-builder/>`_
- `API Documentation <../../pdoc/bfabio_sphinx_rst_builder/index.html>`_
