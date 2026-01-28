Sphinx-Hoverxref Tutorial
=========================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-hoverxref/>`_
   - `API Documentation <../../pdoc/sphinx_hoverxref/index.html>`_
   - `Manual <https://sphinx-hoverxref.readthedocs.io/>`_
   - :doc:`Working Example <../../examples/sphinx-hoverxref-example>`


.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinx-hoverxref to add tooltip previews when hovering over cross-references.

What is Sphinx-Hoverxref?
--------------------------
sphinx-hoverxref is a Sphinx extension that provides:

- Tooltip previews on hover
- Cross-reference previews
- Modal popups for content
- Smooth user experience
- API reference tooltips
- Documentation previews
- Read the Docs integration
- Customizable styling
- Multiple tooltip types
- Lazy loading support

This enhances documentation by showing reference content without navigating away from the current page.

The sphinx-hoverxref extension adds interactive tooltips that display the content of cross-referenced sections, allowing readers to preview content without navigating away from the current page.


Installation
------------

sphinx-hoverxref is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinx_hoverxref; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_hoverxref.extension',
   ]
   
   # Basic configuration
   hoverxref_auto_ref = True
   hoverxref_domains = ['py']
   hoverxref_role_types = {
       'ref': 'tooltip',
       'doc': 'tooltip',
   }

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinx_hoverxref.extension']
   
   # Automatic reference detection
   hoverxref_auto_ref = True
   
   # Domains to enable hoverxref for
   hoverxref_domains = ['py', 'js', 'cpp', 'std']
   
   # Role types configuration
   hoverxref_role_types = {
       'ref': 'tooltip',        # :ref: shows tooltip
       'doc': 'tooltip',        # :doc: shows tooltip
       'class': 'tooltip',      # :class: shows tooltip
       'func': 'tooltip',       # :func: shows tooltip
       'meth': 'modal',         # :meth: shows modal
       'attr': 'tooltip',       # :attr: shows tooltip
       'exc': 'tooltip',        # :exc: shows tooltip
       'mod': 'modal',          # :mod: shows modal
   }
   
   # Tooltip configuration
   hoverxref_tooltip_maxwidth = 600
   hoverxref_tooltip_animation = 'fade'
   hoverxref_tooltip_theme = 'tooltipster-shadow'
   
   # Modal configuration
   hoverxref_modal_maxwidth = 800
   hoverxref_modal_class = 'hoverxref-modal'
   
   # API URL (for Read the Docs)
   hoverxref_api_host = 'https://readthedocs.org'
   
   # Tooltip content
   hoverxref_tooltip_lazy = True
   hoverxref_tooltip_hover_delay = 500

Basic Usage
-----------

Automatic Tooltips
~~~~~~~~~~~~~~~~~~

With ``hoverxref_auto_ref = True``, standard cross-references automatically get tooltips:

.. code-block:: rst

   See :ref:`installation` for setup instructions.
   
   Check out the :class:`MyClass` documentation.
   
   Use the :func:`process_data` function.

Hovering over these references shows a tooltip with the referenced content.

Explicit Hoverxref Roles
~~~~~~~~~~~~~~~~~~~~~~~~~

Use explicit roles:

.. code-block:: rst

   See :hoverxref:`installation guide <installation>`.
   
   The :hoverxref:`MyClass <api.MyClass>` handles data processing.

   API Reference
   =============
   
   .. _api-client:
   
   Client Class
   ------------
   
   .. class:: Client(api_key, timeout=30)
      
      Main client for API interactions.
      
      :param api_key: Your API authentication key
      :param timeout: Request timeout in seconds
      
      .. method:: get(endpoint)
         
         Fetch data from an endpoint.
         
         :param endpoint: API endpoint path
         :return: Response data
         :raises: ConnectionError if request fails
      
      .. method:: post(endpoint, data)
         
         Send data to an endpoint.
         
         :param endpoint: API endpoint path
         :param data: Data to send
         :return: Response data

``docs/quickstart.rst``:

.. code-block:: rst

   Quick Start
   ===========
   
   Create a :class:`Client` instance with your API key.
   
   Use the :meth:`Client.get` method to fetch data.
   
   For sending data, use :meth:`Client.post`.
   
   See the complete :ref:`API reference <api-client>` for details.

``docs/conf.py``:

.. code-block:: python

   hoverxref_auto_ref = True
   hoverxref_domains = ['py', 'std']
   hoverxref_role_types = {
       'class': 'tooltip',
       'meth': 'tooltip',
       'ref': 'modal',  # Full section in modal
   }

Example 2: Glossary with Tooltips
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/glossary.rst``:

.. code-block:: rst

   Glossary
   ========
   
   .. glossary::
      
      API
         Application Programming Interface - a set of protocols
         and tools for building software applications.
      
      REST
         Representational State Transfer - an architectural style
         for distributed hypermedia systems.
      
      JSON
         JavaScript Object Notation - a lightweight data
         interchange format.
      
      Authentication
         The process of verifying the identity of a user or
         application accessing the API.

``docs/usage.rst``:

.. code-block:: rst

   Usage Guide
   ===========
   
   Our :term:`API` uses :term:`REST` principles and returns data
   in :term:`JSON` format.
   
   All requests require :term:`authentication` using an API key.

``docs/conf.py``:

.. code-block:: python

   hoverxref_role_types = {
       'term': 'tooltip',
   }
   hoverxref_tooltip_maxwidth = 400

Example 3: Code Examples with Modal Previews
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/examples/basic.rst``:

.. code-block:: rst

   .. _example-basic:
   
   Basic Usage Example
   ===================
   
   .. code-block:: python
      
      from mylib import Client
      
      # Initialize client
      client = Client(api_key='your-key')
      
      # Fetch data
      data = client.get('/users')
      
      # Process results
      for user in data:
          print(user['name'])

``docs/examples/advanced.rst``:

.. code-block:: rst

   .. _example-advanced:
   
   Advanced Usage Example
   ======================
   
   .. code-block:: python
      
      from mylib import Client
      import asyncio
      
      async def fetch_multiple():
          client = Client(api_key='your-key')
          
          # Parallel requests
          users = await client.async_get('/users')
          posts = await client.async_get('/posts')
          
          return users, posts
      
      # Run async
      asyncio.run(fetch_multiple())

``docs/tutorial.rst``:

.. code-block:: rst

   Tutorial
   ========
   
   Start with the :ref:`basic example <example-basic>` to understand
   the fundamentals.
   
   Then explore the :ref:`advanced example <example-advanced>` for
   asynchronous operations.

``docs/conf.py``:

.. code-block:: python

   hoverxref_role_types = {
       'ref': 'modal',  # Show full example in modal
   }
   hoverxref_modal_maxwidth = 900

Example 4: Custom Tooltip Styling
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/conf.py``:

.. code-block:: python

   hoverxref_tooltip_theme = 'tooltipster-custom'
   hoverxref_tooltip_animation = 'grow'
   hoverxref_tooltip_maxwidth = 500

``docs/_static/custom-tooltips.css``:

.. code-block:: css

   /* Custom tooltip theme */
   .tooltipster-custom {
       border-radius: 8px;
       border: 2px solid #3498db;
       background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
       color: white;
       box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
   }
   
   .tooltipster-custom .tooltipster-content {
       font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
       padding: 12px 16px;
       font-size: 14px;
       line-height: 1.6;
   }
   
   .tooltipster-custom .tooltipster-content code {
       background-color: rgba(255, 255, 255, 0.2);
       padding: 2px 6px;
       border-radius: 3px;
       font-family: 'Courier New', monospace;
   }
   
   /* Modal customization */
   .hoverxref-modal {
       border-radius: 12px;
       box-shadow: 0 20px 60px rgba(0, 0, 0, 0.4);
   }
   
   .hoverxref-modal-content {
       padding: 24px;
       max-height: 600px;
       overflow-y: auto;
   }

``docs/conf.py``:

.. code-block:: python

   html_css_files = ['custom-tooltips.css']

Advanced Features
-----------------

Lazy Loading Tooltips
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Load tooltip content only when hovered
   hoverxref_tooltip_lazy = True
   hoverxref_tooltip_hover_delay = 300  # ms

Read the Docs Integration
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import os
   
   # Detect Read the Docs
   on_rtd = os.environ.get('READTHEDOCS') == 'True'
   
   if on_rtd:
       hoverxref_api_host = 'https://readthedocs.org'
       hoverxref_project = 'myproject'
       hoverxref_version = 'latest'

Intersphinx with Hoverxref
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = [
       'sphinx.ext.intersphinx',
       'sphinx_hoverxref.extension',
   ]
   
   # Intersphinx configuration
   intersphinx_mapping = {
       'python': ('https://docs.python.org/3', None),
       'requests': ('https://requests.readthedocs.io/en/latest/', None),
   }
   
   # Enable hoverxref for intersphinx
   hoverxref_intersphinx = [
       'python',
       'requests',
   ]
   
   hoverxref_intersphinx_types = {
       'python': {
           'class': 'tooltip',
           'func': 'tooltip',
       },
   }

Selective Hoverxref
~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Regular link: :ref:`installation`
   
   Tooltip preview: :hoverxref:`installation guide <installation>`
   
   Modal preview: :hoverxreftooltip:`installation <installation>`

Docker Integration
------------------

Build with Hoverxref
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     kensai-sphinx:latest \
     sphinx-build -b html /project/docs /project/docs/_build/html

Serve and Test
~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     -p 8000:8000 \
     kensai-sphinx:latest \
     sh -c "cd /project/docs/_build/html && python -m http.server 8000"
   
   # Test tooltips at http://localhost:8000

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Build Docs with Hoverxref
   
   on: [push]
   
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Build Documentation
           run: |
             docker run --rm -v $(pwd):/project \
               kensai-sphinx:latest \
               sphinx-build -b html /project/docs /project/docs/_build/html
         
         - name: Test Hoverxref
           run: |
             # Check hoverxref JavaScript is included
             if ! grep -q "hoverxref" docs/_build/html/index.html; then
               echo "Hoverxref not found in output!"
               exit 1
             fi
         
         - name: Deploy
           uses: peaceiris/actions-gh-pages@v3
           with:
             github_token: ${{ secrets.GITHUB_TOKEN }}
             publish_dir: ./docs/_build/html

Best Practices
--------------

1. **Use Wisely**
   
   Don't overuse tooltips - focus on frequently referenced items

2. **Choose Right Type**
   
   Tooltips for brief content, modals for detailed content

3. **Performance**
   
   Enable lazy loading for large documentation

4. **Accessibility**
   
   Ensure tooltips work with keyboard navigation

5. **Test Thoroughly**
   
   Verify tooltips on different devices

6. **Keep Content Brief**
   
   Tooltip content should be concise

Troubleshooting
---------------

Tooltips Not Showing
~~~~~~~~~~~~~~~~~~~~

**Solution:**

Check JavaScript console for errors. Ensure extension is loaded:

.. code-block:: python

   extensions = ['sphinx_hoverxref.extension']

Content Too Large
~~~~~~~~~~~~~~~~~

**Solution:**

Adjust maxwidth or use modal:

.. code-block:: python

   hoverxref_tooltip_maxwidth = 800
   # or
   hoverxref_role_types = {
       'ref': 'modal',
   }

Slow Performance
~~~~~~~~~~~~~~~~

**Solution:**

Enable lazy loading:

.. code-block:: python

   hoverxref_tooltip_lazy = True

Styling Conflicts
~~~~~~~~~~~~~~~~~

**Solution:**

Use custom theme:

.. code-block:: python

   hoverxref_tooltip_theme = 'tooltipster-custom'

Read the Docs Issues
~~~~~~~~~~~~~~~~~~~~

**Solution:**

Configure API host:

.. code-block:: python

   hoverxref_api_host = 'https://readthedocs.org'

Next Steps
----------

1. Enable hoverxref extension
2. Configure role types
3. Test tooltips locally
4. Customize styling
5. Deploy and verify

Additional Resources
--------------------

- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `sphinx-hoverxref Documentation <https://sphinx-hoverxref.readthedocs.io/>`_
- `Tooltipster Documentation <http://iamceege.github.io/tooltipster/>`_
