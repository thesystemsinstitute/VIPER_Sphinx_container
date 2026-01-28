Sphinx-Pyreverse Tutorial
=========================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-pyreverse/>`_
   - :doc:`See Working Example <../../examples/sphinx-pyreverse-example>`


This tutorial demonstrates how to use sphinx-pyreverse to automatically generate UML class diagrams and package diagrams from Python code using Pylint's pyreverse tool.

What is Sphinx-Pyreverse?
--------------------------

sphinx-pyreverse is a Sphinx extension that integrates pyreverse (from Pylint) to automatically generate UML diagrams:

- Class diagrams from Python code
- Package dependency diagrams
- Inheritance hierarchies
- Class relationships and associations
- Method and attribute visualization
- Module structure diagrams
- Automatic diagram generation during build
- SVG, PNG, and PDF output formats

This is invaluable for documenting Python project architecture and class relationships.

Installation
------------

sphinx-pyreverse is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinx_pyreverse; print('Installed')"

**Note:** Pyreverse is included in the pylint package which is already installed.

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_pyreverse',
   ]
   
   # Path to Python source code
   pyreverse_source_paths = ['../src']

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinx_pyreverse']
   
   # Source code paths
   pyreverse_source_paths = ['../src', '../lib']
   pyreverse_exclude_patterns = ['*_test.py', 'test_*']
   
   # Diagram options
   pyreverse_output_format = 'svg'  # or 'png', 'pdf'
   pyreverse_output_dir = '_static/diagrams'
   
   # Class diagram options
   pyreverse_show_attributes = True
   pyreverse_show_methods = True
   pyreverse_show_private = False
   pyreverse_show_magic = False
   pyreverse_show_inheritance = True
   pyreverse_show_associations = True
   
   # Diagram styling
   pyreverse_colorized = True
   pyreverse_max_depth = 3
   pyreverse_font_size = 10
   
   # Filtering
   pyreverse_ignore = ['__pycache__', '.git']
   pyreverse_filter_mode = 'ALL'  # or 'PUB_ONLY', 'SPECIAL'

Basic Usage
-----------

Generate Class Diagram
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. pyreverse:: mymodule
      :type: class
      :caption: Class diagram for mymodule

Generate Package Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. pyreverse:: mypackage
      :type: package
      :caption: Package structure

Specific Classes
~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. pyreverse:: mymodule
      :classes: MyClass, AnotherClass
      :show-inheritance: true

Module Diagram
~~~~~~~~~~~~~~

.. code-block:: rst

   .. pyreverse-module:: mymodule.core
      :show-attributes: true
      :show-methods: true

Practical Examples
------------------

Example 1: Simple Class Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create ``src/data_processor.py``:

.. code-block:: python

   """Data processing module."""
   
   class DataProcessor:
       """Main data processor class."""
       
       def __init__(self, config):
           """Initialize processor.
           
           Args:
               config: Configuration dictionary
           """
           self.config = config
           self._cache = {}
       
       def process(self, data):
           """Process input data.
           
           Args:
               data: Input data to process
               
           Returns:
               Processed data
           """
           return self._transform(data)
       
       def _transform(self, data):
           """Internal transformation method."""
           return data.upper()
   
   
   class DataValidator(DataProcessor):
       """Validates data before processing."""
       
       def validate(self, data):
           """Validate input data.
           
           Args:
               data: Data to validate
               
           Returns:
               bool: True if valid
           """
           return data is not None
       
       def process(self, data):
           """Process with validation."""
           if self.validate(data):
               return super().process(data)
           raise ValueError("Invalid data")

Document in ``docs/api/data_processor.rst``:

.. code-block:: rst

   Data Processor Module
   =====================
   
   This module provides data processing and validation.
   
   Class Diagram
   -------------
   
   .. pyreverse:: data_processor
      :type: class
      :show-inheritance: true
      :show-attributes: true
      :show-methods: true
      :caption: DataProcessor class hierarchy
   
   Classes
   -------
   
   .. automodule:: data_processor
      :members:
      :undoc-members:
      :show-inheritance:
   
   Usage Example
   -------------
   
   .. code-block:: python
   
      from data_processor import DataValidator
      
      validator = DataValidator({'strict': True})
      result = validator.process("hello")

Example 2: Package Architecture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Project structure:

.. code-block:: text

   mylib/
   ├── __init__.py
   ├── core/
   │   ├── __init__.py
   │   ├── processor.py
   │   └── validator.py
   ├── io/
   │   ├── __init__.py
   │   ├── reader.py
   │   └── writer.py
   └── utils/
       ├── __init__.py
       └── helpers.py

``docs/architecture.rst``:

.. code-block:: rst

   Architecture Overview
   =====================
   
   Package Structure
   -----------------
   
   .. pyreverse:: mylib
      :type: package
      :max-depth: 2
      :caption: Package dependency diagram
   
   Core Module
   -----------
   
   .. pyreverse:: mylib.core
      :type: class
      :caption: Core module classes
   
   I/O Module
   ----------
   
   .. pyreverse:: mylib.io
      :type: class
      :caption: I/O module classes
   
   Module Dependencies
   -------------------
   
   The package structure shows clear separation:
   
   - **core**: Main processing logic
   - **io**: Input/output handlers  
   - **utils**: Helper functions
   
   Class Relationships
   -------------------
   
   .. pyreverse:: mylib
      :type: class
      :show-associations: true
      :show-inheritance: true

Example 3: Inheritance Hierarchy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``src/shapes.py``:

.. code-block:: python

   """Geometric shapes module."""
   from abc import ABC, abstractmethod
   import math
   
   class Shape(ABC):
       """Abstract base shape class."""
       
       def __init__(self, color='black'):
           self.color = color
       
       @abstractmethod
       def area(self):
           """Calculate area."""
           pass
       
       @abstractmethod
       def perimeter(self):
           """Calculate perimeter."""
           pass
   
   
   class Rectangle(Shape):
       """Rectangle shape."""
       
       def __init__(self, width, height, color='black'):
           super().__init__(color)
           self.width = width
           self.height = height
       
       def area(self):
           return self.width * self.height
       
       def perimeter(self):
           return 2 * (self.width + self.height)
   
   
   class Square(Rectangle):
       """Square shape (special rectangle)."""
       
       def __init__(self, side, color='black'):
           super().__init__(side, side, color)
   
   
   class Circle(Shape):
       """Circle shape."""
       
       def __init__(self, radius, color='black'):
           super().__init__(color)
           self.radius = radius
       
       def area(self):
           return math.pi * self.radius ** 2
       
       def perimeter(self):
           return 2 * math.pi * self.radius

``docs/shapes.rst``:

.. code-block:: rst

   Shapes Module
   =============
   
   Inheritance Hierarchy
   ---------------------
   
   .. pyreverse:: shapes
      :type: class
      :show-inheritance: true
      :show-attributes: true
      :caption: Shape class hierarchy
   
   The diagram shows:
   
   - ``Shape`` - Abstract base class
   - ``Rectangle`` - Concrete implementation
   - ``Square`` - Specialized rectangle
   - ``Circle`` - Separate concrete implementation
   
   Class Details
   -------------
   
   .. automodule:: shapes
      :members:
      :show-inheritance:

Example 4: Complete Project Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/project_structure.rst``:

.. code-block:: rst

   Project Structure
   =================
   
   High-Level Overview
   -------------------
   
   .. pyreverse:: myproject
      :type: package
      :max-depth: 1
      :caption: Top-level package structure
   
   Core Components
   ---------------
   
   Core Classes
   ~~~~~~~~~~~~
   
   .. pyreverse:: myproject.core
      :type: class
      :show-all: true
      :caption: Core module class diagram
   
   Data Models
   ~~~~~~~~~~~
   
   .. pyreverse:: myproject.models
      :type: class
      :show-inheritance: true
      :caption: Data model classes
   
   Services
   ~~~~~~~~
   
   .. pyreverse:: myproject.services
      :type: class
      :show-associations: true
      :caption: Service layer
   
   Full Class Diagram
   ------------------
   
   .. pyreverse:: myproject
      :type: class
      :max-depth: 3
      :show-inheritance: true
      :show-associations: true
      :caption: Complete class diagram

Advanced Features
-----------------

Filtering Classes
~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. pyreverse:: mymodule
      :classes: ClassA, ClassB
      :exclude: TestClass, MockClass

Custom Output Path
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. pyreverse:: mymodule
      :output: _static/my_diagram.svg

Specific Module
~~~~~~~~~~~~~~~

.. code-block:: rst

   .. pyreverse-module:: package.module
      :depth: 2

All Classes
~~~~~~~~~~~

.. code-block:: rst

   .. pyreverse-all:: myproject
      :show-builtin: false
      :show-stdlib: false

Colorized Diagrams
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   pyreverse_colorized = True
   pyreverse_color_scheme = {
       'class': '#lightblue',
       'interface': '#lightgreen',
       'abstract': '#yellow',
   }

Docker Integration
------------------

Generate Diagrams
~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     kensai-sphinx:latest \
     sphinx-build -b html /project/docs /project/docs/_build/html

Manual Pyreverse
~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Generate class diagram manually
   docker run --rm -v $(pwd):/project kensai-sphinx:latest \
     pyreverse -o svg -p myproject /project/src/myproject

Batch Generation
~~~~~~~~~~~~~~~~

Create ``generate_diagrams.sh``:

.. code-block:: bash

   #!/bin/bash
   
   MODULES=("core" "models" "services" "utils")
   
   for module in "${MODULES[@]}"; do
       echo "Generating diagram for $module..."
       docker run --rm -v $(pwd):/project kensai-sphinx:latest \
           pyreverse -o svg -p $module /project/src/myproject/$module
   done

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Generate UML Diagrams
   
   on:
     push:
       paths:
         - 'src/**'
         - 'docs/**'
   
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Build Docs with Diagrams
           run: |
             docker run --rm -v $(pwd):/project \
               kensai-sphinx:latest \
               sphinx-build -b html /project/docs /project/docs/_build/html

Best Practices
--------------

1. **Keep Code Clean**
   
   Pyreverse works best with well-structured code:
   
   .. code-block:: python
   
      class WellDocumented:
          """Clear docstrings help diagram readability."""
          pass

2. **Limit Diagram Scope**
   
   Don't try to diagram entire large projects:
   
   .. code-block:: rst
   
      .. pyreverse:: myproject.core
         :max-depth: 2

3. **Use Meaningful Names**
   
   Class names appear in diagrams - make them clear

4. **Document Relationships**
   
   Show important relationships:
   
   .. code-block:: rst
   
      .. pyreverse:: mymodule
         :show-inheritance: true
         :show-associations: true

5. **Update Regularly**
   
   Regenerate diagrams when code changes

6. **Organize by Module**
   
   Create separate diagrams for each major module

Common Patterns
---------------

Module Documentation Template
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   {{ module_name }} Module
   ========================
   
   Overview
   --------
   
   Brief description of the module.
   
   Class Diagram
   -------------
   
   .. pyreverse:: {{ module_name }}
      :type: class
      :show-all: true
   
   Classes
   -------
   
   .. automodule:: {{ module_name }}
      :members:

Package Overview Template
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   {{ package_name }} Package
   ==========================
   
   Package Structure
   -----------------
   
   .. pyreverse:: {{ package_name }}
      :type: package
   
   Submodules
   ----------
   
   {% for module in modules %}
   {{ module }}
   ~~~~~~~~~~~
   
   .. pyreverse:: {{ package_name }}.{{ module }}
      :type: class
   {% endfor %}

Troubleshooting
---------------

No Diagrams Generated
~~~~~~~~~~~~~~~~~~~~~

**Solution:**

Check source paths:

.. code-block:: python

   pyreverse_source_paths = ['../src']

Verify path is correct relative to ``conf.py``.

Import Errors
~~~~~~~~~~~~~

**Solution:**

Add source to Python path:

.. code-block:: python

   import sys
   import os
   sys.path.insert(0, os.path.abspath('../src'))

Diagram Too Complex
~~~~~~~~~~~~~~~~~~~

**Solution:**

Limit depth and filter:

.. code-block:: rst

   .. pyreverse:: mymodule
      :max-depth: 2
      :exclude: TestClass, MockClass

SVG Not Displaying
~~~~~~~~~~~~~~~~~~

**Solution:**

Check output format:

.. code-block:: python

   pyreverse_output_format = 'svg'

Low Quality PNG
~~~~~~~~~~~~~~~

**Solution:**

Increase DPI:

.. code-block:: python

   pyreverse_output_format = 'png'
   pyreverse_dpi = 300

Next Steps
----------

1. Configure pyreverse source paths
2. Generate class diagrams for main modules
3. Create package structure diagram
4. Document class relationships
5. Integrate diagram generation into build

Additional Resources
--------------------

- :doc:`sphinx-uml` - PlantUML integration
- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `Pyreverse Documentation <https://pylint.pycqa.org/en/latest/pyreverse.html>`_
- `UML Class Diagrams <https://www.uml-diagrams.org/class-diagrams-overview.html>`_
