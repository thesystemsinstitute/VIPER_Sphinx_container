Sphinxcontrib-Asyncio Example
=============================

This page demonstrates the **sphinxcontrib-asyncio** extension for documenting Python asyncio code with enhanced support for coroutines, async context managers, and async iterators.

.. contents:: Contents
   :local:
   :depth: 2

Overview
--------

The sphinxcontrib-asyncio extension provides specialized directives and roles for documenting asynchronous Python code, making it easier to document async/await patterns.

Documenting Coroutines
----------------------

Simple Coroutine
~~~~~~~~~~~~~~~~

.. asyncio:coroutine:: fetch_data(url)

   Fetch data from a URL asynchronously.
   
   :param str url: The URL to fetch
   :returns: Response data
   :rtype: dict
   :raises aiohttp.ClientError: If request fails
   
   **Example**:
   
   .. code-block:: python
   
      async def fetch_data(url):
          async with aiohttp.ClientSession() as session:
              async with session.get(url) as response:
                  return await response.json()

Coroutine with Multiple Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. asyncio:coroutine:: process_items(items, batch_size=10, timeout=30)

   Process items in batches asynchronously.
   
   :param list items: Items to process
   :param int batch_size: Number of items per batch
   :param float timeout: Timeout in seconds
   :returns: Processing results
   :rtype: list[dict]
   
   **Usage**:
   
   .. code-block:: python
   
      results = await process_items(
          items=['item1', 'item2', 'item3'],
          batch_size=5,
          timeout=60
      )

Async Context Managers
-----------------------

Database Connection
~~~~~~~~~~~~~~~~~~~

.. asyncio:asynccontextmanager:: database_connection(url)

   Asynchronous context manager for database connections.
   
   :param str url: Database connection URL
   :yields: Database connection object
   :raises ConnectionError: If connection fails
   
   **Example**:
   
   .. code-block:: python
   
      @asynccontextmanager
      async def database_connection(url):
          conn = await connect(url)
          try:
              yield conn
          finally:
              await conn.close()
      
      # Usage
      async with database_connection('postgresql://...') as conn:
          result = await conn.execute('SELECT * FROM users')

File Operations
~~~~~~~~~~~~~~~

.. asyncio:asynccontextmanager:: async_file(path, mode='r')

   Asynchronous file context manager.
   
   :param str path: File path
   :param str mode: File mode ('r', 'w', 'a', etc.)
   :yields: Async file object
   
   **Usage**:
   
   .. code-block:: python
   
      async with async_file('data.txt', 'w') as f:
          await f.write('Hello, async world!')

Async Iterators
---------------

Data Stream
~~~~~~~~~~~

.. asyncio:asynciterator:: stream_data(source)

   Asynchronously iterate over data from a source.
   
   :param str source: Data source identifier
   :yields: Data chunks
   :yieldtype: bytes
   
   **Example**:
   
   .. code-block:: python
   
      async def stream_data(source):
          async with open_stream(source) as stream:
              async for chunk in stream:
                  yield chunk
      
      # Usage
      async for data in stream_data('source_url'):
          process(data)

Paginated Results
~~~~~~~~~~~~~~~~~

.. asyncio:asynciterator:: paginate(endpoint, page_size=100)

   Iterate through paginated API results.
   
   :param str endpoint: API endpoint
   :param int page_size: Items per page
   :yields: Individual items
   :yieldtype: dict
   
   **Implementation**:
   
   .. code-block:: python
   
      async def paginate(endpoint, page_size=100):
          page = 1
          while True:
              response = await fetch(f"{endpoint}?page={page}&size={page_size}")
              items = response['items']
              if not items:
                  break
              for item in items:
                  yield item
              page += 1

Async Generators
----------------

Event Generator
~~~~~~~~~~~~~~~

.. asyncio:asyncgenerator:: watch_events(topic)

   Generate events from a topic as they occur.
   
   :param str topic: Event topic to watch
   :yields: Event objects
   :yieldtype: Event
   
   **Example**:
   
   .. code-block:: python
   
      async def watch_events(topic):
          subscriber = EventSubscriber(topic)
          async with subscriber:
              async for event in subscriber:
                  yield event

Task Management
---------------

Task Spawning
~~~~~~~~~~~~~

.. asyncio:function:: create_task(coro, name=None)

   Create and schedule an asyncio task.
   
   :param coroutine coro: Coroutine to execute
   :param str name: Optional task name
   :returns: Task object
   :rtype: asyncio.Task
   
   **Usage**:
   
   .. code-block:: python
   
      task = create_task(fetch_data('https://api.example.com'))
      result = await task

Task Groups
~~~~~~~~~~~

.. asyncio:coroutine:: gather_tasks(*tasks, return_exceptions=False)

   Execute multiple tasks concurrently.
   
   :param tasks: Coroutines or tasks to execute
   :param bool return_exceptions: Return exceptions instead of raising
   :returns: List of results
   :rtype: list
   
   **Example**:
   
   .. code-block:: python
   
      results = await gather_tasks(
          fetch_data(url1),
          fetch_data(url2),
          fetch_data(url3)
      )

Configuration Examples
----------------------

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx.ext.autodoc',
       'sphinxcontrib.asyncio',
   ]
   
   # Asyncio documentation settings
   asyncio_default_domain = 'py'

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

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

Autodoc Integration
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Automatic detection of async functions
   autodoc_type_aliases = {
       'Awaitable': 'typing.Awaitable',
       'AsyncIterator': 'typing.AsyncIterator',
       'AsyncContextManager': 'typing.AsyncContextManager',
   }

Practical Examples
------------------

HTTP Client
~~~~~~~~~~~

.. asyncio:coroutine:: get(url, params=None, headers=None)

   Make an async HTTP GET request.
   
   :param str url: Target URL
   :param dict params: Query parameters
   :param dict headers: HTTP headers
   :returns: Response object
   :rtype: Response
   
   .. code-block:: python
   
      async def get(url, params=None, headers=None):
          async with aiohttp.ClientSession() as session:
              async with session.get(url, params=params, headers=headers) as resp:
                  return await resp.json()

Web Scraper
~~~~~~~~~~~

.. asyncio:coroutine:: scrape_pages(urls, concurrency=5)

   Scrape multiple web pages concurrently.
   
   :param list urls: URLs to scrape
   :param int concurrency: Maximum concurrent requests
   :returns: Scraped data
   :rtype: list[dict]
   
   .. code-block:: python
   
      async def scrape_pages(urls, concurrency=5):
          semaphore = asyncio.Semaphore(concurrency)
          
          async def scrape_one(url):
              async with semaphore:
                  return await fetch_and_parse(url)
          
          tasks = [scrape_one(url) for url in urls]
          return await asyncio.gather(*tasks)

Message Queue Consumer
~~~~~~~~~~~~~~~~~~~~~~

.. asyncio:asynciterator:: consume_messages(queue_name)

   Consume messages from an async queue.
   
   :param str queue_name: Name of the queue
   :yields: Message objects
   :yieldtype: Message
   
   .. code-block:: python
   
      async def consume_messages(queue_name):
          queue = await connect_queue(queue_name)
          try:
              while True:
                  message = await queue.get()
                  if message is None:
                      break
                  yield message
          finally:
              await queue.close()

WebSocket Handler
~~~~~~~~~~~~~~~~~

.. asyncio:coroutine:: handle_websocket(websocket, path)

   Handle WebSocket connections.
   
   :param websocket: WebSocket connection
   :param str path: Connection path
   
   .. code-block:: python
   
      async def handle_websocket(websocket, path):
          async for message in websocket:
              response = await process_message(message)
              await websocket.send(response)

Advanced Patterns
-----------------

Retry Logic
~~~~~~~~~~~

.. asyncio:coroutine:: retry_async(func, max_attempts=3, delay=1.0)

   Retry an async function with exponential backoff.
   
   :param coroutine func: Function to retry
   :param int max_attempts: Maximum retry attempts
   :param float delay: Initial delay in seconds
   :returns: Function result
   :raises: Last exception if all attempts fail
   
   .. code-block:: python
   
      async def retry_async(func, max_attempts=3, delay=1.0):
          for attempt in range(max_attempts):
              try:
                  return await func()
              except Exception as e:
                  if attempt == max_attempts - 1:
                      raise
                  await asyncio.sleep(delay * (2 ** attempt))

Rate Limiting
~~~~~~~~~~~~~

.. asyncio:asynccontextmanager:: rate_limit(calls_per_second)

   Rate-limited async context manager.
   
   :param float calls_per_second: Maximum calls per second
   
   .. code-block:: python
   
      @asynccontextmanager
      async def rate_limit(calls_per_second):
          min_interval = 1.0 / calls_per_second
          last_call = 0
          
          async def acquire():
              nonlocal last_call
              now = asyncio.get_event_loop().time()
              elapsed = now - last_call
              if elapsed < min_interval:
                  await asyncio.sleep(min_interval - elapsed)
              last_call = asyncio.get_event_loop().time()
          
          yield acquire

Connection Pool
~~~~~~~~~~~~~~~

.. asyncio:class:: ConnectionPool

   Asynchronous connection pool manager.
   
   .. asyncio:coroutine:: acquire()
   
      Acquire a connection from the pool.
      
      :returns: Connection object
   
   .. asyncio:coroutine:: release(connection)
   
      Release a connection back to the pool.
      
      :param connection: Connection to release
   
   **Example**:
   
   .. code-block:: python
   
      pool = ConnectionPool(min_size=5, max_size=20)
      
      conn = await pool.acquire()
      try:
          result = await conn.execute(query)
      finally:
          await pool.release(conn)

Testing Async Code
------------------

Async Test Fixtures
~~~~~~~~~~~~~~~~~~~

.. asyncio:coroutine:: setup_database()

   Setup test database asynchronously.
   
   :returns: Database instance
   
   .. code-block:: python
   
      import pytest
      
      @pytest.fixture
      async def db():
          database = await setup_database()
          yield database
          await database.cleanup()

Mocking Async Functions
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from unittest.mock import AsyncMock
   
   async def test_fetch_data():
       mock_client = AsyncMock()
       mock_client.get.return_value = {'data': 'test'}
       
       result = await fetch_data_with_client(mock_client)
       assert result == {'data': 'test'}

See Also
--------

- :doc:`../tutorials/packages/sphinxcontrib-asyncio` - Complete tutorial
- Python asyncio documentation: https://docs.python.org/3/library/asyncio.html
- GitHub repository: https://github.com/aio-libs/sphinxcontrib-asyncio
