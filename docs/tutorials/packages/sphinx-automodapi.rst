Sphinx-Automodapi Tutorial
==========================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-automodapi/>`_
   - `API Documentation <../../pdoc/sphinx_automodapi/index.html>`_
   - `Manual <https://sphinx-automodapi.readthedocs.io/en/latest/>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

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


The sphinx-automodapi extension simplifies documenting entire modules by automatically generating API documentation for all classes, functions, and submodules.

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


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Basic Setup
~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx.ext.autodoc',
       'sphinx_automodapi.automodapi',
   ]

Options
~~~~~~~

.. code-block:: python

   automodapi_toctreedirnm = 'api'
   automodapi_writereprocessed = False

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


Practical Examples
------------------

Basic Usage
-----------

Simple Module
~~~~~~~~~~~~~

.. code-block:: rst

   .. automodapi:: mypackage.mymodule

This automatically documents all public classes and functions in the module.

With Options
~~~~~~~~~~~~

.. code-block:: rst

   .. automodapi:: mypackage.core
      :no-inheritance-diagram:
      :skip: internal_function

Examples
--------

Full Package
~~~~~~~~~~~~

.. code-block:: rst

   .. automodapi:: mypackage
      :no-main-docstring:
      :headings: ^=

Filtered Documentation
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. automodapi:: mypackage.utils
      :allowed-package-names: mypackage
      :skip: _internal_helper

Example 1: Data Processing Package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``sphinx_automodapi_mylib/__init__.py``:

.. literalinclude:: sphinx_automodapi_mylib/__init__.py
   :language: python

``sphinx_automodapi_mylib/readers.py``:

.. literalinclude:: sphinx_automodapi_mylib/readers.py
   :language: python

``mylib/processors.py``:

.. literalinclude:: sphinx_automodapi_mylib/processors.py
   :language: python

``sphinx_automodapi_mylib/writers.py``:

.. literalinclude:: sphinx_automodapi_mylib/writers.py
   :language: python

``sphinx_automodapi_mylib/api.rst``:

.. literalinclude:: sphinx_automodapi_mylib/api.rst
   :language: rst

**Generated Output:**

View the actual generated API documentation: :doc:`sphinx_automodapi_mylib/api`

.. toctree::
   :maxdepth: 1

   sphinx_automodapi_mylib/api
   ../../api/index

The automodapi directives in the file above automatically generate:

- Complete class documentation for all public classes (BaseReader, CSVReader, JSONReader, XMLReader, DataProcessor, FilterProcessor, TransformProcessor, BaseWriter, CSVWriter, JSONWriter, XMLWriter)
- Method documentation with parameters, return types, and examples  
- Inheritance diagrams showing class hierarchies (e.g., BaseReader → CSVReader, JSONReader, XMLReader)
- Cross-references between related classes and functions
- Organized sections for each module with proper headings

**Explanation:**

As you can see above, the automodapi directive automatically generated:

- Complete class documentation for all public classes
- Method signatures with parameters and return types
- Inheritance diagrams (unless disabled with ``:no-inheritance-diagram:``)
- Cross-references between related classes and functions
- Organized sections for each module with proper headings


Practical Examples
------------------

Basic Usage
-----------

Simple Module
~~~~~~~~~~~~~

.. code-block:: rst

   .. automodapi:: mypackage.mymodule

This automatically documents all public classes and functions in the module.

With Options
~~~~~~~~~~~~

.. code-block:: rst

   .. automodapi:: mypackage.core
      :no-inheritance-diagram:
      :skip: internal_function

Examples
--------

Full Package
~~~~~~~~~~~~

.. code-block:: rst

   .. automodapi:: mypackage
      :no-main-docstring:
      :headings: ^=

Filtered Documentation
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. automodapi:: mypackage.utils
      :allowed-package-names: mypackage
      :skip: _internal_helper

Example 1: Data Processing Package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``sphinx_automodapi_mylib/__init__.py``:

.. literalinclude:: sphinx_automodapi_mylib/__init__.py
   :language: python

``sphinx_automodapi_mylib/readers.py``:

.. literalinclude:: sphinx_automodapi_mylib/readers.py
   :language: python

``mylib/processors.py``:

.. literalinclude:: sphinx_automodapi_mylib/processors.py
   :language: python

``sphinx_automodapi_mylib/writers.py``:

.. literalinclude:: sphinx_automodapi_mylib/writers.py
   :language: python

``sphinx_automodapi_mylib/api.rst``:

.. literalinclude:: sphinx_automodapi_mylib/api.rst
   :language: rst

**Generated Output:**

View the actual generated API documentation: :doc:`sphinx_automodapi_mylib/api`

The automodapi directives in the file above automatically generate:

- Complete class documentation for all public classes (BaseReader, CSVReader, JSONReader, XMLReader, DataProcessor, FilterProcessor, TransformProcessor, BaseWriter, CSVWriter, JSONWriter, XMLWriter)
- Method documentation with parameters, return types, and examples  
- Inheritance diagrams showing class hierarchies (e.g., BaseReader → CSVReader, JSONReader, XMLReader)
- Cross-references between related classes and functions
- Organized sections for each module with proper headings

**Explanation:**

As you can see above, the automodapi directive automatically generated:

- Complete class documentation for all public classes
- Method signatures with parameters and return types
- Inheritance diagrams (unless disabled with ``:no-inheritance-diagram:``)
- Cross-references between related classes and functions
- Organized sections for each module with proper headings


Practical Examples
------------------

Basic Usage
-----------

Simple Module
~~~~~~~~~~~~~

.. code-block:: rst

   .. automodapi:: mypackage.mymodule

This automatically documents all public classes and functions in the module.

With Options
~~~~~~~~~~~~

.. code-block:: rst

   .. automodapi:: mypackage.core
      :no-inheritance-diagram:
      :skip: internal_function

Examples
--------

Full Package
~~~~~~~~~~~~

.. code-block:: rst

   .. automodapi:: mypackage
      :no-main-docstring:
      :headings: ^=

Filtered Documentation
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. automodapi:: mypackage.utils
      :allowed-package-names: mypackage
      :skip: _internal_helper

Example 1: Data Processing Package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``sphinx_automodapi_mylib/__init__.py``:

.. literalinclude:: sphinx_automodapi_mylib/__init__.py
   :language: python

``sphinx_automodapi_mylib/readers.py``:

.. literalinclude:: sphinx_automodapi_mylib/readers.py
   :language: python

``mylib/processors.py``:

.. literalinclude:: sphinx_automodapi_mylib/processors.py
   :language: python

``sphinx_automodapi_mylib/writers.py``:

.. literalinclude:: sphinx_automodapi_mylib/writers.py
   :language: python

``sphinx_automodapi_mylib/api.rst``:

.. literalinclude:: sphinx_automodapi_mylib/api.rst
   :language: rst

**Generated Output:**

View the actual generated API documentation: :doc:`sphinx_automodapi_mylib/api`

The automodapi directives in the file above automatically generate:

- Complete class documentation for all public classes (BaseReader, CSVReader, JSONReader, XMLReader, DataProcessor, FilterProcessor, TransformProcessor, BaseWriter, CSVWriter, JSONWriter, XMLWriter)
- Method documentation with parameters, return types, and examples  
- Inheritance diagrams showing class hierarchies (e.g., BaseReader → CSVReader, JSONReader, XMLReader)
- Cross-references between related classes and functions
- Organized sections for each module with proper headings

**Explanation:**

As you can see above, the automodapi directive automatically generated:

- Complete class documentation for all public classes
- Method signatures with parameters and return types
- Inheritance diagrams (unless disabled with ``:no-inheritance-diagram:``)
- Cross-references between related classes and functions
- Organized sections for each module with proper headings

Additional Resources
--------------------
- :doc:`sphinx-autodoc-annotation` - Type annotations
- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `Automodapi Documentation <https://sphinx-automodapi.readthedocs.io/>`_
- `Astropy <https://www.astropy.org/>`_
- :doc:`../tutorials/packages/sphinx-automodapi` - Complete tutorial
- GitHub repository: https://github.com/astropy/sphinx-automodapi

