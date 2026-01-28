Sphinx Spelling Tutorial
========================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinxcontrib-spelling/>`_

   - `Official Documentation <https://sphinxcontrib-spelling.readthedocs.io/>`_

This tutorial demonstrates how to use sphinx-spelling in your Sphinx documentation.

What is Sphinx Spelling?
-------------------------
sphinx-spelling is a Sphinx extension that provides:

- Spell checker for documentation
- Easy integration with Sphinx
- Comprehensive configuration options
- Professional documentation output

sphinx-spelling provides:

- Spell checker for documentation
- Integration with Sphinx documentation
- Flexible configuration options
- Professional output formatting

Key Features
~~~~~~~~~~~~

- **Spell Checking**: Comprehensive spell checking for documentation
- **Custom Dictionaries**: Support for project-specific word lists
- **Multiple Languages**: Support for various languages
- **CI/CD Integration**: Easy integration with build pipelines


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


Complete configuration with all features:

.. code-block:: python

   extensions = ['sphinxcontrib.spelling']
   
   # Package-specific configuration
   spelling_lang = 'en_US'
   spelling_word_list_filename = 'spelling_wordlist.txt'
   spelling_show_suggestions = True
   spelling_suggestion_limit = 5
   
   # Exclude patterns
   spelling_exclude_patterns = [
       '_build/**',
       'Thumbs.db',
       '.DS_Store',
   ]
   
   # Filters
   spelling_filters = [
       'enchant.tokenize.EmailFilter',
       'enchant.tokenize.URLFilter',
   ]
   
   # Ignore specific content
   spelling_ignore_pypi_package_names = True
   spelling_ignore_wiki_words = True
   spelling_ignore_acronyms = True
   spelling_ignore_python_builtins = True
   spelling_ignore_importable_modules = True

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


Practical Examples
------------------

Overview
--------


Key Features
~~~~~~~~~~~~

- **Spell Checking**: Comprehensive spell checking for documentation
- **Custom Dictionaries**: Support for project-specific word lists
- **Multiple Languages**: Support for various languages
- **CI/CD Integration**: Easy integration with build pipelines

Installation
------------

Using pip
~~~~~~~~~

Install the extension:

.. code-block:: bash

   pip install sphinxcontrib-spelling pyenchant

Or add to your ``requirements.txt``:

.. code-block:: text

   sphinxcontrib-spelling
   pyenchant
   sphinx>=5.0.0

Configuration
-------------

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinxcontrib.spelling',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

Complete configuration with all features:

.. code-block:: python

   extensions = ['sphinxcontrib.spelling']
   
   # Package-specific configuration
   spelling_lang = 'en_US'
   spelling_word_list_filename = 'spelling_wordlist.txt'
   spelling_show_suggestions = True
   spelling_suggestion_limit = 5
   
   # Exclude patterns
   spelling_exclude_patterns = [
       '_build/**',
       'Thumbs.db',
       '.DS_Store',
   ]
   
   # Filters
   spelling_filters = [
       'enchant.tokenize.EmailFilter',
       'enchant.tokenize.URLFilter',
   ]
   
   # Ignore specific content
   spelling_ignore_pypi_package_names = True
   spelling_ignore_wiki_words = True
   spelling_ignore_acronyms = True
   spelling_ignore_python_builtins = True
   spelling_ignore_importable_modules = True

Basic Usage
-----------

Example 1: Run Spell Check
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Check spelling:

.. code-block:: bash

   # Using Sphinx build
   sphinx-build -b spelling docs/ docs/_build/spelling
   
   # Using make
   make spelling
   
   # View results
   cat docs/_build/spelling/output.txt

Example 2: Custom Word List
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create ``spelling_wordlist.txt``:

.. code-block:: text

   # Technical terms
   API
   JSON
   YAML
   XML
   
   # Framework names
   Sphinx
   reStructuredText
   Markdown
   
   # Domain-specific terms
   SQLAlchemy
   PostgreSQL
   Kubernetes
   
   # Custom terms
   docstring
   docstrings
   autosummary
   autodoc

Real-World Examples
-------------------

Example: Project Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Complete project setup:

.. code-block:: python

   # docs/conf.py
   extensions = [
       'sphinxcontrib.spelling',
       'sphinx.ext.autodoc',
       'sphinx.ext.napoleon',
   ]
   
   # Spelling configuration
   spelling_lang = 'en_US'
   spelling_word_list_filename = ['spelling_wordlist.txt']
   spelling_show_suggestions = True
   
   # Ignore patterns
   spelling_exclude_patterns = [
       '_build/**',
       'api/**',  # Generated API docs
   ]

Example: CI/CD Integration
~~~~~~~~~~~~~~~~~~~~~~~~~~

GitHub Actions workflow:

.. code-block:: yaml

   name: Documentation Spelling
   
   on: [push, pull_request]
   
   jobs:
     spelling:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Set up Python
           uses: actions/setup-python@v4
           with:
             python-version: '3.11'
         
         - name: Install dependencies
           run: |
             sudo apt-get update
             sudo apt-get install -y enchant-2
             pip install sphinxcontrib-spelling pyenchant sphinx
         
         - name: Check spelling
           run: |
             cd docs
             make spelling
             
         - name: Upload spelling errors
           if: failure()
           uses: actions/upload-artifact@v3
           with:
             name: spelling-errors
             path: docs/_build/spelling/output.txt

Example: Makefile Target
~~~~~~~~~~~~~~~~~~~~~~~~

Add to ``Makefile``:

.. code-block:: makefile

   .PHONY: spelling
   spelling:
   	@echo "Checking spelling..."
   	$(SPHINXBUILD) -b spelling $(SOURCEDIR) $(BUILDDIR)/spelling
   	@if [ -s $(BUILDDIR)/spelling/output.txt ]; then \
   		echo "Spelling errors found:"; \
   		cat $(BUILDDIR)/spelling/output.txt; \
   		exit 1; \
   	else \
   		echo "No spelling errors found."; \
   	fi

Best Practices
--------------

Recommendations
~~~~~~~~~~~~~~~

- Maintain a comprehensive word list
- Run spelling checks in CI/CD
- Review suggestions before adding to word list
- Use language-specific dictionaries
- Filter technical content appropriately

Common Patterns
~~~~~~~~~~~~~~~

Standard patterns for using sphinx-spelling:

1. **Word List Management**: Keep project-specific terms in word list
2. **CI/CD Integration**: Fail builds on spelling errors
3. **Filtering**: Exclude auto-generated content

Integration Tips
----------------

Working with Other Extensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

sphinx-spelling integrates well with:

- rstcheck for syntax validation
- doc8 for style checking
- sphinx-build for comprehensive validation

Additional Resources
--------------------

- `PyPI Package <https://pypi.org/project/sphinxcontrib-spelling/>`_
- `Official Documentation <https://sphinxcontrib-spelling.readthedocs.io/>`_
- :doc:`Complete Tutorial <../tutorials/packages/sphinx-spelling>`
- :ref:`Package API Documentation <pdoc-sphinx-spelling>`
Next Steps
----------
- Explore the :doc:`tutorial <../tutorials/packages/sphinx-spelling>`
- Check the official documentation
- Try the examples in your own projects
- Customize for your specific needs

