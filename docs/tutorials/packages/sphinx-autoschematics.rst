Sphinx-Autoschematics Tutorial
==============================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-autoschematics/>`_
   - `API Documentation <../../pdoc/sphinx_autoschematics/index.html>`_
   - `Manual <https://github.com/LudditeLabs/autodoc-tool>`_

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

   docker run --rm viper-sphinx:latest python -c "import sphinx_autoschematics; print('Installed')"

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
     viper-sphinx:latest \
     sphinx-build -b html /project/docs /project/docs/_build/html

With Circuit Simulation
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: dockerfile

   FROM viper-sphinx:latest
   
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
               viper-sphinx:latest \
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


Practical Examples
------------------

Basic Circuit Diagrams
----------------------

Simple Circuit
~~~~~~~~~~~~~~

.. schematic::
   :circuit: basic-led
   
   R1: resistor, value=330
   LED1: led, color=red
   V1: voltage_source, voltage=5V
   
   V1.positive -> R1.in
   R1.out -> LED1.anode
   LED1.cathode -> V1.negative

Resistor Divider
~~~~~~~~~~~~~~~~

.. schematic::
   :circuit: voltage-divider
   :width: 400
   
   V1: voltage_source, voltage=12V
   R1: resistor, value=10k
   R2: resistor, value=10k
   GND: ground
   
   V1.positive -> R1.in
   R1.out -> R2.in -> Vout
   R2.out -> GND
   V1.negative -> GND

Amplifier Circuit
~~~~~~~~~~~~~~~~~

.. schematic::
   :circuit: basic-amplifier
   :style: detailed
   
   VCC: voltage_source, voltage=12V
   R1: resistor, value=1k
   R2: resistor, value=10k
   C1: capacitor, value=10uF
   Q1: transistor, type=NPN
   Input: port, type=input
   Output: port, type=output
   GND: ground
   
   VCC -> R1 -> Q1.collector -> Output
   Input -> C1 -> Q1.base
   Q1.base -> R2 -> GND
   Q1.emitter -> GND

Digital Circuits
----------------

Logic Gates
~~~~~~~~~~~

.. schematic::
   :circuit: logic-gates
   :type: digital
   
   A: input_port
   B: input_port
   AND1: and_gate
   OR1: or_gate
   NOT1: not_gate
   Y: output_port
   
   A -> AND1.in1
   B -> AND1.in2
   AND1.out -> OR1.in1
   B -> NOT1.in
   NOT1.out -> OR1.in2
   OR1.out -> Y

Flip-Flop
~~~~~~~~~

.. schematic::
   :circuit: d-flipflop
   :type: digital
   
   D: input_port, label="Data"
   CLK: input_port, label="Clock"
   Q: output_port, label="Q"
   Qn: output_port, label="Q̄"
   
   DFF1: d_flipflop
   
   D -> DFF1.D
   CLK -> DFF1.CLK
   DFF1.Q -> Q
   DFF1.Qn -> Qn

Counter Circuit
~~~~~~~~~~~~~~~

.. schematic::
   :circuit: 4bit-counter
   :type: digital
   :orientation: horizontal
   
   CLK: input_port
   RST: input_port
   Q0: output_port
   Q1: output_port
   Q2: output_port
   Q3: output_port
   
   FF0: jk_flipflop
   FF1: jk_flipflop
   FF2: jk_flipflop
   FF3: jk_flipflop
   
   CLK -> FF0.CLK -> FF1.CLK -> FF2.CLK -> FF3.CLK
   RST -> FF0.RST, FF1.RST, FF2.RST, FF3.RST
   FF0.Q -> Q0, FF1.CLK
   FF1.Q -> Q1, FF2.CLK
   FF2.Q -> Q2, FF3.CLK
   FF3.Q -> Q3

Integrated Circuits
-------------------

Op-Amp Circuit
~~~~~~~~~~~~~~

.. schematic::
   :circuit: opamp-buffer
   :component-lib: analog
   
   Input: port
   Output: port
   U1: opamp, model=LM358
   R1: resistor, value=10k
   VCC: power, voltage=+12V
   VEE: power, voltage=-12V
   
   Input -> U1.in_positive
   U1.out -> Output, U1.in_negative
   VCC -> U1.vcc
   VEE -> U1.vee

555 Timer
~~~~~~~~~

.. schematic::
   :circuit: 555-astable
   :component-lib: ic
   
   VCC: voltage_source, voltage=9V
   U1: ic_555
   R1: resistor, value=10k
   R2: resistor, value=100k
   C1: capacitor, value=100nF
   C2: capacitor, value=10uF
   Output: port
   GND: ground
   
   VCC -> U1.vcc, R1
   R1 -> U1.discharge, R2
   R2 -> U1.threshold, U1.trigger, C1
   C1 -> GND
   U1.control -> C2 -> GND
   U1.reset -> VCC
   U1.output -> Output
   U1.gnd -> GND

Microcontroller Circuit
~~~~~~~~~~~~~~~~~~~~~~~~

.. schematic::
   :circuit: mcu-basic
   :scale: 0.8
   
   MCU: microcontroller, model=ATmega328P
   XTAL: crystal, frequency=16MHz
   C1: capacitor, value=22pF
   C2: capacitor, value=22pF
   R1: resistor, value=10k
   C3: capacitor, value=100nF
   VCC: power, voltage=5V
   GND: ground
   
   VCC -> MCU.VCC, MCU.AVCC, R1
   R1 -> MCU.RESET
   MCU.XTAL1 -> XTAL -> MCU.XTAL2
   XTAL -> C1 -> GND
   XTAL -> C2 -> GND
   MCU.GND -> GND
   VCC -> C3 -> GND

Power Supply Circuits
----------------------

Linear Regulator
~~~~~~~~~~~~~~~~

.. schematic::
   :circuit: 5v-regulator
   :style: power
   
   Input: port, voltage=12V
   U1: regulator, model=LM7805
   C1: capacitor, value=100nF, type=ceramic
   C2: capacitor, value=10uF, type=electrolytic
   C3: capacitor, value=100nF, type=ceramic
   Output: port, voltage=5V
   GND: ground
   
   Input -> C1 -> GND
   Input -> U1.in
   U1.out -> C2 -> GND
   U1.out -> C3 -> GND
   U1.out -> Output
   U1.gnd -> GND

Buck Converter
~~~~~~~~~~~~~~

.. schematic::
   :circuit: buck-converter
   :type: switching
   
   VIN: voltage_source, voltage=12V
   Q1: mosfet, type=NMOS
   D1: diode, type=schottky
   L1: inductor, value=100uH
   C1: capacitor, value=100uF
   Driver: pwm_controller
   VOUT: port, voltage=5V
   GND: ground
   
   VIN -> Q1.drain
   Q1.source -> L1, D1.cathode
   L1 -> C1 -> VOUT
   D1.anode -> GND
   C1 -> GND
   Driver.out -> Q1.gate

Schematic Annotations
---------------------

With Labels
~~~~~~~~~~~

.. schematic::
   :circuit: annotated
   :show-values:
   :show-labels:
   
   VCC: voltage_source, voltage=5V, label="Power Supply"
   R1: resistor, value=1k, label="Current Limit"
   LED1: led, color=green, label="Status"
   GND: ground
   
   VCC -> R1 -> LED1 -> GND
   
   annotation: "LED current = 4mA", position=(R1, LED1)
   annotation: "Forward voltage = 2V", position=LED1

With Measurements
~~~~~~~~~~~~~~~~~

.. schematic::
   :circuit: measured
   :show-measurements:
   
   V1: voltage_source, voltage=12V
   R1: resistor, value=100
   R2: resistor, value=200
   GND: ground
   
   V1 -> R1 -> Node1 -> R2 -> GND
   V1 -> GND
   
   voltmeter: Node1 to GND, reading="4V"
   ammeter: V1 to R1, reading="40mA"

PCB Layout Integration
----------------------

Component Placement
~~~~~~~~~~~~~~~~~~~

.. schematic::
   :circuit: pcb-layout
   :format: pcb
   :layers: top, bottom
   
   # Component placement
   U1: ic, package=DIP16, position=(50, 50)
   C1: capacitor, package=0805, position=(30, 50)
   R1: resistor, package=0603, position=(70, 50)
   
   # Connections
   U1.vcc -> C1.1 -> VCC
   U1.gnd -> GND
   U1.out -> R1.1

Configuration Examples
----------------------

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_autoschematics',
   ]
   
   # Schematic generation
   autoschematics_output_format = 'svg'  # 'svg', 'png', 'pdf'
   autoschematics_dpi = 300

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

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

Netlist Export
~~~~~~~~~~~~~~

.. code-block:: python

   # Generate SPICE netlists
   autoschematics_export_spice = True
   autoschematics_spice_dir = '_schematics/netlists'
   
   # Generate KiCad netlists
   autoschematics_export_kicad = True
   autoschematics_kicad_dir = '_schematics/kicad'

Simulation Integration
----------------------

Transient Analysis
~~~~~~~~~~~~~~~~~~

.. schematic::
   :circuit: rc-circuit
   :simulate: transient
   :tstop: 1ms
   :tstep: 1us
   
   V1: pulse_source, v1=0, v2=5, period=1ms
   R1: resistor, value=1k
   C1: capacitor, value=1uF
   GND: ground
   
   V1 -> R1 -> Node1 -> C1 -> GND
   
   plot: voltage(Node1) vs time

AC Analysis
~~~~~~~~~~~

.. schematic::
   :circuit: rc-filter
   :simulate: ac
   :fstart: 1Hz
   :fstop: 1MHz
   :points: 100
   
   VIN: ac_source, amplitude=1V
   R1: resistor, value=1k
   C1: capacitor, value=100nF
   VOUT: port
   GND: ground
   
   VIN -> R1 -> C1 -> VOUT
   C1 -> GND
   
   plot: frequency_response(VOUT)

Custom Components
-----------------

Component Definition
~~~~~~~~~~~~~~~~~~~~

.. schematic::
   :circuit: custom-components
   
   # Define custom component
   component CustomFilter:
       ports: input, output, gnd
       subcircuit:
           R1: resistor, value=1k
           C1: capacitor, value=100nF
           input -> R1 -> output, C1
           C1 -> gnd
   
   # Use custom component
   VIN: voltage_source
   Filter1: CustomFilter
   VOUT: port
   GND: ground
   
   VIN -> Filter1.input
   Filter1.output -> VOUT
   Filter1.gnd -> GND

Practical Examples
------------------

Arduino Shield
~~~~~~~~~~~~~~

.. schematic::
   :circuit: arduino-shield
   :board: arduino-uno
   
   # Digital pins
   D2: arduino_pin, type=digital
   D3: arduino_pin, type=digital
   
   # Analog pins
   A0: arduino_pin, type=analog
   
   # Components
   R1: resistor, value=10k
   LED1: led, color=red
   Sensor: temperature_sensor, model=LM35
   
   # Connections
   D2 -> R1 -> LED1 -> GND
   A0 -> Sensor.out
   Sensor.vcc -> 5V
   Sensor.gnd -> GND

Motor Driver
~~~~~~~~~~~~

.. schematic::
   :circuit: h-bridge
   :component-lib: power
   
   VCC: power, voltage=12V
   Q1: mosfet, type=PMOS
   Q2: mosfet, type=NMOS
   Q3: mosfet, type=PMOS
   Q4: mosfet, type=NMOS
   M1: dc_motor
   Driver: motor_driver_ic
   IN1: input_port
   IN2: input_port
   GND: ground
   
   VCC -> Q1.source, Q3.source
   Q1.drain -> M1.terminal1, Q2.drain
   Q3.drain -> M1.terminal2, Q4.drain
   Q2.source -> GND
   Q4.source -> GND
   IN1 -> Driver.in1
   IN2 -> Driver.in2
   Driver.out1 -> Q1.gate, Q2.gate
   Driver.out2 -> Q3.gate, Q4.gate


Practical Examples
------------------

Basic Circuit Diagrams
----------------------

Simple Circuit
~~~~~~~~~~~~~~

.. schematic::
   :circuit: basic-led
   
   R1: resistor, value=330
   LED1: led, color=red
   V1: voltage_source, voltage=5V
   
   V1.positive -> R1.in
   R1.out -> LED1.anode
   LED1.cathode -> V1.negative

Resistor Divider
~~~~~~~~~~~~~~~~

.. schematic::
   :circuit: voltage-divider
   :width: 400
   
   V1: voltage_source, voltage=12V
   R1: resistor, value=10k
   R2: resistor, value=10k
   GND: ground
   
   V1.positive -> R1.in
   R1.out -> R2.in -> Vout
   R2.out -> GND
   V1.negative -> GND

Amplifier Circuit
~~~~~~~~~~~~~~~~~

.. schematic::
   :circuit: basic-amplifier
   :style: detailed
   
   VCC: voltage_source, voltage=12V
   R1: resistor, value=1k
   R2: resistor, value=10k
   C1: capacitor, value=10uF
   Q1: transistor, type=NPN
   Input: port, type=input
   Output: port, type=output
   GND: ground
   
   VCC -> R1 -> Q1.collector -> Output
   Input -> C1 -> Q1.base
   Q1.base -> R2 -> GND
   Q1.emitter -> GND

Digital Circuits
----------------

Logic Gates
~~~~~~~~~~~

.. schematic::
   :circuit: logic-gates
   :type: digital
   
   A: input_port
   B: input_port
   AND1: and_gate
   OR1: or_gate
   NOT1: not_gate
   Y: output_port
   
   A -> AND1.in1
   B -> AND1.in2
   AND1.out -> OR1.in1
   B -> NOT1.in
   NOT1.out -> OR1.in2
   OR1.out -> Y

Flip-Flop
~~~~~~~~~

.. schematic::
   :circuit: d-flipflop
   :type: digital
   
   D: input_port, label="Data"
   CLK: input_port, label="Clock"
   Q: output_port, label="Q"
   Qn: output_port, label="Q̄"
   
   DFF1: d_flipflop
   
   D -> DFF1.D
   CLK -> DFF1.CLK
   DFF1.Q -> Q
   DFF1.Qn -> Qn

Counter Circuit
~~~~~~~~~~~~~~~

.. schematic::
   :circuit: 4bit-counter
   :type: digital
   :orientation: horizontal
   
   CLK: input_port
   RST: input_port
   Q0: output_port
   Q1: output_port
   Q2: output_port
   Q3: output_port
   
   FF0: jk_flipflop
   FF1: jk_flipflop
   FF2: jk_flipflop
   FF3: jk_flipflop
   
   CLK -> FF0.CLK -> FF1.CLK -> FF2.CLK -> FF3.CLK
   RST -> FF0.RST, FF1.RST, FF2.RST, FF3.RST
   FF0.Q -> Q0, FF1.CLK
   FF1.Q -> Q1, FF2.CLK
   FF2.Q -> Q2, FF3.CLK
   FF3.Q -> Q3

Integrated Circuits
-------------------

Op-Amp Circuit
~~~~~~~~~~~~~~

.. schematic::
   :circuit: opamp-buffer
   :component-lib: analog
   
   Input: port
   Output: port
   U1: opamp, model=LM358
   R1: resistor, value=10k
   VCC: power, voltage=+12V
   VEE: power, voltage=-12V
   
   Input -> U1.in_positive
   U1.out -> Output, U1.in_negative
   VCC -> U1.vcc
   VEE -> U1.vee

555 Timer
~~~~~~~~~

.. schematic::
   :circuit: 555-astable
   :component-lib: ic
   
   VCC: voltage_source, voltage=9V
   U1: ic_555
   R1: resistor, value=10k
   R2: resistor, value=100k
   C1: capacitor, value=100nF
   C2: capacitor, value=10uF
   Output: port
   GND: ground
   
   VCC -> U1.vcc, R1
   R1 -> U1.discharge, R2
   R2 -> U1.threshold, U1.trigger, C1
   C1 -> GND
   U1.control -> C2 -> GND
   U1.reset -> VCC
   U1.output -> Output
   U1.gnd -> GND

Microcontroller Circuit
~~~~~~~~~~~~~~~~~~~~~~~~

.. schematic::
   :circuit: mcu-basic
   :scale: 0.8
   
   MCU: microcontroller, model=ATmega328P
   XTAL: crystal, frequency=16MHz
   C1: capacitor, value=22pF
   C2: capacitor, value=22pF
   R1: resistor, value=10k
   C3: capacitor, value=100nF
   VCC: power, voltage=5V
   GND: ground
   
   VCC -> MCU.VCC, MCU.AVCC, R1
   R1 -> MCU.RESET
   MCU.XTAL1 -> XTAL -> MCU.XTAL2
   XTAL -> C1 -> GND
   XTAL -> C2 -> GND
   MCU.GND -> GND
   VCC -> C3 -> GND

Power Supply Circuits
----------------------

Linear Regulator
~~~~~~~~~~~~~~~~

.. schematic::
   :circuit: 5v-regulator
   :style: power
   
   Input: port, voltage=12V
   U1: regulator, model=LM7805
   C1: capacitor, value=100nF, type=ceramic
   C2: capacitor, value=10uF, type=electrolytic
   C3: capacitor, value=100nF, type=ceramic
   Output: port, voltage=5V
   GND: ground
   
   Input -> C1 -> GND
   Input -> U1.in
   U1.out -> C2 -> GND
   U1.out -> C3 -> GND
   U1.out -> Output
   U1.gnd -> GND

Buck Converter
~~~~~~~~~~~~~~

.. schematic::
   :circuit: buck-converter
   :type: switching
   
   VIN: voltage_source, voltage=12V
   Q1: mosfet, type=NMOS
   D1: diode, type=schottky
   L1: inductor, value=100uH
   C1: capacitor, value=100uF
   Driver: pwm_controller
   VOUT: port, voltage=5V
   GND: ground
   
   VIN -> Q1.drain
   Q1.source -> L1, D1.cathode
   L1 -> C1 -> VOUT
   D1.anode -> GND
   C1 -> GND
   Driver.out -> Q1.gate

Schematic Annotations
---------------------

With Labels
~~~~~~~~~~~

.. schematic::
   :circuit: annotated
   :show-values:
   :show-labels:
   
   VCC: voltage_source, voltage=5V, label="Power Supply"
   R1: resistor, value=1k, label="Current Limit"
   LED1: led, color=green, label="Status"
   GND: ground
   
   VCC -> R1 -> LED1 -> GND
   
   annotation: "LED current = 4mA", position=(R1, LED1)
   annotation: "Forward voltage = 2V", position=LED1

With Measurements
~~~~~~~~~~~~~~~~~

.. schematic::
   :circuit: measured
   :show-measurements:
   
   V1: voltage_source, voltage=12V
   R1: resistor, value=100
   R2: resistor, value=200
   GND: ground
   
   V1 -> R1 -> Node1 -> R2 -> GND
   V1 -> GND
   
   voltmeter: Node1 to GND, reading="4V"
   ammeter: V1 to R1, reading="40mA"

PCB Layout Integration
----------------------

Component Placement
~~~~~~~~~~~~~~~~~~~

.. schematic::
   :circuit: pcb-layout
   :format: pcb
   :layers: top, bottom
   
   # Component placement
   U1: ic, package=DIP16, position=(50, 50)
   C1: capacitor, package=0805, position=(30, 50)
   R1: resistor, package=0603, position=(70, 50)
   
   # Connections
   U1.vcc -> C1.1 -> VCC
   U1.gnd -> GND
   U1.out -> R1.1

Configuration Examples
----------------------

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_autoschematics',
   ]
   
   # Schematic generation
   autoschematics_output_format = 'svg'  # 'svg', 'png', 'pdf'
   autoschematics_dpi = 300

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

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

Netlist Export
~~~~~~~~~~~~~~

.. code-block:: python

   # Generate SPICE netlists
   autoschematics_export_spice = True
   autoschematics_spice_dir = '_schematics/netlists'
   
   # Generate KiCad netlists
   autoschematics_export_kicad = True
   autoschematics_kicad_dir = '_schematics/kicad'

Simulation Integration
----------------------

Transient Analysis
~~~~~~~~~~~~~~~~~~

.. schematic::
   :circuit: rc-circuit
   :simulate: transient
   :tstop: 1ms
   :tstep: 1us
   
   V1: pulse_source, v1=0, v2=5, period=1ms
   R1: resistor, value=1k
   C1: capacitor, value=1uF
   GND: ground
   
   V1 -> R1 -> Node1 -> C1 -> GND
   
   plot: voltage(Node1) vs time

AC Analysis
~~~~~~~~~~~

.. schematic::
   :circuit: rc-filter
   :simulate: ac
   :fstart: 1Hz
   :fstop: 1MHz
   :points: 100
   
   VIN: ac_source, amplitude=1V
   R1: resistor, value=1k
   C1: capacitor, value=100nF
   VOUT: port
   GND: ground
   
   VIN -> R1 -> C1 -> VOUT
   C1 -> GND
   
   plot: frequency_response(VOUT)

Custom Components
-----------------

Component Definition
~~~~~~~~~~~~~~~~~~~~

.. schematic::
   :circuit: custom-components
   
   # Define custom component
   component CustomFilter:
       ports: input, output, gnd
       subcircuit:
           R1: resistor, value=1k
           C1: capacitor, value=100nF
           input -> R1 -> output, C1
           C1 -> gnd
   
   # Use custom component
   VIN: voltage_source
   Filter1: CustomFilter
   VOUT: port
   GND: ground
   
   VIN -> Filter1.input
   Filter1.output -> VOUT
   Filter1.gnd -> GND

Practical Examples
------------------

Arduino Shield
~~~~~~~~~~~~~~

.. schematic::
   :circuit: arduino-shield
   :board: arduino-uno
   
   # Digital pins
   D2: arduino_pin, type=digital
   D3: arduino_pin, type=digital
   
   # Analog pins
   A0: arduino_pin, type=analog
   
   # Components
   R1: resistor, value=10k
   LED1: led, color=red
   Sensor: temperature_sensor, model=LM35
   
   # Connections
   D2 -> R1 -> LED1 -> GND
   A0 -> Sensor.out
   Sensor.vcc -> 5V
   Sensor.gnd -> GND

Motor Driver
~~~~~~~~~~~~

.. schematic::
   :circuit: h-bridge
   :component-lib: power
   
   VCC: power, voltage=12V
   Q1: mosfet, type=PMOS
   Q2: mosfet, type=NMOS
   Q3: mosfet, type=PMOS
   Q4: mosfet, type=NMOS
   M1: dc_motor
   Driver: motor_driver_ic
   IN1: input_port
   IN2: input_port
   GND: ground
   
   VCC -> Q1.source, Q3.source
   Q1.drain -> M1.terminal1, Q2.drain
   Q3.drain -> M1.terminal2, Q4.drain
   Q2.source -> GND
   Q4.source -> GND
   IN1 -> Driver.in1
   IN2 -> Driver.in2
   Driver.out1 -> Q1.gate, Q2.gate
   Driver.out2 -> Q3.gate, Q4.gate


Practical Examples
------------------

Basic Circuit Diagrams
----------------------

Simple Circuit
~~~~~~~~~~~~~~

.. schematic::
   :circuit: basic-led
   
   R1: resistor, value=330
   LED1: led, color=red
   V1: voltage_source, voltage=5V
   
   V1.positive -> R1.in
   R1.out -> LED1.anode
   LED1.cathode -> V1.negative

Resistor Divider
~~~~~~~~~~~~~~~~

.. schematic::
   :circuit: voltage-divider
   :width: 400
   
   V1: voltage_source, voltage=12V
   R1: resistor, value=10k
   R2: resistor, value=10k
   GND: ground
   
   V1.positive -> R1.in
   R1.out -> R2.in -> Vout
   R2.out -> GND
   V1.negative -> GND

Amplifier Circuit
~~~~~~~~~~~~~~~~~

.. schematic::
   :circuit: basic-amplifier
   :style: detailed
   
   VCC: voltage_source, voltage=12V
   R1: resistor, value=1k
   R2: resistor, value=10k
   C1: capacitor, value=10uF
   Q1: transistor, type=NPN
   Input: port, type=input
   Output: port, type=output
   GND: ground
   
   VCC -> R1 -> Q1.collector -> Output
   Input -> C1 -> Q1.base
   Q1.base -> R2 -> GND
   Q1.emitter -> GND

Digital Circuits
----------------

Logic Gates
~~~~~~~~~~~

.. schematic::
   :circuit: logic-gates
   :type: digital
   
   A: input_port
   B: input_port
   AND1: and_gate
   OR1: or_gate
   NOT1: not_gate
   Y: output_port
   
   A -> AND1.in1
   B -> AND1.in2
   AND1.out -> OR1.in1
   B -> NOT1.in
   NOT1.out -> OR1.in2
   OR1.out -> Y

Flip-Flop
~~~~~~~~~

.. schematic::
   :circuit: d-flipflop
   :type: digital
   
   D: input_port, label="Data"
   CLK: input_port, label="Clock"
   Q: output_port, label="Q"
   Qn: output_port, label="Q̄"
   
   DFF1: d_flipflop
   
   D -> DFF1.D
   CLK -> DFF1.CLK
   DFF1.Q -> Q
   DFF1.Qn -> Qn

Counter Circuit
~~~~~~~~~~~~~~~

.. schematic::
   :circuit: 4bit-counter
   :type: digital
   :orientation: horizontal
   
   CLK: input_port
   RST: input_port
   Q0: output_port
   Q1: output_port
   Q2: output_port
   Q3: output_port
   
   FF0: jk_flipflop
   FF1: jk_flipflop
   FF2: jk_flipflop
   FF3: jk_flipflop
   
   CLK -> FF0.CLK -> FF1.CLK -> FF2.CLK -> FF3.CLK
   RST -> FF0.RST, FF1.RST, FF2.RST, FF3.RST
   FF0.Q -> Q0, FF1.CLK
   FF1.Q -> Q1, FF2.CLK
   FF2.Q -> Q2, FF3.CLK
   FF3.Q -> Q3

Integrated Circuits
-------------------

Op-Amp Circuit
~~~~~~~~~~~~~~

.. schematic::
   :circuit: opamp-buffer
   :component-lib: analog
   
   Input: port
   Output: port
   U1: opamp, model=LM358
   R1: resistor, value=10k
   VCC: power, voltage=+12V
   VEE: power, voltage=-12V
   
   Input -> U1.in_positive
   U1.out -> Output, U1.in_negative
   VCC -> U1.vcc
   VEE -> U1.vee

555 Timer
~~~~~~~~~

.. schematic::
   :circuit: 555-astable
   :component-lib: ic
   
   VCC: voltage_source, voltage=9V
   U1: ic_555
   R1: resistor, value=10k
   R2: resistor, value=100k
   C1: capacitor, value=100nF
   C2: capacitor, value=10uF
   Output: port
   GND: ground
   
   VCC -> U1.vcc, R1
   R1 -> U1.discharge, R2
   R2 -> U1.threshold, U1.trigger, C1
   C1 -> GND
   U1.control -> C2 -> GND
   U1.reset -> VCC
   U1.output -> Output
   U1.gnd -> GND

Microcontroller Circuit
~~~~~~~~~~~~~~~~~~~~~~~~

.. schematic::
   :circuit: mcu-basic
   :scale: 0.8
   
   MCU: microcontroller, model=ATmega328P
   XTAL: crystal, frequency=16MHz
   C1: capacitor, value=22pF
   C2: capacitor, value=22pF
   R1: resistor, value=10k
   C3: capacitor, value=100nF
   VCC: power, voltage=5V
   GND: ground
   
   VCC -> MCU.VCC, MCU.AVCC, R1
   R1 -> MCU.RESET
   MCU.XTAL1 -> XTAL -> MCU.XTAL2
   XTAL -> C1 -> GND
   XTAL -> C2 -> GND
   MCU.GND -> GND
   VCC -> C3 -> GND

Power Supply Circuits
----------------------

Linear Regulator
~~~~~~~~~~~~~~~~

.. schematic::
   :circuit: 5v-regulator
   :style: power
   
   Input: port, voltage=12V
   U1: regulator, model=LM7805
   C1: capacitor, value=100nF, type=ceramic
   C2: capacitor, value=10uF, type=electrolytic
   C3: capacitor, value=100nF, type=ceramic
   Output: port, voltage=5V
   GND: ground
   
   Input -> C1 -> GND
   Input -> U1.in
   U1.out -> C2 -> GND
   U1.out -> C3 -> GND
   U1.out -> Output
   U1.gnd -> GND

Buck Converter
~~~~~~~~~~~~~~

.. schematic::
   :circuit: buck-converter
   :type: switching
   
   VIN: voltage_source, voltage=12V
   Q1: mosfet, type=NMOS
   D1: diode, type=schottky
   L1: inductor, value=100uH
   C1: capacitor, value=100uF
   Driver: pwm_controller
   VOUT: port, voltage=5V
   GND: ground
   
   VIN -> Q1.drain
   Q1.source -> L1, D1.cathode
   L1 -> C1 -> VOUT
   D1.anode -> GND
   C1 -> GND
   Driver.out -> Q1.gate

Schematic Annotations
---------------------

With Labels
~~~~~~~~~~~

.. schematic::
   :circuit: annotated
   :show-values:
   :show-labels:
   
   VCC: voltage_source, voltage=5V, label="Power Supply"
   R1: resistor, value=1k, label="Current Limit"
   LED1: led, color=green, label="Status"
   GND: ground
   
   VCC -> R1 -> LED1 -> GND
   
   annotation: "LED current = 4mA", position=(R1, LED1)
   annotation: "Forward voltage = 2V", position=LED1

With Measurements
~~~~~~~~~~~~~~~~~

.. schematic::
   :circuit: measured
   :show-measurements:
   
   V1: voltage_source, voltage=12V
   R1: resistor, value=100
   R2: resistor, value=200
   GND: ground
   
   V1 -> R1 -> Node1 -> R2 -> GND
   V1 -> GND
   
   voltmeter: Node1 to GND, reading="4V"
   ammeter: V1 to R1, reading="40mA"

PCB Layout Integration
----------------------

Component Placement
~~~~~~~~~~~~~~~~~~~

.. schematic::
   :circuit: pcb-layout
   :format: pcb
   :layers: top, bottom
   
   # Component placement
   U1: ic, package=DIP16, position=(50, 50)
   C1: capacitor, package=0805, position=(30, 50)
   R1: resistor, package=0603, position=(70, 50)
   
   # Connections
   U1.vcc -> C1.1 -> VCC
   U1.gnd -> GND
   U1.out -> R1.1

Configuration Examples
----------------------

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_autoschematics',
   ]
   
   # Schematic generation
   autoschematics_output_format = 'svg'  # 'svg', 'png', 'pdf'
   autoschematics_dpi = 300

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

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

Netlist Export
~~~~~~~~~~~~~~

.. code-block:: python

   # Generate SPICE netlists
   autoschematics_export_spice = True
   autoschematics_spice_dir = '_schematics/netlists'
   
   # Generate KiCad netlists
   autoschematics_export_kicad = True
   autoschematics_kicad_dir = '_schematics/kicad'

Simulation Integration
----------------------

Transient Analysis
~~~~~~~~~~~~~~~~~~

.. schematic::
   :circuit: rc-circuit
   :simulate: transient
   :tstop: 1ms
   :tstep: 1us
   
   V1: pulse_source, v1=0, v2=5, period=1ms
   R1: resistor, value=1k
   C1: capacitor, value=1uF
   GND: ground
   
   V1 -> R1 -> Node1 -> C1 -> GND
   
   plot: voltage(Node1) vs time

AC Analysis
~~~~~~~~~~~

.. schematic::
   :circuit: rc-filter
   :simulate: ac
   :fstart: 1Hz
   :fstop: 1MHz
   :points: 100
   
   VIN: ac_source, amplitude=1V
   R1: resistor, value=1k
   C1: capacitor, value=100nF
   VOUT: port
   GND: ground
   
   VIN -> R1 -> C1 -> VOUT
   C1 -> GND
   
   plot: frequency_response(VOUT)

Custom Components
-----------------

Component Definition
~~~~~~~~~~~~~~~~~~~~

.. schematic::
   :circuit: custom-components
   
   # Define custom component
   component CustomFilter:
       ports: input, output, gnd
       subcircuit:
           R1: resistor, value=1k
           C1: capacitor, value=100nF
           input -> R1 -> output, C1
           C1 -> gnd
   
   # Use custom component
   VIN: voltage_source
   Filter1: CustomFilter
   VOUT: port
   GND: ground
   
   VIN -> Filter1.input
   Filter1.output -> VOUT
   Filter1.gnd -> GND

Practical Examples
------------------

Arduino Shield
~~~~~~~~~~~~~~

.. schematic::
   :circuit: arduino-shield
   :board: arduino-uno
   
   # Digital pins
   D2: arduino_pin, type=digital
   D3: arduino_pin, type=digital
   
   # Analog pins
   A0: arduino_pin, type=analog
   
   # Components
   R1: resistor, value=10k
   LED1: led, color=red
   Sensor: temperature_sensor, model=LM35
   
   # Connections
   D2 -> R1 -> LED1 -> GND
   A0 -> Sensor.out
   Sensor.vcc -> 5V
   Sensor.gnd -> GND

Motor Driver
~~~~~~~~~~~~

.. schematic::
   :circuit: h-bridge
   :component-lib: power
   
   VCC: power, voltage=12V
   Q1: mosfet, type=PMOS
   Q2: mosfet, type=NMOS
   Q3: mosfet, type=PMOS
   Q4: mosfet, type=NMOS
   M1: dc_motor
   Driver: motor_driver_ic
   IN1: input_port
   IN2: input_port
   GND: ground
   
   VCC -> Q1.source, Q3.source
   Q1.drain -> M1.terminal1, Q2.drain
   Q3.drain -> M1.terminal2, Q4.drain
   Q2.source -> GND
   Q4.source -> GND
   IN1 -> Driver.in1
   IN2 -> Driver.in2
   Driver.out1 -> Q1.gate, Q2.gate
   Driver.out2 -> Q3.gate, Q4.gate

Additional Resources
--------------------
- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- :doc:`sphinx-diagrams` - General diagram tools
- `SPICE Documentation <http://ngspice.sourceforge.net/docs.html>`_
- `KiCad Documentation <https://docs.kicad.org/>`_
- :doc:`../tutorials/packages/sphinx-autoschematics` - Complete tutorial
- Official documentation: https://sphinx-autoschematics.readthedocs.io/
- GitHub repository: https://github.com/sphinx-doc/sphinx-autoschematics

