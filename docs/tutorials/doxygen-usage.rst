Using Doxygen from the Container
==================================

This tutorial demonstrates how to use Doxygen from within the Sphinx container to generate documentation for C, C++, and other supported languages.

What is Doxygen?
----------------

Doxygen is a documentation generator that creates documentation from annotated source code. It supports multiple programming languages including:

- C, C++, C#, Objective-C
- Python, Java, PHP
- IDL, Fortran
- VHDL

The container includes Doxygen along with Graphviz for generating diagrams.

Checking Doxygen Installation
------------------------------

To verify Doxygen is installed in the container:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest doxygen --version

Basic Doxygen Usage
-------------------

Running Doxygen on Your Code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To run Doxygen on your source code:

1. Mount your project directory to the container
2. Generate a Doxyfile configuration
3. Run Doxygen

.. code-block:: bash

   # Mount your project and generate Doxyfile
   docker run --rm -v /path/to/your/project:/project kensai-sphinx:latest \
       sh -c "cd /project && doxygen -g"
   
   # Run Doxygen to generate documentation
   docker run --rm -v /path/to/your/project:/project kensai-sphinx:latest \
       sh -c "cd /project && doxygen Doxyfile"

Example: Documenting C++ Code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a simple C++ file with Doxygen comments:

**example.cpp:**

.. code-block:: cpp

   /**
    * @file example.cpp
    * @brief Example C++ code with Doxygen documentation
    * @author Your Name
    * @date 2026-01-25
    */
   
   /**
    * @class Calculator
    * @brief A simple calculator class
    */
   class Calculator {
   public:
       /**
        * @brief Adds two numbers
        * @param a First number
        * @param b Second number
        * @return Sum of a and b
        */
       int add(int a, int b) {
           return a + b;
       }
       
       /**
        * @brief Multiplies two numbers
        * @param a First number
        * @param b Second number
        * @return Product of a and b
        */
       int multiply(int a, int b) {
           return a * b;
       }
   };

Create a **Doxyfile** configuration:

.. code-block:: bash

   docker run --rm -v $(pwd):/project kensai-sphinx:latest \
       sh -c "cd /project && doxygen -g"

Edit the Doxyfile to set key parameters:

.. code-block:: text

   PROJECT_NAME           = "My C++ Project"
   OUTPUT_DIRECTORY       = docs
   INPUT                  = .
   RECURSIVE              = YES
   GENERATE_HTML          = YES
   GENERATE_LATEX         = NO
   HAVE_DOT               = YES
   CALL_GRAPH             = YES
   CALLER_GRAPH           = YES

Generate the documentation:

.. code-block:: bash

   docker run --rm -v $(pwd):/project kensai-sphinx:latest \
       sh -c "cd /project && doxygen"

The HTML documentation will be in ``docs/html/index.html``.

Doxygen Configuration Options
------------------------------

Key Doxyfile Settings
~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Option
     - Description
   * - PROJECT_NAME
     - Name of your project
   * - OUTPUT_DIRECTORY
     - Where to put generated documentation
   * - INPUT
     - Source directories to document
   * - FILE_PATTERNS
     - File extensions to process (*.cpp, *.h, etc.)
   * - RECURSIVE
     - Process subdirectories recursively
   * - EXTRACT_ALL
     - Extract documentation even without comments
   * - GENERATE_HTML
     - Generate HTML output
   * - GENERATE_LATEX
     - Generate LaTeX/PDF output
   * - HAVE_DOT
     - Use Graphviz dot for diagrams
   * - CALL_GRAPH
     - Generate call dependency graphs
   * - CALLER_GRAPH
     - Generate caller dependency graphs

Graphviz Integration
~~~~~~~~~~~~~~~~~~~~

The container includes Graphviz, which Doxygen uses to generate diagrams:

- Class hierarchies
- Collaboration diagrams
- Include dependency graphs
- Call/caller graphs

Enable in Doxyfile:

.. code-block:: text

   HAVE_DOT               = YES
   CLASS_DIAGRAMS         = YES
   COLLABORATION_GRAPH    = YES
   INCLUDE_GRAPH          = YES
   INCLUDED_BY_GRAPH      = YES
   CALL_GRAPH             = YES
   CALLER_GRAPH           = YES

Using Doxygen with Docker Compose
----------------------------------

Create a **docker-compose.yml** for repeated documentation builds:

.. code-block:: yaml

   version: '3.8'
   
   services:
     doxygen:
       image: kensai-sphinx:latest
       volumes:
         - ./:/project
       working_dir: /project
       command: doxygen Doxyfile

Run with:

.. code-block:: bash

   docker-compose run --rm doxygen

Advanced: Integrating with Sphinx
----------------------------------

For integrating Doxygen documentation into Sphinx, see:

- :doc:`doxygen-breathe-exhale` - Full tutorial on Sphinx + Doxygen integration using breathe and exhale

Next Steps
----------

- See :doc:`doxygen-breathe-exhale` for integrating Doxygen with Sphinx
- Explore :doc:`../examples/graphviz` for diagram generation
- Check the `Doxygen Manual <https://www.doxygen.nl/manual/>`_ for comprehensive documentation

Common Commands Reference
--------------------------

.. code-block:: bash

   # Generate default Doxyfile
   docker run --rm -v $(pwd):/project kensai-sphinx:latest \
       sh -c "cd /project && doxygen -g"
   
   # Generate documentation
   docker run --rm -v $(pwd):/project kensai-sphinx:latest \
       sh -c "cd /project && doxygen"
   
   # Check Doxygen version
   docker run --rm kensai-sphinx:latest doxygen --version
   
   # Run Doxygen with specific config file
   docker run --rm -v $(pwd):/project kensai-sphinx:latest \
       sh -c "cd /project && doxygen MyDoxyfile"
