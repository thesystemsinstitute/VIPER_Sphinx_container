Sphinx-Autoschematics Example
=============================

This page demonstrates the **sphinx-autoschematics** extension for automatically generating circuit schematics and electronic diagrams in documentation.

.. contents:: Contents
   :local:
   :depth: 2

Overview
--------

The sphinx-autoschematics extension integrates with circuit design tools to generate and embed electronic schematics directly in Sphinx documentation.

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

See Also
--------

- :doc:`../tutorials/packages/sphinx-autoschematics` - Complete tutorial
- Official documentation: https://sphinx-autoschematics.readthedocs.io/
- GitHub repository: https://github.com/sphinx-doc/sphinx-autoschematics
