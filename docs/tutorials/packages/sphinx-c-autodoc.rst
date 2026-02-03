Sphinx-C-Autodoc Tutorial
=========================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-c-autodoc/>`_
   - `API Documentation <../../pdoc/sphinx_c_autodoc/index.html>`_
   - `Manual <https://sphinx-c-autodoc.readthedocs.io/en/latest/>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinx-c-autodoc to automatically generate documentation for C code from source files, similar to how autodoc works for Python.

What is Sphinx-C-Autodoc?
--------------------------
sphinx-c-autodoc is a Sphinx extension that automatically extracts and documents C code elements including:

- Functions and their signatures
- Structures and unions
- Enumerations and typedefs
- Macros and constants
- Global variables
- Function pointers
- Documentation from C comments (Doxygen-style)

Unlike Doxygen + Breathe, sphinx-c-autodoc works directly with C source files without requiring a separate Doxygen build step.

sphinx-c-autodoc provides automatic API documentation generation for C projects:

- Extract documentation from C header files
- Document functions, structs, enums, and macros
- Support for Doxygen-style comments
- Generate API references automatically


Installation
------------

sphinx-c-autodoc is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm viper-sphinx:latest python -c "import sphinx_c_autodoc; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_c_autodoc',
   ]
   
   # Path to C source files
   c_autodoc_roots = ['../src']

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinx_c_autodoc']
   
   # C source configuration
   c_autodoc_roots = ['../src', '../include']
   c_autodoc_exclude_patterns = ['*_test.c', 'test_*.c']
   
   # Compiler settings for parsing
   c_autodoc_compiler_args = [
       '-I../include',
       '-DDEBUG=1',
       '-std=c11',
   ]
   
   # Documentation options
   c_autodoc_show_private = False
   c_autodoc_show_static = True
   c_autodoc_show_macros = True
   c_autodoc_show_typedefs = True
   
   # Comment style
   c_autodoc_comment_style = 'doxygen'  # or 'kernel'
   
   # Code highlighting
   c_autodoc_syntax_highlight = True


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_c_autodoc',
       # ... other extensions
   ]
   
   # C source directories
   c_autodoc_roots = ['src/', 'include/']
   
   # Header file patterns
   c_autodoc_include_patterns = ['*.h']

Basic Usage
-----------

Documenting Functions
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. c:autofunction:: calculate_sum

This will extract the function signature and documentation from the C source.

Documenting Structures
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. c:autostruct:: point
      :members:

Documenting Enums
~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. c:autoenum:: status_code

Documenting Macros
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. c:automacro:: MAX_SIZE

Auto-Document Entire File
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. c:autofile:: utils.c
      :show-functions:
      :show-structs:
      :show-macros:

C Code Documentation
--------------------

Doxygen-Style Comments
~~~~~~~~~~~~~~~~~~~~~~

Create ``src/math_utils.c``:

.. code-block:: c

   /**
    * @file math_utils.c
    * @brief Mathematical utility functions
    */
   
   #include <stdint.h>
   
   /**
    * @brief Calculate the sum of two integers
    * 
    * @param a First operand
    * @param b Second operand
    * @return Sum of a and b
    * 
    * @note This function performs basic addition
    * 
    * Example:
    * @code
    * int result = add(5, 3);  // result = 8
    * @endcode
    */
   int add(int a, int b) {
       return a + b;
   }
   
   /**
    * @brief Calculate factorial of a number
    * 
    * @param n Number to calculate factorial for
    * @return Factorial of n, or 0 if n < 0
    * 
    * @warning Large values of n may cause overflow
    */
   uint64_t factorial(int n) {
       if (n < 0) return 0;
       if (n == 0 || n == 1) return 1;
       
       uint64_t result = 1;
       for (int i = 2; i <= n; i++) {
           result *= i;
       }
       return result;
   }

Document in ``docs/math.rst``:

.. code-block:: rst

   Math Utilities
   ==============
   
   .. c:autofile:: math_utils.c
   
   Functions
   ---------
   
   Addition
   ~~~~~~~~
   
   .. c:autofunction:: add
   
   Factorial
   ~~~~~~~~~
   
   .. c:autofunction:: factorial

Structures and Types
~~~~~~~~~~~~~~~~~~~~

``src/types.h``:

.. code-block:: c

   /**
    * @file types.h
    * @brief Common type definitions
    */
   
   #ifndef TYPES_H
   #define TYPES_H
   
   #include <stdint.h>
   #include <stdbool.h>
   
   /**
    * @brief 2D point structure
    */
   typedef struct {
       double x;  ///< X coordinate
       double y;  ///< Y coordinate
   } point_t;
   
   /**
    * @brief 3D vector structure
    */
   typedef struct {
       double x;  ///< X component
       double y;  ///< Y component
       double z;  ///< Z component
   } vector3_t;
   
   /**
    * @brief Status codes
    */
   typedef enum {
       STATUS_OK = 0,      ///< Operation successful
       STATUS_ERROR = -1,  ///< Generic error
       STATUS_NOMEM = -2,  ///< Out of memory
       STATUS_INVAL = -3   ///< Invalid argument
   } status_t;
   
   /**
    * @brief Configuration structure
    */
   typedef struct {
       bool debug;           ///< Enable debug mode
       uint32_t buffer_size; ///< Buffer size in bytes
       const char *filename; ///< Configuration filename
   } config_t;
   
   #endif

``docs/types.rst``:

.. code-block:: rst

   Type Definitions
   ================
   
   Structures
   ----------
   
   Point
   ~~~~~
   
   .. c:autostruct:: point_t
      :members:
   
   Vector3
   ~~~~~~~
   
   .. c:autostruct:: vector3_t
      :members:
   
   Configuration
   ~~~~~~~~~~~~~
   
   .. c:autostruct:: config_t
      :members:
   
   Enumerations
   ------------
   
   Status Codes
   ~~~~~~~~~~~~
   
   .. c:autoenum:: status_t

   String Utilities
   ================
   
   This module provides string manipulation functions.
   
   .. c:autofile:: string_utils.c
   
   API Reference
   -------------
   
   Case Conversion
   ~~~~~~~~~~~~~~~
   
   .. c:autofunction:: str_upper
   
   String Validation
   ~~~~~~~~~~~~~~~~~
   
   .. c:autofunction:: str_is_empty
   
   String Modification
   ~~~~~~~~~~~~~~~~~~~
   
   .. c:autofunction:: str_trim
   
   Usage Examples
   --------------
   
   Basic Usage
   ~~~~~~~~~~~
   
   .. code-block:: c
   
      #include "string_utils.h"
      
      int main() {
          char text[] = "  Hello World  ";
          
          str_trim(text);
          printf("Trimmed: '%s'\n", text);  // "Hello World"
          
          str_upper(text);
          printf("Upper: '%s'\n", text);    // "HELLO WORLD"
          
          if (str_is_empty("")) {
              printf("String is empty\n");
          }
          
          return 0;
      }

Example 2: Data Structure Library
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``src/list.h``:

.. code-block:: c

   /**
    * @file list.h
    * @brief Linked list implementation
    */
   
   #ifndef LIST_H
   #define LIST_H
   
   #include <stddef.h>
   #include <stdbool.h>
   
   /**
    * @brief List node structure
    */
   typedef struct list_node {
       void *data;              ///< Pointer to node data
       struct list_node *next;  ///< Pointer to next node
   } list_node_t;
   
   /**
    * @brief Linked list structure
    */
   typedef struct {
       list_node_t *head;  ///< Pointer to first node
       list_node_t *tail;  ///< Pointer to last node
       size_t size;        ///< Number of nodes
   } list_t;
   
   /**
    * @brief Initialize a new list
    * 
    * @param list Pointer to list structure
    */
   void list_init(list_t *list);
   
   /**
    * @brief Append data to end of list
    * 
    * @param list Pointer to list
    * @param data Pointer to data to append
    * @return true if successful, false on allocation failure
    */
   bool list_append(list_t *list, void *data);
   
   /**
    * @brief Get data at specified index
    * 
    * @param list Pointer to list
    * @param index Index of element to retrieve
    * @return Pointer to data, or NULL if index out of bounds
    */
   void* list_get(const list_t *list, size_t index);
   
   /**
    * @brief Remove element at specified index
    * 
    * @param list Pointer to list
    * @param index Index of element to remove
    * @return Pointer to removed data, or NULL if index out of bounds
    */
   void* list_remove(list_t *list, size_t index);
   
   /**
    * @brief Clear all elements from list
    * 
    * @param list Pointer to list
    * @param free_func Function to free node data (can be NULL)
    */
   void list_clear(list_t *list, void (*free_func)(void*));
   
   /**
    * @brief Get number of elements in list
    * 
    * @param list Pointer to list
    * @return Number of elements
    */
   static inline size_t list_size(const list_t *list) {
       return list ? list->size : 0;
   }
   
   #endif

``docs/list.rst``:

.. code-block:: rst

   Linked List
   ===========
   
   A simple singly-linked list implementation.
   
   Data Structures
   ---------------
   
   .. c:autostruct:: list_t
      :members:
   
   .. c:autostruct:: list_node_t
      :members:
   
   Functions
   ---------
   
   Initialization
   ~~~~~~~~~~~~~~
   
   .. c:autofunction:: list_init
   
   Modification
   ~~~~~~~~~~~~
   
   .. c:autofunction:: list_append
   .. c:autofunction:: list_remove
   .. c:autofunction:: list_clear
   
   Access
   ~~~~~~
   
   .. c:autofunction:: list_get
   .. c:autofunction:: list_size
   
Advanced Features
-----------------

Macro Documentation
~~~~~~~~~~~~~~~~~~~

``src/macros.h``:

.. code-block:: c

   /**
    * @def MAX(a, b)
    * @brief Return maximum of two values
    */
   #define MAX(a, b) ((a) > (b) ? (a) : (b))
   
   /**
    * @def MIN(a, b)
    * @brief Return minimum of two values
    */
   #define MIN(a, b) ((a) < (b) ? (a) : (b))
   
   /**
    * @def ARRAY_SIZE(arr)
    * @brief Get number of elements in array
    */
   #define ARRAY_SIZE(arr) (sizeof(arr) / sizeof((arr)[0]))

Document:

.. code-block:: rst

   .. c:automacro:: MAX
   .. c:automacro:: MIN
   .. c:automacro:: ARRAY_SIZE

Function Pointers
~~~~~~~~~~~~~~~~~

.. code-block:: c

   /**
    * @brief Comparison function type
    * 
    * @param a First value
    * @param b Second value
    * @return <0 if a<b, 0 if a==b, >0 if a>b
    */
   typedef int (*compare_fn)(const void *a, const void *b);

.. code-block:: rst

   .. c:autotype:: compare_fn

Complete Module
~~~~~~~~~~~~~~~

.. code-block:: rst

   .. c:automodule:: utils
      :members:
      :show-private:

Docker Integration
------------------

Build C Documentation
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     viper-sphinx:latest \
     sphinx-build -b html /project/docs /project/docs/_build/html

With Compilation Check
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm -v $(pwd):/project viper-sphinx:latest sh -c "
       cd /project
       
       # Compile C code to verify
       gcc -c src/*.c -Iinclude
       
       # Build documentation
       sphinx-build -b html docs/ docs/_build/html
   "

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Build C Documentation
   
   on:
     push:
       paths:
         - 'src/**'
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
               sphinx-build -b html /project/docs /project/docs/_build/html

Best Practices
--------------

1. **Use Doxygen-Style Comments**
   
   .. code-block:: c
   
      /**
       * @brief Brief description
       * 
       * @param param1 Description
       * @return Return value description
       */

2. **Document All Public API**
   
   Every public function, struct, and macro should have documentation

3. **Provide Examples**
   
   Include usage examples in comments:
   
   .. code-block:: c
   
      /**
       * Example:
       * @code
       * int result = func(10);
       * @endcode
       */

4. **Group Related Functions**
   
   Use file-level documentation to organize

5. **Document Parameters and Returns**
   
   Always describe what goes in and comes out

6. **Note Special Behavior**
   
   Use ``@note``, ``@warning``, ``@see`` tags

Common Patterns
---------------

API Reference Template
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   {Module Name}
   =============
   
   Overview
   --------
   
   Brief module description.
   
   Types
   -----
   
   .. c:autostruct:: {struct_name}
      :members:
   
   Functions
   ---------
   
   .. c:autofunction:: {function_name}
   
Troubleshooting
---------------

Functions Not Found
~~~~~~~~~~~~~~~~~~~

**Solution:**

Check ``c_autodoc_roots`` includes source directory:

.. code-block:: python

   c_autodoc_roots = ['../src', '../include']

Compilation Errors
~~~~~~~~~~~~~~~~~~

**Solution:**

Add necessary compiler flags:

.. code-block:: python

   c_autodoc_compiler_args = [
       '-I../include',
       '-std=c11',
   ]

Next Steps
----------

1. Add documentation comments to your C code
2. Configure source paths in conf.py
3. Create RST files for your modules
4. Build and review the documentation
5. Consider :doc:`doxygen-breathe-exhale` for more features


Practical Examples
------------------

This page demonstrates the **sphinx-c-autodoc** extension which automatically generates documentation for C code, similar to autodoc for Python.


Configuration
-------------

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_c_autodoc',
       # ... other extensions
   ]
   
   # C source directories
   c_autodoc_roots = ['src/', 'include/']
   
   # Header file patterns
   c_autodoc_include_patterns = ['*.h']

Basic Usage
-----------

Function Documentation
~~~~~~~~~~~~~~~~~~~~~~

**C Header** (``math_utils.h``):

.. code-block:: c

   /**
    * @file math_utils.h
    * @brief Mathematical utility functions
    * @author Development Team
    * @date 2026-01-26
    */
   
   #ifndef MATH_UTILS_H
   #define MATH_UTILS_H
   
   /**
    * @brief Calculate factorial of a number
    * 
    * Computes n! = n × (n-1) × (n-2) × ... × 1
    * 
    * @param n Input number (must be >= 0)
    * @return Factorial of n, or -1 on error
    * 
    * @note Maximum input value is 20 to prevent overflow
    * @warning Returns -1 for negative inputs
    * 
    * @code
    * int result = factorial(5);  // Returns 120
    * @endcode
    */
   long factorial(int n);
   
   /**
    * @brief Check if number is prime
    * 
    * @param num Number to check
    * @return 1 if prime, 0 otherwise
    * 
    * @par Algorithm:
    * Uses trial division up to sqrt(num)
    * 
    * @see factorial()
    */
   int is_prime(unsigned int num);
   
   #endif

**Sphinx Documentation** (``api.rst``):

.. code-block:: rst

   Math Utilities API
   ==================
   
   .. c:autofunction:: factorial
   
   .. c:autofunction:: is_prime

Struct Documentation
~~~~~~~~~~~~~~~~~~~~

**C Header** (``data_structures.h``):

.. code-block:: c

   /**
    * @brief Configuration structure
    * 
    * Holds application configuration parameters
    */
   typedef struct {
       /** Server hostname or IP address */
       char *host;
       
       /** Server port number (1-65535) */
       unsigned int port;
       
       /** Connection timeout in seconds */
       int timeout;
       
       /** Enable SSL/TLS encryption */
       int use_ssl;
       
       /** Maximum retry attempts */
       unsigned int max_retries;
   } config_t;
   
   /**
    * @brief Initialize configuration with defaults
    * 
    * @param cfg Pointer to configuration structure
    * @return 0 on success, -1 on error
    * 
    * @pre cfg must not be NULL
    * @post cfg is initialized with default values
    */
   int config_init(config_t *cfg);
   
   /**
    * @brief Free configuration resources
    * 
    * @param cfg Pointer to configuration structure
    */
   void config_free(config_t *cfg);

**Documentation**:

.. code-block:: rst

   Configuration API
   =================
   
   .. c:autostruct:: config_t
      :members:
   
   Initialization
   --------------
   
   .. c:autofunction:: config_init
   
   Cleanup
   -------
   
   .. c:autofunction:: config_free

Enum Documentation
~~~~~~~~~~~~~~~~~~

**C Header** (``status_codes.h``):

.. code-block:: c

   /**
    * @brief Operation status codes
    * 
    * Standard return codes for API functions
    */
   typedef enum {
       /** Operation completed successfully */
       STATUS_SUCCESS = 0,
       
       /** General failure */
       STATUS_ERROR = -1,
       
       /** Invalid function argument */
       STATUS_INVALID_ARG = -2,
       
       /** Memory allocation failed */
       STATUS_NO_MEMORY = -3,
       
       /** I/O operation failed */
       STATUS_IO_ERROR = -4,
       
       /** Operation timed out */
       STATUS_TIMEOUT = -5
   } status_code_t;
   
   /**
    * @brief Convert status code to string
    * 
    * @param code Status code
    * @return Human-readable error message
    */
   const char* status_to_string(status_code_t code);

**Documentation**:

.. code-block:: rst

   Status Codes
   ============
   
   .. c:autoenum:: status_code_t
      :members:
   
   .. c:autofunction:: status_to_string

Advanced Examples
-----------------

Macro Documentation
~~~~~~~~~~~~~~~~~~~

**C Header** (``macros.h``):

.. code-block:: c

   /**
    * @def MAX(a, b)
    * @brief Return maximum of two values
    * 
    * @param a First value
    * @param b Second value
    * @return The larger of a and b
    * 
    * @warning Evaluates arguments multiple times
    */
   #define MAX(a, b) ((a) > (b) ? (a) : (b))
   
   /**
    * @def MIN(a, b)
    * @brief Return minimum of two values
    */
   #define MIN(a, b) ((a) < (b) ? (a) : (b))
   
   /**
    * @def ARRAY_SIZE(arr)
    * @brief Calculate number of elements in array
    * 
    * @param arr Array variable (not pointer)
    * @return Number of elements
    * 
    * @note Only works with actual arrays, not pointers
    */
   #define ARRAY_SIZE(arr) (sizeof(arr) / sizeof((arr)[0]))

**Documentation**:

.. code-block:: rst

   Utility Macros
   ==============
   
   .. c:automacro:: MAX
   
   .. c:automacro:: MIN
   
   .. c:automacro:: ARRAY_SIZE

Complete Module Example
~~~~~~~~~~~~~~~~~~~~~~~~

**C Header** (``logger.h``):

.. code-block:: c

   /**
    * @file logger.h
    * @brief Logging system
    * 
    * Provides hierarchical logging with multiple severity levels
    * and output destinations.
    */
   
   #ifndef LOGGER_H
   #define LOGGER_H
   
   #include <stdio.h>
   
   /**
    * @brief Log severity levels
    */
   typedef enum {
       LOG_TRACE,    /**< Detailed trace information */
       LOG_DEBUG,    /**< Debug information */
       LOG_INFO,     /**< Informational messages */
       LOG_WARNING,  /**< Warning messages */
       LOG_ERROR,    /**< Error messages */
       LOG_FATAL     /**< Fatal errors */
   } log_level_t;
   
   /**
    * @brief Logger instance
    */
   typedef struct logger {
       FILE *output;           /**< Output file handle */
       log_level_t min_level;  /**< Minimum level to log */
       int use_colors;         /**< Enable colored output */
       const char *prefix;     /**< Message prefix */
   } logger_t;
   
   /**
    * @brief Create a new logger
    * 
    * @param output Output file (stdout, stderr, or file)
    * @param min_level Minimum severity level to log
    * @return Pointer to logger, or NULL on error
    * 
    * @par Example:
    * @code
    * logger_t *log = logger_create(stdout, LOG_INFO);
    * logger_log(log, LOG_INFO, "Application started");
    * logger_destroy(log);
    * @endcode
    */
   logger_t* logger_create(FILE *output, log_level_t min_level);
   
   /**
    * @brief Log a message
    * 
    * @param logger Logger instance
    * @param level Message severity level
    * @param format Printf-style format string
    * @param ... Format arguments
    * 
    * @return Number of characters written, or -1 on error
    */
   int logger_log(logger_t *logger, log_level_t level, 
                  const char *format, ...);
   
   /**
    * @brief Destroy logger and free resources
    * 
    * @param logger Logger to destroy
    */
   void logger_destroy(logger_t *logger);
   
   #endif

**Documentation** (``logging.rst``):

.. code-block:: rst

   Logging System
   ==============
   
   The logging system provides structured logging with severity levels.
   
   Types
   -----
   
   .. c:autoenum:: log_level_t
      :members:
   
   .. c:autostruct:: logger_t
      :members:
   
   Functions
   ---------
   
   Initialization
   ~~~~~~~~~~~~~~
   
   .. c:autofunction:: logger_create
   
   Logging
   ~~~~~~~
   
   .. c:autofunction:: logger_log
   
   Cleanup
   ~~~~~~~
   
   .. c:autofunction:: logger_destroy
   
   Example Usage
   -------------
   
   .. code-block:: c
   
      #include "logger.h"
      
      int main() {
          // Create logger
          logger_t *log = logger_create(stdout, LOG_INFO);
          
          // Log messages
          logger_log(log, LOG_INFO, "Starting application");
          logger_log(log, LOG_WARNING, "Configuration file not found");
          logger_log(log, LOG_ERROR, "Failed to connect: %s", error);
          
          // Cleanup
          logger_destroy(log);
          return 0;
      }

Documentation Styles
--------------------

Doxygen Style
~~~~~~~~~~~~~

.. code-block:: c

   /**
    * @brief Short description
    * @param x First parameter
    * @param y Second parameter
    * @return Return value description
    */

Javadoc Style
~~~~~~~~~~~~~

.. code-block:: c

   /**
    * Short description
    *
    * Detailed description goes here
    *
    * @param x First parameter
    * @param y Second parameter
    * @return Return value description
    */

Qt Style
~~~~~~~~

.. code-block:: c

   /*!
    * \brief Short description
    * \param x First parameter
    * \param y Second parameter
    * \return Return value description
    */

Configuration Options
---------------------

.. code-block:: python

   # conf.py
   
   # Source directories
   c_autodoc_roots = ['src/', 'include/']
   
   # File patterns
   c_autodoc_include_patterns = ['*.h', '*.hpp']
   c_autodoc_exclude_patterns = ['*_private.h']
   
   # Comment parsing
   c_autodoc_comment_style = 'doxygen'  # or 'javadoc', 'qt'
   
   # Private members
   c_autodoc_show_private = False
   
   # Generate module index
   c_autodoc_generate_index = True

Directive Options
-----------------

.. code-block:: rst

   .. c:autofunction:: my_function
      :no-index:
      :no-signature:
   
   .. c:autostruct:: my_struct
      :members:
      :undoc-members:
      :private-members:

Cross-References
----------------

.. code-block:: rst

   The :c:func:`factorial` function is used by :c:func:`calculate_power`.
   
   See :c:type:`config_t` for configuration options.
   
   Status codes are defined in :c:enum:`status_code_t`.

Benefits
--------

1. **Automatic Generation**: No manual API documentation needed
2. **Stay in Sync**: Docs update with code changes
3. **Consistent Format**: Standardized documentation style
4. **IDE Integration**: Works with Doxygen-compatible editors
5. **Cross-Language**: Mix with Python autodoc

Learn More
----------

For complete C documentation features, see:

- :doc:`../tutorials/packages/sphinx-c-autodoc` - Full tutorial
- `Doxygen Manual <https://www.doxygen.nl/manual/>`_ - Comment syntax
- `Sphinx C Domain <https://www.sphinx-doc.org/en/master/usage/domains/c.html>`_ - C domain reference

Additional Resources
--------------------

- :doc:`doxygen-usage` - Full-featured C/C++ documentation
- :doc:`doxygen-breathe-exhale` - Doxygen + Sphinx integration
- :doc:`../sphinx-basics` - Sphinx fundamentals
- `Doxygen Comment Style <https://www.doxygen.nl/manual/docblocks.html>`_
