Sphinxcontrib-Asyncio Tutorial
==============================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinxcontrib-asyncio/>`_
   - `API Documentation <../../pdoc/sphinxcontrib_asyncio/index.html>`_
   - `Manual <https://github.com/sphinx-contrib/asyncio>`_
   - :doc:`Working Example <../../examples/sphinxcontrib-asyncio-example>`


.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinxcontrib-asyncio to document asynchronous Python code with proper async/await syntax highlighting and examples.

What is Sphinxcontrib-Asyncio?
-------------------------------
sphinxcontrib-asyncio is a Sphinx extension that provides enhanced support for documenting asynchronous Python code:

- Proper highlighting of async/await syntax
- Async function and coroutine documentation
- Event loop examples
- Concurrent execution patterns
- Async context managers and generators
- asyncio patterns and best practices
- Code examples with proper async syntax
- Integration with autodoc for async methods

This is essential for documenting modern Python applications using asyncio, FastAPI, aiohttp, and other async frameworks.

The sphinxcontrib-asyncio extension provides specialized directives and roles for documenting asynchronous Python code, making it easier to document async/await patterns.


Installation
------------

sphinxcontrib-asyncio is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinxcontrib.asyncio; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinxcontrib.asyncio',
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = [
       'sphinx.ext.autodoc',
       'sphinxcontrib.asyncio',
   ]
   
   # Asyncio documentation options
   asyncio_show_async_keyword = True
   asyncio_highlight_coroutines = True
   asyncio_show_event_loop = True
   
   # Code block styling
   asyncio_code_style = 'monokai'
   asyncio_show_line_numbers = True
   
   # Example options
   asyncio_run_examples = False  # Don't execute examples during build
   asyncio_example_timeout = 30  # Seconds


.. code-block:: python

   # Custom role names
   asyncio_role_names = {
       'coroutine': 'async',
       'asynccontextmanager': 'async-ctx',
       'asynciterator': 'async-iter',
   }
   
   # Highlighting
   asyncio_highlight_async = True
   asyncio_show_awaitable = True

Basic Usage
-----------

Document Async Functions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. asyncio:function:: fetch_data(url)
      
      Asynchronously fetch data from URL.
      
      :param url: URL to fetch
      :type url: str
      :returns: Response data
      :rtype: dict

Document Coroutines
~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. asyncio:coroutine:: process_items(items)
      
      Process items asynchronously.
      
      :param items: Items to process
      :yields: Processed results

Async Context Managers
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. asyncio:contextmanager:: async_resource()
      
      Async context manager for resource handling.

Event Loop Examples
~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. asyncio:example::
      
      import asyncio
      
      async def main():
          result = await fetch_data("https://api.example.com")
          print(result)
      
      asyncio.run(main())

   Async HTTP Module
   =================
   
   This module provides asynchronous HTTP operations.
   
   .. automodule:: mylib.async_http
      :members:
      :undoc-members:
   
   Basic Usage
   -----------
   
   Single Request
   ~~~~~~~~~~~~~~
   
   .. code-block:: python
   
      import asyncio
      from mylib.async_http import fetch_url
      
      async def main():
          content = await fetch_url("https://api.example.com/data")
          print(content)
      
      asyncio.run(main())
   
   Multiple Concurrent Requests
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   
   .. code-block:: python
   
      import asyncio
      from mylib.async_http import fetch_multiple
      
      async def main():
          urls = [
              "https://api.example.com/users",
              "https://api.example.com/posts",
              "https://api.example.com/comments",
          ]
          results = await fetch_multiple(urls)
          for url, result in zip(urls, results):
              print(f"{url}: {len(result)} bytes")
      
      asyncio.run(main())

Example 2: Async Database Operations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``mylib/async_db.py``:

.. code-block:: python

   """Asynchronous database operations."""
   import asyncio
   from contextlib import asynccontextmanager
   from typing import AsyncIterator
   
   class AsyncDatabase:
       """
       Asynchronous database connection manager.
       
       Example::
       
           db = AsyncDatabase("postgresql://localhost/mydb")
           await db.connect()
           try:
               result = await db.query("SELECT * FROM users")
           finally:
               await db.disconnect()
       """
       
       def __init__(self, connection_string: str):
           """
           Initialize database connection.
           
           :param connection_string: Database connection string
           :type connection_string: str
           """
           self.connection_string = connection_string
           self._connection = None
       
       async def connect(self) -> None:
           """
           Establish database connection.
           
           :raises ConnectionError: If connection fails
           """
           # Simulated connection
           await asyncio.sleep(0.1)
           self._connection = {"connected": True}
       
       async def disconnect(self) -> None:
           """Close database connection."""
           await asyncio.sleep(0.1)
           self._connection = None
       
       async def query(self, sql: str) -> list[dict]:
           """
           Execute SQL query asynchronously.
           
           :param sql: SQL query string
           :type sql: str
           :returns: Query results
           :rtype: list[dict]
           """
           if not self._connection:
               raise RuntimeError("Not connected to database")
           await asyncio.sleep(0.1)
           return [{"id": 1, "name": "example"}]
   
   
   @asynccontextmanager
   async def database_session(connection_string: str) -> AsyncIterator[AsyncDatabase]:
       """
       Async context manager for database sessions.
       
       :param connection_string: Database connection string
       :type connection_string: str
       :yields: Database connection
       :rtype: AsyncDatabase
       
       Example::
       
           async with database_session("postgresql://localhost/db") as db:
               results = await db.query("SELECT * FROM users")
       """
       db = AsyncDatabase(connection_string)
       await db.connect()
       try:
           yield db
       finally:
           await db.disconnect()

``docs/api/async_db.rst``:

.. code-block:: rst

   Async Database Module
   =====================
   
   .. automodule:: mylib.async_db
      :members:
      :show-inheritance:
   
   Usage Patterns
   --------------
   
   Using Context Manager
   ~~~~~~~~~~~~~~~~~~~~~
   
   .. code-block:: python
   
      import asyncio
      from mylib.async_db import database_session
      
      async def main():
          async with database_session("postgresql://localhost/mydb") as db:
              users = await db.query("SELECT * FROM users")
              for user in users:
                  print(user)
      
      asyncio.run(main())
   
   Manual Connection Management
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   
   .. code-block:: python
   
      from mylib.async_db import AsyncDatabase
      
      async def main():
          db = AsyncDatabase("postgresql://localhost/mydb")
          await db.connect()
          
          try:
              users = await db.query("SELECT * FROM users")
              posts = await db.query("SELECT * FROM posts")
          finally:
              await db.disconnect()

Example 3: Async Worker Pool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``mylib/async_worker.py``:

.. code-block:: python

   """Asynchronous worker pool for concurrent task processing."""
   import asyncio
   from typing import Callable, Any, Coroutine
   
   class WorkerPool:
       """
       Pool of async workers for concurrent task execution.
       
       :param max_workers: Maximum concurrent workers
       :type max_workers: int
       
       Example::
       
           async def process_item(item):
               await asyncio.sleep(1)
               return item * 2
           
           pool = WorkerPool(max_workers=5)
           items = range(10)
           results = await pool.map(process_item, items)
       """
       
       def __init__(self, max_workers: int = 5):
           self.max_workers = max_workers
           self.semaphore = asyncio.Semaphore(max_workers)
       
       async def _worker(
           self,
           func: Callable[[Any], Coroutine],
           item: Any
       ) -> Any:
           """
           Execute a single task with semaphore control.
           
           :param func: Async function to execute
           :param item: Item to process
           :returns: Result from function
           """
           async with self.semaphore:
               return await func(item)
       
       async def map(
           self,
           func: Callable[[Any], Coroutine],
           items: list[Any]
       ) -> list[Any]:
           """
           Map async function over items concurrently.
           
           :param func: Async function to apply
           :type func: Callable[[Any], Coroutine]
           :param items: Items to process
           :type items: list[Any]
           :returns: Results in original order
           :rtype: list[Any]
           """
           tasks = [self._worker(func, item) for item in items]
           return await asyncio.gather(*tasks)

``docs/api/async_worker.rst``:

.. code-block:: rst

   Async Worker Pool
   =================
   
   .. autoclass:: mylib.async_worker.WorkerPool
      :members:
   
Advanced Features
-----------------

Async Generators
~~~~~~~~~~~~~~~~

.. code-block:: python

   async def async_range(count: int):
       """
       Async generator example.
       
       :param count: Number of items to generate
       :type count: int
       :yields: Sequential numbers
       :rtype: int
       
       Example::
       
           async for i in async_range(10):
               print(i)
       """
       for i in range(count):
           await asyncio.sleep(0.1)
           yield i

Document:

.. code-block:: rst

   .. autofunction:: async_range
   
   Usage::
   
       async def main():
           async for value in async_range(5):
               print(value)

Async Decorators
~~~~~~~~~~~~~~~~

.. code-block:: python

   def async_retry(max_attempts: int = 3):
       """
       Decorator for retrying async functions.
       
       :param max_attempts: Maximum retry attempts
       :type max_attempts: int
       
       Example::
       
           @async_retry(max_attempts=5)
           async def unstable_api_call():
               response = await fetch_data()
               return response
       """
       def decorator(func):
           async def wrapper(*args, **kwargs):
               for attempt in range(max_attempts):
                   try:
                       return await func(*args, **kwargs)
                   except Exception as e:
                       if attempt == max_attempts - 1:
                           raise
                       await asyncio.sleep(2 ** attempt)
           return wrapper
       return decorator

Async Testing
~~~~~~~~~~~~~

.. code-block:: rst

   Testing Async Code
   ==================
   
   .. code-block:: python
   
      import pytest
      
      @pytest.mark.asyncio
      async def test_fetch_url():
          """Test async URL fetching."""
          from mylib.async_http import fetch_url
          
          result = await fetch_url("https://example.com")
          assert result is not None
          assert len(result) > 0

Docker Integration
------------------

Run Async Examples
~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     kensai-sphinx:latest \
     python -c "
   import asyncio
   from mylib.async_http import fetch_url
   
   async def main():
       result = await fetch_url('https://example.com')
       print(len(result), 'bytes')
   
   asyncio.run(main())
   "

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

   name: Build Async Documentation
   
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
         
         - name: Test Async Code
           run: |
             docker run --rm -v $(pwd):/project \
               kensai-sphinx:latest \
               pytest tests/test_async*.py
         
         - name: Build Docs
           run: |
             docker run --rm -v $(pwd):/project \
               kensai-sphinx:latest \
               sphinx-build -b html /project/docs /project/docs/_build/html

Best Practices
--------------

1. **Document Async Nature Clearly**
   
   Always indicate when functions are async:
   
   .. code-block:: python
   
      async def my_function():
          """
          Async function - must be awaited.
          
          Example::
          
              result = await my_function()
          """

2. **Show Event Loop Usage**
   
   Include complete examples with asyncio.run():
   
   .. code-block:: python
   
      # In documentation
      import asyncio
      asyncio.run(main())

3. **Document Concurrency**
   
   Explain concurrent execution patterns:
   
   .. code-block:: rst
   
      This function can be called concurrently::
      
          results = await asyncio.gather(
              func(1), func(2), func(3)
          )

4. **Handle Exceptions**
   
   Document async exception handling:
   
   .. code-block:: python
   
      try:
          result = await risky_operation()
      except asyncio.TimeoutError:
          # Handle timeout

5. **Show Context Manager Usage**
   
   Document async context managers properly

6. **Include Performance Notes**
   
   Mention when async provides benefits

Common Patterns
---------------

Async API Client Template
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   API Client
   ==========
   
   .. autoclass:: MyAPIClient
      :members:
   
   Example Usage::
   
       import asyncio
       
       async def main():
           async with MyAPIClient("https://api.example.com") as client:
               data = await client.get("/endpoint")
               print(data)
       
       asyncio.run(main())

Troubleshooting
---------------

Async Examples Not Executing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Solution:**

Check event loop is running:

.. code-block:: python

   import asyncio
   
   # Correct
   asyncio.run(main())
   
   # Not in Jupyter/IPython
   await main()  # Only works in async context

Autodoc Not Detecting Async
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Solution:**

Ensure sphinxcontrib-asyncio is loaded:

.. code-block:: python

   extensions = [
       'sphinx.ext.autodoc',
       'sphinxcontrib.asyncio',
   ]

Next Steps
----------

1. Document your async functions with proper examples
2. Include event loop usage patterns
3. Show concurrent execution examples
4. Document async context managers
5. Add async testing examples

Additional Resources
--------------------

- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `asyncio Documentation <https://docs.python.org/3/library/asyncio.html>`_
- `aiohttp Documentation <https://docs.aiohttp.org/>`_
- `FastAPI Documentation <https://fastapi.tiangolo.com/>`_
