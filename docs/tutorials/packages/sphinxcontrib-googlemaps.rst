Sphinxcontrib-Googlemaps Tutorial
==================================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinxcontrib-googlemaps/>`_
   - :doc:`See Working Example <../../examples/sphinxcontrib-googlemaps-example>`


This tutorial demonstrates how to use sphinxcontrib-googlemaps to embed interactive Google Maps in your Sphinx documentation.

What is Sphinxcontrib-Googlemaps?
----------------------------------

sphinxcontrib-googlemaps is a Sphinx extension that provides directives for embedding Google Maps:

- Interactive map embedding
- Custom markers and locations
- Multiple map types (roadmap, satellite, terrain, hybrid)
- Zoom and center control
- Multiple markers on single map
- Custom styling and controls
- Directions and routes
- Street View integration
- Responsive map sizing

This is perfect for documentation that needs to show locations, facilities, offices, or geographic data.

Installation
------------

sphinxcontrib-googlemaps is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinxcontrib.googlemaps; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinxcontrib.googlemaps',
   ]
   
   # Google Maps API key (optional for basic usage)
   googlemaps_api_key = 'YOUR_API_KEY_HERE'

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinxcontrib.googlemaps']
   
   # API configuration
   googlemaps_api_key = 'YOUR_GOOGLE_MAPS_API_KEY'
   googlemaps_api_version = '3'
   
   # Default map settings
   googlemaps_default_zoom = 10
   googlemaps_default_maptype = 'roadmap'  # roadmap, satellite, terrain, hybrid
   googlemaps_default_width = '100%'
   googlemaps_default_height = '400px'
   
   # Map controls
   googlemaps_show_zoom_control = True
   googlemaps_show_map_type_control = True
   googlemaps_show_scale_control = True
   googlemaps_show_street_view_control = True
   
   # Styling
   googlemaps_custom_styles = []  # Custom map styles

Getting API Key
~~~~~~~~~~~~~~~

1. Go to `Google Cloud Console <https://console.cloud.google.com/>`_
2. Create a new project or select existing
3. Enable Maps JavaScript API
4. Create credentials (API Key)
5. Restrict key to your domain (recommended)

Basic Usage
-----------

Simple Map
~~~~~~~~~~

.. code-block:: rst

   .. googlemaps::
      :location: New York, NY, USA
      :zoom: 12

Map with Coordinates
~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. googlemaps::
      :lat: 40.7128
      :lng: -74.0060
      :zoom: 13
      :maptype: roadmap

Custom Size
~~~~~~~~~~~

.. code-block:: rst

   .. googlemaps::
      :location: San Francisco, CA
      :width: 800px
      :height: 600px
      :zoom: 11

Multiple Markers
~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. googlemaps::
      :markers:
         - lat: 40.7128, lng: -74.0060, title: New York Office
         - lat: 34.0522, lng: -118.2437, title: Los Angeles Office
         - lat: 41.8781, lng: -87.6298, title: Chicago Office
      :zoom: 4

Practical Examples
------------------

Example 1: Company Locations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/contact/offices.rst``:

.. code-block:: rst

   Our Offices
   ===========
   
   We have offices in major cities across the United States.
   
   Headquarters - San Francisco
   -----------------------------
   
   .. googlemaps::
      :location: 123 Market St, San Francisco, CA 94103
      :zoom: 15
      :maptype: roadmap
      :width: 100%
      :height: 400px
   
   **Address:**
   123 Market Street
   San Francisco, CA 94103
   
   **Phone:** (415) 555-0123
   
   **Hours:** Mon-Fri 9am-5pm PST
   
   East Coast Office - New York
   -----------------------------
   
   .. googlemaps::
      :location: 350 Fifth Avenue, New York, NY 10118
      :zoom: 16
      :maptype: roadmap
   
   **Address:**
   350 Fifth Avenue
   New York, NY 10118
   
   **Phone:** (212) 555-0456
   
   All Locations
   -------------
   
   .. googlemaps::
      :markers:
         - lat: 37.7749, lng: -122.4194, title: San Francisco HQ
         - lat: 40.7484, lng: -73.9857, title: New York Office
         - lat: 34.0522, lng: -118.2437, title: Los Angeles Office
         - lat: 41.8781, lng: -87.6298, title: Chicago Office
         - lat: 47.6062, lng: -122.3321, title: Seattle Office
      :zoom: 4
      :width: 100%
      :height: 500px

Example 2: Event Venue
~~~~~~~~~~~~~~~~~~~~~~

``docs/events/conference.rst``:

.. code-block:: rst

   Annual Conference 2026
   ======================
   
   Join us for our annual conference in Austin, Texas!
   
   Venue Location
   --------------
   
   .. googlemaps::
      :location: Austin Convention Center, Austin, TX
      :zoom: 17
      :maptype: hybrid
      :width: 100%
      :height: 450px
   
   **Venue:** Austin Convention Center
   
   **Address:**
   500 E Cesar Chavez St
   Austin, TX 78701
   
   **Dates:** March 15-17, 2026
   
   Getting There
   -------------
   
   From Airport
   ~~~~~~~~~~~~
   
   .. googlemaps::
      :markers:
         - lat: 30.1975, lng: -97.6664, title: Austin Airport
         - lat: 30.2638, lng: -97.7364, title: Convention Center
      :zoom: 11
   
   - **Distance:** 7 miles
   - **Uber/Lyft:** ~$20-30
   - **Rental Car:** Available at airport
   
   Nearby Hotels
   ~~~~~~~~~~~~~
   
   .. googlemaps::
      :markers:
         - lat: 30.2638, lng: -97.7364, title: Convention Center, color: red
         - lat: 30.2672, lng: -97.7431, title: Hotel A
         - lat: 30.2651, lng: -97.7401, title: Hotel B
         - lat: 30.2701, lng: -97.7382, title: Hotel C
      :zoom: 15

Example 3: Facility Tour
~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/facilities/datacenter.rst``:

.. code-block:: rst

   Data Center Locations
   =====================
   
   Our global data center infrastructure.
   
   North America
   -------------
   
   US-East (Virginia)
   ~~~~~~~~~~~~~~~~~~
   
   .. googlemaps::
      :location: Ashburn, VA, USA
      :zoom: 12
      :maptype: satellite
   
   - **Region:** us-east-1
   - **Availability Zones:** 6
   - **Opened:** 2010
   
   US-West (Oregon)
   ~~~~~~~~~~~~~~~~
   
   .. googlemaps::
      :location: Portland, OR, USA
      :zoom: 12
      :maptype: satellite
   
   - **Region:** us-west-2
   - **Availability Zones:** 4
   - **Opened:** 2012
   
   Europe
   ------
   
   EU-West (Ireland)
   ~~~~~~~~~~~~~~~~~
   
   .. googlemaps::
      :location: Dublin, Ireland
      :zoom: 10
      :maptype: roadmap
   
   - **Region:** eu-west-1
   - **Availability Zones:** 3
   - **Opened:** 2013
   
   Global Network
   --------------
   
   .. googlemaps::
      :markers:
         - lat: 39.0438, lng: -77.4874, title: US-East (Virginia)
         - lat: 45.5152, lng: -122.6784, title: US-West (Oregon)
         - lat: 53.3498, lng: -6.2603, title: EU-West (Ireland)
         - lat: 35.6762, lng: 139.6503, title: AP-Northeast (Tokyo)
         - lat: -33.8688, lng: 151.2093, title: AP-Southeast (Sydney)
      :zoom: 2
      :width: 100%
      :height: 500px

Advanced Features
-----------------

Custom Markers
~~~~~~~~~~~~~~

.. code-block:: rst

   .. googlemaps::
      :markers:
         - lat: 40.7128, lng: -74.0060, title: Headquarters, color: red, label: HQ
         - lat: 34.0522, lng: -118.2437, title: Branch Office, color: blue, label: LA

Map Types
~~~~~~~~~

.. code-block:: rst

   Roadmap View
   
   .. googlemaps::
      :location: Grand Canyon, AZ
      :maptype: roadmap
      :zoom: 10
   
   Satellite View
   
   .. googlemaps::
      :location: Grand Canyon, AZ
      :maptype: satellite
      :zoom: 10
   
   Terrain View
   
   .. googlemaps::
      :location: Grand Canyon, AZ
      :maptype: terrain
      :zoom: 10
   
   Hybrid View
   
   .. googlemaps::
      :location: Grand Canyon, AZ
      :maptype: hybrid
      :zoom: 10

Info Windows
~~~~~~~~~~~~

.. code-block:: rst

   .. googlemaps::
      :markers:
         - lat: 37.7749, lng: -122.4194
           title: San Francisco Office
           info: |
             123 Market Street<br>
             San Francisco, CA 94103<br>
             <a href="tel:+14155550123">(415) 555-0123</a>

Directions
~~~~~~~~~~

.. code-block:: rst

   .. googlemaps-directions::
      :origin: New York, NY
      :destination: Boston, MA
      :mode: driving

Custom Styling
~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   googlemaps_custom_styles = [
       {
           "featureType": "water",
           "elementType": "geometry",
           "stylers": [{"color": "#193341"}]
       },
       {
           "featureType": "landscape",
           "elementType": "geometry",
           "stylers": [{"color": "#2c5a71"}]
       }
   ]

Street View
~~~~~~~~~~~

.. code-block:: rst

   .. googlemaps-streetview::
      :location: Times Square, New York, NY
      :heading: 90
      :pitch: 0

Docker Integration
------------------

Build with Maps
~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     -e GOOGLE_MAPS_API_KEY="your-key-here" \
     kensai-sphinx:latest \
     sphinx-build -b html /project/docs /project/docs/_build/html

Environment Variables
~~~~~~~~~~~~~~~~~~~~~

``docker-compose.yml``:

.. code-block:: yaml

   version: '3.8'
   
   services:
     docs:
       image: kensai-sphinx:latest
       volumes:
         - ./:/project
       environment:
         - GOOGLE_MAPS_API_KEY=${GOOGLE_MAPS_API_KEY}
       command: sphinx-build -b html /project/docs /project/docs/_build/html

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Build Docs with Maps
   
   on: [push]
   
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Build Documentation
           env:
             GOOGLE_MAPS_API_KEY: ${{ secrets.GOOGLE_MAPS_API_KEY }}
           run: |
             docker run --rm \
               -v $(pwd):/project \
               -e GOOGLE_MAPS_API_KEY \
               kensai-sphinx:latest \
               sphinx-build -b html /project/docs /project/docs/_build/html

Best Practices
--------------

1. **Protect Your API Key**
   
   Use environment variables:
   
   .. code-block:: python
   
      import os
      googlemaps_api_key = os.getenv('GOOGLE_MAPS_API_KEY')

2. **Restrict API Key**
   
   In Google Cloud Console, restrict by:
   
   - HTTP referrers
   - IP addresses
   - APIs (only Maps JavaScript API)

3. **Use Appropriate Zoom**
   
   - City: 10-12
   - Street: 15-17
   - Building: 18-20

4. **Provide Fallback**
   
   Include text address for accessibility

5. **Optimize Loading**
   
   Don't embed too many maps on one page

6. **Test Responsive**
   
   Use percentage widths for mobile

Common Patterns
---------------

Location Page Template
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   {{ Location Name }}
   ===================
   
   Map
   ---
   
   .. googlemaps::
      :location: {{ address }}
      :zoom: 15
      :width: 100%
      :height: 400px
   
   Address
   -------
   
   {{ full_address }}
   
   Contact
   -------
   
   - **Phone:** {{ phone }}
   - **Email:** {{ email }}

Troubleshooting
---------------

Map Not Displaying
~~~~~~~~~~~~~~~~~~

**Solution:**

1. Check API key is set:

   .. code-block:: python
   
      googlemaps_api_key = 'YOUR_KEY'

2. Verify API is enabled in Google Cloud Console

3. Check browser console for errors

API Key Errors
~~~~~~~~~~~~~~

**Solution:**

- Ensure Maps JavaScript API is enabled
- Check API key restrictions
- Verify billing is enabled

Markers Not Showing
~~~~~~~~~~~~~~~~~~~

**Solution:**

Check coordinate format:

.. code-block:: rst

   # Correct
   :markers:
      - lat: 40.7128, lng: -74.0060

Invalid Location
~~~~~~~~~~~~~~~~

**Solution:**

Use coordinates instead of address:

.. code-block:: rst

   .. googlemaps::
      :lat: 40.7128
      :lng: -74.0060

Next Steps
----------

1. Get Google Maps API key
2. Add maps to location-based documentation
3. Create office/facility location pages
4. Add event venue maps
5. Document geographic data

Additional Resources
--------------------

- :doc:`sphinx-kml` - KML file integration
- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `Google Maps JavaScript API <https://developers.google.com/maps/documentation/javascript>`_
- `Google Maps Platform <https://cloud.google.com/maps-platform>`_
