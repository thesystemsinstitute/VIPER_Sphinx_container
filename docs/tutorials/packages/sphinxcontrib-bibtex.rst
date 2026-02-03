Sphinxcontrib Bibtex Tutorial
=============================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinxcontrib-bibtex/>`_
   - `API Documentation <../../pdoc/sphinxcontrib_bibtex/index.html>`_
   - `Manual <https://sphinxcontrib-bibtex.readthedocs.io/>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinxcontrib-bibtex in your Sphinx documentation.

What is Sphinxcontrib Bibtex?
------------------------------
sphinxcontrib-bibtex is a Sphinx extension that provides:

- BibTeX bibliography support
- Easy integration with Sphinx
- Comprehensive configuration options
- Professional documentation output

sphinxcontrib-bibtex provides:

- BibTeX bibliography support
- Integration with Sphinx documentation
- Flexible configuration options
- Professional output formatting

Key Features
~~~~~~~~~~~~

- **BibTeX Integration**: Use standard BibTeX files
- **Citation Styles**: Multiple citation and reference styles
- **Filtering**: Filter bibliography entries
- **Cross-references**: Link citations to bibliography


Installation
------------

sphinxcontrib-bibtex is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm viper-sphinx:latest python -c "import sphinxcontrib.bibtex; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``docs/conf.py``:

.. code-block:: python

   extensions = [
       'sphinxcontrib.bibtex',
       # ... other extensions
   ]
   
   bibtex_bibfiles = ['references.bib']

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinxcontrib.bibtex']
   
   # Configuration options
   bibtex_bibfiles = ['references.bib', 'additional.bib']
   bibtex_default_style = 'plain'
   bibtex_reference_style = 'author_year'
   bibtex_footbibliography_header = ''


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinxcontrib.bibtex',
       # ... other extensions
   ]
   
   bibtex_bibfiles = ['references.bib']

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

Complete configuration with all features:

.. code-block:: python

   extensions = ['sphinxcontrib.bibtex']
   
   # Package-specific configuration
   bibtex_bibfiles = ['references.bib', 'additional.bib']
   bibtex_default_style = 'plain'
   bibtex_reference_style = 'author_year'
   
   # Bibliography options
   bibtex_footbibliography_header = ''
   bibtex_footbibliography_footer = ''
   
   # Encoding
   bibtex_encoding = 'utf-8'

Basic Usage
-----------

Getting Started
~~~~~~~~~~~~~~~

Create a BibTeX file ``references.bib``:

.. code-block:: bibtex

   @article{einstein1905,
       author = {Einstein, Albert},
       title = {On the Electrodynamics of Moving Bodies},
       journal = {Annalen der Physik},
       year = {1905},
       volume = {17},
       pages = {891--921}
   }

Cite References
~~~~~~~~~~~~~~~

Cite in RST files:

.. code-block:: rst

   According to :cite:`einstein1905`, the theory of relativity...
   
   .. bibliography::

Common Use Cases
----------------

Multiple Citations
~~~~~~~~~~~~~~~~~~

Cite multiple references:

.. code-block:: rst

   Research shows :cite:`author2020,author2021,author2022` that...

Custom Bibliography
~~~~~~~~~~~~~~~~~~~

Add bibliography with custom style:

.. code-block:: rst

   .. bibliography::
      :style: alpha
      :filter: author % "Einstein"

Advanced Features
-----------------

Reference Styles
~~~~~~~~~~~~~~~~

Configure citation style:

.. code-block:: python

   # In conf.py
   bibtex_reference_style = 'label'  # or 'author_year'

Multiple BibTeX Files
~~~~~~~~~~~~~~~~~~~~~

Use multiple bibliography files:

.. code-block:: python

   bibtex_bibfiles = [
       'papers.bib',
       'books.bib',
       'websites.bib',
   ]

Best Practices
--------------

Tips and Guidelines
~~~~~~~~~~~~~~~~~~~

- Organize references by topic
- Use consistent BibTeX keys
- Include all required fields
- Keep bibliography files updated
- Test citation rendering

Troubleshooting
---------------

Common Issues
~~~~~~~~~~~~~

**Issue**: Citation not found

**Solution**: Check BibTeX key spelling and ensure file is listed in bibtex_bibfiles.

**Issue**: Bibliography not displaying

**Solution**: Ensure ``.. bibliography::`` directive is present.


Practical Examples
------------------

Overview
--------


Key Features
~~~~~~~~~~~~

- **BibTeX Integration**: Use standard BibTeX files
- **Citation Styles**: Multiple citation and reference styles
- **Filtering**: Filter bibliography entries
- **Cross-references**: Link citations to bibliography

Installation
------------

Using pip
~~~~~~~~~

Install the extension:

.. code-block:: bash

   pip install sphinxcontrib-bibtex

Or add to your ``requirements.txt``:

.. code-block:: text

   sphinxcontrib-bibtex
   sphinx>=5.0.0

Configuration
-------------

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinxcontrib.bibtex',
       # ... other extensions
   ]
   
   bibtex_bibfiles = ['references.bib']

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

Complete configuration with all features:

.. code-block:: python

   extensions = ['sphinxcontrib.bibtex']
   
   # Package-specific configuration
   bibtex_bibfiles = ['references.bib', 'additional.bib']
   bibtex_default_style = 'plain'
   bibtex_reference_style = 'author_year'
   
   # Bibliography options
   bibtex_footbibliography_header = ''
   bibtex_footbibliography_footer = ''
   
   # Encoding
   bibtex_encoding = 'utf-8'

Basic Usage
-----------

Example 1: Create BibTeX File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create ``references.bib``:

.. code-block:: bibtex

   @article{einstein1905,
       author = {Einstein, Albert},
       title = {On the Electrodynamics of Moving Bodies},
       journal = {Annalen der Physik},
       year = {1905},
       volume = {17},
       pages = {891--921},
       doi = {10.1002/andp.19053221004}
   }
   
   @book{knuth1984,
       author = {Knuth, Donald E.},
       title = {The TeXbook},
       publisher = {Addison-Wesley},
       year = {1984},
       isbn = {0-201-13447-0}
   }
   
   @inproceedings{dijkstra1968,
       author = {Dijkstra, Edsger W.},
       title = {Go To Statement Considered Harmful},
       booktitle = {Communications of the ACM},
       year = {1968},
       volume = {11},
       number = {3},
       pages = {147--148}
   }

Example 2: Cite References
~~~~~~~~~~~~~~~~~~~~~~~~~~

Use citations in RST:

.. code-block:: rst

   Introduction
   ============
   
   The theory of relativity :cite:`einstein1905` revolutionized physics.
   For typesetting mathematics, see :cite:`knuth1984`.
   
   Bibliography
   ============
   
   .. bibliography::

Real-World Examples
-------------------

Example: Academic Paper
~~~~~~~~~~~~~~~~~~~~~~~

Complete academic paper with citations:

.. code-block:: rst

   Research Paper
   ==============
   
   Abstract
   --------
   
   This paper builds on previous work :cite:`einstein1905,knuth1984`.
   
   Introduction
   ------------
   
   As demonstrated by :cite:`dijkstra1968`, structured programming is essential.
   
   Related Work
   ------------
   
   Several authors :cite:`einstein1905,knuth1984,dijkstra1968` have 
   contributed to this field.
   
   References
   ----------
   
   .. bibliography::
      :style: plain
      :all:

Example: Filtered Bibliography
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Filter bibliography entries:

.. code-block:: rst

   Physics References
   ==================
   
   .. bibliography::
      :filter: author % "Einstein"
      :style: alpha
   
   Computer Science References
   ===========================
   
   .. bibliography::
      :filter: author % "Knuth" or author % "Dijkstra"
      :style: plain

Example: Custom Styles
~~~~~~~~~~~~~~~~~~~~~~

Different citation styles:

.. code-block:: rst

   Author-Year Style
   =================
   
   According to Einstein (1905) :cite:`einstein1905`, ...
   
   .. bibliography::
      :style: author_year
   
   Numbered Style
   ==============
   
   The theory [1] :cite:`einstein1905` states that...
   
   .. bibliography::
      :style: plain

Example: Multiple BibTeX Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Organize references by topic:

.. code-block:: python

   # In conf.py
   bibtex_bibfiles = [
       'physics.bib',
       'computer-science.bib',
       'mathematics.bib',
   ]

Then in RST:

.. code-block:: rst

   All References
   ==============
   
   .. bibliography::
      :all:

Best Practices
--------------

Recommendations
~~~~~~~~~~~~~~~

- Organize BibTeX files by topic
- Use consistent citation keys
- Include DOIs when available
- Validate BibTeX syntax
- Keep bibliography updated

Common Patterns
~~~~~~~~~~~~~~~

Standard patterns for using sphinxcontrib-bibtex:

1. **Single Bibliography**: One bibliography at end of document
2. **Chapter Bibliographies**: Separate bibliography per chapter
3. **Filtered Lists**: Topic-specific reference lists

Integration Tips
----------------

Working with Other Extensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

sphinxcontrib-bibtex integrates well with:

- Standard Sphinx extensions
- Academic writing workflows
- Citation management tools

Additional Resources
--------------------

- `PyPI Package <https://pypi.org/project/sphinxcontrib-bibtex/>`_
- `Official Documentation <https://sphinxcontrib-bibtex.readthedocs.io/>`_
- :doc:`Complete Tutorial <../tutorials/packages/sphinxcontrib-bibtex>`
- :ref:`Package API Documentation <pdoc-sphinxcontrib-bibtex>`
Next Steps
----------
- Explore the :doc:`tutorial <../tutorials/packages/sphinxcontrib-bibtex>`
- Check the official documentation
- Try the examples in your own projects
- Customize for your specific needs

