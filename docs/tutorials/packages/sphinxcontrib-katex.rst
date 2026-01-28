Sphinxcontrib Katex Tutorial
============================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinxcontrib-katex/>`_
   - `API Documentation <../../pdoc/sphinxcontrib_katex/index.html>`_
   - `Manual <https://sphinxcontrib-katex.readthedocs.io/>`_

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


Practical Examples
------------------

Overview
--------


Key Features
~~~~~~~~~~~~

- **Fast Rendering**: Client-side math rendering with KaTeX
- **LaTeX Support**: Full LaTeX math syntax support
- **Inline & Display**: Both inline and display math modes
- **Customizable**: Configure delimiters and options

Installation
------------

Using pip
~~~~~~~~~

Install the extension:

.. code-block:: bash

   pip install sphinxcontrib-katex

Or add to your ``requirements.txt``:

.. code-block:: text

   sphinxcontrib-katex
   sphinx>=5.0.0

Configuration
-------------

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

Example 1: Inline Math
~~~~~~~~~~~~~~~~~~~~~~

Embed math in text:

.. code-block:: rst

   Einstein's famous equation :math:`E = mc^2` relates energy and mass.
   
   The Pythagorean theorem states that :math:`a^2 + b^2 = c^2` for 
   right triangles.

Example 2: Display Math
~~~~~~~~~~~~~~~~~~~~~~~

Display equations:

.. code-block:: rst

   .. math::
   
      \int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
   
   .. math::
   
      \frac{d}{dx}\left(x^n\right) = nx^{n-1}

Real-World Examples
-------------------

Example: Mathematical Formulas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Common mathematical expressions:

.. code-block:: rst

   Mathematical Constants
   ======================
   
   Euler's Number
   --------------
   
   .. math::
   
      e = \lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n
   
   The Golden Ratio
   ----------------
   
   .. math::
   
      \phi = \frac{1 + \sqrt{5}}{2} \approx 1.618
   
   Trigonometric Identity
   ----------------------
   
   .. math::
   
      \sin^2(\theta) + \cos^2(\theta) = 1

Example: Linear Algebra
~~~~~~~~~~~~~~~~~~~~~~~

Matrix and vector operations:

.. code-block:: rst

   Matrices and Vectors
   ====================
   
   Matrix Multiplication
   ---------------------
   
   .. math::
   
      \mathbf{C} = \mathbf{A}\mathbf{B} = 
      \begin{pmatrix}
         a_{11} & a_{12} \\
         a_{21} & a_{22}
      \end{pmatrix}
      \begin{pmatrix}
         b_{11} & b_{12} \\
         b_{21} & b_{22}
      \end{pmatrix}
   
   Eigenvalues
   -----------
   
   .. math::
   
      \det(\mathbf{A} - \lambda\mathbf{I}) = 0

Example: Calculus
~~~~~~~~~~~~~~~~~

Calculus notation:

.. code-block:: rst

   Calculus Formulas
   =================
   
   Fundamental Theorem of Calculus
   -------------------------------
   
   .. math::
   
      \int_a^b f(x)\,dx = F(b) - F(a)
   
   Chain Rule
   ----------
   
   .. math::
   
      \frac{d}{dx}f(g(x)) = f'(g(x)) \cdot g'(x)
   
   Taylor Series
   -------------
   
   .. math::
   
      f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x-a)^n

Example: Statistics
~~~~~~~~~~~~~~~~~~~

Statistical formulas:

.. code-block:: rst

   Statistical Measures
   ====================
   
   Mean
   ----
   
   .. math::
   
      \mu = \frac{1}{n}\sum_{i=1}^{n} x_i
   
   Standard Deviation
   ------------------
   
   .. math::
   
      \sigma = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(x_i - \mu)^2}
   
   Normal Distribution
   -------------------
   
   .. math::
   
      f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}

Best Practices
--------------

Recommendations
~~~~~~~~~~~~~~~

- Use inline math for simple expressions
- Use display math for complex equations
- Define macros for frequently used symbols
- Test rendering in different browsers
- Keep equations readable and well-formatted

Common Patterns
~~~~~~~~~~~~~~~

Standard patterns for using sphinxcontrib-katex:

1. **Inline Math**: Simple expressions in text
2. **Display Math**: Centered equations with numbering
3. **Aligned Equations**: Multiple related equations

Integration Tips
----------------

Working with Other Extensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

sphinxcontrib-katex integrates well with:

- sphinx.ext.mathjax as an alternative
- Standard Sphinx extensions
- Custom math preprocessing

Additional Resources
--------------------

- `PyPI Package <https://pypi.org/project/sphinxcontrib-katex/>`_
- `Official Documentation <https://sphinxcontrib-katex.readthedocs.io/>`_
- :doc:`Complete Tutorial <../tutorials/packages/sphinxcontrib-katex>`
- `KaTeX Documentation <https://katex.org/>`_
- :ref:`Package API Documentation <pdoc-sphinxcontrib-katex>`
Next Steps
----------
- Explore the :doc:`tutorial <../tutorials/packages/sphinxcontrib-katex>`
- Check the official documentation
- Try the examples in your own projects
- Customize for your specific needs

