Sphinx Extensions Guide
=======================

Sphinx extensions add powerful features to your documentation. This container includes 
dozens of useful extensions pre-installed.

Core Extensions
---------------

These extensions come with Sphinx itself.

autodoc
~~~~~~~

Automatically document Python code from docstrings.

**Configuration:**

.. code-block:: python

   extensions = ['sphinx.ext.autodoc']

**Usage:**

.. code-block:: rst

   .. automodule:: mypackage
      :members:
      :undoc-members:
      :show-inheritance:

   .. autoclass:: mypackage.MyClass
      :members:
      :special-members: __init__

   .. autofunction:: mypackage.my_function

**Example:**

Given this Python code:

.. code-block:: python

   def greet(name, greeting="Hello"):
       """Greet someone.
       
       Args:
           name (str): The name to greet
           greeting (str): The greeting to use
           
       Returns:
           str: The greeting message
       """
       return f"{greeting}, {name}!"

Document it with:

.. code-block:: rst

   .. autofunction:: mymodule.greet

napoleon
~~~~~~~~

Support for Google and NumPy style docstrings.

**Configuration:**

.. code-block:: python

   extensions = ['sphinx.ext.napoleon']
   
   napoleon_google_docstring = True
   napoleon_numpy_docstring = True
   napoleon_include_init_with_doc = True

**Google Style:**

.. code-block:: python

   def function(arg1, arg2):
       """Summary line.
       
       Args:
           arg1 (int): Description
           arg2 (str): Description
           
       Returns:
           bool: Description
           
       Raises:
           ValueError: Description
       """

**NumPy Style:**

.. code-block:: python

   def function(arg1, arg2):
       """Summary line.
       
       Parameters
       ----------
       arg1 : int
           Description
       arg2 : str
           Description
           
       Returns
       -------
       bool
           Description
       """

viewcode
~~~~~~~~

Add links to highlighted source code.

**Configuration:**

.. code-block:: python

   extensions = ['sphinx.ext.viewcode']

Adds "[source]" links next to documented functions and classes.

intersphinx
~~~~~~~~~~~

Link to other Sphinx documentation.

**Configuration:**

.. code-block:: python

   extensions = ['sphinx.ext.intersphinx']
   
   intersphinx_mapping = {
       'python': ('https://docs.python.org/3', None),
       'numpy': ('https://numpy.org/doc/stable/', None),
       'pandas': ('https://pandas.pydata.org/docs/', None),
   }

**Usage:**

.. code-block:: rst

   See :class:`python:dict` and :func:`numpy:numpy.array`

graphviz
~~~~~~~~

Embed Graphviz graphs.

**Configuration:**

.. code-block:: python

   extensions = ['sphinx.ext.graphviz']
   graphviz_output_format = 'svg'

**Usage:**

.. code-block:: rst

   .. graphviz::

      digraph {
          "Start" -> "Process" -> "End";
      }

Popular Third-Party Extensions
-------------------------------

MyST Parser
~~~~~~~~~~~

Write documentation in Markdown instead of reStructuredText.

**Configuration:**

.. code-block:: python

   extensions = ['myst_parser']
   
   source_suffix = {
       '.rst': 'restructuredtext',
       '.md': 'markdown',
   }
   
   myst_enable_extensions = [
       "colon_fence",
       "deflist",
       "substitution",
       "tasklist",
   ]

**Usage:**

Create ``page.md``:

.. code-block:: markdown

   # My Page
   
   This is **bold** and *italic*.
   
   ```python
   def hello():
       print("Hello!")
   ```
   
   See {doc}`other-page` for more.

sphinx-copybutton
~~~~~~~~~~~~~~~~~

Add copy buttons to code blocks.

**Configuration:**

.. code-block:: python

   extensions = ['sphinx_copybutton']
   
   copybutton_prompt_text = ">>> "
   copybutton_prompt_is_regexp = True

Automatically adds a copy button to all code blocks!

sphinx-autoapi
~~~~~~~~~~~~~~

Automatic API documentation (alternative to autodoc).

**Configuration:**

.. code-block:: python

   extensions = ['autoapi.extension']
   
   autoapi_type = 'python'
   autoapi_dirs = ['../src']
   autoapi_options = [
       'members',
       'undoc-members',
       'show-inheritance',
       'show-module-summary',
   ]

**Advantages:**

* Doesn't require importing code
* Generates full API reference automatically
* Better for large projects

nbsphinx
~~~~~~~~

Include Jupyter Notebooks in documentation.

**Configuration:**

.. code-block:: python

   extensions = ['nbsphinx']
   
   nbsphinx_execute = 'never'  # or 'always', 'auto'

**Usage:**

.. code-block:: rst

   .. toctree::
   
      tutorial.ipynb
      examples.ipynb

sphinxcontrib-httpdomain
~~~~~~~~~~~~~~~~~~~~~~~~

Document HTTP APIs.

**Configuration:**

.. code-block:: python

   extensions = ['sphinxcontrib.httpdomain']

**Usage:**

.. code-block:: rst

   .. http:get:: /users/(int:user_id)/posts
   
      Get posts for a user.
      
      **Example request**:
      
      .. sourcecode:: http
      
         GET /users/123/posts HTTP/1.1
         Host: example.com
      
      **Example response**:
      
      .. sourcecode:: http
      
         HTTP/1.1 200 OK
         Content-Type: application/json
         
         {
           "posts": [...]
         }
      
      :param user_id: The user's ID
      :statuscode 200: Success
      :statuscode 404: User not found

sphinx-autobuild
~~~~~~~~~~~~~~~~

Automatically rebuild and reload documentation.

**Usage:**

.. code-block:: bash

   docker run -p 8000:8000 -v $(pwd):/project kensai-sphinx \
       sphinx-autobuild /project/docs /project/docs/_build/html \
       --host 0.0.0.0 --port 8000

Visit ``http://localhost:8000`` - changes appear automatically!

sphinxext-opengraph
~~~~~~~~~~~~~~~~~~~

Generate OpenGraph metadata for social media sharing.

**Configuration:**

.. code-block:: python

   extensions = ['sphinxext.opengraph']
   
   ogp_site_url = "https://example.com/docs/"
   ogp_image = "https://example.com/docs/_static/logo.png"
   ogp_description_length = 200

sphinx-hoverxref
~~~~~~~~~~~~~~~~

Show tooltips when hovering over cross-references.

**Configuration:**

.. code-block:: python

   extensions = ['hoverxref.extension']
   
   hoverxref_auto_ref = True
   hoverxref_domains = ['py']
   hoverxref_role_types = {
       'ref': 'tooltip',
       'class': 'tooltip',
       'func': 'tooltip',
   }

Specialized Extensions
----------------------

sphinx-charts
~~~~~~~~~~~~~

Embed interactive charts.

**Usage:**

.. code-block:: rst

   .. charts::
      :type: bar
      :data: data.json

sphinx-git
~~~~~~~~~~

Show git commit information.

**Configuration:**

.. code-block:: python

   extensions = ['sphinx_git']

**Usage:**

.. code-block:: rst

   .. git_changelog::
      :revisions: 10

sphinx-last-updated-by-git
~~~~~~~~~~~~~~~~~~~~~~~~~~

Show "Last updated" based on git commits.

**Configuration:**

.. code-block:: python

   extensions = ['sphinx_last_updated_by_git']

Adds last update timestamp to each page.

Extension Configuration Examples
---------------------------------

Minimal Setup
~~~~~~~~~~~~~

.. code-block:: python

   extensions = [
       'sphinx.ext.autodoc',
       'sphinx.ext.napoleon',
       'sphinx.ext.viewcode',
   ]

Python Project
~~~~~~~~~~~~~~

.. code-block:: python

   extensions = [
       'sphinx.ext.autodoc',
       'sphinx.ext.napoleon',
       'sphinx.ext.viewcode',
       'sphinx.ext.intersphinx',
       'sphinx_copybutton',
       'autoapi.extension',
   ]
   
   intersphinx_mapping = {
       'python': ('https://docs.python.org/3', None),
   }
   
   autoapi_dirs = ['../src']

Web API Documentation
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = [
       'sphinxcontrib.httpdomain',
       'sphinxext.opengraph',
       'sphinx_copybutton',
   ]
   
   ogp_site_url = "https://api.example.com/docs/"

Tutorial/Book
~~~~~~~~~~~~~

.. code-block:: python

   extensions = [
       'myst_parser',
       'nbsphinx',
       'sphinx_copybutton',
       'sphinx.ext.graphviz',
       'sphinxemoji.sphinxemoji',
   ]
   
   myst_enable_extensions = [
       "colon_fence",
       "deflist",
       "tasklist",
   ]

Creating Custom Extensions
---------------------------

Simple Extension
~~~~~~~~~~~~~~~~

Create ``_ext/my_extension.py``:

.. code-block:: python

   def setup(app):
       app.add_config_value('my_option', 'default', 'html')
       return {
           'version': '0.1',
           'parallel_read_safe': True,
           'parallel_write_safe': True,
       }

Load in ``conf.py``:

.. code-block:: python

   import sys, os
   sys.path.insert(0, os.path.abspath('_ext'))
   
   extensions = ['my_extension']
   
   my_option = 'custom value'

Best Practices
--------------

1. **Only Enable What You Need**: Too many extensions slow builds
2. **Read the Docs**: Each extension has specific configuration
3. **Test Thoroughly**: Some extensions may conflict
4. **Keep Updated**: Update extensions with Sphinx
5. **Check Compatibility**: Ensure extensions work with your Sphinx version

Troubleshooting
---------------

Extension Not Found
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Install missing extension
   docker run kensai-sphinx pip install sphinx-extension-name
   
   # Or add to requirements.txt and rebuild

Build Errors
~~~~~~~~~~~~

.. code-block:: bash

   # Build with verbose output
   docker run -v $(pwd):/project kensai-sphinx \
       sphinx-build -v -b html /project/docs /project/docs/_build/html

Resources
---------

* `Sphinx Extensions Documentation <https://www.sphinx-doc.org/en/master/usage/extensions/>`_
* `Sphinx Contrib <https://github.com/sphinx-contrib/>`_
* `Awesome Sphinx <https://github.com/yoloseem/awesome-sphinxdoc>`_

Video Tutorial
--------------

.. raw:: html

   <iframe width="560" height="315" 
   src="https://www.youtube.com/embed/BWIrhgCAae0" 
   title="Sphinx Extensions Tutorial" 
   frameborder="0" 
   allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
   allowfullscreen></iframe>
