Sphinx-Charts Example
=====================

This page demonstrates the interactive Plotly charts that can be created using the **sphinx-charts** extension.

.. note::
   The sphinx-charts extension uses Plotly for interactive visualizations. Charts are defined using JSON files that contain Plotly chart specifications.

Monthly Sales Bar Chart
------------------------

An interactive bar chart showing monthly sales figures:

.. chart:: examples/_charts/sales-bar.json
   :width: 700
   :height: 400

   {}

Temperature Trends
------------------

A line chart displaying temperature changes over time:

.. chart:: examples/_charts/temperature-line.json
   :width: 700
   :height: 400

   {}

Market Share Analysis
---------------------

A pie chart (with donut hole) showing market share distribution:

.. chart:: examples/_charts/market-pie.json
   :width: 600
   :height: 400

   {}

Key Features
------------

These Plotly charts demonstrate:

- **Interactive**: Hover over data points to see values, zoom, pan, and more
- **Responsive**: Charts adapt to different screen sizes
- **Customizable**: Full control over colors, labels, and styling using Plotly configuration
- **Professional**: Publication-ready visualizations
- **Easy to Embed**: Simple reStructuredText syntax with JSON data files

Chart Data Format
-----------------

Charts are defined using JSON files with Plotly specifications. Here's an example:

.. code-block:: json

   {
     "data": [{
       "type": "bar",
       "x": ["Jan", "Feb", "Mar"],
       "y": [65, 78, 90],
       "marker": {"color": "rgba(54, 162, 235, 0.8)"}
     }],
     "layout": {
       "title": "Monthly Sales",
       "xaxis": {"title": "Month"},
       "yaxis": {"title": "Revenue ($K)"}
     }
   }

Learn More
----------

For detailed information on creating your own charts, see:

- :doc:`../tutorials/packages/sphinx-charts` - Complete tutorial
- `Plotly Documentation <https://plotly.com/javascript/>`_ - Plotly chart reference
- `sphinx-charts GitHub <https://github.com/thclark/sphinx-charts>`_ - Extension repository
