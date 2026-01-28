Sphinxcontrib-CADQuery Example
==============================

This page demonstrates the **sphinxcontrib-cadquery** extension for embedding 3D CAD models created with CadQuery in Sphinx documentation.

.. contents:: Contents
   :local:
   :depth: 2


Basic Models
------------

Simple Box
~~~~~~~~~~

.. cadquery::

   import cadquery as cq
   
   result = cq.Workplane("XY").box(10, 10, 10)

Cylinder
~~~~~~~~

.. cadquery::

   import cadquery as cq
   
   result = cq.Workplane("XY").cylinder(5, 10)

Parametric Models
-----------------

Rounded Box
~~~~~~~~~~~

.. cadquery::

   import cadquery as cq
   
   result = (cq.Workplane("XY")
       .box(20, 20, 5)
       .edges("|Z")
       .fillet(1.0)
   )

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinxcontrib.cadquery',
   ]
   
   cadquery_output_dir = '_cadquery'
   cadquery_format = 'stl'  # or 'step', 'gltf'

See Also
--------

- :doc:`../tutorials/packages/sphinxcontrib-cadquery` - Complete tutorial
- CadQuery documentation: https://cadquery.readthedocs.io/
- GitHub repository: https://github.com/CadQuery/sphinxcontrib-cadquery
