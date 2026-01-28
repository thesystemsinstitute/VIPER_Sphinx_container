Sphinxcontrib-Googlemaps Example
================================

This page demonstrates the **sphinxcontrib-googlemaps** extension for embedding Google Maps in Sphinx documentation.

.. contents:: Contents
   :local:
   :depth: 2

Overview
--------

The sphinxcontrib-googlemaps extension allows embedding interactive Google Maps with markers, routes, and custom styling directly in documentation.

Basic Maps
----------

Simple Map
~~~~~~~~~~

.. googlemap::
   :center: 37.7749, -122.4194
   :zoom: 12
   
   Basic map centered on San Francisco

With Marker
~~~~~~~~~~~

.. googlemap::
   :center: 40.7128, -74.0060
   :zoom: 13
   :marker: 40.7128, -74.0060, "New York City"
   
   Map with a single marker

Multiple Markers
~~~~~~~~~~~~~~~~

.. googlemap::
   :center: 51.5074, -0.1278
   :zoom: 10
   
   :marker: 51.5074, -0.1278, "London"
   :marker: 51.5194, -0.1270, "King's Cross"
   :marker: 51.5007, -0.1246, "Tower Bridge"

Custom Markers
--------------

With Info Windows
~~~~~~~~~~~~~~~~~

.. googlemap::
   :center: 48.8566, 2.3522
   :zoom: 12
   
   :marker: 48.8584, 2.2945, "Eiffel Tower", "icon:eiffel.png"
   :marker: 48.8606, 2.3376, "Louvre Museum", "icon:museum.png"
   :info: "Click markers for details"

Colored Markers
~~~~~~~~~~~~~~~

.. googlemap::
   :center: 35.6762, 139.6503
   :zoom: 11
   
   :marker: 35.6762, 139.6503, "Tokyo", "color:red"
   :marker: 35.6595, 139.7004, "Tokyo Skytree", "color:blue"
   :marker: 35.6586, 139.7454, "Tokyo Disneyland", "color:green"

Routes and Paths
----------------

Simple Route
~~~~~~~~~~~~

.. googlemap::
   :center: 37.7749, -122.4194
   :zoom: 13
   :route: 37.7849, -122.4094 to 37.7649, -122.4294
   
   Route between two points

Multiple Waypoints
~~~~~~~~~~~~~~~~~~

.. googlemap::
   :center: 34.0522, -118.2437
   :zoom: 12
   
   :route: 34.0522, -118.2437 via 34.0689, -118.4452 to 34.0195, -118.4912
   :mode: driving

Transit Directions
~~~~~~~~~~~~~~~~~~

.. googlemap::
   :center: 40.7589, -73.9851
   :zoom: 13
   
   :route: 40.7589, -73.9851 to 40.7614, -73.9776
   :mode: transit
   :transit-mode: subway

Map Styling
-----------

Custom Theme
~~~~~~~~~~~~

.. googlemap::
   :center: 41.9028, 12.4964
   :zoom: 12
   :style: dark
   
   Dark-themed map of Rome

Minimal UI
~~~~~~~~~~

.. googlemap::
   :center: 55.7558, 37.6173
   :zoom: 11
   :controls: zoom
   :ui: minimal
   
   Minimal interface map

Full Screen
~~~~~~~~~~~

.. googlemap::
   :center: -33.8688, 151.2093
   :zoom: 12
   :fullscreen: true
   :height: 600px
   
   Full-screen capable map of Sydney

Interactive Features
--------------------

Click Events
~~~~~~~~~~~~

.. googlemap::
   :center: 52.5200, 13.4050
   :zoom: 12
   :onclick: addMarker
   
   Click to add markers (Berlin)

Search Box
~~~~~~~~~~

.. googlemap::
   :center: 19.4326, -99.1332
   :zoom: 11
   :searchbox: true
   
   Map with search functionality (Mexico City)

Geolocation
~~~~~~~~~~~

.. googlemap::
   :zoom: 12
   :geolocation: true
   
   Map centered on user's location

Overlays
--------

Polygons
~~~~~~~~

.. googlemap::
   :center: 25.7617, -80.1918
   :zoom: 11
   
   :polygon: 25.7800, -80.2200; 25.7900, -80.1900; 25.7700, -80.1800
   :polygon-color: #FF0000
   :polygon-opacity: 0.35
   
   Polygon overlay on Miami

Circles
~~~~~~~

.. googlemap::
   :center: 37.3861, -122.0839
   :zoom: 12
   
   :circle: 37.3861, -122.0839, 5000
   :circle-color: #0000FF
   :circle-opacity: 0.2
   
   5km radius circle (Mountain View)

Rectangles
~~~~~~~~~~

.. googlemap::
   :center: 47.6062, -122.3321
   :zoom: 11
   
   :rectangle: 47.6500, -122.4000, 47.5500, -122.2500
   :rectangle-color: #00FF00
   
   Rectangle overlay (Seattle)

Map Types
---------

Satellite View
~~~~~~~~~~~~~~

.. googlemap::
   :center: 36.2048, -112.4280
   :zoom: 14
   :maptype: satellite
   
   Satellite view of Grand Canyon

Terrain View
~~~~~~~~~~~~

.. googlemap::
   :center: 46.8182, 8.2275
   :zoom: 10
   :maptype: terrain
   
   Terrain view of Swiss Alps

Hybrid View
~~~~~~~~~~~

.. googlemap::
   :center: 64.2008, -149.4937
   :zoom: 12
   :maptype: hybrid
   
   Hybrid view of Denali

Configuration Examples
----------------------

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinxcontrib.googlemaps',
   ]
   
   # Google Maps API key
   googlemaps_api_key = 'YOUR_API_KEY_HERE'

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Map defaults
   googlemaps_defaults = {
       'zoom': 13,
       'maptype': 'roadmap',
       'language': 'en',
       'region': 'US',
   }
   
   # API settings
   googlemaps_version = '3.exp'
   googlemaps_libraries = ['places', 'geometry']

Custom Styling
~~~~~~~~~~~~~~

.. code-block:: python

   # Custom map styles
   googlemaps_styles = {
       'dark': [
           {'elementType': 'geometry', 'stylers': [{'color': '#242f3e'}]},
           {'elementType': 'labels.text.stroke', 'stylers': [{'color': '#242f3e'}]},
           {'elementType': 'labels.text.fill', 'stylers': [{'color': '#746855'}]},
       ],
       'light': [
           {'elementType': 'geometry', 'stylers': [{'color': '#f5f5f5'}]},
           {'elementType': 'labels', 'stylers': [{'visibility': 'on'}]},
       ],
   }

Practical Examples
------------------

Office Locations
~~~~~~~~~~~~~~~~

.. googlemap::
   :center: 37.4224, -122.0842
   :zoom: 4
   :height: 500px
   
   :marker: 37.7749, -122.4194, "San Francisco Office", "icon:office.png"
   :marker: 40.7128, -74.0060, "New York Office", "icon:office.png"
   :marker: 41.8781, -87.6298, "Chicago Office", "icon:office.png"
   :marker: 34.0522, -118.2437, "Los Angeles Office", "icon:office.png"
   
   Company office locations across the United States

Event Venue
~~~~~~~~~~~

.. googlemap::
   :center: 37.8044, -122.2712
   :zoom: 15
   :marker: 37.8044, -122.2712, "Conference Center"
   
   :polygon: 37.8050, -122.2720; 37.8050, -122.2700; 37.8040, -122.2700; 37.8040, -122.2720
   :polygon-color: #FF0000
   :polygon-opacity: 0.25
   
   Event venue with parking area highlighted

Delivery Zone
~~~~~~~~~~~~~

.. googlemap::
   :center: 40.7589, -73.9851
   :zoom: 13
   
   :marker: 40.7589, -73.9851, "Restaurant"
   :circle: 40.7589, -73.9851, 3000
   :circle-color: #00AA00
   :circle-opacity: 0.2
   
   3km delivery radius from restaurant

Tourist Guide
~~~~~~~~~~~~~

.. googlemap::
   :center: 48.8566, 2.3522
   :zoom: 13
   :searchbox: true
   
   :marker: 48.8584, 2.2945, "Eiffel Tower"
   :marker: 48.8606, 2.3376, "Louvre"
   :marker: 48.8530, 2.3499, "Notre-Dame"
   :marker: 48.8738, 2.2950, "Arc de Triomphe"
   
   :route: 48.8584, 2.2945 via 48.8738, 2.2950 via 48.8606, 2.3376 to 48.8530, 2.3499
   :mode: walking
   
   Walking tour of Paris landmarks

Store Locator
~~~~~~~~~~~~~

.. googlemap::
   :center: 34.0522, -118.2437
   :zoom: 10
   :geolocation: true
   :searchbox: true
   
   :marker: 34.0522, -118.2437, "Downtown Store"
   :marker: 34.0689, -118.4452, "Santa Monica Store"
   :marker: 34.1478, -118.1445, "Pasadena Store"
   
   Find stores near you

Integration Examples
--------------------

With Location Data
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Restaurant Locations
   ====================
   
   .. googlemap::
      :center: 40.7128, -74.0060
      :zoom: 12
      
      :marker: 40.7489, -73.9680, "Midtown Location"
      :marker: 40.7282, -74.0776, "Chelsea Location"
      :marker: 40.7061, -74.0087, "Financial District"
   
   Each location offers full menu and delivery services.

With Directions
~~~~~~~~~~~~~~~

.. code-block:: rst

   Getting to Our Office
   =====================
   
   .. googlemap::
      :center: 37.7749, -122.4194
      :zoom: 14
      :marker: 37.7749, -122.4194, "Our Office"
   
   **By Public Transit:**
   
   .. googlemap::
      :center: 37.7749, -122.4194
      :zoom: 13
      :route: BART Powell Station to 37.7749, -122.4194
      :mode: transit

With Custom Data
~~~~~~~~~~~~~~~~

.. code-block:: rst

   Property Locations
   ==================
   
   .. googlemap::
      :center: 33.4484, -112.0740
      :zoom: 12
      
      :marker: 33.4484, -112.0740, "Property A - $500,000"
      :marker: 33.5076, -112.0740, "Property B - $650,000"
      :marker: 33.4255, -112.0740, "Property C - $450,000"

Advanced Features
-----------------

Clustering
~~~~~~~~~~

.. googlemap::
   :center: 37.0902, -95.7129
   :zoom: 4
   :cluster: true
   
   :marker: 37.7749, -122.4194, "San Francisco"
   :marker: 34.0522, -118.2437, "Los Angeles"
   :marker: 40.7128, -74.0060, "New York"
   :marker: 41.8781, -87.6298, "Chicago"
   :marker: 29.7604, -95.3698, "Houston"
   
   Markers automatically cluster at lower zoom levels

Heatmap
~~~~~~~

.. googlemap::
   :center: 37.7749, -122.4194
   :zoom: 12
   :heatmap: 37.7849, -122.4294; 37.7749, -122.4194; 37.7649, -122.4094
   :heatmap-radius: 20
   
   Heatmap visualization of data points

Street View
~~~~~~~~~~~

.. googlemap::
   :center: 37.8692, -122.2581
   :zoom: 14
   :streetview: 37.8692, -122.2581
   :streetview-heading: 90
   
   Map with Street View integration

See Also
--------

- :doc:`../tutorials/packages/sphinxcontrib-googlemaps` - Complete tutorial
- Google Maps JavaScript API: https://developers.google.com/maps/documentation/javascript
- GitHub repository: https://github.com/sphinx-contrib/googlemaps
