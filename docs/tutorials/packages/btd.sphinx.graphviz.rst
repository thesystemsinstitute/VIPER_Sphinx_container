BTD Sphinx Graphviz Tutorial
============================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/btd.sphinx.graphviz/>`_
   - `API Documentation <../../pdoc/btd_sphinx_graphviz/index.html>`_
   - `Manual <https://github.com/berteh/btd.sphinx.graphviz>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use btd.sphinx.graphviz for advanced Graphviz integration in Sphinx documentation.

What is BTD Sphinx Graphviz?
-----------------------------

btd.sphinx.graphviz is an enhanced Sphinx extension for Graphviz that provides:

- Advanced Graphviz diagram integration
- Custom graph attributes
- Multiple output formats
- Interactive diagrams
- Graph styling options
- Layout algorithms
- Subgraph support
- Edge and node customization
- DOT language syntax highlighting
- Image map generation
- SVG output with links

This extends the standard ``sphinx.ext.graphviz`` with additional features and better control.

Installation
------------

btd.sphinx.graphviz is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm viper-sphinx:latest python -c "import btd.sphinx.graphviz; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'btd.sphinx.graphviz',
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['btd.sphinx.graphviz']
   
   # Graphviz configuration
   graphviz_dot = '/usr/bin/dot'
   graphviz_dot_args = ['-Gdpi=300']
   graphviz_output_format = 'svg'  # png, svg, pdf
   
   # Default graph attributes
   graphviz_graph_attrs = {
       'rankdir': 'LR',
       'bgcolor': 'transparent',
       'fontname': 'Arial',
       'fontsize': '12',
   }
   
   graphviz_node_attrs = {
       'shape': 'box',
       'style': 'rounded,filled',
       'fillcolor': '#E8F4F8',
       'fontname': 'Arial',
   }
   
   graphviz_edge_attrs = {
       'fontname': 'Arial',
       'fontsize': '10',
       'color': '#666666',
   }
   
   # Interactive features
   graphviz_create_maps = True  # Create image maps
   graphviz_clickable = True
   
   # Cache settings
   graphviz_cache_dir = '_build/graphviz'


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Basic Setup
~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'btd.sphinx.graphviz',
   ]
   
   graphviz_output_format = 'svg'
   graphviz_dot_args = ['-Gdpi=300']

Advanced Options
~~~~~~~~~~~~~~~~

.. code-block:: python

   graphviz_default_options = {
       'layout': 'dot',
       'optimize': True,
       'rankdir': 'TB',
   }

Custom Themes
~~~~~~~~~~~~~

.. code-block:: python

   graphviz_themes = {
       'modern': {
           'node_color': '#4A90E2',
           'edge_color': '#333333',
           'bg_color': '#FFFFFF',
       },
   }

Basic Usage
-----------

Simple Graph
~~~~~~~~~~~~

.. code-block:: rst

   .. graphviz::
      
      digraph G {
          A -> B -> C;
          A -> C;
      }

With Caption
~~~~~~~~~~~~

.. code-block:: rst

   .. graphviz::
      :caption: Data Flow Diagram
      :alt: Shows data flow from A to C
      
      digraph DataFlow {
          A [label="Input"];
          B [label="Process"];
          C [label="Output"];
          
          A -> B -> C;
      }

Custom Alignment
~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. graphviz::
      :align: center
      :name: my_graph
      
      digraph {
          node [shape=circle];
          A -> B -> C;
      }

External DOT File
~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. graphviz:: architecture.dot

   System Architecture
   ===================
   
   Component Diagram
   -----------------
   
   .. graphviz::
      :caption: System Components
      
      digraph Components {
          rankdir=TB;
          node [shape=component, style=filled, fillcolor=lightblue];
          
          // Define components
          ui [label="User Interface"];
          api [label="API Gateway"];
          auth [label="Auth Service"];
          db [label="Database"];
          cache [label="Cache"];
          
          // Define relationships
          ui -> api [label="HTTP/REST"];
          api -> auth [label="Verify Token"];
          api -> db [label="Query"];
          api -> cache [label="Get/Set"];
          
          // Subgraph for external services
          subgraph cluster_external {
              label="External Services";
              style=dashed;
              
              email [label="Email Service"];
              payment [label="Payment Gateway"];
          }
          
          api -> email [label="Send Email"];
          api -> payment [label="Process Payment"];
      }
   
   Data Flow
   ---------
   
   .. graphviz::
      :caption: Request Processing Flow
      
      digraph DataFlow {
          rankdir=LR;
          node [shape=box, style="rounded,filled", fillcolor=wheat];
          
          start [shape=ellipse, label="Start"];
          end [shape=ellipse, label="End"];
          
          start -> validate [label="Request"];
          validate -> {auth, cache} [label="Check"];
          
          auth -> process [label="Authenticated"];
          cache -> process [label="Cache Miss"];
          cache -> end [label="Cache Hit", style=dashed];
          
          process -> database [label="Query"];
          database -> transform [label="Raw Data"];
          transform -> cache [label="Update"];
          transform -> end [label="Response"];
      }

Example 2: Class Hierarchy
~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/api/classes.rst``:

.. code-block:: rst

   Class Hierarchy
   ===============
   
   .. graphviz::
      :caption: Inheritance Diagram
      
      digraph Classes {
          rankdir=BT;
          node [shape=record, style=filled, fillcolor=lightgray];
          
          // Base classes
          BaseClass [label="{BaseClass|+ method1()\l+ method2()\l}"];
          
          // Derived classes
          ClassA [label="{ClassA|+ method1()\l+ methodA()\l}"];
          ClassB [label="{ClassB|+ method1()\l+ methodB()\l}"];
          ClassC [label="{ClassC|+ method2()\l+ methodC()\l}"];
          
          // Inheritance relationships
          ClassA -> BaseClass [arrowhead=empty];
          ClassB -> BaseClass [arrowhead=empty];
          ClassC -> ClassA [arrowhead=empty];
      }
   
   Interface Implementation
   ------------------------
   
   .. graphviz::
      
      digraph Interfaces {
          rankdir=BT;
          node [shape=record];
          
          // Interfaces (italicized)
          IReadable [label="{«interface»\nIReadable|+ read()\l}", 
                     style=filled, fillcolor=lightyellow];
          IWritable [label="{«interface»\nIWritable|+ write()\l}", 
                     style=filled, fillcolor=lightyellow];
          
          // Classes
          File [label="{File|+ read()\l+ write()\l+ close()\l}",
                style=filled, fillcolor=lightblue];
          Stream [label="{Stream|+ read()\l+ write()\l}",
                  style=filled, fillcolor=lightblue];
          
          // Implementation relationships
          File -> IReadable [style=dashed, arrowhead=empty];
          File -> IWritable [style=dashed, arrowhead=empty];
          Stream -> IReadable [style=dashed, arrowhead=empty];
          Stream -> IWritable [style=dashed, arrowhead=empty];
      }

Example 3: State Machine
~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/design/states.rst``:

.. code-block:: rst

   State Machine
   =============
   
   Order Processing States
   -----------------------
   
   .. graphviz::
      :caption: Order State Transitions
      
      digraph OrderStates {
          rankdir=LR;
          node [shape=circle, style=filled];
          
          // States
          start [shape=point];
          created [fillcolor=lightblue, label="Created"];
          pending [fillcolor=yellow, label="Pending"];
          processing [fillcolor=orange, label="Processing"];
          completed [fillcolor=lightgreen, label="Completed"];
          cancelled [fillcolor=red, label="Cancelled"];
          end [shape=doublecircle, fillcolor=gray, label="End"];
          
          // Transitions
          start -> created [label="new order"];
          created -> pending [label="payment pending"];
          pending -> processing [label="payment confirmed"];
          processing -> completed [label="shipped"];
          completed -> end;
          
          // Cancellation paths
          created -> cancelled [label="cancel", color=red];
          pending -> cancelled [label="payment failed", color=red];
          processing -> cancelled [label="out of stock", color=red];
          cancelled -> end [color=red];
      }
   
   Connection States
   -----------------
   
   .. graphviz::
      
      digraph ConnectionStates {
          rankdir=TB;
          node [shape=box, style="rounded,filled"];
          
          disconnected [fillcolor=lightgray, label="Disconnected"];
          connecting [fillcolor=yellow, label="Connecting"];
          connected [fillcolor=lightgreen, label="Connected"];
          error [fillcolor=red, label="Error"];
          
          disconnected -> connecting [label="connect()"];
          connecting -> connected [label="success"];
          connecting -> error [label="timeout"];
          connected -> disconnected [label="disconnect()"];
          connected -> error [label="connection lost"];
          error -> disconnected [label="reset()"];
          error -> connecting [label="retry()"];
      }

Example 4: Database Schema
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create ``docs/_static/schema.dot``:

.. code-block:: dot

   digraph DatabaseSchema {
       rankdir=LR;
       node [shape=record];
       
       // Tables
       users [label="{users|id: INTEGER\lpk\l|username: VARCHAR\lemail: VARCHAR\l}"];
       posts [label="{posts|id: INTEGER\lpk\l|user_id: INTEGER\lfk\l|title: VARCHAR\lcontent: TEXT\l}"];
       comments [label="{comments|id: INTEGER\lpk\l|post_id: INTEGER\lfk\l|user_id: INTEGER\lfk\l|text: TEXT\l}"];
       tags [label="{tags|id: INTEGER\lpk\l|name: VARCHAR\l}"];
       post_tags [label="{post_tags|post_id: INTEGER\lfk\l|tag_id: INTEGER\lfk\l}"];
       
       // Relationships
       posts -> users [label="user_id", dir=back];
       comments -> posts [label="post_id", dir=back];
       comments -> users [label="user_id", dir=back];
       post_tags -> posts [label="post_id", dir=back];
       post_tags -> tags [label="tag_id", dir=back];
   }

Reference in ``docs/database/schema.rst``:

.. code-block:: rst

   Database Schema
   ===============
   
   .. graphviz:: ../_static/schema.dot
      :caption: Database Entity Relationship Diagram

Advanced Features
-----------------

Subgraphs and Clusters
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. graphviz::
      
      digraph G {
          subgraph cluster_0 {
              label="Frontend";
              style=filled;
              color=lightgrey;
              
              a0 -> a1 -> a2;
          }
          
          subgraph cluster_1 {
              label="Backend";
              style=filled;
              color=lightblue;
              
              b0 -> b1 -> b2;
          }
          
          a2 -> b0;
      }

Custom Node Shapes
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. graphviz::
      
      digraph Shapes {
          // Different shapes
          box [shape=box, label="Box"];
          circle [shape=circle, label="Circle"];
          diamond [shape=diamond, label="Decision"];
          ellipse [shape=ellipse, label="Ellipse"];
          parallelogram [shape=parallelogram, label="Input/Output"];
          hexagon [shape=hexagon, label="Hexagon"];
          
          box -> circle -> diamond -> ellipse;
          diamond -> parallelogram -> hexagon;
      }

Edge Styles
~~~~~~~~~~~

.. code-block:: rst

   .. graphviz::
      
      digraph Edges {
          A -> B [label="normal"];
          A -> C [style=dashed, label="dashed"];
          A -> D [style=dotted, label="dotted"];
          A -> E [style=bold, label="bold"];
          A -> F [dir=both, label="bidirectional"];
          A -> G [color=red, label="colored"];
      }

Colors and Styling
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. graphviz::
      
      digraph Styled {
          node [style=filled];
          
          a [fillcolor=red, fontcolor=white, label="Red"];
          b [fillcolor="#00FF00", label="Green"];
          c [fillcolor="blue", fontcolor=white, label="Blue"];
          d [fillcolor="yellow", label="Yellow"];
          
          a -> b -> c -> d;
          d -> a [color="purple", penwidth=3.0];
      }

HTML-Like Labels
~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. graphviz::
      
      digraph HTMLLabels {
          node [shape=none];
          
          a [label=<
              <table border="0" cellborder="1" cellspacing="0">
                  <tr><td bgcolor="lightblue"><b>Header</b></td></tr>
                  <tr><td>Content</td></tr>
              </table>
          >];
          
          b [label=<
              <table border="1" cellborder="0">
                  <tr><td port="p1">Port 1</td></tr>
                  <tr><td port="p2">Port 2</td></tr>
              </table>
          >];
          
          a -> b:p1;
      }

Layout Algorithms
~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Different layouts:
   
   .. graphviz::
      :layout: dot
      
      digraph { A -> B -> C; }
   
   .. graphviz::
      :layout: neato
      
      graph { A -- B -- C -- A; }
   
   .. graphviz::
      :layout: circo
      
      graph { A -- B -- C -- D -- A; }

Docker Integration
------------------

Build with Graphviz
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     viper-sphinx:latest \
     sphinx-build -b html /project/docs /project/docs/_build/html

Generate DOT Files
~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     viper-sphinx:latest \
     dot -Tpng input.dot -o output.png

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Build Docs with Graphviz
   
   on: [push]
   
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Validate DOT files
           run: |
             docker run --rm -v $(pwd):/project \
               viper-sphinx:latest \
               sh -c "for f in /project/docs/_static/*.dot; do \
                        dot -Tpng \$f -o /dev/null || exit 1; \
                      done"
         
         - name: Build Documentation
           run: |
             docker run --rm -v $(pwd):/project \
               viper-sphinx:latest \
               sphinx-build -b html /project/docs /project/docs/_build/html

Best Practices
--------------

1. **Use Meaningful Labels**
   
   Clear, descriptive node names

2. **Choose Appropriate Layout**
   
   - ``dot``: Hierarchical
   - ``neato``: Spring model
   - ``circo``: Circular
   - ``fdp``: Force-directed

3. **Consistent Styling**
   
   Define styles in conf.py

4. **Subgraphs for Organization**
   
   Group related nodes

5. **External Files for Complex Graphs**
   
   Keep RST files clean

6. **Comments in DOT Files**
   
   Document complex relationships

Common Patterns
---------------

Flowchart Template
~~~~~~~~~~~~~~~~~~

.. code-block:: dot

   digraph Flowchart {
       rankdir=TB;
       node [shape=box, style="rounded,filled", fillcolor=lightblue];
       
       start [shape=ellipse, label="Start"];
       end [shape=ellipse, label="End"];
       decision [shape=diamond, label="Condition?"];
       
       start -> process1;
       process1 -> decision;
       decision -> process2 [label="Yes"];
       decision -> process3 [label="No"];
       process2 -> end;
       process3 -> end;
   }

Troubleshooting
---------------

Graphviz Not Found
~~~~~~~~~~~~~~~~~~

**Solution:**

Install Graphviz:

.. code-block:: bash

   # Alpine
   apk add --no-cache graphviz
   
   # Ubuntu
   apt-get install graphviz

Syntax Errors
~~~~~~~~~~~~~

**Solution:**

Validate DOT syntax:

.. code-block:: bash

   dot -Tpng file.dot -o /dev/null

Image Not Generated
~~~~~~~~~~~~~~~~~~~

**Solution:**

Check output format:

.. code-block:: python

   graphviz_output_format = 'svg'  # or 'png'

Layout Issues
~~~~~~~~~~~~~

**Solution:**

Try different layout engine:

.. code-block:: rst

   .. graphviz::
      :layout: neato
      
      graph { ... }


Basic Graphs
------------

Simple Graph
~~~~~~~~~~~~

.. graphviz::

   digraph simple {
       A -> B;
       B -> C;
       C -> A;
   }

Styled Nodes
~~~~~~~~~~~~

.. graphviz::

   digraph styled {
       node [shape=box, style=filled, fillcolor=lightblue];
       
       Start [fillcolor=green];
       Process [fillcolor=yellow];
       End [fillcolor=red];
       
       Start -> Process -> End;
   }

Clusters
~~~~~~~~

.. graphviz::

   digraph clusters {
       subgraph cluster_0 {
           label="Cluster A";
           a0 -> a1 -> a2;
       }
       
       subgraph cluster_1 {
           label="Cluster B";
           b0 -> b1 -> b2;
       }
       
       a2 -> b0;
   }

Advanced Features
-----------------

Auto Layout
~~~~~~~~~~~

.. graphviz::
   :layout: dot
   :optimize: true

   digraph auto {
       rankdir=LR;
       node [shape=circle];
       
       1 -> 2 -> 3;
       1 -> 4 -> 5;
       2 -> 6;
       3 -> 7;
   }

Custom Styles
~~~~~~~~~~~~~

.. graphviz::
   :style: modern

   digraph custom {
       graph [fontname="Arial", fontsize=12];
       node [fontname="Arial", fontsize=10];
       edge [fontname="Arial", fontsize=9];
       
       A [label="Start"];
       B [label="Process"];
       C [label="End"];
       
       A -> B [label="step 1"];
       B -> C [label="step 2"];
   }

Interactive Graphs
~~~~~~~~~~~~~~~~~~

.. graphviz::
   :interactive: true

   digraph interactive {
       A [href="page1.html", tooltip="Go to Page 1"];
       B [href="page2.html", tooltip="Go to Page 2"];
       C [href="page3.html", tooltip="Go to Page 3"];
       
       A -> B -> C;
   }

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'btd.sphinx.graphviz',
   ]
   
   graphviz_output_format = 'svg'
   graphviz_dot_args = ['-Gdpi=300']

Advanced Options
~~~~~~~~~~~~~~~~

.. code-block:: python

   graphviz_default_options = {
       'layout': 'dot',
       'optimize': True,
       'rankdir': 'TB',
   }

Custom Themes
~~~~~~~~~~~~~

.. code-block:: python

   graphviz_themes = {
       'modern': {
           'node_color': '#4A90E2',
           'edge_color': '#333333',
           'bg_color': '#FFFFFF',
       },
   }

Practical Examples
------------------

Data Flow
~~~~~~~~~

.. graphviz::

   digraph dataflow {
       rankdir=LR;
       node [shape=box, style=rounded];
       
       Input [shape=folder];
       Process1 [label="Validate"];
       Process2 [label="Transform"];
       Process3 [label="Aggregate"];
       Output [shape=folder];
       
       Input -> Process1 -> Process2 -> Process3 -> Output;
   }

State Machine
~~~~~~~~~~~~~

.. graphviz::

   digraph state {
       node [shape=circle];
       start [shape=point];
       end [shape=doublecircle];
       
       start -> Idle;
       Idle -> Running [label="start"];
       Running -> Paused [label="pause"];
       Paused -> Running [label="resume"];
       Running -> end [label="stop"];
   }


Next Steps
----------

1. Create architecture diagrams
2. Document state machines
3. Visualize data flows
4. Generate class diagrams
5. Add database schemas

Additional Resources
--------------------

- :doc:`sphinx-diagrams` - Cloud architecture diagrams
- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `Graphviz Documentation <https://graphviz.org/documentation/>`_
- `DOT Language Guide <https://graphviz.org/doc/info/lang.html>`_
