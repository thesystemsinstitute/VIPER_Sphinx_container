Sphinx-Refdoc Tutorial
======================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-refdoc/>`_
   - `API Documentation <../../pdoc/sphinx_refdoc/index.html>`_
   - `Manual <https://github.com/sphinx-contrib/refdoc>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinx-refdoc to create and manage reference documentation with enhanced cross-referencing capabilities.

What is Sphinx-Refdoc?
-----------------------
sphinx-refdoc is a Sphinx extension that provides enhanced reference documentation features:

- Advanced cross-referencing between documents
- Automatic reference link generation
- Reference glossaries and indexes
- External reference management
- Reference validation and checking
- Smart reference resolution
- Reference documentation templates
- API reference organization

This is particularly useful for large documentation projects with complex cross-referencing needs.

The sphinx-refdoc extension provides advanced reference documentation features, including automatic reference generation, enhanced cross-referencing, and structured API documentation.


Installation
------------

sphinx-refdoc is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm viper-sphinx:latest python -c "import sphinx_refdoc; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_refdoc',
   ]
   
   # Basic configuration
   refdoc_enabled = True

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinx_refdoc']
   
   # Reference documentation settings
   refdoc_enabled = True
   refdoc_validate_refs = True
   refdoc_warn_broken = True
   
   # Cross-reference options
   refdoc_external_refs = {
       'python': ('https://docs.python.org/3/', None),
       'numpy': ('https://numpy.org/doc/stable/', None),
       'pandas': ('https://pandas.pydata.org/docs/', None),
   }
   
   # Reference templates
   refdoc_templates = {
       'api': 'templates/api_reference.rst',
       'class': 'templates/class_reference.rst',
       'function': 'templates/function_reference.rst',
   }
   
   # Reference index
   refdoc_generate_index = True
   refdoc_index_file = 'references.rst'
   
   # Glossary settings
   refdoc_glossary_enabled = True
   refdoc_glossary_file = 'glossary.rst'


.. code-block:: python

   # Custom reference resolvers
   refdoc_resolvers = {
       'function': 'path.to.function_resolver',
       'class': 'path.to.class_resolver',
   }
   
   # Reference templates
   refdoc_templates = {
       'function': 'templates/function_ref.html',
       'class': 'templates/class_ref.html',
   }
   
   # Cross-reference prefixes
   refdoc_prefixes = {
       'api': 'api/',
       'internal': 'internal/',
   }

Basic Usage
-----------

Creating References
~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. refdoc:: MyClass
      :type: class
      :module: mymodule
      
      This is the MyClass reference documentation.

Referencing Items
~~~~~~~~~~~~~~~~~

.. code-block:: rst

   See :refdoc:`MyClass` for details.
   
   The :refdoc:`calculate_sum` function is documented here.
   
   Refer to :refdoc:`mymodule.MyClass.method` for implementation.

Cross-References
~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. refdoc-xref::
      :target: external_api
      :url: https://external-api.example.com/docs
      
      Link to external API documentation.

Reference Index
~~~~~~~~~~~~~~~

.. code-block:: rst

   .. refdoc-index::
      :sort: alphabetical
      :group-by: type
      
      Automatically generated index of all references.

   API Reference
   =============
   
   This page contains the complete API reference.
   
   .. refdoc-index::
      :type: api
      :sort: module
      
   Core Classes
   ------------
   
   .. refdoc:: DataProcessor
      :type: class
      :module: mylib.core
      
      Main data processing class.
      
      Methods
      ~~~~~~~
      
      .. refdoc:: DataProcessor.process
         :type: method
         
         Process input data.
         
         :param data: Input data
         :type data: dict
         :return: Processed result
         :rtype: dict
      
      .. refdoc:: DataProcessor.validate
         :type: method
         
         Validate input data.
         
         :param data: Data to validate
         :type data: dict
         :return: True if valid
         :rtype: bool

Create ``docs/usage.rst``:

.. code-block:: rst

   Usage Guide
   ===========
   
   To process data, use the :refdoc:`DataProcessor` class:
   
   .. code-block:: python
   
      from mylib.core import DataProcessor
      
      processor = DataProcessor()
      result = processor.process(data)
   
   For validation, see :refdoc:`DataProcessor.validate`.

Example 2: External References
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``conf.py``:

.. code-block:: python

   refdoc_external_refs = {
       'python': ('https://docs.python.org/3/', None),
       'requests': ('https://requests.readthedocs.io/', None),
       'numpy': ('https://numpy.org/doc/stable/', None),
   }

``docs/dependencies.rst``:

.. code-block:: rst

   Dependencies
   ============
   
   This project uses:
   
   - Python standard library
     
     - :refdoc-ext:`dict <python:stdtypes.html#dict>`
     - :refdoc-ext:`list <python:stdtypes.html#list>`
   
   - External packages
     
     - :refdoc-ext:`requests.get <requests:api>`
     - :refdoc-ext:`numpy.array <numpy:reference/generated/numpy.array>`

Example 3: Reference Glossary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create ``docs/glossary.rst``:

.. code-block:: rst

   Glossary
   ========
   
   .. refdoc-glossary::
      :sort: alphabetical
   
   .. refdoc-term:: API
      
      Application Programming Interface. See :refdoc:`api/index` for details.
   
   .. refdoc-term:: Data Processor
      
      A component that transforms input data. Implemented in :refdoc:`DataProcessor`.
   
   .. refdoc-term:: Validation
      
      The process of checking data integrity. See :refdoc:`DataProcessor.validate`.

Use in documentation:

.. code-block:: rst

   The :term:`Data Processor` validates input using :term:`Validation`.
   
   For :term:`API` details, see the reference documentation.

Example 4: Reference Templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create ``templates/class_reference.rst``:

.. code-block:: rst

   {{ class_name }}
   {{ "=" * class_name|length }}
   
   .. currentmodule:: {{ module_name }}
   
   .. autoclass:: {{ class_name }}
      :members:
      :undoc-members:
      :show-inheritance:
   
   Description
   -----------
   
   {{ description }}
   
Advanced Features
-----------------

Reference Validation
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   refdoc_validate_refs = True
   refdoc_warn_broken = True
   refdoc_fail_on_broken = False

This will check all references during build and warn about broken links.

Reference Groups
~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. refdoc-group:: Core API
      :type: class
      
      .. refdoc:: DataProcessor
      .. refdoc:: DataValidator
      .. refdoc:: DataTransformer
   
   .. refdoc-group:: Utilities
      :type: function
      
      .. refdoc:: parse_config
      .. refdoc:: load_data
      .. refdoc:: save_results

Smart Reference Resolution
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   See :refdoc:`process` for details.
   
   # Automatically resolves to:
   # - DataProcessor.process if in DataProcessor context
   # - module.process if at module level
   # - Full path if ambiguous

Reference Inheritance
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. refdoc:: BaseClass
      :type: class
      
      Base class documentation.
   
   .. refdoc:: DerivedClass
      :type: class
      :inherits: BaseClass
      
      Derived class inherits all references from BaseClass.

Complete Documentation Example
-------------------------------

Project Structure
~~~~~~~~~~~~~~~~~

.. code-block:: text

   myproject/
   ├── docs/
   │   ├── conf.py
   │   ├── index.rst
   │   ├── api/
   │   │   ├── index.rst
   │   │   ├── core.rst
   │   │   └── utils.rst
   │   ├── guides/
   │   │   ├── quickstart.rst
   │   │   └── advanced.rst
   │   ├── glossary.rst
   │   └── references.rst
   └── src/
       └── mylib/
           ├── core.py
           └── utils.py

api/index.rst
~~~~~~~~~~~~~

.. code-block:: rst

   API Reference
   =============
   
   Complete API documentation.
   
   .. refdoc-index::
      :group-by: module
      :show-summary: true
   
   Core Module
   -----------
   
   .. toctree::
      :maxdepth: 2
      
      core
      utils

api/core.rst
~~~~~~~~~~~~

.. code-block:: rst

   Core Module
   ===========
   
   .. currentmodule:: mylib.core
   
   Classes
   -------
   
   DataProcessor
   ~~~~~~~~~~~~~
   
   .. refdoc:: DataProcessor
      :type: class
      :module: mylib.core
      
      Main data processing class.
      
      .. refdoc:: DataProcessor.__init__
         :type: method
         
         Initialize the processor.
         
         :param config: Configuration dict
      
      .. refdoc:: DataProcessor.process
         :type: method
         
         Process data.
         
         :param data: Input data
         :return: Processed result

guides/quickstart.rst
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Quick Start
   ===========
   
   Installation
   ------------
   
   .. code-block:: bash
   
      pip install mylib
   
   Basic Usage
   -----------
   
   Import and use the :refdoc:`DataProcessor`:
   
   .. code-block:: python
   
      from mylib.core import DataProcessor
      
      processor = DataProcessor()
      result = processor.process(data)
   
   For more details, see:
   
   - :refdoc:`DataProcessor` - Full API reference
   - :refdoc:`DataProcessor.process` - Process method
   - :term:`Data Processor` - Glossary entry

Docker Integration
------------------

Build Reference Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     viper-sphinx:latest \
     sphinx-build -b html /project/docs /project/docs/_build/html

Validate References
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     viper-sphinx:latest \
     sh -c "
       cd /project
       sphinx-build -W -b html docs/ docs/_build/html
     "

Generate Reference Index
~~~~~~~~~~~~~~~~~~~~~~~~

Create ``generate_refs.py``:

.. code-block:: python

   import os
   import re
   from pathlib import Path
   
   def find_references(docs_dir):
       refs = []
       for rst_file in Path(docs_dir).rglob('*.rst'):
           with open(rst_file, 'r') as f:
               content = f.read()
               matches = re.findall(r'\.\. refdoc:: (\w+)', content)
               refs.extend(matches)
       return sorted(set(refs))
   
   refs = find_references('docs')
   
   print("Reference Index")
   print("=" * 50)
   for ref in refs:
       print(f"- {ref}")

Run:

.. code-block:: bash

   docker run --rm -v $(pwd):/project \
     viper-sphinx:latest \
     python /project/generate_refs.py

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Build and Validate References
   
   on:
     push:
       paths:
         - 'docs/**'
   
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Build Docs
           run: |
             docker run --rm -v $(pwd):/project \
               viper-sphinx:latest \
               sphinx-build -W -b html /project/docs /project/docs/_build/html
         
         - name: Check References
           run: |
             docker run --rm -v $(pwd):/project \
               viper-sphinx:latest \
               sphinx-build -b linkcheck /project/docs /project/docs/_build/linkcheck

Best Practices
--------------

1. **Use Consistent Naming**
   
   .. code-block:: rst
   
      .. refdoc:: MyClass  # PascalCase for classes
      .. refdoc:: my_function  # snake_case for functions

2. **Group Related References**
   
   .. code-block:: rst
   
      .. refdoc-group:: Data Processing
         
         .. refdoc:: DataProcessor
         .. refdoc:: DataValidator

3. **Provide Context**
   
   Always include type and module information:
   
   .. code-block:: rst
   
      .. refdoc:: MyClass
         :type: class
         :module: mylib.core

4. **Maintain Glossary**
   
   Keep a central glossary of terms

5. **Validate Regularly**
   
   Enable reference validation in CI/CD

6. **Use Templates**
   
   Create templates for common reference patterns

Common Patterns
---------------

Module Reference
~~~~~~~~~~~~~~~~

.. code-block:: rst

   Module: {{ module_name }}
   ========================
   
   .. refdoc-module:: {{ module_name }}
   
   Classes
   -------
   
   .. refdoc-index::
      :type: class
      :module: {{ module_name }}
   
   Functions
   ---------
   
   .. refdoc-index::
      :type: function
      :module: {{ module_name }}

Function Reference
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. refdoc:: function_name
      :type: function
      :module: mymodule
      
      Brief description.
      
      :param arg1: Description
      :param arg2: Description
      :return: Description
      
      Example::
      
          result = function_name(arg1, arg2)

Class Reference
~~~~~~~~~~~~~~~

.. code-block:: rst

   .. refdoc:: ClassName
      :type: class
      :module: mymodule
      
      Class description.
      
      Attributes
      ----------
      
      .. refdoc:: ClassName.attribute
         :type: attribute
      
      Methods
      -------
      
      .. refdoc:: ClassName.method
         :type: method

Troubleshooting
---------------

Broken References
~~~~~~~~~~~~~~~~~

**Solution:**

Enable validation:

.. code-block:: python

   refdoc_validate_refs = True
   refdoc_warn_broken = True

References Not Linking
~~~~~~~~~~~~~~~~~~~~~~~

**Solution:**

Check reference target exists:

.. code-block:: rst

   # Define before referencing
   .. refdoc:: MyClass
      :type: class
   
   # Then reference
   See :refdoc:`MyClass`

External Links Failing
~~~~~~~~~~~~~~~~~~~~~~~

**Solution:**

Verify external reference configuration:

.. code-block:: python

   refdoc_external_refs = {
       'project': ('https://project.example.com/docs/', None),
   }

Next Steps
----------

1. Set up reference documentation structure
2. Create reference templates
3. Build API reference index
4. Add cross-references throughout documentation
5. Enable reference validation


Practical Examples
------------------

Basic Reference Documentation
------------------------------

Simple Reference
~~~~~~~~~~~~~~~~

.. refdoc:: example_function
   :type: function
   :module: mymodule
   
   A simple function that demonstrates basic reference documentation.
   
   :param str name: The name parameter
   :param int value: The value parameter
   :returns: Processed result
   :rtype: str

Class Reference
~~~~~~~~~~~~~~~

.. refdoc:: ExampleClass
   :type: class
   :module: mymodule
   
   An example class demonstrating class reference documentation.
   
   .. method:: process(data)
   
      Process the input data.
      
      :param data: Input data to process
      :type data: dict
      :returns: Processed result
      :rtype: dict
   
   .. attribute:: config
   
      Configuration dictionary for the class.
      
      :type: dict

Advanced Cross-Referencing
---------------------------

Reference Links
~~~~~~~~~~~~~~~

The extension provides enhanced reference linking:

- Function reference: :refdoc:`example_function`
- Class reference: :refdoc:`ExampleClass`
- Method reference: :refdoc:`ExampleClass.process`
- Module reference: :refdoc:`mymodule`

Automatic Reference Resolution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. refdoc:: calculate_total
   :type: function
   :module: finance
   :auto-resolve:
   
   Automatically resolves references to related functions and classes.
   
   This function uses :refdoc:`TaxCalculator` to compute taxes
   and :refdoc:`format_currency` to format the output.

API Documentation Structure
----------------------------

Module Documentation
~~~~~~~~~~~~~~~~~~~~

.. refdoc-module:: authentication
   
   Authentication module providing user authentication services.
   
   Functions
   ^^^^^^^^^
   
   .. refdoc:: login
      :type: function
      
      Authenticate a user with username and password.
      
      :param str username: User's username
      :param str password: User's password
      :returns: Authentication token
      :rtype: str
      :raises AuthenticationError: If credentials are invalid
   
   .. refdoc:: logout
      :type: function
      
      Terminate user session and invalidate token.
      
      :param str token: Authentication token
      :returns: Success status
      :rtype: bool
   
   Classes
   ^^^^^^^
   
   .. refdoc:: User
      :type: class
      
      Represents an authenticated user.
      
      .. attribute:: username
         
         User's username
         
         :type: str
      
      .. attribute:: email
         
         User's email address
         
         :type: str
      
      .. method:: get_permissions()
         
         Retrieve user permissions.
         
         :returns: List of permission strings
         :rtype: list[str]

Package Documentation
~~~~~~~~~~~~~~~~~~~~~

.. refdoc-package:: myapp
   
   Main application package.
   
   Modules
   ^^^^^^^
   
   - :refdoc:`myapp.auth` - Authentication services
   - :refdoc:`myapp.database` - Database connections
   - :refdoc:`myapp.api` - REST API endpoints
   - :refdoc:`myapp.utils` - Utility functions

Reference Index
---------------

Automatic Index Generation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. refdoc-index::
   :modules: mymodule, finance, authentication
   :types: function, class
   :sort: alphabetical
   
   Generates an alphabetical index of all documented items.

Filtered Index
~~~~~~~~~~~~~~

.. refdoc-index::
   :modules: authentication
   :types: function
   :visibility: public
   
   Shows only public functions from the authentication module.

Configuration Examples
----------------------

Extension Configuration
~~~~~~~~~~~~~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx.ext.autodoc',
       'sphinx_refdoc',
   ]
   
   # Refdoc configuration
   refdoc_show_private = False
   refdoc_show_inherited = True
   refdoc_group_by_type = True
   refdoc_auto_resolve = True
   refdoc_include_toc = True

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Custom reference resolvers
   refdoc_resolvers = {
       'function': 'path.to.function_resolver',
       'class': 'path.to.class_resolver',
   }
   
   # Reference templates
   refdoc_templates = {
       'function': 'templates/function_ref.html',
       'class': 'templates/class_ref.html',
   }
   
   # Cross-reference prefixes
   refdoc_prefixes = {
       'api': 'api/',
       'internal': 'internal/',
   }

Specialized Documentation
--------------------------

Property Documentation
~~~~~~~~~~~~~~~~~~~~~~

.. refdoc:: DataModel
   :type: class
   
   A model class with documented properties.
   
   .. property:: name
      
      The model's name.
      
      :type: str
      :getter: Returns the name
      :setter: Sets the name with validation
   
   .. property:: created_at
      
      Creation timestamp.
      
      :type: datetime
      :getter: Returns creation time
      :readonly:

Exception Documentation
~~~~~~~~~~~~~~~~~~~~~~~

.. refdoc:: ValidationError
   :type: exception
   
   Raised when data validation fails.
   
   .. attribute:: field
      
      The field that failed validation
      
      :type: str
   
   .. attribute:: message
      
      Error message describing the failure
      
      :type: str
   
   Example usage::
   
      try:
          validate_data(data)
      except ValidationError as e:
          print(f"Validation failed on {e.field}: {e.message}")

Decorator Documentation
~~~~~~~~~~~~~~~~~~~~~~~

.. refdoc:: cached_property
   :type: decorator
   
   Caches the result of a property method.
   
   Usage::
   
      class MyClass:
          @cached_property
          def expensive_calculation(self):
              return compute_result()

Integration Features
--------------------

With Autodoc
~~~~~~~~~~~~

.. code-block:: python

   # Combine with sphinx.ext.autodoc
   
   .. automodule:: mymodule
      :members:
      :refdoc-enhance:
      
   This adds refdoc cross-referencing to autodoc output.

With Type Hints
~~~~~~~~~~~~~~~

.. refdoc:: process_data
   :type: function
   :use-type-hints:
   
   Automatically extracts type information from Python type hints.
   
   .. code-block:: python
   
      def process_data(
          items: list[dict[str, Any]],
          config: Config | None = None
      ) -> ProcessedData:
          pass

Search Integration
~~~~~~~~~~~~~~~~~~

The refdoc extension integrates with Sphinx search:

.. code-block:: python

   refdoc_search_priority = {
       'function': 10,
       'class': 20,
       'module': 5,
   }
   
   # Search results will prioritize classes, then functions, then modules

Practical Examples
------------------

Complete Module Reference
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. refdoc-module:: calculator
   
   A simple calculator module.
   
   .. refdoc:: add
      :type: function
      
      Add two numbers.
      
      :param float a: First number
      :param float b: Second number
      :returns: Sum of a and b
      :rtype: float
      
      Example::
      
         result = add(5, 3)  # Returns 8.0
   
   .. refdoc:: Calculator
      :type: class
      
      A calculator class with memory.
      
      .. method:: __init__(initial_value=0)
         
         Initialize calculator with optional starting value.
         
         :param float initial_value: Starting value
      
      .. method:: add(value)
         
         Add to current value.
         
         :param float value: Value to add
         :returns: Updated total
         :rtype: float
      
      .. method:: clear()
         
         Reset calculator to zero.
      
      Example::
      
         calc = Calculator(10)
         calc.add(5)  # Returns 15
         calc.clear()  # Resets to 0

Reference with Examples
~~~~~~~~~~~~~~~~~~~~~~~

.. refdoc:: connect_database
   :type: function
   :examples:
   
   Connect to a database.
   
   :param str host: Database host
   :param int port: Database port
   :param str database: Database name
   :returns: Database connection
   :rtype: Connection
   
   **Basic Connection**::
   
      conn = connect_database('localhost', 5432, 'mydb')
   
   **With Context Manager**::
   
      with connect_database('localhost', 5432, 'mydb') as conn:
          cursor = conn.cursor()
          cursor.execute('SELECT * FROM users')
   
   **Error Handling**::
   
      try:
          conn = connect_database('remote', 5432, 'mydb')
      except ConnectionError as e:
          print(f"Failed to connect: {e}")


Practical Examples
------------------

Basic Reference Documentation
------------------------------

Simple Reference
~~~~~~~~~~~~~~~~

.. refdoc:: example_function
   :type: function
   :module: mymodule
   
   A simple function that demonstrates basic reference documentation.
   
   :param str name: The name parameter
   :param int value: The value parameter
   :returns: Processed result
   :rtype: str

Class Reference
~~~~~~~~~~~~~~~

.. refdoc:: ExampleClass
   :type: class
   :module: mymodule
   
   An example class demonstrating class reference documentation.
   
   .. method:: process(data)
   
      Process the input data.
      
      :param data: Input data to process
      :type data: dict
      :returns: Processed result
      :rtype: dict
   
   .. attribute:: config
   
      Configuration dictionary for the class.
      
      :type: dict

Advanced Cross-Referencing
---------------------------

Reference Links
~~~~~~~~~~~~~~~

The extension provides enhanced reference linking:

- Function reference: :refdoc:`example_function`
- Class reference: :refdoc:`ExampleClass`
- Method reference: :refdoc:`ExampleClass.process`
- Module reference: :refdoc:`mymodule`

Automatic Reference Resolution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. refdoc:: calculate_total
   :type: function
   :module: finance
   :auto-resolve:
   
   Automatically resolves references to related functions and classes.
   
   This function uses :refdoc:`TaxCalculator` to compute taxes
   and :refdoc:`format_currency` to format the output.

API Documentation Structure
----------------------------

Module Documentation
~~~~~~~~~~~~~~~~~~~~

.. refdoc-module:: authentication
   
   Authentication module providing user authentication services.
   
   Functions
   ^^^^^^^^^
   
   .. refdoc:: login
      :type: function
      
      Authenticate a user with username and password.
      
      :param str username: User's username
      :param str password: User's password
      :returns: Authentication token
      :rtype: str
      :raises AuthenticationError: If credentials are invalid
   
   .. refdoc:: logout
      :type: function
      
      Terminate user session and invalidate token.
      
      :param str token: Authentication token
      :returns: Success status
      :rtype: bool
   
   Classes
   ^^^^^^^
   
   .. refdoc:: User
      :type: class
      
      Represents an authenticated user.
      
      .. attribute:: username
         
         User's username
         
         :type: str
      
      .. attribute:: email
         
         User's email address
         
         :type: str
      
      .. method:: get_permissions()
         
         Retrieve user permissions.
         
         :returns: List of permission strings
         :rtype: list[str]

Package Documentation
~~~~~~~~~~~~~~~~~~~~~

.. refdoc-package:: myapp
   
   Main application package.
   
   Modules
   ^^^^^^^
   
   - :refdoc:`myapp.auth` - Authentication services
   - :refdoc:`myapp.database` - Database connections
   - :refdoc:`myapp.api` - REST API endpoints
   - :refdoc:`myapp.utils` - Utility functions

Reference Index
---------------

Automatic Index Generation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. refdoc-index::
   :modules: mymodule, finance, authentication
   :types: function, class
   :sort: alphabetical
   
   Generates an alphabetical index of all documented items.

Filtered Index
~~~~~~~~~~~~~~

.. refdoc-index::
   :modules: authentication
   :types: function
   :visibility: public
   
   Shows only public functions from the authentication module.

Configuration Examples
----------------------

Extension Configuration
~~~~~~~~~~~~~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx.ext.autodoc',
       'sphinx_refdoc',
   ]
   
   # Refdoc configuration
   refdoc_show_private = False
   refdoc_show_inherited = True
   refdoc_group_by_type = True
   refdoc_auto_resolve = True
   refdoc_include_toc = True

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Custom reference resolvers
   refdoc_resolvers = {
       'function': 'path.to.function_resolver',
       'class': 'path.to.class_resolver',
   }
   
   # Reference templates
   refdoc_templates = {
       'function': 'templates/function_ref.html',
       'class': 'templates/class_ref.html',
   }
   
   # Cross-reference prefixes
   refdoc_prefixes = {
       'api': 'api/',
       'internal': 'internal/',
   }

Specialized Documentation
--------------------------

Property Documentation
~~~~~~~~~~~~~~~~~~~~~~

.. refdoc:: DataModel
   :type: class
   
   A model class with documented properties.
   
   .. property:: name
      
      The model's name.
      
      :type: str
      :getter: Returns the name
      :setter: Sets the name with validation
   
   .. property:: created_at
      
      Creation timestamp.
      
      :type: datetime
      :getter: Returns creation time
      :readonly:

Exception Documentation
~~~~~~~~~~~~~~~~~~~~~~~

.. refdoc:: ValidationError
   :type: exception
   
   Raised when data validation fails.
   
   .. attribute:: field
      
      The field that failed validation
      
      :type: str
   
   .. attribute:: message
      
      Error message describing the failure
      
      :type: str
   
   Example usage::
   
      try:
          validate_data(data)
      except ValidationError as e:
          print(f"Validation failed on {e.field}: {e.message}")

Decorator Documentation
~~~~~~~~~~~~~~~~~~~~~~~

.. refdoc:: cached_property
   :type: decorator
   
   Caches the result of a property method.
   
   Usage::
   
      class MyClass:
          @cached_property
          def expensive_calculation(self):
              return compute_result()

Integration Features
--------------------

With Autodoc
~~~~~~~~~~~~

.. code-block:: python

   # Combine with sphinx.ext.autodoc
   
   .. automodule:: mymodule
      :members:
      :refdoc-enhance:
      
   This adds refdoc cross-referencing to autodoc output.

With Type Hints
~~~~~~~~~~~~~~~

.. refdoc:: process_data
   :type: function
   :use-type-hints:
   
   Automatically extracts type information from Python type hints.
   
   .. code-block:: python
   
      def process_data(
          items: list[dict[str, Any]],
          config: Config | None = None
      ) -> ProcessedData:
          pass

Search Integration
~~~~~~~~~~~~~~~~~~

The refdoc extension integrates with Sphinx search:

.. code-block:: python

   refdoc_search_priority = {
       'function': 10,
       'class': 20,
       'module': 5,
   }
   
   # Search results will prioritize classes, then functions, then modules

Practical Examples
------------------

Complete Module Reference
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. refdoc-module:: calculator
   
   A simple calculator module.
   
   .. refdoc:: add
      :type: function
      
      Add two numbers.
      
      :param float a: First number
      :param float b: Second number
      :returns: Sum of a and b
      :rtype: float
      
      Example::
      
         result = add(5, 3)  # Returns 8.0
   
   .. refdoc:: Calculator
      :type: class
      
      A calculator class with memory.
      
      .. method:: __init__(initial_value=0)
         
         Initialize calculator with optional starting value.
         
         :param float initial_value: Starting value
      
      .. method:: add(value)
         
         Add to current value.
         
         :param float value: Value to add
         :returns: Updated total
         :rtype: float
      
      .. method:: clear()
         
         Reset calculator to zero.
      
      Example::
      
         calc = Calculator(10)
         calc.add(5)  # Returns 15
         calc.clear()  # Resets to 0

Reference with Examples
~~~~~~~~~~~~~~~~~~~~~~~

.. refdoc:: connect_database
   :type: function
   :examples:
   
   Connect to a database.
   
   :param str host: Database host
   :param int port: Database port
   :param str database: Database name
   :returns: Database connection
   :rtype: Connection
   
   **Basic Connection**::
   
      conn = connect_database('localhost', 5432, 'mydb')
   
   **With Context Manager**::
   
      with connect_database('localhost', 5432, 'mydb') as conn:
          cursor = conn.cursor()
          cursor.execute('SELECT * FROM users')
   
   **Error Handling**::
   
      try:
          conn = connect_database('remote', 5432, 'mydb')
      except ConnectionError as e:
          print(f"Failed to connect: {e}")


Practical Examples
------------------

Basic Reference Documentation
------------------------------

Simple Reference
~~~~~~~~~~~~~~~~

.. refdoc:: example_function
   :type: function
   :module: mymodule
   
   A simple function that demonstrates basic reference documentation.
   
   :param str name: The name parameter
   :param int value: The value parameter
   :returns: Processed result
   :rtype: str

Class Reference
~~~~~~~~~~~~~~~

.. refdoc:: ExampleClass
   :type: class
   :module: mymodule
   
   An example class demonstrating class reference documentation.
   
   .. method:: process(data)
   
      Process the input data.
      
      :param data: Input data to process
      :type data: dict
      :returns: Processed result
      :rtype: dict
   
   .. attribute:: config
   
      Configuration dictionary for the class.
      
      :type: dict

Advanced Cross-Referencing
---------------------------

Reference Links
~~~~~~~~~~~~~~~

The extension provides enhanced reference linking:

- Function reference: :refdoc:`example_function`
- Class reference: :refdoc:`ExampleClass`
- Method reference: :refdoc:`ExampleClass.process`
- Module reference: :refdoc:`mymodule`

Automatic Reference Resolution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. refdoc:: calculate_total
   :type: function
   :module: finance
   :auto-resolve:
   
   Automatically resolves references to related functions and classes.
   
   This function uses :refdoc:`TaxCalculator` to compute taxes
   and :refdoc:`format_currency` to format the output.

API Documentation Structure
----------------------------

Module Documentation
~~~~~~~~~~~~~~~~~~~~

.. refdoc-module:: authentication
   
   Authentication module providing user authentication services.
   
   Functions
   ^^^^^^^^^
   
   .. refdoc:: login
      :type: function
      
      Authenticate a user with username and password.
      
      :param str username: User's username
      :param str password: User's password
      :returns: Authentication token
      :rtype: str
      :raises AuthenticationError: If credentials are invalid
   
   .. refdoc:: logout
      :type: function
      
      Terminate user session and invalidate token.
      
      :param str token: Authentication token
      :returns: Success status
      :rtype: bool
   
   Classes
   ^^^^^^^
   
   .. refdoc:: User
      :type: class
      
      Represents an authenticated user.
      
      .. attribute:: username
         
         User's username
         
         :type: str
      
      .. attribute:: email
         
         User's email address
         
         :type: str
      
      .. method:: get_permissions()
         
         Retrieve user permissions.
         
         :returns: List of permission strings
         :rtype: list[str]

Package Documentation
~~~~~~~~~~~~~~~~~~~~~

.. refdoc-package:: myapp
   
   Main application package.
   
   Modules
   ^^^^^^^
   
   - :refdoc:`myapp.auth` - Authentication services
   - :refdoc:`myapp.database` - Database connections
   - :refdoc:`myapp.api` - REST API endpoints
   - :refdoc:`myapp.utils` - Utility functions

Reference Index
---------------

Automatic Index Generation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. refdoc-index::
   :modules: mymodule, finance, authentication
   :types: function, class
   :sort: alphabetical
   
   Generates an alphabetical index of all documented items.

Filtered Index
~~~~~~~~~~~~~~

.. refdoc-index::
   :modules: authentication
   :types: function
   :visibility: public
   
   Shows only public functions from the authentication module.

Configuration Examples
----------------------

Extension Configuration
~~~~~~~~~~~~~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx.ext.autodoc',
       'sphinx_refdoc',
   ]
   
   # Refdoc configuration
   refdoc_show_private = False
   refdoc_show_inherited = True
   refdoc_group_by_type = True
   refdoc_auto_resolve = True
   refdoc_include_toc = True

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Custom reference resolvers
   refdoc_resolvers = {
       'function': 'path.to.function_resolver',
       'class': 'path.to.class_resolver',
   }
   
   # Reference templates
   refdoc_templates = {
       'function': 'templates/function_ref.html',
       'class': 'templates/class_ref.html',
   }
   
   # Cross-reference prefixes
   refdoc_prefixes = {
       'api': 'api/',
       'internal': 'internal/',
   }

Specialized Documentation
--------------------------

Property Documentation
~~~~~~~~~~~~~~~~~~~~~~

.. refdoc:: DataModel
   :type: class
   
   A model class with documented properties.
   
   .. property:: name
      
      The model's name.
      
      :type: str
      :getter: Returns the name
      :setter: Sets the name with validation
   
   .. property:: created_at
      
      Creation timestamp.
      
      :type: datetime
      :getter: Returns creation time
      :readonly:

Exception Documentation
~~~~~~~~~~~~~~~~~~~~~~~

.. refdoc:: ValidationError
   :type: exception
   
   Raised when data validation fails.
   
   .. attribute:: field
      
      The field that failed validation
      
      :type: str
   
   .. attribute:: message
      
      Error message describing the failure
      
      :type: str
   
   Example usage::
   
      try:
          validate_data(data)
      except ValidationError as e:
          print(f"Validation failed on {e.field}: {e.message}")

Decorator Documentation
~~~~~~~~~~~~~~~~~~~~~~~

.. refdoc:: cached_property
   :type: decorator
   
   Caches the result of a property method.
   
   Usage::
   
      class MyClass:
          @cached_property
          def expensive_calculation(self):
              return compute_result()

Integration Features
--------------------

With Autodoc
~~~~~~~~~~~~

.. code-block:: python

   # Combine with sphinx.ext.autodoc
   
   .. automodule:: mymodule
      :members:
      :refdoc-enhance:
      
   This adds refdoc cross-referencing to autodoc output.

With Type Hints
~~~~~~~~~~~~~~~

.. refdoc:: process_data
   :type: function
   :use-type-hints:
   
   Automatically extracts type information from Python type hints.
   
   .. code-block:: python
   
      def process_data(
          items: list[dict[str, Any]],
          config: Config | None = None
      ) -> ProcessedData:
          pass

Search Integration
~~~~~~~~~~~~~~~~~~

The refdoc extension integrates with Sphinx search:

.. code-block:: python

   refdoc_search_priority = {
       'function': 10,
       'class': 20,
       'module': 5,
   }
   
   # Search results will prioritize classes, then functions, then modules

Practical Examples
------------------

Complete Module Reference
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. refdoc-module:: calculator
   
   A simple calculator module.
   
   .. refdoc:: add
      :type: function
      
      Add two numbers.
      
      :param float a: First number
      :param float b: Second number
      :returns: Sum of a and b
      :rtype: float
      
      Example::
      
         result = add(5, 3)  # Returns 8.0
   
   .. refdoc:: Calculator
      :type: class
      
      A calculator class with memory.
      
      .. method:: __init__(initial_value=0)
         
         Initialize calculator with optional starting value.
         
         :param float initial_value: Starting value
      
      .. method:: add(value)
         
         Add to current value.
         
         :param float value: Value to add
         :returns: Updated total
         :rtype: float
      
      .. method:: clear()
         
         Reset calculator to zero.
      
      Example::
      
         calc = Calculator(10)
         calc.add(5)  # Returns 15
         calc.clear()  # Resets to 0

Reference with Examples
~~~~~~~~~~~~~~~~~~~~~~~

.. refdoc:: connect_database
   :type: function
   :examples:
   
   Connect to a database.
   
   :param str host: Database host
   :param int port: Database port
   :param str database: Database name
   :returns: Database connection
   :rtype: Connection
   
   **Basic Connection**::
   
      conn = connect_database('localhost', 5432, 'mydb')
   
   **With Context Manager**::
   
      with connect_database('localhost', 5432, 'mydb') as conn:
          cursor = conn.cursor()
          cursor.execute('SELECT * FROM users')
   
   **Error Handling**::
   
      try:
          conn = connect_database('remote', 5432, 'mydb')
      except ConnectionError as e:
          print(f"Failed to connect: {e}")

Additional Resources
--------------------
- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- :doc:`sphinx-autoapi` - Automatic API documentation
- `Sphinx Cross-Referencing <https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html>`_
- :doc:`../tutorials/packages/sphinx-refdoc` - Complete tutorial
- Official documentation: https://sphinx-refdoc.readthedocs.io/
- GitHub repository: https://github.com/sphinx-doc/sphinx-refdoc

