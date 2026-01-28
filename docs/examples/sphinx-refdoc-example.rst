Sphinx-Refdoc Example
=====================

This page demonstrates the **sphinx-refdoc** extension for creating reference documentation with enhanced cross-referencing capabilities.

.. contents:: Contents
   :local:
   :depth: 2

Overview
--------

The sphinx-refdoc extension provides advanced reference documentation features, including automatic reference generation, enhanced cross-referencing, and structured API documentation.

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

See Also
--------

- :doc:`../tutorials/packages/sphinx-refdoc` - Complete tutorial
- Official documentation: https://sphinx-refdoc.readthedocs.io/
- GitHub repository: https://github.com/sphinx-doc/sphinx-refdoc
