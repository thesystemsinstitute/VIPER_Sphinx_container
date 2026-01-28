Sphinxcontrib Bibtex Example
============================

.. note::

   **Package**: sphinxcontrib-bibtex  
   **Purpose**: BibTeX bibliography support  
   **Tutorial**: See :doc:`../tutorials/packages/sphinxcontrib-bibtex` for complete tutorial

This page demonstrates **sphinxcontrib-bibtex** - BibTeX bibliography support.

.. contents:: Contents
   :local:
   :depth: 3

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

- :doc:`Complete Tutorial <../tutorials/packages/sphinxcontrib-bibtex>`
- `PyPI Package <https://pypi.org/project/sphinxcontrib-bibtex/>`_
- `Official Documentation <https://sphinxcontrib-bibtex.readthedocs.io/>`_
- :ref:`Package API Documentation <pdoc-sphinxcontrib-bibtex>`

Next Steps
----------

- Explore the :doc:`tutorial <../tutorials/packages/sphinxcontrib-bibtex>`
- Check the official documentation
- Try the examples in your own projects
- Customize for your specific needs
