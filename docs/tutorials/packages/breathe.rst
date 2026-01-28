Breathe Tutorial
================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/breathe/>`_
   - `Official Documentation <https://breathe.readthedocs.io/>`_
   - :doc:`See Working Example <../../examples/breathe-example>`


This tutorial demonstrates how to use Breathe to integrate Doxygen-generated documentation into Sphinx.

What is Breathe?
----------------

Breathe is a Sphinx extension that provides:

- Doxygen XML integration
- C/C++ documentation
- API documentation from source
- Automatic class/function docs
- Inheritance diagrams
- Cross-referencing
- Code signature display
- Namespace documentation
- Template support
- Multiple project support

This bridges Doxygen (C/C++ documentation) with Sphinx (Python documentation), allowing unified documentation.

Installation
------------

Breathe is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import breathe; print('Installed')"

Prerequisites
-------------

Breathe requires Doxygen to generate XML output first. Doxygen must be installed separately.

Check Doxygen installation:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest doxygen --version

Configuration
-------------

Basic Setup
~~~~~~~~~~~

1. Generate Doxygen XML
2. Configure Breathe in Sphinx

``Doxyfile``:

.. code-block:: text

   # Doxygen configuration
   GENERATE_XML = YES
   XML_OUTPUT = xml

``docs/conf.py``:

.. code-block:: python

   extensions = [
       'breathe',
   ]
   
   # Breathe configuration
   breathe_projects = {
       "myproject": "../build/doxygen/xml"
   }
   breathe_default_project = "myproject"

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['breathe']
   
   # Projects configuration
   breathe_projects = {
       "myproject": "../build/doxygen/xml",
       "mylib": "../lib/doxygen/xml",
   }
   
   breathe_default_project = "myproject"
   
   # Display options
   breathe_default_members = ('members', 'undoc-members')
   breathe_show_define_initializer = True
   breathe_show_enumvalue_initializer = True
   
   # Domains
   breathe_domain_by_extension = {
       "h": "cpp",
       "hpp": "cpp",
       "c": "c",
   }
   
   # Implementation details
   breathe_implementation_filename_extensions = ['.c', '.cc', '.cpp']

Basic Usage
-----------

Document a Class
~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. doxygenclass:: MyClass
      :members:
      :protected-members:
      :private-members:

Document a Function
~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. doxygenfunction:: processData

Document a Namespace
~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. doxygennamespace:: MyNamespace
      :members:

Practical Examples
------------------

Example 1: C++ Library Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``include/calculator.hpp``:

.. code-block:: cpp

   #ifndef CALCULATOR_HPP
   #define CALCULATOR_HPP
   
   /**
    * @brief A simple calculator class
    * 
    * This class provides basic arithmetic operations.
    */
   class Calculator {
   public:
       /**
        * @brief Add two numbers
        * @param a First number
        * @param b Second number
        * @return Sum of a and b
        */
       int add(int a, int b);
       
       /**
        * @brief Subtract two numbers
        * @param a First number
        * @param b Second number
        * @return Difference of a and b
        */
       int subtract(int a, int b);
       
       /**
        * @brief Multiply two numbers
        * @param a First number
        * @param b Second number
        * @return Product of a and b
        */
       int multiply(int a, int b);
   
   private:
       int result_;  ///< Last calculation result
   };
   
   #endif // CALCULATOR_HPP

``Doxyfile``:

.. code-block:: text

   PROJECT_NAME = "Calculator"
   INPUT = include
   RECURSIVE = YES
   GENERATE_HTML = NO
   GENERATE_XML = YES
   XML_OUTPUT = ../docs/doxygen/xml

``docs/api.rst``:

.. code-block:: rst

   API Reference
   =============
   
   Calculator Class
   ----------------
   
   .. doxygenclass:: Calculator
      :members:
      :private-members:
   
   This class provides basic arithmetic operations.
   
   Usage Example
   ~~~~~~~~~~~~~
   
   .. code-block:: cpp
      
      Calculator calc;
      int result = calc.add(5, 3);  // result = 8

``docs/conf.py``:

.. code-block:: python

   extensions = ['breathe']
   
   breathe_projects = {
       "calculator": "./doxygen/xml"
   }
   breathe_default_project = "calculator"

Example 2: Complete API Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``include/api/client.h``:

.. code-block:: c

   /**
    * @file client.h
    * @brief Client API for network operations
    */
   
   #ifndef CLIENT_H
   #define CLIENT_H
   
   /**
    * @brief Client connection structure
    */
   typedef struct {
       int socket;       ///< Socket file descriptor
       char* hostname;   ///< Remote hostname
       int port;         ///< Remote port
   } Client;
   
   /**
    * @brief Connect to a remote server
    * 
    * @param client Pointer to client structure
    * @param host Hostname to connect to
    * @param port Port number
    * @return 0 on success, -1 on error
    */
   int client_connect(Client* client, const char* host, int port);
   
   /**
    * @brief Send data to server
    * 
    * @param client Pointer to client structure
    * @param data Data buffer to send
    * @param length Length of data
    * @return Number of bytes sent, -1 on error
    */
   int client_send(Client* client, const void* data, size_t length);
   
   /**
    * @brief Close client connection
    * 
    * @param client Pointer to client structure
    */
   void client_close(Client* client);
   
   #endif // CLIENT_H

``docs/api/client.rst``:

.. code-block:: rst

   Client API
   ==========
   
   The client API provides functions for network communication.
   
   Data Structures
   ---------------
   
   .. doxygenstruct:: Client
      :members:
   
   Functions
   ---------
   
   Connection Management
   ~~~~~~~~~~~~~~~~~~~~~
   
   .. doxygenfunction:: client_connect
   
   .. doxygenfunction:: client_close
   
   Data Transfer
   ~~~~~~~~~~~~~
   
   .. doxygenfunction:: client_send
   
   Example Usage
   -------------
   
   .. code-block:: c
      
      #include "api/client.h"
      
      int main() {
          Client client;
          
          if (client_connect(&client, "example.com", 8080) == 0) {
              const char* message = "Hello, Server!";
              client_send(&client, message, strlen(message));
              client_close(&client);
          }
          
          return 0;
      }

Example 3: Namespace Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``include/utils/string.hpp``:

.. code-block:: cpp

   /**
    * @namespace utils
    * @brief Utility functions
    */
   namespace utils {
   
   /**
    * @namespace utils::string
    * @brief String manipulation utilities
    */
   namespace string {
   
   /**
    * @brief Convert string to uppercase
    * @param str Input string
    * @return Uppercase string
    */
   std::string toUpper(const std::string& str);
   
   /**
    * @brief Convert string to lowercase
    * @param str Input string
    * @return Lowercase string
    */
   std::string toLower(const std::string& str);
   
   /**
    * @brief Trim whitespace from string
    * @param str Input string
    * @return Trimmed string
    */
   std::string trim(const std::string& str);
   
   } // namespace string
   } // namespace utils

``docs/api/utils.rst``:

.. code-block:: rst

   Utilities
   =========
   
   String Utilities
   ----------------
   
   .. doxygennamespace:: utils::string
      :members:
   
   All Utilities
   -------------
   
   .. doxygennamespace:: utils
      :members:
      :undoc-members:

Example 4: Mixed C++ and Python Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/conf.py``:

.. code-block:: python

   extensions = [
       'breathe',
       'sphinx.ext.autodoc',
   ]
   
   # C++ documentation via Breathe
   breathe_projects = {
       "cpplib": "./doxygen/xml"
   }
   breathe_default_project = "cpplib"

``docs/api/index.rst``:

.. code-block:: rst

   API Reference
   =============
   
   This documentation covers both Python and C++ APIs.
   
   Python API
   ----------
   
   .. automodule:: mymodule
      :members:
      :undoc-members:
   
   C++ Core Library
   ----------------
   
   .. doxygenclass:: CoreEngine
      :members:
   
   The C++ core engine is wrapped by the Python API above.

Advanced Features
-----------------

Custom Domains
~~~~~~~~~~~~~~

.. code-block:: python

   breathe_domain_by_extension = {
       "h": "c",
       "hpp": "cpp",
       "hxx": "cpp",
   }

Multiple Projects
~~~~~~~~~~~~~~~~~

.. code-block:: python

   breathe_projects = {
       "core": "./doxygen/core/xml",
       "plugins": "./doxygen/plugins/xml",
   }

.. code-block:: rst

   Core Library
   ------------
   
   .. doxygenclass:: CoreClass
      :project: core
      :members:
   
   Plugin API
   ----------
   
   .. doxygenclass:: PluginInterface
      :project: plugins
      :members:

Selective Member Display
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. doxygenclass:: MyClass
      :members: publicMethod, importantMethod
      :exclude-members: internalMethod

Inheritance Diagrams
~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. doxygenclass:: DerivedClass
      :members:
   
   .. inheritance-diagram:: DerivedClass
      :parts: 2

Docker Integration
------------------

Complete Build Pipeline
~~~~~~~~~~~~~~~~~~~~~~~~

``Dockerfile.docs``:

.. code-block:: dockerfile

   FROM kensai-sphinx:latest
   
   # Install Doxygen
   RUN apk add --no-cache doxygen graphviz
   
   WORKDIR /project
   
   # Build script
   COPY build-docs.sh /usr/local/bin/
   RUN chmod +x /usr/local/bin/build-docs.sh
   
   CMD ["build-docs.sh"]

``build-docs.sh``:

.. code-block:: bash

   #!/bin/sh
   set -e
   
   # Generate Doxygen XML
   echo "Generating Doxygen XML..."
   cd /project
   doxygen Doxyfile
   
   # Build Sphinx documentation
   echo "Building Sphinx documentation..."
   sphinx-build -b html docs docs/_build/html
   
   echo "Documentation built successfully!"

Build and Run:

.. code-block:: bash

   docker build -f Dockerfile.docs -t myproject-docs .
   docker run --rm -v $(pwd):/project myproject-docs

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Build C++ Documentation
   
   on: [push]
   
   jobs:
     docs:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Install Doxygen
           run: sudo apt-get install -y doxygen graphviz
         
         - name: Generate Doxygen XML
           run: doxygen Doxyfile
         
         - name: Build Sphinx Docs
           run: |
             docker run --rm -v $(pwd):/project \
               kensai-sphinx:latest \
               sphinx-build -b html /project/docs /project/docs/_build/html
         
         - name: Deploy
           uses: peaceiris/actions-gh-pages@v3
           with:
             github_token: ${{ secrets.GITHUB_TOKEN }}
             publish_dir: ./docs/_build/html

Makefile Integration
~~~~~~~~~~~~~~~~~~~~

.. code-block:: makefile

   .PHONY: docs clean doxygen
   
   docs: doxygen sphinx
   
   doxygen:
   	doxygen Doxyfile
   
   sphinx:
   	docker run --rm -v $(PWD):/project \
   		kensai-sphinx:latest \
   		sphinx-build -b html /project/docs /project/docs/_build/html
   
   clean:
   	rm -rf docs/_build docs/doxygen

Best Practices
--------------

1. **Document C++ Code**
   
   Use Doxygen comments consistently

2. **Organize by Module**
   
   Separate documentation by component

3. **Include Examples**
   
   Show usage examples

4. **Version Control XML**
   
   Or regenerate in CI/CD

5. **Cross-Reference**
   
   Link between C++ and Python docs

6. **Keep Synchronized**
   
   Regenerate Doxygen regularly

Troubleshooting
---------------

XML Not Found
~~~~~~~~~~~~~

**Solution:**

Check Doxygen generated XML:

.. code-block:: bash

   ls docs/doxygen/xml

Verify path in conf.py:

.. code-block:: python

   breathe_projects = {
       "myproject": "./doxygen/xml"  # Relative to conf.py
   }

Class Not Documented
~~~~~~~~~~~~~~~~~~~~

**Solution:**

Ensure Doxygen processed the file:

.. code-block:: text

   # Doxyfile
   INPUT = include src
   RECURSIVE = YES

Missing Members
~~~~~~~~~~~~~~~

**Solution:**

Enable member documentation:

.. code-block:: rst

   .. doxygenclass:: MyClass
      :members:
      :undoc-members:

Build Errors
~~~~~~~~~~~~

**Solution:**

Check Doxygen warnings:

.. code-block:: bash

   doxygen Doxyfile 2>&1 | grep -i warning

Next Steps
----------

1. Install and configure Doxygen
2. Add Doxygen comments to code
3. Configure Breathe in Sphinx
4. Generate and test documentation
5. Integrate with CI/CD

Additional Resources
--------------------

- :doc:`exhale` - Automatic C++ API page generation
- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `Breathe Documentation <https://breathe.readthedocs.io/>`_
- `Doxygen Documentation <https://www.doxygen.nl/manual/>`_
