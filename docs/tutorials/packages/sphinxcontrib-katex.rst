Sphinxcontrib Katex Tutorial
============================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinxcontrib-katex/>`_
   - `API Documentation <../../pdoc/sphinxcontrib_katex/index.html>`_
   - `Manual <https://sphinxcontrib-katex.readthedocs.io/>`_
   - :doc:`Working Example <../../examples/sphinxcontrib-katex-example>`


.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinxcontrib-katex in your Sphinx documentation.

What is Sphinxcontrib Katex?
-----------------------------
sphinxcontrib-katex is a Sphinx extension that provides:

- KaTeX math rendering
- Easy integration with Sphinx
- Comprehensive configuration options
- Professional documentation output

sphinxcontrib-katex provides:

- KaTeX math rendering
- Integration with Sphinx documentation
- Flexible configuration options
- Professional output formatting

Key Features
~~~~~~~~~~~~

- **Fast Rendering**: Client-side math rendering with KaTeX
- **LaTeX Support**: Full LaTeX math syntax support
- **Inline & Display**: Both inline and display math modes
- **Customizable**: Configure delimiters and options


Installation
------------

sphinxcontrib-katex is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinxcontrib.katex; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``docs/conf.py``:

.. code-block:: python

   extensions = [
       'sphinxcontrib.katex',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinxcontrib.katex']
   
   # Configuration options
   katex_css_path = 'https://cdn.jsdelivr.net/npm/katex@0.16.0/dist/katex.min.css'
   katex_js_path = 'https://cdn.jsdelivr.net/npm/katex@0.16.0/dist/katex.min.js'
   katex_autorender_path = 'https://cdn.jsdelivr.net/npm/katex@0.16.0/dist/contrib/auto-render.min.js'
   katex_inline = [r'\(', r'\)']
   katex_display = [r'\[', r'\]']
   katex_options = {'displayMode': True}


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinxcontrib.katex',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

Complete configuration with all features:

.. code-block:: python

   extensions = ['sphinxcontrib.katex']
   
   # Package-specific configuration
   katex_css_path = 'https://cdn.jsdelivr.net/npm/katex@0.16.0/dist/katex.min.css'
   katex_js_path = 'https://cdn.jsdelivr.net/npm/katex@0.16.0/dist/katex.min.js'
   katex_autorender_path = 'https://cdn.jsdelivr.net/npm/katex@0.16.0/dist/contrib/auto-render.min.js'
   
   # Delimiters
   katex_inline = [r'\(', r'\)']
   katex_display = [r'\[', r'\]']
   
   # KaTeX options
   katex_options = {
       'displayMode': True,
       'throwOnError': False,
       'errorColor': '#cc0000',
       'fleqn': False,
       'macros': {
           r'\RR': r'\mathbb{R}',
           r'\NN': r'\mathbb{N}',
           r'\ZZ': r'\mathbb{Z}',
       }
   }

Basic Usage
-----------

Getting Started
~~~~~~~~~~~~~~~

Write inline math:

.. code-block:: rst

   The equation :math:`E = mc^2` represents energy-mass equivalence.

Display Math
~~~~~~~~~~~~

Use display math for equations:

.. code-block:: rst

   .. math::
   
      \int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}

Common Use Cases
----------------

Inline Equations
~~~~~~~~~~~~~~~~

Embed math in text:

.. code-block:: rst

   The quadratic formula :math:`x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}` 
   solves any quadratic equation.

Complex Equations
~~~~~~~~~~~~~~~~~

Display complex mathematical expressions:

.. code-block:: rst

   .. math::
   
      f(x) = \begin{cases}
         x^2 & \text{if } x \geq 0 \\
         -x^2 & \text{if } x < 0
      \end{cases}

Advanced Features
-----------------

Custom Delimiters
~~~~~~~~~~~~~~~~~

Configure custom math delimiters:

.. code-block:: python

   # In conf.py
   katex_inline = [r'$', r'$']
   katex_display = [r'$$', r'$$']

KaTeX Options
~~~~~~~~~~~~~

Configure KaTeX rendering options:

.. code-block:: python

   katex_options = {
       'displayMode': True,
       'throwOnError': False,
       'errorColor': '#cc0000',
       'macros': {
           r'\RR': r'\mathbb{R}',
       }
   }

Best Practices
--------------

Tips and Guidelines
~~~~~~~~~~~~~~~~~~~

- Use appropriate math environments
- Test complex equations
- Prefer KaTeX for fast rendering
- Use macros for common symbols
- Keep equations readable

Troubleshooting
---------------

Common Issues
~~~~~~~~~~~~~

**Issue**: Math not rendering

**Solution**: Check KaTeX CDN URLs and ensure JavaScript is loading.

**Issue**: Special characters not displaying

**Solution**: Use proper LaTeX escaping.

Additional Resources
--------------------

- :doc:`Working Example <../../examples/sphinxcontrib-katex-example>`
- `PyPI Package <https://pypi.org/project/sphinxcontrib-katex/>`_
- `Official Documentation <https://sphinxcontrib-katex.readthedocs.io/>`_
