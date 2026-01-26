Examples
========

This section contains practical examples demonstrating various Sphinx features.

.. toctree::
   :maxdepth: 2
   
   basic-example
   api-docs-example
   jupyter-example
   graphviz-example

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
