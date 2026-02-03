Breathe Tutorial
================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/breathe/>`_
   - `API Documentation <../../pdoc/breathe/index.html>`_
   - `Manual <https://breathe.readthedocs.io/>`_

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

   docker run --rm viper-sphinx:latest python -c "import breathe; print('Installed')"

Prerequisites
-------------

Breathe requires Doxygen to generate XML output first. Doxygen must be installed separately.

Check Doxygen installation:

.. code-block:: bash

   docker run --rm viper-sphinx:latest doxygen --version

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

   FROM viper-sphinx:latest
   
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
               viper-sphinx:latest \
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
   		viper-sphinx:latest \
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


Practical Examples
------------------

Installation
------------

Basic Installation
~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   pip install breathe

The extension is already installed in this environment:

.. code-block:: python

   import breathe
   print(f"Breathe version: {breathe.__version__}")

Doxygen Requirement
~~~~~~~~~~~~~~~~~~~

Breathe requires Doxygen to be installed:

.. code-block:: bash

   # Ubuntu/Debian
   sudo apt-get install doxygen
   
   # macOS
   brew install doxygen
   
   # Windows
   choco install doxygen.install

Configuration
-------------

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

Workflow Setup
--------------

Build Process
~~~~~~~~~~~~~

Typical documentation build workflow:

.. code-block:: bash

   # Step 1: Run Doxygen
   doxygen Doxyfile
   
   # Step 2: Build Sphinx documentation
   cd docs
   make html

Automated Build
~~~~~~~~~~~~~~~

Using Make:

.. code-block:: makefile

   # Makefile
   .PHONY: doxygen sphinx clean
   
   all: doxygen sphinx
   
   doxygen:
   	doxygen Doxyfile
   
   sphinx:
   	cd docs && make html
   
   clean:
   	rm -rf docs/doxygen
   	cd docs && make clean

CMake Integration
~~~~~~~~~~~~~~~~~

.. code-block:: cmake

   # CMakeLists.txt
   find_package(Doxygen REQUIRED)
   find_package(Sphinx REQUIRED)
   
   # Doxygen target
   set(DOXYGEN_OUTPUT_DIR ${CMAKE_CURRENT_BINARY_DIR}/doxygen)
   configure_file(Doxyfile.in ${CMAKE_CURRENT_BINARY_DIR}/Doxyfile @ONLY)
   
   add_custom_target(doxygen
       COMMAND ${DOXYGEN_EXECUTABLE} ${CMAKE_CURRENT_BINARY_DIR}/Doxyfile
       WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
       COMMENT "Generating Doxygen XML"
   )
   
   # Sphinx target depends on Doxygen
   add_custom_target(docs
       COMMAND ${SPHINX_EXECUTABLE} -b html ${CMAKE_SOURCE_DIR}/docs ${CMAKE_BINARY_DIR}/docs/html
       DEPENDS doxygen
       COMMENT "Building Sphinx documentation"
   )

Breathe Directives
------------------

Function Documentation
~~~~~~~~~~~~~~~~~~~~~~

The ``doxygenfunction`` directive:

.. code-block:: rst

   .. doxygenfunction:: calculateSum
      :project: MyProject

This renders function documentation including:

- Function signature
- Parameter descriptions
- Return value documentation
- Detailed description

Class Documentation
~~~~~~~~~~~~~~~~~~~

The ``doxygenclass`` directive:

.. code-block:: rst

   .. doxygenclass:: MyClass
      :project: MyProject
      :members:
      :private-members:
      :undoc-members:

Options:

- ``:members:`` - Include member functions
- ``:private-members:`` - Include private members
- ``:protected-members:`` - Include protected members
- ``:undoc-members:`` - Include undocumented members

Struct Documentation
~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. doxygenstruct:: Point
      :project: MyProject
      :members:

Documenting structs with all fields.

File Documentation
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. doxygenfile:: utility.h
      :project: MyProject

Includes all documentation from a header file.

Namespace Documentation
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. doxygennamespace:: MyNamespace
      :project: MyProject
      :members:
      :content-only:

Group Documentation
~~~~~~~~~~~~~~~~~~~

Doxygen groups (modules):

.. code-block:: rst

   .. doxygengroup:: MathFunctions
      :project: MyProject
      :members:
      :content-only:

Enum Documentation
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. doxygenenum:: Status
      :project: MyProject

Typedef Documentation
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. doxygentypedef:: ErrorCode
      :project: MyProject

Variable Documentation
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. doxygenvariable:: globalCounter
      :project: MyProject

C++ Examples
------------

Simple Function
~~~~~~~~~~~~~~~

**C++ Header** (``math.h``):

.. code-block:: cpp

   /**
    * @brief Calculates the sum of two integers
    * @param a First integer
    * @param b Second integer
    * @return Sum of a and b
    */
   int add(int a, int b);

**Sphinx Documentation**:

.. code-block:: rst

   Mathematical Functions
   ======================
   
   .. doxygenfunction:: add

Class with Methods
~~~~~~~~~~~~~~~~~~

**C++ Header** (``vector.h``):

.. code-block:: cpp

   /**
    * @brief A 3D vector class
    */
   class Vector3 {
   public:
       /**
        * @brief Default constructor
        */
       Vector3();
       
       /**
        * @brief Construct vector from components
        * @param x X component
        * @param y Y component
        * @param z Z component
        */
       Vector3(double x, double y, double z);
       
       /**
        * @brief Calculate magnitude
        * @return Length of vector
        */
       double magnitude() const;
       
   private:
       double x_, y_, z_; ///< Vector components
   };

**Sphinx Documentation**:

.. code-block:: rst

   Vector3 Class
   =============
   
   .. doxygenclass:: Vector3
      :members:

Template Class
~~~~~~~~~~~~~~

**C++ Header**:

.. code-block:: cpp

   /**
    * @brief Generic container class
    * @tparam T Type of elements
    */
   template<typename T>
   class Container {
   public:
       /**
        * @brief Add element to container
        * @param element Element to add
        */
       void add(const T& element);
       
       /**
        * @brief Get number of elements
        * @return Element count
        */
       size_t size() const;
   };

**Sphinx Documentation**:

.. code-block:: rst

   .. doxygenclass:: template<typename T> Container
      :members:

Namespace Example
~~~~~~~~~~~~~~~~~

**C++ Header**:

.. code-block:: cpp

   /**
    * @namespace geometry
    * @brief Geometric utility functions
    */
   namespace geometry {
       /**
        * @brief Calculate circle area
        * @param radius Circle radius
        * @return Area
        */
       double circleArea(double radius);
       
       /**
        * @brief Calculate rectangle area
        * @param width Rectangle width
        * @param height Rectangle height
        * @return Area
        */
       double rectangleArea(double width, double height);
   }

**Sphinx Documentation**:

.. code-block:: rst

   Geometry Functions
   ==================
   
   .. doxygennamespace:: geometry
      :members:

Advanced Features
-----------------

Member Selection
~~~~~~~~~~~~~~~~

Control which members to include:

.. code-block:: rst

   .. doxygenclass:: MyClass
      :members: publicMethod, anotherMethod
      :private-members: privateHelper
      :protected-members:

Outlining Only
~~~~~~~~~~~~~~

Show only declarations without details:

.. code-block:: rst

   .. doxygenclass:: MyClass
      :outline:
      :members:

Combining Multiple Items
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   API Reference
   =============
   
   .. doxygennamespace:: api
   
   .. doxygenclass:: api::Client
      :members:
   
   .. doxygenclass:: api::Server
      :members:

Custom Projects
~~~~~~~~~~~~~~~

Switch between multiple Doxygen projects:

.. code-block:: rst

   .. doxygenclass:: MainClass
      :project: MainProject
   
   .. doxygenclass:: PluginClass
      :project: PluginProject

Best Practices
--------------

Documentation Comments
~~~~~~~~~~~~~~~~~~~~~~

Use Doxygen-style comments in C++:

.. code-block:: cpp

   /**
    * @brief Brief description (single line)
    *
    * Detailed description can span multiple lines
    * and include additional information.
    *
    * @param paramName Description of parameter
    * @return Description of return value
    * @throws ExceptionType When this exception is thrown
    * @see relatedFunction()
    */
   int myFunction(int paramName);

Alternative styles:

.. code-block:: cpp

   /// Brief description
   /// @param x Parameter description
   /// @return Return description
   int function(int x);
   
   //! Brief description
   //! @param x Parameter description
   int function2(int x);

Organizing Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~

Use Doxygen groups for organization:

.. code-block:: cpp

   /**
    * @defgroup math Mathematical Functions
    * @{
    */
   
   /// Add two numbers
   int add(int a, int b);
   
   /// Subtract two numbers
   int subtract(int a, int b);
   
   /** @} */ // end of math group

In Sphinx:

.. code-block:: rst

   .. doxygengroup:: math
      :content-only:

Cross-References
~~~~~~~~~~~~~~~~

Link between Doxygen and Sphinx content:

.. code-block:: rst

   The :cpp:class:`MyClass` provides functionality for...
   
   See :cpp:func:`processData` for more information.

Filtering Output
~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   breathe_default_members = ('members',)
   
   # Show only public members by default
   # Override per-directive with :private-members: etc.

Troubleshooting
---------------

XML Not Found
~~~~~~~~~~~~~

.. code-block:: python

   # Ensure Doxygen XML path is correct
   breathe_projects = {
       "MyProject": "./path/to/xml/"  # Should contain index.xml
   }

.. code-block:: bash

   # Verify XML was generated
   ls ./path/to/xml/index.xml

Directive Errors
~~~~~~~~~~~~~~~~

Enable debug output:

.. code-block:: python

   # conf.py
   breathe_debug_trace_directives = True
   breathe_debug_trace_doxygen_ids = True

.. code-block:: bash

   # Rebuild with verbose output
   sphinx-build -v -b html . _build/html

Symbol Not Found
~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Ensure Doxygen processed the file
   grep "symbolName" doxyxml/index.xml
   
   # Check Doxygen warnings
   doxygen Doxyfile 2>&1 | grep -i warning

Integration Patterns
--------------------

Read the Docs
~~~~~~~~~~~~~

.. code-block:: yaml

   # .readthedocs.yml
   version: 2
   
   build:
     os: ubuntu-22.04
     tools:
       python: "3.11"
     apt_packages:
       - doxygen
     
     jobs:
       pre_build:
         - doxygen Doxyfile
   
   sphinx:
     configuration: docs/conf.py

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   # .github/workflows/docs.yml
   name: Documentation
   
   on: [push]
   
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v2
         
         - name: Install Doxygen
           run: sudo apt-get install -y doxygen
         
         - name: Generate Doxygen XML
           run: doxygen Doxyfile
         
         - name: Install Python deps
           run: pip install sphinx breathe
         
         - name: Build docs
           run: cd docs && make html

Docker Build
~~~~~~~~~~~~

.. code-block:: dockerfile

   FROM python:3.11
   
   # Install Doxygen
   RUN apt-get update && apt-get install -y doxygen
   
   # Install Python packages
   RUN pip install sphinx breathe
   
   # Copy source
   COPY . /app
   WORKDIR /app
   
   # Generate docs
   RUN doxygen Doxyfile
   RUN cd docs && make html

Additional Resources
--------------------
- :doc:`exhale` - Automatic C++ API page generation
- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `Breathe Documentation <https://breathe.readthedocs.io/>`_
- `Doxygen Documentation <https://www.doxygen.nl/manual/>`_
**Related Extensions**:
- :doc:`exhale-example` - Automatic hierarchy generation
- :doc:`sphinx-autodoc-defaultargs-example` - Python autodoc
- :doc:`sphinx-c-autodoc-example` - Pure C documentation
**External Resources**:
- `Doxygen Manual <https://www.doxygen.nl/manual/>`_
- `Doxygen XML Output <https://www.doxygen.nl/manual/xmlcmds.html>`_
Summary
-------
Breathe provides seamless Doxygen-Sphinx integration:
**Key Capabilities**:
✅ Import Doxygen XML documentation
✅ Support C, C++, C#, IDL
✅ Comprehensive directive set
✅ Automatic API documentation
✅ Cross-referencing support
**Common Use Cases**:
- C++ library documentation
- Mixed Python/C++ projects
- Existing Doxygen migration
- API reference generation
- Cross-language documentation
Breathe is essential for projects that need to document C/C++ code within the Sphinx ecosystem.

