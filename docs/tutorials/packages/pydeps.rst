Pydeps Tutorial
===============

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/pydeps/>`_
   - `API Documentation <../../pdoc/pydeps/index.html>`_
   - `Manual <https://github.com/thebjorn/pydeps>`_
   - :doc:`Working Example <../../examples/pydeps-example>`


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

   docker run --rm kensai-sphinx:latest pydeps --version

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
     kensai-sphinx:latest \
     pydeps /project/src --cluster -o /project/docs/_static/deps.svg

Batch Generation
~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     kensai-sphinx:latest \
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
               kensai-sphinx:latest \
               bash -c "
                 mkdir -p /project/docs/_static/dependencies
                 pydeps /project/src --cluster \
                   -o /project/docs/_static/dependencies/deps.svg
               "
         
         - name: Check for cycles
           run: |
             docker run --rm -v $(pwd):/project \
               kensai-sphinx:latest \
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
         kensai-sphinx:latest \
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

Additional Resources
--------------------

- :doc:`pydot` - Programmatic graph generation
- :doc:`graphviz` - DOT language visualization
- `Pydeps Documentation <https://pydeps.readthedocs.io/>`_
