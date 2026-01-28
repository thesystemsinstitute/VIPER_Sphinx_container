Epub2Sphinx Tutorial
====================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/epub2sphinx/>`_
   - `API Documentation <../../pdoc/epub2sphinx/index.html>`_
   - `Manual <https://github.com/sphinx-contrib/epub>`_
   - :doc:`Working Example <../../examples/epub2sphinx-example>`


.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use epub2sphinx to convert EPUB ebook files to Sphinx documentation format.

What is Epub2Sphinx?
---------------------
epub2sphinx is a tool that enables:

- Convert EPUB files to reStructuredText
- Import ebook content into Sphinx
- Preserve book structure
- Extract images and media
- Maintain formatting
- Convert chapters to documents
- Table of contents generation
- Metadata preservation
- Multi-format conversion
- Book documentation workflow

This is useful for converting existing ebooks, technical manuals, or publications into maintainable Sphinx documentation.

The epub2sphinx extension converts EPUB ebooks into reStructuredText format for integration with Sphinx documentation projects.


Installation
------------

epub2sphinx is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import epub2sphinx; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'epub2sphinx',
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['epub2sphinx']
   
   # Epub2Sphinx configuration
   epub_to_sphinx_output_dir = 'docs/imported'
   epub_to_sphinx_images_dir = '_static/epub_images'
   epub_to_sphinx_preserve_structure = True
   
   # Conversion options
   epub_to_sphinx_extract_images = True
   epub_to_sphinx_clean_html = True
   epub_to_sphinx_convert_links = True
   
   # Formatting options
   epub_to_sphinx_max_heading_depth = 6
   epub_to_sphinx_code_block_lang = 'python'
   epub_to_sphinx_preserve_metadata = True
   
   # TOC options
   epub_to_sphinx_create_index = True
   epub_to_sphinx_chapter_pattern = 'chapter_{:02d}.rst'


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

Basic Usage
-----------

Convert EPUB File
~~~~~~~~~~~~~~~~~

.. code-block:: bash

   epub2sphinx book.epub -o docs/book

With Custom Options
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   epub2sphinx book.epub \
     --output docs/book \
     --images-dir _static/book_images \
     --preserve-structure

Extract Metadata
~~~~~~~~~~~~~~~~

.. code-block:: bash

   epub2sphinx book.epub --metadata-only

Convert Specific Chapters
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   epub2sphinx book.epub \
     --chapters 1,2,3,4,5 \
     --output docs/intro

   About This Guide
   ----------------
   
   This documentation was automatically converted from the EPUB version
   of our user guide.
   
   .. note::
      
      Some formatting may differ from the original ebook.

Example 2: Programming Book
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Convert a programming book:

.. code-block:: bash

   # Convert programming book
   docker run --rm \
     -v $(pwd):/project \
     kensai-sphinx:latest \
     epub2sphinx /project/books/python_guide.epub \
       --output /project/docs/python_book \
       --code-language python

``docs/python_book/index.rst``:

.. code-block:: rst

   Python Programming Guide
   =========================
   
   Complete Python programming guide converted from EPUB.
   
   .. toctree::
      :maxdepth: 2
      :numbered:
      
      introduction
      basics
      data_structures
      functions
      oop
      advanced
      appendix
   
   Code Examples
   -------------
   
   All code examples from the book are included and can be tested.
   
   .. code-block:: python
      
      # Example from Chapter 1
      def hello():
          print("Hello, World!")
      
      hello()

Example 3: Documentation Archive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Convert multiple EPUB documentation files:

``scripts/convert_books.sh``:

.. code-block:: bash

   #!/bin/bash
   
   # Convert all EPUB files in archive
   for epub in archive/*.epub; do
       basename=$(basename "$epub" .epub)
       echo "Converting $basename..."
       
       docker run --rm \
         -v $(pwd):/project \
         kensai-sphinx:latest \
         epub2sphinx "/project/$epub" \
           --output "/project/docs/archive/$basename" \
           --images-dir "_static/archive_images/$basename"
   done
   
   echo "All books converted!"

``docs/archive/index.rst``:

.. code-block:: rst

   Documentation Archive
   =====================
   
   Historical documentation converted from EPUB format.
   
   .. toctree::
      :maxdepth: 1
      :caption: Archived Manuals:
      
      manual_v1/index
      manual_v2/index
      manual_v3/index
      guide_2024/index
      reference_2025/index
   
   Version History
   ---------------
   
   .. list-table::
      :header-rows: 1
      
      * - Version
        - Release Date
        - Format
        - Status
      * - v3.0
        - 2025-12-01
        - EPUB/Sphinx
        - Current
      * - v2.0
        - 2024-06-15
        - EPUB
        - Archived
      * - v1.0
        - 2023-01-10
        - EPUB
        - Archived

Advanced Features
-----------------

Custom Chapter Naming
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   epub_to_sphinx_chapter_naming = lambda i, title: f"{i:03d}_{title.lower().replace(' ', '_')}.rst"

Metadata Extraction
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Extract and use metadata
   epub_to_sphinx_use_metadata = True
   
   # Metadata will be added as:
   # :Author: Book Author
   # :Publisher: Publisher Name
   # :Date: Publication Date

Image Conversion
~~~~~~~~~~~~~~~~

.. code-block:: bash

   epub2sphinx book.epub \
     --output docs/book \
     --convert-images \
     --image-format png \
     --image-quality 90

HTML Cleaning
~~~~~~~~~~~~~

.. code-block:: bash

   epub2sphinx book.epub \
     --output docs/book \
     --clean-html \
     --remove-styles \
     --fix-links

Custom Processing
~~~~~~~~~~~~~~~~~

Create ``scripts/post_process.py``:

.. code-block:: python

   """Post-process converted EPUB files."""
   import re
   from pathlib import Path
   
   def clean_rst_file(filepath):
       """Clean up converted RST file."""
       content = filepath.read_text(encoding='utf-8')
       
       # Remove extra blank lines
       content = re.sub(r'\n\n\n+', '\n\n', content)
       
       # Fix code blocks
       content = re.sub(
           r'.. code::\s*$',
           '.. code-block:: python',
           content,
           flags=re.MULTILINE
       )
       
       # Fix image paths
       content = content.replace(
           '../images/',
           '/_static/epub_images/'
       )
       
       filepath.write_text(content, encoding='utf-8')
   
   def process_directory(dirpath):
       """Process all RST files in directory."""
       for rst_file in Path(dirpath).glob('**/*.rst'):
           print(f"Processing {rst_file}...")
           clean_rst_file(rst_file)
   
   if __name__ == '__main__':
       process_directory('docs/imported')

Run post-processing:

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     kensai-sphinx:latest \
     python /project/scripts/post_process.py

Table of Contents Generation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Generate master TOC
   def generate_toc(chapters):
       """Generate toctree from chapters."""
       toc = [".. toctree::", "   :maxdepth: 2", ""]
       for chapter in chapters:
           toc.append(f"   {chapter}")
       return '\n'.join(toc)

Docker Integration
------------------

Convert in Container
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     -v $(pwd)/epubs:/epubs \
     kensai-sphinx:latest \
     epub2sphinx /epubs/book.epub \
       --output /project/docs/book

Batch Conversion
~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     kensai-sphinx:latest \
     sh -c "
       for epub in /project/epubs/*.epub; do
         basename=\$(basename \"\$epub\" .epub)
         epub2sphinx \"\$epub\" --output /project/docs/books/\$basename
       done
     "

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Convert EPUB Books
   
   on:
     push:
       paths:
         - 'epubs/**/*.epub'
   
   jobs:
     convert:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Convert EPUB Files
           run: |
             docker run --rm -v $(pwd):/project \
               kensai-sphinx:latest \
               sh -c "
                 for epub in /project/epubs/*.epub; do
                   base=\$(basename \$epub .epub)
                   epub2sphinx \$epub --output /project/docs/books/\$base
                 done
               "
         
         - name: Build Documentation
           run: |
             docker run --rm -v $(pwd):/project \
               kensai-sphinx:latest \
               sphinx-build -b html /project/docs /project/docs/_build/html
         
         - name: Deploy
           uses: peaceiris/actions-gh-pages@v3
           with:
             github_token: ${{ secrets.GITHUB_TOKEN }}
             publish_dir: ./docs/_build/html

Best Practices
--------------

1. **Verify EPUB Quality**
   
   Check EPUB is valid before conversion:
   
   .. code-block:: bash
   
      epubcheck book.epub

2. **Review Output**
   
   Always review converted files for:
   
   - Formatting issues
   - Broken links
   - Missing images
   - Code blocks

3. **Post-Process**
   
   Clean up converted content:
   
   - Fix heading levels
   - Adjust code blocks
   - Update image paths
   - Fix internal links

4. **Preserve Metadata**
   
   Include book metadata in documentation

5. **Organize Structure**
   
   Create logical directory structure

6. **Version Control**
   
   Track both EPUB and converted RST

Common Patterns
---------------

Conversion Workflow
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # 1. Convert EPUB
   epub2sphinx book.epub --output docs/book
   
   # 2. Post-process
   python scripts/clean_rst.py docs/book
   
   # 3. Build docs
   sphinx-build -b html docs docs/_build/html
   
   # 4. Review
   open docs/_build/html/index.html

Troubleshooting
---------------

Conversion Fails
~~~~~~~~~~~~~~~~

**Solution:**

Check EPUB validity:

.. code-block:: bash

   epubcheck book.epub

Missing Images
~~~~~~~~~~~~~~

**Solution:**

Enable image extraction:

.. code-block:: bash

   epub2sphinx book.epub --extract-images --images-dir _static/images

Formatting Issues
~~~~~~~~~~~~~~~~~

**Solution:**

Enable HTML cleaning:

.. code-block:: bash

   epub2sphinx book.epub --clean-html

Broken Code Blocks
~~~~~~~~~~~~~~~~~~

**Solution:**

Specify code language:

.. code-block:: bash

   epub2sphinx book.epub --code-language python

Encoding Errors
~~~~~~~~~~~~~~~

**Solution:**

Specify encoding:

.. code-block:: bash

   epub2sphinx book.epub --encoding utf-8

Next Steps
----------

1. Convert your EPUB books to Sphinx
2. Review and clean converted content
3. Organize into documentation structure
4. Build and deploy documentation
5. Maintain both formats

Additional Resources
--------------------

- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `EPUB Specification <http://idpf.org/epub>`_
- `EPUBCheck <https://github.com/w3c/epubcheck>`_
- `Pandoc <https://pandoc.org/>`_ - Alternative converter
