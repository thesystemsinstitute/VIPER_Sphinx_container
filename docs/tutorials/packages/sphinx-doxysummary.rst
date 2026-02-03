Sphinx Doxysummary Tutorial
===========================

.. note::

   **Package Resources:**

   - `PyPI Package <https://pypi.org/project/sphinx-doxysummary/>`_
   - `API Documentation <../../pdoc/sphinx_doxysummary/index.html>`_
   - `Manual <https://doxysummary.readthedocs.io/en/latest/>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial explains sphinx-doxysummary, a Sphinx extension that builds autosummary tables from Doxygen XML.

What is Sphinx Doxysummary?
---------------------------
Sphinx Doxysummary integrates Doxygen XML with Sphinx autosummary-style tables.

Installation
------------

Install via pip:

.. code-block:: bash

   pip install sphinx-doxysummary

Configuration
-------------

Enable the extension and set XML paths in ``conf.py``:

.. code-block:: python

   extensions = [
       "sphinx_doxysummary",
   ]

   doxygen_xml = ["./xml"]

Basic Usage
-----------

Add a ``doxysummary`` directive:

.. code-block:: restructuredtext

   .. doxysummary::
      :toctree: generated
      :template: cppclass.rst

      MyNamespace::MyClass

This generates autosummary-style tables from your Doxygen XML output.

Advanced Features
-----------------

- Use ``:scope:`` to set a namespace or class scope.
- Alias entries with quoted display names.
- Generate stub files for detailed documentation.
- Custom templates for different entity types.
- Support for functions, classes, and namespaces.

Configuration Options
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py

   extensions = [
       "breathe",           # For Doxygen integration
       "sphinx_doxysummary",
   ]

   # Doxygen XML paths
   doxygen_xml = ["./xml"]  # Path to Doxygen XML output

   # Doxysummary configuration
   doxysummary_template_path = ["_templates/doxysummary"]
   doxysummary_generate = True  # Auto-generate stub files

Examples
--------

Project Setup
~~~~~~~~~~~~~

1. **Generate Doxygen XML:**

   Create a ``Doxyfile``:

   .. code-block:: text

      # Doxyfile
      PROJECT_NAME     = "MyProject"
      OUTPUT_DIRECTORY = docs/doxygen
      INPUT            = src/
      RECURSIVE        = YES
      GENERATE_XML     = YES
      GENERATE_HTML    = NO
      GENERATE_LATEX   = NO
      XML_OUTPUT       = xml

   Run Doxygen:

   .. code-block:: bash

      doxygen Doxyfile

2. **Configure Sphinx:**

   .. code-block:: python

      # docs/conf.py

      extensions = [
          "breathe",
          "sphinx_doxysummary",
      ]

      # Breathe configuration
      breathe_projects = {
          "MyProject": "doxygen/xml"
      }
      breathe_default_project = "MyProject"

      # Doxysummary configuration
      doxygen_xml = ["doxygen/xml"]
      doxysummary_generate = True

Basic Class Table
~~~~~~~~~~~~~~~~~

Create a summary table for C++ classes:

.. code-block:: restructuredtext

   Core Classes
   ============

   .. doxysummary::
      :toctree: api/generated

      MyProject::Widget
      MyProject::Button
      MyProject::Label
      MyProject::Container

This generates a table like:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Class
     - Description
   * - ``Widget``
     - Base class for all UI elements
   * - ``Button``
     - Clickable button widget
   * - ``Label``
     - Text display widget
   * - ``Container``
     - Widget container for layout

Namespace Scoping
~~~~~~~~~~~~~~~~~

Use ``:scope:`` to avoid repeating namespace prefixes:

.. code-block:: restructuredtext

   Network Module
   ==============

   .. doxysummary::
      :toctree: api/generated
      :scope: MyProject::Network

      Socket
      Connection
      Server
      Client
      Protocol

This is equivalent to:

.. code-block:: restructuredtext

   .. doxysummary::
      :toctree: api/generated

      MyProject::Network::Socket
      MyProject::Network::Connection
      MyProject::Network::Server
      MyProject::Network::Client
      MyProject::Network::Protocol

Function Summary Tables
~~~~~~~~~~~~~~~~~~~~~~~

Document functions with summaries:

.. code-block:: restructuredtext

   Utility Functions
   =================

   .. doxysummary::
      :toctree: api/generated
      :scope: MyProject::Utils

      split_string
      trim_whitespace
      to_uppercase
      to_lowercase
      format_bytes

Custom Display Names
~~~~~~~~~~~~~~~~~~~~

Alias entries with custom display names:

.. code-block:: restructuredtext

   Key Classes
   ===========

   .. doxysummary::
      :toctree: api/generated

      "Main Application" MyProject::Application
      "Configuration Manager" MyProject::Config::Manager
      "Event System" MyProject::Events::Dispatcher

This renders as:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Class
     - Description
   * - Main Application
     - Entry point for the application
   * - Configuration Manager
     - Handles configuration loading and saving
   * - Event System
     - Dispatches events to registered handlers

Custom Templates
~~~~~~~~~~~~~~~~

Create custom templates for different entity types.

**Template structure:**

.. code-block:: text

   docs/
   └── _templates/
       └── doxysummary/
           ├── class.rst
           ├── function.rst
           └── namespace.rst

**Class template** (``_templates/doxysummary/class.rst``):

.. code-block:: restructuredtext

   {{ name }}
   {{ '=' * name|length }}

   .. doxygenclass:: {{ fullname }}
      :project: {{ project }}
      :members:
      :protected-members:
      :undoc-members:

   See Also
   --------

   {% for related in related_classes %}
   - :cpp:class:`{{ related }}`
   {% endfor %}

**Function template** (``_templates/doxysummary/function.rst``):

.. code-block:: restructuredtext

   {{ name }}
   {{ '=' * name|length }}

   .. doxygenfunction:: {{ fullname }}
      :project: {{ project }}

   Example
   -------

   .. code-block:: cpp

      // Example usage of {{ name }}
      auto result = {{ name }}(/* parameters */);

Hierarchical Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~

Organize documentation by namespace hierarchy:

.. code-block:: restructuredtext

   API Reference
   =============

   .. toctree::
      :maxdepth: 2

      api/core
      api/network
      api/graphics

**api/core.rst:**

.. code-block:: restructuredtext

   Core Module
   ===========

   Classes
   -------

   .. doxysummary::
      :toctree: generated
      :scope: MyProject::Core

      Application
      Context
      Logger
      Configuration

   Functions
   ---------

   .. doxysummary::
      :toctree: generated
      :scope: MyProject::Core

      initialize
      shutdown
      get_version

**api/network.rst:**

.. code-block:: restructuredtext

   Network Module
   ==============

   Connection Classes
   ------------------

   .. doxysummary::
      :toctree: generated
      :scope: MyProject::Network

      Socket
      TCPSocket
      UDPSocket
      SSLSocket

   Server Classes
   --------------

   .. doxysummary::
      :toctree: generated
      :scope: MyProject::Network

      Server
      HTTPServer
      WebSocketServer

Complete Build Pipeline
~~~~~~~~~~~~~~~~~~~~~~~

Makefile for building Doxygen + Sphinx:

.. code-block:: makefile

   # Makefile

   DOXYGEN     = doxygen
   SPHINXBUILD = sphinx-build
   SOURCEDIR   = docs
   BUILDDIR    = docs/_build

   .PHONY: doxygen html clean

   doxygen:
   	$(DOXYGEN) Doxyfile

   html: doxygen
   	$(SPHINXBUILD) -b html "$(SOURCEDIR)" "$(BUILDDIR)/html"

   clean:
   	rm -rf "$(BUILDDIR)"
   	rm -rf docs/doxygen

CI/CD Integration
~~~~~~~~~~~~~~~~~

GitHub Actions workflow:

.. code-block:: yaml

   # .github/workflows/docs.yml
   name: Build Documentation

   on: [push, pull_request]

   jobs:
     docs:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v4

         - name: Install Doxygen
           run: sudo apt-get install -y doxygen

         - name: Set up Python
           uses: actions/setup-python@v5
           with:
             python-version: '3.11'

         - name: Install dependencies
           run: pip install sphinx breathe sphinx-doxysummary

         - name: Generate Doxygen XML
           run: doxygen Doxyfile

         - name: Build documentation
           run: sphinx-build -b html docs docs/_build/html

Additional Resources
--------------------

- `Manual <https://doxysummary.readthedocs.io/en/latest/>`_
- `PyPI <https://pypi.org/project/sphinx-doxysummary/>`_
- `API Documentation <../../pdoc/sphinx_doxysummary/index.html>`_
