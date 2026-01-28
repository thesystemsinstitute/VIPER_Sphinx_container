Sphinx-Advanced Tutorial
========================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-advanced/>`_
   - :doc:`See Working Example <../../examples/sphinx-advanced-example>`


This tutorial demonstrates how to use sphinx-advanced for advanced Sphinx features and customizations.

What is Sphinx-Advanced?
-------------------------

sphinx-advanced is a Sphinx extension that provides:

- Advanced directives
- Custom roles
- Enhanced cross-referencing
- Template enhancements
- Build customization
- Event hooks
- Custom builders
- Domain extensions
- Transform chains
- Plugin architecture

This enables sophisticated documentation workflows and custom functionality.

Installation
------------

sphinx-advanced is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinx_advanced; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``docs/conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_advanced',
   ]
   
   # Advanced features
   advanced_features = ['custom-directives', 'enhanced-roles']

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinx_advanced']
   
   # Feature flags
   advanced_features = [
       'custom-directives',
       'enhanced-roles',
       'advanced-transforms',
       'custom-builders',
   ]
   
   # Custom directives
   advanced_directive_options = {
       'strict': True,
       'allow_nesting': True,
   }
   
   # Enhanced cross-referencing
   advanced_xref_options = {
       'auto_resolve': True,
       'fuzzy_matching': True,
   }

Basic Usage
-----------

Custom Directives
~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. advanced-note::
      :icon: info
      :color: blue
      
      This is an advanced note with custom styling.

Enhanced Cross-References
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   See :smartref:`installation guide` for setup instructions.

Custom Roles
~~~~~~~~~~~~

.. code-block:: rst

   Use the :badge:`new` feature for better performance.

Practical Examples
------------------

Example 1: Custom Admonition Directives
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/conf.py``:

.. code-block:: python

   from docutils import nodes
   from docutils.parsers.rst import Directive
   from sphinx.util.docutils import SphinxDirective
   
   class TipDirective(SphinxDirective):
       """Custom tip directive with icon."""
       
       has_content = True
       required_arguments = 0
       optional_arguments = 1
       option_spec = {
           'icon': str,
           'title': str,
       }
       
       def run(self):
           # Get options
           icon = self.options.get('icon', '💡')
           title = self.options.get('title', 'Tip')
           
           # Create container
           container = nodes.container()
           container['classes'].append('custom-tip')
           
           # Add title
           title_node = nodes.paragraph()
           title_node += nodes.Text(f'{icon} {title}')
           title_node['classes'].append('tip-title')
           
           # Add content
           self.state.nested_parse(self.content, self.content_offset, container)
           
           # Insert title at beginning
           container.insert(0, title_node)
           
           return [container]
   
   def setup(app):
       app.add_directive('tip', TipDirective)
       app.add_css_file('custom-admonitions.css')

``docs/_static/custom-admonitions.css``:

.. code-block:: css

   .custom-tip {
       padding: 15px 20px;
       margin: 20px 0;
       border-left: 4px solid #3498db;
       background-color: #e8f4f8;
       border-radius: 4px;
   }
   
   .custom-tip .tip-title {
       font-weight: bold;
       font-size: 1.1em;
       color: #2c3e50;
       margin-bottom: 10px;
   }

``docs/guide.rst``:

.. code-block:: rst

   User Guide
   ==========
   
   .. tip::
      :icon: 🚀
      :title: Pro Tip
      
      Use keyboard shortcuts for faster navigation!

Example 2: Smart Cross-References
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/conf.py``:

.. code-block:: python

   from sphinx.roles import XRefRole
   
   class SmartRefRole(XRefRole):
       """Smart reference that tries multiple strategies."""
       
       def process_link(self, env, refnode, has_explicit_title, title, target):
           # Try direct reference
           if env.get_doctree(target):
               return title, target
           
           # Try with .rst extension
           if env.get_doctree(f'{target}.rst'):
               return title, f'{target}.rst'
           
           # Fuzzy search in all documents
           for docname in env.found_docs:
               if target.lower() in docname.lower():
                   return title, docname
           
           # Fall back to original
           return title, target
   
   def setup(app):
       app.add_role('smartref', SmartRefRole())

Usage:

.. code-block:: rst

   See :smartref:`installation` - finds docs/installation.rst
   See :smartref:`user guide` - finds docs/guides/user-guide.rst

Example 3: Custom Builder
~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/conf.py``:

.. code-block:: python

   from sphinx.builders import Builder
   from sphinx.util.fileutil import copy_asset_file
   import json
   
   class JSONBuilder(Builder):
       """Build JSON representation of documentation."""
       
       name = 'json'
       format = 'json'
       out_suffix = '.json'
       
       def init(self):
           pass
       
       def get_outdated_docs(self):
           return self.env.found_docs
       
       def write_doc(self, docname, doctree):
           """Write document as JSON."""
           destination = self.outdir / f'{docname}.json'
           
           # Convert doctree to dict
           doc_data = {
               'title': self.env.titles[docname].astext(),
               'toc': self.env.tocs[docname].astext(),
               'body': doctree.astext(),
               'metadata': self.env.metadata.get(docname, {}),
           }
           
           # Write JSON
           with open(destination, 'w') as f:
               json.dump(doc_data, f, indent=2)
       
       def finish(self):
           """Create index."""
           index = {
               'documents': list(self.env.found_docs),
               'metadata': self.env.metadata,
           }
           
           with open(self.outdir / 'index.json', 'w') as f:
               json.dump(index, f, indent=2)
   
   def setup(app):
       app.add_builder(JSONBuilder)

Build JSON docs:

.. code-block:: bash

   sphinx-build -b json docs docs/_build/json

Example 4: Transform Chain
~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/conf.py``:

.. code-block:: python

   from docutils import nodes
   from sphinx.transforms import SphinxTransform
   
   class AddReadingTime(SphinxTransform):
       """Add estimated reading time to pages."""
       
       default_priority = 500
       
       def apply(self):
           # Count words
           text = self.document.astext()
           word_count = len(text.split())
           
           # Calculate reading time (200 wpm)
           reading_time = max(1, word_count // 200)
           
           # Create reading time node
           para = nodes.paragraph()
           para += nodes.Text(f'📖 Estimated reading time: {reading_time} min')
           para['classes'].append('reading-time')
           
           # Insert at beginning
           if self.document.children:
               self.document.insert(1, para)
   
   class HighlightCodeBlocks(SphinxTransform):
       """Add copy buttons to code blocks."""
       
       default_priority = 600
       
       def apply(self):
           for node in self.document.traverse(nodes.literal_block):
               # Add copy button class
               if 'classes' not in node:
                   node['classes'] = []
               node['classes'].append('has-copy-button')
   
   def setup(app):
       app.add_transform(AddReadingTime)
       app.add_transform(HighlightCodeBlocks)

Example 5: Event Hooks
~~~~~~~~~~~~~~~~~~~~~~~

``docs/conf.py``:

.. code-block:: python

   import datetime
   
   def on_build_finished(app, exception):
       """Post-build processing."""
       if exception is None:
           print(f"✓ Build completed at {datetime.datetime.now()}")
           
           # Generate sitemap
           sitemap = []
           for docname in app.env.found_docs:
               url = f"{app.config.html_baseurl}/{docname}.html"
               sitemap.append(url)
           
           sitemap_file = app.outdir / 'sitemap.txt'
           with open(sitemap_file, 'w') as f:
               f.write('\n'.join(sitemap))
   
   def on_source_read(app, docname, source):
       """Process source before parsing."""
       # Add automatic last-updated notice
       if source[0]:
           source[0] = f".. meta::\n   :last-updated: {datetime.date.today()}\n\n{source[0]}"
   
   def on_doctree_resolved(app, doctree, docname):
       """Process doctree after resolution."""
       # Add custom metadata
       for node in doctree.traverse(nodes.section):
           if 'ids' in node:
               # Add anchor links
               node['data-section-id'] = node['ids'][0]
   
   def setup(app):
       app.connect('build-finished', on_build_finished)
       app.connect('source-read', on_source_read)
       app.connect('doctree-resolved', on_doctree_resolved)

Advanced Features
-----------------

Custom Domain
~~~~~~~~~~~~~

.. code-block:: python

   from sphinx.domains import Domain, ObjType
   from sphinx.roles import XRefRole
   
   class RecipeDomain(Domain):
       """Domain for recipe documentation."""
       
       name = 'recipe'
       label = 'Recipe'
       
       object_types = {
           'ingredient': ObjType('ingredient', 'ing'),
           'dish': ObjType('dish', 'dish'),
       }
       
       directives = {
           'ingredient': IngredientDirective,
           'dish': DishDirective,
       }
       
       roles = {
           'ing': XRefRole(),
           'dish': XRefRole(),
       }

Parallel Processing
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   from multiprocessing import cpu_count
   
   # Enable parallel reading
   parallel_read_safe = True
   parallel_write_safe = True
   
   # Use all CPUs
   numjobs = cpu_count()

Custom Warnings
~~~~~~~~~~~~~~~

.. code-block:: python

   def check_links(app, doctree, docname):
       """Check for broken internal links."""
       for node in doctree.traverse(nodes.reference):
           if 'refuri' in node:
               target = node['refuri']
               if target.startswith('#'):
                   # Check internal reference
                   if target[1:] not in doctree.ids:
                       app.warn(f'Broken link in {docname}: {target}')
   
   def setup(app):
       app.connect('doctree-resolved', check_links)

Docker Integration
------------------

Build with Advanced Features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     kensai-sphinx:latest \
     sphinx-build -b html /project/docs /project/docs/_build/html

Custom Builder
~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     kensai-sphinx:latest \
     sphinx-build -b json /project/docs /project/docs/_build/json

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Build Advanced Docs
   
   on: [push]
   
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Build HTML
           run: |
             docker run --rm -v $(pwd):/project \
               kensai-sphinx:latest \
               sphinx-build -b html /project/docs /project/docs/_build/html
         
         - name: Build JSON
           run: |
             docker run --rm -v $(pwd):/project \
               kensai-sphinx:latest \
               sphinx-build -b json /project/docs /project/docs/_build/json
         
         - name: Deploy
           uses: peaceiris/actions-gh-pages@v3
           with:
             github_token: ${{ secrets.GITHUB_TOKEN }}
             publish_dir: ./docs/_build/html

Best Practices
--------------

1. **Test Extensions**
   
   Thoroughly test custom code

2. **Handle Errors**
   
   Graceful error handling

3. **Document Features**
   
   Clear usage documentation

4. **Version Control**
   
   Track custom code

5. **Performance**
   
   Optimize transforms

6. **Compatibility**
   
   Test with Sphinx versions

Troubleshooting
---------------

Extension Not Loading
~~~~~~~~~~~~~~~~~~~~~

**Solution:**

Check setup function:

.. code-block:: python

   def setup(app):
       app.add_directive('custom', CustomDirective)
       return {'version': '1.0', 'parallel_read_safe': True}

Directive Not Found
~~~~~~~~~~~~~~~~~~~

**Solution:**

Verify registration:

.. code-block:: python

   app.add_directive('directive-name', DirectiveClass)

Transform Not Applied
~~~~~~~~~~~~~~~~~~~~~

**Solution:**

Check priority:

.. code-block:: python

   class MyTransform(SphinxTransform):
       default_priority = 500  # Adjust as needed

Build Errors
~~~~~~~~~~~~

**Solution:**

Enable verbose output:

.. code-block:: bash

   sphinx-build -v -b html docs docs/_build/html

Next Steps
----------

1. Learn Sphinx extension API
2. Create custom directives
3. Add transforms
4. Test thoroughly
5. Document usage

Additional Resources
--------------------

- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `Sphinx Extension Development <https://www.sphinx-doc.org/en/master/development/index.html>`_
- `Docutils Documentation <https://docutils.sourceforge.io/>`_
