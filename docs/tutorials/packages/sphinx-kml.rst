Sphinx-KML Tutorial
===================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-kml/>`_
   - `API Documentation <../../pdoc/sphinx_kml/index.html>`_
   - `Manual <https://github.com/sphinx-contrib/kml>`_
   - :doc:`Working Example <../../examples/sphinx-kml-example>`


.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinx-kml to embed and document KML (Keyhole Markup Language) files in your Sphinx documentation.

What is Sphinx-KML?
-------------------
sphinx-kml is a Sphinx extension that provides support for working with KML files:

- Embed KML files in documentation
- Display KML content on maps
- Document geographic data
- Visualize GPS tracks and routes
- Show placemarks and polygons
- Integration with Google Earth
- Map layer documentation
- GIS data presentation
- Geographic feature documentation

KML is an XML-based format used for displaying geographic data in mapping applications like Google Earth and Google Maps.

The sphinx-kml extension allows you to include KML/KMZ files, create geographic placemarks, and visualize geographic data in documentation.


Installation
------------

sphinx-kml is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinx_kml; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_kml',
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinx_kml']
   
   # KML configuration
   kml_output_dir = '_static/kml'
   kml_default_map_width = '100%'
   kml_default_map_height = '600px'
   
   # Google Maps integration
   kml_google_maps_api_key = 'YOUR_API_KEY'
   kml_default_zoom = 10
   kml_default_maptype = 'roadmap'  # roadmap, satellite, terrain, hybrid
   
   # Display options
   kml_show_sidebar = True
   kml_enable_download = True
   kml_auto_center = True
   
   # Styling
   kml_default_line_color = '#FF0000'
   kml_default_line_width = 2
   kml_default_fill_color = '#FF000080'


.. code-block:: python

   # Default styles
   kml_default_style = {
       'icon_scale': 1.0,
       'icon_color': 'ff0000ff',
       'line_width': 2,
       'line_color': 'ff00ff00',
       'poly_color': '7f00ff00',
   }
   
   # Viewer settings
   kml_viewer_width = '100%'
   kml_viewer_height = '600px'
   kml_enable_3d = True

Basic Usage
-----------

Embed KML File
~~~~~~~~~~~~~~

.. code-block:: rst

   .. kml::
      :file: _static/data/route.kml

Display with Custom Size
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. kml::
      :file: _static/data/locations.kml
      :width: 800px
      :height: 600px

With Custom Center and Zoom
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. kml::
      :file: _static/data/area.kml
      :center: 37.7749, -122.4194
      :zoom: 12

Multiple KML Layers
~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. kml::
      :files:
         - _static/data/layer1.kml
         - _static/data/layer2.kml
         - _static/data/layer3.kml

   Mountain Hike Trail
   ===================
   
   A beautiful 5-mile loop trail with scenic viewpoints.
   
   Trail Map
   ---------
   
   .. kml::
      :file: ../_static/data/hike.kml
      :width: 100%
      :height: 600px
      :maptype: terrain
   
   Trail Information
   -----------------
   
   - **Distance:** 5 miles
   - **Elevation Gain:** 300 feet
   - **Difficulty:** Moderate
   - **Duration:** 2-3 hours
   - **Best Season:** Spring and Fall
   
   Points of Interest
   ------------------
   
   Trailhead
   ~~~~~~~~~
   
   - GPS: 37.7749, -122.4194
   - Parking available
   - Restrooms on-site
   
   Scenic Viewpoint
   ~~~~~~~~~~~~~~~~
   
   - GPS: 37.7800, -122.4150
   - Elevation: 250 feet
   - Best time: Sunset
   
   Download Trail Data
   -------------------
   
   :download:`Download KML file <../_static/data/hike.kml>`
   
   For use with:
   
   - Google Earth
   - GPS devices
   - Mobile mapping apps

Example 2: Service Area Coverage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/_static/data/coverage.kml``:

.. code-block:: xml

   <?xml version="1.0" encoding="UTF-8"?>
   <kml xmlns="http://www.opengis.net/kml/2.2">
     <Document>
       <name>Service Coverage Areas</name>
       
       <Style id="area1">
         <PolyStyle>
           <color>7f00ff00</color>
         </PolyStyle>
         <LineStyle>
           <color>ff00ff00</color>
           <width>2</width>
         </LineStyle>
       </Style>
       
       <Style id="area2">
         <PolyStyle>
           <color>7fff0000</color>
         </PolyStyle>
         <LineStyle>
           <color>ffff0000</color>
           <width>2</width>
         </LineStyle>
       </Style>
       
       <Placemark>
         <name>Downtown Coverage</name>
         <description>High-speed fiber available</description>
         <styleUrl>#area1</styleUrl>
         <Polygon>
           <outerBoundaryIs>
             <LinearRing>
               <coordinates>
                 -122.42,37.77,0
                 -122.40,37.77,0
                 -122.40,37.79,0
                 -122.42,37.79,0
                 -122.42,37.77,0
               </coordinates>
             </LinearRing>
           </outerBoundaryIs>
         </Polygon>
       </Placemark>
       
       <Placemark>
         <name>Suburban Coverage</name>
         <description>Standard broadband available</description>
         <styleUrl>#area2</styleUrl>
         <Polygon>
           <outerBoundaryIs>
             <LinearRing>
               <coordinates>
                 -122.45,37.75,0
                 -122.42,37.75,0
                 -122.42,37.77,0
                 -122.45,37.77,0
                 -122.45,37.75,0
               </coordinates>
             </LinearRing>
           </outerBoundaryIs>
         </Polygon>
       </Placemark>
     </Document>
   </kml>

``docs/coverage/map.rst``:

.. code-block:: rst

   Service Coverage Map
   ====================
   
   Our network coverage areas.
   
   Coverage Map
   ------------
   
   .. kml::
      :file: ../_static/data/coverage.kml
      :width: 100%
      :height: 500px
      :center: 37.77, -122.42
      :zoom: 13
   
   Coverage Tiers
   --------------
   
   Tier 1 - Downtown (Green)
   ~~~~~~~~~~~~~~~~~~~~~~~~~~
   
   - **Speed:** Up to 1 Gbps
   - **Technology:** Fiber optic
   - **Availability:** 99.9% uptime
   
   Tier 2 - Suburban (Red)
   ~~~~~~~~~~~~~~~~~~~~~~~
   
   - **Speed:** Up to 100 Mbps
   - **Technology:** Cable
   - **Availability:** 99.5% uptime

Example 3: Site Survey Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/_static/data/survey.kml``:

.. code-block:: xml

   <?xml version="1.0" encoding="UTF-8"?>
   <kml xmlns="http://www.opengis.net/kml/2.2">
     <Document>
       <name>Site Survey - Project Alpha</name>
       
       <Style id="proposed">
         <IconStyle>
           <color>ff00ff00</color>
           <Icon>
               <href>http://maps.google.com/mapfiles/kml/paddle/grn-circle.png</href>
           </Icon>
         </IconStyle>
       </Style>
       
       <Style id="existing">
         <IconStyle>
           <color>ff0000ff</color>
           <Icon>
               <href>http://maps.google.com/mapfiles/kml/paddle/blu-circle.png</href>
           </Icon>
         </IconStyle>
       </Style>
       
       <Folder>
         <name>Existing Infrastructure</name>
         <Placemark>
           <name>Tower Site A</name>
           <description>
             <![CDATA[
               <h3>Cell Tower A</h3>
               <ul>
                 <li>Height: 150 ft</li>
                 <li>Power: Grid + Backup</li>
                 <li>Status: Operational</li>
               </ul>
             ]]>
           </description>
           <styleUrl>#existing</styleUrl>
           <Point>
             <coordinates>-122.41,37.78,0</coordinates>
           </Point>
         </Placemark>
       </Folder>
       
       <Folder>
         <name>Proposed Sites</name>
         <Placemark>
           <name>Proposed Site B</name>
           <description>
             <![CDATA[
               <h3>Proposed Tower B</h3>
               <ul>
                 <li>Height: 180 ft</li>
                 <li>Coverage: 2 mile radius</li>
                 <li>Status: Pending approval</li>
               </ul>
             ]]>
           </description>
           <styleUrl>#proposed</styleUrl>
           <Point>
             <coordinates>-122.43,37.76,0</coordinates>
           </Point>
         </Placemark>
       </Folder>
     </Document>
   </kml>

``docs/projects/site-survey.rst``:

.. code-block:: rst

   Project Alpha - Site Survey
   ============================
   
   Network infrastructure expansion plan.
   
   Site Map
   --------
   
   .. kml::
      :file: ../_static/data/survey.kml
      :width: 100%
      :height: 600px
      :maptype: hybrid
   
   Legend:
   
   - 🔵 Blue: Existing infrastructure
   - 🟢 Green: Proposed sites
   
   Infrastructure Summary
   ----------------------
   
   Existing Sites
   ~~~~~~~~~~~~~~
   
   .. list-table::
      :header-rows: 1
      
      * - Site ID
        - Location
        - Status
        - Coverage
      * - Tower A
        - 37.78, -122.41
        - Operational
        - 1.5 mi radius
   
   Proposed Additions
   ~~~~~~~~~~~~~~~~~~
   
   .. list-table::
      :header-rows: 1
      
      * - Site ID
        - Location
        - Status
        - Coverage
      * - Tower B
        - 37.76, -122.43
        - Pending
        - 2.0 mi radius

Advanced Features
-----------------

Network Links
~~~~~~~~~~~~~

Reference external KML:

.. code-block:: xml

   <NetworkLink>
     <name>Real-time Traffic</name>
     <Link>
       <href>https://example.com/traffic.kml</href>
       <refreshMode>onInterval</refreshMode>
       <refreshInterval>60</refreshInterval>
     </Link>
   </NetworkLink>

Time-based Animation
~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <Placemark>
     <name>Moving Vehicle</name>
     <TimeSpan>
       <begin>2026-01-25T09:00:00Z</begin>
       <end>2026-01-25T17:00:00Z</end>
     </TimeSpan>
     <Point>
       <coordinates>-122.41,37.78,0</coordinates>
     </Point>
   </Placemark>

Custom Icons
~~~~~~~~~~~~

.. code-block:: xml

   <Style id="customIcon">
     <IconStyle>
       <Icon>
         <href>https://example.com/icon.png</href>
       </Icon>
       <scale>1.2</scale>
     </IconStyle>
   </Style>

3D Models
~~~~~~~~~

.. code-block:: xml

   <Placemark>
     <name>Building</name>
     <Model>
       <altitudeMode>absolute</altitudeMode>
       <Location>
         <longitude>-122.41</longitude>
         <latitude>37.78</latitude>
         <altitude>100</altitude>
       </Location>
       <Link>
         <href>models/building.dae</href>
       </Link>
     </Model>
   </Placemark>

Docker Integration
------------------

Build with KML Files
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     kensai-sphinx:latest \
     sphinx-build -b html /project/docs /project/docs/_build/html

Validate KML Files
~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     kensai-sphinx:latest \
     xmllint --noout /project/docs/_static/data/*.kml

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Build Docs with KML
   
   on:
     push:
       paths:
         - 'docs/**'
         - 'docs/_static/data/*.kml'
   
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Validate KML Files
           run: |
             docker run --rm -v $(pwd):/project \
               kensai-sphinx:latest \
               sh -c "xmllint --noout /project/docs/_static/data/*.kml"
         
         - name: Build Documentation
           run: |
             docker run --rm -v $(pwd):/project \
               kensai-sphinx:latest \
               sphinx-build -b html /project/docs /project/docs/_build/html
         
         - name: Deploy
           uses: peaceiris/actions-gh-pages@v3
           with:
             github_token: ${{ secrets.GITHUB_TOKEN }}
             publish_dir: ./docs/_build/html

Best Practices
--------------

1. **Organize KML Files**
   
   Structure your files:
   
   .. code-block:: text
   
      docs/
      └── _static/
          └── data/
              ├── routes/
              │   ├── trail1.kml
              │   └── trail2.kml
              ├── coverage/
              │   └── areas.kml
              └── sites/
                  └── locations.kml

2. **Use Folders for Organization**
   
   .. code-block:: xml
   
      <Folder>
        <name>Category 1</name>
        <!-- Placemarks -->
      </Folder>

3. **Add Rich Descriptions**
   
   Use HTML in descriptions:
   
   .. code-block:: xml
   
      <description>
        <![CDATA[
          <h3>Title</h3>
          <p>Details here</p>
          <img src="photo.jpg" />
        ]]>
      </description>

4. **Validate KML**
   
   Use xmllint or online validators

5. **Provide Downloads**
   
   Let users download KML files for their own use

6. **Document Coordinate System**
   
   Specify if using WGS84 (standard)

Common Patterns
---------------

Location Documentation
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Location: {{ name }}
   =====================
   
   .. kml::
      :file: {{ kml_file }}
      :width: 100%
      :height: 500px
   
   :download:`Download KML <{{ kml_file }}>`

Troubleshooting
---------------

KML Not Displaying
~~~~~~~~~~~~~~~~~~

**Solution:**

1. Validate XML syntax:

   .. code-block:: bash
   
      xmllint --noout file.kml

2. Check file path is correct

3. Verify namespace declaration

Invalid Coordinates
~~~~~~~~~~~~~~~~~~~

**Solution:**

Format: longitude,latitude,altitude

.. code-block:: xml

   <!-- Correct -->
   <coordinates>-122.41,37.78,0</coordinates>
   
   <!-- Wrong - latitude first -->
   <coordinates>37.78,-122.41,0</coordinates>

Styling Not Applied
~~~~~~~~~~~~~~~~~~~

**Solution:**

Define styles before referencing:

.. code-block:: xml

   <Style id="myStyle">
     <!-- Style definition -->
   </Style>
   
   <Placemark>
     <styleUrl>#myStyle</styleUrl>
   </Placemark>

Large Files Performance
~~~~~~~~~~~~~~~~~~~~~~~

**Solution:**

- Split into multiple files
- Use NetworkLinks for dynamic loading
- Simplify geometries

Next Steps
----------

1. Create KML files for your geographic data
2. Organize files in _static/data directory
3. Embed maps in relevant documentation
4. Add download links for users
5. Document coordinate systems and projections

Additional Resources
--------------------

- :doc:`sphinxcontrib-googlemaps` - Google Maps integration
- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `KML Reference <https://developers.google.com/kml/documentation/kmlreference>`_
- `Google Earth <https://earth.google.com/>`_
