Sphinx-Autodoc-Annotation Tutorial
===================================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-autodoc-annotation/>`_
   - `Manual <https://github.com/hsoft/sphinx-autodoc-annotation>`_
   - :doc:`Working Example <../../examples/sphinx-autodoc-annotation-example>`


.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinx-autodoc-annotation to display Python type annotations in your API documentation.

What is Sphinx-Autodoc-Annotation?
-----------------------------------
sphinx-autodoc-annotation is a Sphinx extension that enhances autodoc to:

- Display type annotations from function signatures
- Show return type annotations
- Format type hints nicely
- Support complex typing constructs
- Handle generic types
- Show Optional, Union, List types
- Display custom type aliases
- Format typing.Literal values
- Support Python 3.10+ syntax

This makes API documentation clearer by showing exact type information from annotations.

The sphinx-autodoc-annotation extension improves how Python type annotations are displayed in Sphinx documentation.


Installation
------------

sphinx-autodoc-annotation is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinx_autodoc_annotation; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx.ext.autodoc',
       'sphinx.ext.napoleon',
       'sphinx_autodoc_annotation',
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = [
       'sphinx.ext.autodoc',
       'sphinx.ext.napoleon',
       'sphinx_autodoc_annotation',
   ]
   
   # Annotation configuration
   autodoc_annotation_display = 'signature'  # signature, description, both
   autodoc_annotation_format = 'short'  # short, long, full
   autodoc_annotation_show_optional = True
   autodoc_annotation_show_none = True
   
   # Type formatting
   autodoc_annotation_simplify_types = True
   autodoc_annotation_use_aliases = True
   autodoc_annotation_max_length = 100
   
   # Display options
   autodoc_typehints = 'description'  # signature, description, none, both
   autodoc_typehints_description_target = 'all'  # all, documented, documented_params
   autodoc_typehints_format = 'short'


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Basic Setup
~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx.ext.autodoc',
       'sphinx_autodoc_annotation',
   ]

Options
~~~~~~~

.. code-block:: python

   autodoc_annotation_format = 'short'  # or 'long', 'full'
   autodoc_typehints = 'description'  # or 'signature', 'both'

Basic Usage
-----------

Simple Function with Annotations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``mylib/math_ops.py``:

.. code-block:: python

   """Mathematical operations."""
   
   def add(a: int, b: int) -> int:
       """
       Add two numbers.
       
       :param a: First number
       :param b: Second number
       :return: Sum of a and b
       """
       return a + b
   
   
   def divide(a: float, b: float) -> float:
       """
       Divide two numbers.
       
       :param a: Numerator
       :param b: Denominator
       :return: Result of division
       :raises ZeroDivisionError: If b is zero
       """
       return a / b

Document:

.. code-block:: rst

   .. automodule:: mylib.math_ops
      :members:

Complex Type Annotations
~~~~~~~~~~~~~~~~~~~~~~~~~

``mylib/data_processor.py``:

.. code-block:: python

   """Data processing with complex types."""
   from typing import List, Dict, Optional, Union, Tuple
   
   def process_items(
       items: List[str],
       config: Dict[str, Union[int, str]],
       default: Optional[str] = None
   ) -> Tuple[List[str], int]:
       """
       Process list of items.
       
       :param items: Items to process
       :param config: Configuration dictionary
       :param default: Default value
       :return: Processed items and count
       """
       processed = [item.upper() for item in items]
       return processed, len(processed)

Document:

.. code-block:: rst

   .. autofunction:: mylib.data_processor.process_items

   Data Pipeline
   =============
   
   Generic data processing pipeline with full type safety.
   
   .. autoclass:: mylib.pipeline.Pipeline
      :members:
      :special-members: __init__
   
   Utility Functions
   -----------------
   
   .. autofunction:: mylib.pipeline.filter_items
   
   .. autofunction:: mylib.pipeline.map_items
   
   Protocols
   ---------
   
   .. autoclass:: mylib.pipeline.Processor
      :members:

Example 3: Configuration System
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``mylib/config.py``:

.. code-block:: python

   """Configuration system with type annotations."""
   from typing import TypedDict, NotRequired, Literal, Union
   from pathlib import Path
   from enum import Enum
   
   
   class LogLevel(Enum):
       """Logging levels."""
       DEBUG = "debug"
       INFO = "info"
       WARNING = "warning"
       ERROR = "error"
   
   
   class DatabaseConfig(TypedDict):
       """Database configuration."""
       host: str
       port: int
       database: str
       username: str
       password: NotRequired[str]
       ssl: NotRequired[bool]
   
   
   class AppConfig(TypedDict):
       """Application configuration."""
       name: str
       version: str
       debug: bool
       log_level: LogLevel
       database: DatabaseConfig
       cache_dir: NotRequired[Path]
   
   
   def load_config(
       path: Union[str, Path],
       env: Literal["development", "staging", "production"] = "development"
   ) -> AppConfig:
       """
       Load configuration from file.
       
       :param path: Path to config file
       :param env: Environment name
       :return: Application configuration
       :raises FileNotFoundError: If config file not found
       """
       return {
           'name': 'MyApp',
           'version': '1.0.0',
           'debug': env == 'development',
           'log_level': LogLevel.INFO,
           'database': {
               'host': 'localhost',
               'port': 5432,
               'database': 'myapp',
               'username': 'user',
           }
       }
   
   
   def validate_config(config: AppConfig) -> bool:
       """
       Validate configuration.
       
       :param config: Configuration to validate
       :return: True if valid
       :raises ValueError: If configuration is invalid
       """
       if not config.get('name'):
           raise ValueError("Name is required")
       return True

Advanced Features
-----------------

Python 3.10+ Union Syntax
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   def process(data: str | int | None) -> dict[str, list[int]]:
       """Process data with modern union syntax."""
       return {}

Literal Types
~~~~~~~~~~~~~

.. code-block:: python

   from typing import Literal
   
   def set_mode(mode: Literal["read", "write", "append"]) -> None:
       """Set file mode."""
       pass

Type Aliases
~~~~~~~~~~~~

.. code-block:: python

   from typing import TypeAlias
   
   UserId: TypeAlias = int
   UserName: TypeAlias = str
   
   def get_user(user_id: UserId) -> UserName:
       """Get username by ID."""
       return "John"

Generic Classes
~~~~~~~~~~~~~~~

.. code-block:: python

   from typing import Generic, TypeVar
   
   T = TypeVar('T')
   
   class Container(Generic[T]):
       """Generic container."""
       
       def __init__(self, value: T) -> None:
           self.value = value
       
       def get(self) -> T:
           return self.value

Callable Types
~~~~~~~~~~~~~~

.. code-block:: python

   from typing import Callable
   
   def execute(
       func: Callable[[int, int], int],
       a: int,
       b: int
   ) -> int:
       """Execute function with arguments."""
       return func(a, b)

Docker Integration
------------------

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

   name: Build Typed Documentation
   
   on:
     push:
       paths:
         - '**/*.py'
         - 'docs/**'
   
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Type Check
           run: |
             docker run --rm -v $(pwd):/project \
               kensai-sphinx:latest \
               mypy /project/mylib
         
         - name: Build Documentation
           run: |
             docker run --rm -v $(pwd):/project \
               kensai-sphinx:latest \
               sphinx-build -b html /project/docs /project/docs/_build/html

Best Practices
--------------

1. **Use Type Hints Everywhere**
   
   Annotate all functions:
   
   .. code-block:: python
   
      def func(name: str, count: int) -> str:
          return name * count

2. **Import from typing**
   
   Use proper typing imports:
   
   .. code-block:: python
   
      from typing import List, Dict, Optional

3. **Use TypedDict for Dicts**
   
   Define structure for dictionaries

4. **Document Complex Types**
   
   Explain what complex types represent

5. **Keep Types Simple**
   
   Avoid overly complex nested types

6. **Use Type Aliases**
   
   Create aliases for complex types

Troubleshooting
---------------

Types Not Showing
~~~~~~~~~~~~~~~~~

**Solution:**

Check configuration:

.. code-block:: python

   autodoc_typehints = 'description'
   extensions = ['sphinx_autodoc_annotation']

Import Errors
~~~~~~~~~~~~~

**Solution:**

Ensure typing imports are available:

.. code-block:: python

   from typing import List, Dict, Optional

Long Type Names
~~~~~~~~~~~~~~~

**Solution:**

Use short format:

.. code-block:: python

   autodoc_annotation_format = 'short'

Next Steps
----------

1. Add type annotations to your code
2. Configure autodoc to show types
3. Build and review documentation
4. Use mypy for type checking
5. Keep annotations up to date

Additional Resources
--------------------

- :doc:`sphinx-autodoc-defaultargs` - Show default values
- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `Python typing module <https://docs.python.org/3/library/typing.html>`_
- `MyPy <https://mypy.readthedocs.io/>`_
