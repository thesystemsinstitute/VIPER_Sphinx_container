Sphinx-Apischema Tutorial
=========================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-apischema/>`_
   - `API Documentation <../../pdoc/sphinx_apischema/index.html>`_
   - `Manual <https://wyfo.github.io/apischema/>`_
   - :doc:`Working Example <../../examples/sphinx-apischema-example>`


.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinx-apischema to generate API documentation from JSON Schema and OpenAPI specifications.

What is Sphinx-Apischema?
--------------------------

sphinx-apischema is a Sphinx extension that provides:

- JSON Schema documentation
- OpenAPI/Swagger integration
- API schema rendering
- Type documentation
- Validation rules display
- Example generation
- Interactive schema viewer
- Cross-referencing
- Multiple schema formats
- REST API documentation

This allows you to document APIs directly from their schema definitions.

Installation
------------

sphinx-apischema is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinx_apischema; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``docs/conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_apischema',
   ]
   
   # Schema directory
   apischema_dir = '../schemas'

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinx_apischema']
   
   # Schema locations
   apischema_dir = '../schemas'
   apischema_openapi_dir = '../openapi'
   
   # Display options
   apischema_show_examples = True
   apischema_show_validation = True
   apischema_show_defaults = True
   
   # Formatting
   apischema_compact_mode = False
   apischema_expand_depth = 2


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

Basic Usage
-----------

Document JSON Schema
~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. apischema:: user.json

This renders the JSON schema from ``schemas/user.json``.

Document OpenAPI Spec
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. openapi:: api.yaml

Inline Schema
~~~~~~~~~~~~~

.. code-block:: rst

   .. apischema::
      
      {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {
          "name": {"type": "string"},
          "age": {"type": "integer"}
        }
      }

   API Schemas
   ===========
   
   User Schema
   -----------
   
   The User schema defines the structure of user objects in our API.
   
   .. apischema:: user.json
   
   Example Usage
   ~~~~~~~~~~~~~
   
   Valid user object:
   
   .. code-block:: json
      
      {
        "id": 123,
        "email": "john@example.com",
        "name": "John Doe",
        "age": 30,
        "roles": ["user"],
        "metadata": {
          "department": "Engineering",
          "location": "Remote"
        }
      }

Example 2: OpenAPI Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``openapi/api.yaml``:

.. code-block:: yaml

   openapi: 3.0.0
   info:
     title: User Management API
     version: 1.0.0
     description: API for managing users
   
   servers:
     - url: https://api.example.com/v1
       description: Production server
   
   paths:
     /users:
       get:
         summary: List users
         description: Retrieve a list of all users
         parameters:
           - name: limit
             in: query
             description: Maximum number of users to return
             schema:
               type: integer
               default: 20
               minimum: 1
               maximum: 100
           - name: offset
             in: query
             description: Number of users to skip
             schema:
               type: integer
               default: 0
               minimum: 0
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
                     total:
                       type: integer
       
       post:
         summary: Create user
         description: Create a new user
         requestBody:
           required: true
           content:
             application/json:
               schema:
                 $ref: '#/components/schemas/UserCreate'
         responses:
           '201':
             description: User created
             content:
               application/json:
                 schema:
                   $ref: '#/components/schemas/User'
   
   components:
     schemas:
       User:
         type: object
         required: [id, email, name]
         properties:
           id:
             type: integer
           email:
             type: string
             format: email
           name:
             type: string
       
       UserCreate:
         type: object
         required: [email, name]
         properties:
           email:
             type: string
             format: email
           name:
             type: string
           age:
             type: integer

``docs/api/rest.rst``:

.. code-block:: rst

   REST API
   ========
   
   This page documents our REST API endpoints.
   
   API Specification
   -----------------
   
   .. openapi:: api.yaml
   
   Authentication
   --------------
   
   All API requests require authentication using an API key:
   
   .. code-block:: bash
      
      curl -H "Authorization: Bearer YOUR_API_KEY" \
        https://api.example.com/v1/users
   
   Rate Limiting
   -------------
   
   - 1000 requests per hour per API key
   - Rate limit headers included in responses

Example 3: Complex Nested Schema
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``schemas/order.json``:

.. code-block:: json

   {
     "$schema": "http://json-schema.org/draft-07/schema#",
     "title": "Order",
     "type": "object",
     "required": ["id", "customer", "items", "total"],
     "properties": {
       "id": {
         "type": "string",
         "format": "uuid"
       },
       "customer": {
         "type": "object",
         "required": ["id", "email"],
         "properties": {
           "id": {"type": "integer"},
           "email": {"type": "string", "format": "email"},
           "name": {"type": "string"}
         }
       },
       "items": {
         "type": "array",
         "minItems": 1,
         "items": {
           "type": "object",
           "required": ["product_id", "quantity", "price"],
           "properties": {
             "product_id": {"type": "integer"},
             "product_name": {"type": "string"},
             "quantity": {
               "type": "integer",
               "minimum": 1
             },
             "price": {
               "type": "number",
               "minimum": 0
             }
           }
         }
       },
       "total": {
         "type": "number",
         "minimum": 0
       },
       "status": {
         "type": "string",
         "enum": ["pending", "processing", "shipped", "delivered", "cancelled"],
         "default": "pending"
       },
       "created_at": {
         "type": "string",
         "format": "date-time"
       }
     }
   }

``docs/api/order-schema.rst``:

.. code-block:: rst

   Order Schema
   ============
   
   .. apischema:: order.json
      :expand-depth: 3
      :show-examples: true

Example 4: Schema with References
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``schemas/definitions.json``:

.. code-block:: json

   {
     "$schema": "http://json-schema.org/draft-07/schema#",
     "definitions": {
       "address": {
         "type": "object",
         "properties": {
           "street": {"type": "string"},
           "city": {"type": "string"},
           "country": {"type": "string"},
           "postal_code": {"type": "string"}
         }
       },
       "contact": {
         "type": "object",
         "properties": {
           "email": {"type": "string", "format": "email"},
           "phone": {"type": "string"}
         }
       }
     }
   }

``schemas/company.json``:

.. code-block:: json

   {
     "$schema": "http://json-schema.org/draft-07/schema#",
     "title": "Company",
     "type": "object",
     "properties": {
       "name": {"type": "string"},
       "headquarters": {
         "$ref": "definitions.json#/definitions/address"
       },
       "contact": {
         "$ref": "definitions.json#/definitions/contact"
       }
     }
   }

Example 5: Interactive Schema Viewer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/api/interactive.rst``:

.. code-block:: rst

   Interactive API Documentation
   =============================
   
   .. apischema:: user.json
      :interactive: true
      :try-it-out: true
   
   Features:
   
   - Interactive schema browser
   - Example generator
   - Validation testing
   - Copy-paste examples

Advanced Features
-----------------

Schema Validation
~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   apischema_validate = True
   apischema_strict = True

Custom Templates
~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   apischema_templates = {
       'schema': '_templates/schema.html',
       'property': '_templates/property.html',
   }

Schema Preprocessing
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   def preprocess_schema(schema, filename):
       """Modify schema before rendering."""
       # Add custom fields
       schema['x-generated'] = True
       return schema
   
   apischema_preprocessor = preprocess_schema

Multiple Schema Versions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Version 2.0
   -----------
   
   .. apischema:: user-v2.json
   
   Version 1.0 (Legacy)
   --------------------
   
   .. apischema:: user-v1.json

Docker Integration
------------------

Build with Schemas
~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     kensai-sphinx:latest \
     sphinx-build -b html /project/docs /project/docs/_build/html

Validate Schemas
~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Validate all JSON schemas
   docker run --rm \
     -v $(pwd):/project \
     kensai-sphinx:latest \
     sh -c "cd /project && find schemas -name '*.json' -exec python -m json.tool {} \;"

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Build API Documentation
   
   on: [push]
   
   jobs:
     docs:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Validate Schemas
           run: |
             # Validate JSON schemas
             for file in schemas/*.json; do
               python -m json.tool "$file" > /dev/null || exit 1
             done
         
         - name: Build Documentation
           run: |
             docker run --rm -v $(pwd):/project \
               kensai-sphinx:latest \
               sphinx-build -b html /project/docs /project/docs/_build/html
         
         - name: Verify Schema Docs
           run: |
             # Check schemas were processed
             if ! grep -q "apischema" docs/_build/html/api/schemas.html; then
               echo "Schema documentation not found!"
               exit 1
             fi
         
         - name: Deploy
           uses: peaceiris/actions-gh-pages@v3
           with:
             github_token: ${{ secrets.GITHUB_TOKEN }}
             publish_dir: ./docs/_build/html

Best Practices
--------------

1. **Validate Schemas**
   
   Use JSON Schema validators

2. **Add Descriptions**
   
   Document all properties

3. **Include Examples**
   
   Show valid data

4. **Use References**
   
   Reuse common definitions

5. **Version Schemas**
   
   Track schema changes

6. **Keep Updated**
   
   Sync with API changes

Troubleshooting
---------------

Schema Not Found
~~~~~~~~~~~~~~~~

**Solution:**

Check path configuration:

.. code-block:: python

   apischema_dir = '../schemas'

Verify file exists:

.. code-block:: bash

   ls schemas/user.json

Invalid JSON
~~~~~~~~~~~~

**Solution:**

Validate JSON:

.. code-block:: bash

   python -m json.tool schemas/user.json

Reference Not Resolved
~~~~~~~~~~~~~~~~~~~~~~~

**Solution:**

Check reference path:

.. code-block:: json

   "$ref": "definitions.json#/definitions/address"

Ensure referenced file exists.

Rendering Issues
~~~~~~~~~~~~~~~~

**Solution:**

Check schema format:

.. code-block:: python

   apischema_validate = True

Review build warnings.

Next Steps
----------

1. Create JSON schemas
2. Configure apischema
3. Document in RST files
4. Add examples
5. Deploy documentation

Additional Resources
--------------------

- :doc:`sphinxcontrib-httpdomain` - HTTP API documentation
- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `JSON Schema <https://json-schema.org/>`_
- `OpenAPI Specification <https://swagger.io/specification/>`_
