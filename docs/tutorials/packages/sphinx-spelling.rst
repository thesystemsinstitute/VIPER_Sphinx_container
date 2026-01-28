Sphinx Spelling Tutorial
========================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinxcontrib-spelling/>`_
   - :doc:`See Working Example <../../examples/sphinx-spelling-example>`
   - `Official Documentation <https://sphinxcontrib-spelling.readthedocs.io/>`_

This tutorial demonstrates how to use sphinx-spelling in your Sphinx documentation.

What is Sphinx Spelling?
-------------------------

sphinx-spelling is a Sphinx extension that provides:

- Spell checker for documentation
- Easy integration with Sphinx
- Comprehensive configuration options
- Professional documentation output

Installation
------------

sphinx-spelling is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinxcontrib.spelling; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``docs/conf.py``:

.. code-block:: python

   extensions = [
       'sphinxcontrib.spelling',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinxcontrib.spelling']
   
   # Configuration options
   spelling_lang = 'en_US'
   spelling_word_list_filename = 'spelling_wordlist.txt'
   spelling_show_suggestions = True
   spelling_exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

Basic Usage
-----------

Getting Started
~~~~~~~~~~~~~~~

Build documentation with spelling check:

.. code-block:: bash

   make spelling

Custom Word List
~~~~~~~~~~~~~~~~

Create ``spelling_wordlist.txt`` in your docs directory:

.. code-block:: text

   API
   JSON
   YAML
   reStructuredText
   docstring
   docstrings

Common Use Cases
----------------

CI/CD Integration
~~~~~~~~~~~~~~~~~

Add spelling check to CI pipeline:

.. code-block:: yaml

   # .github/workflows/docs.yml
   - name: Check spelling
     run: |
       cd docs
       make spelling

Ignore Technical Terms
~~~~~~~~~~~~~~~~~~~~~~

Add technical terms to word list:

.. code-block:: text

   # spelling_wordlist.txt
   SQLAlchemy
   PostgreSQL
   Kubernetes
   GraphQL
   asyncio

Advanced Features
-----------------

Multiple Languages
~~~~~~~~~~~~~~~~~~

Support multiple languages:

.. code-block:: python

   # In conf.py
   spelling_lang = 'en_US'
   # Or use en_GB, de_DE, etc.

Custom Filters
~~~~~~~~~~~~~~

Filter specific content:

.. code-block:: python

   spelling_filters = [
       'enchant.tokenize.EmailFilter',
       'enchant.tokenize.URLFilter',
   ]

Best Practices
--------------

Tips and Guidelines
~~~~~~~~~~~~~~~~~~~

- Maintain a project word list
- Run spelling checks regularly
- Add domain-specific terms to word list
- Review spelling suggestions carefully
- Integrate with CI/CD pipeline

Troubleshooting
---------------

Common Issues
~~~~~~~~~~~~~

**Issue**: PyEnchant not found

**Solution**: Install PyEnchant: ``pip install pyenchant``

**Issue**: Too many false positives

**Solution**: Add technical terms to spelling_wordlist.txt

Additional Resources
--------------------

- :doc:`Working Example <../../examples/sphinx-spelling-example>`
- `PyPI Package <https://pypi.org/project/sphinxcontrib-spelling/>`_
- `Official Documentation <https://sphinxcontrib-spelling.readthedocs.io/>`_
