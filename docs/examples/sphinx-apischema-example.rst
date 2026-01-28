Sphinx-APISchema Example
=========================

.. note::

   **Package**: sphinx-apischema  
   **Purpose**: Automatic API documentation generation from JSON/OpenAPI schemas  
   **Tutorial**: See :doc:`../tutorials/packages/sphinx-apischema` for complete tutorial

This page demonstrates the **sphinx-apischema** extension for generating API documentation from OpenAPI/Swagger specifications and JSON schemas.

.. contents:: Contents
   :local:
   :depth: 3

Overview
--------

What is sphinx-apischema?
~~~~~~~~~~~~~~~~~~~~~~~~~

sphinx-apischema is a powerful Sphinx extension that automatically generates comprehensive API documentation from:

- OpenAPI 3.0/3.1 specifications
- Swagger 2.0 specifications
- JSON Schema documents
- API Blueprint files

Key Features
~~~~~~~~~~~~

- **Automatic Documentation**: Generate complete API reference from schema files
- **Interactive Examples**: Include request/response examples automatically
- **Schema Validation**: Validate API schemas during build
- **Multiple Formats**: Support for OpenAPI, Swagger, JSON Schema
- **Customizable Templates**: Control documentation appearance
- **Type Information**: Detailed parameter and response type documentation
- **Authentication Documentation**: Automatic security scheme documentation
- **Code Generation**: Generate client code examples in multiple languages

Installation
------------

Using pip
~~~~~~~~~

Install the extension:

.. code-block:: bash

   pip install sphinx-apischema

Or add to your ``requirements.txt``:

.. code-block:: text

   sphinx-apischema>=2.0.0

With Optional Dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~~~

For full functionality:

.. code-block:: bash

   pip install sphinx-apischema[openapi,validation,codegen]

Configuration
-------------

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_apischema',
       # ... other extensions
   ]
   
   # Basic settings
   apischema_spec_file = '_static/openapi.yaml'
   apischema_output_dir = 'api'

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

Complete configuration with all options:

.. code-block:: python

   # API Schema Configuration
   apischema_spec_file = '_static/openapi.yaml'
   apischema_spec_format = 'openapi3'  # 'openapi3', 'swagger2', 'jsonschema'
   apischema_output_dir = 'api'
   
   # Generation Options
   apischema_generate_examples = True
   apischema_generate_models = True
   apischema_generate_endpoints = True
   
   # Documentation Options
   apischema_include_authentication = True
   apischema_include_responses = True
   apischema_include_request_body = True
   apischema_include_parameters = True
   
   # Display Options
   apischema_show_base_url = True
   apischema_show_operation_id = True
   apischema_show_tags = True
   apischema_group_by_tag = True
   
   # Code Examples
   apischema_example_languages = ['python', 'javascript', 'curl', 'java']
   apischema_example_format = 'tabs'  # 'tabs', 'accordion', 'list'
   
   # Validation
   apischema_validate_schema = True
   apischema_strict_mode = False
   
   # Template Customization
   apischema_template_dir = '_templates/apischema'
   apischema_custom_css = 'custom-api.css'

Directives
----------

apischema Directive
~~~~~~~~~~~~~~~~~~~

Generate API documentation from schema:

.. code-block:: rst

   .. apischema::
      :spec: _static/openapi.yaml
      :format: openapi3
      
      This is the main API documentation.

With Custom Options
~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. apischema::
      :spec: _static/api-spec.yaml
      :format: openapi3
      :output-dir: generated-api
      :title: REST API Reference
      :description: Complete API documentation
      :group-by: tag
      :show-base-url: true
      :generate-examples: true
      :languages: python, javascript, curl

apischema-endpoint Directive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Document a single endpoint:

.. code-block:: rst

   .. apischema-endpoint::
      :method: GET
      :path: /api/v1/users/{id}
      :spec: _static/openapi.yaml
      
      Retrieve user information by ID.

apischema-model Directive
~~~~~~~~~~~~~~~~~~~~~~~~~

Document a schema model:

.. code-block:: rst

   .. apischema-model::
      :name: User
      :spec: _static/openapi.yaml
      :show-examples: true
      :show-required: true
      
      User data model schema.

apischema-security Directive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Document authentication schemes:

.. code-block:: rst

   .. apischema-security::
      :spec: _static/openapi.yaml
      :schemes: bearer, apikey
      
      Authentication and security configuration.

Roles
-----

Inline API References
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Use the :apischema-endpoint:`GET /users` to list users.
   
   The :apischema-model:`User` model contains user data.
   
   Authentication requires :apischema-security:`bearer` token.

Practical Examples
------------------

Complete REST API Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**File**: ``api/index.rst``

.. code-block:: rst

   API Documentation
   =================
   
   .. apischema::
      :spec: ../_static/openapi.yaml
      :format: openapi3
      :title: MyApp REST API
      :group-by: tag
      :generate-examples: true
      :languages: python, javascript, curl, java
      
      Complete API reference for MyApp platform.

Sample OpenAPI Specification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**File**: ``_static/openapi.yaml``

.. code-block:: yaml

   openapi: 3.0.3
   info:
     title: MyApp API
     version: 1.0.0
     description: RESTful API for MyApp platform
     contact:
       name: API Support
       email: api@myapp.com
   
   servers:
     - url: https://api.myapp.com/v1
       description: Production server
     - url: https://staging-api.myapp.com/v1
       description: Staging server
   
   paths:
     /users:
       get:
         summary: List users
         description: Retrieve a paginated list of users
         operationId: listUsers
         tags:
           - Users
         parameters:
           - name: page
             in: query
             description: Page number
             required: false
             schema:
               type: integer
               default: 1
           - name: limit
             in: query
             description: Items per page
             required: false
             schema:
               type: integer
               default: 20
               maximum: 100
         responses:
           '200':
             description: Successful response
             content:
               application/json:
                 schema:
                   type: object
                   properties:
                     users:
                       type: array
                       items:
                         $ref: '#/components/schemas/User'
                     pagination:
                       $ref: '#/components/schemas/Pagination'
           '401':
             $ref: '#/components/responses/Unauthorized'
     
     /users/{id}:
       get:
         summary: Get user by ID
         description: Retrieve detailed user information
         operationId: getUser
         tags:
           - Users
         parameters:
           - name: id
             in: path
             description: User ID
             required: true
             schema:
               type: string
               format: uuid
         responses:
           '200':
             description: User found
             content:
               application/json:
                 schema:
                   $ref: '#/components/schemas/User'
           '404':
             $ref: '#/components/responses/NotFound'
       
       put:
         summary: Update user
         description: Update user information
         operationId: updateUser
         tags:
           - Users
         parameters:
           - name: id
             in: path
             required: true
             schema:
               type: string
               format: uuid
         requestBody:
           required: true
           content:
             application/json:
               schema:
                 $ref: '#/components/schemas/UserUpdate'
         responses:
           '200':
             description: User updated
             content:
               application/json:
                 schema:
                   $ref: '#/components/schemas/User'
           '400':
             $ref: '#/components/responses/BadRequest'
   
   components:
     schemas:
       User:
         type: object
         required:
           - id
           - email
           - username
         properties:
           id:
             type: string
             format: uuid
             description: Unique user identifier
           email:
             type: string
             format: email
             description: User email address
           username:
             type: string
             minLength: 3
             maxLength: 50
             description: Unique username
           firstName:
             type: string
             description: User's first name
           lastName:
             type: string
             description: User's last name
           createdAt:
             type: string
             format: date-time
             description: Account creation timestamp
           updatedAt:
             type: string
             format: date-time
             description: Last update timestamp
         example:
           id: "550e8400-e29b-41d4-a716-446655440000"
           email: "user@example.com"
           username: "johndoe"
           firstName: "John"
           lastName: "Doe"
           createdAt: "2024-01-15T10:30:00Z"
           updatedAt: "2024-01-20T14:45:00Z"
       
       UserUpdate:
         type: object
         properties:
           email:
             type: string
             format: email
           firstName:
             type: string
           lastName:
             type: string
       
       Pagination:
         type: object
         properties:
           page:
             type: integer
           limit:
             type: integer
           total:
             type: integer
           totalPages:
             type: integer
       
       Error:
         type: object
         required:
           - code
           - message
         properties:
           code:
             type: string
           message:
             type: string
           details:
             type: object
     
     responses:
       Unauthorized:
         description: Authentication required
         content:
           application/json:
             schema:
               $ref: '#/components/schemas/Error'
       
       NotFound:
         description: Resource not found
         content:
           application/json:
             schema:
               $ref: '#/components/schemas/Error'
       
       BadRequest:
         description: Invalid request
         content:
           application/json:
             schema:
               $ref: '#/components/schemas/Error'
     
     securitySchemes:
       bearerAuth:
         type: http
         scheme: bearer
         bearerFormat: JWT
       
       apiKey:
         type: apiKey
         in: header
         name: X-API-Key
   
   security:
     - bearerAuth: []

Endpoint Documentation
~~~~~~~~~~~~~~~~~~~~~~

Document specific endpoints:

.. code-block:: rst

   User Endpoints
   --------------
   
   List Users
   ~~~~~~~~~~
   
   .. apischema-endpoint::
      :method: GET
      :path: /users
      :spec: ../_static/openapi.yaml
      :show-examples: true
      :languages: python, curl
      
      Retrieve a paginated list of all users.
   
   Get User by ID
   ~~~~~~~~~~~~~~
   
   .. apischema-endpoint::
      :method: GET
      :path: /users/{id}
      :spec: ../_static/openapi.yaml
      :show-examples: true
      
      Retrieve detailed information for a specific user.

Model Documentation
~~~~~~~~~~~~~~~~~~~

Document data models separately:

.. code-block:: rst

   Data Models
   -----------
   
   User Model
   ~~~~~~~~~~
   
   .. apischema-model::
      :name: User
      :spec: ../_static/openapi.yaml
      :show-examples: true
      :show-required: true
      :show-constraints: true
      
      The User model represents a user account in the system.
   
   Pagination Model
   ~~~~~~~~~~~~~~~~
   
   .. apischema-model::
      :name: Pagination
      :spec: ../_static/openapi.yaml
      
      Pagination metadata for list responses.

Authentication Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Authentication
   --------------
   
   .. apischema-security::
      :spec: ../_static/openapi.yaml
      
      The API supports multiple authentication methods.
   
   Bearer Token Authentication
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~
   
   Include JWT token in Authorization header:
   
   .. code-block:: http
   
      GET /api/v1/users HTTP/1.1
      Host: api.myapp.com
      Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
   
   API Key Authentication
   ~~~~~~~~~~~~~~~~~~~~~~
   
   Include API key in custom header:
   
   .. code-block:: http
   
      GET /api/v1/users HTTP/1.1
      Host: api.myapp.com
      X-API-Key: your-api-key-here

Customization
-------------

Custom Templates
~~~~~~~~~~~~~~~~

Create custom templates in ``_templates/apischema/``:

**File**: ``_templates/apischema/endpoint.html``

.. code-block:: html+jinja

   <div class="api-endpoint">
     <div class="endpoint-header">
       <span class="method method-{{ method|lower }}">{{ method }}</span>
       <code class="endpoint-path">{{ path }}</code>
     </div>
     
     <div class="endpoint-description">
       {{ description }}
     </div>
     
     {% if parameters %}
     <div class="endpoint-parameters">
       <h4>Parameters</h4>
       <table>
         <thead>
           <tr>
             <th>Name</th>
             <th>Type</th>
             <th>Required</th>
             <th>Description</th>
           </tr>
         </thead>
         <tbody>
           {% for param in parameters %}
           <tr>
             <td><code>{{ param.name }}</code></td>
             <td>{{ param.type }}</td>
             <td>{{ 'Yes' if param.required else 'No' }}</td>
             <td>{{ param.description }}</td>
           </tr>
           {% endfor %}
         </tbody>
       </table>
     </div>
     {% endif %}
     
     {% if examples %}
     <div class="endpoint-examples">
       <h4>Examples</h4>
       {{ examples }}
     </div>
     {% endif %}
   </div>

Custom CSS
~~~~~~~~~~

**File**: ``_static/custom-api.css``

.. code-block:: css

   .api-endpoint {
       margin: 2em 0;
       border: 1px solid #ddd;
       border-radius: 4px;
       padding: 1em;
   }
   
   .endpoint-header {
       margin-bottom: 1em;
   }
   
   .method {
       display: inline-block;
       padding: 0.25em 0.5em;
       border-radius: 3px;
       font-weight: bold;
       color: white;
       margin-right: 0.5em;
   }
   
   .method-get { background-color: #61affe; }
   .method-post { background-color: #49cc90; }
   .method-put { background-color: #fca130; }
   .method-delete { background-color: #f93e3e; }
   .method-patch { background-color: #50e3c2; }
   
   .endpoint-path {
       font-family: monospace;
       font-size: 1.1em;
   }
   
   .endpoint-parameters table {
       width: 100%;
       border-collapse: collapse;
   }
   
   .endpoint-parameters th,
   .endpoint-parameters td {
       padding: 0.5em;
       border: 1px solid #ddd;
       text-align: left;
   }
   
   .endpoint-parameters th {
       background-color: #f5f5f5;
       font-weight: bold;
   }

Best Practices
--------------

Schema Organization
~~~~~~~~~~~~~~~~~~~

1. **Separate Schema Files**: Keep API specs separate from documentation
2. **Version Control**: Include schema files in version control
3. **Schema Validation**: Enable validation in conf.py
4. **Modular Schemas**: Use $ref for reusable components

Example structure:

.. code-block:: text

   docs/
   ├── _static/
   │   ├── openapi.yaml          # Main spec
   │   └── schemas/
   │       ├── users.yaml        # User schemas
   │       ├── products.yaml     # Product schemas
   │       └── common.yaml       # Shared schemas
   ├── api/
   │   ├── index.rst             # API overview
   │   ├── endpoints.rst         # Endpoint reference
   │   ├── models.rst            # Data models
   │   └── authentication.rst    # Auth documentation
   └── conf.py

Documentation Structure
~~~~~~~~~~~~~~~~~~~~~~~

Organize API documentation logically:

.. code-block:: rst

   API Reference
   =============
   
   .. toctree::
      :maxdepth: 2
      
      api/overview
      api/authentication
      api/endpoints
      api/models
      api/errors
      api/changelog

Schema Validation
~~~~~~~~~~~~~~~~~

Enable strict validation:

.. code-block:: python

   # conf.py
   apischema_validate_schema = True
   apischema_strict_mode = True
   apischema_fail_on_warnings = True

Code Examples
~~~~~~~~~~~~~

Provide examples in multiple languages:

.. code-block:: python

   apischema_example_languages = [
       'python',
       'javascript',
       'curl',
       'java',
       'ruby',
       'php',
   ]

Troubleshooting
---------------

Schema Not Found
~~~~~~~~~~~~~~~~

**Problem**: Schema file not found during build

**Solution**:

.. code-block:: python

   import os
   
   # Use absolute path
   apischema_spec_file = os.path.join(
       os.path.dirname(__file__), 
       '_static/openapi.yaml'
   )

Invalid Schema Format
~~~~~~~~~~~~~~~~~~~~~

**Problem**: Schema validation errors

**Solution**: Validate schema separately:

.. code-block:: bash

   # Install validator
   pip install openapi-spec-validator
   
   # Validate schema
   openapi-spec-validator docs/_static/openapi.yaml

Missing Examples
~~~~~~~~~~~~~~~~

**Problem**: Code examples not generated

**Solution**:

.. code-block:: python

   # Enable example generation
   apischema_generate_examples = True
   
   # Specify languages
   apischema_example_languages = ['python', 'curl']
   
   # Ensure examples exist in schema
   # Add 'example' fields to OpenAPI spec

Build Performance
~~~~~~~~~~~~~~~~~

**Problem**: Slow documentation builds

**Solution**:

.. code-block:: python

   # Cache generated documentation
   apischema_cache_enabled = True
   apischema_cache_dir = '.apischema_cache'
   
   # Limit generation
   apischema_generate_models = False  # If not needed
   apischema_generate_examples = False  # For faster builds

Integration Examples
--------------------

With Sphinx-Autodoc
~~~~~~~~~~~~~~~~~~~

Combine API schema documentation with Python autodoc:

.. code-block:: rst

   API Client
   ----------
   
   Python SDK
   ~~~~~~~~~~
   
   .. autoclass:: myapp.client.APIClient
      :members:
      :undoc-members:
   
   API Reference
   ~~~~~~~~~~~~~
   
   .. apischema::
      :spec: ../_static/openapi.yaml
      :title: REST API Endpoints

With Sphinx-Tabs
~~~~~~~~~~~~~~~~

Organize examples with tabs:

.. code-block:: rst

   .. tabs::
   
      .. tab:: Python
      
         .. code-block:: python
         
            import requests
            
            response = requests.get('https://api.myapp.com/v1/users')
            users = response.json()
      
      .. tab:: JavaScript
      
         .. code-block:: javascript
         
            fetch('https://api.myapp.com/v1/users')
              .then(response => response.json())
              .then(users => console.log(users));
      
      .. tab:: cURL
      
         .. code-block:: bash
         
            curl https://api.myapp.com/v1/users

With ReadTheDocs
~~~~~~~~~~~~~~~~

Configure for ReadTheDocs builds:

.. code-block:: python

   # conf.py
   import os
   
   # Detect RTD environment
   on_rtd = os.environ.get('READTHEDOCS') == 'True'
   
   if on_rtd:
       # Use relative paths for RTD
       apischema_spec_file = '_static/openapi.yaml'
   else:
       # Use absolute paths locally
       apischema_spec_file = os.path.join(
           os.path.dirname(__file__),
           '_static/openapi.yaml'
       )

Advanced Usage
--------------

Multiple API Versions
~~~~~~~~~~~~~~~~~~~~~

Document multiple API versions:

.. code-block:: rst

   API v1
   ------
   
   .. apischema::
      :spec: ../_static/openapi-v1.yaml
      :output-dir: api/v1
      :title: API v1 Reference
   
   API v2
   ------
   
   .. apischema::
      :spec: ../_static/openapi-v2.yaml
      :output-dir: api/v2
      :title: API v2 Reference

GraphQL Integration
~~~~~~~~~~~~~~~~~~~

Document GraphQL APIs alongside REST:

.. code-block:: rst

   REST API
   --------
   
   .. apischema::
      :spec: ../_static/openapi.yaml
   
   GraphQL API
   -----------
   
   .. graphql-schema:: ../_static/schema.graphql
      :show-queries: true
      :show-mutations: true

Dynamic Schema Loading
~~~~~~~~~~~~~~~~~~~~~~

Load schemas dynamically:

.. code-block:: python

   # conf.py
   import requests
   import yaml
   
   def download_schema(url, output_path):
       response = requests.get(url)
       with open(output_path, 'w') as f:
           f.write(response.text)
   
   # Download schema before build
   def setup(app):
       schema_url = 'https://api.myapp.com/openapi.json'
       schema_path = '_static/openapi.yaml'
       download_schema(schema_url, schema_path)
   
   apischema_spec_file = '_static/openapi.yaml'

See Also
--------

Related Extensions
~~~~~~~~~~~~~~~~~~

- :doc:`sphinx-autodoc-example` - Python API documentation
- :doc:`sphinx-autoapi-example` - Automatic API documentation
- :doc:`breathe-example` - C/C++ API documentation
- :doc:`sphinx-swagger-example` - Swagger UI integration

External Resources
~~~~~~~~~~~~~~~~~~

- OpenAPI Specification: https://spec.openapis.org/
- JSON Schema: https://json-schema.org/
- API Blueprint: https://apiblueprint.org/
- Swagger Editor: https://editor.swagger.io/

Summary
-------

sphinx-apischema provides comprehensive API documentation generation from schema files:

- **Multiple Formats**: OpenAPI, Swagger, JSON Schema support
- **Automatic Generation**: Complete documentation from specifications
- **Rich Documentation**: Parameters, models, examples, authentication
- **Customizable**: Templates, styling, organization options
- **Integration**: Works with other Sphinx extensions
- **Validation**: Schema validation during builds

Perfect for documenting REST APIs, microservices, and web services with formal API specifications.
