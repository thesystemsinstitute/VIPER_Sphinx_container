Sphinx2Doxygen Tutorial
=======================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx2doxygen/>`_
   - `API Documentation <../../pdoc/sphinx2doxygen/index.html>`_
   - `Manual <https://github.com/phn/sphinx2doxygen>`_
   - :doc:`Working Example <../../examples/sphinx2doxygen-example>`


.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinx2doxygen to convert Sphinx-style Python docstrings to Doxygen format, enabling integration between Python and C/C++ documentation.

What is Sphinx2Doxygen?
------------------------
sphinx2doxygen is a conversion tool that:

- Converts Sphinx-style docstrings to Doxygen format
- Enables unified documentation for mixed Python/C++ projects
- Generates Doxygen-compatible documentation from Python code
- Bridges the gap between Python and C/C++ documentation systems
- Supports reStructuredText to Doxygen comment conversion
- Facilitates documentation consistency across languages

sphinx2doxygen bridges the gap between Python documentation (Sphinx) and C/C++ documentation (Doxygen), allowing you to:

- Export Sphinx documentation to Doxygen XML format
- Integrate Python API docs with C++ projects
- Maintain unified documentation across languages
- Generate cross-referenced documentation


Use Cases
---------

- Python extensions written in C/C++
- Mixed-language projects requiring unified documentation
- Migrating from Sphinx to Doxygen
- Generating Doxygen docs for Python code
- Creating cross-language API references

Installation
------------

sphinx2doxygen is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinx2doxygen; print('Installed')"

Basic Usage
-----------

Command-Line Interface
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Convert a single Python file
   docker run --rm -v $(pwd):/project kensai-sphinx:latest \
       sphinx2doxygen /project/mymodule.py

   # Convert multiple files
   docker run --rm -v $(pwd):/project kensai-sphinx:latest \
       sphinx2doxygen /project/module1.py /project/module2.py

   # Convert entire directory
   docker run --rm -v $(pwd):/project kensai-sphinx:latest \
       sphinx2doxygen -r /project/src/

   # Specify output directory
   docker run --rm -v $(pwd):/project kensai-sphinx:latest \
       sphinx2doxygen -o /project/doxygen_output /project/src/

Python API
~~~~~~~~~~

.. code-block:: python

   from sphinx2doxygen import convert_file, convert_string
   
   # Convert a file
   convert_file('mymodule.py', 'output.dox')
   
   # Convert docstring directly
   sphinx_docstring = '''
   Brief description.
   
   :param x: Parameter description
   :type x: int
   :return: Return description
   :rtype: str
   '''
   
   doxygen_output = convert_string(sphinx_docstring)

Docstring Conversion
--------------------

Sphinx Format (Input)
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   def process_data(data, threshold=0.5, verbose=False):
       """
       Process input data with optional threshold.
       
       This function analyzes the input data and applies
       filtering based on the threshold value.
       
       :param data: Input data to process
       :type data: list or numpy.ndarray
       :param threshold: Filtering threshold
       :type threshold: float
       :param verbose: Enable verbose output
       :type verbose: bool
       :return: Processed data
       :rtype: numpy.ndarray
       :raises ValueError: If data is empty
       :raises TypeError: If data is not iterable
       
       Example::
       
           result = process_data([1, 2, 3], threshold=0.7)
       
       .. note::
           This function requires numpy.
       
       .. warning::
           Large datasets may require significant memory.
       """
       pass

Doxygen Format (Output)
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

   /**
    * @brief Process input data with optional threshold.
    *
    * This function analyzes the input data and applies
    * filtering based on the threshold value.
    *
    * @param data Input data to process
    * @param threshold Filtering threshold
    * @param verbose Enable verbose output
    * @return Processed data
    * @throws ValueError If data is empty
    * @throws TypeError If data is not iterable
    *
    * Example:
    * @code{.py}
    * result = process_data([1, 2, 3], threshold=0.7)
    * @endcode
    *
    * @note This function requires numpy.
    * @warning Large datasets may require significant memory.
    */
   void process_data(data, threshold=0.5, verbose=False);

Supported Conversions
---------------------

Parameters and Returns
~~~~~~~~~~~~~~~~~~~~~~

Sphinx:

.. code-block:: python

   """
   :param name: User name
   :type name: str
   :param age: User age
   :type age: int
   :return: User object
   :rtype: User
   """

Doxygen:

.. code-block:: cpp

   /**
    * @param name User name
    * @param age User age
    * @return User object
    */

Exceptions
~~~~~~~~~~

Sphinx:

.. code-block:: python

   """
   :raises ValueError: If input is invalid
   :raises IOError: If file cannot be read
   """

Doxygen:

.. code-block:: cpp

   /**
    * @throws ValueError If input is invalid
    * @throws IOError If file cannot be read
    */

Class Documentation
~~~~~~~~~~~~~~~~~~~

Sphinx:

.. code-block:: python

   class DataProcessor:
       """
       Main data processor class.
       
       :ivar name: Processor name
       :vartype name: str
       :ivar config: Configuration object
       :vartype config: Config
       """

Doxygen:

.. code-block:: cpp

   /**
    * @brief Main data processor class.
    *
    * @var name Processor name
    * @var config Configuration object
    */

Notes and Warnings
~~~~~~~~~~~~~~~~~~

Sphinx:

.. code-block:: python

   """
   .. note::
       This is a note.
   
   .. warning::
       This is a warning.
   
   .. seealso::
       :func:`other_function`
   """

Doxygen:

.. code-block:: cpp

   /**
    * @note This is a note.
    * @warning This is a warning.
    * @see other_function
    */

Configuration Options
---------------------

Command-Line Options
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   sphinx2doxygen [OPTIONS] INPUT [INPUT...]

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Option
     - Description
   * - ``-o, --output DIR``
     - Output directory for converted files
   * - ``-r, --recursive``
     - Recursively process directories
   * - ``-e, --extension EXT``
     - Output file extension (default: .dox)
   * - ``--include-private``
     - Include private members (leading underscore)
   * - ``--format FORMAT``
     - Output format (doxygen, javadoc)
   * - ``-v, --verbose``
     - Verbose output
   * - ``--dry-run``
     - Show what would be converted without writing

Python API Options
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from sphinx2doxygen import Converter
   
   converter = Converter(
       include_private=False,
       format='doxygen',
       verbose=True,
       preserve_blank_lines=True,
       convert_code_blocks=True,
   )
   
   result = converter.convert_file('input.py', 'output.dox')

Docker Integration
------------------

Automated Conversion in Dockerfile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create ``Dockerfile``:

.. code-block:: dockerfile

   FROM kensai-sphinx:latest
   
   # Copy Python source
   COPY src/python /project/python
   
   # Convert to Doxygen
   RUN sphinx2doxygen -r -o /project/doxygen_py /project/python
   
   # Copy C++ source
   COPY src/cpp /project/cpp
   
   # Generate Doxygen docs
   COPY docs/Doxyfile /project/
   RUN doxygen /project/Doxyfile
   
   # Copy to web server
   RUN cp -r /project/docs/html /var/www/html/

Docker Compose
~~~~~~~~~~~~~~

``docker-compose.yml``:

.. code-block:: yaml

   version: '3.8'
   
   services:
     convert:
       image: kensai-sphinx:latest
       volumes:
         - ./src:/project/src
         - ./docs:/project/docs
       command: >
         sh -c "sphinx2doxygen -r -o /project/docs/doxygen_py /project/src/python &&
                doxygen /project/docs/Doxyfile"

Run:

.. code-block:: bash

   docker-compose run --rm convert

Advanced Usage
--------------

Custom Conversion Rules
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from sphinx2doxygen import Converter, Rule
   
   # Define custom rule
   class CustomParamRule(Rule):
       def apply(self, text):
           # Custom transformation
           return text.replace(':parameter:', '@param')
   
   # Add to converter
   converter = Converter()
   converter.add_rule(CustomParamRule())
   converter.convert_file('input.py', 'output.dox')

Batch Processing
~~~~~~~~~~~~~~~~

.. code-block:: python

   from pathlib import Path
   from sphinx2doxygen import convert_file
   
   def batch_convert(source_dir, output_dir):
       source = Path(source_dir)
       output = Path(output_dir)
       output.mkdir(exist_ok=True)
       
       for py_file in source.rglob('*.py'):
           relative = py_file.relative_to(source)
           out_file = output / relative.with_suffix('.dox')
           out_file.parent.mkdir(parents=True, exist_ok=True)
           
           print(f"Converting {py_file} -> {out_file}")
           convert_file(str(py_file), str(out_file))
   
   batch_convert('src/python', 'docs/doxygen_py')

Integration with Breathe
~~~~~~~~~~~~~~~~~~~~~~~~~

After conversion, use with Breathe:

``conf.py``:

.. code-block:: python

   extensions = ['breathe']
   
   breathe_projects = {
       "MyProject": "./doxygen/xml",
       "PythonAPI": "./doxygen_py/xml"
   }
   
   breathe_default_project = "MyProject"

In RST files:

.. code-block:: rst

   Python API
   ==========
   
   .. doxygenfunction:: process_data
      :project: PythonAPI

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Generate Documentation
   
   on: [push]
   
   jobs:
     docs:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Convert Python to Doxygen
           run: |
             docker run --rm -v $(pwd):/project \
               kensai-sphinx:latest \
               sphinx2doxygen -r -o /project/docs/doxygen_py /project/src/python
         
         - name: Generate Doxygen Documentation
           run: |
             docker run --rm -v $(pwd):/project \
               kensai-sphinx:latest \
               doxygen /project/docs/Doxyfile

GitLab CI
~~~~~~~~~

.. code-block:: yaml

   generate-docs:
     image: kensai-sphinx:latest
     script:
       - sphinx2doxygen -r -o docs/doxygen_py src/python
       - doxygen docs/Doxyfile
     artifacts:
       paths:
         - docs/html

Common Issues and Solutions
---------------------------

Conversion Errors
~~~~~~~~~~~~~~~~~

**Issue:** Some docstrings don't convert properly

**Solution:** Ensure docstrings follow Sphinx conventions:

.. code-block:: python

   # Wrong
   def func(x):
       """x: the input"""  # Missing :param:
   
   # Correct
   def func(x):
       """
       :param x: The input
       """

Missing Type Information
~~~~~~~~~~~~~~~~~~~~~~~~

**Issue:** Type information lost in conversion

**Solution:** Always specify types:

.. code-block:: python

   """
   :param data: Input data
   :type data: list[int]  # Include type
   """

Complex Formatting
~~~~~~~~~~~~~~~~~~

**Issue:** Complex reST formatting doesn't convert

**Solution:** Use simpler formatting or post-process:

.. code-block:: python

   # Avoid complex tables, nested directives
   # Keep formatting simple for Doxygen compatibility

Best Practices
--------------

1. **Consistent Docstring Style**
   
   Use standard Sphinx conventions throughout:
   
   .. code-block:: python
   
      def example(param1, param2):
          """
          Brief description.
          
          Longer description here.
          
          :param param1: Description
          :type param1: type
          :param param2: Description
          :type param2: type
          :return: Description
          :rtype: type
          """

2. **Separate Concerns**
   
   Keep Python and C++ documentation in separate directories

3. **Automate Conversion**
   
   Run conversion as part of build process, not manually

4. **Validate Output**
   
   Always check converted Doxygen files for correctness

5. **Version Control**
   
   Don't commit generated .dox files - generate on build

6. **Test Both Systems**
   
   Ensure documentation works in both Sphinx and Doxygen

Troubleshooting
---------------

Installation Issues
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Verify installation
   docker run --rm kensai-sphinx:latest pip show sphinx2doxygen

Encoding Problems
~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Specify encoding
   convert_file('input.py', 'output.dox', encoding='utf-8')

Import Errors
~~~~~~~~~~~~~

.. code-block:: bash

   # Ensure Python path is correct
   docker run --rm -v $(pwd):/project \
     -e PYTHONPATH=/project/src \
     kensai-sphinx:latest \
     sphinx2doxygen /project/src/module.py

Next Steps
----------

1. Convert your Python modules to Doxygen format
2. Integrate with existing Doxygen documentation
3. Set up automated conversion in your build process
4. Explore :doc:`doxygen-breathe-exhale` for complete workflow
5. Check :doc:`breathe` for Sphinx-Doxygen integration

Additional Resources
--------------------

- :doc:`doxygen-usage` - Doxygen basics
- :doc:`doxygen-breathe-exhale` - Complete C++ documentation workflow
- :doc:`breathe` - Breathe extension tutorial
- `Doxygen Manual <https://www.doxygen.nl/manual/>`_
- `Sphinx Documentation <https://www.sphinx-doc.org/>`_
