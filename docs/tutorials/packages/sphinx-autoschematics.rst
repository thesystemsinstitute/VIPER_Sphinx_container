Sphinx-Autoschematics Tutorial
==============================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-autoschematics/>`_
   - `API Documentation <../../pdoc/sphinx_autoschematics/index.html>`_
   - `Manual <https://github.com/LudditeLabs/autodoc-tool>`_
   - :doc:`Working Example <../../examples/sphinx-autoschematics-example>`


.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinx-autoschematics to automatically generate circuit schematics and electrical diagrams in your Sphinx documentation from netlist or schematic description files.

What is Sphinx-Autoschematics?
-------------------------------
sphinx-autoschematics is a Sphinx extension that provides automatic generation of circuit schematics:

- Generate schematics from netlist files (SPICE, etc.)
- Convert schematic descriptions to diagrams
- Support for various EDA tool formats
- Automatic circuit diagram rendering
- Component library integration
- Interactive circuit diagrams
- Symbol and footprint visualization
- PCB layout documentation

This is essential for electronics documentation, hardware design guides, and circuit analysis.

The sphinx-autoschematics extension integrates with circuit design tools to generate and embed electronic schematics directly in Sphinx documentation.


Installation
------------

sphinx-autoschematics is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinx_autoschematics; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_autoschematics',
   ]
   
   # Path to schematic files
   autoschematics_path = ['../schematics']

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinx_autoschematics']
   
   # Schematic file paths
   autoschematics_path = ['../schematics', '../circuits']
   autoschematics_include_patterns = ['*.net', '*.cir', '*.asc']
   autoschematics_exclude_patterns = ['*_backup.*']
   
   # Rendering options
   autoschematics_format = 'svg'  # or 'png', 'pdf'
   autoschematics_dpi = 300
   autoschematics_scale = 1.0
   autoschematics_background = 'white'
   
   # Component libraries
   autoschematics_libraries = [
       'default',
       '../lib/custom_components'
   ]
   
   # Netlist parser
   autoschematics_netlist_format = 'spice'  # or 'kicad', 'eagle'
   autoschematics_simulator = 'ngspice'
   
   # Display options
   autoschematics_show_values = True
   autoschematics_show_labels = True
   autoschematics_show_grid = False
   autoschematics_wire_style = 'orthogonal'


.. code-block:: python

   # Circuit simulator integration
   autoschematics_simulator = 'ngspice'  # 'ngspice', 'ltspice'
   autoschematics_simulate = True
   
   # Component libraries
   autoschematics_libraries = [
       '/path/to/custom/lib',
       'builtin:analog',
       'builtin:digital',
       'builtin:power',
   ]
   
   # Style configuration
   autoschematics_style = {
       'wire_width': 2,
       'component_scale': 1.0,
       'font_size': 12,
       'grid_size': 10,
   }

Basic Usage
-----------

Include Schematic from File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. autoschematic:: amplifier.cir
      :format: svg
      :caption: Basic amplifier circuit

Inline Circuit Description
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. schematic::
      
      R1 in out 10k
      C1 out gnd 100n
      
      Circuit description in netlist format.

Component Diagram
~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. component:: LM358
      :type: opamp
      :show-pinout: true

Circuit Symbol
~~~~~~~~~~~~~~

.. code-block:: rst

   .. circuit-symbol:: resistor
      :value: 10kΩ
      :label: R1

   Voltage Divider
   ===============
   
   A simple voltage divider circuit that reduces 12V to 6V.
   
   Schematic
   ---------
   
   .. autoschematic:: voltage_divider.cir
      :caption: Voltage divider circuit
      :scale: 1.5
   
   Circuit Description
   -------------------
   
   The circuit consists of:
   
   - **V1**: 12V DC source
   - **R1**: 10kΩ resistor (upper)
   - **R2**: 10kΩ resistor (lower)
   
   The output voltage is calculated as:
   
   .. math::
   
      V_{out} = V_{in} \times \frac{R_2}{R_1 + R_2} = 12V \times \frac{10k}{20k} = 6V
   
   Component Values
   ----------------
   
   .. list-table::
      :header-rows: 1
      :widths: 20 30 50
   
      * - Component
        - Value
        - Notes
      * - R1
        - 10kΩ
        - ±5%, 1/4W
      * - R2
        - 10kΩ
        - ±5%, 1/4W
      * - V1
        - 12V DC
        - Power supply
   
   Simulation
   ----------
   
   .. code-block:: spice
   
      .control
      dc V1 0 15 0.1
      plot vout
      .endc

Example 2: Op-Amp Circuit
~~~~~~~~~~~~~~~~~~~~~~~~~~

``circuits/opamp_amplifier.cir``:

.. code-block:: spice

   * Non-Inverting Amplifier
   * Gain = 11 (1 + R2/R1)
   
   .title Non-Inverting Amplifier
   
   V1 vin 0 AC 1
   X1 0 vin vout opamp
   R1 vout vn 100k
   R2 vn 0 10k
   
   .model opamp OPA
   
   .end

``docs/circuits/opamp_amp.rst``:

.. code-block:: rst

   Non-Inverting Amplifier
   ========================
   
   An op-amp based non-inverting amplifier with gain of 11.
   
   Schematic
   ---------
   
   .. autoschematic:: opamp_amplifier.cir
      :show-values: true
      :show-labels: true
   
   Theory of Operation
   -------------------
   
   The gain is determined by the feedback resistors:
   
   .. math::
   
      A_v = 1 + \frac{R_2}{R_1} = 1 + \frac{100k}{10k} = 11
   
   For an input of 1V, the output will be 11V.
   
   Op-Amp Pinout
   -------------
   
   .. component:: LM358
      :show-pinout: true
      :pin-labels: true
   
   Frequency Response
   ------------------
   
   .. code-block:: spice
   
      .ac dec 10 1 1Meg
      .plot ac vdb(vout)

Example 3: Power Supply Circuit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``circuits/power_supply.cir``:

.. code-block:: spice

   * 5V Linear Regulator
   
   .title 5V Power Supply
   
   V1 vin 0 DC 12
   
   * Bridge Rectifier
   D1 vin n1 1N4007
   D2 0 n1 1N4007
   D3 vin n2 1N4007
   D4 0 n2 1N4007
   
   * Filter Capacitor
   C1 n1 0 1000u
   
   * Voltage Regulator
   X1 n1 0 vout LM7805
   
   * Output Capacitor
   C2 vout 0 100u
   
   .end

``docs/circuits/power_supply.rst``:

.. code-block:: rst

   5V Power Supply
   ===============
   
   A regulated 5V power supply using LM7805.
   
   Complete Schematic
   ------------------
   
   .. autoschematic:: power_supply.cir
      :caption: 5V linear regulator circuit
      :background: white
   
   Circuit Blocks
   --------------
   
   Rectifier
   ~~~~~~~~~
   
   .. schematic::
      :section: rectifier
      
      Bridge rectifier using 1N4007 diodes.
   
   Filter
   ~~~~~~
   
   .. schematic::
      :section: filter
      
      1000µF electrolytic capacitor for ripple reduction.
   
   Regulator
   ~~~~~~~~~
   
   .. component:: LM7805
      :show-pinout: true
      :typical-circuit: true
   
   Bill of Materials
   -----------------
   
   .. list-table::
      :header-rows: 1
   
      * - Qty
        - Ref
        - Value
        - Package
        - Notes
      * - 4
        - D1-D4
        - 1N4007
        - DO-41
        - 1A, 1000V
      * - 1
        - C1
        - 1000µF
        - Radial
        - 25V electrolytic
      * - 1
        - C2
        - 100µF
        - Radial
        - 16V electrolytic
      * - 1
        - U1
        - LM7805
        - TO-220
        - 1A regulator

Example 4: PCB Layout Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   PCB Layout Guide
   ================
   
   Schematic
   ---------
   
   .. autoschematic:: board.cir
      :view: schematic
   
   PCB Layout
   ----------
   
   .. autoschematic:: board.cir
      :view: pcb
      :layers: all
   
   Top Layer
   ~~~~~~~~~
   
   .. autoschematic:: board.cir
      :view: pcb
      :layer: top
      :show-silkscreen: true
   
   Bottom Layer
   ~~~~~~~~~~~~
   
   .. autoschematic:: board.cir
      :view: pcb
      :layer: bottom
   
   3D View
   ~~~~~~~
   
   .. autoschematic:: board.cir
      :view: 3d
      :rotate: 30,45,0

Advanced Features
-----------------

Interactive Schematics
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. autoschematic:: circuit.cir
      :interactive: true
      :allow-zoom: true
      :highlight-on-hover: true

Subcircuit Extraction
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. autoschematic:: main.cir
      :subcircuit: amplifier_stage
      :depth: 2

Component Search
~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. component-search::
      :type: resistor
      :value-range: 1k-100k
      :package: 0805

Netlist Analysis
~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. netlist-stats::
      :file: circuit.cir
      
      - Total components: {{ component_count }}
      - Total nets: {{ net_count }}
      - Nodes: {{ node_count }}

Signal Flow Diagram
~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. signal-flow:: circuit.cir
      :from: input
      :to: output
      :show-gains: true

Simulation Results
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. simulation-plot::
      :netlist: circuit.cir
      :analysis: ac
      :x-axis: frequency
      :y-axis: gain
      :log-scale: both

Docker Integration
------------------

Build Documentation with Schematics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     kensai-sphinx:latest \
     sphinx-build -b html /project/docs /project/docs/_build/html

With Circuit Simulation
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: dockerfile

   FROM kensai-sphinx:latest
   
   # Install circuit simulator
   RUN apk add --no-cache ngspice
   
   # Copy circuits
   COPY circuits/ /project/circuits/
   
   # Generate schematics
   WORKDIR /project
   RUN sphinx-build -b html docs/ docs/_build/html

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Build Circuit Documentation
   
   on:
     push:
       paths:
         - 'circuits/**'
         - 'docs/**'
   
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Build Docs
           run: |
             docker run --rm \
               -v $(pwd):/project \
               kensai-sphinx:latest \
               sphinx-build -b html /project/docs /project/docs/_build/html

Best Practices
--------------

1. **Organize Circuit Files**
   
   Keep schematics in dedicated directory:
   
   .. code-block:: text
   
      project/
      ├── circuits/
      │   ├── power/
      │   ├── analog/
      │   └── digital/
      └── docs/

2. **Use Descriptive Names**
   
   Name files clearly:
   
   - ``5v_regulator.cir``
   - ``audio_amplifier.cir``
   - ``usb_interface.cir``

3. **Include Comments**
   
   Document netlists:
   
   .. code-block:: spice
   
      * Component values
      R1 in out 10k  ; Pull-up resistor

4. **Specify Component Values**
   
   Always include component values in schematics

5. **Provide Context**
   
   Include theory, calculations, and notes

6. **Test Simulations**
   
   Verify SPICE netlists compile correctly

Common Patterns
---------------

Circuit Template
~~~~~~~~~~~~~~~~

.. code-block:: rst

   {{ circuit_name }}
   ==================
   
   Overview
   --------
   
   Brief description of the circuit.
   
   Schematic
   ---------
   
   .. autoschematic:: {{ filename }}
   
   Theory
   ------
   
   Circuit analysis and equations.
   
   Components
   ----------
   
   .. list-table::
      :header-rows: 1
      
      * - Ref
        - Value
        - Notes
   
   Simulation
   ----------
   
   .. code-block:: spice
   
      .control
      ...
      .endc

Troubleshooting
---------------

Schematic Not Rendering
~~~~~~~~~~~~~~~~~~~~~~~~

**Solution:**

Check file path and format:

.. code-block:: python

   autoschematics_path = ['../circuits']
   autoschematics_include_patterns = ['*.cir']

Missing Components
~~~~~~~~~~~~~~~~~~

**Solution:**

Add component library:

.. code-block:: python

   autoschematics_libraries = [
       'default',
       '../lib/custom'
   ]

Netlist Parse Errors
~~~~~~~~~~~~~~~~~~~~

**Solution:**

Verify netlist syntax:

.. code-block:: bash

   ngspice -b circuit.cir

Next Steps
----------

1. Create circuit schematic files
2. Configure autoschematics paths
3. Add schematics to documentation
4. Include component specifications
5. Add simulation examples

Additional Resources
--------------------

- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- :doc:`sphinx-diagrams` - General diagram tools
- `SPICE Documentation <http://ngspice.sourceforge.net/docs.html>`_
- `KiCad Documentation <https://docs.kicad.org/>`_
