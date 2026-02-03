Sphinxcontrib-CadQuery Tutorial
===============================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinxcontrib-cadquery/>`_
   - `API Documentation <../../pdoc/sphinxcontrib_cadquery/index.html>`_
   - `Manual <https://github.com/CadQuery/sphinxcontrib-cadquery>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinxcontrib-cadquery to embed interactive 3D CAD models created with CadQuery in your Sphinx documentation.

What is Sphinxcontrib-CadQuery?
--------------------------------
sphinxcontrib-cadquery is a Sphinx extension that provides:

- Embed CadQuery 3D models in documentation
- Interactive 3D visualization
- Parametric CAD model documentation
- STL/STEP file generation
- Design documentation
- Engineering drawings integration
- Assembly visualization
- Part libraries documentation
- Manufacturing documentation
- 3D viewer integration

CadQuery is a Python library for building parametric 3D CAD models. This extension lets you document those models directly in Sphinx.

The sphinxcontrib-cadquery extension allows you to include parametric 3D CAD models in documentation with interactive viewers.


Installation
------------

sphinxcontrib-cadquery is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm viper-sphinx:latest python -c "import sphinxcontrib.cadquery; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinxcontrib.cadquery',
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinxcontrib.cadquery']
   
   # CadQuery configuration
   cadquery_output_dir = '_static/cadquery'
   cadquery_image_format = 'png'  # png, svg
   cadquery_image_width = 800
   cadquery_image_height = 600
   
   # 3D viewer options
   cadquery_enable_3d_viewer = True
   cadquery_viewer_backend = 'threejs'  # threejs, x3dom
   cadquery_viewer_width = '100%'
   cadquery_viewer_height = '600px'
   
   # Rendering options
   cadquery_default_color = (204, 204, 204)
   cadquery_render_edges = True
   cadquery_render_axes = True
   cadquery_background_color = (255, 255, 255)
   
   # Export options
   cadquery_export_stl = True
   cadquery_export_step = True
   cadquery_export_svg = True
   
   # Display options
   cadquery_show_code = True
   cadquery_show_download_links = True


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Basic Setup
~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinxcontrib.cadquery',
   ]
   
   cadquery_output_dir = '_cadquery'
   cadquery_format = 'stl'  # or 'step', 'gltf'

Basic Usage
-----------

Simple 3D Model
~~~~~~~~~~~~~~~

.. code-block:: rst

   .. cadquery::
      
      import cadquery as cq
      
      result = cq.Workplane("XY").box(10, 10, 10)

With Parameters
~~~~~~~~~~~~~~~

.. code-block:: rst

   .. cadquery::
      :height: 500
      :width: 800
      
      import cadquery as cq
      
      # Create a cube with chamfered edges
      result = (cq.Workplane("XY")
                  .box(20, 20, 20)
                  .edges()
                  .chamfer(2))

Multiple Views
~~~~~~~~~~~~~~

.. code-block:: rst

   .. cadquery::
      :views: isometric, top, front
      
      import cadquery as cq
      
      result = cq.Workplane("XY").cylinder(10, 20)

With Download Links
~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. cadquery::
      :export: stl, step
      
      import cadquery as cq
      
      result = cq.Workplane("XY").sphere(10)

   Mounting Bracket
   ================
   
   A simple L-bracket for mounting components.
   
   Design Overview
   ---------------
   
   .. cadquery::
      :height: 600
      :export: stl, step
      
      import cadquery as cq
      
      # Parameters
      length = 50
      width = 40
      thickness = 5
      hole_dia = 5
      
      # Create the L-bracket
      result = (
          cq.Workplane("XY")
          # Base plate
          .box(length, width, thickness)
          # Vertical plate
          .faces(">Z")
          .workplane()
          .transformed(offset=(0, width/2 - thickness/2, length/2 - thickness/2))
          .box(thickness, thickness, length)
          # Add mounting holes
          .faces("<Z")
          .workplane()
          .pushPoints([(-15, 0), (15, 0)])
          .hole(hole_dia)
          # Chamfer edges
          .edges()
          .chamfer(1)
      )
   
   Specifications
   --------------
   
   .. list-table::
      :header-rows: 1
      
      * - Parameter
        - Value
        - Unit
      * - Length
        - 50
        - mm
      * - Width
        - 40
        - mm
      * - Thickness
        - 5
        - mm
      * - Hole Diameter
        - 5
        - mm
      * - Material
        - Aluminum 6061
        - 
   
   Manufacturing Notes
   -------------------
   
   - **Process:** CNC milling or waterjet cutting
   - **Tolerance:** ±0.1 mm
   - **Finish:** Anodized
   - **Post-processing:** Deburr all edges
   
   Downloads
   ---------
   
   - :download:`STL file </_static/cadquery/bracket.stl>`
   - :download:`STEP file </_static/cadquery/bracket.step>`

Example 2: Parametric Design
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/parts/enclosure.rst``:

.. code-block:: rst

   Electronics Enclosure
   =====================
   
   Parametric enclosure design for electronics projects.
   
   Default Configuration
   ---------------------
   
   .. cadquery::
      :height: 600
      :views: isometric, top
      
      import cadquery as cq
      
      # Enclosure parameters
      box_length = 100
      box_width = 60
      box_height = 40
      wall_thickness = 3
      corner_radius = 5
      
      # Create outer shell
      outer = (
          cq.Workplane("XY")
          .box(box_length, box_width, box_height)
          .edges("|Z")
          .fillet(corner_radius)
      )
      
      # Create inner cavity
      inner = (
          cq.Workplane("XY")
          .box(
              box_length - 2*wall_thickness,
              box_width - 2*wall_thickness,
              box_height - wall_thickness
          )
          .translate((0, 0, wall_thickness/2))
      )
      
      # Subtract inner from outer
      result = outer.cut(inner)
      
      # Add mounting posts
      post_positions = [
          (box_length/2 - 10, box_width/2 - 10),
          (-box_length/2 + 10, box_width/2 - 10),
          (box_length/2 - 10, -box_width/2 + 10),
          (-box_length/2 + 10, -box_width/2 + 10),
      ]
      
      for x, y in post_positions:
          post = (
              cq.Workplane("XY")
              .transformed(offset=(x, y, -box_height/2 + wall_thickness))
              .circle(3)
              .extrude(box_height - 2*wall_thickness)
              .faces(">Z")
              .hole(2.5)
          )
          result = result.union(post)
   
   Custom Sizes
   ------------
   
   Small Version (60x40x30 mm):
   
   .. cadquery::
      
      import cadquery as cq
      
      # Parameters for small enclosure
      params = {
          'length': 60,
          'width': 40,
          'height': 30,
          'wall': 2,
      }
      
      result = (
          cq.Workplane("XY")
          .box(params['length'], params['width'], params['height'])
          .shell(-params['wall'])
      )
   
   Large Version (150x100x50 mm):
   
   .. cadquery::
      
      import cadquery as cq
      
      params = {
          'length': 150,
          'width': 100,
          'height': 50,
          'wall': 4,
      }
      
      result = (
          cq.Workplane("XY")
          .box(params['length'], params['width'], params['height'])
          .shell(-params['wall'])
          .edges("|Z")
          .fillet(8)
      )

Example 3: Assembly Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/assemblies/gearbox.rst``:

.. code-block:: rst

   Gearbox Assembly
   ================
   
   Simple gear reduction assembly.
   
   Drive Gear
   ----------
   
   .. cadquery::
      
      import cadquery as cq
      
      # Drive gear parameters
      teeth = 20
      module = 2
      width = 10
      bore = 6
      
      # Simplified gear (actual gear teeth require more complex code)
      outer_dia = teeth * module
      
      result = (
          cq.Workplane("XY")
          .circle(outer_dia/2)
          .extrude(width)
          .faces(">Z")
          .circle(bore/2)
          .cutThruAll()
      )
   
   Driven Gear
   -----------
   
   .. cadquery::
      
      import cadquery as cq
      
      # Driven gear (larger, 2:1 ratio)
      teeth = 40
      module = 2
      width = 10
      bore = 8
      
      outer_dia = teeth * module
      
      result = (
          cq.Workplane("XY")
          .circle(outer_dia/2)
          .extrude(width)
          .faces(">Z")
          .circle(bore/2)
          .cutThruAll()
      )
   
   Housing
   -------
   
   .. cadquery::
      :height: 600
      
      import cadquery as cq
      
      # Gearbox housing
      length = 120
      width = 80
      height = 30
      wall = 5
      
      result = (
          cq.Workplane("XY")
          .box(length, width, height)
          .shell(-wall)
          # Shaft holes
          .faces(">Y")
          .workplane()
          .pushPoints([(-30, 0), (30, 0)])
          .hole(10)
      )

Advanced Features
-----------------

Custom Materials
~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. cadquery::
      :color: (100, 150, 200)
      :alpha: 0.8
      
      import cadquery as cq
      
      result = cq.Workplane("XY").box(10, 10, 10)

Multiple Objects
~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. cadquery::
      
      import cadquery as cq
      
      # Create multiple objects
      box1 = cq.Workplane("XY").box(10, 10, 10).translate((-15, 0, 0))
      box2 = cq.Workplane("XY").box(10, 10, 10).translate((0, 0, 0))
      box3 = cq.Workplane("XY").box(10, 10, 10).translate((15, 0, 0))
      
      result = box1.union(box2).union(box3)

Cross-sections
~~~~~~~~~~~~~~

.. code-block:: rst

   .. cadquery::
      
      import cadquery as cq
      
      # Create part
      part = cq.Workplane("XY").box(20, 20, 20)
      
      # Show cross-section
      result = part.faces(">X").workplane(-10).split(keepTop=True)

Annotations
~~~~~~~~~~~

Add dimensions and notes:

.. code-block:: rst

   .. cadquery::
      :show-dimensions: True
      
      import cadquery as cq
      
      result = cq.Workplane("XY").box(50, 30, 10)

Boolean Operations
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. cadquery::
      
      import cadquery as cq
      
      # Create base
      base = cq.Workplane("XY").box(30, 30, 10)
      
      # Create hole
      hole = cq.Workplane("XY").cylinder(15, 5)
      
      # Subtract hole from base
      result = base.cut(hole)

Docker Integration
------------------

Build Documentation
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     viper-sphinx:latest \
     sphinx-build -b html /project/docs /project/docs/_build/html

Generate STL Files
~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     viper-sphinx:latest \
     python /project/scripts/export_models.py

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Build CAD Documentation
   
   on:
     push:
       paths:
         - 'docs/parts/**'
         - 'docs/assemblies/**'
   
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Build Documentation
           run: |
             docker run --rm -v $(pwd):/project \
               viper-sphinx:latest \
               sphinx-build -b html /project/docs /project/docs/_build/html
         
         - name: Upload STL Files
           uses: actions/upload-artifact@v3
           with:
             name: stl-files
             path: docs/_build/html/_static/cadquery/*.stl
         
         - name: Upload STEP Files
           uses: actions/upload-artifact@v3
           with:
             name: step-files
             path: docs/_build/html/_static/cadquery/*.step

Best Practices
--------------

1. **Use Parameters**
   
   Make designs configurable:
   
   .. code-block:: python
   
      # Define parameters at top
      LENGTH = 50
      WIDTH = 30
      HEIGHT = 10

2. **Comment Your Code**
   
   Explain design decisions

3. **Consistent Units**
   
   Always use millimeters (mm)

4. **Meaningful Names**
   
   Use descriptive variable names

5. **Modular Design**
   
   Break complex models into functions

6. **Export Multiple Formats**
   
   Provide STL and STEP files

Common Patterns
---------------

Parametric Function
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   def create_bracket(length, width, thickness, hole_dia):
       """Create parametric L-bracket."""
       result = (
           cq.Workplane("XY")
           .box(length, width, thickness)
           .faces(">Z")
           .workplane()
           .hole(hole_dia)
       )
       return result

Troubleshooting
---------------

CadQuery Import Error
~~~~~~~~~~~~~~~~~~~~~

**Solution:**

Ensure CadQuery is installed:

.. code-block:: bash

   pip install cadquery

Viewer Not Loading
~~~~~~~~~~~~~~~~~~

**Solution:**

Check JavaScript is enabled:

.. code-block:: python

   cadquery_enable_3d_viewer = True

Export Files Missing
~~~~~~~~~~~~~~~~~~~~

**Solution:**

Enable exports:

.. code-block:: python

   cadquery_export_stl = True
   cadquery_export_step = True

Render Quality Issues
~~~~~~~~~~~~~~~~~~~~~

**Solution:**

Increase image resolution:

.. code-block:: python

   cadquery_image_width = 1200
   cadquery_image_height = 900

Next Steps
----------

1. Document your mechanical parts
2. Create parametric designs
3. Generate manufacturing files
4. Build part libraries
5. Create assembly documentation


Practical Examples
------------------

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


Practical Examples
------------------

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


Practical Examples
------------------

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

Additional Resources
--------------------
- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `CadQuery Documentation <https://cadquery.readthedocs.io/>`_
- `CadQuery GitHub <https://github.com/CadQuery/cadquery>`_
- `OpenCASCADE <https://www.opencascade.com/>`_
- :doc:`../tutorials/packages/sphinxcontrib-cadquery` - Complete tutorial
- CadQuery documentation: https://cadquery.readthedocs.io/
- GitHub repository: https://github.com/CadQuery/sphinxcontrib-cadquery

