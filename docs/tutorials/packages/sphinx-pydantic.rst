Sphinx Pydantic Tutorial
========================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-pydantic/>`_
   - `API Documentation <../../pdoc/sphinx_pydantic/index.html>`_
   - `Manual <https://autodoc-pydantic.readthedocs.io/>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinx-pydantic in your Sphinx documentation.

What is Sphinx Pydantic?
-------------------------
sphinx-pydantic is a Sphinx extension that provides:

- Enhanced Pydantic documentation
- Easy integration with Sphinx
- Comprehensive configuration options
- Professional documentation output

sphinx-pydantic provides:

- Enhanced Pydantic documentation
- Integration with Sphinx documentation
- Flexible configuration options
- Professional output formatting

Key Features
~~~~~~~~~~~~

- **Enhanced Documentation**: Rich Pydantic model documentation
- **Field Summary**: Tabular field information
- **JSON Schema**: Display JSON/YAML schemas
- **Validators**: Document custom validators


Installation
------------

sphinx-pydantic is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinx_pydantic; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``docs/conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_pydantic',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinx_pydantic']
   
   # Configuration options
   pydantic_show_json = True
   pydantic_show_field_summary = True


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_pydantic',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

Complete configuration with all features:

.. code-block:: python

   extensions = ['sphinx_pydantic']
   
   # Package-specific configuration
   pydantic_show_json = True
   pydantic_show_field_summary = True
   pydantic_show_validators = True
   pydantic_show_config_summary = True
   pydantic_show_schema = True

Basic Usage
-----------

Getting Started
~~~~~~~~~~~~~~~

Document Pydantic models:

.. code-block:: rst

   .. pydantic:: myapp.models.User

Show Field Details
~~~~~~~~~~~~~~~~~~

Display field information:

.. code-block:: rst

   .. pydantic:: myapp.models.User
      :show-fields:
      :show-json:

Common Use Cases
----------------

Model Documentation
~~~~~~~~~~~~~~~~~~~

Document data models:

.. code-block:: rst

   .. pydantic:: myapp.models.User
      :show-fields:
      :show-validators:
      :show-config:

API Models
~~~~~~~~~~

Document API models:

.. code-block:: rst

   .. pydantic:: myapp.api.UserRequest
      :show-json-schema:

Advanced Features
-----------------

Field Summary
~~~~~~~~~~~~~

Show field summary table:

.. code-block:: rst

   .. pydantic:: myapp.models.User
      :field-summary:

JSON Schema
~~~~~~~~~~~

Display JSON schema:

.. code-block:: rst

   .. pydantic:: myapp.models.User
      :show-json-schema:
      :schema-format: yaml

Best Practices
--------------

Tips and Guidelines
~~~~~~~~~~~~~~~~~~~

- Add field descriptions
- Document validators
- Show JSON examples
- Include config options
- Keep documentation updated

Troubleshooting
---------------

Common Issues
~~~~~~~~~~~~~

**Issue**: Model not rendering

**Solution**: Check model path and ensure Pydantic is installed.

**Issue**: Fields missing

**Solution**: Verify field definitions and configuration.


Practical Examples
------------------

Overview
--------


Key Features
~~~~~~~~~~~~

- **Enhanced Documentation**: Rich Pydantic model documentation
- **Field Summary**: Tabular field information
- **JSON Schema**: Display JSON/YAML schemas
- **Validators**: Document custom validators

Installation
------------

Using pip
~~~~~~~~~

Install the extension:

.. code-block:: bash

   pip install sphinx-pydantic

Or add to your ``requirements.txt``:

.. code-block:: text

   sphinx-pydantic
   sphinx>=5.0.0
   pydantic>=1.8.0

Configuration
-------------

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_pydantic',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

Complete configuration with all features:

.. code-block:: python

   extensions = ['sphinx_pydantic']
   
   # Package-specific configuration
   pydantic_show_json = True
   pydantic_show_field_summary = True
   pydantic_show_validators = True
   pydantic_show_config_summary = True
   pydantic_show_schema = True

Basic Usage
-----------

Example 1: Basic Model Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create and document a model:

.. code-block:: python

   # myapp/models.py
   from pydantic import BaseModel, Field
   
   class User(BaseModel):
       """User model for authentication."""
       
       id: int = Field(..., description="Unique user identifier")
       username: str = Field(..., min_length=3, max_length=50)
       email: str = Field(..., description="User email address")
       is_active: bool = Field(default=True)

Document it:

.. code-block:: rst

   User Model
   ==========
   
   .. pydantic:: myapp.models.User
      :show-fields:
      :show-json:

Example 2: Complete Model Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Full documentation with all features:

.. code-block:: rst

   .. pydantic:: myapp.models.User
      :show-fields:
      :show-validators:
      :show-config:
      :show-json-schema:

Real-World Examples
-------------------

Example: API Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~

Document REST API models:

.. code-block:: python

   # myapp/api/models.py
   from typing import Optional, List
   from pydantic import BaseModel, Field, HttpUrl, validator
   from datetime import datetime
   
   class CreatePostRequest(BaseModel):
       """Request model for creating a blog post."""
       
       title: str = Field(
           ...,
           min_length=1,
           max_length=200,
           description="Post title"
       )
       content: str = Field(
           ...,
           min_length=10,
           description="Post content"
       )
       tags: List[str] = Field(
           default_factory=list,
           description="Post tags"
       )
       published: bool = Field(
           default=False,
           description="Publication status"
       )
       
       @validator('tags')
       def validate_tags(cls, v):
           """Ensure tags are lowercase and unique."""
           return list(set(tag.lower() for tag in v))
   
   class PostResponse(BaseModel):
       """Response model for a blog post."""
       
       id: int = Field(..., description="Post ID")
       title: str
       content: str
       tags: List[str]
       author_id: int
       published: bool
       created_at: datetime
       updated_at: Optional[datetime] = None
       view_count: int = Field(default=0, ge=0)
       
       class Config:
           orm_mode = True
           json_encoders = {
               datetime: lambda v: v.isoformat()
           }

Documentation:

.. code-block:: rst

   Blog API Models
   ===============
   
   Create Post Request
   -------------------
   
   .. pydantic:: myapp.api.models.CreatePostRequest
      :show-fields:
      :show-validators:
      :show-json:
   
   Example Usage:
   
   .. code-block:: python
   
      request = CreatePostRequest(
          title="My First Post",
          content="This is the content...",
          tags=["python", "tutorial"],
          published=True
      )
   
   Post Response
   -------------
   
   .. pydantic:: myapp.api.models.PostResponse
      :show-fields:
      :show-config:
      :show-json-schema:

Example: Configuration Models
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Document application settings:

.. code-block:: python

   # myapp/settings.py
   from pydantic import BaseSettings, Field, validator
   from typing import Optional
   
   class DatabaseSettings(BaseSettings):
       """Database configuration."""
       
       host: str = Field("localhost", description="Database host")
       port: int = Field(5432, ge=1, le=65535)
       username: str = Field(..., description="Database username")
       password: str = Field(..., description="Database password")
       database: str = Field(..., description="Database name")
       pool_size: int = Field(10, ge=1, le=100)
       
       class Config:
           env_prefix = "DB_"
       
       @property
       def url(self) -> str:
           """Generate database URL."""
           return f"postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"
   
   class AppSettings(BaseSettings):
       """Application configuration."""
       
       app_name: str = Field("MyApp", description="Application name")
       debug: bool = Field(False, description="Debug mode")
       secret_key: str = Field(..., min_length=32)
       allowed_hosts: List[str] = Field(default_factory=list)
       database: DatabaseSettings = Field(default_factory=DatabaseSettings)
       
       class Config:
           env_file = ".env"
           env_nested_delimiter = "__"

Documentation:

.. code-block:: rst

   Application Configuration
   =========================
   
   App Settings
   ------------
   
   .. pydantic:: myapp.settings.AppSettings
      :show-fields:
      :show-config:
      :show-json:
   
   Database Settings
   -----------------
   
   .. pydantic:: myapp.settings.DatabaseSettings
      :show-fields:
      :show-config:
      :show-json:
   
   Environment Variables
   ---------------------
   
   App settings can be configured via environment variables:
   
   .. code-block:: bash
   
      # App configuration
      export APP_NAME="MyApp"
      export DEBUG=true
      export SECRET_KEY="your-secret-key-here"
      
      # Database configuration
      export DB_HOST=localhost
      export DB_PORT=5432
      export DB_USERNAME=myuser
      export DB_PASSWORD=mypassword
      export DB_DATABASE=mydb

Example: Complex Nested Models
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Document nested data structures:

.. code-block:: python

   from pydantic import BaseModel, Field
   from typing import List, Optional
   from datetime import datetime
   from enum import Enum
   
   class OrderStatus(str, Enum):
       """Order status enumeration."""
       pending = "pending"
       processing = "processing"
       shipped = "shipped"
       delivered = "delivered"
       cancelled = "cancelled"
   
   class ProductVariant(BaseModel):
       """Product variant model."""
       
       sku: str = Field(..., description="Stock keeping unit")
       size: str
       color: str
       price: float = Field(..., gt=0)
       stock: int = Field(..., ge=0)
   
   class OrderItem(BaseModel):
       """Order item model."""
       
       product_id: int
       variant: ProductVariant
       quantity: int = Field(..., gt=0)
       unit_price: float = Field(..., gt=0)
       
       @property
       def total_price(self) -> float:
           """Calculate total price."""
           return self.quantity * self.unit_price
   
   class ShippingAddress(BaseModel):
       """Shipping address model."""
       
       recipient: str
       street: str
       city: str
       state: str = Field(..., min_length=2, max_length=2)
       zip_code: str
       country: str = Field(default="US")
       phone: Optional[str] = None
   
   class Order(BaseModel):
       """Order model."""
       
       id: int
       customer_id: int
       items: List[OrderItem]
       shipping_address: ShippingAddress
       status: OrderStatus = Field(default=OrderStatus.pending)
       created_at: datetime
       updated_at: Optional[datetime] = None
       
       @property
       def total_amount(self) -> float:
           """Calculate total order amount."""
           return sum(item.total_price for item in self.items)

Documentation:

.. code-block:: rst

   E-commerce Models
   =================
   
   Order Model
   -----------
   
   .. pydantic:: myapp.models.Order
      :show-fields:
      :show-json-schema:
   
   Order Item
   ----------
   
   .. pydantic:: myapp.models.OrderItem
      :show-fields:
   
   Product Variant
   ---------------
   
   .. pydantic:: myapp.models.ProductVariant
      :show-fields:
   
   Shipping Address
   ----------------
   
   .. pydantic:: myapp.models.ShippingAddress
      :show-fields:
      :show-json:

Best Practices
--------------

Recommendations
~~~~~~~~~~~~~~~

- Add comprehensive field descriptions
- Use Field() for all fields
- Document validators with docstrings
- Show JSON examples for API models
- Display JSON schema for integrations

Common Patterns
~~~~~~~~~~~~~~~

Standard patterns for using sphinx-pydantic:

1. **API Documentation**: Show fields, JSON, and schema
2. **Settings**: Document configuration with examples
3. **Complex Models**: Break down nested structures

Integration Tips
----------------

Working with Other Extensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

sphinx-pydantic integrates well with:

- pydantic-sphinx for alternative approach
- sphinx.ext.autodoc for general documentation
- OpenAPI extensions for REST APIs

Additional Resources
--------------------

- `PyPI Package <https://pypi.org/project/sphinx-pydantic/>`_
- `Official Documentation <https://sphinx-pydantic.readthedocs.io/>`_
- :doc:`Complete Tutorial <../tutorials/packages/sphinx-pydantic>`
- `Pydantic Documentation <https://docs.pydantic.dev/>`_
- :ref:`Package API Documentation <pdoc-sphinx-pydantic>`
Next Steps
----------
- Explore the :doc:`tutorial <../tutorials/packages/sphinx-pydantic>`
- Check the official documentation
- Try the examples in your own projects
- Customize for your specific needs

