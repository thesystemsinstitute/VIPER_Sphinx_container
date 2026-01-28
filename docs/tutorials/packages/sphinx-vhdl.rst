Sphinx-VHDL Tutorial
====================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-vhdl/>`_
   - `API Documentation <../../pdoc/sphinx_vhdl/index.html>`_
   - `Manual <https://cesnet.github.io/sphinx-vhdl/>`_
   - :doc:`Working Example <../../examples/sphinx-vhdl-example>`


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

Additional Resources
--------------------

- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- :doc:`../doxygen-usage` - Alternative for hardware docs
- `VHDL Standard <https://standards.ieee.org/>`_
- `Sphinx Documentation <https://www.sphinx-doc.org/>`_
