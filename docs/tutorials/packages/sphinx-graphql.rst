Sphinx GraphQL Tutorial
=======================

.. note::

   **Package Resources:**

   - `PyPI Package <https://pypi.org/project/sphinx-graphql/>`_
   - `API Documentation <../../pdoc/sphinx_graphql/index.html>`_
   - `Manual <https://dls-controls.github.io/sphinx-graphql>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial covers sphinx-graphql, a Sphinx extension for documenting GraphQL APIs.

What is Sphinx GraphQL?
----------------------
Sphinx GraphQL provides directives for rendering GraphQL schemas and GraphiQL views inside Sphinx documentation.

Installation
------------

Install via pip:

.. code-block:: bash

   pip install sphinx-graphql

Configuration
-------------

Enable the extension in ``conf.py``:

.. code-block:: python

   extensions = [
       "sphinx_graphql",
   ]

Basic Usage
-----------

Embed a GraphiQL view:

.. code-block:: restructuredtext

   .. graphiql::
      :endpoint: https://api.example.com/graphql

Document GraphQL Types
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: restructuredtext

   .. graphql:type:: User

      Represents a user in the system.

      **Fields:**

      - ``id: ID!`` - Unique identifier
      - ``name: String!`` - User's display name
      - ``email: String`` - Email address
      - ``createdAt: DateTime!`` - Account creation timestamp

Advanced Features
-----------------

- Render schema documentation alongside GraphiQL.
- Configure endpoints per environment.
- Document types, queries, mutations, and subscriptions.
- Auto-generate type references.
- Support for schema introspection.

Configuration Options
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py

   extensions = ["sphinx_graphql"]

   # GraphQL configuration
   graphql_endpoint = "https://api.example.com/graphql"
   graphql_schema_path = "_static/schema.graphql"  # Local schema file
   graphql_introspection = True  # Enable schema introspection
   graphql_headers = {
       "Authorization": "Bearer ${GRAPHQL_TOKEN}"
   }

Examples
--------

Complete API Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Define your GraphQL schema (``_static/schema.graphql``):

.. code-block:: graphql

   """
   User account in the system.
   """
   type User {
     "Unique identifier"
     id: ID!

     "User's display name"
     name: String!

     "Email address (optional)"
     email: String

     "User's posts"
     posts(first: Int = 10): [Post!]!

     "Account creation date"
     createdAt: DateTime!
   }

   """
   Blog post content.
   """
   type Post {
     id: ID!
     title: String!
     content: String!
     author: User!
     tags: [String!]!
     publishedAt: DateTime
     status: PostStatus!
   }

   enum PostStatus {
     DRAFT
     PUBLISHED
     ARCHIVED
   }

   type Query {
     "Get user by ID"
     user(id: ID!): User

     "List all users"
     users(first: Int = 20, after: String): UserConnection!

     "Get post by ID"
     post(id: ID!): Post

     "Search posts"
     searchPosts(query: String!, limit: Int = 10): [Post!]!
   }

   type Mutation {
     "Create a new user"
     createUser(input: CreateUserInput!): User!

     "Update user profile"
     updateUser(id: ID!, input: UpdateUserInput!): User

     "Create a new post"
     createPost(input: CreatePostInput!): Post!

     "Publish a draft post"
     publishPost(id: ID!): Post
   }

   input CreateUserInput {
     name: String!
     email: String!
   }

   input UpdateUserInput {
     name: String
     email: String
   }

   input CreatePostInput {
     title: String!
     content: String!
     tags: [String!]
   }

   type Subscription {
     "Subscribe to new posts"
     postCreated: Post!

     "Subscribe to user updates"
     userUpdated(userId: ID!): User!
   }

2. Document your API (``docs/api/graphql.rst``):

.. code-block:: restructuredtext

   GraphQL API Reference
   =====================

   Interactive Explorer
   --------------------

   Use the GraphiQL interface below to explore the API:

   .. graphiql::
      :endpoint: https://api.example.com/graphql
      :height: 600px

   Types
   -----

   User
   ~~~~

   .. graphql:type:: User
      :schema: _static/schema.graphql

      Represents a user account in the system.

      **Fields:**

      .. list-table::
         :header-rows: 1
         :widths: 20 20 60

         * - Field
           - Type
           - Description
         * - ``id``
           - ``ID!``
           - Unique identifier
         * - ``name``
           - ``String!``
           - User's display name
         * - ``email``
           - ``String``
           - Email address (optional)
         * - ``posts``
           - ``[Post!]!``
           - User's authored posts
         * - ``createdAt``
           - ``DateTime!``
           - Account creation timestamp

   Post
   ~~~~

   .. graphql:type:: Post

      Blog post or article content.

      **Fields:**

      .. list-table::
         :header-rows: 1
         :widths: 20 20 60

         * - Field
           - Type
           - Description
         * - ``id``
           - ``ID!``
           - Unique identifier
         * - ``title``
           - ``String!``
           - Post title
         * - ``content``
           - ``String!``
           - Post body content
         * - ``author``
           - ``User!``
           - Post author
         * - ``status``
           - ``PostStatus!``
           - Publication status

   Queries
   -------

   user
   ~~~~

   .. graphql:query:: user(id: ID!): User

      Retrieve a user by their unique identifier.

      **Arguments:**

      - ``id`` (ID!, required): The user's unique identifier

      **Returns:** User or null if not found

      **Example:**

      .. code-block:: graphql

         query GetUser {
           user(id: "user-123") {
             id
             name
             email
             posts(first: 5) {
               title
               status
             }
           }
         }

   searchPosts
   ~~~~~~~~~~~

   .. graphql:query:: searchPosts(query: String!, limit: Int = 10): [Post!]!

      Search for posts matching a query string.

      **Arguments:**

      - ``query`` (String!, required): Search term
      - ``limit`` (Int, optional): Max results (default: 10)

      **Example:**

      .. code-block:: graphql

         query SearchPosts {
           searchPosts(query: "sphinx documentation", limit: 5) {
             id
             title
             author {
               name
             }
             publishedAt
           }
         }

   Mutations
   ---------

   createUser
   ~~~~~~~~~~

   .. graphql:mutation:: createUser(input: CreateUserInput!): User!

      Create a new user account.

      **Input Fields:**

      - ``name`` (String!, required): Display name
      - ``email`` (String!, required): Email address

      **Example:**

      .. code-block:: graphql

         mutation CreateUser {
           createUser(input: {
             name: "John Doe"
             email: "john@example.com"
           }) {
             id
             name
             createdAt
           }
         }

   publishPost
   ~~~~~~~~~~~

   .. graphql:mutation:: publishPost(id: ID!): Post

      Publish a draft post, making it publicly visible.

      **Example:**

      .. code-block:: graphql

         mutation PublishPost {
           publishPost(id: "post-456") {
             id
             title
             status
             publishedAt
           }
         }

   Subscriptions
   -------------

   postCreated
   ~~~~~~~~~~~

   .. graphql:subscription:: postCreated: Post!

      Subscribe to new post creation events.

      **Example:**

      .. code-block:: graphql

         subscription OnPostCreated {
           postCreated {
             id
             title
             author {
               name
             }
           }
         }

Multi-Environment Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   import os

   # Environment-based endpoint
   graphql_endpoints = {
       "production": "https://api.example.com/graphql",
       "staging": "https://staging-api.example.com/graphql",
       "development": "http://localhost:4000/graphql",
   }

   graphql_endpoint = graphql_endpoints.get(
       os.environ.get("DOCS_ENV", "production")
   )

   # Authentication for private schemas
   graphql_headers = {}
   if os.environ.get("GRAPHQL_TOKEN"):
       graphql_headers["Authorization"] = f"Bearer {os.environ['GRAPHQL_TOKEN']}"

Schema Documentation Generation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Auto-generate documentation from introspection:

.. code-block:: bash

   # Generate schema documentation
   sphinx-graphql-generate-docs \
       --endpoint https://api.example.com/graphql \
       --output docs/api/generated/

Integration with Apollo/Relay
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: restructuredtext

   Client Integration
   ==================

   Apollo Client Example
   ---------------------

   .. code-block:: typescript

      import { ApolloClient, InMemoryCache, gql } from '@apollo/client';

      const client = new ApolloClient({
        uri: 'https://api.example.com/graphql',
        cache: new InMemoryCache(),
      });

      // Query matching :graphql:query:`user`
      const GET_USER = gql`
        query GetUser($id: ID!) {
          user(id: $id) {
            id
            name
            email
          }
        }
      `;

   See :graphql:query:`user` for the full API specification.

Additional Resources
--------------------

- `Manual <https://dls-controls.github.io/sphinx-graphql>`_
- `PyPI <https://pypi.org/project/sphinx-graphql/>`_
- `API Documentation <../../pdoc/sphinx_graphql/index.html>`_
