BTD.Sphinx.Graphviz Example
===========================

This page demonstrates the **btd.sphinx.graphviz** extension for enhanced Graphviz integration with additional features beyond the standard sphinxcontrib-graphviz.

.. contents:: Contents
   :local:
   :depth: 2

Overview
--------

The btd.sphinx.graphviz extension provides advanced Graphviz features including automatic layout optimization, custom node types, and enhanced styling options.

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

See Also
--------

- :doc:`../tutorials/packages/btd-sphinx-graphviz` - Complete tutorial
- Graphviz documentation: https://graphviz.org/
- GitHub repository: https://github.com/btd/sphinx-graphviz
