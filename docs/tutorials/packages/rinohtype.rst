Rinohtype Tutorial
==================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/rinohtype/>`_
   - `API Documentation <../../pdoc/rinohtype/index.html>`_
   - `Manual <https://www.mos6581.org/rinohtype/>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use rinohtype in your Sphinx documentation.

What is Rinohtype?
------------------
rinohtype is a Sphinx extension that provides:

- PDF renderer for Sphinx
- Easy integration with Sphinx
- Comprehensive configuration options
- Professional documentation output

rinohtype provides:

- PDF renderer for Sphinx
- Integration with Sphinx documentation
- Flexible configuration options
- Professional output formatting

Key Features
~~~~~~~~~~~~

- **PDF Generation**: High-quality PDF output from RST
- **Custom Templates**: Multiple document templates
- **Styling**: Rich styling and formatting options
- **Typography**: Professional typography support


Installation
------------

rinohtype is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import rinoh; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``docs/conf.py``:

.. code-block:: python

   extensions = [
       'rinoh.frontend.sphinx',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['rinoh.frontend.sphinx']
   
   # Configuration options
   rinoh_documents = [
       dict(doc='index',
            target='manual',
            title='Project Documentation',
            author='Your Name')
   ]
   
   rinoh_template = 'book'
   rinoh_paper_size = 'A4'


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'rinoh.frontend.sphinx',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

Complete configuration with all features:

.. code-block:: python

   extensions = ['rinoh.frontend.sphinx']
   
   # Package-specific configuration
   rinoh_documents = [
       dict(
           doc='index',
           target='manual',
           title='Project Documentation',
           subtitle='Complete Guide',
           author='Your Name',
           date='2026',
           template='book',
       )
   ]
   
   # PDF settings
   rinoh_paper_size = 'A4'
   rinoh_page_orientation = 'portrait'
   rinoh_columns = 1
   
   # Styling
   rinoh_stylesheet = 'sphinx_base14'
   rinoh_logo = '_static/logo.pdf'
   
   # Table of contents
   rinoh_toc_depth = 3

Basic Usage
-----------

Getting Started
~~~~~~~~~~~~~~~

Build PDF documentation:

.. code-block:: bash

   sphinx-build -b rinoh docs docs/_build/rinoh

Generate PDF
~~~~~~~~~~~~

Create PDF from RST files:

.. code-block:: bash

   make rinoh

Common Use Cases
----------------

Custom PDF Template
~~~~~~~~~~~~~~~~~~~

Create custom PDF styling:

.. code-block:: python

   # In conf.py
   rinoh_documents = [
       dict(
           doc='index',
           target='manual',
           title='My Project',
           author='Author Name',
           template='book',
       )
   ]

Multi-document PDF
~~~~~~~~~~~~~~~~~~

Generate multiple PDFs:

.. code-block:: python

   rinoh_documents = [
       dict(doc='index', target='manual', title='User Manual'),
       dict(doc='api', target='api', title='API Reference'),
   ]

Advanced Features
-----------------

Custom Styling
~~~~~~~~~~~~~~

Apply custom styles:

.. code-block:: python

   # In conf.py
   rinoh_stylesheet = 'custom.rts'
   rinoh_template = 'article'
   
   # Custom options
   rinoh_paper_size = 'letter'
   rinoh_logo = '_static/logo.pdf'

Page Layout
~~~~~~~~~~~

Configure page layout:

.. code-block:: python

   rinoh_page_size = 'A4'
   rinoh_page_orientation = 'portrait'
   rinoh_columns = 1

Best Practices
--------------

Tips and Guidelines
~~~~~~~~~~~~~~~~~~~

- Test PDF builds regularly
- Use appropriate templates
- Optimize images for PDF
- Configure page breaks appropriately
- Review PDF output for formatting

Troubleshooting
---------------

Common Issues
~~~~~~~~~~~~~

**Issue**: Build fails with missing fonts

**Solution**: Install required fonts or use alternative fonts in configuration.

**Issue**: Images not rendering properly

**Solution**: Use PDF-compatible image formats (PNG, PDF).


Practical Examples
------------------

Overview
--------


Key Features
~~~~~~~~~~~~

- **PDF Generation**: High-quality PDF output from RST
- **Custom Templates**: Multiple document templates
- **Styling**: Rich styling and formatting options
- **Typography**: Professional typography support

Installation
------------

Using pip
~~~~~~~~~

Install the extension:

.. code-block:: bash

   pip install rinohtype

Or add to your ``requirements.txt``:

.. code-block:: text

   rinohtype
   sphinx>=5.0.0

Configuration
-------------

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'rinoh.frontend.sphinx',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

Complete configuration with all features:

.. code-block:: python

   extensions = ['rinoh.frontend.sphinx']
   
   # Package-specific configuration
   rinoh_documents = [
       dict(
           doc='index',
           target='manual',
           title='Project Documentation',
           subtitle='Complete Guide',
           author='Your Name',
           date='2026',
           template='book',
       )
   ]
   
   # PDF settings
   rinoh_paper_size = 'A4'
   rinoh_page_orientation = 'portrait'
   rinoh_columns = 1
   
   # Styling
   rinoh_stylesheet = 'sphinx_base14'
   rinoh_logo = '_static/logo.pdf'
   
   # Table of contents
   rinoh_toc_depth = 3

Basic Usage
-----------

Example 1: Build PDF
~~~~~~~~~~~~~~~~~~~~

Generate PDF documentation:

.. code-block:: bash

   # Using sphinx-build
   sphinx-build -b rinoh docs docs/_build/rinoh
   
   # Using make
   make rinoh
   
   # Output location
   # docs/_build/rinoh/manual.pdf

Example 2: Multiple PDFs
~~~~~~~~~~~~~~~~~~~~~~~~

Generate multiple PDF documents:

.. code-block:: python

   # In conf.py
   rinoh_documents = [
       dict(
           doc='index',
           target='user-manual',
           title='User Manual',
           template='book',
       ),
       dict(
           doc='api/index',
           target='api-reference',
           title='API Reference',
           template='article',
       ),
   ]

Real-World Examples
-------------------

Example: Complete Book Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Full book-style documentation:

.. code-block:: python

   # docs/conf.py
   extensions = ['rinoh.frontend.sphinx']
   
   rinoh_documents = [
       dict(
           doc='index',
           target='complete-guide',
           title='Complete Python Project Guide',
           subtitle='From Beginner to Expert',
           author='John Doe',
           date='2026',
           template='book',
           logo='_static/logo.pdf',
           cover='_static/cover.pdf',
       )
   ]
   
   # Paper and layout
   rinoh_paper_size = 'A4'
   rinoh_page_orientation = 'portrait'
   rinoh_columns = 1
   
   # Typography
   rinoh_stylesheet = 'sphinx_article'
   
   # Table of contents
   rinoh_toc_depth = 3
   rinoh_toc_max_depth = 4

Example: Article Template
~~~~~~~~~~~~~~~~~~~~~~~~~~

Technical article configuration:

.. code-block:: python

   rinoh_documents = [
       dict(
           doc='whitepaper',
           target='technical-whitepaper',
           title='Advanced Topic Deep Dive',
           author='Technical Team',
           template='article',
       )
   ]
   
   rinoh_paper_size = 'letter'
   rinoh_stylesheet = 'sphinx_base14'

Example: Custom Styling
~~~~~~~~~~~~~~~~~~~~~~~

Create custom stylesheet ``custom.rts``:

.. code-block:: text

   # custom.rts
   [STYLESHEET]
   name = Custom Style
   base = sphinx
   
   [heading1]
   typeface = $(sans_typeface)
   font-weight = BOLD
   font-size = 18pt
   
   [body]
   typeface = $(serif_typeface)
   font-size = 11pt
   line-spacing = 1.2

Then use in ``conf.py``:

.. code-block:: python

   rinoh_stylesheet = 'custom.rts'

Best Practices
--------------

Recommendations
~~~~~~~~~~~~~~~

- Use appropriate templates (book vs article)
- Optimize images for PDF (PNG, PDF formats)
- Test PDF builds regularly
- Configure appropriate page sizes
- Use semantic markup in RST

Common Patterns
~~~~~~~~~~~~~~~

Standard patterns for using rinohtype:

1. **User Manual**: Use book template with TOC
2. **API Reference**: Use article template
3. **White Papers**: Use article with custom styling

Integration Tips
----------------

Working with Other Extensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

rinohtype integrates well with:

- rst2pdf for alternative PDF generation
- sphinx-build for standard builds
- Standard Sphinx extensions

Additional Resources
--------------------

- `PyPI Package <https://pypi.org/project/rinohtype/>`_
- `Official Documentation <https://www.mos6581.org/rinohtype/>`_
- :doc:`Complete Tutorial <../tutorials/packages/rinohtype>`
- :ref:`Package API Documentation <pdoc-rinohtype>`
Next Steps
----------
- Explore the :doc:`tutorial <../tutorials/packages/rinohtype>`
- Check the official documentation
- Try the examples in your own projects
- Customize for your specific needs

