Sphinx2Doxygen Example
======================

This page demonstrates the **sphinx2doxygen** extension which converts Sphinx documentation to Doxygen format for integration with C/C++ documentation systems.

What is sphinx2doxygen?
-----------------------

sphinx2doxygen bridges the gap between Python documentation (Sphinx) and C/C++ documentation (Doxygen), allowing you to:

- Export Sphinx documentation to Doxygen XML format
- Integrate Python API docs with C++ projects
- Maintain unified documentation across languages
- Generate cross-referenced documentation

Basic Configuration
-------------------

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx2doxygen',
       # ... other extensions
   ]
   
   # Doxygen output directory
   sphinx2doxygen_output = '_doxygen'
   
   # XML format for Doxygen
   sphinx2doxygen_format = 'xml'

Example: Converting Python Documentation
-----------------------------------------

**Python Module** (``mymodule.py``):

.. code-block:: python

   """MyModule - Core functionality
   
   This module provides essential features for the application.
   """
   
   class DataProcessor:
       """Process and transform data.
       
       This class handles all data transformation operations
       including validation, normalization, and conversion.
       
       :param config: Configuration dictionary
       :type config: dict
       """
       
       def __init__(self, config):
           """Initialize the processor."""
           self.config = config
       
       def process(self, data):
           """Process the input data.
           
           :param data: Input data to process
           :type data: list
           :return: Processed data
           :rtype: list
           :raises ValueError: If data is invalid
           
           Example:
               >>> processor = DataProcessor({})
               >>> result = processor.process([1, 2, 3])
           """
           if not data:
               raise ValueError("Data cannot be empty")
           return [x * 2 for x in data]

**Sphinx Documentation** (``api.rst``):

.. code-block:: rst

   API Reference
   =============
   
   .. automodule:: mymodule
      :members:
      :undoc-members:
      :show-inheritance:

**Generated Doxygen XML Output**:

.. code-block:: xml

   <?xml version="1.0" encoding="UTF-8"?>
   <doxygen version="1.9.1">
     <compounddef id="classDataProcessor" kind="class">
       <compoundname>DataProcessor</compoundname>
       <briefdescription>
         <para>Process and transform data.</para>
       </briefdescription>
       <detaileddescription>
         <para>This class handles all data transformation operations
         including validation, normalization, and conversion.</para>
         <parameterlist kind="param">
           <parameteritem>
             <parameternamelist>
               <parametername>config</parametername>
             </parameternamelist>
             <parameterdescription>
               <para>Configuration dictionary</para>
             </parameterdescription>
           </parameteritem>
         </parameterlist>
       </detaileddescription>
       <sectiondef kind="public-func">
         <memberdef kind="function" id="process">
           <name>process</name>
           <type>list</type>
           <definition>process</definition>
           <briefdescription>
             <para>Process the input data.</para>
           </briefdescription>
         </memberdef>
       </sectiondef>
     </compounddef>
   </doxygen>

Integration Example
-------------------

**Doxyfile Configuration**:

.. code-block:: text

   # Import Sphinx-generated XML
   INPUT = docs/_doxygen/xml src/
   
   # Enable XML input
   XML_INPUT = docs/_doxygen/xml
   
   # Generate combined documentation
   GENERATE_HTML = YES
   HTML_OUTPUT = html
   
   # Cross-reference configuration
   TAGFILES = sphinx_tags.xml=../sphinx/_build/html

**Build Process**:

.. code-block:: bash

   # 1. Build Sphinx documentation with doxygen export
   sphinx-build -b xml docs/ docs/_build/xml
   
   # 2. Convert to Doxygen format
   sphinx2doxygen docs/_build/xml docs/_doxygen/xml
   
   # 3. Build Doxygen documentation
   doxygen Doxyfile

Use Cases
---------

1. **Mixed Language Projects**
   
   - Python backend with C++ performance modules
   - Unified API documentation across languages
   - Single documentation source

2. **Legacy Integration**
   
   - Adding Python components to existing C++ projects
   - Maintaining consistent documentation style
   - Cross-language API references

3. **Documentation Migration**
   
   - Transitioning from Doxygen to Sphinx
   - Preserving existing Doxygen workflows
   - Gradual migration path

Output Formats
--------------

sphinx2doxygen supports multiple output formats:

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Format
     - Description
   * - XML
     - Doxygen XML format for processing
   * - HTML
     - Direct HTML generation
   * - LaTeX
     - LaTeX output for PDF generation
   * - RTF
     - Rich Text Format documents

Key Features
------------

- **Automatic Conversion**: Seamlessly converts Sphinx RST to Doxygen XML
- **Type Preservation**: Maintains Python type hints in Doxygen format
- **Cross-References**: Preserves links between documentation sections
- **Inheritance Tracking**: Documents class hierarchies correctly
- **Example Preservation**: Maintains code examples and doctests

Learn More
----------

For complete documentation and advanced usage, see:

- :doc:`../tutorials/packages/sphinx2doxygen` - Full tutorial
- `Doxygen Manual <https://www.doxygen.nl/manual/>`_ - Doxygen reference
- `Sphinx Domains <https://www.sphinx-doc.org/en/master/usage/domains/>`_ - Domain documentation
