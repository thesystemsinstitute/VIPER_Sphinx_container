Flake8 Markdown Tutorial
========================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/flake8-markdown/>`_
   - :doc:`See Working Example <../../examples/flake8-markdown-example>`


This tutorial demonstrates how to use flake8-markdown, a linter for Python code in Markdown files.

What is Flake8 Markdown?
-----------------------

Flake8 Markdown provides features for:

- Core functionality
- Integration with Sphinx
- Configuration options
- Advanced features
- Best practices

Installation
------------

Install via pip:

.. code-block:: bash

   pip install flake8-markdown

Configuration
-------------

Add to your Sphinx ``conf.py``:

.. code-block:: python

   extensions = [
       'flake8_markdown',
   ]

Basic Usage
-----------

Simple Example
~~~~~~~~~~~~~~

Basic usage example:

.. code-block:: python

   # Example code here
   pass

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

Advanced configuration options:

.. code-block:: python

   # Configuration in conf.py
   flake8_markdown_config = {
       'option1': 'value1',
       'option2': 'value2',
   }

Best Practices
--------------

1. Follow documentation conventions
2. Use appropriate settings
3. Test thoroughly
4. Keep configuration simple
5. Document usage patterns

Common Issues
-------------

Issue 1
~~~~~~~

**Problem:** Common issue description

**Solution:** How to resolve it

Issue 2
~~~~~~~

**Problem:** Another common issue

**Solution:** Resolution steps

Resources
---------

- `Official Documentation <https://pypi.org/project/flake8-markdown/>`_
- `PyPI Package <https://pypi.org/project/flake8-markdown/>`_
- :doc:`Example Usage <../../examples/flake8-markdown-example>`

See Also
--------

- :doc:`Sphinx Basics <../sphinx-basics>`
- :doc:`Package Overview <../../sphinx-packages>`
