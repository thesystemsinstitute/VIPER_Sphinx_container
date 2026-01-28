Sphinxcontrib Katex Tutorial
============================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinxcontrib-katex/>`_
   - :doc:`See Working Example <../../examples/sphinxcontrib-katex-example>`
   - `Official Documentation <https://sphinxcontrib-katex.readthedocs.io/>`_

This tutorial demonstrates how to use sphinxcontrib-katex in your Sphinx documentation.

What is Sphinxcontrib Katex?
-----------------------------

sphinxcontrib-katex is a Sphinx extension that provides:

- KaTeX math rendering
- Easy integration with Sphinx
- Comprehensive configuration options
- Professional documentation output

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
