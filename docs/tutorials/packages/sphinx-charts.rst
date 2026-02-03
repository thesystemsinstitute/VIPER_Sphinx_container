Sphinx-Charts Tutorial
======================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-charts/>`_
   - `API Documentation <../../pdoc/sphinx_charts/index.html>`_
   - `Manual <https://sphinx-charts.readthedocs.io/>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinx-charts to create interactive Plotly visualizations in your Sphinx documentation.

What is Sphinx-Charts?
-----------------------

sphinx-charts is a Sphinx extension that allows you to embed interactive Plotly charts directly in your documentation. It provides:

- Interactive Plotly visualizations
- Multiple chart types (line, bar, pie, scatter, etc.)
- Zoom, pan, and hover interactions
- Export capabilities
- JSON-based chart definitions

Installation
------------

sphinx-charts is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm viper-sphinx:latest pip show sphinx-charts

Configuration
-------------

Add sphinx-charts to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_charts.charts',
       # ... other extensions
   ]

Basic Usage
-----------

Chart File Structure
~~~~~~~~~~~~~~~~~~~~

Charts are defined using JSON files containing Plotly specifications. Create a JSON file with your chart data:

**File: `_charts/my-chart.json`**

.. code-block:: json

   {
     "data": [{
       "type": "bar",
       "x": ["January", "February", "March", "April", "May", "June"],
       "y": [65, 78, 90, 81, 95, 110],
       "marker": {
         "color": "rgba(54, 162, 235, 0.8)"
       },
       "name": "Revenue ($K)"
     }],
     "layout": {
       "title": "Monthly Sales - 2026",
       "xaxis": {"title": "Month"},
       "yaxis": {"title": "Revenue ($K)"},
       "showlegend": false
     }
   }

Embedding Charts
~~~~~~~~~~~~~~~~

Reference the JSON file in your RST document:

.. code-block:: rst

   .. chart:: _charts/my-chart.json
      :width: 700
      :height: 400

      {}

.. note::
   The empty ``{}`` content block is required by the directive, even though the chart data is in the JSON file.

Line Chart Example
~~~~~~~~~~~~~~~~~~

**File: `_charts/temperature.json`**

.. code-block:: json

   {
     "data": [{
       "type": "scatter",
       "mode": "lines+markers",
       "x": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
       "y": [32, 35, 38, 36, 33, 30, 28],
       "line": {
         "color": "rgba(255, 99, 132, 1)",
         "width": 2
       },
       "marker": {
         "size": 8,
         "color": "rgba(255, 99, 132, 1)"
       },
       "fill": "tozeroy",
       "fillcolor": "rgba(255, 99, 132, 0.1)",
       "name": "Temperature (°F)"
     }],
     "layout": {
       "title": "Daily Temperature",
       "xaxis": {"title": "Day"},
       "yaxis": {"title": "Temperature (°F)"}
     }
   }

**Usage in RST:**

.. code-block:: rst

   .. chart:: _charts/temperature.json
      :width: 700
      :height: 400

      {}

Pie Chart Example
~~~~~~~~~~~~~~~~~

**File: `_charts/market-share.json`**

.. code-block:: json

   {
     "data": [{
       "type": "pie",
       "labels": ["Chrome", "Safari", "Firefox", "Edge", "Other"],
       "values": [62.8, 20.3, 8.5, 5.2, 3.2],
       "marker": {
         "colors": [
           "rgba(66, 133, 244, 0.8)",
           "rgba(52, 168, 83, 0.8)",
           "rgba(251, 188, 5, 0.8)",
           "rgba(234, 67, 53, 0.8)",
           "rgba(158, 158, 158, 0.8)"
         ]
       },
       "hole": 0.4
     }],
     "layout": {
       "title": "Browser Market Share 2026"
     }
   }

**Usage in RST:**

.. code-block:: rst

   .. chart:: _charts/market-share.json
      :width: 600
      :height: 400

      {}

Advanced Features
-----------------

Multiple Datasets
~~~~~~~~~~~~~~~~~

**File: `_charts/multi-series.json`**

.. code-block:: json

   {
     "data": [
       {
         "type": "scatter",
         "mode": "lines",
         "name": "Product A",
         "x": ["Q1", "Q2", "Q3", "Q4"],
         "y": [65, 70, 80, 85],
         "line": {"color": "rgb(255, 99, 132)"}
       },
       {
         "type": "scatter",
         "mode": "lines",
         "name": "Product B",
         "x": ["Q1", "Q2", "Q3", "Q4"],
         "y": [45, 55, 60, 70],
         "line": {"color": "rgb(54, 162, 235)"}
       }
     ],
     "layout": {
       "title": "Product Comparison",
       "xaxis": {"title": "Quarter"},
       "yaxis": {"title": "Sales"}
     }
   }

Stacked Bar Chart
~~~~~~~~~~~~~~~~~

**File: `_charts/stacked-bar.json`**

.. code-block:: json

   {
     "data": [
       {
         "type": "bar",
         "name": "Online Sales",
         "x": ["Jan", "Feb", "Mar", "Apr"],
         "y": [12, 19, 15, 17],
         "marker": {"color": "rgba(255, 99, 132, 0.7)"}
       },
       {
         "type": "bar",
         "name": "In-Store Sales",
         "x": ["Jan", "Feb", "Mar", "Apr"],
         "y": [8, 11, 13, 9],
         "marker": {"color": "rgba(54, 162, 235, 0.7)"}
       }
     ],
     "layout": {
       "title": "Stacked Revenue",
       "barmode": "stack",
       "xaxis": {"title": "Month"},
       "yaxis": {"title": "Sales ($K)"}
     }
   }

3D Scatter Plot
~~~~~~~~~~~~~~~

**File: `_charts/3d-scatter.json`**

.. code-block:: json

   {
     "data": [{
       "type": "scatter3d",
       "mode": "markers",
       "x": [1, 2, 3, 4, 5],
       "y": [1, 4, 9, 16, 25],
       "z": [1, 8, 27, 64, 125],
       "marker": {
         "size": 12,
         "color": [1, 2, 3, 4, 5],
         "colorscale": "Viridis"
       }
     }],
     "layout": {
       "title": "3D Data Visualization",
       "scene": {
         "xaxis": {"title": "X"},
         "yaxis": {"title": "Y"},
         "zaxis": {"title": "Z"}
       }
     }
   }

Configuration Options
---------------------

Chart Directive Options
~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 20 60

   * - Option
     - Type
     - Description
   * - *argument*
     - path
     - Path to JSON file (relative to docs directory)
   * - :width
     - integer
     - Chart width in pixels
   * - :height
     - integer
     - Chart height in pixels
   * - :download_name
     - string
     - Name for downloaded chart file

Plotly JSON Structure
~~~~~~~~~~~~~~~~~~~~~

The JSON file must contain:

.. code-block:: json

   {
     "data": [
       {
         "type": "chart_type",
         // Chart-specific properties
       }
     ],
     "layout": {
       "title": "Chart Title",
       // Layout configuration
     }
   }

**Common Chart Types:**

- ``bar`` - Bar charts
- ``scatter`` - Line/scatter plots (use ``mode: "lines"``)
- ``pie`` - Pie charts
- ``scatter3d`` - 3D scatter plots
- ``heatmap`` - Heatmaps
- ``box`` - Box plots
- ``violin`` - Violin plots

**Layout Options:**

.. code-block:: json

   {
     "layout": {
       "title": "Chart Title",
       "xaxis": {
         "title": "X Axis Label",
         "gridcolor": "#E5E5E5"
       },
       "yaxis": {
         "title": "Y Axis Label",
         "gridcolor": "#E5E5E5"
       },
       "showlegend": true,
       "legend": {
         "x": 1,
         "y": 1
       },
       "hovermode": "closest"
     }
   }

Best Practices
--------------

1. **Organize Chart Files**: Keep all chart JSON files in a dedicated directory (e.g., `_charts/`)
2. **Keep it Simple**: Don't overcrowd charts with too much data
3. **Use Meaningful Colors**: Choose colors that make sense for your data
4. **Add Context**: Use titles and axis labels to explain what the chart shows
5. **Responsive Design**: Set appropriate width/height for readability
6. **Accessibility**: Provide text descriptions alongside charts
7. **Consistent Style**: Use the same color scheme across your documentation
8. **Version Control**: JSON files are easy to track in Git

Common Chart Types
------------------

Line Charts
~~~~~~~~~~~
- **Use for**: Time series data, trends over time
- **Best when**: Showing continuous data, comparing multiple series
- **Plotly type**: ``scatter`` with ``mode: "lines"``

Bar Charts
~~~~~~~~~~
- **Use for**: Comparing discrete categories
- **Best when**: Values are significantly different, need easy comparison

Bar Charts
~~~~~~~~~~
- **Use for**: Comparing discrete categories
- **Best when**: Showing rankings, comparisons across groups
- **Plotly type**: ``bar``

Pie/Doughnut Charts
~~~~~~~~~~~~~~~~~~~
- **Use for**: Showing proportions of a whole
- **Best when**: You have 5-7 categories maximum
- **Plotly type**: ``pie`` (use ``hole`` property for doughnut)

Scatter Plots
~~~~~~~~~~~~~
- **Use for**: Showing correlations between two variables
- **Best when**: Displaying relationships, identifying outliers
- **Plotly type**: ``scatter``

3D Charts
~~~~~~~~~
- **Use for**: Visualizing multi-dimensional data
- **Best when**: Showing spatial relationships
- **Plotly type**: ``scatter3d``, ``surface``, ``mesh3d``

Troubleshooting
---------------

Charts Not Displaying
~~~~~~~~~~~~~~~~~~~~~

If charts don't appear:

1. Check that ``sphinx_charts.charts`` is in ``extensions`` list in conf.py
2. Verify JSON file path is correct (relative to docs directory)
3. Ensure JSON data is valid (use a JSON validator)
4. Check the empty content block ``{}`` is present
5. Verify the JSON file exists at the specified location
6. Clear Sphinx build cache: ``sphinx-build -E -a``

Invalid JSON
~~~~~~~~~~~~

Common JSON mistakes:

.. code-block:: json

   // Wrong - single quotes
   {"label": 'Data'}
   
   // Wrong - trailing comma
   {"label": "Data",}
   
   // Wrong - comments (not allowed in JSON)
   {
     "label": "Data"  // This is a comment
   }
   
   // Correct
   {"label": "Data"}

File Path Issues
~~~~~~~~~~~~~~~~

If you get "file not found" errors:

- Chart JSON files must be relative to the docs directory
- If your RST file is at ``docs/examples/page.rst`` and chart is at ``docs/examples/_charts/chart.json``, use ``examples/_charts/chart.json``
- Paths are case-sensitive on Linux containers
- Don't include leading slashes


Practical Examples
------------------

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

Additional Resources
--------------------

- `Plotly JavaScript Documentation <https://plotly.com/javascript/>`_ - Complete Plotly reference
- `Sphinx-Charts GitHub <https://github.com/thclark/sphinx-charts>`_ - Extension repository
- :doc:`../sphinx-basics` - Learn more about Sphinx
- :doc:`../extensions` - Other useful extensions

Next Steps
----------

Try creating your own charts in your documentation:

1. Create a ``_charts`` directory in your docs folder
2. Add JSON files with your chart data in Plotly format
3. Reference them using the ``.. chart::`` directive
4. Experiment with different chart types and configurations

Start with simple bar or line charts, then explore more advanced visualizations like 3D plots and heatmaps!

