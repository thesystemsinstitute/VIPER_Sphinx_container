Sphinx-Pyreverse Example
========================

This page demonstrates the **sphinx-pyreverse** extension for generating UML class diagrams and package diagrams from Python code using Pyreverse.

.. contents:: Contents
   :local:
   :depth: 2

Overview
--------

The sphinx-pyreverse extension integrates Pyreverse (from Pylint) to automatically generate UML diagrams from Python source code, including class diagrams, package diagrams, and dependency graphs.

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
   :pyreverse:
   
   Automatically generates and includes class diagram with autodoc output.

Combined Documentation
~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: myapp.models.User
   :members:
   :pyreverse-class:
   
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

See Also
--------

- :doc:`../tutorials/packages/sphinx-pyreverse` - Complete tutorial
- Official Pyreverse documentation: https://pylint.readthedocs.io/en/latest/pyreverse.html
- GitHub repository: https://github.com/sphinx-doc/sphinx-pyreverse
