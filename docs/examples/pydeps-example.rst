Pydeps - Working Example
=========================

.. note::
   :doc:`See Working Example <../tutorials/packages/pydeps>`


Installation
------------

Install pydeps with pip:

.. code-block:: bash

   pip install pydeps

With all optional dependencies:

.. code-block:: bash

   pip install pydeps[all]

GraphViz is required for rendering:

.. code-block:: bash

   # Ubuntu/Debian
   sudo apt-get install graphviz
   
   # macOS
   brew install graphviz
   
   # Windows (using Chocolatey)
   choco install graphviz

Verify installation:

.. code-block:: bash

   pydeps --version

Basic Usage
-----------

Command-Line Interface
~~~~~~~~~~~~~~~~~~~~~~

Generate basic dependency graph:

.. code-block:: bash

   pydeps mypackage

Save to file:

.. code-block:: bash

   pydeps mypackage --output mypackage.png

Generate SVG output:

.. code-block:: bash

   pydeps mypackage --format svg --output deps.svg

Show only internal dependencies:

.. code-block:: bash

   pydeps mypackage --no-externals

Python API
~~~~~~~~~~

Basic usage:

.. code-block:: python

   from pydeps.pydeps import pydeps
   
   pydeps('mypackage', output='deps.png')

Advanced usage:

.. code-block:: python

   from pydeps.pydeps import pydeps
   
   pydeps(
       'mypackage',
       output='detailed.svg',
       format='svg',
       show_deps=True,
       max_bacon=2,
       no_externals=False
   )

Simple Examples
---------------

Basic Package Analysis
~~~~~~~~~~~~~~~~~~~~~~

Example project structure:

.. code-block:: text

   myproject/
   ├── __init__.py
   ├── core.py
   ├── utils.py
   ├── models.py
   └── api.py

File contents:

.. code-block:: python

   # core.py
   from .utils import helper_function
   from .models import DataModel
   
   def process_data(data):
       model = DataModel(data)
       return helper_function(model)
   
   # utils.py
   def helper_function(obj):
       return str(obj)
   
   # models.py
   class DataModel:
       def __init__(self, data):
           self.data = data
   
   # api.py
   from .core import process_data
   
   def handle_request(data):
       return process_data(data)

Generate dependency graph:

.. code-block:: bash

   pydeps myproject --output myproject_deps.png

**Expected output structure:**

.. code-block:: text

   api ──> core ──> models
             │
             └──> utils

Filtering Dependencies
~~~~~~~~~~~~~~~~~~~~~~

Show only specific modules:

.. code-block:: bash

   pydeps mypackage --only "core,api,models"

Exclude test modules:

.. code-block:: bash

   pydeps mypackage --exclude "*test*,*mock*"

Maximum depth:

.. code-block:: bash

   pydeps mypackage --max-bacon 2

Advanced Features
-----------------

Circular Dependency Detection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Detect and visualize circular dependencies:

.. code-block:: bash

   pydeps mypackage --show-cycles

Example with circular dependency:

.. code-block:: python

   # module_a.py
   from . import module_b
   
   def function_a():
       module_b.function_b()
   
   # module_b.py
   from . import module_a
   
   def function_b():
       module_a.function_a()

Pydeps output will highlight the cycle:

.. code-block:: bash

   pydeps mypackage --show-cycles --output cycles.png

**Circular dependencies shown in red**

Cluster by Package
~~~~~~~~~~~~~~~~~~

Group related modules:

.. code-block:: bash

   pydeps mypackage --cluster

Example with sub-packages:

.. code-block:: text

   myproject/
   ├── api/
   │   ├── __init__.py
   │   ├── handlers.py
   │   └── validators.py
   ├── core/
   │   ├── __init__.py
   │   ├── engine.py
   │   └── processor.py
   └── models/
       ├── __init__.py
       └── data.py

Generate clustered graph:

.. code-block:: bash

   pydeps myproject --cluster --output clustered.svg

External Dependencies
~~~~~~~~~~~~~~~~~~~~~

Show external package dependencies:

.. code-block:: bash

   pydeps mypackage --show-externals

Include specific external packages:

.. code-block:: bash

   pydeps mypackage --externals "numpy,pandas,requests"

Color external dependencies:

.. code-block:: bash

   pydeps mypackage --externals --external-style "filled,color=lightblue"

Reverse Dependencies
~~~~~~~~~~~~~~~~~~~~

Show what depends on a module:

.. code-block:: bash

   pydeps mypackage --reverse

Focus on specific module:

.. code-block:: bash

   pydeps mypackage --reverse --only "core"

Practical Examples
------------------

Large Project Analysis
~~~~~~~~~~~~~~~~~~~~~~

Analyze large project with filtering:

.. code-block:: python

   # analyze_project.py
   from pydeps.pydeps import pydeps
   import os
   
   def analyze_large_project(package_name, output_dir='dependency_graphs'):
       """Analyze large project with multiple views."""
       os.makedirs(output_dir, exist_ok=True)
       
       # Overview - high level only
       pydeps(
           package_name,
           output=f'{output_dir}/overview.svg',
           format='svg',
           max_bacon=1,
           no_externals=True
       )
       
       # Detailed internal
       pydeps(
           package_name,
           output=f'{output_dir}/detailed.svg',
           format='svg',
           no_externals=True,
           cluster=True
       )
       
       # External dependencies
       pydeps(
           package_name,
           output=f'{output_dir}/external.svg',
           format='svg',
           only_externals=True
       )
       
       # Circular dependencies
       pydeps(
           package_name,
           output=f'{output_dir}/cycles.svg',
           format='svg',
           show_cycles=True
       )
   
   if __name__ == '__main__':
       analyze_large_project('mypackage')

Django Project Analysis
~~~~~~~~~~~~~~~~~~~~~~~

Analyze Django application:

.. code-block:: bash

   # Exclude migrations and tests
   pydeps myapp \
     --exclude "*migrations*,*tests*" \
     --cluster \
     --output django_deps.svg

Example Django structure:

.. code-block:: python

   # myapp/views.py
   from .models import MyModel
   from .forms import MyForm
   from .utils import helper
   
   # myapp/models.py
   from django.db import models
   
   # myapp/forms.py
   from .models import MyModel
   
   # myapp/utils.py
   # Utility functions

Generate focused view:

.. code-block:: bash

   pydeps myapp \
     --no-externals \
     --exclude "*admin*,*migrations*,*tests*" \
     --output myapp_structure.png

Flask API Dependencies
~~~~~~~~~~~~~~~~~~~~~~

Analyze Flask application:

.. code-block:: python

   # api/
   # ├── __init__.py
   # ├── routes/
   # │   ├── users.py
   # │   └── auth.py
   # ├── services/
   # │   ├── user_service.py
   # │   └── auth_service.py
   # └── models/
   #     └── user.py

Generate API dependency map:

.. code-block:: bash

   pydeps api \
     --cluster \
     --rankdir LR \
     --output api_deps.svg

Data Science Project
~~~~~~~~~~~~~~~~~~~~

Analyze data science pipeline:

.. code-block:: python

   # ml_project/
   # ├── data/
   # │   ├── loaders.py
   # │   └── preprocessors.py
   # ├── features/
   # │   ├── engineering.py
   # │   └── selection.py
   # ├── models/
   # │   ├── train.py
   # │   └── evaluate.py
   # └── utils/
   #     └── helpers.py

Visualize pipeline:

.. code-block:: bash

   pydeps ml_project \
     --cluster \
     --max-bacon 3 \
     --output ml_pipeline.svg

Customization
-------------

Custom Styling
~~~~~~~~~~~~~~

Use GraphViz attributes:

.. code-block:: bash

   pydeps mypackage \
     --rankdir LR \
     --node-shape box \
     --node-color lightblue \
     --edge-color gray \
     --output styled.svg

Create configuration file `.pydeps`:

.. code-block:: ini

   # .pydeps
   [pydeps]
   max_bacon = 2
   no_externals = True
   cluster = True
   rankdir = TB
   
   [graphviz]
   node_shape = box
   node_color = lightblue
   edge_color = gray
   concentrate = True

Use configuration:

.. code-block:: bash

   pydeps mypackage --config .pydeps

Custom Filters
~~~~~~~~~~~~~~

Advanced filtering with Python API:

.. code-block:: python

   from pydeps.pydeps import pydeps
   from pydeps.target import Target
   
   def custom_filter(package, output):
       """Generate graph with custom filtering."""
       
       # Create target
       target = Target(package)
       
       # Custom exclusions
       excludes = ['*test*', '*mock*', '*migrations*']
       
       pydeps(
           package,
           output=output,
           exclude=','.join(excludes),
           no_externals=True,
           max_bacon=2
       )
   
   custom_filter('mypackage', 'custom.svg')

Report Generation
-----------------

HTML Report
~~~~~~~~~~~

Generate comprehensive HTML report:

.. code-block:: python

   # generate_report.py
   from pydeps.pydeps import pydeps
   import json
   import os
   
   def generate_dependency_report(package, output_dir='report'):
       """Generate comprehensive dependency report."""
       os.makedirs(output_dir, exist_ok=True)
       
       # Generate various visualizations
       views = {
           'overview': {'max_bacon': 1, 'no_externals': True},
           'detailed': {'no_externals': True, 'cluster': True},
           'external': {'only_externals': True},
           'cycles': {'show_cycles': True}
       }
       
       for name, options in views.items():
           pydeps(
               package,
               output=f'{output_dir}/{name}.svg',
               format='svg',
               **options
           )
       
       # Generate HTML report
       html = f"""
       <html>
       <head>
           <title>Dependency Report: {package}</title>
           <style>
               body {{ font-family: Arial, sans-serif; margin: 20px; }}
               .section {{ margin: 30px 0; }}
               img {{ max-width: 100%; border: 1px solid #ccc; }}
           </style>
       </head>
       <body>
           <h1>Dependency Report: {package}</h1>
           
           <div class="section">
               <h2>Overview</h2>
               <img src="overview.svg" alt="Overview">
           </div>
           
           <div class="section">
               <h2>Detailed Structure</h2>
               <img src="detailed.svg" alt="Detailed">
           </div>
           
           <div class="section">
               <h2>External Dependencies</h2>
               <img src="external.svg" alt="External">
           </div>
           
           <div class="section">
               <h2>Circular Dependencies</h2>
               <img src="cycles.svg" alt="Cycles">
           </div>
       </body>
       </html>
       """
       
       with open(f'{output_dir}/index.html', 'w') as f:
           f.write(html)
       
       print(f"Report generated in {output_dir}/index.html")
   
   if __name__ == '__main__':
       generate_dependency_report('mypackage')

JSON Export
~~~~~~~~~~~

Export dependency data:

.. code-block:: python

   # export_deps.py
   from pydeps.pydeps import py2depgraph
   import json
   
   def export_dependencies_json(package, output='deps.json'):
       """Export dependencies as JSON."""
       
       # Generate dependency graph
       graph = py2depgraph(package)
       
       # Extract data
       dependencies = {}
       for node in graph.nodes():
           deps = list(graph.successors(node))
           dependencies[node] = deps
       
       # Save to JSON
       with open(output, 'w') as f:
           json.dump(dependencies, f, indent=2)
       
       print(f"Dependencies exported to {output}")
   
   if __name__ == '__main__':
       export_dependencies_json('mypackage')

Integration
-----------

CI/CD Integration
~~~~~~~~~~~~~~~~~

GitHub Actions workflow:

.. code-block:: yaml

   # .github/workflows/dependencies.yml
   name: Dependency Graph
   
   on:
     push:
       branches: [main]
   
   jobs:
     dependencies:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v2
         
         - name: Set up Python
           uses: actions/setup-python@v2
           with:
             python-version: 3.9
         
         - name: Install dependencies
           run: |
             sudo apt-get install -y graphviz
             pip install pydeps
         
         - name: Generate dependency graphs
           run: |
             mkdir -p docs/dependencies
             pydeps mypackage --output docs/dependencies/overview.svg
             pydeps mypackage --show-cycles --output docs/dependencies/cycles.svg
         
         - name: Commit graphs
           run: |
             git config user.name "GitHub Actions"
             git config user.email "actions@github.com"
             git add docs/dependencies/
             git commit -m "Update dependency graphs" || echo "No changes"
             git push

Pre-commit Hook
~~~~~~~~~~~~~~~

Check for circular dependencies:

.. code-block:: bash

   #!/bin/bash
   # .git/hooks/pre-commit
   
   echo "Checking for circular dependencies..."
   pydeps mypackage --show-cycles --no-output
   
   if [ $? -ne 0 ]; then
       echo "ERROR: Circular dependencies detected!"
       exit 1
   fi

Sphinx Documentation
~~~~~~~~~~~~~~~~~~~~

Auto-generate in Sphinx:

.. code-block:: python

   # docs/conf.py
   import os
   from pydeps.pydeps import pydeps
   
   def generate_dependency_graphs(app):
       """Generate dependency graphs during build."""
       static_dir = os.path.join(app.srcdir, '_static', 'dependencies')
       os.makedirs(static_dir, exist_ok=True)
       
       pydeps(
           '../mypackage',
           output=os.path.join(static_dir, 'overview.svg'),
           format='svg',
           no_externals=True
       )
   
   def setup(app):
       app.connect('builder-inited', generate_dependency_graphs)

Best Practices
--------------

1. **Regular Analysis**

   .. code-block:: bash

      # Add to development workflow
      make deps:
          pydeps mypackage --output latest_deps.svg
          open latest_deps.svg

2. **Track Changes**

   .. code-block:: bash

      # Version control dependency graphs
      git add docs/dependencies/*.svg
      git commit -m "Update dependency graphs"

3. **Focus Views**

   .. code-block:: bash

      # Create different views for different purposes
      pydeps mypackage --max-bacon 1 --output high_level.svg
      pydeps mypackage --only "core,api" --output core_api.svg

4. **Document Architecture**

   .. code-block:: rst

      Architecture
      ============
      
      .. image:: _static/dependencies/overview.svg
         :alt: Dependency Overview

5. **Detect Issues Early**

   .. code-block:: python

      # CI check for circular dependencies
      import sys
      from pydeps.pydeps import pydeps
      
      result = pydeps('mypackage', show_cycles=True, no_output=True)
      if result has_cycles:
          sys.exit(1)

Troubleshooting
---------------

Common Issues
~~~~~~~~~~~~~

**Issue: GraphViz not found**

.. code-block:: bash

   # Install GraphViz
   sudo apt-get install graphviz  # Ubuntu
   brew install graphviz          # macOS

**Issue: Import errors**

.. code-block:: bash

   # Add package to PYTHONPATH
   export PYTHONPATH="${PYTHONPATH}:$(pwd)"
   pydeps mypackage

**Issue: Too complex graph**

.. code-block:: bash

   # Simplify with filtering
   pydeps mypackage --max-bacon 2 --no-externals

**Issue: Missing dependencies**

.. code-block:: bash

   # Ensure package is installed
   pip install -e .
   pydeps mypackage

See Also
--------

- **pyprojectviz-example.rst** - Alternative dependency visualization
- **pylint-example.rst** - Code analysis with pyreverse
- **graphviz-example.rst** - Graph visualization backend
- **sphinx-autodoc-annotation-example.rst** - API documentation

External Resources:

- Pydeps GitHub: https://github.com/thebjorn/pydeps
- GraphViz Documentation: https://graphviz.org/
- Dependency Management Best Practices: https://example.com/python-deps

Summary
-------

Pydeps is a powerful tool for Python dependency visualization:

- **Clear Visualizations**: Beautiful dependency graphs
- **Circular Detection**: Identifies dependency cycles
- **Flexible Filtering**: Show exactly what you need
- **Multiple Formats**: PNG, SVG, PDF output
- **Clustering**: Group related modules
- **External Dependencies**: Track third-party packages
- **Reverse Dependencies**: See what depends on what
- **CI/CD Integration**: Automate dependency tracking
- **Large Project Support**: Handles complex codebases
- **Open Source**: Free and well-maintained

Regular use of pydeps helps maintain clean architecture, prevent circular dependencies, and understand project structure as codebases evolve.
