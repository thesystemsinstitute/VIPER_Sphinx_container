Sphinx Gherkindoc Tutorial
==========================

.. note::

   **Package Resources:**

   - `PyPI Package <https://pypi.org/project/sphinx-gherkindoc/>`_
   - `API Documentation <../../pdoc/sphinx_gherkindoc/index.html>`_
   - `Manual <https://jolly-good-toolbelt.github.io/sphinx_gherkindoc/>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial covers sphinx-gherkindoc, a tool that converts Gherkin feature files into Sphinx-ready reStructuredText.

What is Sphinx Gherkindoc?
--------------------------
Sphinx Gherkindoc scans a directory of ``.feature`` files and generates rST files you can include in your Sphinx build.

Installation
------------

Install via pip:

.. code-block:: bash

   pip install sphinx-gherkindoc

Configuration
-------------

Choose a source directory for your features and an output directory for generated rST.

Basic Usage
-----------

Generate rST files from Gherkin features:

.. code-block:: bash

   sphinx-gherkindoc features docs/_gherkin

Command Line Options
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Basic usage
   sphinx-gherkindoc <feature-source-dir> <rst-output-dir>

   # Generate with step glossary
   sphinx-gherkindoc -G step_glossary features docs/_gherkin

   # Exclude specific directories
   sphinx-gherkindoc --exclude "**/draft/**" features docs/_gherkin

   # Integrate steps with source code
   sphinx-gherkindoc --integrate-with-source-code features docs/_gherkin

Advanced Features
-----------------

- Generate a step glossary with ``-G``.
- Exclude directories with ``--exclude`` patterns.
- Integrate with Python step definitions.
- Custom templates for RST output.
- Toctree generation for feature files.

Configuration Options
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Full options example
   sphinx-gherkindoc \
       --root-doc features \           # Root document name
       --doc-suffix .rst \             # Output file suffix
       -G step_glossary \              # Generate step glossary
       --step-glossary-name glossary \ # Glossary document name
       --integrate-with-source-code \  # Link to Python steps
       --steps-dir steps \             # Steps directory
       --exclude "**/wip/**" \         # Exclude patterns
       --exclude "**/deprecated/**" \
       features \                      # Source directory
       docs/_gherkin                   # Output directory

Examples
--------

Complete Project Setup
~~~~~~~~~~~~~~~~~~~~~~

1. Create your feature files:

.. code-block:: text

   features/
   ├── authentication/
   │   ├── login.feature
   │   ├── logout.feature
   │   └── registration.feature
   ├── shopping/
   │   ├── cart.feature
   │   ├── checkout.feature
   │   └── payment.feature
   └── steps/
       ├── auth_steps.py
       ├── cart_steps.py
       └── common_steps.py

2. Example feature file (``features/authentication/login.feature``):

.. code-block:: gherkin

   @auth @smoke
   Feature: User Login

     Background:
       Given the application is running

     Scenario: Successful login
       Given I am on the login page
       When I enter valid credentials
       Then I should see the dashboard

     Scenario: Failed login attempt
       Given I am on the login page
       When I enter invalid credentials
       Then I should see an error message

3. Generate documentation:

.. code-block:: bash

   # Generate RST with step glossary
   sphinx-gherkindoc -G step_glossary features docs/_gherkin

   # This creates:
   # docs/_gherkin/
   # ├── features.rst
   # ├── authentication/
   # │   ├── login.rst
   # │   ├── logout.rst
   # │   └── registration.rst
   # ├── shopping/
   # │   ├── cart.rst
   # │   ├── checkout.rst
   # │   └── payment.rst
   # └── step_glossary.rst

4. Include in your Sphinx toctree (``docs/index.rst``):

.. code-block:: restructuredtext

   BDD Documentation
   =================

   .. toctree::
      :maxdepth: 2
      :caption: Features

      _gherkin/features

   .. toctree::
      :maxdepth: 1
      :caption: Reference

      _gherkin/step_glossary

Generated Output Example
~~~~~~~~~~~~~~~~~~~~~~~~

The generated ``login.rst`` will look like:

.. code-block:: restructuredtext

   User Login
   ==========

   .. tags:: auth, smoke

   **Background:**

   - Given the application is running

   Successful login
   ----------------

   1. Given I am on the login page
   2. When I enter valid credentials
   3. Then I should see the dashboard

   Failed login attempt
   --------------------

   1. Given I am on the login page
   2. When I enter invalid credentials
   3. Then I should see an error message

Step Glossary Generation
~~~~~~~~~~~~~~~~~~~~~~~~

The ``step_glossary.rst`` provides a comprehensive list of all steps:

.. code-block:: restructuredtext

   Step Glossary
   =============

   Given Steps
   -----------

   I am on the login page
      Used in:

      - authentication/login: Successful login
      - authentication/login: Failed login attempt

   the application is running
      Used in:

      - authentication/login: (Background)
      - shopping/cart: (Background)

   When Steps
   ----------

   I enter valid credentials
      Used in:

      - authentication/login: Successful login

   I enter invalid credentials
      Used in:

      - authentication/login: Failed login attempt

Integration with Sphinx Build
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add to your ``Makefile`` or build script:

.. code-block:: makefile

   # Makefile
   .PHONY: gherkin html

   FEATURES_SRC = features
   GHERKIN_OUT = docs/_gherkin

   gherkin:
   	sphinx-gherkindoc -G step_glossary $(FEATURES_SRC) $(GHERKIN_OUT)

   html: gherkin
   	sphinx-build -b html docs docs/_build/html

   clean:
   	rm -rf docs/_build docs/_gherkin

Or using a Python script (``docs/conf.py``):

.. code-block:: python

   import subprocess
   from pathlib import Path

   # Auto-generate Gherkin docs before build
   def setup(app):
       features_dir = Path(__file__).parent.parent / "features"
       output_dir = Path(__file__).parent / "_gherkin"

       if features_dir.exists():
           subprocess.run([
               "sphinx-gherkindoc",
               "-G", "step_glossary",
               str(features_dir),
               str(output_dir)
           ], check=True)

   # Or use pre-build hook
   def builder_inited(app):
       # Generate gherkin docs on every build
       pass

CI/CD Integration
~~~~~~~~~~~~~~~~~

GitHub Actions example:

.. code-block:: yaml

   # .github/workflows/docs.yml
   name: Build Documentation

   on: [push, pull_request]

   jobs:
     docs:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v4

         - name: Set up Python
           uses: actions/setup-python@v5
           with:
             python-version: '3.11'

         - name: Install dependencies
           run: |
             pip install sphinx sphinx-gherkindoc

         - name: Generate Gherkin documentation
           run: |
             sphinx-gherkindoc -G step_glossary features docs/_gherkin

         - name: Build Sphinx documentation
           run: |
             sphinx-build -b html docs docs/_build/html

         - name: Upload artifacts
           uses: actions/upload-artifact@v4
           with:
             name: documentation
             path: docs/_build/html

Additional Resources
--------------------

- `Manual <https://jolly-good-toolbelt.github.io/sphinx_gherkindoc/>`_
- `PyPI <https://pypi.org/project/sphinx-gherkindoc/>`_
- `API Documentation <../../pdoc/sphinx_gherkindoc/index.html>`_
