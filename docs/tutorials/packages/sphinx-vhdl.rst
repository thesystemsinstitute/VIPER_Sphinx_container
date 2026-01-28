Sphinx-VHDL Tutorial
====================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-vhdl/>`_
   - `API Documentation <../../pdoc/sphinx_vhdl/index.html>`_
   - `Manual <https://cesnet.github.io/sphinx-vhdl/>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinx-vhdl to document VHDL (VHSIC Hardware Description Language) code with Sphinx, enabling professional hardware design documentation.

What is Sphinx-VHDL?
---------------------
sphinx-vhdl is a Sphinx extension that provides support for documenting VHDL hardware designs. It offers:

- Automatic extraction of VHDL entities, architectures, and packages
- Syntax highlighting for VHDL code
- Cross-referencing between VHDL components
- Entity diagrams and port descriptions
- Signal flow documentation
- Integration with hardware design workflows
- Support for VHDL-2008 standard

This is essential for FPGA developers, digital design engineers, and hardware verification teams.

sphinx-vhdl adds comprehensive VHDL support to Sphinx, enabling:

- Automatic VHDL code documentation
- Hardware entity documentation
- Architecture and component descriptions
- Signal and port documentation
- Cross-referencing between hardware modules

- Automatic VHDL code documentation
- Hardware entity documentation
- Architecture and component descriptions
- Signal and port documentation
- Cross-referencing between hardware modules


Installation
------------

sphinx-vhdl is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinxcontrib.vhdl; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinxcontrib.vhdl',
   ]
   
   # Path to VHDL source files
   vhdl_source_path = ['../hdl/src']
   
   # Auto-generate documentation
   vhdl_autodoc = True

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinxcontrib.vhdl']
   
   # VHDL source configuration
   vhdl_source_path = ['../hdl/src', '../hdl/lib']
   vhdl_exclude_patterns = ['*_tb.vhd', 'test_*.vhd']
   
   # Documentation options
   vhdl_autodoc = True
   vhdl_show_ports = True
   vhdl_show_generics = True
   vhdl_show_signals = True
   vhdl_show_constants = True
   
   # Diagram generation
   vhdl_generate_diagrams = True
   vhdl_diagram_format = 'svg'
   
   # VHDL standard
   vhdl_standard = '2008'  # or '93', '2002'
   
   # Naming conventions
   vhdl_entity_style = 'title_case'
   vhdl_signal_prefix = 's_'
   vhdl_generic_prefix = 'g_'


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_vhdl',
       # ... other extensions
   ]
   
   # VHDL source directory
   vhdl_source_path = ['hardware/src']
   
   # Autodoc options
   vhdl_autodoc_options = {
       'members': True,
       'show-inheritance': True
   }

Basic Usage
-----------

Documenting Entities
~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. vhdl:entity:: counter
      :file: counter.vhd
      
      8-bit up/down counter with synchronous reset.

Documenting Architectures
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. vhdl:architecture:: rtl
      :entity: counter
      :file: counter.vhd
      
      RTL implementation of the counter.

Documenting Packages
~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. vhdl:package:: math_pkg
      :file: math_pkg.vhd
      
      Mathematical functions and types.

Auto-Documentation
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. vhdl:autoentity:: counter
   
   .. vhdl:autopackage:: math_pkg

VHDL Code Examples
------------------

Basic Counter Example
~~~~~~~~~~~~~~~~~~~~~

Create ``hdl/src/counter.vhd``:

.. code-block:: vhdl

   library IEEE;
   use IEEE.STD_LOGIC_1164.ALL;
   use IEEE.NUMERIC_STD.ALL;
   
   --! @brief 8-bit up/down counter
   --! @details Synchronous counter with enable and direction control
   entity counter is
       generic (
           WIDTH : integer := 8  --! Counter width in bits
       );
       port (
           clk    : in  std_logic;                      --! Clock input
           rst    : in  std_logic;                      --! Synchronous reset
           enable : in  std_logic;                      --! Count enable
           up     : in  std_logic;                      --! Direction: 1=up, 0=down
           count  : out std_logic_vector(WIDTH-1 downto 0)  --! Counter output
       );
   end counter;
   
   --! @brief RTL architecture
   architecture rtl of counter is
       signal count_reg : unsigned(WIDTH-1 downto 0);
   begin
       process(clk)
       begin
           if rising_edge(clk) then
               if rst = '1' then
                   count_reg <= (others => '0');
               elsif enable = '1' then
                   if up = '1' then
                       count_reg <= count_reg + 1;
                   else
                       count_reg <= count_reg - 1;
                   end if;
               end if;
           end if;
       end process;
       
       count <= std_logic_vector(count_reg);
   end rtl;

Document it in ``docs/counter.rst``:

.. code-block:: rst

   Counter Module
   ==============
   
   .. vhdl:autoentity:: counter
      :show-ports:
      :show-generics:
      :show-diagram:
      
   Entity Description
   ------------------
   
   The counter entity implements a simple up/down counter with:
   
   - Configurable width (default 8 bits)
   - Synchronous reset
   - Count enable
   - Direction control
   
   Port Description
   ----------------
   
   .. vhdl:ports:: counter
   
   Generic Parameters
   ------------------
   
   .. vhdl:generics:: counter
   
   Usage Example
   -------------
   
   .. code-block:: vhdl
   
      -- Instantiate 16-bit counter
      u_counter : counter
          generic map (
              WIDTH => 16
          )
          port map (
              clk    => sys_clk,
              rst    => sys_rst,
              enable => cnt_enable,
              up     => direction,
              count  => count_value
          );

   Common Packages
   ===============
   
   Types Package
   -------------
   
   .. vhdl:autopackage:: types_pkg
      :show-constants:
      :show-types:
   
   Constants
   ~~~~~~~~~
   
   .. vhdl:constant:: DATA_WIDTH
      :package: types_pkg
      
      Standard data bus width used throughout the design.
   
   Types
   ~~~~~
   
   .. vhdl:type:: ctrl_t
      :package: types_pkg
      
      Control signal bundle for memory operations.

Example 3: Complete Design Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Project structure:

.. code-block:: text

   myproject/
   ├── hdl/
   │   ├── src/
   │   │   ├── top.vhd
   │   │   ├── counter.vhd
   │   │   ├── alu.vhd
   │   │   └── types_pkg.vhd
   │   └── tb/
   │       └── counter_tb.vhd
   └── docs/
       ├── conf.py
       ├── index.rst
       ├── architecture.rst
       ├── entities/
       │   ├── top.rst
       │   ├── counter.rst
       │   └── alu.rst
       └── packages/
           └── types_pkg.rst

``docs/architecture.rst``:

.. code-block:: rst

   System Architecture
   ===================
   
   Block Diagram
   -------------
   
   .. vhdl:diagram:: top
      :format: svg
      :style: hierarchical
   
   Component Overview
   ------------------
   
   The design consists of:
   
   .. vhdl:entity-list::
      :exclude-testbenches:
   
   Top Level
   ---------
   
   .. vhdl:autoentity:: top
      :show-diagram:
      :show-instantiations:
   
   Submodules
   ----------
   
   Counter
   ~~~~~~~
   
   .. vhdl:autoentity:: counter
   
   ALU
   ~~~
   
   .. vhdl:autoentity:: alu

Advanced Features
-----------------

Port Tables
~~~~~~~~~~~

.. code-block:: rst

   .. vhdl:port-table:: counter
      :show-direction:
      :show-type:
      :show-description:

Signal Flow Diagrams
~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. vhdl:signal-flow:: counter
      :architecture: rtl
      :show-signals:
      :show-processes:

Timing Diagrams
~~~~~~~~~~~~~~~

.. code-block:: rst

   .. vhdl:timing:: counter
      :signals: clk, rst, enable, count
      :cycles: 10

Cross-References
~~~~~~~~~~~~~~~~

.. code-block:: rst

   The :vhdl:entity:`counter` uses :vhdl:pkg:`types_pkg`.
   
   See :vhdl:signal:`count_reg` in architecture :vhdl:arch:`rtl`.

Component Instantiation
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. vhdl:instantiation::
      
      u_counter : counter
          generic map (
              WIDTH => 16
          )
          port map (
              clk    => sys_clk,
              rst    => sys_rst,
              enable => '1',
              up     => direction,
              count  => counter_out
          );

Docker Integration
------------------

Build VHDL Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     kensai-sphinx:latest \
     sphinx-build -b html /project/docs /project/docs/_build/html

With VHDL Analysis
~~~~~~~~~~~~~~~~~~

Create ``analyze_vhdl.sh``:

.. code-block:: bash

   #!/bin/bash
   
   echo "Analyzing VHDL files..."
   
   docker run --rm -v $(pwd):/project kensai-sphinx:latest sh -c "
       cd /project
       
       # Find all VHDL files
       find hdl/src -name '*.vhd' > vhdl_files.txt
       
       # Generate documentation
       sphinx-build -b html docs/ docs/_build/html
   "
   
   echo "Documentation generated!"

Complete Workflow
~~~~~~~~~~~~~~~~~

.. code-block:: dockerfile

   FROM kensai-sphinx:latest
   
   # Copy VHDL sources
   COPY hdl/ /project/hdl/
   
   # Copy documentation
   COPY docs/ /project/docs/
   
   # Build documentation
   RUN sphinx-build -b html /project/docs /project/docs/_build/html
   
   # Serve documentation
   EXPOSE 8080
   CMD ["python", "-m", "http.server", "8080", "-d", "/project/docs/_build/html"]

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Build VHDL Documentation
   
   on:
     push:
       paths:
         - 'hdl/**'
         - 'docs/**'
   
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Build Docs
           run: |
             docker run --rm -v $(pwd):/project \
               kensai-sphinx:latest \
               sphinx-build -b html /project/docs /project/docs/_build/html
         
         - name: Deploy
           uses: peaceiris/actions-gh-pages@v3
           with:
             github_token: ${{ secrets.GITHUB_TOKEN }}
             publish_dir: ./docs/_build/html

GitLab CI
~~~~~~~~~

.. code-block:: yaml

   build-vhdl-docs:
     image: kensai-sphinx:latest
     script:
       - sphinx-build -b html docs/ public
     artifacts:
       paths:
         - public


Use Cases
---------

1. **FPGA Design Documentation**

Best Practices
--------------

1. **Comment Your VHDL Code**
   
   Use ``--!`` for documentation comments:
   
   .. code-block:: vhdl
   
      --! @brief Brief description
      --! @details Detailed description
      entity my_entity is
          generic (
              WIDTH : integer := 8  --! Parameter description
          );
          port (
              clk : in std_logic  --! Clock input
          );
      end my_entity;

2. **Organize by Hierarchy**
   
   Document from top-level down:
   
   - Top-level entity
   - Major subsystems
   - Individual components
   - Packages and types

3. **Include Diagrams**
   
   Visual representations help understanding:
   
   .. code-block:: rst
   
      .. vhdl:diagram:: top
         :show-hierarchy:

4. **Document Interfaces**
   
   Clearly describe all ports and generics:
   
   .. code-block:: rst
   
      .. vhdl:port-table:: entity_name
         :show-all:

5. **Provide Examples**
   
   Show how to instantiate components:
   
   .. code-block:: rst
   
      .. code-block:: vhdl
      
         u_instance : entity work.my_entity
             generic map (...)
             port map (...);

6. **Link Related Components**
   
   Use cross-references:
   
   .. code-block:: rst
   
      The :vhdl:entity:`alu` uses types from :vhdl:pkg:`types_pkg`.

Common Patterns
---------------

Module Template
~~~~~~~~~~~~~~~

.. code-block:: rst

   {Module Name}
   =============
   
   Overview
   --------
   
   Brief description of the module.
   
   Entity
   ------
   
   .. vhdl:autoentity:: {entity_name}
   
   Ports
   -----
   
   .. vhdl:port-table:: {entity_name}
   
   Generics
   --------
   
   .. vhdl:generic-table:: {entity_name}
   
   Architecture
   ------------
   
   Description of the implementation.
   
   .. vhdl:diagram:: {entity_name}
   
   Usage Example
   -------------
   
   .. code-block:: vhdl
   
      -- Instantiation example

Package Template
~~~~~~~~~~~~~~~~

.. code-block:: rst

   {Package Name}
   ==============
   
   Overview
   --------
   
   Package description.
   
   .. vhdl:autopackage:: {package_name}
   
   Constants
   ---------
   
   .. vhdl:constant-list:: {package_name}
   
   Types
   -----
   
   .. vhdl:type-list:: {package_name}
   
   Functions
   ---------
   
   .. vhdl:function-list:: {package_name}

Troubleshooting
---------------

VHDL Files Not Found
~~~~~~~~~~~~~~~~~~~~~

**Solution:**

Check ``vhdl_source_path`` in ``conf.py``:

.. code-block:: python

   vhdl_source_path = ['../hdl/src']  # Relative to conf.py

Syntax Errors
~~~~~~~~~~~~~

**Solution:**

Ensure VHDL code compiles:

.. code-block:: bash

   # Test with GHDL or other simulator
   ghdl -a counter.vhd

Diagrams Not Generating
~~~~~~~~~~~~~~~~~~~~~~~~

**Solution:**

Enable diagram generation:

.. code-block:: python

   vhdl_generate_diagrams = True
   vhdl_diagram_format = 'svg'

Next Steps
----------

1. Set up VHDL source paths
2. Add documentation comments to your VHDL code
3. Create RST files for each entity
4. Generate diagrams and port tables
5. Integrate into your FPGA workflow


Practical Examples
------------------

This page demonstrates the **sphinx-vhdl** extension which provides VHDL (VHSIC Hardware Description Language) domain support for documenting hardware designs.


Configuration
-------------

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_vhdl',
       # ... other extensions
   ]
   
   # VHDL source directory
   vhdl_source_path = ['hardware/src']
   
   # Autodoc options
   vhdl_autodoc_options = {
       'members': True,
       'show-inheritance': True
   }

Basic VHDL Documentation
------------------------

Entity Documentation
~~~~~~~~~~~~~~~~~~~~

**VHDL Source** (``counter.vhdl``):

.. code-block:: vhdl

   -- Simple counter module
   -- Author: Hardware Team
   -- Date: 2026-01-26
   
   library IEEE;
   use IEEE.STD_LOGIC_1164.ALL;
   use IEEE.NUMERIC_STD.ALL;
   
   --! 8-bit up counter with enable and reset
   --!
   --! This entity implements a synchronous counter with:
   --! * Asynchronous reset
   --! * Synchronous enable
   --! * Configurable maximum count
   --!
   --! @param CLK       System clock input
   --! @param RESET     Asynchronous reset (active high)
   --! @param ENABLE    Counter enable signal
   --! @param COUNT_OUT Current count value
   --! @param OVERFLOW  High when counter reaches max value
   
   entity counter is
       generic (
           MAX_COUNT : integer := 255  --! Maximum count value
       );
       port (
           CLK       : in  std_logic;  --! Clock input
           RESET     : in  std_logic;  --! Reset input
           ENABLE    : in  std_logic;  --! Enable input
           COUNT_OUT : out std_logic_vector(7 downto 0); --! Count output
           OVERFLOW  : out std_logic   --! Overflow flag
       );
   end counter;

**Sphinx Documentation** (``hardware.rst``):

.. code-block:: rst

   Counter Module
   ==============
   
   .. vhdl:entity:: counter
      :file: hardware/src/counter.vhdl
   
   The counter module provides an 8-bit synchronous counter.
   
   Ports
   -----
   
   .. vhdl:port:: CLK
      :direction: in
      :type: std_logic
      
      System clock input. Counter increments on rising edge.
   
   .. vhdl:port:: RESET
      :direction: in
      :type: std_logic
      
      Asynchronous active-high reset.
   
   .. vhdl:port:: ENABLE
      :direction: in
      :type: std_logic
      
      Synchronous enable. Counter only increments when high.
   
   Generics
   --------
   
   .. vhdl:generic:: MAX_COUNT
      :type: integer
      :default: 255
      
      Maximum count value before overflow.

Architecture Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: vhdl

   --! RTL implementation of counter
   --!
   --! Uses a single process with synchronous logic.
   --! Overflow detection included.
   
   architecture rtl of counter is
       signal count_reg : unsigned(7 downto 0);  --! Internal counter register
   begin
   
       --! Main counter process
       --!
       --! Implements synchronous counter with:
       --! * Rising edge triggered
       --! * Asynchronous reset
       --! * Overflow detection
       
       counter_proc: process(CLK, RESET)
       begin
           if RESET = '1' then
               count_reg <= (others => '0');
           elsif rising_edge(CLK) then
               if ENABLE = '1' then
                   if count_reg = MAX_COUNT then
                       count_reg <= (others => '0');
                   else
                       count_reg <= count_reg + 1;
                   end if;
               end if;
           end if;
       end process counter_proc;
       
       -- Output assignments
       COUNT_OUT <= std_logic_vector(count_reg);
       OVERFLOW  <= '1' when count_reg = MAX_COUNT else '0';
       
   end rtl;

**Documentation**:

.. code-block:: rst

   .. vhdl:architecture:: rtl
      :entity: counter
   
   RTL implementation using a single synchronous process.

Advanced Examples
-----------------

Component Documentation
~~~~~~~~~~~~~~~~~~~~~~~

**VHDL Component**:

.. code-block:: vhdl

   --! UART Transmitter
   --! Sends data serially with configurable baud rate
   
   component uart_tx is
       generic (
           CLK_FREQ  : integer := 50000000; --! Clock frequency (Hz)
           BAUD_RATE : integer := 115200    --! Baud rate (bps)
       );
       port (
           clk       : in  std_logic;
           reset     : in  std_logic;
           tx_start  : in  std_logic;
           tx_data   : in  std_logic_vector(7 downto 0);
           tx_busy   : out std_logic;
           tx_done   : out std_logic;
           tx_serial : out std_logic
       );
   end component;

**Documentation**:

.. code-block:: rst

   UART Transmitter
   ================
   
   .. vhdl:component:: uart_tx
   
   Serial UART transmitter with configurable baud rate.
   
   Generic Parameters
   ------------------
   
   .. vhdl:generic:: CLK_FREQ
      :type: integer
      :default: 50000000
      
      System clock frequency in Hz.
   
   .. vhdl:generic:: BAUD_RATE
      :type: integer
      :default: 115200
      
      Serial baud rate in bits per second.
   
   Timing Diagram
   --------------
   
   .. code-block:: text
   
       clk      __|‾|_|‾|_|‾|_|‾|_|‾|_|‾|_|‾|_|‾|_
       tx_start ___|‾‾‾‾|_____________________
       tx_busy  ______|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|_______
       tx_serial ‾‾‾‾|_|‾|_|‾|_|‾|_|‾|_|‾‾‾‾‾‾
                    START D0 D1 D2...D7 STOP

Package Documentation
~~~~~~~~~~~~~~~~~~~~~

**VHDL Package**:

.. code-block:: vhdl

   --! Utility functions package
   --! Provides common hardware functions
   
   package utils is
   
       --! Calculate log base 2 (ceiling)
       --! @param n Input value
       --! @return Minimum bits needed to represent n
       function clog2(n : positive) return natural;
       
       --! Reverse bit order
       --! @param vec Input vector
       --! @return Reversed vector
       function reverse_vector(
           vec : std_logic_vector
       ) return std_logic_vector;
       
       --! Check if value is power of 2
       --! @param n Value to check
       --! @return True if power of 2
       function is_power_of_2(n : natural) return boolean;
       
   end package utils;

**Documentation**:

.. code-block:: rst

   Utility Functions
   =================
   
   .. vhdl:package:: utils
   
   Common hardware utility functions.
   
   Functions
   ---------
   
   .. vhdl:function:: clog2
      :param n: Input value (positive)
      :returns: Minimum bits needed (natural)
      
      Calculates ceiling of log base 2.
      
      Example:
      
      .. code-block:: vhdl
      
         constant ADDR_BITS : natural := clog2(1024); -- Returns 10

Signal Documentation
~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Internal Signals
   ================
   
   .. vhdl:signal:: state_reg
      :type: state_type
      
      Current FSM state register.
   
   .. vhdl:signal:: data_buffer
      :type: std_logic_vector(31 downto 0)
      
      32-bit data buffer for FIFO.
   
   .. vhdl:signal:: write_enable
      :type: std_logic
      
      Internal write enable signal.

Complete Module Example
-----------------------

**Full VHDL Module with Documentation**:

.. code-block:: rst

   SPI Master Controller
   =====================
   
   .. vhdl:entity:: spi_master
      :file: hardware/spi/spi_master.vhdl
   
   Overview
   --------
   
   Configurable SPI master controller supporting:
   
   * Modes 0-3
   * Configurable clock divider
   * Variable data width (1-32 bits)
   * Full-duplex operation
   
   Block Diagram
   -------------
   
   .. code-block:: text
   
       ┌─────────────────────────────────────┐
       │         SPI Master                  │
       │                                     │
       │  ┌──────────┐      ┌────────────┐  │
       │  │  Clock   │──────▶   Shift    │  │
       │  │ Divider  │      │  Register  │  │
       │  └──────────┘      └────────────┘  │
       │       │                  │          │
       │       ▼                  ▼          │
       │  ┌──────────┐      ┌────────────┐  │
       │  │   FSM    │◀─────│  Control   │  │
       │  └──────────┘      └────────────┘  │
       └─────────────────────────────────────┘
   
   Ports
   -----
   
   .. list-table::
      :header-rows: 1
      :widths: 20 10 15 55
   
      * - Port
        - Dir
        - Type
        - Description
      * - sclk
        - out
        - std_logic
        - SPI clock output
      * - mosi
        - out
        - std_logic
        - Master out, slave in
      * - miso
        - in
        - std_logic
        - Master in, slave out
      * - ss_n
        - out
        - std_logic
        - Slave select (active low)
   
   Timing Specifications
   ---------------------
   
   .. list-table::
      :header-rows: 1
   
      * - Parameter
        - Min
        - Typ
        - Max
        - Unit
      * - Clock Frequency
        - 1
        - \-
        - 50
        - MHz
      * - Setup Time
        - 5
        - \-
        - \-
        - ns
      * - Hold Time
        - 5
        - \-
        - \-
        - ns

Cross-References
----------------

.. code-block:: rst

   The :vhdl:entity:`counter` module connects to :vhdl:entity:`uart_tx`
   using the :vhdl:signal:`data_bus`.
   
   See :vhdl:function:`clog2` for address width calculation.
   
   Configuration uses :vhdl:generic:`MAX_COUNT` parameter.

Configuration Options
---------------------

.. code-block:: python

   # conf.py
   
   # VHDL source paths
   vhdl_source_path = [
       'hardware/rtl',
       'hardware/components',
       'hardware/testbenches'
   ]
   
   # Include private signals
   vhdl_show_private = False
   
   # Generate hierarchy diagrams
   vhdl_generate_diagrams = True
   
   # Diagram output format
   vhdl_diagram_format = 'svg'
   
   # Cross-reference format
   vhdl_ref_format = 'detailed'

Use Cases
---------

1. **FPGA Design Documentation**
   
   - RTL module descriptions
   - Interface specifications
   - Timing constraints

2. **IP Core Libraries**
   
   - Reusable component docs
   - Integration guides
   - Parameter configuration

3. **Design Reviews**
   
   - Architecture overviews
   - Signal flow diagrams
   - Port specifications

Learn More
----------

For complete VHDL documentation features, see:

- :doc:`../tutorials/packages/sphinx-vhdl` - Full tutorial
- `VHDL Language Reference <https://www.eda.org/vhdl-200x/>`_ - VHDL standard
- `Sphinx Domains <https://www.sphinx-doc.org/en/master/usage/domains/>`_ - Domain system

Additional Resources
--------------------

- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- :doc:`../doxygen-usage` - Alternative for hardware docs
- `VHDL Standard <https://standards.ieee.org/>`_
- `Sphinx Documentation <https://www.sphinx-doc.org/>`_
