Sphinxcontrib-HTTPDomain Tutorial
==================================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinxcontrib-httpdomain/>`_
   - `Official Documentation <https://sphinxcontrib-httpdomain.readthedocs.io/>`_
   - :doc:`See Working Example <../../examples/sphinxcontrib-httpdomain-example>`


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

Practical Examples
------------------

Example 1: Complete REST API Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/api/users.rst``:

.. code-block:: rst

   User API
   ========
   
   Endpoints for managing users.
   
   List Users
   ----------
   
   .. http:get:: /api/v1/users
      
      Retrieve a paginated list of users.
      
      **Example request**:
      
      .. sourcecode:: http
         
         GET /api/v1/users?page=1&per_page=10 HTTP/1.1
         Host: api.example.com
         Authorization: Bearer YOUR_TOKEN
         Accept: application/json
      
      **Example response**:
      
      .. sourcecode:: http
         
         HTTP/1.1 200 OK
         Content-Type: application/json
         X-Total-Count: 100
         X-Page: 1
         X-Per-Page: 10
         
         {
           "users": [
             {
               "id": 1,
               "name": "John Doe",
               "email": "john@example.com",
               "created_at": "2024-01-01T00:00:00Z"
             },
             {
               "id": 2,
               "name": "Jane Smith",
               "email": "jane@example.com",
               "created_at": "2024-01-02T00:00:00Z"
             }
           ],
           "pagination": {
             "page": 1,
             "per_page": 10,
             "total": 100,
             "pages": 10
           }
         }
      
      :query int page: Page number (default: 1)
      :query int per_page: Items per page (default: 10, max: 100)
      :query string sort: Sort field (name, email, created_at)
      :query string order: Sort order (asc, desc)
      
      :reqheader Authorization: Bearer token
      :reqheader Accept: Must be ``application/json``
      
      :resheader Content-Type: ``application/json``
      :resheader X-Total-Count: Total number of users
      :resheader X-Page: Current page number
      :resheader X-Per-Page: Items per page
      
      :>json array users: List of user objects
      :>json int users[].id: User ID
      :>json string users[].name: User's name
      :>json string users[].email: User's email
      :>json string users[].created_at: ISO 8601 timestamp
      :>json object pagination: Pagination information
      
      :statuscode 200: Success
      :statuscode 401: Unauthorized
      :statuscode 422: Invalid query parameters
   
   Get User
   --------
   
   .. http:get:: /api/v1/users/(int:id)
      
      Retrieve a specific user by ID.
      
      **Example request**:
      
      .. sourcecode:: http
         
         GET /api/v1/users/123 HTTP/1.1
         Host: api.example.com
         Authorization: Bearer YOUR_TOKEN
      
      **Example response**:
      
      .. sourcecode:: http
         
         HTTP/1.1 200 OK
         Content-Type: application/json
         
         {
           "id": 123,
           "name": "John Doe",
           "email": "john@example.com",
           "role": "admin",
           "created_at": "2024-01-01T00:00:00Z",
           "updated_at": "2024-01-15T10:30:00Z"
         }
      
      :param int id: User ID
      
      :>json int id: User ID
      :>json string name: User's name
      :>json string email: User's email
      :>json string role: User's role (admin, user)
      :>json string created_at: Creation timestamp
      :>json string updated_at: Last update timestamp
      
      :statuscode 200: User found
      :statuscode 404: User not found
   
   Create User
   -----------
   
   .. http:post:: /api/v1/users
      
      Create a new user.
      
      **Example request**:
      
      .. sourcecode:: http
         
         POST /api/v1/users HTTP/1.1
         Host: api.example.com
         Authorization: Bearer YOUR_TOKEN
         Content-Type: application/json
         
         {
           "name": "John Doe",
           "email": "john@example.com",
           "password": "SecurePass123!",
           "role": "user"
         }
      
      **Example response**:
      
      .. sourcecode:: http
         
         HTTP/1.1 201 Created
         Content-Type: application/json
         Location: /api/v1/users/124
         
         {
           "id": 124,
           "name": "John Doe",
           "email": "john@example.com",
           "role": "user",
           "created_at": "2024-01-20T15:30:00Z"
         }
      
      :<json string name: User's full name (required)
      :<json string email: Valid email address (required)
      :<json string password: Password (min 8 chars, required)
      :<json string role: User role (default: user)
      
      :>json int id: Created user ID
      :>json string name: User's name
      :>json string email: User's email
      :>json string role: Assigned role
      :>json string created_at: Creation timestamp
      
      :reqheader Authorization: Bearer token required
      :reqheader Content-Type: Must be ``application/json``
      
      :resheader Location: URL of created user
      
      :statuscode 201: User created successfully
      :statuscode 400: Invalid input data
      :statuscode 409: Email already exists
   
   Update User
   -----------
   
   .. http:patch:: /api/v1/users/(int:id)
      
      Update user information.
      
      **Example request**:
      
      .. sourcecode:: http
         
         PATCH /api/v1/users/123 HTTP/1.1
         Host: api.example.com
         Authorization: Bearer YOUR_TOKEN
         Content-Type: application/json
         
         {
           "name": "John Updated",
           "role": "admin"
         }
      
      :param int id: User ID to update
      
      :<json string name: New name (optional)
      :<json string email: New email (optional)
      :<json string role: New role (optional)
      
      :statuscode 200: User updated
      :statuscode 400: Invalid input
      :statuscode 404: User not found
   
   Delete User
   -----------
   
   .. http:delete:: /api/v1/users/(int:id)
      
      Delete a user.
      
      **Example request**:
      
      .. sourcecode:: http
         
         DELETE /api/v1/users/123 HTTP/1.1
         Host: api.example.com
         Authorization: Bearer YOUR_TOKEN
      
      **Example response**:
      
      .. sourcecode:: http
         
         HTTP/1.1 204 No Content
      
      :param int id: User ID to delete
      
      :statuscode 204: User deleted successfully
      :statuscode 404: User not found
      :statuscode 403: Cannot delete own account

Example 2: Authentication API
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/api/auth.rst``:

.. code-block:: rst

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
