Sphinx-Refdoc Tutorial
======================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-refdoc/>`_
   - `API Documentation <../../pdoc/sphinx_refdoc/index.html>`_
   - `Manual <https://github.com/sphinx-contrib/refdoc>`_
   - :doc:`Working Example <../../examples/sphinx-refdoc-example>`


.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinx-refdoc to create and manage reference documentation with enhanced cross-referencing capabilities.

What is Sphinx-Refdoc?
-----------------------
sphinx-refdoc is a Sphinx extension that provides enhanced reference documentation features:

- Advanced cross-referencing between documents
- Automatic reference link generation
- Reference glossaries and indexes
- External reference management
- Reference validation and checking
- Smart reference resolution
- Reference documentation templates
- API reference organization

This is particularly useful for large documentation projects with complex cross-referencing needs.

The sphinx-refdoc extension provides advanced reference documentation features, including automatic reference generation, enhanced cross-referencing, and structured API documentation.


Installation
------------

sphinx-refdoc is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinx_refdoc; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_refdoc',
   ]
   
   # Basic configuration
   refdoc_enabled = True

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinx_refdoc']
   
   # Reference documentation settings
   refdoc_enabled = True
   refdoc_validate_refs = True
   refdoc_warn_broken = True
   
   # Cross-reference options
   refdoc_external_refs = {
       'python': ('https://docs.python.org/3/', None),
       'numpy': ('https://numpy.org/doc/stable/', None),
       'pandas': ('https://pandas.pydata.org/docs/', None),
   }
   
   # Reference templates
   refdoc_templates = {
       'api': 'templates/api_reference.rst',
       'class': 'templates/class_reference.rst',
       'function': 'templates/function_reference.rst',
   }
   
   # Reference index
   refdoc_generate_index = True
   refdoc_index_file = 'references.rst'
   
   # Glossary settings
   refdoc_glossary_enabled = True
   refdoc_glossary_file = 'glossary.rst'


.. code-block:: python

   # Custom reference resolvers
   refdoc_resolvers = {
       'function': 'path.to.function_resolver',
       'class': 'path.to.class_resolver',
   }
   
   # Reference templates
   refdoc_templates = {
       'function': 'templates/function_ref.html',
       'class': 'templates/class_ref.html',
   }
   
   # Cross-reference prefixes
   refdoc_prefixes = {
       'api': 'api/',
       'internal': 'internal/',
   }

Basic Usage
-----------

Creating References
~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. refdoc:: MyClass
      :type: class
      :module: mymodule
      
      This is the MyClass reference documentation.

Referencing Items
~~~~~~~~~~~~~~~~~

.. code-block:: rst

   See :refdoc:`MyClass` for details.
   
   The :refdoc:`calculate_sum` function is documented here.
   
   Refer to :refdoc:`mymodule.MyClass.method` for implementation.

Cross-References
~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. refdoc-xref::
      :target: external_api
      :url: https://external-api.example.com/docs
      
      Link to external API documentation.

Reference Index
~~~~~~~~~~~~~~~

.. code-block:: rst

   .. refdoc-index::
      :sort: alphabetical
      :group-by: type
      
      Automatically generated index of all references.

   API Reference
   =============
   
   This page contains the complete API reference.
   
   .. refdoc-index::
      :type: api
      :sort: module
      
   Core Classes
   ------------
   
   .. refdoc:: DataProcessor
      :type: class
      :module: mylib.core
      
      Main data processing class.
      
      Methods
      ~~~~~~~
      
      .. refdoc:: DataProcessor.process
         :type: method
         
         Process input data.
         
         :param data: Input data
         :type data: dict
         :return: Processed result
         :rtype: dict
      
      .. refdoc:: DataProcessor.validate
         :type: method
         
         Validate input data.
         
         :param data: Data to validate
         :type data: dict
         :return: True if valid
         :rtype: bool

Create ``docs/usage.rst``:

.. code-block:: rst

   Usage Guide
   ===========
   
   To process data, use the :refdoc:`DataProcessor` class:
   
   .. code-block:: python
   
      from mylib.core import DataProcessor
      
      processor = DataProcessor()
      result = processor.process(data)
   
   For validation, see :refdoc:`DataProcessor.validate`.

Example 2: External References
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``conf.py``:

.. code-block:: python

   refdoc_external_refs = {
       'python': ('https://docs.python.org/3/', None),
       'requests': ('https://requests.readthedocs.io/', None),
       'numpy': ('https://numpy.org/doc/stable/', None),
   }

``docs/dependencies.rst``:

.. code-block:: rst

   Dependencies
   ============
   
   This project uses:
   
   - Python standard library
     
     - :refdoc-ext:`dict <python:stdtypes.html#dict>`
     - :refdoc-ext:`list <python:stdtypes.html#list>`
   
   - External packages
     
     - :refdoc-ext:`requests.get <requests:api>`
     - :refdoc-ext:`numpy.array <numpy:reference/generated/numpy.array>`

Example 3: Reference Glossary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create ``docs/glossary.rst``:

.. code-block:: rst

   Glossary
   ========
   
   .. refdoc-glossary::
      :sort: alphabetical
   
   .. refdoc-term:: API
      
      Application Programming Interface. See :refdoc:`api/index` for details.
   
   .. refdoc-term:: Data Processor
      
      A component that transforms input data. Implemented in :refdoc:`DataProcessor`.
   
   .. refdoc-term:: Validation
      
      The process of checking data integrity. See :refdoc:`DataProcessor.validate`.

Use in documentation:

.. code-block:: rst

   The :term:`Data Processor` validates input using :term:`Validation`.
   
   For :term:`API` details, see the reference documentation.

Example 4: Reference Templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create ``templates/class_reference.rst``:

.. code-block:: rst

   {{ class_name }}
   {{ "=" * class_name|length }}
   
   .. currentmodule:: {{ module_name }}
   
   .. autoclass:: {{ class_name }}
      :members:
      :undoc-members:
      :show-inheritance:
   
   Description
   -----------
   
   {{ description }}
   
Advanced Features
-----------------

Reference Validation
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   refdoc_validate_refs = True
   refdoc_warn_broken = True
   refdoc_fail_on_broken = False

This will check all references during build and warn about broken links.

Reference Groups
~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. refdoc-group:: Core API
      :type: class
      
      .. refdoc:: DataProcessor
      .. refdoc:: DataValidator
      .. refdoc:: DataTransformer
   
   .. refdoc-group:: Utilities
      :type: function
      
      .. refdoc:: parse_config
      .. refdoc:: load_data
      .. refdoc:: save_results

Smart Reference Resolution
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   See :refdoc:`process` for details.
   
   # Automatically resolves to:
   # - DataProcessor.process if in DataProcessor context
   # - module.process if at module level
   # - Full path if ambiguous

Reference Inheritance
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. refdoc:: BaseClass
      :type: class
      
      Base class documentation.
   
   .. refdoc:: DerivedClass
      :type: class
      :inherits: BaseClass
      
      Derived class inherits all references from BaseClass.

Complete Documentation Example
-------------------------------

Project Structure
~~~~~~~~~~~~~~~~~

.. code-block:: text

   myproject/
   ├── docs/
   │   ├── conf.py
   │   ├── index.rst
   │   ├── api/
   │   │   ├── index.rst
   │   │   ├── core.rst
   │   │   └── utils.rst
   │   ├── guides/
   │   │   ├── quickstart.rst
   │   │   └── advanced.rst
   │   ├── glossary.rst
   │   └── references.rst
   └── src/
       └── mylib/
           ├── core.py
           └── utils.py

api/index.rst
~~~~~~~~~~~~~

.. code-block:: rst

   API Reference
   =============
   
   Complete API documentation.
   
   .. refdoc-index::
      :group-by: module
      :show-summary: true
   
   Core Module
   -----------
   
   .. toctree::
      :maxdepth: 2
      
      core
      utils

api/core.rst
~~~~~~~~~~~~

.. code-block:: rst

   Core Module
   ===========
   
   .. currentmodule:: mylib.core
   
   Classes
   -------
   
   DataProcessor
   ~~~~~~~~~~~~~
   
   .. refdoc:: DataProcessor
      :type: class
      :module: mylib.core
      
      Main data processing class.
      
      .. refdoc:: DataProcessor.__init__
         :type: method
         
         Initialize the processor.
         
         :param config: Configuration dict
      
      .. refdoc:: DataProcessor.process
         :type: method
         
         Process data.
         
         :param data: Input data
         :return: Processed result

guides/quickstart.rst
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Quick Start
   ===========
   
   Installation
   ------------
   
   .. code-block:: bash
   
      pip install mylib
   
   Basic Usage
   -----------
   
   Import and use the :refdoc:`DataProcessor`:
   
   .. code-block:: python
   
      from mylib.core import DataProcessor
      
      processor = DataProcessor()
      result = processor.process(data)
   
   For more details, see:
   
   - :refdoc:`DataProcessor` - Full API reference
   - :refdoc:`DataProcessor.process` - Process method
   - :term:`Data Processor` - Glossary entry

Docker Integration
------------------

Build Reference Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     kensai-sphinx:latest \
     sphinx-build -b html /project/docs /project/docs/_build/html

Validate References
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     kensai-sphinx:latest \
     sh -c "
       cd /project
       sphinx-build -W -b html docs/ docs/_build/html
     "

Generate Reference Index
~~~~~~~~~~~~~~~~~~~~~~~~

Create ``generate_refs.py``:

.. code-block:: python

   import os
   import re
   from pathlib import Path
   
   def find_references(docs_dir):
       refs = []
       for rst_file in Path(docs_dir).rglob('*.rst'):
           with open(rst_file, 'r') as f:
               content = f.read()
               matches = re.findall(r'\.\. refdoc:: (\w+)', content)
               refs.extend(matches)
       return sorted(set(refs))
   
   refs = find_references('docs')
   
   print("Reference Index")
   print("=" * 50)
   for ref in refs:
       print(f"- {ref}")

Run:

.. code-block:: bash

   docker run --rm -v $(pwd):/project \
     kensai-sphinx:latest \
     python /project/generate_refs.py

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Build and Validate References
   
   on:
     push:
       paths:
         - 'docs/**'
   
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Build Docs
           run: |
             docker run --rm -v $(pwd):/project \
               kensai-sphinx:latest \
               sphinx-build -W -b html /project/docs /project/docs/_build/html
         
         - name: Check References
           run: |
             docker run --rm -v $(pwd):/project \
               kensai-sphinx:latest \
               sphinx-build -b linkcheck /project/docs /project/docs/_build/linkcheck

Best Practices
--------------

1. **Use Consistent Naming**
   
   .. code-block:: rst
   
      .. refdoc:: MyClass  # PascalCase for classes
      .. refdoc:: my_function  # snake_case for functions

2. **Group Related References**
   
   .. code-block:: rst
   
      .. refdoc-group:: Data Processing
         
         .. refdoc:: DataProcessor
         .. refdoc:: DataValidator

3. **Provide Context**
   
   Always include type and module information:
   
   .. code-block:: rst
   
      .. refdoc:: MyClass
         :type: class
         :module: mylib.core

4. **Maintain Glossary**
   
   Keep a central glossary of terms

5. **Validate Regularly**
   
   Enable reference validation in CI/CD

6. **Use Templates**
   
   Create templates for common reference patterns

Common Patterns
---------------

Module Reference
~~~~~~~~~~~~~~~~

.. code-block:: rst

   Module: {{ module_name }}
   ========================
   
   .. refdoc-module:: {{ module_name }}
   
   Classes
   -------
   
   .. refdoc-index::
      :type: class
      :module: {{ module_name }}
   
   Functions
   ---------
   
   .. refdoc-index::
      :type: function
      :module: {{ module_name }}

Function Reference
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. refdoc:: function_name
      :type: function
      :module: mymodule
      
      Brief description.
      
      :param arg1: Description
      :param arg2: Description
      :return: Description
      
      Example::
      
          result = function_name(arg1, arg2)

Class Reference
~~~~~~~~~~~~~~~

.. code-block:: rst

   .. refdoc:: ClassName
      :type: class
      :module: mymodule
      
      Class description.
      
      Attributes
      ----------
      
      .. refdoc:: ClassName.attribute
         :type: attribute
      
      Methods
      -------
      
      .. refdoc:: ClassName.method
         :type: method

Troubleshooting
---------------

Broken References
~~~~~~~~~~~~~~~~~

**Solution:**

Enable validation:

.. code-block:: python

   refdoc_validate_refs = True
   refdoc_warn_broken = True

References Not Linking
~~~~~~~~~~~~~~~~~~~~~~~

**Solution:**

Check reference target exists:

.. code-block:: rst

   # Define before referencing
   .. refdoc:: MyClass
      :type: class
   
   # Then reference
   See :refdoc:`MyClass`

External Links Failing
~~~~~~~~~~~~~~~~~~~~~~~

**Solution:**

Verify external reference configuration:

.. code-block:: python

   refdoc_external_refs = {
       'project': ('https://project.example.com/docs/', None),
   }

Next Steps
----------

1. Set up reference documentation structure
2. Create reference templates
3. Build API reference index
4. Add cross-references throughout documentation
5. Enable reference validation

Additional Resources
--------------------

- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- :doc:`sphinx-autoapi` - Automatic API documentation
- `Sphinx Cross-Referencing <https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html>`_
