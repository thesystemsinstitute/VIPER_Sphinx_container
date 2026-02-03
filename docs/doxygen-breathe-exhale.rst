C++ Documentation in Sphinx
===========================

This tutorial shows how to create professional C++ API documentation by combining Doxygen with Sphinx using the breathe and exhale extensions.

Overview
--------

**The workflow:**

1. **Doxygen** - Extracts documentation from C++ source code and generates XML output
2. **Breathe** - Sphinx extension that reads Doxygen XML and creates reStructuredText directives
3. **Exhale** - Automatically generates Sphinx pages for your entire C++ API
4. **Sphinx** - Builds the final HTML documentation with your custom content

This integration gives you:

- Beautiful, searchable HTML documentation
- Automatic API reference pages for all classes/functions
- Mix C++ API docs with tutorials, guides, and examples
- Cross-references between C++ code and Sphinx docs
- Consistent theme and styling

Prerequisites
-------------

This container includes:

- Doxygen (C++ documentation generator)
- Graphviz (for diagrams)
- breathe (Sphinx ↔ Doxygen bridge)
- exhale (automatic API page generation)
- Sphinx and themes

Project Structure
-----------------

Recommended directory layout:

.. code-block:: text

   my_cpp_project/
   ├── include/
   │   └── mylib/
   │       ├── calculator.h
   │       └── utils.h
   ├── src/
   │   ├── calculator.cpp
   │   └── utils.cpp
   ├── docs/
   │   ├── conf.py          # Sphinx configuration
   │   ├── index.rst        # Main documentation page
   │   ├── api/             # Generated API docs (by exhale)
   │   └── tutorials/       # Your custom tutorials
   ├── Doxyfile             # Doxygen configuration
   └── README.md

Step 1: Prepare C++ Code with Doxygen Comments
-----------------------------------------------

Add Doxygen comments to your C++ code:

**include/mylib/calculator.h:**

.. code-block:: cpp

   /**
    * @file calculator.h
    * @brief Mathematical calculator utilities
    */
   
   #ifndef CALCULATOR_H
   #define CALCULATOR_H
   
   /**
    * @namespace mylib
    * @brief Main library namespace
    */
   namespace mylib {
   
   /**
    * @class Calculator
    * @brief Performs basic mathematical operations
    * 
    * This class provides methods for common arithmetic operations
    * with built-in overflow protection and error handling.
    */
   class Calculator {
   public:
       /**
        * @brief Constructor
        * @param precision Number of decimal places for results
        */
       Calculator(int precision = 2);
       
       /**
        * @brief Adds two numbers
        * @param a First operand
        * @param b Second operand
        * @return Sum of a and b
        * @throws std::overflow_error if result exceeds limits
        */
       double add(double a, double b);
       
       /**
        * @brief Multiplies two numbers
        * @param a First operand
        * @param b Second operand
        * @return Product of a and b
        */
       double multiply(double a, double b);
       
       /**
        * @brief Divides two numbers
        * @param numerator The dividend
        * @param denominator The divisor
        * @return Result of division
        * @throws std::invalid_argument if denominator is zero
        */
       double divide(double numerator, double denominator);
   
   private:
       int precision_;  ///< Number of decimal places for results
   };
   
   }  // namespace mylib
   
   #endif  // CALCULATOR_H

Step 2: Configure Doxygen for XML Output
-----------------------------------------

Generate a Doxyfile:

.. code-block:: bash

   docker run --rm -v $(pwd):/project kensai-sphinx:latest \
       sh -c "cd /project && doxygen -g"

Edit **Doxyfile** with these critical settings:

.. code-block:: text

   # Project information
   PROJECT_NAME           = "My C++ Library"
   PROJECT_BRIEF          = "A powerful C++ mathematical library"
   PROJECT_NUMBER         = "1.0.0"
   
   # Input configuration
   INPUT                  = include src
   RECURSIVE              = YES
   FILE_PATTERNS          = *.h *.hpp *.cpp
   EXCLUDE_PATTERNS       = */test/* */build/*
   
   # Output configuration - CRITICAL for Breathe
   GENERATE_HTML          = NO
   GENERATE_LATEX         = NO
   GENERATE_XML           = YES
   XML_OUTPUT             = xml
   
   # Enhanced documentation extraction
   EXTRACT_ALL            = YES
   EXTRACT_PRIVATE        = YES
   EXTRACT_STATIC         = YES
   
   # Graphviz/Dot diagrams
   HAVE_DOT               = YES
   CLASS_DIAGRAMS         = YES
   COLLABORATION_GRAPH    = YES
   INCLUDE_GRAPH          = YES
   CALL_GRAPH             = YES
   CALLER_GRAPH           = YES
   
   # Preprocessor
   ENABLE_PREPROCESSING   = YES
   MACRO_EXPANSION        = YES

Step 3: Configure Sphinx with Breathe and Exhale
-------------------------------------------------

Create **docs/conf.py**:

.. code-block:: python

   # Project information
   project = 'My C++ Library'
   author = 'Your Name'
   release = '1.0.0'
   
   # Extensions
   extensions = [
       'breathe',
       'exhale',
       'sphinx.ext.autodoc',
       'sphinx.ext.intersphinx',
       'sphinx.ext.viewcode',
   ]
   
   # Breathe configuration
   breathe_projects = {
       "MyCppProject": "../xml"  # Path to Doxygen XML output
   }
   breathe_default_project = "MyCppProject"
   
   # Exhale configuration
   exhale_args = {
       # Required arguments
       "containmentFolder":     "./api",
       "rootFileName":          "library_root.rst",
       "doxygenStripFromPath":  "..",
       # Suggested optional arguments
       "rootFileTitle":         "C++ API Reference",
       "afterTitleDescription": "Complete API documentation for My C++ Library",
       # Doxygen configuration
       "createTreeView":        True,
       "exhaleExecutesDoxygen": True,
       "exhaleDoxygenStdin":    """
           INPUT = ../include ../src
           GENERATE_XML = YES
           XML_OUTPUT = ../xml
           RECURSIVE = YES
           FILE_PATTERNS = *.h *.hpp *.cpp
           EXTRACT_ALL = YES
           HAVE_DOT = YES
           CLASS_DIAGRAMS = YES
       """
   }
   
   # HTML theme
   html_theme = 'sphinx_rtd_theme'
   html_static_path = ['_static']
   
   # Syntax highlighting
   pygments_style = 'sphinx'

**Alternative:** If you prefer to run Doxygen separately:

.. code-block:: python

   # Exhale configuration without executing Doxygen
   exhale_args = {
       "containmentFolder":     "./api",
       "rootFileName":          "library_root.rst",
       "doxygenStripFromPath":  "..",
       "rootFileTitle":         "C++ API Reference",
       "createTreeView":        True,
       "exhaleExecutesDoxygen": False,  # Run Doxygen manually
   }

Step 4: Create Main Documentation Page
---------------------------------------

Create **docs/index.rst**:

.. code-block:: rst

   My C++ Library Documentation
   =============================
   
   Welcome to My C++ Library - a comprehensive mathematical toolkit for C++.
   
   .. toctree::
      :maxdepth: 2
      :caption: Contents:
      
      introduction
      installation
      tutorials/index
      api/library_root
      changelog
   
   Quick Example
   -------------
   
   .. code-block:: cpp
   
      #include <mylib/calculator.h>
      
      int main() {
          mylib::Calculator calc(2);
          double result = calc.add(10.5, 20.3);
          // result = 30.80
          return 0;
      }
   
   Features
   --------
   
   * **High Performance**: Optimized mathematical operations
   * **Type Safe**: Modern C++ with strong typing
   * **Well Tested**: Comprehensive test coverage
   * **Cross Platform**: Works on Windows, Linux, macOS
   
   API Documentation
   -----------------
   
   See the :doc:`api/library_root` for complete API reference.
   
   Indices and tables
   ==================
   
   * :ref:`genindex`
   * :ref:`search`

Step 5: Build the Documentation
--------------------------------

Build with exhale executing Doxygen:

.. code-block:: bash

   docker run --rm -v $(pwd):/project kensai-sphinx:latest \
       sh -c "cd /project/docs && sphinx-build -b html . _build/html"

Or build with separate Doxygen step:

.. code-block:: bash

   # First run Doxygen
   docker run --rm -v $(pwd):/project kensai-sphinx:latest \
       sh -c "cd /project && doxygen Doxyfile"
   
   # Then build Sphinx
   docker run --rm -v $(pwd):/project kensai-sphinx:latest \
       sh -c "cd /project/docs && sphinx-build -b html . _build/html"

View the documentation:

.. code-block:: bash

   # Open docs/_build/html/index.html in your browser

Using Breathe Directives
-------------------------

Breathe provides directives to include specific C++ elements in your Sphinx docs:

Document a Class
~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. doxygenclass:: mylib::Calculator
      :members:
      :protected-members:
      :private-members:

Document a Function
~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. doxygenfunction:: mylib::Calculator::add

Document a File
~~~~~~~~~~~~~~~

.. code-block:: rst

   .. doxygenfile:: calculator.h

Document a Namespace
~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. doxygennamespace:: mylib
      :members:

Cross-Referencing
~~~~~~~~~~~~~~~~~

Reference C++ elements from anywhere in your docs:

.. code-block:: rst

   See :cpp:class:`mylib::Calculator` for the main API.
   
   Use :cpp:func:`mylib::Calculator::divide` to perform division.

Advanced Exhale Configuration
------------------------------

Customizing the API Tree
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   exhale_args = {
       # ... other settings ...
       
       # Customize page structure
       "listingExclude": [r".*Private.*"],  # Exclude private classes
       "unabridgedOrphanKinds": {"file", "dir"},
       
       # File page customization
       "includeTemplateParamOrderList": True,
       "minifyTreeView": False,
       
       # Custom CSS
       "customSpecificationsMapping": {
           "template": [".. cpp:function::"]
       },
   }

Full Example Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Complete conf.py with all options
   import os
   import sys
   
   # Project information
   project = 'My C++ Library'
   copyright = '2026, Your Name'
   author = 'Your Name'
   version = '1.0'
   release = '1.0.0'
   
   # Extensions
   extensions = [
       'breathe',
       'exhale',
       'sphinx.ext.autodoc',
       'sphinx.ext.intersphinx',
       'sphinx.ext.viewcode',
       'sphinx.ext.todo',
       'sphinx_copybutton',
   ]
   
   # Breathe
   breathe_projects = {"MyCppLib": "./xml"}
   breathe_default_project = "MyCppLib"
   breathe_default_members = ('members', 'undoc-members')
   
   # Exhale
   exhale_args = {
       "containmentFolder": "./api",
       "rootFileName": "library_root.rst",
       "doxygenStripFromPath": "..",
       "rootFileTitle": "C++ API Reference",
       "afterTitleDescription": "Full API documentation",
       "createTreeView": True,
       "exhaleExecutesDoxygen": True,
       "exhaleDoxygenStdin": """
           INPUT = ../include
           GENERATE_XML = YES
           XML_OUTPUT = ./xml
           RECURSIVE = YES
           EXTRACT_ALL = YES
           HAVE_DOT = YES
       """
   }
   
   # Theme
   html_theme = 'sphinx_rtd_theme'
   html_theme_options = {
       'navigation_depth': 4,
       'collapse_navigation': False,
   }

Docker Compose Workflow
-----------------------

Create **docker-compose.yml** for easy rebuilds:

.. code-block:: yaml

   version: '3.8'
   
   services:
     docs:
       image: kensai-sphinx:latest
       volumes:
         - ./:/project
       working_dir: /project/docs
       command: sphinx-build -b html . _build/html
       ports:
         - "8000:8000"
     
     docs-watch:
       image: kensai-sphinx:latest
       volumes:
         - ./:/project
       working_dir: /project/docs
       command: sphinx-autobuild -b html . _build/html --host 0.0.0.0 --port 8000
       ports:
         - "8000:8000"

Build and serve:

.. code-block:: bash

   # One-time build
   docker-compose run --rm docs
   
   # Live reload server
   docker-compose up docs-watch

Troubleshooting
---------------

Common Issues
~~~~~~~~~~~~~

**Issue**: Breathe can't find XML files

.. code-block:: text

   Solution: Ensure GENERATE_XML = YES and XML_OUTPUT path is correct

**Issue**: Exhale doesn't generate API pages

.. code-block:: text

   Solution: Check exhaleExecutesDoxygen is True or run Doxygen manually first

**Issue**: Missing class diagrams

.. code-block:: text

   Solution: Verify HAVE_DOT = YES and Graphviz is installed (it is in this container)

**Issue**: Build takes too long

.. code-block:: text

   Solution: Set EXTRACT_ALL = NO and document only what you need

Next Steps
----------

- See :doc:`doxygen-usage` for standalone Doxygen usage
- Explore :doc:`../examples/api-docs` for Python API documentation
- Check `Breathe Documentation <https://breathe.readthedocs.io/>`_
- Check `Exhale Documentation <https://exhale.readthedocs.io/>`_
- Check `Doxygen Manual <https://www.doxygen.nl/manual/>`_

Complete Example
----------------

Download a complete working example:

.. code-block:: bash

   # Clone example repository (fictional)
   git clone https://github.com/example/cpp-breathe-exhale-demo.git
   cd cpp-breathe-exhale-demo
   
   # Build docs
   docker run --rm -v $(pwd):/project kensai-sphinx:latest \
       sh -c "cd /project/docs && sphinx-build -b html . _build/html"
