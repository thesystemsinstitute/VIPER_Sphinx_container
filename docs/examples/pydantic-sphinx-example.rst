Pydantic Sphinx Example
=======================

.. note::

   **Package**: pydantic-sphinx  
   **Purpose**: Pydantic model documentation  
   **Tutorial**: See :doc:`../tutorials/packages/pydantic-sphinx` for complete tutorial

This page demonstrates **pydantic-sphinx** - Pydantic model documentation.

.. contents:: Contents
   :local:
   :depth: 3

Overview
--------

What is pydantic-sphinx?
------------------------

pydantic-sphinx provides:

- Pydantic model documentation
- Integration with Sphinx documentation
- Flexible configuration options
- Professional output formatting

Key Features
~~~~~~~~~~~~

- **Model Documentation**: Auto-document Pydantic models
- **JSON Schema**: Display JSON schema
- **Validators**: Document custom validators
- **Configuration**: Show model configuration

Installation
------------

Using pip
~~~~~~~~~

Install the extension:

.. code-block:: bash

   pip install pydantic-sphinx

Or add to your ``requirements.txt``:

.. code-block:: text

   pydantic-sphinx
   sphinx>=5.0.0
   pydantic>=1.0

Configuration
-------------

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'pydantic_sphinx',
       'sphinx.ext.autodoc',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

Complete configuration with all features:

.. code-block:: python

   extensions = ['pydantic_sphinx', 'sphinx.ext.autodoc']
   
   # Package-specific configuration
   autodoc_pydantic_model_show_json = True
   autodoc_pydantic_model_show_config = True
   autodoc_pydantic_model_show_validator_members = True
   autodoc_pydantic_settings_show_json = True
   autodoc_pydantic_field_list_validators = True

Basic Usage
-----------

Example 1: Simple Model
~~~~~~~~~~~~~~~~~~~~~~~

Create a Pydantic model:

.. code-block:: python

   # myapp/models.py
   from pydantic import BaseModel, Field
   
   class User(BaseModel):
       """User model."""
       
       id: int = Field(..., description="User ID")
       name: str = Field(..., description="User's full name")
       email: str = Field(..., description="Email address")
       age: int = Field(ge=0, le=150, description="User's age")
       is_active: bool = Field(default=True, description="Account status")

Document it:

.. code-block:: rst

   User Model
   ==========
   
   .. autopydantic_model:: myapp.models.User
      :members:
      :show-json:

Example 2: With Validators
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Model with validators:

.. code-block:: python

   from pydantic import BaseModel, Field, validator
   
   class Product(BaseModel):
       """Product model."""
       
       name: str = Field(..., description="Product name")
       price: float = Field(..., gt=0, description="Product price")
       quantity: int = Field(default=0, ge=0, description="Stock quantity")
       
       @validator('price')
       def price_must_be_positive(cls, v):
           """Ensure price is positive."""
           if v <= 0:
               raise ValueError('Price must be positive')
           return v

Document it:

.. code-block:: rst

   .. autopydantic_model:: myapp.models.Product
      :members:
      :show-validators:
      :show-json:

Real-World Examples
-------------------

Example: API Models
~~~~~~~~~~~~~~~~~~~

Document API request/response models:

.. code-block:: python

   # myapp/api/models.py
   from typing import Optional, List
   from pydantic import BaseModel, Field, HttpUrl
   from datetime import datetime
   
   class Address(BaseModel):
       """Address model."""
       
       street: str = Field(..., description="Street address")
       city: str = Field(..., description="City name")
       state: str = Field(..., min_length=2, max_length=2)
       zip_code: str = Field(..., regex=r'^\d{5}(-\d{4})?$')
   
   class UserProfile(BaseModel):
       """User profile model."""
       
       username: str = Field(..., min_length=3, max_length=50)
       email: str = Field(..., description="Email address")
       full_name: Optional[str] = None
       avatar_url: Optional[HttpUrl] = None
       bio: Optional[str] = Field(None, max_length=500)
       address: Optional[Address] = None
       created_at: datetime = Field(default_factory=datetime.now)
       
       class Config:
           json_encoders = {
               datetime: lambda v: v.isoformat()
           }
   
   class CreateUserRequest(BaseModel):
       """Request model for creating a user."""
       
       username: str = Field(..., min_length=3, max_length=50)
       email: str
       password: str = Field(..., min_length=8)
       full_name: Optional[str] = None
   
   class UserResponse(BaseModel):
       """Response model for user data."""
       
       id: int
       username: str
       email: str
       full_name: Optional[str]
       created_at: datetime

Documentation:

.. code-block:: rst

   API Models
   ==========
   
   User Models
   -----------
   
   .. autopydantic_model:: myapp.api.models.UserProfile
      :members:
      :show-json:
      :show-config:
   
   .. autopydantic_model:: myapp.api.models.CreateUserRequest
      :members:
      :show-json:
   
   .. autopydantic_model:: myapp.api.models.UserResponse
      :members:
      :show-json:
   
   Address Model
   -------------
   
   .. autopydantic_model:: myapp.api.models.Address
      :members:
      :show-json:

Example: Settings Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Document application settings:

.. code-block:: python

   # myapp/config.py
   from pydantic import BaseSettings, Field, PostgresDsn
   
   class Settings(BaseSettings):
       """Application settings."""
       
       app_name: str = Field("MyApp", description="Application name")
       debug: bool = Field(False, description="Debug mode")
       database_url: PostgresDsn = Field(..., description="Database connection URL")
       secret_key: str = Field(..., description="Secret key for encryption")
       max_connections: int = Field(100, ge=1, description="Max database connections")
       
       class Config:
           env_file = ".env"
           case_sensitive = True

Documentation:

.. code-block:: rst

   Configuration
   =============
   
   Application Settings
   --------------------
   
   .. autopydantic_settings:: myapp.config.Settings
      :members:
      :show-json:
      :show-config:
   
   Usage
   -----
   
   .. code-block:: python
   
      from myapp.config import Settings
      
      # Load from environment
      settings = Settings()
      
      # Load from .env file
      settings = Settings(_env_file='.env')

Example: Complex Models
~~~~~~~~~~~~~~~~~~~~~~~

Nested and complex models:

.. code-block:: python

   from typing import List, Dict, Union
   from pydantic import BaseModel, Field, validator
   from enum import Enum
   
   class TaskStatus(str, Enum):
       """Task status enumeration."""
       pending = "pending"
       in_progress = "in_progress"
       completed = "completed"
       failed = "failed"
   
   class Task(BaseModel):
       """Task model."""
       
       id: int
       title: str = Field(..., min_length=1, max_length=200)
       description: Optional[str] = None
       status: TaskStatus = Field(default=TaskStatus.pending)
       tags: List[str] = Field(default_factory=list)
       metadata: Dict[str, Union[str, int, float]] = Field(default_factory=dict)
       
       @validator('tags')
       def validate_tags(cls, v):
           """Ensure tags are unique."""
           if len(v) != len(set(v)):
               raise ValueError('Tags must be unique')
           return v
   
   class Project(BaseModel):
       """Project model."""
       
       id: int
       name: str = Field(..., min_length=1)
       tasks: List[Task] = Field(default_factory=list)
       
       @property
       def completed_tasks(self) -> List[Task]:
           """Get completed tasks."""
           return [t for t in self.tasks if t.status == TaskStatus.completed]

Documentation:

.. code-block:: rst

   Project Management Models
   =========================
   
   Task Model
   ----------
   
   .. autopydantic_model:: myapp.models.Task
      :members:
      :show-json:
      :show-validators:
   
   Project Model
   -------------
   
   .. autopydantic_model:: myapp.models.Project
      :members:
      :show-json:
      :show-validators:
   
   Task Status
   -----------
   
   .. autoclass:: myapp.models.TaskStatus
      :members:

Best Practices
--------------

Recommendations
~~~~~~~~~~~~~~~

- Add descriptions to all fields using Field()
- Document validators with docstrings
- Use type hints consistently
- Show JSON examples for API models
- Include model configuration

Common Patterns
~~~~~~~~~~~~~~~

Standard patterns for using pydantic-sphinx:

1. **API Models**: Document request/response models
2. **Settings**: Document configuration classes
3. **Validators**: Show custom validation logic

Integration Tips
----------------

Working with Other Extensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

pydantic-sphinx integrates well with:

- sphinx.ext.autodoc for general documentation
- sphinx-pydantic for alternative approach
- OpenAPI extensions for API docs

Additional Resources
--------------------

- :doc:`Complete Tutorial <../tutorials/packages/pydantic-sphinx>`
- `PyPI Package <https://pypi.org/project/pydantic-sphinx/>`_
- `Pydantic Documentation <https://docs.pydantic.dev/>`_
- :ref:`Package API Documentation <pdoc-pydantic-sphinx>`

Next Steps
----------

- Explore the :doc:`tutorial <../tutorials/packages/pydantic-sphinx>`
- Check the official documentation
- Try the examples in your own projects
- Customize for your specific needs
