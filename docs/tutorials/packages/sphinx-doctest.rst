Sphinx Doctest Tutorial
=======================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-doctest/>`_

This tutorial demonstrates how to use sphinx-doctest in your Sphinx documentation.

What is Sphinx Doctest?
-----------------------
sphinx-doctest is a Sphinx extension that provides:

- Enhanced doctest integration
- Easy integration with Sphinx
- Comprehensive configuration options
- Professional documentation output

sphinx-doctest provides:

- Enhanced doctest integration
- Integration with Sphinx documentation
- Flexible configuration options
- Professional output formatting

Key Features
~~~~~~~~~~~~

- **Code Testing**: Test code examples in documentation
- **Test Groups**: Organize tests into logical groups
- **Setup/Cleanup**: Add setup and cleanup code for tests
- **Flexible Options**: Control test behavior with options


Installation
------------

sphinx-doctest is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinx.ext.doctest; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``docs/conf.py``:

.. code-block:: python

   extensions = [
       'sphinx.ext.doctest',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinx.ext.doctest']
   
   # Configuration options
   doctest_test_doctest_blocks = 'default'
   doctest_global_setup = '''
   import sys
   import os
   '''
   doctest_global_cleanup = ''


Complete configuration with all features:

.. code-block:: python

   extensions = ['sphinx.ext.doctest']
   
   # Package-specific configuration
   doctest_test_doctest_blocks = 'default'
   doctest_path = ['.']
   
   # Global setup code
   doctest_global_setup = '''
   import sys
   import os
   from pathlib import Path
   '''
   
   # Global cleanup code
   doctest_global_cleanup = '''
   # Cleanup code here
   '''

Basic Usage
-----------

Getting Started
~~~~~~~~~~~~~~~

Here's a basic example of using sphinx-doctest:

.. code-block:: rst

   .. doctest::
   
      >>> 2 + 2
      4
      >>> print("Hello, World!")
      Hello, World!

Doctest Blocks
~~~~~~~~~~~~~~

Use doctest directive for code testing:

.. code-block:: rst

   .. testcode::
   
      def add(a, b):
          return a + b
      
      result = add(2, 3)
   
   .. testoutput::
   
      5

Common Use Cases
----------------

Testing Code Examples
~~~~~~~~~~~~~~~~~~~~~~

Test code examples in documentation:

.. code-block:: rst

   .. doctest::
      :options: +NORMALIZE_WHITESPACE
   
      >>> from mymodule import MyClass
      >>> obj = MyClass()
      >>> obj.method()
      'expected output'

Setup and Cleanup
~~~~~~~~~~~~~~~~~~

Add setup and cleanup code:

.. code-block:: rst

   .. testsetup::
   
      import tempfile
      import os
      test_dir = tempfile.mkdtemp()
   
   .. doctest::
   
      >>> os.path.exists(test_dir)
      True
   
   .. testcleanup::
   
      import shutil
      shutil.rmtree(test_dir)

Advanced Features
-----------------

Skipping Tests
~~~~~~~~~~~~~~

Skip specific tests:

.. code-block:: rst

   .. doctest::
      :options: +SKIP
   
      >>> # This test will be skipped
      >>> raise NotImplementedError()

Test Groups
~~~~~~~~~~~

Organize tests into groups:

.. code-block:: rst

   .. testcode:: group1
   
      x = 5
   
   .. testcode:: group1
   
      print(x)
   
   .. testoutput:: group1
   
      5

Best Practices
--------------

Tips and Guidelines
~~~~~~~~~~~~~~~~~~~

- Test all code examples in documentation
- Use appropriate doctest options
- Keep tests simple and focused
- Add setup/cleanup when needed
- Run doctests regularly as part of CI/CD

Troubleshooting
---------------

Common Issues
~~~~~~~~~~~~~

**Issue**: Doctest failures

**Solution**: Check expected output format and whitespace.

**Issue**: Import errors

**Solution**: Add necessary imports to doctest_global_setup.


Practical Examples
------------------

Overview
--------


Key Features
~~~~~~~~~~~~

- **Code Testing**: Test code examples in documentation
- **Test Groups**: Organize tests into logical groups
- **Setup/Cleanup**: Add setup and cleanup code for tests
- **Flexible Options**: Control test behavior with options

Installation
------------

Using pip
~~~~~~~~~

The doctest extension is built into Sphinx:

.. code-block:: bash

   pip install sphinx>=5.0.0

Configuration
-------------

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx.ext.doctest',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

Complete configuration with all features:

.. code-block:: python

   extensions = ['sphinx.ext.doctest']
   
   # Package-specific configuration
   doctest_test_doctest_blocks = 'default'
   doctest_path = ['.']
   
   # Global setup code
   doctest_global_setup = '''
   import sys
   import os
   from pathlib import Path
   '''
   
   # Global cleanup code
   doctest_global_cleanup = '''
   # Cleanup code here
   '''

Basic Usage
-----------

Example 1: Simple Doctest
~~~~~~~~~~~~~~~~~~~~~~~~~~

Here's a basic example:

.. code-block:: rst

   .. doctest::
   
      >>> 2 + 2
      4
      >>> "hello".upper()
      'HELLO'

Example 2: Test Code Blocks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Test complete code blocks:

.. code-block:: rst

   .. testcode::
   
      def multiply(a, b):
          """Multiply two numbers."""
          return a * b
      
      result = multiply(3, 4)
      print(result)
   
   .. testoutput::
   
      12

Real-World Examples
-------------------

Example: Testing a Calculator Class
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A practical testing example:

.. code-block:: rst

   Calculator Documentation
   ========================
   
   .. testsetup::
   
      class Calculator:
          def add(self, a, b):
              return a + b
          
          def subtract(self, a, b):
              return a - b
          
          def multiply(self, a, b):
              return a * b
          
          def divide(self, a, b):
              if b == 0:
                  raise ValueError("Cannot divide by zero")
              return a / b
   
   Basic Operations
   ----------------
   
   .. doctest::
   
      >>> calc = Calculator()
      >>> calc.add(5, 3)
      8
      >>> calc.subtract(10, 4)
      6
      >>> calc.multiply(3, 7)
      21
      >>> calc.divide(15, 3)
      5.0
   
   Error Handling
   --------------
   
   .. doctest::
   
      >>> calc.divide(10, 0)
      Traceback (most recent call last):
          ...
      ValueError: Cannot divide by zero

Best Practices
--------------

Recommendations
~~~~~~~~~~~~~~~

- Test all code examples
- Use appropriate options for output formatting
- Add setup code when needed
- Keep tests maintainable
- Run doctests as part of build process

Common Patterns
~~~~~~~~~~~~~~~

Standard patterns for using sphinx-doctest:

1. **Simple Tests**: Use doctest directive for interactive examples
2. **Code Blocks**: Use testcode/testoutput for larger examples
3. **Test Groups**: Organize related tests together

Integration Tips
----------------

Working with Other Extensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

sphinx-doctest integrates well with:

- sphinx-autodoc for API documentation
- pytest-doctestplus for enhanced testing
- Standard Sphinx extensions

Additional Resources
--------------------

- `PyPI Package <https://pypi.org/project/sphinx-doctest/>`_
- `Sphinx Doctest Documentation <https://www.sphinx-doc.org/en/master/usage/extensions/doctest.html>`_
- :doc:`Complete Tutorial <../tutorials/packages/sphinx-doctest>`
- `Sphinx Documentation <https://www.sphinx-doc.org/en/master/usage/extensions/doctest.html>`_
- :ref:`Package API Documentation <pdoc-sphinx-doctest>`
Next Steps
----------
- Explore the :doc:`tutorial <../tutorials/packages/sphinx-doctest>`
- Check the official documentation
- Try the examples in your own projects
- Customize for your specific needs

