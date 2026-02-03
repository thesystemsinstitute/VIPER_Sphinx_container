Sphinx Gherkin Tutorial
=======================

.. note::

   **Package Resources:**

   - `PyPI Package <https://pypi.org/project/sphinx-gherkin/>`_
   - `API Documentation <../../pdoc/sphinx_gherkin/index.html>`_
   - `Manual <https://cblegare.gitlab.io/sphinx-gherkin>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial introduces sphinx-gherkin, a Sphinx extension for documenting Gherkin features.

What is Sphinx Gherkin?
-----------------------
Sphinx Gherkin provides a domain for Gherkin features so you can reference scenarios and steps in your docs.

Installation
------------

Install via pip:

.. code-block:: bash

   pip install sphinx-gherkin

Configuration
-------------

Enable the extension in ``conf.py``:

.. code-block:: python

   extensions = [
       "sphinx_gherkin",
   ]

Basic Usage
-----------

Include feature files and reference them in your documentation.

Advanced Features
-----------------

- Cross-reference Gherkin items through the domain.
- Integrate with Sphinx TOCs for feature navigation.

Examples
--------

Include a feature file:

.. code-block:: restructuredtext

   .. include:: features/login.feature
      :code: gherkin

Additional Resources
--------------------

- `Manual <https://cblegare.gitlab.io/sphinx-gherkin>`_
- `PyPI <https://pypi.org/project/sphinx-gherkin/>`_
- `API Documentation <../../pdoc/sphinx_gherkin/index.html>`_
