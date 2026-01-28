Sphinx-Copybutton Example
=========================

This page demonstrates the **sphinx-copybutton** extension for adding copy buttons to code blocks.

.. contents:: Contents
   :local:
   :depth: 2

Overview
--------

The sphinx-copybutton extension adds a small copy button to code blocks, making it easy for users to copy code snippets.

Basic Usage
-----------

Code Blocks
~~~~~~~~~~~

The copy button appears automatically on all code blocks:

.. code-block:: python

   def hello_world():
       print("Hello, World!")

.. code-block:: bash

   pip install sphinx-copybutton

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_copybutton',
   ]

Options
~~~~~~~

.. code-block:: python

   copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
   copybutton_prompt_is_regexp = True
   copybutton_only_copy_prompt_lines = True
   copybutton_remove_prompts = True

Custom Styling
~~~~~~~~~~~~~~

.. code-block:: python

   copybutton_selector = "div.highlight pre"
   copybutton_image_path = "copy-button.svg"

Examples
--------

Python REPL
~~~~~~~~~~~

.. code-block:: python

   >>> x = 10
   >>> y = 20
   >>> x + y
   30

Shell Commands
~~~~~~~~~~~~~~

.. code-block:: bash

   $ git clone https://github.com/user/repo.git
   $ cd repo
   $ pip install -e .

See Also
--------

- :doc:`../tutorials/packages/sphinx-copybutton` - Complete tutorial
- GitHub repository: https://github.com/executablebooks/sphinx-copybutton
