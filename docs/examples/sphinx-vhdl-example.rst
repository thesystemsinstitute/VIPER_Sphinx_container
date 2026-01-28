Sphinx-VHDL Example
===================

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
