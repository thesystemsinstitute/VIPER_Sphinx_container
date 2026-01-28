Sphinxcontrib-HTTPDomain Tutorial
==================================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinxcontrib-httpdomain/>`_
   - `API Documentation <../../pdoc/sphinxcontrib_httpdomain/index.html>`_
   - `Manual <https://github.com/sphinx-contrib/httpdomain>`_
   - :doc:`Working Example <../../examples/sphinxcontrib-httpdomain-example>`


.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinxcontrib-httpdomain to document HTTP APIs, REST endpoints, and web services.

What is Sphinxcontrib-HTTPDomain?
----------------------------------
sphinxcontrib-httpdomain is a Sphinx extension that provides:

- HTTP endpoint documentation
- REST API documentation
- Request/response examples
- Status code documentation
- Header documentation
- Parameter documentation
- JSON schema support
- Auto-generated API reference
- Cross-referencing
- Multiple HTTP methods
- Query parameter docs
- Request body documentation

This creates professional, comprehensive API documentation for web services.

The sphinxcontrib-httpdomain extension provides domain directives for documenting RESTful HTTP APIs, including endpoints, methods, parameters, and responses.


Installation
------------

sphinxcontrib-httpdomain is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinxcontrib.httpdomain; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinxcontrib.httpdomain',
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinxcontrib.httpdomain']
   
   # HTTP domain configuration
   http_index_ignore_prefixes = ['/internal', '/_']
   http_index_shortname = 'API'
   http_index_localname = 'HTTP API Reference'
   
   # Headers to always show
   http_headers_ignore_prefixes = ['X-Internal-']
   
   # Strict mode
   http_strict_mode = True


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Basic Setup
~~~~~~~~~~~

.. code-block:: python

   # conf.py
   extensions = [
       'sphinxcontrib.httpdomain',
   ]

Custom Settings
~~~~~~~~~~~~~~~

.. code-block:: python

   # HTTP domain configuration
   http_index_ignore_prefixes = ['/api/v1', '/api/v2']
   http_index_shortname = 'API'
   http_index_localname = 'HTTP API Index'

Basic Usage
-----------

Document GET Endpoint
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. http:get:: /users/(int:id)
      
      Get user by ID.
      
      **Example request**:
      
      .. sourcecode:: http
         
         GET /users/123 HTTP/1.1
         Host: api.example.com
         Accept: application/json
      
      **Example response**:
      
      .. sourcecode:: http
         
         HTTP/1.1 200 OK
         Content-Type: application/json
         
         {
           "id": 123,
           "name": "John Doe",
           "email": "john@example.com"
         }
      
      :statuscode 200: User found
      :statuscode 404: User not found

Document POST Endpoint
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. http:post:: /users
      
      Create a new user.
      
      :<json string name: User's full name
      :<json string email: User's email address
      :<json string password: User's password (min 8 chars)
      :>json int id: Created user ID
      :>json string name: User's name
      :statuscode 201: User created successfully
      :statuscode 400: Invalid input

   Authentication API
   ==================
   
   Login
   -----
   
   .. http:post:: /api/v1/auth/login
      
      Authenticate and receive access token.
      
      **Example request**:
      
      .. sourcecode:: http
         
         POST /api/v1/auth/login HTTP/1.1
         Host: api.example.com
         Content-Type: application/json
         
         {
           "email": "john@example.com",
           "password": "SecurePass123!"
         }
      
      **Example response**:
      
      .. sourcecode:: http
         
         HTTP/1.1 200 OK
         Content-Type: application/json
         Set-Cookie: refresh_token=abc123; HttpOnly; Secure
         
         {
           "access_token": "eyJhbGc...",
           "token_type": "Bearer",
           "expires_in": 3600,
           "user": {
             "id": 123,
             "name": "John Doe",
             "email": "john@example.com"
           }
         }
      
      :<json string email: User email
      :<json string password: User password
      
      :>json string access_token: JWT access token
      :>json string token_type: Token type (always "Bearer")
      :>json int expires_in: Token lifetime in seconds
      :>json object user: User information
      
      :statuscode 200: Login successful
      :statuscode 401: Invalid credentials
      :statuscode 429: Too many login attempts

Example 3: Complex Data Operations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/api/posts.rst``:

.. code-block:: rst

   Posts API
   =========
   
   Search Posts
   ------------
   
   .. http:get:: /api/v1/posts/search
      
      Search posts with filters.
      
      :query string q: Search query
      :query string author: Filter by author name
      :query string tag: Filter by tag (can be repeated)
      :query string status: Filter by status (published, draft)
      :query date from: Start date (YYYY-MM-DD)
      :query date to: End date (YYYY-MM-DD)
      :query int limit: Max results (default: 20)
      
      **Example**:
      
      .. sourcecode:: http
         
         GET /api/v1/posts/search?q=python&tag=tutorial&tag=beginner HTTP/1.1
      
      :statuscode 200: Results found
      :statuscode 400: Invalid query parameters

Advanced Features
-----------------

Cross-Referencing
~~~~~~~~~~~~~~~~~

.. code-block:: rst

   See :http:get:`/api/v1/users/(int:id)` for details.
   
   Related: :http:post:`/api/v1/users`

Index Generation
~~~~~~~~~~~~~~~~

.. code-block:: rst

   HTTP API Index
   ==============
   
   .. http:index::

Route Tables
~~~~~~~~~~~~

.. code-block:: rst

   .. http:route:: /api/v1/users
      :methods: GET, POST
      
      User collection endpoint

Docker Integration
------------------

Build API Documentation
~~~~~~~~~~~~~~~~~~~~~~~

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

   name: Build API Docs
   
   on:
     push:
       paths:
         - 'docs/api/**'
         - 'openapi.yaml'
   
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

1. **Document All Endpoints**
   
   Include all HTTP methods

2. **Provide Examples**
   
   Show request and response

3. **List All Parameters**
   
   Query, path, body parameters

4. **Document Status Codes**
   
   All possible responses

5. **Include Headers**
   
   Required and optional headers

6. **Cross-Reference**
   
   Link related endpoints

Troubleshooting
---------------

Directive Not Found
~~~~~~~~~~~~~~~~~~~

**Solution:**

Check extension is loaded:

.. code-block:: python

   extensions = ['sphinxcontrib.httpdomain']

Syntax Errors
~~~~~~~~~~~~~

**Solution:**

Validate directive syntax:

.. code-block:: rst

   .. http:get:: /path
      
      Description here
      
      :statuscode 200: OK

Next Steps
----------

1. Document all API endpoints
2. Add request/response examples
3. Generate API index
4. Cross-reference endpoints
5. Keep documentation in sync

Additional Resources
--------------------

- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `HTTPDomain Documentation <https://sphinxcontrib-httpdomain.readthedocs.io/>`_
- `HTTP Status Codes <https://httpstatuses.com/>`_
