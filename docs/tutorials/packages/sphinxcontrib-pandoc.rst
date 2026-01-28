Sphinxcontrib Pandoc Tutorial
=============================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinxcontrib-pandoc/>`_
   - :doc:`See Working Example <../../examples/sphinxcontrib-pandoc-example>`

This tutorial demonstrates how to use sphinxcontrib-pandoc in your Sphinx documentation.

What is Sphinxcontrib Pandoc?
------------------------------

sphinxcontrib-pandoc is a Sphinx extension that provides:

- Pandoc integration for Sphinx
- Easy integration with Sphinx
- Comprehensive configuration options
- Professional documentation output

sphinxcontrib-pandoc provides:

- Pandoc integration for Sphinx
- Integration with Sphinx documentation
- Flexible configuration options
- Professional output formatting

Key Features
~~~~~~~~~~~~

- **Format Conversion**: Convert to multiple formats
- **Pandoc Power**: Leverage Pandoc's conversion capabilities
- **Custom Templates**: Use custom Pandoc templates
- **Flexible Options**: Configure Pandoc behavior
Installation
------------

sphinxcontrib-pandoc is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinxcontrib.pandoc; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``docs/conf.py``:

.. code-block:: python

   extensions = [
       'sphinxcontrib.pandoc',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinxcontrib.pandoc']
   
   # Configuration options
   pandoc_builder_name = 'pandoc'
   pandoc_format = 'markdown'
   pandoc_options = ['--standalone', '--toc']


Complete configuration with all features:

.. code-block:: python

   extensions = ['sphinxcontrib.pandoc']
   
   # Package-specific configuration
   pandoc_builder_name = 'pandoc'
   pandoc_format = 'markdown'
   
   # Pandoc options
   pandoc_options = [
       '--standalone',
       '--toc',
       '--toc-depth=3',
       '--markdown-headings=atx',
   ]
   
   # Template
   pandoc_template = None

Basic Usage
-----------

Getting Started
~~~~~~~~~~~~~~~

Convert documentation with Pandoc:

.. code-block:: bash

   sphinx-build -b pandoc docs docs/_build/pandoc

Convert to Different Formats
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Generate various output formats:

.. code-block:: bash

   # Markdown
   sphinx-build -b pandoc -D pandoc_format=markdown docs docs/_build/md
   
   # DOCX
   sphinx-build -b pandoc -D pandoc_format=docx docs docs/_build/docx

Common Use Cases
----------------

Markdown Export
~~~~~~~~~~~~~~~

Export documentation to Markdown:

.. code-block:: python

   # In conf.py
   pandoc_format = 'markdown'
   pandoc_options = [
       '--standalone',
       '--toc',
       '--markdown-headings=atx',
   ]

DOCX Generation
~~~~~~~~~~~~~~~

Generate Word documents:

.. code-block:: python

   pandoc_format = 'docx'
   pandoc_options = [
       '--reference-doc=template.docx',
   ]

Advanced Features
-----------------

Custom Templates
~~~~~~~~~~~~~~~~

Use custom Pandoc templates:

.. code-block:: python

   pandoc_options = [
       '--template=custom-template.latex',
       '--standalone',
   ]

Multiple Formats
~~~~~~~~~~~~~~~~

Configure multiple output formats:

.. code-block:: python

   # Build script
   formats = ['markdown', 'docx', 'epub', 'latex']
   for fmt in formats:
       # Build each format

Best Practices
--------------

Tips and Guidelines
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Install Pandoc system-wide
- Use appropriate format options
- Test conversions regularly
- Maintain format-specific templates
- Review converted output

Troubleshooting
---------------

Common Issues
~~~~~~~~~~~~~

**Issue**: Pandoc not found

**Solution**: Install Pandoc: ``sudo apt-get install pandoc``

**Issue**: Conversion errors

**Solution**: Check Pandoc options and input format compatibility.

Additional Resources
--------------------

- :doc:`Working Example <../../examples/sphinxcontrib-pandoc-example>`
- `PyPI Package <https://pypi.org/project/sphinxcontrib-pandoc/>`_
