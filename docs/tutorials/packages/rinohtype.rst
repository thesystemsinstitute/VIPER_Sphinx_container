Rinohtype Tutorial
==================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/rinohtype/>`_
   - :doc:`See Working Example <../../examples/rinohtype-example>`
   - `Official Documentation <https://www.mos6581.org/rinohtype/>`_

This tutorial demonstrates how to use rinohtype in your Sphinx documentation.

What is Rinohtype?
------------------

rinohtype is a Sphinx extension that provides:

- PDF renderer for Sphinx
- Easy integration with Sphinx
- Comprehensive configuration options
- Professional documentation output

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

Additional Resources
--------------------

- :doc:`Working Example <../../examples/rinohtype-example>`
- `PyPI Package <https://pypi.org/project/rinohtype/>`_
- `Official Documentation <https://www.mos6581.org/rinohtype/>`_
