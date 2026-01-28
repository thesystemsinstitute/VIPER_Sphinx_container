Sphinx-Autodoc2-Fern Tutorial
=============================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-autodoc2-fern/>`_
   - `API Documentation <../../pdoc/sphinx_autodoc2_fern/index.html>`_
   - `Manual <https://github.com/fern-api/sphinx-autodoc2-fern>`_
   - :doc:`Working Example <../../examples/sphinx-autodoc2-fern-example>`


.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinx-autodoc2-fern, an enhanced autodoc alternative with better performance and features.

What is Sphinx-Autodoc2-Fern?
------------------------------

sphinx-autodoc2-fern is a next-generation autodoc extension that provides:

- Faster documentation generation
- Better Python parsing
- Improved type annotation support
- Cleaner output format
- Advanced filtering options
- Better import handling
- Asynchronous code support
- Dataclass documentation
- Protocol and TypedDict support
- Modern Python feature support

This is a modern alternative to sphinx.ext.autodoc with enhanced capabilities for current Python versions.


The sphinx-autodoc2-fern extension provides modern, Fern-inspired API documentation layouts with enhanced navigation and presentation.

Installation
------------

sphinx-autodoc2-fern is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinx_autodoc2_fern; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_autodoc2_fern',
   ]
   
   # Configure package to document
   autodoc2_packages = [
       'mylib',
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinx_autodoc2_fern']
   
   # Packages to document
   autodoc2_packages = [
       {
           'path': 'mylib',
           'auto_mode': True,
       },
       {
           'path': 'myapp',
           'exclude_dirs': ['tests', 'migrations'],
       }
   ]
   
   # Output configuration
   autodoc2_output_dir = 'api'
   autodoc2_index_template = None
   autodoc2_render_plugin = 'myst'
   
   # Rendering options
   autodoc2_sort_names = True
   autodoc2_class_docstring = 'both'  # merge, both, init, class
   autodoc2_module_all_regexes = [r'\..*']
   
   # Documentation control
   autodoc2_hidden_objects = ['private', 'inherited']
   autodoc2_skip_module_regexes = [r'.*\.tests\..*']
   autodoc2_docstring_parser = 'sphinx'  # sphinx, google, numpy


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Basic Setup
~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_autodoc2_fern',
   ]
   
   autodoc2_fern_layout = 'modern'

Options
~~~~~~~

.. code-block:: python

   autodoc2_fern_options = {
       'sidebar_navigation': True,
       'code_examples': True,
       'response_samples': True,
   }

Basic Usage
-----------

Auto-Generate API Docs
~~~~~~~~~~~~~~~~~~~~~~

Simply configure packages and build:

.. code-block:: python

   # conf.py
   autodoc2_packages = ['mylib']

This automatically generates API documentation for all public modules.

Manual Module Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. autodoc2-object:: mylib.utils.format_string
      :noindex:

Document Specific Class
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. autodoc2-object:: mylib.models.User
      :members:
      :exclude-members: _internal_method

   MyLib Documentation
   ===================
   
   Welcome to MyLib documentation.
   
   .. toctree::
      :maxdepth: 2
      :caption: Contents:
      
      quickstart
      user_guide
      api/index
   
   Quick Example
   -------------
   
   .. code-block:: python
      
      from mylib import Client
      
      async def main():
          client = Client(api_key="your-key")
          user = await client.get_user(123)
          print(user.name)

Example 2: Protocol and TypedDict Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``mylib/protocols.py``:

.. code-block:: python

   """Protocol definitions."""
   from typing import Protocol, TypedDict, runtime_checkable
   
   class ConfigDict(TypedDict):
       """Configuration dictionary structure."""
       host: str
       port: int
       debug: bool
       timeout: int
   
   @runtime_checkable
   class Serializable(Protocol):
       """Protocol for serializable objects."""
       
       def to_dict(self) -> dict:
           """Convert to dictionary."""
           ...
       
       @classmethod
       def from_dict(cls, data: dict) -> 'Serializable':
           """Create from dictionary."""
           ...
   
   @runtime_checkable
   class Cacheable(Protocol):
       """Protocol for cacheable objects."""
       
       def cache_key(self) -> str:
           """Generate cache key."""
           ...
       
       def cache_ttl(self) -> int:
           """Get cache TTL in seconds."""
           ...

``docs/api/protocols.rst``:

.. code-block:: rst

   Protocols
   =========
   
   .. autodoc2-summary::
      :module: mylib.protocols
   
   Type Definitions
   ----------------
   
   .. autodoc2-object:: mylib.protocols.ConfigDict
   
   Protocols
   ---------
   
   .. autodoc2-object:: mylib.protocols.Serializable
      :members:
   
   .. autodoc2-object:: mylib.protocols.Cacheable
      :members:

Example 3: Advanced Type Annotations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``mylib/advanced.py``:

.. code-block:: python

   """Advanced type annotations."""
   from typing import (
       TypeVar, Generic, Protocol, Callable,
       ParamSpec, TypeAlias, Literal
   )
   from collections.abc import Sequence, Mapping
   
   T = TypeVar('T')
   P = ParamSpec('P')
   
   JsonValue: TypeAlias = (
       str | int | float | bool | None |
       dict[str, 'JsonValue'] |
       list['JsonValue']
   )
   
   class Storage(Generic[T]):
       """Generic storage container."""
       
       def __init__(self) -> None:
           """Initialize storage."""
           self._items: list[T] = []
       
       def add(self, item: T) -> None:
           """Add item to storage."""
           self._items.append(item)
       
       def get_all(self) -> Sequence[T]:
           """Get all items."""
           return self._items
       
       def filter(
           self,
           predicate: Callable[[T], bool]
       ) -> list[T]:
           """Filter items by predicate."""
           return [item for item in self._items if predicate(item)]
   
   def retry(
       max_attempts: int = 3
   ) -> Callable[[Callable[P, T]], Callable[P, T]]:
       """Retry decorator."""
       def decorator(func: Callable[P, T]) -> Callable[P, T]:
           def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
               for attempt in range(max_attempts):
                   try:
                       return func(*args, **kwargs)
                   except Exception:
                       if attempt == max_attempts - 1:
                           raise
               raise RuntimeError("Unreachable")
           return wrapper
       return decorator
   
   def process_json(
       data: JsonValue,
       mode: Literal["strict", "lenient"] = "strict"
   ) -> Mapping[str, JsonValue]:
       """Process JSON data."""
       return {}

Advanced Features
-----------------

Custom Rendering
~~~~~~~~~~~~~~~~

.. code-block:: python

   # Use MyST for markdown-style output
   autodoc2_render_plugin = 'myst'
   
   # Use custom template
   autodoc2_index_template = 'custom_template.rst.jinja2'

Filtering Objects
~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Hide private and inherited members
   autodoc2_hidden_objects = ['private', 'inherited', 'dunder']
   
   # Skip test modules
   autodoc2_skip_module_regexes = [
       r'.*\.tests\..*',
       r'.*\.conftest',
   ]

Docstring Parsers
~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Use Google-style docstrings
   autodoc2_docstring_parser = 'google'
   
   # Or NumPy style
   autodoc2_docstring_parser = 'numpy'

Class Docstring Handling
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Merge class and __init__ docstrings
   autodoc2_class_docstring = 'merge'
   
   # Show both separately
   autodoc2_class_docstring = 'both'

Module Summaries
~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. autodoc2-summary::
      :module: mylib.core
      :recursive:

Docker Integration
------------------

Generate API Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     kensai-sphinx:latest \
     sphinx-build -b html /project/docs /project/docs/_build/html

Update API Docs
~~~~~~~~~~~~~~~

.. code-block:: bash

   # Rebuild only if source changed
   docker run --rm \
     -v $(pwd):/project \
     kensai-sphinx:latest \
     sphinx-build -b html -a /project/docs /project/docs/_build/html

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Build API Documentation
   
   on:
     push:
       paths:
         - 'mylib/**/*.py'
         - 'docs/**'
   
   jobs:
     docs:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Generate API Documentation
           run: |
             docker run --rm -v $(pwd):/project \
               kensai-sphinx:latest \
               sphinx-build -b html /project/docs /project/docs/_build/html
         
         - name: Check for Changes
           run: |
             if [ -n "$(git status --porcelain docs/api)" ]; then
               echo "API docs changed"
               git diff docs/api
             fi

Best Practices
--------------

1. **Use Type Hints**
   
   Fully annotate your code

2. **Write Good Docstrings**
   
   Follow consistent style (Google, NumPy, Sphinx)

3. **Organize Modules**
   
   Clear module structure

4. **Use __all__**
   
   Control what gets documented

5. **Keep Docstrings Updated**
   
   Update docs when code changes

6. **Document Public API Only**
   
   Hide internal implementation

Troubleshooting
---------------

Package Not Found
~~~~~~~~~~~~~~~~~

**Solution:**

Check package path:

.. code-block:: python

   autodoc2_packages = [
       {
           'path': './mylib',  # Relative path
       }
   ]

No Documentation Generated
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Solution:**

Enable auto mode:

.. code-block:: python

   autodoc2_packages = [
       {
           'path': 'mylib',
           'auto_mode': True,
       }
   ]

Import Errors
~~~~~~~~~~~~~

**Solution:**

Add to Python path:

.. code-block:: python

   import sys
   import os
   sys.path.insert(0, os.path.abspath('.'))

Type Annotations Not Showing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Solution:**

Check rendering plugin:

.. code-block:: python

   autodoc2_render_plugin = 'myst'

Next Steps
----------

1. Configure autodoc2 for your package
2. Run Sphinx build
3. Review generated documentation
4. Customize rendering and filtering
5. Integrate into CI/CD

Additional Resources
--------------------

- :doc:`sphinx-autodoc-annotation` - Type annotation display
- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `Autodoc2 Documentation <https://sphinx-autodoc2.readthedocs.io/>`_
