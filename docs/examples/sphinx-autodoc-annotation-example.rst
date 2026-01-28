Sphinx-Autodoc-Annotation Example
==================================

This page demonstrates the **sphinx-autodoc-annotation** extension for enhanced Python type annotation documentation.

.. contents:: Contents
   :local:
   :depth: 2

Overview
--------

The sphinx-autodoc-annotation extension improves how Python type annotations are displayed in Sphinx documentation.

Basic Usage
-----------

Type Annotations
~~~~~~~~~~~~~~~~

.. code-block:: python

   def greet(name: str, age: int) -> str:
       """Greet a person.
       
       :param name: Person's name
       :param age: Person's age
       :return: Greeting message
       """
       return f"Hello {name}, you are {age} years old"

Advanced Types
--------------

Generic Types
~~~~~~~~~~~~~

.. code-block:: python

   from typing import List, Dict, Optional, Union
   
   def process_items(
       items: List[str],
       config: Optional[Dict[str, Any]] = None
   ) -> Union[List[str], None]:
       """Process a list of items."""
       pass

Type Aliases
~~~~~~~~~~~~

.. code-block:: python

   from typing import TypeAlias
   
   UserId: TypeAlias = int
   UserData: TypeAlias = Dict[str, Union[str, int]]
   
   def get_user(user_id: UserId) -> UserData:
       """Retrieve user data."""
       pass

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx.ext.autodoc',
       'sphinx_autodoc_annotation',
   ]

Options
~~~~~~~

.. code-block:: python

   autodoc_annotation_format = 'short'  # or 'long', 'full'
   autodoc_typehints = 'description'  # or 'signature', 'both'

Examples
--------

Complex Annotations
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from typing import Callable, TypeVar
   
   T = TypeVar('T')
   
   def map_values(
       func: Callable[[T], T],
       items: List[T]
   ) -> List[T]:
       """Apply function to all items."""
       return [func(item) for item in items]

See Also
--------

- :doc:`../tutorials/packages/sphinx-autodoc-annotation` - Complete tutorial
- PEP 484: https://www.python.org/dev/peps/pep-0484/
- GitHub repository: https://github.com/sphinx-contrib/autodoc-annotation
