Sphinx-Advanced Tutorial
========================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-advanced/>`_
   - `API Documentation <../../pdoc/sphinx_advanced/index.html>`_
   - `Manual <https://github.com/sphinx-contrib/advanced>`_
   - :doc:`Working Example <../../examples/sphinx-advanced-example>`


.. contents:: Table of Contents
   :local:
   :depth: 2

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


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
