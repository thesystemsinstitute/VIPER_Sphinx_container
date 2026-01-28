EPUB2Sphinx Example
===================

This page demonstrates the **epub2sphinx** extension for importing and converting EPUB documents into Sphinx documentation.

.. contents:: Contents
   :local:
   :depth: 2

Overview
--------

The epub2sphinx extension converts EPUB ebooks into reStructuredText format for integration with Sphinx documentation projects.

Basic Conversion
----------------

Import EPUB
~~~~~~~~~~~

.. code-block:: python

   from epub2sphinx import convert_epub
   
   convert_epub('book.epub', 'docs/source/')

This imports the EPUB content into your Sphinx project.

Conversion Options
------------------

With Images
~~~~~~~~~~~

.. code-block:: python

   convert_epub('book.epub', 'docs/source/', 
                extract_images=True,
                image_dir='_images/')

Preserve Structure
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   convert_epub('book.epub', 'docs/source/',
                preserve_structure=True,
                split_chapters=True)

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'epub2sphinx',
   ]
   
   epub2sphinx_output_format = 'rst'

Advanced Options
~~~~~~~~~~~~~~~~

.. code-block:: python

   epub2sphinx_options = {
       'extract_toc': True,
       'convert_images': True,
       'clean_html': True,
   }

Practical Examples
------------------

Book Documentation
~~~~~~~~~~~~~~~~~~

Convert technical books to documentation:

.. code-block:: python

   # Convert programming book
   convert_epub('python_guide.epub', 'docs/',
                split_chapters=True,
                create_toctree=True)

Manual Import
~~~~~~~~~~~~~

.. code-block:: python

   # Import user manual
   convert_epub('user_manual.epub', 'docs/manual/',
                prefix='manual_')

See Also
--------

- :doc:`../tutorials/packages/epub2sphinx` - Complete tutorial
- EPUB format: https://www.w3.org/publishing/epub3/
- GitHub repository: https://github.com/sphinx-doc/epub2sphinx
