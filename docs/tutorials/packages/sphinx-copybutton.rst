sphinx-copybutton Tutorial
===========================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-copybutton/>`_
   - :doc:`See Working Example <../../examples/sphinx-copybutton-example>`
   - `Official Documentation <https://sphinx-copybutton.readthedocs.io/>`_


The ``sphinx-copybutton`` extension adds a "copy" button to code blocks, making it easy 
for users to copy code examples.

Installation
------------

Already included in this container!

In your own environment:

.. code-block:: bash

   pip install sphinx-copybutton

Configuration
-------------

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_copybutton',
   ]

Basic Usage
-----------

The extension automatically adds copy buttons to all code blocks:

.. code-block:: python

   def hello_world():
       print("Hello, World!")

Try hovering over the code block above - you should see a copy button appear!

Advanced Configuration
----------------------

Customize Prompt Removal
~~~~~~~~~~~~~~~~~~~~~~~~~

Remove Python prompts (``>>>`` and ``...``):

.. code-block:: python

   copybutton_prompt_text = r">>> |\.\.\. "
   copybutton_prompt_is_regexp = True

Example with prompts:

.. code-block:: python

   >>> x = 10
   >>> y = 20
   >>> print(x + y)
   30

The copy button will exclude the ``>>>`` prompts!

Remove Shell Prompts
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   copybutton_prompt_text = r"\$ "
   copybutton_prompt_is_regexp = True

Example:

.. code-block:: bash

   $ ls -la
   $ cd myproject
   $ python script.py

Custom Button Text
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   copybutton_copy_text = "Copy"
   copybutton_copied_text = "Copied!"

Exclude Specific Code Blocks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   copybutton_selector = "div:not(.no-copybutton) > div.highlight > pre"

Then use:

.. code-block:: rst

   .. code-block:: python
      :class: no-copybutton
      
      # This block won't have a copy button
      secret_code = "do-not-copy"

Multiple Prompts
~~~~~~~~~~~~~~~~

Handle multiple prompt styles:

.. code-block:: python

   copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
   copybutton_prompt_is_regexp = True

This handles:
- Python (``>>>``, ``...``)
- Shell (``$``)
- IPython (``In [1]:``, ``...::``)

Complete Example
----------------

Full ``conf.py`` configuration:

.. code-block:: python

   # conf.py
   
   extensions = [
       'sphinx_copybutton',
       'sphinx.ext.autodoc',
   ]
   
   # Copybutton configuration
   copybutton_prompt_text = r">>> |\.\.\. |\$ "
   copybutton_prompt_is_regexp = True
   copybutton_only_copy_prompt_lines = True
   copybutton_remove_prompts = True
   copybutton_copy_text = "📋 Copy"
   copybutton_copied_text = "✅ Copied!"
   copybutton_image_path = "copy-button.svg"
   copybutton_selector = "pre"

Usage Examples
--------------

Python Interactive
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   >>> import numpy as np
   >>> arr = np.array([1, 2, 3, 4, 5])
   >>> print(arr.mean())
   3.0

Shell Commands
~~~~~~~~~~~~~~

.. code-block:: bash

   $ docker build -t myapp .
   $ docker run -p 8080:8080 myapp

Code Files
~~~~~~~~~~

.. code-block:: python

   # calculator.py
   class Calculator:
       def add(self, a, b):
           return a + b
       
       def multiply(self, a, b):
           return a * b

JSON Configuration
~~~~~~~~~~~~~~~~~~

.. code-block:: json

   {
       "name": "myproject",
       "version": "1.0.0",
       "dependencies": {
           "sphinx": "^7.0.0",
           "sphinx-copybutton": "^0.5.0"
       }
   }

Benefits
--------

1. **Improved UX**: Users can easily copy code
2. **Reduces Errors**: No manual selection mistakes
3. **Professional**: Modern, polished documentation
4. **Accessibility**: Easier for all users
5. **Mobile-Friendly**: Works on touch devices

Best Practices
--------------

1. **Always Use**: Enable for all documentation
2. **Remove Prompts**: Configure prompt removal
3. **Test**: Verify copy functionality works
4. **Customize**: Match your theme colors
5. **Accessibility**: Ensure keyboard navigation works

Styling
-------

Custom CSS for the button:

.. code-block:: css

   /* _static/custom.css */
   
   button.copybtn {
       background-color: #2196F3;
       border: none;
       color: white;
       padding: 4px 8px;
       border-radius: 4px;
       cursor: pointer;
       opacity: 0.7;
       transition: opacity 0.3s;
   }
   
   button.copybtn:hover {
       opacity: 1;
   }
   
   button.copybtn:active {
       background-color: #0b7dda;
   }

Add to ``conf.py``:

.. code-block:: python

   html_css_files = ['custom.css']

Troubleshooting
---------------

Button Not Appearing
~~~~~~~~~~~~~~~~~~~~

Check that the extension is loaded:

.. code-block:: python

   extensions = ['sphinx_copybutton']

Verify in build output:

.. code-block:: text

   loading intersphinx inventory...
   loading sphinx_copybutton extension...

Prompts Not Removed
~~~~~~~~~~~~~~~~~~~

Ensure regex is correct:

.. code-block:: python

   copybutton_prompt_text = r">>> "
   copybutton_prompt_is_regexp = True
   copybutton_remove_prompts = True

Test regex at https://regex101.com/

Theme Compatibility
~~~~~~~~~~~~~~~~~~~

Some themes may need custom CSS. Check theme documentation.

Resources
---------

* `sphinx-copybutton Documentation <https://sphinx-copybutton.readthedocs.io/>`_
* `GitHub Repository <https://github.com/executablebooks/sphinx-copybutton>`_
* `PyPI Page <https://pypi.org/project/sphinx-copybutton/>`_

Video Tutorial
--------------

.. raw:: html

   <iframe width="560" height="315" 
   src="https://www.youtube.com/embed/oJsUvBQyHBs?start=350" 
   title="Sphinx Copy Button Tutorial" 
   frameborder="0" 
   allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
   allowfullscreen></iframe>

Try It Now
----------

Copy any code block on this page to see the extension in action!

.. code-block:: python

   # Try copying this!
   def greet(name):
       return f"Hello, {name}!"
   
   print(greet("Sphinx User"))
