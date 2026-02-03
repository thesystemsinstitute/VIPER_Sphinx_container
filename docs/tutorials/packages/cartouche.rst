Cartouche Tutorial
==================

.. note::

   **Package Resources:**

   - `PyPI Package <https://pypi.org/project/cartouche/>`_
   - `API Documentation <../../pdoc/cartouche/index.html>`_
   - `Manual <https://github.com/rob-smallshire/cartouche>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial covers cartouche, a Sphinx extension that converts lightweight docstring formats into reStructuredText.

What is Cartouche?
------------------
Cartouche transforms readable docstrings into Sphinx-friendly markup, keeping docstrings IDE-friendly while still rich in Sphinx.

Installation
------------

Install via pip:

.. code-block:: bash

   pip install cartouche

Configuration
-------------

Enable the extension in ``conf.py``:

.. code-block:: python

   extensions = [
       "cartouche",
   ]

Basic Usage
-----------

Write concise docstrings and let Cartouche render them during the Sphinx build.

Cartouche transforms readable, plain-text docstrings into Sphinx-friendly reStructuredText, so your docstrings remain IDE-friendly while still generating rich documentation.

Advanced Features
-----------------

- Keep docstrings readable for introspection tools.
- Use standard Sphinx directives after transformation.
- Support for multiple docstring formats.
- Automatic parameter type extraction.
- Exception documentation support.
- Return value documentation.

Configuration Options
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py

   extensions = [
       "sphinx.ext.autodoc",
       "cartouche",
   ]

   # Cartouche recognizes various docstring formats:
   # - Epytext style (@param, @return, @raise)
   # - reST style (:param:, :returns:, :raises:)
   # - Google style (Args:, Returns:, Raises:)

Examples
--------

Epytext-Style Docstrings
~~~~~~~~~~~~~~~~~~~~~~~~

Cartouche converts Epytext-style docstrings to Sphinx format:

**Source code:**

.. code-block:: python

   def calculate_distance(point1, point2, metric='euclidean'):
       """Calculate the distance between two points.

       @param point1: The first point as (x, y) tuple.
       @type point1: tuple[float, float]
       @param point2: The second point as (x, y) tuple.
       @type point2: tuple[float, float]
       @param metric: Distance metric to use.
       @type metric: str

       @return: The calculated distance.
       @rtype: float

       @raise ValueError: If an unknown metric is specified.
       """
       import math
       if metric == 'euclidean':
           return math.sqrt(
               (point2[0] - point1[0])**2 +
               (point2[1] - point1[1])**2
           )
       elif metric == 'manhattan':
           return abs(point2[0] - point1[0]) + abs(point2[1] - point1[1])
       else:
           raise ValueError(f"Unknown metric: {metric}")

**Rendered documentation:**

   **calculate_distance** (point1, point2, metric='euclidean')

   Calculate the distance between two points.

   :param point1: The first point as (x, y) tuple.
   :type point1: tuple[float, float]
   :param point2: The second point as (x, y) tuple.
   :type point2: tuple[float, float]
   :param metric: Distance metric to use.
   :type metric: str
   :returns: The calculated distance.
   :rtype: float
   :raises ValueError: If an unknown metric is specified.

Google-Style Docstrings
~~~~~~~~~~~~~~~~~~~~~~~

Cartouche also handles Google-style docstrings:

**Source code:**

.. code-block:: python

   def fetch_user_data(user_id, include_metadata=False, timeout=30):
       """Fetch user data from the database.

       Retrieves user information including profile data and optionally
       metadata such as creation date and last login.

       Args:
           user_id: The unique identifier for the user.
           include_metadata: Whether to include additional metadata.
               Defaults to False.
           timeout: Request timeout in seconds. Defaults to 30.

       Returns:
           A dictionary containing user data with keys:
               - 'id': User ID
               - 'name': Display name
               - 'email': Email address
               - 'metadata': Optional metadata dict

       Raises:
           UserNotFoundError: If no user exists with the given ID.
           ConnectionError: If the database connection fails.
           TimeoutError: If the request exceeds the timeout.

       Example:
           >>> user = fetch_user_data(123)
           >>> print(user['name'])
           'John Doe'
       """
       pass

Class Documentation
~~~~~~~~~~~~~~~~~~~

Document classes with their attributes and methods:

**Source code:**

.. code-block:: python

   class DataProcessor:
       """Process and validate data records.

       A flexible data processor that can handle multiple input formats
       and apply configurable validation rules.

       @ivar config: Processor configuration dictionary.
       @type config: dict
       @ivar validators: List of validator functions.
       @type validators: list[Callable]

       @cvar DEFAULT_CONFIG: Default configuration values.
       @type DEFAULT_CONFIG: dict
       """

       DEFAULT_CONFIG = {'strict': False, 'encoding': 'utf-8'}

       def __init__(self, config=None):
           """Initialize the data processor.

           @param config: Configuration dictionary. Uses DEFAULT_CONFIG
               if not specified.
           @type config: dict | None
           """
           self.config = config or self.DEFAULT_CONFIG.copy()
           self.validators = []

       def add_validator(self, validator):
           """Add a validation function to the processor.

           @param validator: A callable that takes a record and returns
               True if valid, False otherwise.
           @type validator: Callable[[dict], bool]

           @return: Self for method chaining.
           @rtype: DataProcessor
           """
           self.validators.append(validator)
           return self

       def process(self, records):
           """Process a batch of records.

           @param records: Iterable of record dictionaries to process.
           @type records: Iterable[dict]

           @return: List of processed and validated records.
           @rtype: list[dict]

           @raise ValidationError: If a record fails validation and
               strict mode is enabled.
           """
           results = []
           for record in records:
               if all(v(record) for v in self.validators):
                   results.append(record)
               elif self.config.get('strict'):
                   raise ValidationError(f"Record failed validation: {record}")
           return results

Complex Type Annotations
~~~~~~~~~~~~~~~~~~~~~~~~

Handle complex type annotations with Cartouche:

**Source code:**

.. code-block:: python

   from typing import Dict, List, Optional, Union, Callable, TypeVar, Generic

   T = TypeVar('T')
   R = TypeVar('R')

   def transform_data(
       data: List[Dict[str, Union[str, int, float]]],
       transformer: Callable[[Dict[str, Union[str, int, float]]], T],
       filter_func: Optional[Callable[[T], bool]] = None,
   ) -> List[T]:
       """Transform a list of data dictionaries.

       Applies a transformation function to each dictionary in the input
       list, optionally filtering the results.

       @param data: List of dictionaries containing string, int, or float values.
       @type data: List[Dict[str, Union[str, int, float]]]
       @param transformer: Function to apply to each dictionary.
       @type transformer: Callable[[Dict[str, Union[str, int, float]]], T]
       @param filter_func: Optional function to filter transformed results.
           If None, all results are included.
       @type filter_func: Optional[Callable[[T], bool]]

       @return: List of transformed (and optionally filtered) results.
       @rtype: List[T]

       @raise TypeError: If data is not a list.
       @raise ValueError: If transformer returns None.
       """
       results = [transformer(item) for item in data]
       if filter_func:
           results = [r for r in results if filter_func(r)]
       return results

Multi-Line Descriptions
~~~~~~~~~~~~~~~~~~~~~~~

Handle multi-line parameter descriptions:

**Source code:**

.. code-block:: python

   def configure_logging(
       level,
       format_string,
       handlers,
       propagate=True,
   ):
       """Configure application logging.

       Sets up logging with the specified configuration. This function
       should be called early in application startup.

       @param level: The minimum logging level. Can be a string like
           'DEBUG', 'INFO', 'WARNING', 'ERROR', or 'CRITICAL', or
           an integer corresponding to those levels.
       @type level: str | int
       @param format_string: The format string for log messages.
           Supports standard logging format specifiers like %(message)s,
           %(levelname)s, %(asctime)s, etc.
       @type format_string: str
       @param handlers: List of handler configurations. Each handler
           should be a dictionary with at least a 'type' key specifying
           the handler class (e.g., 'stream', 'file', 'rotating_file').
           Additional keys depend on the handler type.
       @type handlers: list[dict]
       @param propagate: Whether to propagate log messages to parent
           loggers. Set to False to prevent duplicate logging when
           using multiple handlers.
       @type propagate: bool

       @return: The configured logger instance.
       @rtype: logging.Logger

       @raise ValueError: If level is not a valid logging level.
       @raise IOError: If a file handler cannot be created.
       """
       pass

Integration with autodoc
~~~~~~~~~~~~~~~~~~~~~~~~

Use Cartouche with Sphinx autodoc:

.. code-block:: restructuredtext

   API Reference
   =============

   Data Processing
   ---------------

   .. automodule:: mypackage.processing
      :members:
      :undoc-members:
      :show-inheritance:

   Utilities
   ---------

   .. autofunction:: mypackage.utils.calculate_distance

   .. autofunction:: mypackage.utils.fetch_user_data

   .. autoclass:: mypackage.processing.DataProcessor
      :members:
      :special-members: __init__

Benefits Over Plain Docstrings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **IDE Compatibility**: Docstrings remain readable in IDEs and ``help()``.
2. **Introspection**: ``inspect.getdoc()`` returns clean, readable text.
3. **No Markup Clutter**: Source code stays clean without RST markup.
4. **Gradual Adoption**: Works alongside existing Sphinx-style docstrings.

Additional Resources
--------------------

- `Manual <https://github.com/rob-smallshire/cartouche>`_
- `PyPI <https://pypi.org/project/cartouche/>`_
- `API Documentation <../../pdoc/cartouche/index.html>`_
