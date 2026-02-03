Hatch Sphinx Tutorial
======================

.. note::

   **Package Resources:**

   - `PyPI Package <https://pypi.org/project/hatch-sphinx/>`_
   - `API Documentation <../../pdoc/hatch_sphinx/index.html>`_
   - `Manual <https://github.com/llimeht/hatch-sphinx#readme>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial covers hatch-sphinx, a Hatch build hook for running Sphinx during package builds.

What is Hatch Sphinx?
---------------------
Hatch Sphinx is a Hatchling plugin that runs Sphinx (and optional tooling) as part of your build pipeline.

Installation
------------

Install via pip:

.. code-block:: bash

   pip install hatch-sphinx

Configuration
-------------

Add the hook to your ``pyproject.toml``:

.. code-block:: toml

   [build-system]
   requires = ["hatchling", "hatch-sphinx"]
   build-backend = "hatchling.build"

   [[tool.hatch.build.targets.wheel.hooks.sphinx.tools]]
   tool = "build"
   doc_dir = "docs"
   out_dir = "_build"
   format = "html"

Basic Usage
-----------

Build your wheel and let Hatch run Sphinx automatically:

.. code-block:: bash

   hatch build

Advanced Features
-----------------

- Chain multiple tools (e.g., ``apidoc`` then ``build``).
- Use custom commands for pre/post processing.

Examples
--------

Run ``sphinx-apidoc`` and then build HTML:

.. code-block:: toml

   [[tool.hatch.build.targets.wheel.hooks.sphinx.tools]]
   tool = "apidoc"
   source = "src"
   out_dir = "docs/api"

   [[tool.hatch.build.targets.wheel.hooks.sphinx.tools]]
   tool = "build"
   doc_dir = "docs"
   out_dir = "_build"
   format = "html"

Additional Resources
--------------------

- `Manual <https://github.com/llimeht/hatch-sphinx#readme>`_
- `PyPI <https://pypi.org/project/hatch-sphinx/>`_
- `API Documentation <../../pdoc/hatch_sphinx/index.html>`_
