breathe - Working Example
==========================

This page demonstrates the capabilities of **breathe**, a Sphinx extension that bridges Doxygen documentation with Sphinx, allowing you to document C, C++, C#, and other languages supported by Doxygen.

.. note::

   **About breathe**
   
   breathe is a bridge extension that reads Doxygen XML output and makes it available in Sphinx documentation using custom directives. It's essential for documenting C/C++ projects.
   
   - **Package**: breathe
   - **Purpose**: Doxygen XML to Sphinx integration
   - **Use Case**: C/C++ API documentation in Sphinx
   - **Tutorial**: :doc:`../tutorials/packages/breathe`


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

See Also
--------

**Related Extensions**:

- :doc:`exhale-example` - Automatic hierarchy generation
- :doc:`sphinx-autodoc-defaultargs-example` - Python autodoc
- :doc:`sphinx-c-autodoc-example` - Pure C documentation

**External Resources**:

- `Breathe Documentation <https://breathe.readthedocs.io/>`_
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
