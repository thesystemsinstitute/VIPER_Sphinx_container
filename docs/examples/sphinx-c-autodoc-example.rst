Sphinx-C-Autodoc Example
========================

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
