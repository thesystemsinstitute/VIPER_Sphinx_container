Sphinx Doctest Tutorial
=======================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-doctest/>`_
   - :doc:`See Working Example <../../examples/sphinx-doctest-example>`

This tutorial demonstrates how to use sphinx-doctest in your Sphinx documentation.

What is Sphinx Doctest?
-----------------------

sphinx-doctest is a Sphinx extension that provides:

- Enhanced doctest integration
- Easy integration with Sphinx
- Comprehensive configuration options
- Professional documentation output

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

Additional Resources
--------------------

- :doc:`Working Example <../../examples/sphinx-doctest-example>`
- `PyPI Package <https://pypi.org/project/sphinx-doctest/>`_
- `Sphinx Doctest Documentation <https://www.sphinx-doc.org/en/master/usage/extensions/doctest.html>`_
