Pytest-Doctestplus Tutorial
===========================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/pytest-doctestplus/>`_
   - `API Documentation <../../pdoc/pytest_doctestplus/index.html>`_
   - `Manual <https://github.com/scientific-python/pytest-doctestplus>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

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

The pytest-doctestplus extension provides advanced doctest features including floating-point comparison and output normalization.


Installation
------------

pytest-doctestplus is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm viper-sphinx:latest python -c "import pytest_doctestplus; print('Installed')"

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


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Basic Setup
~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx.ext.doctest',
   ]
   
   # pytest configuration in pyproject.toml
   # [tool.pytest.ini_options]
   # doctest_plus = "enabled"

Options
~~~~~~~

.. code-block:: python

   doctest_global_setup = '''
   import numpy as np
   import pandas as pd
   '''
   
   doctest_test_doctest_blocks = 'default'

Basic Usage
-----------

Test Docstrings
~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm -v $(pwd):/project \
     viper-sphinx:latest \
     pytest --doctest-plus mylib/

Test RST Files
~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm -v $(pwd):/project \
     viper-sphinx:latest \
     pytest --doctest-rst docs/

Run All Doctests
~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm -v $(pwd):/project \
     viper-sphinx:latest \
     pytest --doctest-plus --doctest-rst

Advanced Features
-----------------

Float Comparison
~~~~~~~~~~~~~~~~

.. code-block:: python

   def calculate_pi():
       """
       Calculate pi approximation.
       
Docker Integration
------------------

Run Doctests in Container
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     -w /project \
     viper-sphinx:latest \
     pytest --doctest-plus --doctest-rst

Interactive Testing
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm -it \
     -v $(pwd):/project \
     -w /project \
     viper-sphinx:latest \
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
               viper-sphinx:latest \
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


Practical Examples
------------------

Basic Usage
-----------

Simple Doctest
~~~~~~~~~~~~~~

.. code-block:: python

   def add(a, b):
       """Add two numbers.
       
       >>> add(2, 3)
       5
       >>> add(10, 20)
       30
       """
       return a + b

Floating Point
~~~~~~~~~~~~~~

.. code-block:: python

   def calculate_pi():
       """Calculate pi approximation.
       
       >>> calculate_pi()  # doctest: +FLOAT_CMP
       3.14159265
       """
       return 3.14159265358979

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx.ext.doctest',
   ]
   
   # pytest configuration in pyproject.toml
   # [tool.pytest.ini_options]
   # doctest_plus = "enabled"

Options
~~~~~~~

.. code-block:: python

   doctest_global_setup = '''
   import numpy as np
   import pandas as pd
   '''
   
   doctest_test_doctest_blocks = 'default'

Examples
--------

Array Comparison
~~~~~~~~~~~~~~~~

.. code-block:: python

   def create_array():
       """Create numpy array.
       
       >>> import numpy as np
       >>> create_array()  # doctest: +FLOAT_CMP
       array([1., 2., 3.])
       """
       return np.array([1.0, 2.0, 3.0])


Practical Examples
------------------

Basic Usage
-----------

Simple Doctest
~~~~~~~~~~~~~~

.. code-block:: python

   def add(a, b):
       """Add two numbers.
       
       >>> add(2, 3)
       5
       >>> add(10, 20)
       30
       """
       return a + b

Floating Point
~~~~~~~~~~~~~~

.. code-block:: python

   def calculate_pi():
       """Calculate pi approximation.
       
       >>> calculate_pi()  # doctest: +FLOAT_CMP
       3.14159265
       """
       return 3.14159265358979

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx.ext.doctest',
   ]
   
   # pytest configuration in pyproject.toml
   # [tool.pytest.ini_options]
   # doctest_plus = "enabled"

Options
~~~~~~~

.. code-block:: python

   doctest_global_setup = '''
   import numpy as np
   import pandas as pd
   '''
   
   doctest_test_doctest_blocks = 'default'

Examples
--------

Array Comparison
~~~~~~~~~~~~~~~~

.. code-block:: python

   def create_array():
       """Create numpy array.
       
       >>> import numpy as np
       >>> create_array()  # doctest: +FLOAT_CMP
       array([1., 2., 3.])
       """
       return np.array([1.0, 2.0, 3.0])


Practical Examples
------------------

Basic Usage
-----------

Simple Doctest
~~~~~~~~~~~~~~

.. code-block:: python

   def add(a, b):
       """Add two numbers.
       
       >>> add(2, 3)
       5
       >>> add(10, 20)
       30
       """
       return a + b

Floating Point
~~~~~~~~~~~~~~

.. code-block:: python

   def calculate_pi():
       """Calculate pi approximation.
       
       >>> calculate_pi()  # doctest: +FLOAT_CMP
       3.14159265
       """
       return 3.14159265358979

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx.ext.doctest',
   ]
   
   # pytest configuration in pyproject.toml
   # [tool.pytest.ini_options]
   # doctest_plus = "enabled"

Options
~~~~~~~

.. code-block:: python

   doctest_global_setup = '''
   import numpy as np
   import pandas as pd
   '''
   
   doctest_test_doctest_blocks = 'default'

Examples
--------

Array Comparison
~~~~~~~~~~~~~~~~

.. code-block:: python

   def create_array():
       """Create numpy array.
       
       >>> import numpy as np
       >>> create_array()  # doctest: +FLOAT_CMP
       array([1., 2., 3.])
       """
       return np.array([1.0, 2.0, 3.0])

Additional Resources
--------------------
- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `Pytest Doctestplus Documentation <https://github.com/astropy/pytest-doctestplus>`_
- `Python Doctest <https://docs.python.org/3/library/doctest.html>`_
- :doc:`../tutorials/packages/pytest-doctestplus` - Complete tutorial
- pytest documentation: https://docs.pytest.org/
- GitHub repository: https://github.com/astropy/pytest-doctestplus

