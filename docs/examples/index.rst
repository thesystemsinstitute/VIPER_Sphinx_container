Package-specific Examples
=========================

This section contains practical examples demonstrating various Sphinx features.

.. toctree::
   :maxdepth: 2
   
   basic-example
   api-docs-example
   jupyter-example
   graphviz-example
   sphinx-charts-example
   sphinx-confluence-example
   sphinx-lint-example
   sphinx-library-example
   sphinx2doxygen-example
   sphinx-issues-example
   sphinx-tagtoctree-example
   sphinx-vhdl-example
   sphinx-c-autodoc-example
   sphinx-theme-example
   sphinx-refdoc-example
   sphinx-gitref-example
   sphinx-autoschematics-example
   sphinx-pyreverse-example
   sphinx-uml-example
   sphinxcontrib-asyncio-example
   sphinxcontrib-googlemaps-example
   sphinx-kml-example
   sphinxnotes-fasthtml-example
   sphinx-wagtail-theme-example
   sphinx-diagrams-example
   btd-sphinx-graphviz-example
   sphinx-tojupyter-example
   sphinxcontrib-cadquery-example
   epub2sphinx-example
   sphinx-autodoc-defaultargs-example
   sphinx-autodoc-annotation-example
   sphinx-autodoc2-fern-example
   sphinx-collapsible-autodoc-example
   sphinx-autodoc-toml-example
   sphinx-automodapi-example
   pytest-doctestplus-example
   sphinx-copybutton-example
   sphinx-prompt-example
   sphinxemoji-example
   sphinx-favicon-example
   myst-parser-example
   sphinxcontrib-httpdomain-example
   sphinx-autobuild-example
   sphinx-autoapi-example
   nbsphinx-example
   nbsphinx-link-example
   sphinx-jupyter-kernel-example
   sphinx-notfound-page-example
   sphinx-version-warning-example
   sphinx-hoverxref-example
   sphinx-last-updated-by-git-example
   sphinx-git-example
   sphinxext-opengraph-example
   breathe-example
   exhale-example
   ansible-sphinx-example
   invoke-sphinx-example
   sphinx-analytics-example
   sphinx-apischema-example
   sphinx-autoindex-example
   sphinx-autofixture-example
   sphinx-autopackagesummary-example
   sphinx-advanced-example
   sphinx-changelog-example
   sphinx-rtd-theme-example
   sphinx-book-theme-example
   pydata-sphinx-theme-example
   furo-example
   piccolo-theme-example
   sphinx-material-example
   sphinx-press-theme-example
   karma-sphinx-theme-example
   sphinxawesome-theme-example
   sphinx-immaterial-example
   markdown-example
   enumerate-markdown-example
   flake8-markdown-example
   markdown-it-py-example
   myst-nb-example
   sphinx-markdown-tables-example
   sphinx-panels-example
   sphinx-design-example
   sphinx-togglebutton-example
   sphinx-tabs-example
   sphinx-inline-tabs-example
   pyan3-example
   graphviz-example
   pydot-example
   gprof2dot-example
   graphviz2drawio-example
   python-markdown-graphviz-example
   fsmdot-example
   quickdiagrams-example
   dtreeplt-example
   pyprojectviz-example
   pylint-example
   code2flow-example
   snakeviz-example
   pydeps-example
   diagrams-example
   railroad-diagrams-example
   blockdiag-example
   nwdiag-example
   N2G-example
   rptree-example
   pinout-example
   sphinxcontrib-mermaid-example
   sphinxcontrib-plantuml-example
   sphinxcontrib-blockdiag-example
   sphinxcontrib-seqdiag-example
   sphinxcontrib-nwdiag-example
   sphinxcontrib-actdiag-example
   sphinxcontrib-tikz-example
   svg.py-example

Quick Examples
--------------

Basic Documentation
~~~~~~~~~~~~~~~~~~~

A simple documentation page:

.. code-block:: rst

   My Project
   ==========
   
   Welcome to my project documentation!
   
   Features
   --------
   
   * Feature 1
   * Feature 2
   * Feature 3
   
   Installation
   ------------
   
   Install using pip::
   
       pip install myproject
   
   Quick Start
   -----------
   
   .. code-block:: python
   
       import myproject
       
       result = myproject.do_something()
       print(result)

Code Documentation
~~~~~~~~~~~~~~~~~~

Documenting a Python module:

.. code-block:: rst

   API Reference
   =============
   
   .. automodule:: mymodule
      :members:
      :undoc-members:
      :show-inheritance:

Tables
~~~~~~

.. code-block:: rst

   .. list-table:: Features Comparison
      :header-rows: 1
      :widths: 30 30 40
      
      * - Feature
        - Supported
        - Notes
      * - HTML Output
        - Yes
        - Multiple themes
      * - PDF Output
        - Yes
        - Via LaTeX
      * - Search
        - Yes
        - Full-text search

Admonitions
~~~~~~~~~~~

.. code-block:: rst

   .. note::
      This is important information.
   
   .. warning::
      Be careful with this!
   
   .. tip::
      Here's a helpful tip.

Result:

.. note::
   This is important information.

.. warning::
   Be careful with this!

.. tip::
   Here's a helpful tip.

Images
~~~~~~

.. code-block:: rst

   .. figure:: _static/diagram.png
      :width: 600px
      :alt: System Diagram
      
      This is a system architecture diagram.

More Examples
-------------

See the individual example pages for complete, working examples of different 
documentation scenarios.
