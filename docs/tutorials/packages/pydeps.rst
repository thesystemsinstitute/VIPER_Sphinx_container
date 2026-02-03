Pydeps Tutorial
===============

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/pydeps/>`_
   - `API Documentation <../../pdoc/pydeps/index.html>`_
   - `Manual <https://github.com/thebjorn/pydeps>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use pydeps to generate Python dependency graphs for Sphinx documentation.

What is Pydeps?
---------------
Pydeps is a Python dependency visualization tool that provides:

- Package dependency graphs
- Module-level dependencies
- Import relationship visualization
- Circular dependency detection
- External package tracking
- Grouping by package
- Cluster visualization
- SVG/PNG/PDF output
- Filtering options
- Custom styling
- Dependency analysis
- Integration with documentation

This enables automatic dependency documentation.

Pydeps is a Python module dependency visualization tool that creates dependency graphs showing the relationships between modules in your Python project. It generates beautiful, informative diagrams that help developers understand project structure, identify circular dependencies, and plan refactoring efforts.

Key features include:

- Module dependency graph generation
- Circular dependency detection
- Multiple output formats (PNG, SVG, PDF)
- Customizable filtering and clustering
- External dependency visualization
- Reverse dependency tracking
- Interactive exploration
- Integration with GraphViz
- Large project support
- Command-line and Python API


Installation
------------

pydeps is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm viper-sphinx:latest pydeps --version

Configuration
-------------

Basic Sphinx Integration
~~~~~~~~~~~~~~~~~~~~~~~~~

Add to ``docs/conf.py``:

.. code-block:: python

   import subprocess
   from pathlib import Path
   
   
   def generate_dependency_graphs(app, config):
       """Generate dependency visualizations."""
       project_root = Path(app.srcdir).parent
       source_dir = project_root / 'src'
       output_dir = Path(app.srcdir) / '_static' / 'dependencies'
       
       output_dir.mkdir(parents=True, exist_ok=True)
       
       # Generate overall dependency graph
       subprocess.run([
           'pydeps',
           str(source_dir),
           '--max-bacon', '2',
           '-o', str(output_dir / 'dependencies.svg'),
       ])
       
       # Generate per-package graphs
       for package in source_dir.iterdir():
           if package.is_dir() and not package.name.startswith('_'):
               subprocess.run([
                   'pydeps',
                   str(package),
                   '-o', str(output_dir / f'{package.name}_deps.svg'),
               ])
   
   
   def setup(app):
       app.connect('config-inited', generate_dependency_graphs)

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

``pydeps_config.py``:

.. code-block:: python

   """Advanced pydeps configuration."""
   
   from pathlib import Path
   import subprocess
   
   
   class DependencyAnalyzer:
       """Analyze and visualize dependencies."""
       
       def __init__(self, output_dir='docs/_static/dependencies'):
           self.output_dir = Path(output_dir)
           self.output_dir.mkdir(parents=True, exist_ok=True)
       
       def generate_graph(self, package, name, **options):
           """Generate dependency graph with options."""
           args = ['pydeps', str(package)]
           
           # Clustering options
           if options.get('cluster'):
               args.append('--cluster')
           
           if options.get('max_bacon'):
               args.extend(['--max-bacon', str(options['max_bacon'])])
           
           # Filtering
           if 'exclude' in options:
               for pattern in options['exclude']:
                   args.extend(['--exclude', pattern])
           
           if 'only' in options:
               for pattern in options['only']:
                   args.extend(['--only', pattern])
           
           # Display options
           if options.get('no_show'):
               args.append('--no-show')
           
           if options.get('show_deps'):
               args.append('--show-deps')
           
           if options.get('show_raw_deps'):
               args.append('--show-raw-deps')
           
           # External dependencies
           if options.get('externals'):
               args.append('--externals')
           
           # Output
           args.extend(['-o', str(self.output_dir / name)])
           
           subprocess.run(args)
       
       def detect_cycles(self, package):
           """Detect circular dependencies."""
           result = subprocess.run(
               ['pydeps', str(package), '--show-cycles'],
               capture_output=True,
               text=True,
           )
           
           return result.stdout

Custom Styling
~~~~~~~~~~~~~~

.. code-block:: python

   def style_dependency_graph():
       """Apply custom styling to generated graph."""
       from graphviz import Source
       
       # Read DOT file
       dot_file = 'dependencies.dot'
       
       with open(dot_file) as f:
           content = f.read()
       
       # Modify styling
       styled = content.replace(
           'graph {',
           '''graph {
           rankdir=LR;
           node [shape=box, style=filled, fillcolor="#dbeafe"];
           edge [color="#2563eb"];
           ''',
       )
       
       # Render
       source = Source(styled)
       source.render('dependencies_styled', format='svg')

Basic Usage
-----------

Generate Dependency Graph
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Single package
   pydeps mypackage -o deps.svg
   
   # With clustering
   pydeps mypackage --cluster -o deps.svg
   
   # Show external dependencies
   pydeps mypackage --externals -o deps.svg

Filter Dependencies
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Exclude patterns
   pydeps mypackage --exclude '*test*' -o deps.svg
   
   # Only specific modules
   pydeps mypackage --only 'mypackage.core.*' -o deps.svg

   Project Dependencies
   ====================
   
   Project Overview
   ----------------
   
   Complete dependency structure:
   
   .. figure:: _static/dependencies/project_overview.svg
      :align: center
      :width: 100%
      
      Project dependency graph
   
   Internal Dependencies
   ---------------------
   
   Relationships between project modules:
   
   .. figure:: _static/dependencies/internal_deps.svg
      :align: center
      :width: 100%
      
      Internal module dependencies
   
   External Dependencies
   ---------------------
   
   Third-party package dependencies:
   
   .. figure:: _static/dependencies/external_deps.svg
      :align: center
      :width: 90%
      
      External package dependencies

Example 2: Circular Dependency Detection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``detect_cycles.py``:

.. code-block:: python

   """Detect and document circular dependencies."""
   
   import subprocess
   from pathlib import Path
   
   
   def detect_circular_dependencies():
       """Find and visualize circular dependencies."""
       output_dir = Path('docs/_static/dependencies/cycles')
       output_dir.mkdir(parents=True, exist_ok=True)
       
       # Run pydeps with cycle detection
       result = subprocess.run(
           ['pydeps', 'src', '--show-cycles'],
           capture_output=True,
           text=True,
       )
       
       # Save cycle report
       cycle_report = output_dir / 'cycles.txt'
       cycle_report.write_text(result.stdout)
       
       # Generate cycle visualization
       subprocess.run([
           'pydeps',
           'src',
           '--show-cycles',
           '--cluster',
           '-o', str(output_dir / 'cycles.svg'),
       ])
       
       # Parse and document cycles
       if 'cycles' in result.stdout.lower():
           generate_cycle_documentation(result.stdout, output_dir)
       else:
           print("✓ No circular dependencies detected")
   
   
   def generate_cycle_documentation(cycle_output, output_dir):
       """Create documentation for detected cycles."""
       doc_file = output_dir.parent.parent / 'circular_dependencies.rst'
       
       with open(doc_file, 'w') as f:
           f.write("Circular Dependencies\n")
           f.write("=" * 50 + "\n\n")
           f.write(".. warning::\n\n")
           f.write("   Circular dependencies detected!\n\n")
           f.write("Detected Cycles\n")
           f.write("-" * 20 + "\n\n")
           f.write(".. code-block:: text\n\n")
           for line in cycle_output.split('\n'):
               f.write(f"   {line}\n")
           f.write("\n")
           f.write(".. figure:: _static/dependencies/cycles/cycles.svg\n")
           f.write("   :align: center\n")
           f.write("   :width: 100%\n\n")
           f.write("   Circular dependency visualization\n")

Example 3: Package Evolution Tracking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``track_dependencies.py``:

.. code-block:: python

   """Track dependency changes over time."""
   
   import subprocess
   from pathlib import Path
   import json
   from datetime import datetime
   
   
   def track_dependency_evolution():
       """Record dependency graph over time."""
       output_dir = Path('docs/_static/dependencies/history')
       output_dir.mkdir(parents=True, exist_ok=True)
       
       timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
       
       # Generate current dependency graph
       current_file = output_dir / f'deps_{timestamp}.svg'
       subprocess.run([
           'pydeps',
           'src',
           '--cluster',
           '-o', str(current_file),
       ])
       
       # Extract dependency list
       result = subprocess.run(
           ['pydeps', 'src', '--show-deps'],
           capture_output=True,
           text=True,
       )
       
       # Save metadata
       metadata_file = output_dir / f'deps_{timestamp}.json'
       metadata = {
           'timestamp': timestamp,
           'dependencies': parse_dependencies(result.stdout),
       }
       
       with open(metadata_file, 'w') as f:
           json.dump(metadata, f, indent=2)
       
       # Compare with previous
       compare_with_previous(output_dir, metadata)
   
   
   def parse_dependencies(deps_output):
       """Extract dependency list from output."""
       deps = []
       for line in deps_output.split('\n'):
           if '->' in line:
               parts = line.split('->')
               if len(parts) == 2:
                   deps.append({
                       'from': parts[0].strip(),
                       'to': parts[1].strip(),
                   })
       return deps
   
   
   def compare_with_previous(output_dir, current_metadata):
       """Compare current deps with previous snapshot."""
       metadata_files = sorted(output_dir.glob('deps_*.json'))
       
       if len(metadata_files) > 1:
           # Load previous
           with open(metadata_files[-2]) as f:
               previous = json.load(f)
           
           current_deps = set(
               (d['from'], d['to'])
               for d in current_metadata['dependencies']
           )
           previous_deps = set(
               (d['from'], d['to'])
               for d in previous['dependencies']
           )
           
           added = current_deps - previous_deps
           removed = previous_deps - current_deps
           
           if added or removed:
               generate_change_report(output_dir, added, removed)
   
   
   def generate_change_report(output_dir, added, removed):
       """Create dependency change report."""
       report_file = output_dir.parent.parent / 'dependency_changes.rst'
       
       with open(report_file, 'w') as f:
           f.write("Dependency Changes\n")
           f.write("=" * 50 + "\n\n")
           
           if added:
               f.write("Added Dependencies\n")
               f.write("-" * 20 + "\n\n")
               for from_mod, to_mod in added:
                   f.write(f"- {from_mod} → {to_mod}\n")
               f.write("\n")
           
           if removed:
               f.write("Removed Dependencies\n")
               f.write("-" * 20 + "\n\n")
               for from_mod, to_mod in removed:
                   f.write(f"- {from_mod} → {to_mod}\n")

Example 4: Multi-Package Workspace
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``workspace_dependencies.py``:

.. code-block:: python

   """Analyze dependencies in multi-package workspace."""
   
   import subprocess
   from pathlib import Path
   
   
   def analyze_workspace_dependencies():
       """Generate dependency graphs for workspace packages."""
       workspace_root = Path('.')
       output_dir = Path('docs/_static/dependencies/workspace')
       output_dir.mkdir(parents=True, exist_ok=True)
       
       # Find all packages (directories with __init__.py)
       packages = []
       for item in workspace_root.iterdir():
           if item.is_dir() and (item / '__init__.py').exists():
               packages.append(item)
       
       # Generate per-package graphs
       for package in packages:
           package_name = package.name
           
           # Package internal structure
           subprocess.run([
               'pydeps',
               str(package),
               '--cluster',
               '--no-externals',
               '-o', str(output_dir / f'{package_name}_internal.svg'),
           ])
           
           # Package external dependencies
           subprocess.run([
               'pydeps',
               str(package),
               '--only-external',
               '-o', str(output_dir / f'{package_name}_external.svg'),
           ])
       
       # Generate workspace overview
       subprocess.run([
           'pydeps',
           *[str(p) for p in packages],
           '--cluster',
           '-o', str(output_dir / 'workspace_overview.svg'),
       ])
       
       generate_workspace_docs(output_dir, packages)
   
   
   def generate_workspace_docs(output_dir, packages):
       """Create workspace dependency documentation."""
       doc_file = output_dir.parent.parent / 'workspace_dependencies.rst'
       
       with open(doc_file, 'w') as f:
           f.write("Workspace Dependencies\n")
           f.write("=" * 50 + "\n\n")
           
           f.write("Workspace Overview\n")
           f.write("-" * 20 + "\n\n")
           f.write(".. figure:: _static/dependencies/workspace/workspace_overview.svg\n")
           f.write("   :align: center\n")
           f.write("   :width: 100%\n\n")
           
           for package in packages:
               name = package.name
               f.write(f"{name} Package\n")
               f.write("~" * (len(name) + 8) + "\n\n")
               
               f.write("Internal Structure:\n\n")
               f.write(f".. figure:: _static/dependencies/workspace/{name}_internal.svg\n")
               f.write("   :align: center\n")
               f.write("   :width: 100%\n\n")
               
               f.write("External Dependencies:\n\n")
               f.write(f".. figure:: _static/dependencies/workspace/{name}_external.svg\n")
               f.write("   :align: center\n")
               f.write("   :width: 90%\n\n")

Example 5: Dependency Complexity Analysis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``complexity_analysis.py``:

.. code-block:: python

   """Analyze dependency complexity metrics."""
   
   import subprocess
   from pathlib import Path
   import json
   
   
   def analyze_dependency_complexity():
       """Calculate dependency complexity metrics."""
       output_dir = Path('docs/_static/dependencies/complexity')
       output_dir.mkdir(parents=True, exist_ok=True)
       
       # Get raw dependency data
       result = subprocess.run(
           ['pydeps', 'src', '--show-deps'],
           capture_output=True,
           text=True,
       )
       
       # Parse dependencies
       deps = parse_dependency_data(result.stdout)
       
       # Calculate metrics
       metrics = calculate_metrics(deps)
       
       # Save metrics
       metrics_file = output_dir / 'metrics.json'
       with open(metrics_file, 'w') as f:
           json.dump(metrics, f, indent=2)
       
       # Generate visualization with metrics
       generate_complexity_visualization(output_dir, metrics)
   
   
   def parse_dependency_data(output):
       """Parse dependency relationships."""
       deps = {}
       for line in output.split('\n'):
           if '->' in line:
               parts = line.split('->')
               if len(parts) == 2:
                   from_mod = parts[0].strip()
                   to_mod = parts[1].strip()
                   
                   if from_mod not in deps:
                       deps[from_mod] = []
                   deps[from_mod].append(to_mod)
       
       return deps
   
   
   def calculate_metrics(deps):
       """Calculate complexity metrics."""
       # Afferent coupling (Ca): number of modules that depend on this module
       # Efferent coupling (Ce): number of modules this module depends on
       
       ca = {}  # Afferent coupling
       ce = {}  # Efferent coupling
       
       all_modules = set(deps.keys())
       for targets in deps.values():
           all_modules.update(targets)
       
       for module in all_modules:
           ca[module] = 0
           ce[module] = 0
       
       for from_mod, to_mods in deps.items():
           ce[from_mod] = len(to_mods)
           for to_mod in to_mods:
               ca[to_mod] += 1
       
       # Calculate instability: I = Ce / (Ca + Ce)
       instability = {}
       for module in all_modules:
           total = ca[module] + ce[module]
           instability[module] = ce[module] / total if total > 0 else 0
       
       return {
           'afferent_coupling': ca,
           'efferent_coupling': ce,
           'instability': instability,
           'most_depended_on': max(ca.items(), key=lambda x: x[1]),
           'most_dependencies': max(ce.items(), key=lambda x: x[1]),
       }
   
   
   def generate_complexity_visualization(output_dir, metrics):
       """Create complexity documentation."""
       doc_file = output_dir.parent.parent / 'dependency_complexity.rst'
       
       with open(doc_file, 'w') as f:
           f.write("Dependency Complexity Analysis\n")
           f.write("=" * 50 + "\n\n")
           
           f.write("Key Metrics\n")
           f.write("-" * 20 + "\n\n")
           
           f.write(f"Most Depended On: {metrics['most_depended_on'][0]} ")
           f.write(f"({metrics['most_depended_on'][1]} dependents)\n\n")
           
           f.write(f"Most Dependencies: {metrics['most_dependencies'][0]} ")
           f.write(f"({metrics['most_dependencies'][1]} dependencies)\n\n")

Example 6: Dependency Version Tracking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``version_tracking.py``:

.. code-block:: python

   """Track external dependency versions."""
   
   import subprocess
   from pathlib import Path
   import json
   
   
   def track_external_versions():
       """Document external dependency versions."""
       output_dir = Path('docs/_static/dependencies/versions')
       output_dir.mkdir(parents=True, exist_ok=True)
       
       # Get package versions
       result = subprocess.run(
           ['pip', 'list', '--format=json'],
           capture_output=True,
           text=True,
       )
       
       installed = json.loads(result.stdout)
       
       # Get project dependencies
       deps_result = subprocess.run(
           ['pydeps', 'src', '--only-external', '--show-deps'],
           capture_output=True,
           text=True,
       )
       
       # Match versions
       external_deps = extract_external_deps(deps_result.stdout)
       versioned_deps = match_versions(external_deps, installed)
       
       # Generate documentation
       generate_version_docs(output_dir, versioned_deps)
   
   
   def extract_external_deps(output):
       """Extract external dependency names."""
       deps = set()
       for line in output.split('\n'):
           if '->' in line:
               parts = line.split('->')
               for part in parts:
                   module = part.strip().split('.')[0]
                   if not module.startswith('src'):
                       deps.add(module)
       return deps
   
   
   def match_versions(deps, installed):
       """Match dependencies with installed versions."""
       version_map = {pkg['name']: pkg['version'] for pkg in installed}
       
       return {
           dep: version_map.get(dep, 'unknown')
           for dep in deps
       }
   
   
   def generate_version_docs(output_dir, versioned_deps):
       """Create version documentation."""
       doc_file = output_dir.parent.parent / 'external_versions.rst'
       
       with open(doc_file, 'w') as f:
           f.write("External Dependency Versions\n")
           f.write("=" * 50 + "\n\n")
           
           for dep, version in sorted(versioned_deps.items()):
               f.write(f"- {dep}: {version}\n")

Advanced Features
-----------------

Bacon Number Filtering
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Limit dependency depth
   pydeps mypackage --max-bacon 2 -o deps.svg

Cluster Visualization
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Group related modules
   pydeps mypackage --cluster -o deps.svg

Show Raw Dependencies
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Include all import statements
   pydeps mypackage --show-raw-deps -o deps.svg

Docker Integration
------------------

Generate Graphs
~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     viper-sphinx:latest \
     pydeps /project/src --cluster -o /project/docs/_static/deps.svg

Batch Generation
~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     viper-sphinx:latest \
     bash -c "
       mkdir -p /project/docs/_static/dependencies
       for pkg in /project/src/*/; do
         name=\$(basename \$pkg)
         pydeps \$pkg -o /project/docs/_static/dependencies/\${name}.svg
       done
     "

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Dependency Graphs
   
   on:
     push:
       paths:
         - 'src/**/*.py'
   
   jobs:
     dependencies:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Generate dependency graphs
           run: |
             docker run --rm -v $(pwd):/project \
               viper-sphinx:latest \
               bash -c "
                 mkdir -p /project/docs/_static/dependencies
                 pydeps /project/src --cluster \
                   -o /project/docs/_static/dependencies/deps.svg
               "
         
         - name: Check for cycles
           run: |
             docker run --rm -v $(pwd):/project \
               viper-sphinx:latest \
               pydeps /project/src --show-cycles || true
         
         - name: Commit graphs
           run: |
             git config user.name github-actions
             git config user.email github-actions@github.com
             git add docs/_static/dependencies/
             git commit -m 'Update dependency graphs' || true
             git push

Cycle Detection in CI
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

   - name: Fail on cycles
     run: |
       docker run --rm -v $(pwd):/project \
         viper-sphinx:latest \
         bash -c "
           pydeps /project/src --show-cycles > cycles.txt
           if grep -q 'cycle' cycles.txt; then
             echo 'Circular dependencies detected!'
             cat cycles.txt
             exit 1
           fi
         "

Best Practices
--------------

1. **Regular Updates**
   
   Regenerate on code changes

2. **Multiple Views**
   
   Create overview and detailed graphs

3. **Detect Cycles**
   
   Check for circular dependencies

4. **Filter Appropriately**
   
   Exclude irrelevant dependencies

5. **Document Changes**
   
   Track dependency evolution

6. **Use Clustering**
   
   Group related modules

Troubleshooting
---------------

No Output Generated
~~~~~~~~~~~~~~~~~~~

**Solution:**

Ensure package is importable:

.. code-block:: bash

   python -c "import mypackage"
   pydeps mypackage -o deps.svg

Too Complex Graph
~~~~~~~~~~~~~~~~~

**Solution:**

Reduce bacon number:

.. code-block:: bash

   pydeps mypackage --max-bacon 1 -o deps.svg

Missing Dependencies
~~~~~~~~~~~~~~~~~~~~

**Solution:**

Show raw imports:

.. code-block:: bash

   pydeps mypackage --show-raw-deps -o deps.svg

Import Errors
~~~~~~~~~~~~~

**Solution:**

Use --no-import:

.. code-block:: bash

   pydeps mypackage --no-import -o deps.svg

Next Steps
----------

1. Install pydeps
2. Generate initial graphs
3. Configure filtering
4. Add to documentation
5. Track dependency evolution


Practical Examples
------------------

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

Additional Resources
--------------------
- :doc:`pydot` - Programmatic graph generation
- :doc:`graphviz` - DOT language visualization
- `Pydeps Documentation <https://pydeps.readthedocs.io/>`_
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

