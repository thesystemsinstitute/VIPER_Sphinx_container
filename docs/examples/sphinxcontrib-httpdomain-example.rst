Sphinxcontrib-HTTPDomain Example
=================================

This page demonstrates the **sphinxcontrib-httpdomain** extension for documenting HTTP APIs in Sphinx.

.. contents:: Contents
   :local:
   :depth: 2

Overview
--------

The sphinxcontrib-httpdomain extension provides domain directives for documenting RESTful HTTP APIs, including endpoints, methods, parameters, and responses.

Basic HTTP Methods
------------------

GET Request
~~~~~~~~~~~

.. http:get:: /users/(int:id)

   Get user information by ID.

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

POST Request
~~~~~~~~~~~~

.. http:post:: /users

   Create a new user.

   **Example request**:

   .. sourcecode:: http

      POST /users HTTP/1.1
      Host: api.example.com
      Content-Type: application/json

      {
          "name": "Jane Doe",
          "email": "jane@example.com"
      }

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 201 Created
      Location: /users/124

      {
          "id": 124,
          "name": "Jane Doe",
          "email": "jane@example.com"
      }

   :statuscode 201: User created
   :statuscode 400: Invalid request

PUT Request
~~~~~~~~~~~

.. http:put:: /users/(int:id)

   Update user information.

   **Example request**:

   .. sourcecode:: http

      PUT /users/123 HTTP/1.1
      Host: api.example.com
      Content-Type: application/json

      {
          "name": "John Smith",
          "email": "john.smith@example.com"
      }

   :statuscode 200: User updated
   :statuscode 404: User not found

DELETE Request
~~~~~~~~~~~~~~

.. http:delete:: /users/(int:id)

   Delete a user.

   :statuscode 204: User deleted
   :statuscode 404: User not found

Request Parameters
------------------

Path Parameters
~~~~~~~~~~~~~~~

.. http:get:: /api/v1/posts/(int:post_id)/comments/(int:comment_id)

   Get a specific comment on a post.

   :param post_id: The post identifier
   :param comment_id: The comment identifier
   :type post_id: int
   :type comment_id: int

Query Parameters
~~~~~~~~~~~~~~~~

.. http:get:: /users

   List users with filtering and pagination.

   **Example request**:

   .. sourcecode:: http

      GET /users?role=admin&limit=10&offset=0 HTTP/1.1
      Host: api.example.com

   :query role: Filter by user role
   :query limit: Maximum number of results (default: 20)
   :query offset: Pagination offset (default: 0)
   :query sort: Sort field (name, created_at)

Request Headers
~~~~~~~~~~~~~~~

.. http:post:: /api/data

   Upload data with authentication.

   :reqheader Authorization: Bearer token for authentication
   :reqheader Content-Type: application/json
   :reqheader Accept: application/json
   :reqheader User-Agent: Client application identifier

Request Body
~~~~~~~~~~~~

.. http:post:: /articles

   Create a new article.

   :<json string title: Article title (required)
   :<json string content: Article content (required)
   :<json array tags: List of tags
   :<json boolean published: Publication status
   :<json string author_id: Author identifier

   **Example request**:

   .. sourcecode:: http

      POST /articles HTTP/1.1
      Content-Type: application/json

      {
          "title": "My Article",
          "content": "Article content here...",
          "tags": ["python", "api"],
          "published": true,
          "author_id": "user-123"
      }

Response Fields
---------------

JSON Response
~~~~~~~~~~~~~

.. http:get:: /articles/(int:id)

   Get article details.

   :>json int id: Article identifier
   :>json string title: Article title
   :>json string content: Article content
   :>json array tags: List of tags
   :>json boolean published: Publication status
   :>json object author: Author information
   :>json string author.id: Author ID
   :>json string author.name: Author name
   :>json string created_at: Creation timestamp
   :>json string updated_at: Last update timestamp

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      {
          "id": 42,
          "title": "My Article",
          "content": "Article content...",
          "tags": ["python", "api"],
          "published": true,
          "author": {
              "id": "user-123",
              "name": "John Doe"
          },
          "created_at": "2024-01-26T10:00:00Z",
          "updated_at": "2024-01-26T12:00:00Z"
      }

Response Headers
~~~~~~~~~~~~~~~~

.. http:get:: /download/file.pdf

   Download a file.

   :resheader Content-Type: application/pdf
   :resheader Content-Length: File size in bytes
   :resheader Content-Disposition: attachment; filename="file.pdf"
   :resheader ETag: Entity tag for caching
   :resheader Last-Modified: Last modification date

Status Codes
------------

Success Codes
~~~~~~~~~~~~~

.. http:get:: /resources

   Get list of resources.

   :statuscode 200: Success - resources returned
   :statuscode 201: Created - new resource created
   :statuscode 202: Accepted - request accepted for processing
   :statuscode 204: No Content - success with no body

Client Error Codes
~~~~~~~~~~~~~~~~~~

.. http:post:: /protected

   Protected endpoint.

   :statuscode 400: Bad Request - invalid input
   :statuscode 401: Unauthorized - authentication required
   :statuscode 403: Forbidden - insufficient permissions
   :statuscode 404: Not Found - resource doesn't exist
   :statuscode 409: Conflict - resource conflict

Server Error Codes
~~~~~~~~~~~~~~~~~~

.. http:get:: /data

   Get data that might fail.

   :statuscode 500: Internal Server Error
   :statuscode 502: Bad Gateway
   :statuscode 503: Service Unavailable
   :statuscode 504: Gateway Timeout

Authentication
--------------

Bearer Token
~~~~~~~~~~~~

.. http:get:: /api/protected/data
   :synopsis: Access protected data

   Protected endpoint requiring authentication.

   **Example request**:

   .. sourcecode:: http

      GET /api/protected/data HTTP/1.1
      Host: api.example.com
      Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

   :reqheader Authorization: Bearer {token}
   :statuscode 200: Access granted
   :statuscode 401: Invalid or missing token

API Key
~~~~~~~

.. http:get:: /api/v1/stats

   Get API statistics.

   **Example request**:

   .. sourcecode:: http

      GET /api/v1/stats HTTP/1.1
      Host: api.example.com
      X-API-Key: your-api-key-here

   :reqheader X-API-Key: API key for authentication

OAuth 2.0
~~~~~~~~~

.. http:post:: /oauth/token

   Get OAuth access token.

   **Example request**:

   .. sourcecode:: http

      POST /oauth/token HTTP/1.1
      Content-Type: application/x-www-form-urlencoded

      grant_type=client_credentials&
      client_id=your_client_id&
      client_secret=your_client_secret

   :statuscode 200: Token issued
   :statuscode 401: Invalid credentials

Versioning
----------

URL Versioning
~~~~~~~~~~~~~~

.. http:get:: /api/v1/users
   :synopsis: API version 1

   Users endpoint (version 1).

.. http:get:: /api/v2/users
   :synopsis: API version 2

   Users endpoint (version 2) with additional fields.

Header Versioning
~~~~~~~~~~~~~~~~~

.. http:get:: /api/users

   Get users with version specified in header.

   **Example request**:

   .. sourcecode:: http

      GET /api/users HTTP/1.1
      Accept: application/vnd.api+json; version=2

   :reqheader Accept: API version in Accept header

Complete API Example
--------------------

Blog API
~~~~~~~~

.. http:get:: /api/v1/posts

   List blog posts.

   :query int page: Page number (default: 1)
   :query int per_page: Items per page (default: 10)
   :query string category: Filter by category
   :query string status: Filter by status (draft, published)
   
   :>json array posts: List of post objects
   :>json object pagination: Pagination information
   :>json int pagination.page: Current page
   :>json int pagination.total: Total items
   :>json int pagination.pages: Total pages

.. http:post:: /api/v1/posts

   Create a new blog post.

   :<json string title: Post title (required, max 200 chars)
   :<json string content: Post content (required)
   :<json string category: Post category
   :<json array tags: List of tags
   :<json string status: Status (draft or published)

   :statuscode 201: Post created
   :statuscode 400: Validation error
   :statuscode 401: Authentication required

.. http:get:: /api/v1/posts/(int:id)

   Get a specific blog post.

   :param id: Post identifier
   
   :>json int id: Post ID
   :>json string title: Post title
   :>json string content: Post content
   :>json string category: Category name
   :>json array tags: List of tags
   :>json string status: Publication status
   :>json object author: Author information
   :>json string created_at: Creation timestamp
   :>json string updated_at: Update timestamp

   :statuscode 200: Post found
   :statuscode 404: Post not found

.. http:put:: /api/v1/posts/(int:id)

   Update a blog post.

   :param id: Post identifier

   :<json string title: Post title
   :<json string content: Post content
   :<json string category: Category
   :<json array tags: Tags
   :<json string status: Status

   :statuscode 200: Post updated
   :statuscode 404: Post not found

.. http:delete:: /api/v1/posts/(int:id)

   Delete a blog post.

   :param id: Post identifier
   
   :statuscode 204: Post deleted
   :statuscode 404: Post not found
   :statuscode 403: Insufficient permissions

Configuration
-------------

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

Cross-References
----------------

Link to Endpoints
~~~~~~~~~~~~~~~~~

.. code-block:: rst

   See :http:get:`/users/(int:id)` for user details.
   
   Create users with :http:post:`/users`.
   
   Update via :http:put:`/users/(int:id)`.

Practical Tips
--------------

Organization
~~~~~~~~~~~~

Group related endpoints:

.. code-block:: rst

   Users
   -----
   
   .. http:get:: /users
   .. http:post:: /users
   .. http:get:: /users/(int:id)
   .. http:put:: /users/(int:id)
   .. http:delete:: /users/(int:id)

Error Handling
~~~~~~~~~~~~~~

Document error responses:

.. code-block:: rst

   :statuscode 400: Bad Request
   
      Example error response:
   
      .. sourcecode:: json
   
         {
             "error": "validation_error",
             "message": "Invalid email format",
             "field": "email"
         }

See Also
--------

- :doc:`../tutorials/packages/sphinxcontrib-httpdomain` - Complete tutorial
- GitHub repository: https://github.com/sphinx-contrib/httpdomain
