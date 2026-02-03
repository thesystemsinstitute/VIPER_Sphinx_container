rst-pypi-ref Tutorial
======================

.. note::

   **Package Resources:**

   - `PyPI Package <https://pypi.org/project/rst-pypi-ref/>`_
   - `API Documentation <../../pdoc/rst_pypi_ref/index.html>`_
   - `Manual <https://github.com/attakei-lab/rst-pypi-ref>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial introduces rst-pypi-ref, a reStructuredText role for linking to PyPI projects.

What is rst-pypi-ref?
---------------------
rst-pypi-ref provides a ``:pypi:`` role (and Sphinx integration) for fast links to PyPI packages.

Installation
------------

Install via pip:

.. code-block:: bash

   pip install rst-pypi-ref

Configuration
-------------

Enable the extension in ``conf.py``:

.. code-block:: python

   extensions = [
       "rst_pypi_ref.sphinx",
   ]

Basic Usage
-----------

Use the role in reStructuredText:

.. code-block:: restructuredtext

   See :pypi:`sphinx-readme` for details.

This renders as a hyperlink to the PyPI project page.

Advanced Features
-----------------

- Pin versions: ``:pypi:`package==1.2.3```.
- Customize link text: ``:pypi:`PyPI <package>```.
- Support for extras: ``:pypi:`package[extra]```.
- Integration with intersphinx.
- Works in both Sphinx and standalone docutils.

Configuration Options
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py

   extensions = [
       "rst_pypi_ref.sphinx",
   ]

   # Optional: customize PyPI URL (for private registries)
   pypi_url = "https://pypi.org/project/{package}/"

   # Optional: default to specific version format
   pypi_version_format = "=={version}"

Examples
--------

Basic Package References
~~~~~~~~~~~~~~~~~~~~~~~~

Link to packages on PyPI:

.. code-block:: restructuredtext

   Install the required packages:

   - :pypi:`sphinx` - Documentation generator
   - :pypi:`sphinx-rtd-theme` - Read the Docs theme
   - :pypi:`myst-parser` - Markdown support for Sphinx

   For async support, install :pypi:`aiohttp` and :pypi:`asyncio`.

Renders as:

   Install the required packages:

   - `sphinx <https://pypi.org/project/sphinx/>`_ - Documentation generator
   - `sphinx-rtd-theme <https://pypi.org/project/sphinx-rtd-theme/>`_ - Read the Docs theme
   - `myst-parser <https://pypi.org/project/myst-parser/>`_ - Markdown support for Sphinx

Version Pinning
~~~~~~~~~~~~~~~

Reference specific versions:

.. code-block:: restructuredtext

   This documentation requires:

   - :pypi:`sphinx==7.2.6`
   - :pypi:`sphinx-rtd-theme>=2.0.0`
   - :pypi:`myst-parser~=3.0`

   **Note:** Version :pypi:`sphinx==6.0.0` introduced breaking changes.

Custom Link Text
~~~~~~~~~~~~~~~~

Use custom display text:

.. code-block:: restructuredtext

   See the :pypi:`official Sphinx package <sphinx>` for more information.

   Install :pypi:`the RTD theme <sphinx-rtd-theme>` for a professional look.

   This extension is based on :pypi:`Docutils <docutils>`.

Renders as:

   See the `official Sphinx package <https://pypi.org/project/sphinx/>`_ for more information.

Package with Extras
~~~~~~~~~~~~~~~~~~~

Reference packages with optional extras:

.. code-block:: restructuredtext

   For full functionality, install:

   - :pypi:`sphinx[docs]` - With documentation dependencies
   - :pypi:`requests[security]` - With security extras
   - :pypi:`pandas[excel,sql]` - With Excel and SQL support

Requirements Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~

Document project dependencies:

.. code-block:: restructuredtext

   Dependencies
   ============

   Core Dependencies
   -----------------

   .. list-table::
      :header-rows: 1
      :widths: 30 20 50

      * - Package
        - Version
        - Description
      * - :pypi:`sphinx`
        - ≥7.0
        - Documentation generator
      * - :pypi:`docutils`
        - ≥0.18
        - reStructuredText parser
      * - :pypi:`jinja2`
        - ≥3.0
        - Template engine

   Optional Dependencies
   ---------------------

   For PDF generation:

   - :pypi:`rst2pdf` - Direct PDF generation
   - :pypi:`rinohtype` - Pure Python PDF builder

   For Markdown support:

   - :pypi:`myst-parser` - MyST Markdown dialect
   - :pypi:`recommonmark` - CommonMark support (deprecated)

   Theme packages:

   - :pypi:`sphinx-rtd-theme` - Read the Docs theme
   - :pypi:`furo` - Modern, accessible theme
   - :pypi:`pydata-sphinx-theme` - PyData ecosystem theme

Inline Documentation
~~~~~~~~~~~~~~~~~~~~

Reference packages within documentation:

.. code-block:: restructuredtext

   Installation
   ============

   Using pip
   ---------

   Install the package directly from :pypi:`PyPI <mypackage>`:

   .. code-block:: bash

      pip install mypackage

   With optional dependencies:

   .. code-block:: bash

      pip install mypackage[dev,docs]

   Development Setup
   -----------------

   Clone the repository and install development dependencies:

   .. code-block:: bash

      git clone https://github.com/user/mypackage.git
      cd mypackage
      pip install -e ".[dev]"

   This installs:

   - :pypi:`pytest` - Testing framework
   - :pypi:`black` - Code formatter
   - :pypi:`mypy` - Static type checker
   - :pypi:`pre-commit` - Git hooks manager

Comparison Tables
~~~~~~~~~~~~~~~~~

Compare related packages:

.. code-block:: restructuredtext

   Sphinx Theme Comparison
   =======================

   .. list-table::
      :header-rows: 1
      :widths: 25 15 60

      * - Theme
        - License
        - Features
      * - :pypi:`sphinx-rtd-theme`
        - MIT
        - Classic RTD look, mobile responsive
      * - :pypi:`furo`
        - MIT
        - Modern design, excellent accessibility
      * - :pypi:`pydata-sphinx-theme`
        - BSD
        - Bootstrap-based, sidebar navigation
      * - :pypi:`sphinx-book-theme`
        - BSD
        - Jupyter Book styling
      * - :pypi:`sphinx-material`
        - MIT
        - Material Design styling

Standalone docutils Usage
~~~~~~~~~~~~~~~~~~~~~~~~~

Use without Sphinx (pure docutils):

.. code-block:: python

   # register_roles.py
   from docutils.parsers.rst import roles
   from rst_pypi_ref import pypi_role

   # Register the role
   roles.register_local_role('pypi', pypi_role)

Then in your RST file:

.. code-block:: restructuredtext

   See :pypi:`docutils` for the base parser.

Build with:

.. code-block:: bash

   rst2html --config=register_roles.py document.rst output.html

MyST Markdown Usage
~~~~~~~~~~~~~~~~~~~

The role also works in MyST Markdown files:

.. code-block:: markdown

   # Installation

   Install from {pypi}`PyPI <mypackage>`:

   ```bash
   pip install mypackage
   ```

   ## Dependencies

   - {pypi}`sphinx` - Documentation
   - {pypi}`pytest` - Testing

Additional Resources
--------------------

- `Manual <https://github.com/attakei-lab/rst-pypi-ref>`_
- `PyPI <https://pypi.org/project/rst-pypi-ref/>`_
- `API Documentation <../../pdoc/rst_pypi_ref/index.html>`_
