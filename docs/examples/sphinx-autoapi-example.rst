Sphinx-AutoAPI Example
======================

This page demonstrates the **sphinx-autoapi** extension for automatically generating API documentation from source code.

.. contents:: Contents
   :local:
   :depth: 2

Overview
--------

The sphinx-autoapi extension automatically generates comprehensive API documentation by parsing source code, supporting Python, .NET, JavaScript, and Go.

Basic Configuration
-------------------

Python Project
~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   extensions = [
       'autoapi.extension',
   ]
   
   autoapi_type = 'python'
   autoapi_dirs = ['../mypackage']

Multiple Packages
~~~~~~~~~~~~~~~~~

.. code-block:: python

   autoapi_dirs = [
       '../package1',
       '../package2',
       '../package3',
   ]

Output Configuration
--------------------

Custom Output Directory
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Generate to custom directory
   autoapi_root = 'api'  # docs/api/
   
   # Default is 'autoapi'

Template Customization
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   autoapi_template_dir = '_templates/autoapi'

Generation Options
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Don't generate if no changes
   autoapi_generate_api_docs = True
   
   # Keep generated files
   autoapi_keep_files = True
   
   # Add to toctree automatically
   autoapi_add_toctree_entry = True

Content Filtering
-----------------

Include/Exclude Patterns
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Exclude patterns
   autoapi_ignore = [
       '*/tests/*',
       '*/migrations/*',
       '*/_private/*',
       '*/conftest.py',
   ]

Member Options
~~~~~~~~~~~~~~

.. code-block:: python

   # What to document
   autoapi_options = [
       'members',
       'undoc-members',
       'private-members',
       'show-inheritance',
       'show-module-summary',
       'special-members',
       'imported-members',
   ]

Skip Certain Members
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   def skip_member(app, what, name, obj, skip, options):
       """Skip private and test members."""
       if name.startswith('_') and not name.startswith('__'):
           return True
       if name.startswith('test_'):
           return True
       return skip

   def setup(app):
       app.connect('autoapi-skip-member', skip_member)

Python-Specific Options
-----------------------

Type Annotations
~~~~~~~~~~~~~~~~

.. code-block:: python

   # Show type annotations
   autoapi_python_use_implicit_namespaces = True
   
   # Use napoleon for docstrings
   extensions = [
       'autoapi.extension',
       'sphinx.ext.napoleon',
   ]

Import Resolution
~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Python class resolution
   autoapi_python_class_content = 'both'  # 'class', 'init', 'both'

Package Organization
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Show module summary
   autoapi_member_order = 'groupwise'  # 'alphabetical', 'bysource'
   
   # Show inheritance
   autoapi_options = ['show-inheritance', 'show-module-summary']

Documentation Formats
---------------------

Google Style
~~~~~~~~~~~~

.. code-block:: python

   def example_function(param1, param2):
       """Example function with Google-style docstring.
       
       Args:
           param1 (str): The first parameter.
           param2 (int): The second parameter.
       
       Returns:
           bool: True if successful, False otherwise.
       
       Raises:
           ValueError: If param2 is negative.
       """
       pass

NumPy Style
~~~~~~~~~~~

.. code-block:: python

   def numpy_function(param1, param2):
       """Example function with NumPy-style docstring.
       
       Parameters
       ----------
       param1 : str
           The first parameter.
       param2 : int
           The second parameter.
       
       Returns
       -------
       bool
           True if successful, False otherwise.
       
       Raises
       ------
       ValueError
           If param2 is negative.
       """
       pass

Sphinx Style
~~~~~~~~~~~~

.. code-block:: python

   def sphinx_function(param1, param2):
       """Example function with Sphinx-style docstring.
       
       :param param1: The first parameter
       :type param1: str
       :param param2: The second parameter
       :type param2: int
       :return: True if successful, False otherwise
       :rtype: bool
       :raises ValueError: If param2 is negative
       """
       pass

Advanced Configuration
----------------------

Custom Rendering
~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   def autoapi_prepare_jinja_env(jinja_env):
       """Customize Jinja environment."""
       jinja_env.globals['custom_filter'] = lambda x: x.upper()

   def setup(app):
       app.connect('autoapi-prepare-jinja-env', autoapi_prepare_jinja_env)

Modify Generated Content
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   def modify_autoapi_content(app, what, name, obj, options, lines):
       """Modify generated documentation."""
       if what == "class":
           lines.insert(0, ".. note:: This is an auto-generated class.")

   def setup(app):
       app.connect('autoapi-process-docstring', modify_autoapi_content)

Integration Examples
--------------------

With Type Hints
~~~~~~~~~~~~~~~

.. code-block:: python

   from typing import List, Dict, Optional

   class DataProcessor:
       """Process and transform data.
       
       Attributes:
           data: The data to process
           options: Processing options
       """
       
       def __init__(
           self,
           data: List[Dict[str, Any]],
           options: Optional[Dict[str, Any]] = None
       ):
           """Initialize the processor.
           
           Args:
               data: Input data list
               options: Optional configuration
           """
           self.data = data
           self.options = options or {}
       
       def process(self) -> List[Dict[str, Any]]:
           """Process the data.
           
           Returns:
               Processed data list
           """
           return self.data

With Dataclasses
~~~~~~~~~~~~~~~~

.. code-block:: python

   from dataclasses import dataclass, field
   from typing import List

   @dataclass
   class Config:
       """Application configuration.
       
       Attributes:
           name: Application name
           version: Version string
           features: Enabled features
       """
       name: str
       version: str = "1.0.0"
       features: List[str] = field(default_factory=list)

With Async Functions
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   async def fetch_data(url: str, timeout: int = 30) -> dict:
       """Fetch data from URL asynchronously.
       
       Args:
           url: The URL to fetch from
           timeout: Request timeout in seconds
       
       Returns:
           The fetched data
       
       Raises:
           TimeoutError: If request exceeds timeout
       """
       pass

Package Structure Example
--------------------------

Complete Package
~~~~~~~~~~~~~~~~

.. code-block:: text

   mypackage/
   ├── __init__.py
   ├── core/
   │   ├── __init__.py
   │   ├── processor.py
   │   └── utils.py
   ├── api/
   │   ├── __init__.py
   │   ├── client.py
   │   └── endpoints.py
   └── exceptions.py

Configuration
~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   autoapi_type = 'python'
   autoapi_dirs = ['../mypackage']
   autoapi_root = 'api'
   
   autoapi_options = [
       'members',
       'undoc-members',
       'show-inheritance',
       'show-module-summary',
   ]
   
   autoapi_ignore = [
       '*/tests/*',
       '*/__pycache__/*',
   ]

Generated Structure
~~~~~~~~~~~~~~~~~~~

.. code-block:: text

   docs/
   ├── api/
   │   ├── mypackage/
   │   │   ├── index.rst
   │   │   ├── core/
   │   │   │   ├── index.rst
   │   │   │   ├── processor.rst
   │   │   │   └── utils.rst
   │   │   ├── api/
   │   │   │   ├── index.rst
   │   │   │   ├── client.rst
   │   │   │   └── endpoints.rst
   │   │   └── exceptions.rst
   │   └── index.rst
   └── index.rst

Cross-References
----------------

Linking to API
~~~~~~~~~~~~~~

.. code-block:: rst

   See :py:class:`mypackage.core.Processor` for details.
   
   Use :py:func:`mypackage.api.fetch_data` to retrieve data.
   
   Refer to :py:mod:`mypackage.core.utils` module.

Internal Links
~~~~~~~~~~~~~~

AutoAPI generates automatic cross-references:

.. code-block:: python

   class Manager:
       """Manage resources.
       
       Uses :class:`Processor` internally.
       Calls :func:`utils.validate` for validation.
       """
       pass

Customization
-------------

Custom Templates
~~~~~~~~~~~~~~~~

Create ``_templates/autoapi/python/class.rst``:

.. code-block:: jinja

   {{ obj.name }}
   {{ "=" * obj.name|length }}
   
   .. py:class:: {{ obj.id }}
   
      {{ obj.docstring }}
   
      {% if obj.bases %}
      **Bases:** {{ obj.bases|join(', ') }}
      {% endif %}
   
      {% block methods %}
      {% if obj.methods %}
      Methods
      -------
      {% for method in obj.methods %}
      .. automethod:: {{ method.id }}
      {% endfor %}
      {% endif %}
      {% endblock %}

Custom CSS
~~~~~~~~~~

.. code-block:: css

   /* _static/custom.css */
   .autoapi-section {
       border-left: 3px solid #2980b9;
       padding-left: 10px;
   }

Performance Optimization
------------------------

Caching
~~~~~~~

.. code-block:: python

   # Keep generated files for faster rebuilds
   autoapi_keep_files = True

Selective Generation
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Only generate for specific modules
   autoapi_dirs = ['../mypackage/core']
   
   # Exclude large directories
   autoapi_ignore = ['*/vendor/*', '*/node_modules/*']

Best Practices
--------------

Documentation Quality
~~~~~~~~~~~~~~~~~~~~~

1. Write comprehensive docstrings
2. Include type hints
3. Document parameters and return values
4. Add usage examples
5. Document exceptions

Organization
~~~~~~~~~~~~

1. Use clear module structure
2. Group related functionality
3. Keep public API clean
4. Hide implementation details

Integration
~~~~~~~~~~~

1. Combine with manual documentation
2. Use cross-references
3. Add overview pages
4. Include tutorials

See Also
--------

- :doc:`../tutorials/packages/sphinx-autoapi` - Complete tutorial
- GitHub repository: https://github.com/readthedocs/sphinx-autoapi
- vs autodoc: https://sphinx-autoapi.readthedocs.io/
