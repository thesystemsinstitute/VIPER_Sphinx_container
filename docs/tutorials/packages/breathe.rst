Breathe Tutorial
================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/breathe/>`_
   - `API Documentation <../../pdoc/breathe/index.html>`_
   - `Manual <https://breathe.readthedocs.io/>`_
   - :doc:`Working Example <../../examples/breathe-example>`


.. contents:: Table of Contents
   :local:
   :depth: 2

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

Breathe allows you to use Sphinx's documentation system while leveraging Doxygen's superior C/C++ parsing capabilities.

Key Features
~~~~~~~~~~~~

**Doxygen Integration**

- Import Doxygen XML output
- Support for C, C++, C#, IDL
- Automatic API documentation
- Cross-referencing support

**Sphinx Directives**

- Function documentation
- Class hierarchies
- File documentation
- Group/namespace documentation

**Customization**

- Output filtering
- Member selection
- Documentation styling
- Link configuration


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


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Basic Sphinx Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   # Enable breathe extension
   extensions = ['breathe']
   
   # Breathe configuration
   breathe_projects = {
       "MyProject": "./doxyxml/"
   }
   breathe_default_project = "MyProject"

Doxygen Configuration
~~~~~~~~~~~~~~~~~~~~~

Create a ``Doxyfile``:

.. code-block:: text

   # Doxyfile
   PROJECT_NAME           = "MyProject"
   OUTPUT_DIRECTORY       = docs/doxygen
   GENERATE_HTML          = NO
   GENERATE_XML           = YES
   XML_OUTPUT             = xml
   
   # Input settings
   INPUT                  = src/
   RECURSIVE              = YES
   FILE_PATTERNS          = *.c *.cpp *.h *.hpp
   
   # Extraction settings
   EXTRACT_ALL            = YES
   EXTRACT_PRIVATE        = YES
   EXTRACT_STATIC         = YES

Advanced Breathe Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py - Advanced settings
   breathe_projects = {
       "MyProject": "./doxyxml/",
       "SubProject": "./other_doxyxml/"
   }
   
   breathe_default_project = "MyProject"
   
   # Default settings for directives
   breathe_default_members = ('members', 'undoc-members')
   
   # Domain configuration
   breathe_domain_by_extension = {
       "h": "cpp",
       "cpp": "cpp",
   }
   
   # Debug options
   breathe_debug_trace_directives = False
   breathe_debug_trace_doxygen_ids = False

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
