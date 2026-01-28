Sphinx-Autodoc-Defaultargs Tutorial
====================================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-autodoc-defaultargs/>`_
   - `Manual <https://github.com/zwang123/sphinx-autodoc-defaultargs>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinx-autodoc-defaultargs to show default argument values in your API documentation.

What is Sphinx-Autodoc-Defaultargs?
------------------------------------
sphinx-autodoc-defaultargs is a Sphinx extension that enhances autodoc to:

- Display default argument values
- Show parameter defaults in signatures
- Format default values nicely
- Handle complex default types
- Show mutable defaults safely
- Format None, True, False properly
- Display callable defaults
- Show class and function defaults
- Improve API documentation clarity

This makes API documentation more complete by showing what values parameters default to.

The sphinx-autodoc-defaultargs extension enhances autodoc to show default argument values in function signatures.


Installation
------------

sphinx-autodoc-defaultargs is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinx_autodoc_defaultargs; print('Installed')"


Configuration
-------------

Basic Setup
~~~~~~~~~~~


Add to your ``conf.py``:

.. code-block:: python


   extensions = [
       'sphinx.ext.autodoc',
       'sphinx_autodoc_defaultargs',
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = [
       'sphinx.ext.autodoc',
       'sphinx_autodoc_defaultargs',
   ]
   
   # Default args configuration
   autodoc_defaultargs_format = 'inline'  # inline, below, both
   autodoc_defaultargs_show_none = True
   autodoc_defaultargs_show_false = True
   autodoc_defaultargs_max_length = 80
   
   # Formatting options
   autodoc_defaultargs_quote_strings = True
   autodoc_defaultargs_repr_callable = True
   autodoc_defaultargs_truncate_long = True
   
   # Display options
   autodoc_defaultargs_in_signature = True
   autodoc_defaultargs_in_description = True


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Basic Setup
~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx.ext.autodoc',
       'sphinx_autodoc_defaultargs',
   ]

Options
~~~~~~~

.. code-block:: python

   autodoc_default_options = {
       'show-defaults': True,
       'default-value-format': 'repr',  # or 'str'
   }


Class with Defaults
~~~~~~~~~~~~~~~~~~~

``mylib/client.py``:

.. code-block:: python

   class APIClient:
       """HTTP API client."""
       
       def __init__(self, base_url, timeout=30, retries=3, verify_ssl=True):
           """
           Initialize API client.
           
           :param base_url: Base URL for API
           :param timeout: Request timeout in seconds
           :param retries: Number of retry attempts
           :param verify_ssl: Verify SSL certificates
           """
           self.base_url = base_url
           self.timeout = timeout
           self.retries = retries
           self.verify_ssl = verify_ssl

Document:

.. code-block:: rst

   .. autoclass:: mylib.client.APIClient
      :members:

   Configuration
   =============
   
   Database Configuration
   ----------------------
   
   .. autoclass:: mylib.config.DatabaseConfig
      :members:
      :undoc-members:
      :show-inheritance:
   
   Formatting Utilities
   ====================
   
   .. automodule:: mylib.formatting
      :members:
      :undoc-members:

Example 3: API Client Methods
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``mylib/http_client.py``:

.. code-block:: python

   """HTTP client for API requests."""
   import requests
   from typing import Optional, Dict, Any
   
   class HTTPClient:
       """Simple HTTP client."""
       
       def __init__(self, base_url: str, timeout: int = 30):
           """Initialize client."""
           self.base_url = base_url
           self.timeout = timeout
           self.session = requests.Session()
       
       def get(
           self,
           endpoint: str,
           params: Optional[Dict[str, Any]] = None,
           headers: Optional[Dict[str, str]] = None,
           timeout: Optional[int] = None,
           verify: bool = True,
           allow_redirects: bool = True,
       ) -> requests.Response:
           """
           Send GET request.
           
           :param endpoint: API endpoint
           :param params: Query parameters
           :param headers: Request headers
           :param timeout: Request timeout (uses client default if None)
           :param verify: Verify SSL certificates
           :param allow_redirects: Follow redirects
           :return: Response object
           """
           url = f"{self.base_url}/{endpoint.lstrip('/')}"
           timeout = timeout or self.timeout
           
           return self.session.get(
               url,
               params=params,
               headers=headers,
               timeout=timeout,
               verify=verify,
               allow_redirects=allow_redirects,
           )
       
       def post(
           self,
           endpoint: str,
           data: Optional[Dict[str, Any]] = None,
           json: Optional[Dict[str, Any]] = None,
           headers: Optional[Dict[str, str]] = None,
           timeout: Optional[int] = None,
           files: Optional[Dict[str, Any]] = None,
       ) -> requests.Response:
           """
           Send POST request.
           
           :param endpoint: API endpoint
           :param data: Form data
           :param json: JSON data
           :param headers: Request headers
           :param timeout: Request timeout
           :param files: Files to upload
           :return: Response object
           """
           url = f"{self.base_url}/{endpoint.lstrip('/')}"
           timeout = timeout or self.timeout
           
           return self.session.post(
               url,
               data=data,
               json=json,
               headers=headers,
               timeout=timeout,
               files=files,
           )

``docs/api/http_client.rst``:

.. code-block:: rst

   HTTP Client
   ===========
   
   .. autoclass:: mylib.http_client.HTTPClient
      :members:
      :special-members: __init__

Advanced Features
-----------------

Complex Default Types
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from datetime import datetime, timedelta
   from typing import List, Dict
   
   def schedule_task(
       name: str,
       when: datetime = datetime.now(),
       retry_delays: List[int] = [60, 300, 900],
       metadata: Dict[str, str] = {},
   ):
       """Schedule a task."""
       pass

Callable Defaults
~~~~~~~~~~~~~~~~~

.. code-block:: python

   def process_data(
       data: list,
       transform=str.upper,
       filter_func=None,
   ):
       """Process data with transformations."""
       pass

Enum Defaults
~~~~~~~~~~~~~

.. code-block:: python

   from enum import Enum
   
   class LogLevel(Enum):
       DEBUG = 10
       INFO = 20
       WARNING = 30
       ERROR = 40
   
   def setup_logging(level: LogLevel = LogLevel.INFO):
       """Setup logging."""
       pass

Docker Integration
------------------

Build Documentation
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     kensai-sphinx:latest \
     sphinx-build -b html /project/docs /project/docs/_build/html

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Build API Documentation
   
   on:
     push:
       paths:
         - 'mylib/**/*.py'
         - 'docs/**'
   
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

Best Practices
--------------

1. **Use Type Hints**
   
   Combine with type hints for better docs:
   
   .. code-block:: python
   
      def func(name: str, count: int = 10) -> str:
          pass

2. **Document Defaults**
   
   Explain why defaults were chosen

3. **Avoid Mutable Defaults**
   
   Use None and create in function:
   
   .. code-block:: python
   
      def func(items: Optional[List] = None):
          items = items or []

4. **Meaningful Defaults**
   
   Choose sensible default values

5. **Keep Signatures Clean**
   
   Don't have too many parameters

Troubleshooting
---------------

Defaults Not Showing
~~~~~~~~~~~~~~~~~~~~

**Solution:**

Check extension is loaded:

.. code-block:: python

   extensions = [
       'sphinx.ext.autodoc',
       'sphinx_autodoc_defaultargs',
   ]

Long Defaults Truncated
~~~~~~~~~~~~~~~~~~~~~~~~

**Solution:**

Increase max length:

.. code-block:: python

   autodoc_defaultargs_max_length = 120

Complex Types Not Formatted
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Solution:**

Enable repr for callables:

.. code-block:: python

   autodoc_defaultargs_repr_callable = True

Next Steps
----------

1. Add extension to your project
2. Document functions with default arguments
3. Review generated documentation
4. Adjust formatting options
5. Keep default values up to date


Practical Examples
------------------

Basic Usage
-----------

Function with Defaults
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   def connect(host='localhost', port=5432, timeout=30):
       """Connect to database.
       
       :param host: Database host
       :param port: Database port
       :param timeout: Connection timeout
       """
       pass

With autodoc-defaultargs, the documentation automatically shows:

.. function:: connect(host='localhost', port=5432, timeout=30)

   Connect to database.
   
   :param host: Database host
   :param port: Database port
   :param timeout: Connection timeout

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx.ext.autodoc',
       'sphinx_autodoc_defaultargs',
   ]

Options
~~~~~~~

.. code-block:: python

   autodoc_default_options = {
       'show-defaults': True,
       'default-value-format': 'repr',  # or 'str'
   }

Examples
--------

Complex Defaults
~~~~~~~~~~~~~~~~

.. code-block:: python

   def process_data(items, batch_size=100, options=None, validate=True):
       """Process data in batches."""
       if options is None:
           options = {}
       # process...


Simple Function
~~~~~~~~~~~~~~~

``sphinx_autodoc_defaultargs/utils.py``:

.. literalinclude:: sphinx_autodoc_defaultargs/utils.py
   :language: python


Document:

.. code-block:: rst

   .. autofunction:: sphinx_autodoc_defaultargs.utils.greet


.. autofunction:: sphinx_autodoc_defaultargs.utils.greet


Output shows:

generated documentation: :doc:`sphinx_autodoc_defaultargs/utils`


Practical Examples
------------------

Basic Usage
-----------

Function with Defaults
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   def connect(host='localhost', port=5432, timeout=30):
       """Connect to database.
       
       :param host: Database host
       :param port: Database port
       :param timeout: Connection timeout
       """
       pass

With autodoc-defaultargs, the documentation automatically shows:

.. function:: connect(host='localhost', port=5432, timeout=30)

   Connect to database.
   
   :param host: Database host
   :param port: Database port
   :param timeout: Connection timeout

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx.ext.autodoc',
       'sphinx_autodoc_defaultargs',
   ]

Options
~~~~~~~

.. code-block:: python

   autodoc_default_options = {
       'show-defaults': True,
       'default-value-format': 'repr',  # or 'str'
   }

Examples
--------

Complex Defaults
~~~~~~~~~~~~~~~~

.. code-block:: python

   def process_data(items, batch_size=100, options=None, validate=True):
       """Process data in batches."""
       if options is None:
           options = {}
       # process...


Simple Function
~~~~~~~~~~~~~~~

``sphinx_autodoc_defaultargs/utils.py``:

.. literalinclude:: sphinx_autodoc_defaultargs/utils.py
   :language: python


Document:

.. code-block:: rst

   .. autofunction:: sphinx_autodoc_defaultargs.utils.greet


.. autofunction:: sphinx_autodoc_defaultargs.utils.greet


Output shows:

generated documentation: :doc:`sphinx_autodoc_defaultargs/utils`


Practical Examples
------------------

Basic Usage
-----------

Function with Defaults
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   def connect(host='localhost', port=5432, timeout=30):
       """Connect to database.
       
       :param host: Database host
       :param port: Database port
       :param timeout: Connection timeout
       """
       pass

With autodoc-defaultargs, the documentation automatically shows:

.. function:: connect(host='localhost', port=5432, timeout=30)

   Connect to database.
   
   :param host: Database host
   :param port: Database port
   :param timeout: Connection timeout

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx.ext.autodoc',
       'sphinx_autodoc_defaultargs',
   ]

Options
~~~~~~~

.. code-block:: python

   autodoc_default_options = {
       'show-defaults': True,
       'default-value-format': 'repr',  # or 'str'
   }

Examples
--------

Complex Defaults
~~~~~~~~~~~~~~~~

.. code-block:: python

   def process_data(items, batch_size=100, options=None, validate=True):
       """Process data in batches."""
       if options is None:
           options = {}
       # process...


Simple Function
~~~~~~~~~~~~~~~

``sphinx_autodoc_defaultargs/utils.py``:

.. literalinclude:: sphinx_autodoc_defaultargs/utils.py
   :language: python


Document:

.. code-block:: rst

   .. autofunction:: sphinx_autodoc_defaultargs.utils.greet


.. autofunction:: sphinx_autodoc_defaultargs.utils.greet


Output shows:

generated documentation: :doc:`sphinx_autodoc_defaultargs/utils`

Additional Resources
--------------------
- :doc:`sphinx-autodoc-annotation` - Type annotation display
- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `Autodoc Documentation <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_
- :doc:`../tutorials/packages/sphinx-autodoc-defaultargs` - Complete tutorial
- GitHub repository: https://github.com/sphinx-contrib/autodoc-defaultargs

