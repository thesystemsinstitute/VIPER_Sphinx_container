Sphinx-Automodapi Tutorial
==========================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-automodapi/>`_
   - :doc:`See Working Example <../../examples/sphinx-automodapi-example>`
   - `Official Documentation <https://sphinx-automodapi.readthedocs.io/>`_


This tutorial demonstrates how to use sphinx-automodapi to automatically generate API documentation for Python packages and modules.

What is Sphinx-Automodapi?
---------------------------

sphinx-automodapi is a Sphinx extension developed by the Astropy project that provides:

- Automatic API documentation generation
- Module-level documentation
- Submodule organization
- Automatic inheritance diagrams
- Smart cross-referencing
- Flexible customization
- Clean documentation layout
- Section organization
- Module index generation
- Compatible with autodoc

Originally created for astronomical Python packages, it's useful for any Python project with multiple modules.

Installation
------------

sphinx-automodapi is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinx_automodapi; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx.ext.autodoc',
       'sphinx.ext.napoleon',
       'sphinx_automodapi.automodapi',
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = [
       'sphinx.ext.autodoc',
       'sphinx.ext.napoleon',
       'sphinx.ext.intersphinx',
       'sphinx_automodapi.automodapi',
       'sphinx_automodapi.smart_resolver',
   ]
   
   # Automodapi configuration
   automodapi_toctreedirnm = 'api'
   automodapi_writereprocessed = False
   automodapi_inheritance_diagram = True
   
   # Don't prepend module names
   add_module_names = False
   
   # Autodoc options
   autodoc_default_options = {
       'members': True,
       'undoc-members': True,
       'show-inheritance': True,
       'inherited-members': True,
   }
   
   # Napoleon settings for Google/NumPy docstrings
   napoleon_google_docstring = True
   napoleon_numpy_docstring = True
   napoleon_include_init_with_doc = True

Basic Usage
-----------

Document Complete Module
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. automodapi:: mylib
      :no-inheritance-diagram:

Include Inheritance Diagrams
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. automodapi:: mylib.models
      :inheritance-diagram:

Exclude Submodules
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. automodapi:: mylib
      :no-inheritance-diagram:
      :skip: mylib.internal

Practical Examples
------------------

Example 1: Data Processing Package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``mylib/__init__.py``:

.. code-block:: python

   """Data processing library."""
   
   __version__ = '1.0.0'
   
   from .readers import CSVReader, JSONReader, XMLReader
   from .processors import DataProcessor, FilterProcessor, TransformProcessor
   from .writers import CSVWriter, JSONWriter, XMLWriter
   
   __all__ = [
       'CSVReader', 'JSONReader', 'XMLReader',
       'DataProcessor', 'FilterProcessor', 'TransformProcessor',
       'CSVWriter', 'JSONWriter', 'XMLWriter',
   ]

``mylib/readers.py``:

.. code-block:: python

   """Data readers for various formats."""
   
   from abc import ABC, abstractmethod
   from typing import Any, Dict, List
   import csv
   import json
   import xml.etree.ElementTree as ET
   
   class BaseReader(ABC):
       """
       Base class for data readers.
       
       All readers should inherit from this class and implement
       the read method.
       """
       
       @abstractmethod
       def read(self, filepath: str) -> List[Dict[str, Any]]:
           """
           Read data from file.
           
           Parameters
           ----------
           filepath : str
               Path to the file to read
           
           Returns
           -------
           List[Dict[str, Any]]
               List of dictionaries containing the data
           """
           pass
   
   class CSVReader(BaseReader):
       """
       CSV file reader.
       
       Parameters
       ----------
       delimiter : str, optional
           Field delimiter (default: ',')
       quotechar : str, optional
           Quote character (default: '"')
       
       Examples
       --------
       >>> reader = CSVReader()
       >>> data = reader.read('data.csv')
       """
       
       def __init__(self, delimiter: str = ',', quotechar: str = '"'):
           self.delimiter = delimiter
           self.quotechar = quotechar
       
       def read(self, filepath: str) -> List[Dict[str, Any]]:
           """Read CSV file."""
           with open(filepath, 'r') as f:
               reader = csv.DictReader(
                   f,
                   delimiter=self.delimiter,
                   quotechar=self.quotechar
               )
               return list(reader)
   
   class JSONReader(BaseReader):
       """
       JSON file reader.
       
       Examples
       --------
       >>> reader = JSONReader()
       >>> data = reader.read('data.json')
       """
       
       def read(self, filepath: str) -> List[Dict[str, Any]]:
           """Read JSON file."""
           with open(filepath, 'r') as f:
               data = json.load(f)
               if isinstance(data, list):
                   return data
               return [data]

``mylib/processors.py``:

.. code-block:: python

   """Data processors."""
   
   from typing import Any, Callable, Dict, List
   
   class DataProcessor:
       """
       Generic data processor.
       
       Parameters
       ----------
       transformations : List[Callable], optional
           List of transformation functions to apply
       
       Examples
       --------
       >>> processor = DataProcessor()
       >>> result = processor.process(data)
       """
       
       def __init__(self, transformations: List[Callable] = None):
           self.transformations = transformations or []
       
       def process(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
           """
           Process data through all transformations.
           
           Parameters
           ----------
           data : List[Dict[str, Any]]
               Input data
           
           Returns
           -------
           List[Dict[str, Any]]
               Processed data
           """
           result = data
           for transform in self.transformations:
               result = [transform(item) for item in result]
           return result

``mylib/writers.py``:

.. code-block:: python

   """Data writers."""
   
   from abc import ABC, abstractmethod
   from typing import Any, Dict, List
   import csv
   import json
   
   class BaseWriter(ABC):
       """Base class for data writers."""
       
       @abstractmethod
       def write(self, data: List[Dict[str, Any]], filepath: str) -> None:
           """Write data to file."""
           pass
   
   class CSVWriter(BaseWriter):
       """CSV file writer."""
       
       def write(self, data: List[Dict[str, Any]], filepath: str) -> None:
           """Write data to CSV file."""
           if not data:
               return
           
           with open(filepath, 'w', newline='') as f:
               writer = csv.DictWriter(f, fieldnames=data[0].keys())
               writer.writeheader()
               writer.writerows(data)
   
   class JSONWriter(BaseWriter):
       """JSON file writer."""
       
       def write(self, data: List[Dict[str, Any]], filepath: str) -> None:
           """Write data to JSON file."""
           with open(filepath, 'w') as f:
               json.dump(data, f, indent=2)

``docs/api.rst``:

.. code-block:: rst

   API Reference
   =============
   
   This section provides detailed API documentation for the mylib package.
   
   Main Package
   ------------
   
   .. automodapi:: mylib
      :no-inheritance-diagram:
   
   Data Readers
   ------------
   
   .. automodapi:: mylib.readers
      :inheritance-diagram:
   
   Data Processors
   ---------------
   
   .. automodapi:: mylib.processors
   
   Data Writers
   ------------
   
   .. automodapi:: mylib.writers
      :inheritance-diagram:

Example 2: Web Application Package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``webapp/__init__.py``:

.. code-block:: python

   """Web application package."""
   
   from .app import create_app
   from .config import Config
   from .models import User, Post, Comment
   from .views import index, profile, post_detail
   
   __all__ = ['create_app', 'Config', 'User', 'Post', 'Comment']

``webapp/models.py``:

.. code-block:: python

   """Database models."""
   
   from datetime import datetime
   from typing import Optional
   
   class BaseModel:
       """
       Base model class.
       
       Attributes
       ----------
       id : int
           Primary key
       created_at : datetime
           Creation timestamp
       updated_at : datetime
           Last update timestamp
       """
       
       def __init__(self):
           self.id: Optional[int] = None
           self.created_at = datetime.utcnow()
           self.updated_at = datetime.utcnow()
       
       def save(self):
           """Save model to database."""
           self.updated_at = datetime.utcnow()
   
   class User(BaseModel):
       """
       User model.
       
       Parameters
       ----------
       username : str
           Username (unique)
       email : str
           Email address
       
       Attributes
       ----------
       username : str
           Username
       email : str
           Email address
       is_active : bool
           Whether user is active
       """
       
       def __init__(self, username: str, email: str):
           super().__init__()
           self.username = username
           self.email = email
           self.is_active = True
   
   class Post(BaseModel):
       """
       Blog post model.
       
       Parameters
       ----------
       title : str
           Post title
       content : str
           Post content
       author : User
           Post author
       """
       
       def __init__(self, title: str, content: str, author: User):
           super().__init__()
           self.title = title
           self.content = content
           self.author = author
           self.published = False

``docs/api/models.rst``:

.. code-block:: rst

   Data Models
   ===========
   
   .. automodapi:: webapp.models
      :inheritance-diagram:
      :headings: -~
   
   The inheritance diagram shows the relationships between model classes.

Example 3: Scientific Computing Library
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``scilib/__init__.py``:

.. code-block:: python

   """Scientific computing library."""
   
   from .stats import mean, median, stddev, correlation
   from .linalg import dot, cross, norm, solve
   from .integrate import trapz, simps, quad
   
   __all__ = [
       'mean', 'median', 'stddev', 'correlation',
       'dot', 'cross', 'norm', 'solve',
       'trapz', 'simps', 'quad',
   ]

``docs/api/complete.rst``:

.. code-block:: rst

   Complete API Reference
   ======================
   
   Statistics Module
   -----------------
   
   .. automodapi:: scilib.stats
      :no-inheritance-diagram:
      :headings: ^~
   
   Linear Algebra Module
   ---------------------
   
   .. automodapi:: scilib.linalg
      :no-inheritance-diagram:
      :headings: ^~
   
   Integration Module
   ------------------
   
   .. automodapi:: scilib.integrate
      :no-inheritance-diagram:
      :headings: ^~

Advanced Features
-----------------

Custom Headings
~~~~~~~~~~~~~~~

.. code-block:: rst

   .. automodapi:: mylib
      :headings: -~
      :no-inheritance-diagram:

Skip Specific Items
~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. automodapi:: mylib
      :skip: _internal_function, DeprecatedClass

Include Private Members
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. automodapi:: mylib
      :private-members:

Custom Sections
~~~~~~~~~~~~~~~

.. code-block:: rst

   .. automodapi:: mylib
      :no-inheritance-diagram:
      :allowed-package-names: mylib.core, mylib.utils

Docker Integration
------------------

Build Documentation
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     kensai-sphinx:latest \
     sphinx-build -b html /project/docs /project/docs/_build/html

Generate API Stub Files
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     kensai-sphinx:latest \
     sphinx-apidoc -o /project/docs/api /project/mylib

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
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Build Documentation
           run: |
             docker run --rm -v $(pwd):/project \
               kensai-sphinx:latest \
               sphinx-build -b html /project/docs /project/docs/_build/html
         
         - name: Deploy to GitHub Pages
           uses: peaceiris/actions-gh-pages@v3
           with:
             github_token: ${{ secrets.GITHUB_TOKEN }}
             publish_dir: ./docs/_build/html

Best Practices
--------------

1. **Use Meaningful Module Names**
   
   Organize code logically

2. **Write Comprehensive Docstrings**
   
   Document all public APIs

3. **Maintain __all__**
   
   Control what's exported

4. **Use Inheritance Diagrams**
   
   Show class relationships

5. **Organize by Feature**
   
   Group related modules

6. **Keep Imports Clean**
   
   Expose main APIs at package level

Troubleshooting
---------------

Module Not Found
~~~~~~~~~~~~~~~~

**Solution:**

Ensure module is in Python path:

.. code-block:: python

   import sys
   import os
   sys.path.insert(0, os.path.abspath('..'))

Inheritance Diagram Missing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Solution:**

Install graphviz:

.. code-block:: bash

   docker exec -it sphinx-container apk add graphviz

Circular Import Error
~~~~~~~~~~~~~~~~~~~~~

**Solution:**

Use lazy imports or reorganize code

Duplicate Documentation
~~~~~~~~~~~~~~~~~~~~~~~

**Solution:**

Use ``:no-inheritance-diagram:`` to reduce clutter

Next Steps
----------

1. Structure your package with clear modules
2. Add automodapi directives
3. Enable inheritance diagrams
4. Organize API documentation
5. Customize heading levels

Additional Resources
--------------------

- :doc:`sphinx-autodoc-annotation` - Type annotations
- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `Automodapi Documentation <https://sphinx-automodapi.readthedocs.io/>`_
- `Astropy <https://www.astropy.org/>`_
