Sphinx-KML Tutorial
===================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-kml/>`_
   - `API Documentation <../../pdoc/sphinx_kml/index.html>`_
   - `Manual <https://github.com/sphinx-contrib/kml>`_

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

   docker run --rm viper-sphinx:latest python -c "import sphinx_kml; print('Installed')"

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
     viper-sphinx:latest \
     sphinx-build -b html /project/docs /project/docs/_build/html

Validate KML Files
~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     viper-sphinx:latest \
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
               viper-sphinx:latest \
               sh -c "xmllint --noout /project/docs/_static/data/*.kml"
         
         - name: Build Documentation
           run: |
             docker run --rm -v $(pwd):/project \
               viper-sphinx:latest \
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


Practical Examples
------------------

Basic KML Elements
------------------

Simple Placemark
~~~~~~~~~~~~~~~~

.. kml::

   <?xml version="1.0" encoding="UTF-8"?>
   <kml xmlns="http://www.opengis.net/kml/2.2">
     <Placemark>
       <name>Golden Gate Bridge</name>
       <Point>
         <coordinates>-122.4783,37.8199,0</coordinates>
       </Point>
     </Placemark>
   </kml>

With Description
~~~~~~~~~~~~~~~~

.. kml::

   <Placemark>
     <name>Eiffel Tower</name>
     <description>Famous iron lattice tower in Paris</description>
     <Point>
       <coordinates>2.2945,48.8584,324</coordinates>
     </Point>
   </Placemark>

Multiple Placemarks
~~~~~~~~~~~~~~~~~~~

.. kml::

   <Folder>
     <name>World Landmarks</name>
     <Placemark>
       <name>Statue of Liberty</name>
       <Point>
         <coordinates>-74.0445,40.6892,0</coordinates>
       </Point>
     </Placemark>
     <Placemark>
       <name>Big Ben</name>
       <Point>
         <coordinates>-0.1246,51.5007,0</coordinates>
       </Point>
     </Placemark>
   </Folder>

Styled Elements
---------------

Custom Icon
~~~~~~~~~~~

.. kml::

   <Placemark>
     <name>Custom Marker</name>
     <Style>
       <IconStyle>
         <Icon>
           <href>http://maps.google.com/mapfiles/kml/paddle/red-circle.png</href>
         </Icon>
       </IconStyle>
     </Style>
     <Point>
       <coordinates>-122.0842,37.4224,0</coordinates>
     </Point>
   </Placemark>

Colored Line
~~~~~~~~~~~~

.. kml::

   <Placemark>
     <name>Route</name>
     <Style>
       <LineStyle>
         <color>ff0000ff</color>
         <width>4</width>
       </LineStyle>
     </Style>
     <LineString>
       <coordinates>
         -122.4194,37.7749,0
         -122.0842,37.4224,0
       </coordinates>
     </LineString>
   </Placemark>

Polygon Area
~~~~~~~~~~~~

.. kml::

   <Placemark>
     <name>Coverage Area</name>
     <Style>
       <PolyStyle>
         <color>7f00ff00</color>
       </PolyStyle>
       <LineStyle>
         <color>ff00ff00</color>
         <width>2</width>
       </LineStyle>
     </Style>
     <Polygon>
       <outerBoundaryIs>
         <LinearRing>
           <coordinates>
             -122.5,37.8,0
             -122.3,37.8,0
             -122.3,37.6,0
             -122.5,37.6,0
             -122.5,37.8,0
           </coordinates>
         </LinearRing>
       </outerBoundaryIs>
     </Polygon>
   </Placemark>

Geographic Features
-------------------

Path/Route
~~~~~~~~~~

.. kml::

   <Placemark>
     <name>Hiking Trail</name>
     <description>5 mile scenic trail</description>
     <LineString>
       <tessellate>1</tessellate>
       <coordinates>
         -112.2550,36.0800,2357
         -112.2545,36.0826,2423
         -112.2540,36.0848,2456
         -112.2530,36.0870,2498
       </coordinates>
     </LineString>
   </Placemark>

Ground Overlay
~~~~~~~~~~~~~~

.. kml::

   <GroundOverlay>
     <name>Map Overlay</name>
     <Icon>
       <href>https://example.com/map-overlay.png</href>
     </Icon>
     <LatLonBox>
       <north>37.83234</north>
       <south>37.82234</south>
       <east>-122.37567</east>
       <west>-122.38567</west>
     </LatLonBox>
   </GroundOverlay>

Network Link
~~~~~~~~~~~~

.. kml::

   <NetworkLink>
     <name>Live Data</name>
     <Link>
       <href>https://example.com/live-data.kml</href>
       <refreshMode>onInterval</refreshMode>
       <refreshInterval>300</refreshInterval>
     </Link>
   </NetworkLink>

Organization
------------

Folders
~~~~~~~

.. kml::

   <Folder>
     <name>US Cities</name>
     <Folder>
       <name>West Coast</name>
       <Placemark>
         <name>San Francisco</name>
         <Point><coordinates>-122.4194,37.7749,0</coordinates></Point>
       </Placemark>
       <Placemark>
         <name>Los Angeles</name>
         <Point><coordinates>-118.2437,34.0522,0</coordinates></Point>
       </Placemark>
     </Folder>
     <Folder>
       <name>East Coast</name>
       <Placemark>
         <name>New York</name>
         <Point><coordinates>-74.0060,40.7128,0</coordinates></Point>
       </Placemark>
     </Folder>
   </Folder>

Document Structure
~~~~~~~~~~~~~~~~~~

.. kml::

   <Document>
     <name>My Places</name>
     <description>Collection of interesting locations</description>
     <Style id="redIcon">
       <IconStyle>
         <color>ff0000ff</color>
         <scale>1.2</scale>
       </IconStyle>
     </Style>
     <Placemark>
       <name>Important Location</name>
       <styleUrl>#redIcon</styleUrl>
       <Point><coordinates>-122.0842,37.4224,0</coordinates></Point>
     </Placemark>
   </Document>

Configuration Examples
----------------------

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_kml',
   ]
   
   # KML settings
   kml_output_dir = '_kml'
   kml_viewer = 'google-earth'  # or 'google-maps'

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

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

External KML Files
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # KML file inclusion
   kml_include_path = ['_kml', 'data/kml']
   kml_download_enabled = True

Practical Examples
------------------

Store Locations
~~~~~~~~~~~~~~~

.. kml::

   <Document>
     <name>Store Locations</name>
     <Style id="store">
       <IconStyle>
         <Icon>
           <href>http://maps.google.com/mapfiles/kml/paddle/blu-blank.png</href>
         </Icon>
       </IconStyle>
     </Style>
     <Placemark>
       <name>Downtown Store</name>
       <description>Mon-Sat 9AM-9PM, Sun 10AM-6PM</description>
       <styleUrl>#store</styleUrl>
       <Point><coordinates>-122.4194,37.7749,0</coordinates></Point>
     </Placemark>
     <Placemark>
       <name>Airport Store</name>
       <description>Daily 6AM-10PM</description>
       <styleUrl>#store</styleUrl>
       <Point><coordinates>-122.3900,37.6213,0</coordinates></Point>
     </Placemark>
   </Document>

Delivery Routes
~~~~~~~~~~~~~~~

.. kml::

   <Document>
     <name>Delivery Routes</name>
     <Style id="route1">
       <LineStyle>
         <color>ff0000ff</color>
         <width>3</width>
       </LineStyle>
     </Style>
     <Placemark>
       <name>Route A</name>
       <description>Morning deliveries</description>
       <styleUrl>#route1</styleUrl>
       <LineString>
         <coordinates>
           -122.4194,37.7749,0
           -122.4083,37.7833,0
           -122.4000,37.7900,0
           -122.3917,37.7967,0
         </coordinates>
       </LineString>
     </Placemark>
   </Document>

Service Areas
~~~~~~~~~~~~~

.. kml::

   <Placemark>
     <name>Service Coverage</name>
     <description>Primary service area</description>
     <Style>
       <PolyStyle>
         <color>4d0000ff</color>
       </PolyStyle>
       <LineStyle>
         <color>ff0000ff</color>
         <width>2</width>
       </LineStyle>
     </Style>
     <Polygon>
       <outerBoundaryIs>
         <LinearRing>
           <coordinates>
             -122.5000,37.8000,0
             -122.3000,37.8000,0
             -122.3000,37.6000,0
             -122.5000,37.6000,0
             -122.5000,37.8000,0
           </coordinates>
         </LinearRing>
       </outerBoundaryIs>
     </Polygon>
   </Placemark>

Tourist Attractions
~~~~~~~~~~~~~~~~~~~

.. kml::

   <Document>
     <name>City Tour</name>
     <Placemark>
       <name>Museum</name>
       <description><![CDATA[
         <h3>City Museum</h3>
         <p>Open: 10AM-6PM</p>
         <p>Admission: $15</p>
       ]]></description>
       <Point><coordinates>-122.4183,37.7833,0</coordinates></Point>
     </Placemark>
     <Placemark>
       <name>Park</name>
       <description><![CDATA[
         <h3>Central Park</h3>
         <p>Open: 6AM-10PM</p>
         <p>Free admission</p>
       ]]></description>
       <Point><coordinates>-122.4500,37.7700,0</coordinates></Point>
     </Placemark>
   </Document>

Advanced Features
-----------------

Time-based Animation
~~~~~~~~~~~~~~~~~~~~

.. kml::

   <Placemark>
     <name>Moving Object</name>
     <TimeStamp>
       <when>2024-01-01T12:00:00Z</when>
     </TimeStamp>
     <Point><coordinates>-122.4194,37.7749,0</coordinates></Point>
   </Placemark>

Camera Views
~~~~~~~~~~~~

.. kml::

   <Placemark>
     <name>Viewpoint</name>
     <LookAt>
       <longitude>-122.4194</longitude>
       <latitude>37.7749</latitude>
       <altitude>0</altitude>
       <heading>0</heading>
       <tilt>60</tilt>
       <range>5000</range>
     </LookAt>
     <Point><coordinates>-122.4194,37.7749,0</coordinates></Point>
   </Placemark>

Photo Overlays
~~~~~~~~~~~~~~

.. kml::

   <PhotoOverlay>
     <name>Photo Location</name>
     <Icon>
       <href>https://example.com/photo.jpg</href>
     </Icon>
     <ViewVolume>
       <leftFov>-60</leftFov>
       <rightFov>60</rightFov>
       <bottomFov>-45</bottomFov>
       <topFov>45</topFov>
       <near>10</near>
     </ViewVolume>
     <Point><coordinates>-122.4194,37.7749,10</coordinates></Point>
   </PhotoOverlay>

Integration with Maps
---------------------

Google Earth
~~~~~~~~~~~~

.. kml-file:: locations.kml
   :viewer: google-earth
   :download: true
   
   Interactive visualization in Google Earth

Google Maps
~~~~~~~~~~~

.. kml-file:: routes.kml
   :viewer: google-maps
   :embed: true
   :height: 500px

Inline Rendering
~~~~~~~~~~~~~~~~

.. kml::
   :render: inline
   :width: 800px
   :height: 600px

   <Placemark>
     <name>Location</name>
     <Point><coordinates>-122.4194,37.7749,0</coordinates></Point>
   </Placemark>

Export Options
--------------

Download Links
~~~~~~~~~~~~~~

.. kml-download:: my-places.kml
   
   Download KML file for offline use

Multiple Formats
~~~~~~~~~~~~~~~~

.. kml-export::
   :formats: kml, kmz, geojson
   :source: locations.kml

API Integration
---------------

Dynamic KML
~~~~~~~~~~~

.. code-block:: python

   # Generate KML from data
   from sphinx_kml import KMLGenerator
   
   gen = KMLGenerator()
   for location in get_locations():
       gen.add_placemark(
           name=location.name,
           coords=(location.lon, location.lat),
           description=location.desc
       )
   
   kml_content = gen.to_kml()


Practical Examples
------------------

Basic KML Elements
------------------

Simple Placemark
~~~~~~~~~~~~~~~~

.. kml::

   <?xml version="1.0" encoding="UTF-8"?>
   <kml xmlns="http://www.opengis.net/kml/2.2">
     <Placemark>
       <name>Golden Gate Bridge</name>
       <Point>
         <coordinates>-122.4783,37.8199,0</coordinates>
       </Point>
     </Placemark>
   </kml>

With Description
~~~~~~~~~~~~~~~~

.. kml::

   <Placemark>
     <name>Eiffel Tower</name>
     <description>Famous iron lattice tower in Paris</description>
     <Point>
       <coordinates>2.2945,48.8584,324</coordinates>
     </Point>
   </Placemark>

Multiple Placemarks
~~~~~~~~~~~~~~~~~~~

.. kml::

   <Folder>
     <name>World Landmarks</name>
     <Placemark>
       <name>Statue of Liberty</name>
       <Point>
         <coordinates>-74.0445,40.6892,0</coordinates>
       </Point>
     </Placemark>
     <Placemark>
       <name>Big Ben</name>
       <Point>
         <coordinates>-0.1246,51.5007,0</coordinates>
       </Point>
     </Placemark>
   </Folder>

Styled Elements
---------------

Custom Icon
~~~~~~~~~~~

.. kml::

   <Placemark>
     <name>Custom Marker</name>
     <Style>
       <IconStyle>
         <Icon>
           <href>http://maps.google.com/mapfiles/kml/paddle/red-circle.png</href>
         </Icon>
       </IconStyle>
     </Style>
     <Point>
       <coordinates>-122.0842,37.4224,0</coordinates>
     </Point>
   </Placemark>

Colored Line
~~~~~~~~~~~~

.. kml::

   <Placemark>
     <name>Route</name>
     <Style>
       <LineStyle>
         <color>ff0000ff</color>
         <width>4</width>
       </LineStyle>
     </Style>
     <LineString>
       <coordinates>
         -122.4194,37.7749,0
         -122.0842,37.4224,0
       </coordinates>
     </LineString>
   </Placemark>

Polygon Area
~~~~~~~~~~~~

.. kml::

   <Placemark>
     <name>Coverage Area</name>
     <Style>
       <PolyStyle>
         <color>7f00ff00</color>
       </PolyStyle>
       <LineStyle>
         <color>ff00ff00</color>
         <width>2</width>
       </LineStyle>
     </Style>
     <Polygon>
       <outerBoundaryIs>
         <LinearRing>
           <coordinates>
             -122.5,37.8,0
             -122.3,37.8,0
             -122.3,37.6,0
             -122.5,37.6,0
             -122.5,37.8,0
           </coordinates>
         </LinearRing>
       </outerBoundaryIs>
     </Polygon>
   </Placemark>

Geographic Features
-------------------

Path/Route
~~~~~~~~~~

.. kml::

   <Placemark>
     <name>Hiking Trail</name>
     <description>5 mile scenic trail</description>
     <LineString>
       <tessellate>1</tessellate>
       <coordinates>
         -112.2550,36.0800,2357
         -112.2545,36.0826,2423
         -112.2540,36.0848,2456
         -112.2530,36.0870,2498
       </coordinates>
     </LineString>
   </Placemark>

Ground Overlay
~~~~~~~~~~~~~~

.. kml::

   <GroundOverlay>
     <name>Map Overlay</name>
     <Icon>
       <href>https://example.com/map-overlay.png</href>
     </Icon>
     <LatLonBox>
       <north>37.83234</north>
       <south>37.82234</south>
       <east>-122.37567</east>
       <west>-122.38567</west>
     </LatLonBox>
   </GroundOverlay>

Network Link
~~~~~~~~~~~~

.. kml::

   <NetworkLink>
     <name>Live Data</name>
     <Link>
       <href>https://example.com/live-data.kml</href>
       <refreshMode>onInterval</refreshMode>
       <refreshInterval>300</refreshInterval>
     </Link>
   </NetworkLink>

Organization
------------

Folders
~~~~~~~

.. kml::

   <Folder>
     <name>US Cities</name>
     <Folder>
       <name>West Coast</name>
       <Placemark>
         <name>San Francisco</name>
         <Point><coordinates>-122.4194,37.7749,0</coordinates></Point>
       </Placemark>
       <Placemark>
         <name>Los Angeles</name>
         <Point><coordinates>-118.2437,34.0522,0</coordinates></Point>
       </Placemark>
     </Folder>
     <Folder>
       <name>East Coast</name>
       <Placemark>
         <name>New York</name>
         <Point><coordinates>-74.0060,40.7128,0</coordinates></Point>
       </Placemark>
     </Folder>
   </Folder>

Document Structure
~~~~~~~~~~~~~~~~~~

.. kml::

   <Document>
     <name>My Places</name>
     <description>Collection of interesting locations</description>
     <Style id="redIcon">
       <IconStyle>
         <color>ff0000ff</color>
         <scale>1.2</scale>
       </IconStyle>
     </Style>
     <Placemark>
       <name>Important Location</name>
       <styleUrl>#redIcon</styleUrl>
       <Point><coordinates>-122.0842,37.4224,0</coordinates></Point>
     </Placemark>
   </Document>

Configuration Examples
----------------------

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_kml',
   ]
   
   # KML settings
   kml_output_dir = '_kml'
   kml_viewer = 'google-earth'  # or 'google-maps'

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

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

External KML Files
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # KML file inclusion
   kml_include_path = ['_kml', 'data/kml']
   kml_download_enabled = True

Practical Examples
------------------

Store Locations
~~~~~~~~~~~~~~~

.. kml::

   <Document>
     <name>Store Locations</name>
     <Style id="store">
       <IconStyle>
         <Icon>
           <href>http://maps.google.com/mapfiles/kml/paddle/blu-blank.png</href>
         </Icon>
       </IconStyle>
     </Style>
     <Placemark>
       <name>Downtown Store</name>
       <description>Mon-Sat 9AM-9PM, Sun 10AM-6PM</description>
       <styleUrl>#store</styleUrl>
       <Point><coordinates>-122.4194,37.7749,0</coordinates></Point>
     </Placemark>
     <Placemark>
       <name>Airport Store</name>
       <description>Daily 6AM-10PM</description>
       <styleUrl>#store</styleUrl>
       <Point><coordinates>-122.3900,37.6213,0</coordinates></Point>
     </Placemark>
   </Document>

Delivery Routes
~~~~~~~~~~~~~~~

.. kml::

   <Document>
     <name>Delivery Routes</name>
     <Style id="route1">
       <LineStyle>
         <color>ff0000ff</color>
         <width>3</width>
       </LineStyle>
     </Style>
     <Placemark>
       <name>Route A</name>
       <description>Morning deliveries</description>
       <styleUrl>#route1</styleUrl>
       <LineString>
         <coordinates>
           -122.4194,37.7749,0
           -122.4083,37.7833,0
           -122.4000,37.7900,0
           -122.3917,37.7967,0
         </coordinates>
       </LineString>
     </Placemark>
   </Document>

Service Areas
~~~~~~~~~~~~~

.. kml::

   <Placemark>
     <name>Service Coverage</name>
     <description>Primary service area</description>
     <Style>
       <PolyStyle>
         <color>4d0000ff</color>
       </PolyStyle>
       <LineStyle>
         <color>ff0000ff</color>
         <width>2</width>
       </LineStyle>
     </Style>
     <Polygon>
       <outerBoundaryIs>
         <LinearRing>
           <coordinates>
             -122.5000,37.8000,0
             -122.3000,37.8000,0
             -122.3000,37.6000,0
             -122.5000,37.6000,0
             -122.5000,37.8000,0
           </coordinates>
         </LinearRing>
       </outerBoundaryIs>
     </Polygon>
   </Placemark>

Tourist Attractions
~~~~~~~~~~~~~~~~~~~

.. kml::

   <Document>
     <name>City Tour</name>
     <Placemark>
       <name>Museum</name>
       <description><![CDATA[
         <h3>City Museum</h3>
         <p>Open: 10AM-6PM</p>
         <p>Admission: $15</p>
       ]]></description>
       <Point><coordinates>-122.4183,37.7833,0</coordinates></Point>
     </Placemark>
     <Placemark>
       <name>Park</name>
       <description><![CDATA[
         <h3>Central Park</h3>
         <p>Open: 6AM-10PM</p>
         <p>Free admission</p>
       ]]></description>
       <Point><coordinates>-122.4500,37.7700,0</coordinates></Point>
     </Placemark>
   </Document>

Advanced Features
-----------------

Time-based Animation
~~~~~~~~~~~~~~~~~~~~

.. kml::

   <Placemark>
     <name>Moving Object</name>
     <TimeStamp>
       <when>2024-01-01T12:00:00Z</when>
     </TimeStamp>
     <Point><coordinates>-122.4194,37.7749,0</coordinates></Point>
   </Placemark>

Camera Views
~~~~~~~~~~~~

.. kml::

   <Placemark>
     <name>Viewpoint</name>
     <LookAt>
       <longitude>-122.4194</longitude>
       <latitude>37.7749</latitude>
       <altitude>0</altitude>
       <heading>0</heading>
       <tilt>60</tilt>
       <range>5000</range>
     </LookAt>
     <Point><coordinates>-122.4194,37.7749,0</coordinates></Point>
   </Placemark>

Photo Overlays
~~~~~~~~~~~~~~

.. kml::

   <PhotoOverlay>
     <name>Photo Location</name>
     <Icon>
       <href>https://example.com/photo.jpg</href>
     </Icon>
     <ViewVolume>
       <leftFov>-60</leftFov>
       <rightFov>60</rightFov>
       <bottomFov>-45</bottomFov>
       <topFov>45</topFov>
       <near>10</near>
     </ViewVolume>
     <Point><coordinates>-122.4194,37.7749,10</coordinates></Point>
   </PhotoOverlay>

Integration with Maps
---------------------

Google Earth
~~~~~~~~~~~~

.. kml-file:: locations.kml
   :viewer: google-earth
   :download: true
   
   Interactive visualization in Google Earth

Google Maps
~~~~~~~~~~~

.. kml-file:: routes.kml
   :viewer: google-maps
   :embed: true
   :height: 500px

Inline Rendering
~~~~~~~~~~~~~~~~

.. kml::
   :render: inline
   :width: 800px
   :height: 600px

   <Placemark>
     <name>Location</name>
     <Point><coordinates>-122.4194,37.7749,0</coordinates></Point>
   </Placemark>

Export Options
--------------

Download Links
~~~~~~~~~~~~~~

.. kml-download:: my-places.kml
   
   Download KML file for offline use

Multiple Formats
~~~~~~~~~~~~~~~~

.. kml-export::
   :formats: kml, kmz, geojson
   :source: locations.kml

API Integration
---------------

Dynamic KML
~~~~~~~~~~~

.. code-block:: python

   # Generate KML from data
   from sphinx_kml import KMLGenerator
   
   gen = KMLGenerator()
   for location in get_locations():
       gen.add_placemark(
           name=location.name,
           coords=(location.lon, location.lat),
           description=location.desc
       )
   
   kml_content = gen.to_kml()


Practical Examples
------------------

Basic KML Elements
------------------

Simple Placemark
~~~~~~~~~~~~~~~~

.. kml::

   <?xml version="1.0" encoding="UTF-8"?>
   <kml xmlns="http://www.opengis.net/kml/2.2">
     <Placemark>
       <name>Golden Gate Bridge</name>
       <Point>
         <coordinates>-122.4783,37.8199,0</coordinates>
       </Point>
     </Placemark>
   </kml>

With Description
~~~~~~~~~~~~~~~~

.. kml::

   <Placemark>
     <name>Eiffel Tower</name>
     <description>Famous iron lattice tower in Paris</description>
     <Point>
       <coordinates>2.2945,48.8584,324</coordinates>
     </Point>
   </Placemark>

Multiple Placemarks
~~~~~~~~~~~~~~~~~~~

.. kml::

   <Folder>
     <name>World Landmarks</name>
     <Placemark>
       <name>Statue of Liberty</name>
       <Point>
         <coordinates>-74.0445,40.6892,0</coordinates>
       </Point>
     </Placemark>
     <Placemark>
       <name>Big Ben</name>
       <Point>
         <coordinates>-0.1246,51.5007,0</coordinates>
       </Point>
     </Placemark>
   </Folder>

Styled Elements
---------------

Custom Icon
~~~~~~~~~~~

.. kml::

   <Placemark>
     <name>Custom Marker</name>
     <Style>
       <IconStyle>
         <Icon>
           <href>http://maps.google.com/mapfiles/kml/paddle/red-circle.png</href>
         </Icon>
       </IconStyle>
     </Style>
     <Point>
       <coordinates>-122.0842,37.4224,0</coordinates>
     </Point>
   </Placemark>

Colored Line
~~~~~~~~~~~~

.. kml::

   <Placemark>
     <name>Route</name>
     <Style>
       <LineStyle>
         <color>ff0000ff</color>
         <width>4</width>
       </LineStyle>
     </Style>
     <LineString>
       <coordinates>
         -122.4194,37.7749,0
         -122.0842,37.4224,0
       </coordinates>
     </LineString>
   </Placemark>

Polygon Area
~~~~~~~~~~~~

.. kml::

   <Placemark>
     <name>Coverage Area</name>
     <Style>
       <PolyStyle>
         <color>7f00ff00</color>
       </PolyStyle>
       <LineStyle>
         <color>ff00ff00</color>
         <width>2</width>
       </LineStyle>
     </Style>
     <Polygon>
       <outerBoundaryIs>
         <LinearRing>
           <coordinates>
             -122.5,37.8,0
             -122.3,37.8,0
             -122.3,37.6,0
             -122.5,37.6,0
             -122.5,37.8,0
           </coordinates>
         </LinearRing>
       </outerBoundaryIs>
     </Polygon>
   </Placemark>

Geographic Features
-------------------

Path/Route
~~~~~~~~~~

.. kml::

   <Placemark>
     <name>Hiking Trail</name>
     <description>5 mile scenic trail</description>
     <LineString>
       <tessellate>1</tessellate>
       <coordinates>
         -112.2550,36.0800,2357
         -112.2545,36.0826,2423
         -112.2540,36.0848,2456
         -112.2530,36.0870,2498
       </coordinates>
     </LineString>
   </Placemark>

Ground Overlay
~~~~~~~~~~~~~~

.. kml::

   <GroundOverlay>
     <name>Map Overlay</name>
     <Icon>
       <href>https://example.com/map-overlay.png</href>
     </Icon>
     <LatLonBox>
       <north>37.83234</north>
       <south>37.82234</south>
       <east>-122.37567</east>
       <west>-122.38567</west>
     </LatLonBox>
   </GroundOverlay>

Network Link
~~~~~~~~~~~~

.. kml::

   <NetworkLink>
     <name>Live Data</name>
     <Link>
       <href>https://example.com/live-data.kml</href>
       <refreshMode>onInterval</refreshMode>
       <refreshInterval>300</refreshInterval>
     </Link>
   </NetworkLink>

Organization
------------

Folders
~~~~~~~

.. kml::

   <Folder>
     <name>US Cities</name>
     <Folder>
       <name>West Coast</name>
       <Placemark>
         <name>San Francisco</name>
         <Point><coordinates>-122.4194,37.7749,0</coordinates></Point>
       </Placemark>
       <Placemark>
         <name>Los Angeles</name>
         <Point><coordinates>-118.2437,34.0522,0</coordinates></Point>
       </Placemark>
     </Folder>
     <Folder>
       <name>East Coast</name>
       <Placemark>
         <name>New York</name>
         <Point><coordinates>-74.0060,40.7128,0</coordinates></Point>
       </Placemark>
     </Folder>
   </Folder>

Document Structure
~~~~~~~~~~~~~~~~~~

.. kml::

   <Document>
     <name>My Places</name>
     <description>Collection of interesting locations</description>
     <Style id="redIcon">
       <IconStyle>
         <color>ff0000ff</color>
         <scale>1.2</scale>
       </IconStyle>
     </Style>
     <Placemark>
       <name>Important Location</name>
       <styleUrl>#redIcon</styleUrl>
       <Point><coordinates>-122.0842,37.4224,0</coordinates></Point>
     </Placemark>
   </Document>

Configuration Examples
----------------------

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_kml',
   ]
   
   # KML settings
   kml_output_dir = '_kml'
   kml_viewer = 'google-earth'  # or 'google-maps'

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

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

External KML Files
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # KML file inclusion
   kml_include_path = ['_kml', 'data/kml']
   kml_download_enabled = True

Practical Examples
------------------

Store Locations
~~~~~~~~~~~~~~~

.. kml::

   <Document>
     <name>Store Locations</name>
     <Style id="store">
       <IconStyle>
         <Icon>
           <href>http://maps.google.com/mapfiles/kml/paddle/blu-blank.png</href>
         </Icon>
       </IconStyle>
     </Style>
     <Placemark>
       <name>Downtown Store</name>
       <description>Mon-Sat 9AM-9PM, Sun 10AM-6PM</description>
       <styleUrl>#store</styleUrl>
       <Point><coordinates>-122.4194,37.7749,0</coordinates></Point>
     </Placemark>
     <Placemark>
       <name>Airport Store</name>
       <description>Daily 6AM-10PM</description>
       <styleUrl>#store</styleUrl>
       <Point><coordinates>-122.3900,37.6213,0</coordinates></Point>
     </Placemark>
   </Document>

Delivery Routes
~~~~~~~~~~~~~~~

.. kml::

   <Document>
     <name>Delivery Routes</name>
     <Style id="route1">
       <LineStyle>
         <color>ff0000ff</color>
         <width>3</width>
       </LineStyle>
     </Style>
     <Placemark>
       <name>Route A</name>
       <description>Morning deliveries</description>
       <styleUrl>#route1</styleUrl>
       <LineString>
         <coordinates>
           -122.4194,37.7749,0
           -122.4083,37.7833,0
           -122.4000,37.7900,0
           -122.3917,37.7967,0
         </coordinates>
       </LineString>
     </Placemark>
   </Document>

Service Areas
~~~~~~~~~~~~~

.. kml::

   <Placemark>
     <name>Service Coverage</name>
     <description>Primary service area</description>
     <Style>
       <PolyStyle>
         <color>4d0000ff</color>
       </PolyStyle>
       <LineStyle>
         <color>ff0000ff</color>
         <width>2</width>
       </LineStyle>
     </Style>
     <Polygon>
       <outerBoundaryIs>
         <LinearRing>
           <coordinates>
             -122.5000,37.8000,0
             -122.3000,37.8000,0
             -122.3000,37.6000,0
             -122.5000,37.6000,0
             -122.5000,37.8000,0
           </coordinates>
         </LinearRing>
       </outerBoundaryIs>
     </Polygon>
   </Placemark>

Tourist Attractions
~~~~~~~~~~~~~~~~~~~

.. kml::

   <Document>
     <name>City Tour</name>
     <Placemark>
       <name>Museum</name>
       <description><![CDATA[
         <h3>City Museum</h3>
         <p>Open: 10AM-6PM</p>
         <p>Admission: $15</p>
       ]]></description>
       <Point><coordinates>-122.4183,37.7833,0</coordinates></Point>
     </Placemark>
     <Placemark>
       <name>Park</name>
       <description><![CDATA[
         <h3>Central Park</h3>
         <p>Open: 6AM-10PM</p>
         <p>Free admission</p>
       ]]></description>
       <Point><coordinates>-122.4500,37.7700,0</coordinates></Point>
     </Placemark>
   </Document>

Advanced Features
-----------------

Time-based Animation
~~~~~~~~~~~~~~~~~~~~

.. kml::

   <Placemark>
     <name>Moving Object</name>
     <TimeStamp>
       <when>2024-01-01T12:00:00Z</when>
     </TimeStamp>
     <Point><coordinates>-122.4194,37.7749,0</coordinates></Point>
   </Placemark>

Camera Views
~~~~~~~~~~~~

.. kml::

   <Placemark>
     <name>Viewpoint</name>
     <LookAt>
       <longitude>-122.4194</longitude>
       <latitude>37.7749</latitude>
       <altitude>0</altitude>
       <heading>0</heading>
       <tilt>60</tilt>
       <range>5000</range>
     </LookAt>
     <Point><coordinates>-122.4194,37.7749,0</coordinates></Point>
   </Placemark>

Photo Overlays
~~~~~~~~~~~~~~

.. kml::

   <PhotoOverlay>
     <name>Photo Location</name>
     <Icon>
       <href>https://example.com/photo.jpg</href>
     </Icon>
     <ViewVolume>
       <leftFov>-60</leftFov>
       <rightFov>60</rightFov>
       <bottomFov>-45</bottomFov>
       <topFov>45</topFov>
       <near>10</near>
     </ViewVolume>
     <Point><coordinates>-122.4194,37.7749,10</coordinates></Point>
   </PhotoOverlay>

Integration with Maps
---------------------

Google Earth
~~~~~~~~~~~~

.. kml-file:: locations.kml
   :viewer: google-earth
   :download: true
   
   Interactive visualization in Google Earth

Google Maps
~~~~~~~~~~~

.. kml-file:: routes.kml
   :viewer: google-maps
   :embed: true
   :height: 500px

Inline Rendering
~~~~~~~~~~~~~~~~

.. kml::
   :render: inline
   :width: 800px
   :height: 600px

   <Placemark>
     <name>Location</name>
     <Point><coordinates>-122.4194,37.7749,0</coordinates></Point>
   </Placemark>

Export Options
--------------

Download Links
~~~~~~~~~~~~~~

.. kml-download:: my-places.kml
   
   Download KML file for offline use

Multiple Formats
~~~~~~~~~~~~~~~~

.. kml-export::
   :formats: kml, kmz, geojson
   :source: locations.kml

API Integration
---------------

Dynamic KML
~~~~~~~~~~~

.. code-block:: python

   # Generate KML from data
   from sphinx_kml import KMLGenerator
   
   gen = KMLGenerator()
   for location in get_locations():
       gen.add_placemark(
           name=location.name,
           coords=(location.lon, location.lat),
           description=location.desc
       )
   
   kml_content = gen.to_kml()

Additional Resources
--------------------
- :doc:`sphinxcontrib-googlemaps` - Google Maps integration
- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `KML Reference <https://developers.google.com/kml/documentation/kmlreference>`_
- `Google Earth <https://earth.google.com/>`_
- :doc:`../tutorials/packages/sphinx-kml` - Complete tutorial
- KML Reference: https://developers.google.com/kml/documentation/kmlreference
- GitHub repository: https://github.com/sphinx-doc/sphinx-kml

