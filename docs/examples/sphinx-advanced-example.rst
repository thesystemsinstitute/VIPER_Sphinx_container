Sphinx-Advanced Example
========================

.. note::

   **Package**: sphinx-advanced  
   **Purpose**: Advanced Sphinx features and extensions collection  
   **Tutorial**: See :doc:`../tutorials/packages/sphinx-advanced` for complete tutorial

This page demonstrates **sphinx-advanced** - a collection of advanced Sphinx features, utilities, and enhancement extensions.

.. contents:: Contents
   :local:
   :depth: 3


Installation
------------

Using pip
~~~~~~~~~

Install the extension:

.. code-block:: bash

   pip install sphinx-advanced

Or add to your ``requirements.txt``:

.. code-block:: text

   sphinx-advanced>=2.0.0
   sphinx>=5.0.0

Configuration
-------------

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_advanced',
       # ... other extensions
   ]
   
   # Enable advanced features
   sphinx_advanced_enable = True

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

Complete configuration with all features:

.. code-block:: python

   # Advanced Features
   sphinx_advanced_enable = True
   sphinx_advanced_features = [
       'xref',
       'metadata',
       'transforms',
       'builders',
       'validators',
   ]
   
   # Cross-Reference Options
   sphinx_advanced_xref_aliases = {
       'py:class': 'class',
       'py:func': 'function',
   }
   sphinx_advanced_xref_external = True
   sphinx_advanced_xref_cache = True
   
   # Metadata Management
   sphinx_advanced_metadata = {
       'author': 'Documentation Team',
       'version': '1.0.0',
       'status': 'production',
   }
   sphinx_advanced_metadata_inherit = True
   
   # Content Transforms
   sphinx_advanced_transforms = [
       'heading_anchors',
       'link_rewrite',
       'image_optimize',
       'code_highlight',
   ]
   
   # Build Options
   sphinx_advanced_parallel_build = True
   sphinx_advanced_cache_enabled = True
   sphinx_advanced_cache_dir = '.sphinx_cache'
   
   # Output Formats
   sphinx_advanced_builders = ['epub', 'latex', 'markdown']
   sphinx_advanced_pdf_engine = 'xelatex'
   
   # Validation
   sphinx_advanced_validate_links = True
   sphinx_advanced_validate_refs = True
   sphinx_advanced_strict_warnings = True
   
   # Template Options
   sphinx_advanced_template_dirs = ['_templates/advanced']
   sphinx_advanced_template_bridge = 'myapp.TemplateBridge'

Directives
----------

advanced-section Directive
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create advanced sections with metadata:

.. code-block:: rst

   .. advanced-section:: Installation
      :level: 2
      :tags: setup, installation
      :audience: developers
      :difficulty: beginner
      
      Detailed installation instructions.

advanced-include Directive
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Include files with preprocessing:

.. code-block:: rst

   .. advanced-include:: example.py
      :language: python
      :lines: 10-50
      :emphasize-lines: 15,20-25
      :dedent: 4
      :transform: remove_comments
      :caption: Example code

advanced-toctree Directive
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Enhanced table of contents:

.. code-block:: rst

   .. advanced-toctree::
      :maxdepth: 3
      :caption: Contents
      :numbered:
      :hidden:
      :metadata: show
      :tags: important
      
      intro
      guide
      reference

advanced-metadata Directive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Define document metadata:

.. code-block:: rst

   .. advanced-metadata::
      :author: John Doe
      :version: 1.0.0
      :status: draft
      :tags: api, reference
      :audience: developers
      :reviewed: 2024-01-15

advanced-condition Directive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Conditional content inclusion:

.. code-block:: rst

   .. advanced-condition::
      :if: version >= '2.0'
      :platform: linux, macos
      :python-version: >= 3.8
      
      Content for version 2.0+ on Linux/macOS with Python 3.8+

Roles
-----

Advanced Reference Roles
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   See :xref:`advanced reference <module.Class.method>`.
   
   Link to :external:`GitHub <https://github.com/user/repo>`.
   
   Use :abbr:`API|Application Programming Interface`.
   
   Highlight :mark:`important text`.

Practical Examples
------------------

Advanced Document Structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**File**: ``advanced-doc.rst``

.. code-block:: rst

   Advanced Documentation
   ======================
   
   .. advanced-metadata::
      :author: Documentation Team
      :version: 2.0.0
      :status: production
      :tags: advanced, reference
      :last-updated: 2024-01-20
   
   .. advanced-section:: Overview
      :level: 2
      :tags: introduction
      :audience: all
      
      This document demonstrates advanced Sphinx features.
   
   .. advanced-toctree::
      :maxdepth: 2
      :caption: Contents
      :numbered:
      :metadata: show
      
      installation
      configuration
      usage
      api

Conditional Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Platform-Specific Instructions
   ==============================
   
   .. advanced-condition::
      :platform: windows
      
      Windows Installation
      --------------------
      
      .. code-block:: batch
      
         pip install mypackage
         mypackage-setup.bat
   
   .. advanced-condition::
      :platform: linux, macos
      
      Linux/macOS Installation
      ------------------------
      
      .. code-block:: bash
      
         pip install mypackage
         ./mypackage-setup.sh

Advanced Code Inclusion
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Code Examples
   =============
   
   Complete Example
   ----------------
   
   .. advanced-include:: ../examples/complete.py
      :language: python
      :caption: Complete working example
      :name: complete-example
      :emphasize-lines: 10-15,25-30
      :dedent: 0
      :transform: optimize_imports
   
   Key Section
   -----------
   
   .. advanced-include:: ../examples/complete.py
      :language: python
      :lines: 50-100
      :caption: Key implementation section
      :linenos:
      :lineno-start: 50

Metadata-Driven Navigation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. advanced-metadata::
      :category: tutorial
      :difficulty: intermediate
      :duration: 30 minutes
      :prerequisites: python-basics
   
   Tutorial: Advanced Features
   ===========================
   
   This :duration:`30-minute` tutorial covers intermediate topics.
   
   Prerequisites:
   
   - :prereq:`python-basics`
   - :prereq:`sphinx-fundamentals`

Advanced Features
-----------------

Custom Transformations
~~~~~~~~~~~~~~~~~~~~~~

Define custom content transformers:

.. code-block:: python

   # conf.py
   from docutils import nodes
   from sphinx.transforms import SphinxTransform
   
   class CustomTransform(SphinxTransform):
       """Custom content transformer."""
       
       default_priority = 500
       
       def apply(self):
           """Apply transformation."""
           for node in self.document.traverse(nodes.paragraph):
               # Transform paragraphs
               self.process_paragraph(node)
       
       def process_paragraph(self, node):
           """Process paragraph node."""
           text = node.astext()
           # Custom processing
           if 'NOTE:' in text:
               note = nodes.note()
               note += nodes.paragraph(text=text.replace('NOTE:', ''))
               node.replace_self(note)
   
   def setup(app):
       app.add_transform(CustomTransform)

Custom Builders
~~~~~~~~~~~~~~~

Create custom output formats:

.. code-block:: python

   # conf.py
   from sphinx.builders import Builder
   from sphinx.util import logging
   
   logger = logging.getLogger(__name__)
   
   class CustomBuilder(Builder):
       """Custom documentation builder."""
       
       name = 'custom'
       format = 'custom'
       out_suffix = '.custom'
       
       def init(self):
           """Initialize builder."""
           self.output_dir = self.outdir
       
       def get_outdated_docs(self):
           """Return outdated documents."""
           for docname in self.env.found_docs:
               yield docname
       
       def write_doc(self, docname, doctree):
           """Write document."""
           output_path = self.output_dir / f'{docname}{self.out_suffix}'
           
           # Custom output generation
           content = self.render_document(doctree)
           
           with open(output_path, 'w', encoding='utf-8') as f:
               f.write(content)
           
           logger.info(f'Written: {output_path}')
       
       def render_document(self, doctree):
           """Render document to custom format."""
           # Implement custom rendering
           return str(doctree)
   
   def setup(app):
       app.add_builder(CustomBuilder)

Advanced Cross-References
~~~~~~~~~~~~~~~~~~~~~~~~~~

Complex linking systems:

.. code-block:: python

   # conf.py
   sphinx_advanced_xref_aliases = {
       'bug': 'https://github.com/user/repo/issues/{target}',
       'pr': 'https://github.com/user/repo/pull/{target}',
       'commit': 'https://github.com/user/repo/commit/{target}',
       'api': 'https://api.example.com/v1/{target}',
   }

.. code-block:: rst

   See :bug:`123` for details.
   
   Fixed in :pr:`456`.
   
   Changed in :commit:`abc123`.
   
   Endpoint: :api:`users/list`

Metadata Extraction
~~~~~~~~~~~~~~~~~~~

Extract and use document metadata:

.. code-block:: python

   # conf.py
   def extract_metadata(app, docname, source):
       """Extract metadata from documents."""
       metadata = {}
       
       # Parse metadata from source
       for line in source[0].split('\n'):
           if line.startswith(':meta '):
               key, value = line[6:].split(':', 1)
               metadata[key.strip()] = value.strip()
       
       # Store metadata
       app.env.metadata[docname] = metadata
   
   def setup(app):
       app.connect('source-read', extract_metadata)

Best Practices
--------------

Document Organization
~~~~~~~~~~~~~~~~~~~~~

Use metadata for organization:

.. code-block:: rst

   .. advanced-metadata::
      :category: guide
      :level: advanced
      :tags: performance, optimization
      :reviewed: true
      :last-updated: 2024-01-20

Performance Optimization
~~~~~~~~~~~~~~~~~~~~~~~~

Enable caching and parallel builds:

.. code-block:: python

   # conf.py
   sphinx_advanced_parallel_build = True
   sphinx_advanced_cache_enabled = True
   sphinx_advanced_cache_dir = '.sphinx_cache'
   
   # Optimize image processing
   sphinx_advanced_optimize_images = True
   sphinx_advanced_image_quality = 85

Content Reuse
~~~~~~~~~~~~~

Use advanced inclusion:

.. code-block:: rst

   .. advanced-include:: common/disclaimer.rst
      :transform: update_dates
   
   .. advanced-include:: api/endpoints.yaml
      :parser: yaml
      :template: endpoint-docs.rst

Troubleshooting
---------------

Build Failures
~~~~~~~~~~~~~~

**Problem**: Advanced features causing build errors

**Solution**:

.. code-block:: python

   # Enable debug logging
   sphinx_advanced_debug = True
   
   # Validate configuration
   sphinx_advanced_validate_config = True
   
   # Disable problematic features temporarily
   sphinx_advanced_features = ['xref', 'metadata']

Performance Issues
~~~~~~~~~~~~~~~~~~

**Problem**: Slow builds with advanced features

**Solution**:

.. code-block:: python

   # Enable parallel processing
   sphinx_advanced_parallel_build = True
   sphinx_advanced_parallel_workers = 4
   
   # Use caching
   sphinx_advanced_cache_enabled = True
   
   # Optimize transforms
   sphinx_advanced_transforms = ['essential_only']

Missing Features
~~~~~~~~~~~~~~~~

**Problem**: Advanced features not available

**Solution**:

.. code-block:: python

   # Check feature list
   sphinx_advanced_features = 'all'
   
   # Verify installation
   pip install --upgrade sphinx-advanced
   
   # Check compatibility
   sphinx_advanced_min_sphinx_version = '5.0'

Integration Examples
--------------------

With Custom Extensions
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   extensions = [
       'sphinx_advanced',
       'myextension',
   ]
   
   def setup(app):
       # Use advanced features in custom extension
       from sphinx_advanced import features
       
       if features.is_enabled('metadata'):
           app.connect('doctree-resolved', process_metadata)

With Multiple Builders
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Build multiple formats
   sphinx_advanced_builders = ['html', 'pdf', 'epub', 'markdown']
   
   # Builder-specific options
   sphinx_advanced_builder_options = {
       'html': {
           'theme': 'custom',
           'optimize': True,
       },
       'pdf': {
           'engine': 'xelatex',
           'papersize': 'a4',
       },
   }

With Continuous Integration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

   # .github/workflows/docs.yml
   name: Build Documentation
   
   on: [push, pull_request]
   
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v2
         
         - name: Set up Python
           uses: actions/setup-python@v2
           with:
             python-version: 3.9
         
         - name: Install dependencies
           run: |
             pip install sphinx sphinx-advanced
         
         - name: Build docs
           run: |
             sphinx-build -b html docs build/html
             sphinx-build -b pdf docs build/pdf

Advanced Usage
--------------

Multi-Version Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   version = '2.0'
   release = '2.0.1'
   
   # Version-specific content
   sphinx_advanced_version_config = {
       '1.0': {
           'deprecated': True,
           'redirect_to': '2.0',
       },
       '2.0': {
           'stable': True,
           'features': ['all'],
       },
   }

Dynamic Content Generation
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Generate content during build
   def generate_content(app):
       """Generate dynamic content."""
       output_dir = app.srcdir / 'generated'
       output_dir.mkdir(exist_ok=True)
       
       # Generate documentation
       for item in get_items():
           content = render_template('item.rst', item=item)
           (output_dir / f'{item.name}.rst').write_text(content)
   
   def setup(app):
       app.connect('builder-inited', generate_content)

Custom Validators
~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   from sphinx.application import Sphinx
   
   def validate_document(app: Sphinx, doctree, docname):
       """Custom document validation."""
       # Check for required metadata
       if docname not in app.env.metadata:
           app.warn(f'Missing metadata: {docname}')
       
       # Validate cross-references
       for node in doctree.traverse():
           if hasattr(node, 'rawsource'):
               validate_references(app, node)
   
   def setup(app):
       app.connect('doctree-resolved', validate_document)

See Also
--------

Related Extensions
~~~~~~~~~~~~~~~~~~

- :doc:`sphinx-autodoc-example` - Automatic documentation
- :doc:`sphinx-autobuild-example` - Live reload
- Sphinx Core: https://www.sphinx-doc.org/

External Resources
~~~~~~~~~~~~~~~~~~

- Sphinx Extension Tutorial: https://www.sphinx-doc.org/en/master/development/tutorials/
- Docutils Documentation: https://docutils.sourceforge.io/

Summary
-------

sphinx-advanced provides powerful advanced features:

- **Advanced Cross-Refs**: Sophisticated reference systems
- **Content Transforms**: Flexible content processing
- **Custom Builders**: Additional output formats
- **Metadata Management**: Rich document metadata
- **Build Optimization**: Performance improvements
- **Template Enhancement**: Advanced Jinja2 features
- **Extension API**: Powerful development tools
- **Validation**: Document quality checks

Perfect for complex documentation projects requiring advanced features and customization.
