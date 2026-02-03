Sphinx-Pyreverse Tutorial
=========================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-pyreverse/>`_
   - `API Documentation <../../pdoc/sphinx_pyreverse/index.html>`_
   - `Manual <https://github.com/alendit/sphinx.ext.pyreverse>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

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

The sphinx-pyreverse extension integrates Pyreverse (from Pylint) to automatically generate UML diagrams from Python source code, including class diagrams, package diagrams, and dependency graphs.


Installation
------------

sphinx-pyreverse is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm viper-sphinx:latest python -c "import sphinx_pyreverse; print('Installed')"

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


.. code-block:: python

   # Diagram styling
   pyreverse_defaults = {
       'show-builtin': False,
       'show-stdlib': False,
       'colorized': True,
       'max-color-depth': 2,
   }
   
   # Class diagram options
   pyreverse_class_defaults = {
       'show-ancestors': 2,  # Show up to 2 levels of ancestors
       'show-associated': 1,  # Show 1 level of associations
       'all-ancestors': False,
       'all-associated': False,
   }
   
   # Package diagram options
   pyreverse_package_defaults = {
       'show-only': [],  # List of modules/packages to show
       'ignore': ['test', 'tests'],  # Ignore test modules
   }

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
     viper-sphinx:latest \
     sphinx-build -b html /project/docs /project/docs/_build/html

Manual Pyreverse
~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Generate class diagram manually
   docker run --rm -v $(pwd):/project viper-sphinx:latest \
     pyreverse -o svg -p myproject /project/src/myproject

Batch Generation
~~~~~~~~~~~~~~~~

Create ``generate_diagrams.sh``:

.. code-block:: bash

   #!/bin/bash
   
   MODULES=("core" "models" "services" "utils")
   
   for module in "${MODULES[@]}"; do
       echo "Generating diagram for $module..."
       docker run --rm -v $(pwd):/project viper-sphinx:latest \
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
               viper-sphinx:latest \
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


Practical Examples
------------------

Basic Class Diagrams
--------------------

Single Class
~~~~~~~~~~~~

.. pyreverse:: mymodule.MyClass
   :type: class
   
   Generates a class diagram for MyClass showing attributes and methods.

Multiple Classes
~~~~~~~~~~~~~~~~

.. pyreverse:: mymodule
   :classes: MyClass, AnotherClass, ThirdClass
   :type: class
   
   Shows class diagram for specific classes in a module.

Module Overview
~~~~~~~~~~~~~~~

.. pyreverse:: mypackage.core
   :type: class
   :all-classes:
   
   Generates class diagram for all classes in the module.

Class Relationships
-------------------

Inheritance Diagram
~~~~~~~~~~~~~~~~~~~

.. pyreverse:: myapp.models
   :type: class
   :show-inheritance:
   
   **Example Python Code**:
   
   .. code-block:: python
   
      class Animal:
          def __init__(self, name):
              self.name = name
          
          def speak(self):
              pass
      
      class Dog(Animal):
          def speak(self):
              return "Woof!"
      
      class Cat(Animal):
          def speak(self):
              return "Meow!"
   
   **Generated Diagram**: Shows Animal as base class with Dog and Cat as subclasses.

Composition and Aggregation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. pyreverse:: myapp.components
   :type: class
   :show-composition:
   :show-aggregation:
   
   **Example Python Code**:
   
   .. code-block:: python
   
      class Engine:
          def __init__(self, horsepower):
              self.horsepower = horsepower
      
      class Wheel:
          def __init__(self, size):
              self.size = size
      
      class Car:
          def __init__(self):
              self.engine = Engine(200)  # Composition
              self.wheels = [Wheel(17) for _ in range(4)]  # Aggregation
   
   **Generated Diagram**: Shows Car containing Engine and Wheels.

Association Diagram
~~~~~~~~~~~~~~~~~~~

.. pyreverse:: myapp.database
   :type: class
   :show-associations:
   
   **Example Python Code**:
   
   .. code-block:: python
   
      class User:
          def __init__(self):
              self.posts = []
          
          def add_post(self, post):
              self.posts.append(post)
      
      class Post:
          def __init__(self, author):
              self.author = author  # Association
   
   **Generated Diagram**: Shows bidirectional association between User and Post.

Package Diagrams
----------------

Package Structure
~~~~~~~~~~~~~~~~~

.. pyreverse:: myproject
   :type: package
   
   Shows package structure and inter-package dependencies.

Module Dependencies
~~~~~~~~~~~~~~~~~~~

.. pyreverse:: myapp
   :type: package
   :show-modules:
   
   Displays modules within packages and their dependencies.

Nested Packages
~~~~~~~~~~~~~~~

.. pyreverse:: myproject.subpackage
   :type: package
   :depth: 3
   
   Shows nested package structure up to 3 levels deep.

Filtering Options
-----------------

Filter by Pattern
~~~~~~~~~~~~~~~~~

.. pyreverse:: myapp
   :filter: Test*,*Helper
   :type: class
   
   Excludes classes matching Test* or *Helper patterns.

Show Only Public
~~~~~~~~~~~~~~~~

.. pyreverse:: mymodule
   :only-public:
   :type: class
   
   Shows only public classes and methods (no underscore prefix).

Filter by Attribute
~~~~~~~~~~~~~~~~~~~

.. pyreverse:: myapp.models
   :show-attributes: public
   :show-methods: public
   :type: class
   
   Shows only public attributes and methods.

Customization Options
---------------------

Detailed Diagrams
~~~~~~~~~~~~~~~~~

.. pyreverse:: mymodule
   :type: class
   :show-attributes:
   :show-methods:
   :show-docstrings:
   
   Shows full class details including docstrings.

Simplified Diagrams
~~~~~~~~~~~~~~~~~~~

.. pyreverse:: myapp
   :type: class
   :no-attributes:
   :no-methods:
   
   Shows only class names and relationships.

Custom Layout
~~~~~~~~~~~~~

.. pyreverse:: myproject
   :type: package
   :layout: dot
   :orientation: TB
   
   Top-to-bottom layout using Graphviz dot engine.

Configuration Examples
----------------------

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx.ext.autodoc',
       'sphinx_pyreverse',
   ]
   
   # Pyreverse configuration
   pyreverse_output_format = 'svg'  # 'svg', 'png', 'pdf', 'dot'
   pyreverse_output_dir = '_pyreverse'

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Diagram styling
   pyreverse_defaults = {
       'show-builtin': False,
       'show-stdlib': False,
       'colorized': True,
       'max-color-depth': 2,
   }
   
   # Class diagram options
   pyreverse_class_defaults = {
       'show-ancestors': 2,  # Show up to 2 levels of ancestors
       'show-associated': 1,  # Show 1 level of associations
       'all-ancestors': False,
       'all-associated': False,
   }
   
   # Package diagram options
   pyreverse_package_defaults = {
       'show-only': [],  # List of modules/packages to show
       'ignore': ['test', 'tests'],  # Ignore test modules
   }

Theme Integration
~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Color scheme
   pyreverse_colors = {
       'class': '#E8F4F8',
       'interface': '#F8E8E8',
       'abstract': '#F8F8E8',
       'association': '#000000',
       'inheritance': '#0000FF',
   }
   
   # Font settings
   pyreverse_font = {
       'name': 'Arial',
       'size': 10,
   }

Integration with Autodoc
------------------------

Automatic Generation
~~~~~~~~~~~~~~~~~~~~

.. automodule:: myapp.models
   :members:
   :no-index:
   
   Automatically generates and includes class diagram with autodoc output.

Combined Documentation
~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: myapp.models.User
   :members:
   :no-index:
   
   **Class Diagram**:
   
   .. pyreverse:: myapp.models.User
      :type: class
      :show-inheritance:
   
   **Documentation**:
   
   The User class represents a registered user...

Practical Examples
------------------

Django Models
~~~~~~~~~~~~~

.. pyreverse:: myproject.models
   :type: class
   :show-inheritance:
   :show-associations:
   
   **Django Model Example**:
   
   .. code-block:: python
   
      from django.db import models
      
      class Author(models.Model):
          name = models.CharField(max_length=100)
          email = models.EmailField()
      
      class Book(models.Model):
          title = models.CharField(max_length=200)
          author = models.ForeignKey(Author, on_delete=models.CASCADE)
          published_date = models.DateField()
      
      class Review(models.Model):
          book = models.ForeignKey(Book, on_delete=models.CASCADE)
          rating = models.IntegerField()
          comment = models.TextField()
   
   **Generated Diagram**: Shows relationships between Author, Book, and Review models.

Flask Application
~~~~~~~~~~~~~~~~~

.. pyreverse:: myapp
   :type: package
   :show-modules:
   
   **Flask App Structure**:
   
   .. code-block:: text
   
      myapp/
      ├── __init__.py
      ├── models.py
      ├── views.py
      ├── forms.py
      └── utils.py
   
   **Generated Diagram**: Shows module dependencies and structure.

Design Patterns
~~~~~~~~~~~~~~~

.. pyreverse:: patterns
   :type: class
   :show-inheritance:
   :show-composition:
   
   **Singleton Pattern**:
   
   .. code-block:: python
   
      class Singleton:
          _instance = None
          
          def __new__(cls):
              if cls._instance is None:
                  cls._instance = super().__new__(cls)
              return cls._instance
   
   **Factory Pattern**:
   
   .. code-block:: python
   
      class Product:
          pass
      
      class ConcreteProductA(Product):
          pass
      
      class ConcreteProductB(Product):
          pass
      
      class Factory:
          def create_product(self, product_type):
              if product_type == 'A':
                  return ConcreteProductA()
              elif product_type == 'B':
                  return ConcreteProductB()
   
   **Generated Diagram**: Visualizes design pattern structure.

Advanced Features
-----------------

Inheritance Depth
~~~~~~~~~~~~~~~~~

.. pyreverse:: myapp.models
   :type: class
   :max-inheritance-depth: 3
   
   Limits inheritance tree display to 3 levels.

Association Level
~~~~~~~~~~~~~~~~~

.. pyreverse:: myapp.services
   :type: class
   :max-association-level: 2
   
   Shows associations up to 2 levels deep.

Clustering
~~~~~~~~~~

.. pyreverse:: myproject
   :type: package
   :cluster-by: module
   
   Groups classes by module in the diagram.

Interactive Diagrams
--------------------

With Links
~~~~~~~~~~

.. pyreverse:: myapp
   :type: class
   :link-to-docs:
   
   Generated diagram includes clickable links to class documentation.

With Tooltips
~~~~~~~~~~~~~

.. pyreverse:: mymodule
   :type: class
   :show-tooltips:
   
   Hovering over classes shows brief descriptions.

Export Options
--------------

Multiple Formats
~~~~~~~~~~~~~~~~

.. pyreverse:: myapp
   :type: class
   :export: svg, png, pdf
   
   Exports diagram in multiple formats.

High Resolution
~~~~~~~~~~~~~~~

.. pyreverse:: mymodule
   :type: class
   :dpi: 300
   :format: png
   
   Generates high-resolution PNG diagram.

Analysis Examples
-----------------

Complexity Analysis
~~~~~~~~~~~~~~~~~~~

.. pyreverse:: myapp
   :type: class
   :complexity-metric:
   
   Highlights classes by complexity level (color-coded).

Coupling Analysis
~~~~~~~~~~~~~~~~~

.. pyreverse:: myproject
   :type: package
   :show-coupling:
   
   Shows coupling between packages and modules.

Cohesion Metrics
~~~~~~~~~~~~~~~~

.. pyreverse:: myapp.services
   :type: class
   :cohesion-metric:
   
   Visualizes class cohesion levels.

Documentation Generation
------------------------

Full Project
~~~~~~~~~~~~

.. pyreverse:: myproject
   :type: both
   :output-dir: diagrams
   
   Generates both class and package diagrams for entire project.

Incremental Updates
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # In conf.py
   pyreverse_cache = True
   pyreverse_incremental = True
   
   # Only regenerates diagrams for changed modules

API Reference Diagrams
~~~~~~~~~~~~~~~~~~~~~~

.. pyreverse:: myapi
   :type: class
   :only-public:
   :show-methods:
   :link-to-docs:
   
   Creates API reference with linked class diagrams.


Practical Examples
------------------

Basic Class Diagrams
--------------------

Single Class
~~~~~~~~~~~~

.. pyreverse:: mymodule.MyClass
   :type: class
   
   Generates a class diagram for MyClass showing attributes and methods.

Multiple Classes
~~~~~~~~~~~~~~~~

.. pyreverse:: mymodule
   :classes: MyClass, AnotherClass, ThirdClass
   :type: class
   
   Shows class diagram for specific classes in a module.

Module Overview
~~~~~~~~~~~~~~~

.. pyreverse:: mypackage.core
   :type: class
   :all-classes:
   
   Generates class diagram for all classes in the module.

Class Relationships
-------------------

Inheritance Diagram
~~~~~~~~~~~~~~~~~~~

.. pyreverse:: myapp.models
   :type: class
   :show-inheritance:
   
   **Example Python Code**:
   
   .. code-block:: python
   
      class Animal:
          def __init__(self, name):
              self.name = name
          
          def speak(self):
              pass
      
      class Dog(Animal):
          def speak(self):
              return "Woof!"
      
      class Cat(Animal):
          def speak(self):
              return "Meow!"
   
   **Generated Diagram**: Shows Animal as base class with Dog and Cat as subclasses.

Composition and Aggregation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. pyreverse:: myapp.components
   :type: class
   :show-composition:
   :show-aggregation:
   
   **Example Python Code**:
   
   .. code-block:: python
   
      class Engine:
          def __init__(self, horsepower):
              self.horsepower = horsepower
      
      class Wheel:
          def __init__(self, size):
              self.size = size
      
      class Car:
          def __init__(self):
              self.engine = Engine(200)  # Composition
              self.wheels = [Wheel(17) for _ in range(4)]  # Aggregation
   
   **Generated Diagram**: Shows Car containing Engine and Wheels.

Association Diagram
~~~~~~~~~~~~~~~~~~~

.. pyreverse:: myapp.database
   :type: class
   :show-associations:
   
   **Example Python Code**:
   
   .. code-block:: python
   
      class User:
          def __init__(self):
              self.posts = []
          
          def add_post(self, post):
              self.posts.append(post)
      
      class Post:
          def __init__(self, author):
              self.author = author  # Association
   
   **Generated Diagram**: Shows bidirectional association between User and Post.

Package Diagrams
----------------

Package Structure
~~~~~~~~~~~~~~~~~

.. pyreverse:: myproject
   :type: package
   
   Shows package structure and inter-package dependencies.

Module Dependencies
~~~~~~~~~~~~~~~~~~~

.. pyreverse:: myapp
   :type: package
   :show-modules:
   
   Displays modules within packages and their dependencies.

Nested Packages
~~~~~~~~~~~~~~~

.. pyreverse:: myproject.subpackage
   :type: package
   :depth: 3
   
   Shows nested package structure up to 3 levels deep.

Filtering Options
-----------------

Filter by Pattern
~~~~~~~~~~~~~~~~~

.. pyreverse:: myapp
   :filter: Test*,*Helper
   :type: class
   
   Excludes classes matching Test* or *Helper patterns.

Show Only Public
~~~~~~~~~~~~~~~~

.. pyreverse:: mymodule
   :only-public:
   :type: class
   
   Shows only public classes and methods (no underscore prefix).

Filter by Attribute
~~~~~~~~~~~~~~~~~~~

.. pyreverse:: myapp.models
   :show-attributes: public
   :show-methods: public
   :type: class
   
   Shows only public attributes and methods.

Customization Options
---------------------

Detailed Diagrams
~~~~~~~~~~~~~~~~~

.. pyreverse:: mymodule
   :type: class
   :show-attributes:
   :show-methods:
   :show-docstrings:
   
   Shows full class details including docstrings.

Simplified Diagrams
~~~~~~~~~~~~~~~~~~~

.. pyreverse:: myapp
   :type: class
   :no-attributes:
   :no-methods:
   
   Shows only class names and relationships.

Custom Layout
~~~~~~~~~~~~~

.. pyreverse:: myproject
   :type: package
   :layout: dot
   :orientation: TB
   
   Top-to-bottom layout using Graphviz dot engine.

Configuration Examples
----------------------

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx.ext.autodoc',
       'sphinx_pyreverse',
   ]
   
   # Pyreverse configuration
   pyreverse_output_format = 'svg'  # 'svg', 'png', 'pdf', 'dot'
   pyreverse_output_dir = '_pyreverse'

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Diagram styling
   pyreverse_defaults = {
       'show-builtin': False,
       'show-stdlib': False,
       'colorized': True,
       'max-color-depth': 2,
   }
   
   # Class diagram options
   pyreverse_class_defaults = {
       'show-ancestors': 2,  # Show up to 2 levels of ancestors
       'show-associated': 1,  # Show 1 level of associations
       'all-ancestors': False,
       'all-associated': False,
   }
   
   # Package diagram options
   pyreverse_package_defaults = {
       'show-only': [],  # List of modules/packages to show
       'ignore': ['test', 'tests'],  # Ignore test modules
   }

Theme Integration
~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Color scheme
   pyreverse_colors = {
       'class': '#E8F4F8',
       'interface': '#F8E8E8',
       'abstract': '#F8F8E8',
       'association': '#000000',
       'inheritance': '#0000FF',
   }
   
   # Font settings
   pyreverse_font = {
       'name': 'Arial',
       'size': 10,
   }

Integration with Autodoc
------------------------

Automatic Generation
~~~~~~~~~~~~~~~~~~~~

.. automodule:: myapp.models
   :members:
   :no-index:
   
   Automatically generates and includes class diagram with autodoc output.

Combined Documentation
~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: myapp.models.User
   :members:
   :no-index:
   
   **Class Diagram**:
   
   .. pyreverse:: myapp.models.User
      :type: class
      :show-inheritance:
   
   **Documentation**:
   
   The User class represents a registered user...

Practical Examples
------------------

Django Models
~~~~~~~~~~~~~

.. pyreverse:: myproject.models
   :type: class
   :show-inheritance:
   :show-associations:
   
   **Django Model Example**:
   
   .. code-block:: python
   
      from django.db import models
      
      class Author(models.Model):
          name = models.CharField(max_length=100)
          email = models.EmailField()
      
      class Book(models.Model):
          title = models.CharField(max_length=200)
          author = models.ForeignKey(Author, on_delete=models.CASCADE)
          published_date = models.DateField()
      
      class Review(models.Model):
          book = models.ForeignKey(Book, on_delete=models.CASCADE)
          rating = models.IntegerField()
          comment = models.TextField()
   
   **Generated Diagram**: Shows relationships between Author, Book, and Review models.

Flask Application
~~~~~~~~~~~~~~~~~

.. pyreverse:: myapp
   :type: package
   :show-modules:
   
   **Flask App Structure**:
   
   .. code-block:: text
   
      myapp/
      ├── __init__.py
      ├── models.py
      ├── views.py
      ├── forms.py
      └── utils.py
   
   **Generated Diagram**: Shows module dependencies and structure.

Design Patterns
~~~~~~~~~~~~~~~

.. pyreverse:: patterns
   :type: class
   :show-inheritance:
   :show-composition:
   
   **Singleton Pattern**:
   
   .. code-block:: python
   
      class Singleton:
          _instance = None
          
          def __new__(cls):
              if cls._instance is None:
                  cls._instance = super().__new__(cls)
              return cls._instance
   
   **Factory Pattern**:
   
   .. code-block:: python
   
      class Product:
          pass
      
      class ConcreteProductA(Product):
          pass
      
      class ConcreteProductB(Product):
          pass
      
      class Factory:
          def create_product(self, product_type):
              if product_type == 'A':
                  return ConcreteProductA()
              elif product_type == 'B':
                  return ConcreteProductB()
   
   **Generated Diagram**: Visualizes design pattern structure.

Advanced Features
-----------------

Inheritance Depth
~~~~~~~~~~~~~~~~~

.. pyreverse:: myapp.models
   :type: class
   :max-inheritance-depth: 3
   
   Limits inheritance tree display to 3 levels.

Association Level
~~~~~~~~~~~~~~~~~

.. pyreverse:: myapp.services
   :type: class
   :max-association-level: 2
   
   Shows associations up to 2 levels deep.

Clustering
~~~~~~~~~~

.. pyreverse:: myproject
   :type: package
   :cluster-by: module
   
   Groups classes by module in the diagram.

Interactive Diagrams
--------------------

With Links
~~~~~~~~~~

.. pyreverse:: myapp
   :type: class
   :link-to-docs:
   
   Generated diagram includes clickable links to class documentation.

With Tooltips
~~~~~~~~~~~~~

.. pyreverse:: mymodule
   :type: class
   :show-tooltips:
   
   Hovering over classes shows brief descriptions.

Export Options
--------------

Multiple Formats
~~~~~~~~~~~~~~~~

.. pyreverse:: myapp
   :type: class
   :export: svg, png, pdf
   
   Exports diagram in multiple formats.

High Resolution
~~~~~~~~~~~~~~~

.. pyreverse:: mymodule
   :type: class
   :dpi: 300
   :format: png
   
   Generates high-resolution PNG diagram.

Analysis Examples
-----------------

Complexity Analysis
~~~~~~~~~~~~~~~~~~~

.. pyreverse:: myapp
   :type: class
   :complexity-metric:
   
   Highlights classes by complexity level (color-coded).

Coupling Analysis
~~~~~~~~~~~~~~~~~

.. pyreverse:: myproject
   :type: package
   :show-coupling:
   
   Shows coupling between packages and modules.

Cohesion Metrics
~~~~~~~~~~~~~~~~

.. pyreverse:: myapp.services
   :type: class
   :cohesion-metric:
   
   Visualizes class cohesion levels.

Documentation Generation
------------------------

Full Project
~~~~~~~~~~~~

.. pyreverse:: myproject
   :type: both
   :output-dir: diagrams
   
   Generates both class and package diagrams for entire project.

Incremental Updates
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # In conf.py
   pyreverse_cache = True
   pyreverse_incremental = True
   
   # Only regenerates diagrams for changed modules

API Reference Diagrams
~~~~~~~~~~~~~~~~~~~~~~

.. pyreverse:: myapi
   :type: class
   :only-public:
   :show-methods:
   :link-to-docs:
   
   Creates API reference with linked class diagrams.


Practical Examples
------------------

Basic Class Diagrams
--------------------

Single Class
~~~~~~~~~~~~

.. pyreverse:: mymodule.MyClass
   :type: class
   
   Generates a class diagram for MyClass showing attributes and methods.

Multiple Classes
~~~~~~~~~~~~~~~~

.. pyreverse:: mymodule
   :classes: MyClass, AnotherClass, ThirdClass
   :type: class
   
   Shows class diagram for specific classes in a module.

Module Overview
~~~~~~~~~~~~~~~

.. pyreverse:: mypackage.core
   :type: class
   :all-classes:
   
   Generates class diagram for all classes in the module.

Class Relationships
-------------------

Inheritance Diagram
~~~~~~~~~~~~~~~~~~~

.. pyreverse:: myapp.models
   :type: class
   :show-inheritance:
   
   **Example Python Code**:
   
   .. code-block:: python
   
      class Animal:
          def __init__(self, name):
              self.name = name
          
          def speak(self):
              pass
      
      class Dog(Animal):
          def speak(self):
              return "Woof!"
      
      class Cat(Animal):
          def speak(self):
              return "Meow!"
   
   **Generated Diagram**: Shows Animal as base class with Dog and Cat as subclasses.

Composition and Aggregation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. pyreverse:: myapp.components
   :type: class
   :show-composition:
   :show-aggregation:
   
   **Example Python Code**:
   
   .. code-block:: python
   
      class Engine:
          def __init__(self, horsepower):
              self.horsepower = horsepower
      
      class Wheel:
          def __init__(self, size):
              self.size = size
      
      class Car:
          def __init__(self):
              self.engine = Engine(200)  # Composition
              self.wheels = [Wheel(17) for _ in range(4)]  # Aggregation
   
   **Generated Diagram**: Shows Car containing Engine and Wheels.

Association Diagram
~~~~~~~~~~~~~~~~~~~

.. pyreverse:: myapp.database
   :type: class
   :show-associations:
   
   **Example Python Code**:
   
   .. code-block:: python
   
      class User:
          def __init__(self):
              self.posts = []
          
          def add_post(self, post):
              self.posts.append(post)
      
      class Post:
          def __init__(self, author):
              self.author = author  # Association
   
   **Generated Diagram**: Shows bidirectional association between User and Post.

Package Diagrams
----------------

Package Structure
~~~~~~~~~~~~~~~~~

.. pyreverse:: myproject
   :type: package
   
   Shows package structure and inter-package dependencies.

Module Dependencies
~~~~~~~~~~~~~~~~~~~

.. pyreverse:: myapp
   :type: package
   :show-modules:
   
   Displays modules within packages and their dependencies.

Nested Packages
~~~~~~~~~~~~~~~

.. pyreverse:: myproject.subpackage
   :type: package
   :depth: 3
   
   Shows nested package structure up to 3 levels deep.

Filtering Options
-----------------

Filter by Pattern
~~~~~~~~~~~~~~~~~

.. pyreverse:: myapp
   :filter: Test*,*Helper
   :type: class
   
   Excludes classes matching Test* or *Helper patterns.

Show Only Public
~~~~~~~~~~~~~~~~

.. pyreverse:: mymodule
   :only-public:
   :type: class
   
   Shows only public classes and methods (no underscore prefix).

Filter by Attribute
~~~~~~~~~~~~~~~~~~~

.. pyreverse:: myapp.models
   :show-attributes: public
   :show-methods: public
   :type: class
   
   Shows only public attributes and methods.

Customization Options
---------------------

Detailed Diagrams
~~~~~~~~~~~~~~~~~

.. pyreverse:: mymodule
   :type: class
   :show-attributes:
   :show-methods:
   :show-docstrings:
   
   Shows full class details including docstrings.

Simplified Diagrams
~~~~~~~~~~~~~~~~~~~

.. pyreverse:: myapp
   :type: class
   :no-attributes:
   :no-methods:
   
   Shows only class names and relationships.

Custom Layout
~~~~~~~~~~~~~

.. pyreverse:: myproject
   :type: package
   :layout: dot
   :orientation: TB
   
   Top-to-bottom layout using Graphviz dot engine.

Configuration Examples
----------------------

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx.ext.autodoc',
       'sphinx_pyreverse',
   ]
   
   # Pyreverse configuration
   pyreverse_output_format = 'svg'  # 'svg', 'png', 'pdf', 'dot'
   pyreverse_output_dir = '_pyreverse'

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Diagram styling
   pyreverse_defaults = {
       'show-builtin': False,
       'show-stdlib': False,
       'colorized': True,
       'max-color-depth': 2,
   }
   
   # Class diagram options
   pyreverse_class_defaults = {
       'show-ancestors': 2,  # Show up to 2 levels of ancestors
       'show-associated': 1,  # Show 1 level of associations
       'all-ancestors': False,
       'all-associated': False,
   }
   
   # Package diagram options
   pyreverse_package_defaults = {
       'show-only': [],  # List of modules/packages to show
       'ignore': ['test', 'tests'],  # Ignore test modules
   }

Theme Integration
~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Color scheme
   pyreverse_colors = {
       'class': '#E8F4F8',
       'interface': '#F8E8E8',
       'abstract': '#F8F8E8',
       'association': '#000000',
       'inheritance': '#0000FF',
   }
   
   # Font settings
   pyreverse_font = {
       'name': 'Arial',
       'size': 10,
   }

Integration with Autodoc
------------------------

Automatic Generation
~~~~~~~~~~~~~~~~~~~~

.. automodule:: myapp.models
   :members:
   :no-index:
   
   Automatically generates and includes class diagram with autodoc output.

Combined Documentation
~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: myapp.models.User
   :members:
   :no-index:
   
   **Class Diagram**:
   
   .. pyreverse:: myapp.models.User
      :type: class
      :show-inheritance:
   
   **Documentation**:
   
   The User class represents a registered user...

Practical Examples
------------------

Django Models
~~~~~~~~~~~~~

.. pyreverse:: myproject.models
   :type: class
   :show-inheritance:
   :show-associations:
   
   **Django Model Example**:
   
   .. code-block:: python
   
      from django.db import models
      
      class Author(models.Model):
          name = models.CharField(max_length=100)
          email = models.EmailField()
      
      class Book(models.Model):
          title = models.CharField(max_length=200)
          author = models.ForeignKey(Author, on_delete=models.CASCADE)
          published_date = models.DateField()
      
      class Review(models.Model):
          book = models.ForeignKey(Book, on_delete=models.CASCADE)
          rating = models.IntegerField()
          comment = models.TextField()
   
   **Generated Diagram**: Shows relationships between Author, Book, and Review models.

Flask Application
~~~~~~~~~~~~~~~~~

.. pyreverse:: myapp
   :type: package
   :show-modules:
   
   **Flask App Structure**:
   
   .. code-block:: text
   
      myapp/
      ├── __init__.py
      ├── models.py
      ├── views.py
      ├── forms.py
      └── utils.py
   
   **Generated Diagram**: Shows module dependencies and structure.

Design Patterns
~~~~~~~~~~~~~~~

.. pyreverse:: patterns
   :type: class
   :show-inheritance:
   :show-composition:
   
   **Singleton Pattern**:
   
   .. code-block:: python
   
      class Singleton:
          _instance = None
          
          def __new__(cls):
              if cls._instance is None:
                  cls._instance = super().__new__(cls)
              return cls._instance
   
   **Factory Pattern**:
   
   .. code-block:: python
   
      class Product:
          pass
      
      class ConcreteProductA(Product):
          pass
      
      class ConcreteProductB(Product):
          pass
      
      class Factory:
          def create_product(self, product_type):
              if product_type == 'A':
                  return ConcreteProductA()
              elif product_type == 'B':
                  return ConcreteProductB()
   
   **Generated Diagram**: Visualizes design pattern structure.

Advanced Features
-----------------

Inheritance Depth
~~~~~~~~~~~~~~~~~

.. pyreverse:: myapp.models
   :type: class
   :max-inheritance-depth: 3
   
   Limits inheritance tree display to 3 levels.

Association Level
~~~~~~~~~~~~~~~~~

.. pyreverse:: myapp.services
   :type: class
   :max-association-level: 2
   
   Shows associations up to 2 levels deep.

Clustering
~~~~~~~~~~

.. pyreverse:: myproject
   :type: package
   :cluster-by: module
   
   Groups classes by module in the diagram.

Interactive Diagrams
--------------------

With Links
~~~~~~~~~~

.. pyreverse:: myapp
   :type: class
   :link-to-docs:
   
   Generated diagram includes clickable links to class documentation.

With Tooltips
~~~~~~~~~~~~~

.. pyreverse:: mymodule
   :type: class
   :show-tooltips:
   
   Hovering over classes shows brief descriptions.

Export Options
--------------

Multiple Formats
~~~~~~~~~~~~~~~~

.. pyreverse:: myapp
   :type: class
   :export: svg, png, pdf
   
   Exports diagram in multiple formats.

High Resolution
~~~~~~~~~~~~~~~

.. pyreverse:: mymodule
   :type: class
   :dpi: 300
   :format: png
   
   Generates high-resolution PNG diagram.

Analysis Examples
-----------------

Complexity Analysis
~~~~~~~~~~~~~~~~~~~

.. pyreverse:: myapp
   :type: class
   :complexity-metric:
   
   Highlights classes by complexity level (color-coded).

Coupling Analysis
~~~~~~~~~~~~~~~~~

.. pyreverse:: myproject
   :type: package
   :show-coupling:
   
   Shows coupling between packages and modules.

Cohesion Metrics
~~~~~~~~~~~~~~~~

.. pyreverse:: myapp.services
   :type: class
   :cohesion-metric:
   
   Visualizes class cohesion levels.

Documentation Generation
------------------------

Full Project
~~~~~~~~~~~~

.. pyreverse:: myproject
   :type: both
   :output-dir: diagrams
   
   Generates both class and package diagrams for entire project.

Incremental Updates
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # In conf.py
   pyreverse_cache = True
   pyreverse_incremental = True
   
   # Only regenerates diagrams for changed modules

API Reference Diagrams
~~~~~~~~~~~~~~~~~~~~~~

.. pyreverse:: myapi
   :type: class
   :only-public:
   :show-methods:
   :link-to-docs:
   
   Creates API reference with linked class diagrams.

Additional Resources
--------------------
- :doc:`sphinx-uml` - PlantUML integration
- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `Pyreverse Documentation <https://pylint.pycqa.org/en/latest/pyreverse.html>`_
- `UML Class Diagrams <https://www.uml-diagrams.org/class-diagrams-overview.html>`_
- :doc:`../tutorials/packages/sphinx-pyreverse` - Complete tutorial
- Official Pyreverse documentation: https://pylint.readthedocs.io/en/latest/pyreverse.html
- GitHub repository: https://github.com/sphinx-doc/sphinx-pyreverse

