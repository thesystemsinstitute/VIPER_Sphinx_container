Pytest-Doctestplus Tutorial
===========================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/pytest-doctestplus/>`_
   - :doc:`See Working Example <../../examples/pytest-doctestplus-example>`
   - `Official Documentation <https://pytest-doctestplus.readthedocs.io/>`_


This tutorial demonstrates how to use pytest-doctestplus to run and test code examples in docstrings and RST documentation.

What is Pytest-Doctestplus?
----------------------------

pytest-doctestplus is a pytest plugin that enhances Python's doctest capabilities with:

- Extended doctest support
- RST file testing
- Float comparison
- Ellipsis handling
- Output normalization
- Remote data handling
- Skip directives
- Better error messages
- Numpy array support
- Integration with pytest
- Fixture support
- Parametrization

Originally developed for the Astropy project, it's useful for any project with documentation examples.

Installation
------------

pytest-doctestplus is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import pytest_doctestplus; print('Installed')"

Configuration
-------------

pytest.ini Setup
~~~~~~~~~~~~~~~~

Create ``pytest.ini``:

.. code-block:: ini

   [pytest]
   addopts = --doctest-plus --doctest-rst
   doctest_optionflags = NORMALIZE_WHITESPACE ELLIPSIS
   doctest_plus = enabled
   text_file_format = rst

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: ini

   [pytest]
   # Enable doctestplus
   addopts = --doctest-plus --doctest-rst
   
   # Doctest options
   doctest_optionflags = 
       NORMALIZE_WHITESPACE
       ELLIPSIS
       FLOAT_CMP
       IGNORE_EXCEPTION_DETAIL
   
   # File patterns
   doctest_plus = enabled
   text_file_format = rst
   doctest_rst_path = docs
   
   # Float comparison
   doctest_float_tolerance = 1e-6
   
   # Remote data
   remote_data_strict = true

Basic Usage
-----------

Test Docstrings
~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm -v $(pwd):/project \
     kensai-sphinx:latest \
     pytest --doctest-plus mylib/

Test RST Files
~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm -v $(pwd):/project \
     kensai-sphinx:latest \
     pytest --doctest-rst docs/

Run All Doctests
~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm -v $(pwd):/project \
     kensai-sphinx:latest \
     pytest --doctest-plus --doctest-rst

Practical Examples
------------------

Example 1: Testing Function Docstrings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``mylib/math_utils.py``:

.. code-block:: python

   """Mathematical utility functions."""
   
   import numpy as np
   from typing import List, Union
   
   def mean(values: List[float]) -> float:
       """
       Calculate arithmetic mean.
       
       Parameters
       ----------
       values : List[float]
           List of numbers
       
       Returns
       -------
       float
           Mean value
       
       Examples
       --------
       >>> mean([1, 2, 3, 4, 5])
       3.0
       
       >>> mean([10, 20, 30])
       20.0
       
       Works with numpy arrays:
       
       >>> import numpy as np
       >>> mean(np.array([1.5, 2.5, 3.5]))  # doctest: +FLOAT_CMP
       2.5
       """
       return sum(values) / len(values)
   
   def std_dev(values: List[float]) -> float:
       """
       Calculate standard deviation.
       
       Parameters
       ----------
       values : List[float]
           List of numbers
       
       Returns
       -------
       float
           Standard deviation
       
       Examples
       --------
       >>> std_dev([2, 4, 4, 4, 5, 5, 7, 9])  # doctest: +FLOAT_CMP
       2.0
       
       Handles edge cases:
       
       >>> std_dev([5, 5, 5, 5])  # doctest: +FLOAT_CMP
       0.0
       """
       avg = mean(values)
       variance = sum((x - avg) ** 2 for x in values) / len(values)
       return variance ** 0.5
   
   def normalize(values: List[float]) -> List[float]:
       """
       Normalize values to 0-1 range.
       
       Parameters
       ----------
       values : List[float]
           Input values
       
       Returns
       -------
       List[float]
           Normalized values
       
       Examples
       --------
       >>> normalize([0, 5, 10])  # doctest: +ELLIPSIS
       [0.0, 0.5, 1.0...]
       
       >>> normalize([100, 200, 300])  # doctest: +ELLIPSIS
       [0.0, 0.5, 1.0...]
       
       Single value:
       
       >>> normalize([42])
       [0.0]
       """
       min_val = min(values)
       max_val = max(values)
       if min_val == max_val:
           return [0.0] * len(values)
       return [(x - min_val) / (max_val - min_val) for x in values]

Run tests:

.. code-block:: bash

   pytest --doctest-plus mylib/math_utils.py -v

Example 2: Testing Class Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``mylib/data.py``:

.. code-block:: python

   """Data structures."""
   
   from typing import Any, Dict, List, Optional
   
   class DataContainer:
       """
       Container for data with metadata.
       
       Parameters
       ----------
       data : Any
           The data to store
       metadata : Dict, optional
           Metadata dictionary
       
       Examples
       --------
       Create a container:
       
       >>> container = DataContainer([1, 2, 3], {'source': 'test'})
       >>> container.data
       [1, 2, 3]
       >>> container.metadata['source']
       'test'
       
       Add metadata:
       
       >>> container.add_metadata('author', 'John Doe')
       >>> container.metadata['author']
       'John Doe'
       
       Get data with metadata:
       
       >>> info = container.get_info()
       >>> info['has_metadata']
       True
       """
       
       def __init__(self, data: Any, metadata: Optional[Dict] = None):
           self.data = data
           self.metadata = metadata or {}
       
       def add_metadata(self, key: str, value: Any) -> None:
           """
           Add metadata entry.
           
           Examples
           --------
           >>> container = DataContainer([1, 2, 3])
           >>> container.add_metadata('version', '1.0')
           >>> container.metadata['version']
           '1.0'
           """
           self.metadata[key] = value
       
       def get_info(self) -> Dict[str, Any]:
           """
           Get container information.
           
           Examples
           --------
           >>> container = DataContainer([1, 2, 3])
           >>> info = container.get_info()
           >>> info['data_type']
           "<class 'list'>"
           >>> info['has_metadata']
           False
           """
           return {
               'data_type': str(type(self.data)),
               'has_metadata': bool(self.metadata),
               'metadata_keys': list(self.metadata.keys()),
           }

Example 3: Testing RST Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/examples/tutorial.rst``:

.. code-block:: rst

   Tutorial
   ========
   
   This tutorial demonstrates basic usage.
   
   Getting Started
   ---------------
   
   Import the library:
   
   .. code-block:: python
   
      >>> from mylib import math_utils
      >>> math_utils.mean([1, 2, 3, 4, 5])
      3.0
   
   Calculate Statistics
   --------------------
   
   Calculate mean and standard deviation:
   
   .. code-block:: python
   
      >>> data = [2, 4, 4, 4, 5, 5, 7, 9]
      >>> math_utils.mean(data)
      5.0
      >>> math_utils.std_dev(data)  # doctest: +FLOAT_CMP
      2.0
   
   Normalize Data
   --------------
   
   Normalize values to 0-1 range:
   
   .. code-block:: python
   
      >>> values = [0, 5, 10]
      >>> normalized = math_utils.normalize(values)
      >>> normalized  # doctest: +ELLIPSIS
      [0.0, 0.5, 1.0...]
   
   Using Data Containers
   ---------------------
   
   Create and use a data container:
   
   .. code-block:: python
   
      >>> from mylib.data import DataContainer
      >>> container = DataContainer([1, 2, 3], {'source': 'example'})
      >>> container.data
      [1, 2, 3]
      >>> container.metadata
      {'source': 'example'}

Test the RST file:

.. code-block:: bash

   pytest --doctest-rst docs/examples/tutorial.rst -v

Advanced Features
-----------------

Float Comparison
~~~~~~~~~~~~~~~~

.. code-block:: python

   def calculate_pi():
       """
       Calculate pi approximation.
       
       Examples
       --------
       >>> calculate_pi()  # doctest: +FLOAT_CMP
       3.14159265
       """
       return 3.14159265358979

Ellipsis for Long Output
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   def get_config():
       """
       Get configuration.
       
       Examples
       --------
       >>> config = get_config()  # doctest: +ELLIPSIS
       {'database': ..., 'cache': ..., 'logging': ...}
       """
       return {
           'database': {'host': 'localhost', 'port': 5432},
           'cache': {'backend': 'redis', 'timeout': 300},
           'logging': {'level': 'INFO', 'file': 'app.log'},
       }

Skip Tests
~~~~~~~~~~

.. code-block:: python

   def requires_network():
       """
       Function requiring network.
       
       Examples
       --------
       >>> requires_network()  # doctest: +SKIP
       'Success'
       """
       pass

Remote Data
~~~~~~~~~~~

.. code-block:: python

   def fetch_data():
       """
       Fetch remote data.
       
       Examples
       --------
       >>> data = fetch_data()  # doctest: +REMOTE_DATA
       >>> len(data) > 0
       True
       """
       pass

Docker Integration
------------------

Run Doctests in Container
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     -w /project \
     kensai-sphinx:latest \
     pytest --doctest-plus --doctest-rst

Interactive Testing
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm -it \
     -v $(pwd):/project \
     -w /project \
     kensai-sphinx:latest \
     sh
   
   # Inside container
   pytest --doctest-plus mylib/ -v

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Test Documentation Examples
   
   on:
     push:
       paths:
         - '**/*.py'
         - 'docs/**/*.rst'
   
   jobs:
     doctest:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Run Doctests
           run: |
             docker run --rm -v $(pwd):/project -w /project \
               kensai-sphinx:latest \
               pytest --doctest-plus --doctest-rst -v
         
         - name: Upload Results
           if: failure()
           uses: actions/upload-artifact@v3
           with:
             name: doctest-results
             path: test-results/

Best Practices
--------------

1. **Test All Examples**
   
   Ensure examples work

2. **Use Appropriate Flags**
   
   FLOAT_CMP for floats, ELLIPSIS for long output

3. **Keep Examples Simple**
   
   Focus on common use cases

4. **Test RST Documentation**
   
   Validate tutorial examples

5. **Handle Edge Cases**
   
   Show what happens with empty input

6. **Use Skip Wisely**
   
   Skip tests requiring external resources

Troubleshooting
---------------

Tests Fail Due to Whitespace
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Solution:**

Use NORMALIZE_WHITESPACE:

.. code-block:: python

   >>> result()  # doctest: +NORMALIZE_WHITESPACE
   [1, 2, 3]

Float Comparison Fails
~~~~~~~~~~~~~~~~~~~~~~~

**Solution:**

Use FLOAT_CMP flag:

.. code-block:: python

   >>> 0.1 + 0.2  # doctest: +FLOAT_CMP
   0.3

Import Errors
~~~~~~~~~~~~~

**Solution:**

Ensure package is importable:

.. code-block:: python

   import sys
   sys.path.insert(0, '/project')

RST Tests Not Running
~~~~~~~~~~~~~~~~~~~~~~

**Solution:**

Check pytest.ini configuration:

.. code-block:: ini

   [pytest]
   addopts = --doctest-rst
   text_file_format = rst

Next Steps
----------

1. Add examples to docstrings
2. Configure pytest-doctestplus
3. Run doctests regularly
4. Integrate with CI/CD
5. Monitor test coverage

Additional Resources
--------------------

- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `Pytest Doctestplus Documentation <https://github.com/astropy/pytest-doctestplus>`_
- `Python Doctest <https://docs.python.org/3/library/doctest.html>`_
