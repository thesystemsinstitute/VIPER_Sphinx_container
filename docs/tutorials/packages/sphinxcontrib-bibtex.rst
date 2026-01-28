Sphinxcontrib Bibtex Tutorial
=============================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinxcontrib-bibtex/>`_
   - :doc:`See Working Example <../../examples/sphinxcontrib-bibtex-example>`
   - `Official Documentation <https://sphinxcontrib-bibtex.readthedocs.io/>`_

This tutorial demonstrates how to use sphinxcontrib-bibtex in your Sphinx documentation.

What is Sphinxcontrib Bibtex?
------------------------------

sphinxcontrib-bibtex is a Sphinx extension that provides:

- BibTeX bibliography support
- Easy integration with Sphinx
- Comprehensive configuration options
- Professional documentation output

Installation
------------

sphinxcontrib-bibtex is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinxcontrib.bibtex; print('Installed')"

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

Additional Resources
--------------------

- :doc:`Working Example <../../examples/sphinxcontrib-bibtex-example>`
- `PyPI Package <https://pypi.org/project/sphinxcontrib-bibtex/>`_
- `Official Documentation <https://sphinxcontrib-bibtex.readthedocs.io/>`_
