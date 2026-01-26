Graphviz Examples
=================

This page demonstrates various Graphviz diagrams you can create in Sphinx.

Simple Directed Graph
---------------------

.. graphviz::

   digraph {
       "Start" -> "Process" -> "End";
   }

**Code:**

.. code-block:: rst

   .. graphviz::

      digraph {
          "Start" -> "Process" -> "End";
      }

Flowchart
---------

.. graphviz::

   digraph flowchart {
       rankdir=TB;
       node [shape=box, style=rounded];
       
       start [label="Start", shape=ellipse];
       input [label="Get Input"];
       process [label="Process Data"];
       decision [label="Valid?", shape=diamond];
       output [label="Display Result"];
       error [label="Show Error"];
       end [label="End", shape=ellipse];
       
       start -> input;
       input -> process;
       process -> decision;
       decision -> output [label="Yes"];
       decision -> error [label="No"];
       output -> end;
       error -> end;
   }

**Code:**

.. code-block:: rst

   .. graphviz::

      digraph flowchart {
          rankdir=TB;
          node [shape=box, style=rounded];
          
          start [label="Start", shape=ellipse];
          input [label="Get Input"];
          process [label="Process Data"];
          decision [label="Valid?", shape=diamond];
          output [label="Display Result"];
          error [label="Show Error"];
          end [label="End", shape=ellipse];
          
          start -> input -> process -> decision;
          decision -> output [label="Yes"];
          decision -> error [label="No"];
          output -> end;
          error -> end;
      }

Class Diagram
-------------

.. graphviz::

   digraph classes {
       rankdir=BT;
       node [shape=record];
       
       Animal [label="{Animal|+ name: str\l+ age: int\l|+ speak(): void\l+ move(): void\l}"];
       Dog [label="{Dog|+ breed: str\l|+ bark(): void\l+ fetch(): void\l}"];
       Cat [label="{Cat|+ color: str\l|+ meow(): void\l+ scratch(): void\l}"];
       
       Dog -> Animal [arrowhead=empty];
       Cat -> Animal [arrowhead=empty];
   }

**Code:**

.. code-block:: rst

   .. graphviz::

      digraph classes {
          rankdir=BT;
          node [shape=record];
          
          Animal [label="{Animal|+ name\l+ age\l|+ speak()\l+ move()\l}"];
          Dog [label="{Dog|+ breed\l|+ bark()\l}"];
          Cat [label="{Cat|+ color\l|+ meow()\l}"];
          
          Dog -> Animal [arrowhead=empty];
          Cat -> Animal [arrowhead=empty];
      }

System Architecture
-------------------

.. graphviz::

   digraph architecture {
       rankdir=LR;
       node [shape=box3d, style=filled, fillcolor=lightblue];
       
       client [label="Web Browser", fillcolor=lightgreen];
       lb [label="Load Balancer", fillcolor=lightyellow];
       web1 [label="Web Server 1"];
       web2 [label="Web Server 2"];
       app [label="Application Server", fillcolor=lightpink];
       db [label="Database", shape=cylinder, fillcolor=lightgray];
       cache [label="Redis Cache", shape=cylinder, fillcolor=orange];
       
       client -> lb;
       lb -> web1;
       lb -> web2;
       web1 -> app;
       web2 -> app;
       app -> db;
       app -> cache;
   }

State Machine
-------------

.. graphviz::

   digraph states {
       rankdir=LR;
       node [shape=circle, style=filled, fillcolor=lightblue];
       
       idle [fillcolor=lightgreen];
       running [fillcolor=yellow];
       paused [fillcolor=orange];
       stopped [fillcolor=red];
       
       idle -> running [label="start"];
       running -> paused [label="pause"];
       paused -> running [label="resume"];
       running -> stopped [label="stop"];
       paused -> stopped [label="stop"];
       stopped -> idle [label="reset"];
   }

Network Topology
----------------

.. graphviz::

   graph network {
       node [shape=box, style=filled, fillcolor=lightblue];
       
       router [label="Router", shape=diamond, fillcolor=yellow];
       switch1 [label="Switch 1", fillcolor=lightgreen];
       switch2 [label="Switch 2", fillcolor=lightgreen];
       
       pc1 [label="PC 1"];
       pc2 [label="PC 2"];
       pc3 [label="PC 3"];
       pc4 [label="PC 4"];
       server [label="Server", fillcolor=orange];
       
       router -- switch1;
       router -- switch2;
       switch1 -- pc1;
       switch1 -- pc2;
       switch2 -- pc3;
       switch2 -- pc4;
       router -- server;
   }

Decision Tree
-------------

.. graphviz::

   digraph tree {
       node [shape=box];
       
       root [label="Age >= 18?", shape=diamond];
       q1 [label="Has License?", shape=diamond];
       q2 [label="Needs Training?", shape=diamond];
       
       allow [label="Allow Driving", style=filled, fillcolor=green];
       deny [label="Deny Driving", style=filled, fillcolor=red];
       train [label="Provide Training", style=filled, fillcolor=yellow];
       
       root -> deny [label="No"];
       root -> q1 [label="Yes"];
       q1 -> deny [label="No"];
       q1 -> allow [label="Yes"];
   }

Dependency Graph
----------------

.. graphviz::

   digraph dependencies {
       rankdir=LR;
       node [shape=box, style="rounded,filled", fillcolor=lightblue];
       
       main [fillcolor=lightgreen];
       auth [label="Authentication"];
       db [label="Database"];
       api [label="API Client"];
       logger [label="Logger"];
       config [label="Configuration"];
       
       main -> auth;
       main -> db;
       main -> api;
       auth -> db;
       auth -> logger;
       api -> logger;
       api -> config;
       db -> config;
   }

Custom Colors and Styles
------------------------

.. graphviz::

   digraph styled {
       node [fontname="Helvetica"];
       edge [fontname="Helvetica"];
       
       a [label="Node A", shape=box, style="filled,rounded", 
          fillcolor="#FF6B6B", fontcolor=white];
       b [label="Node B", shape=ellipse, style=filled, 
          fillcolor="#4ECDC4", fontcolor=white];
       c [label="Node C", shape=polygon, sides=6, style=filled,
          fillcolor="#45B7D1", fontcolor=white];
       d [label="Node D", shape=star, style=filled,
          fillcolor="#F7DC6F", fontcolor=black];
       
       a -> b [color="#FF6B6B", penwidth=2];
       b -> c [color="#4ECDC4", penwidth=2, style=dashed];
       c -> d [color="#45B7D1", penwidth=2, style=dotted];
       d -> a [color="#F7DC6F", penwidth=2];
   }

Using External DOT Files
------------------------

You can also load diagrams from external files:

.. code-block:: rst

   .. graphviz:: diagrams/architecture.dot

Configuration Options
---------------------

In ``conf.py``:

.. code-block:: python

   # Graphviz output format
   graphviz_output_format = 'svg'  # or 'png'
   
   # Graphviz dot command
   graphviz_dot = 'dot'
   
   # Additional dot options
   graphviz_dot_args = ['-Gfontname=Helvetica', '-Nfontname=Helvetica']

Resources
---------

* `Graphviz Documentation <https://graphviz.org/documentation/>`_
* `DOT Language Guide <https://graphviz.org/doc/info/lang.html>`_
* `Node Shapes <https://graphviz.org/doc/info/shapes.html>`_
* `Color Names <https://graphviz.org/doc/info/colors.html>`_
