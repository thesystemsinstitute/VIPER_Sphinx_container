Sphinx-KML Example
==================

This page demonstrates the **sphinx-kml** extension for embedding KML (Keyhole Markup Language) geographic data and visualizations in Sphinx documentation.

.. contents:: Contents
   :local:
   :depth: 2


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

See Also
--------

- :doc:`../tutorials/packages/sphinx-kml` - Complete tutorial
- KML Reference: https://developers.google.com/kml/documentation/kmlreference
- GitHub repository: https://github.com/sphinx-doc/sphinx-kml
