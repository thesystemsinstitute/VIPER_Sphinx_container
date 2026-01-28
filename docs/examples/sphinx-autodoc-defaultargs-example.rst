Sphinx-Autodoc-Defaultargs Example
===================================

This page demonstrates the **sphinx-autodoc-defaultargs** extension for displaying function default arguments in documentation.

.. contents:: Contents
   :local:
   :depth: 2


Basic Usage
-----------

Function with Defaults
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   def connect(host='localhost', port=5432, timeout=30):
       """Connect to database.
       
       :param host: Database host
       :param port: Database port
       :param timeout: Connection timeout
       """
       pass

With autodoc-defaultargs, the documentation automatically shows:

.. function:: connect(host='localhost', port=5432, timeout=30)

   Connect to database.
   
   :param host: Database host
   :param port: Database port
   :param timeout: Connection timeout

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx.ext.autodoc',
       'sphinx_autodoc_defaultargs',
   ]

Options
~~~~~~~

.. code-block:: python

   autodoc_default_options = {
       'show-defaults': True,
       'default-value-format': 'repr',  # or 'str'
   }

Examples
--------

Complex Defaults
~~~~~~~~~~~~~~~~

.. code-block:: python

   def process_data(items, batch_size=100, options=None, validate=True):
       """Process data in batches."""
       if options is None:
           options = {}
       # process...



Simple Function
~~~~~~~~~~~~~~~

``sphinx_autodoc_defaultargs/utils.py``:

.. literalinclude:: sphinx_autodoc_defaultargs/utils.py
   :language: python


Document:

.. code-block:: rst

   .. autofunction:: sphinx_autodoc_defaultargs.utils.greet


.. autofunction:: sphinx_autodoc_defaultargs.utils.greet


Output shows:

generated documentation: :doc:`sphinx_autodoc_defaultargs/utils`




See Also
--------

- :doc:`../tutorials/packages/sphinx-autodoc-defaultargs` - Complete tutorial
- GitHub repository: https://github.com/sphinx-contrib/autodoc-defaultargs
