Sphinx-Diagrams Example
=======================

This page demonstrates the **sphinx-diagrams** extension for creating diagrams using the Diagrams library for Python cloud architecture visualization.

.. contents:: Contents
   :local:
   :depth: 2

Overview
--------

The sphinx-diagrams extension integrates the Diagrams library to create cloud architecture diagrams, network diagrams, and system design visualizations.

Basic Diagrams
--------------

Simple Architecture
~~~~~~~~~~~~~~~~~~~

.. diagrams::
   :filename: simple-arch

   from diagrams import Diagram
   from diagrams.aws.compute import EC2
   from diagrams.aws.database import RDS
   from diagrams.aws.network import ELB
   
   with Diagram("Simple Web Service", show=False):
       ELB("lb") >> EC2("web") >> RDS("database")

Three-Tier Architecture
~~~~~~~~~~~~~~~~~~~~~~~

.. diagrams::
   :filename: three-tier

   from diagrams import Diagram, Cluster
   from diagrams.aws.compute import EC2
   from diagrams.aws.database import RDS
   from diagrams.aws.network import ELB
   
   with Diagram("Three Tier Architecture", show=False):
       lb = ELB("Load Balancer")
       
       with Cluster("Web Tier"):
           web_servers = [EC2("web1"), EC2("web2"), EC2("web3")]
       
       with Cluster("Database Tier"):
           db_master = RDS("master")
           db_slave = RDS("slave")
       
       lb >> web_servers >> db_master
       db_master - db_slave

AWS Architecture
----------------

Serverless
~~~~~~~~~~

.. diagrams::
   :filename: serverless

   from diagrams import Diagram
   from diagrams.aws.compute import Lambda
   from diagrams.aws.database import DynamoDB
   from diagrams.aws.network import APIGateway
   
   with Diagram("Serverless Architecture", show=False):
       api = APIGateway("API")
       func = Lambda("Function")
       db = DynamoDB("Database")
       
       api >> func >> db

Microservices
~~~~~~~~~~~~~

.. diagrams::
   :filename: microservices

   from diagrams import Diagram, Cluster
   from diagrams.aws.compute import ECS
   from diagrams.aws.database import RDS, ElastiCache
   from diagrams.aws.network import ELB
   
   with Diagram("Microservices", show=False):
       lb = ELB("Load Balancer")
       
       with Cluster("Services"):
           svc1 = ECS("user-service")
           svc2 = ECS("order-service")
           svc3 = ECS("payment-service")
       
       cache = ElastiCache("cache")
       db = RDS("database")
       
       lb >> [svc1, svc2, svc3]
       svc1 >> cache
       [svc1, svc2, svc3] >> db

Azure Diagrams
--------------

Web Application
~~~~~~~~~~~~~~~

.. diagrams::
   :filename: azure-web

   from diagrams import Diagram
   from diagrams.azure.compute import AppServices
   from diagrams.azure.database import SQLDatabases
   from diagrams.azure.storage import BlobStorage
   
   with Diagram("Azure Web App", show=False):
       app = AppServices("Web App")
       db = SQLDatabases("SQL Database")
       storage = BlobStorage("Blob Storage")
       
       app >> db
       app >> storage

GCP Diagrams
------------

Data Pipeline
~~~~~~~~~~~~~

.. diagrams::
   :filename: gcp-pipeline

   from diagrams import Diagram, Cluster
   from diagrams.gcp.analytics import BigQuery, Dataflow
   from diagrams.gcp.storage import Storage
   
   with Diagram("GCP Data Pipeline", show=False):
       source = Storage("Source Data")
       process = Dataflow("Processing")
       dest = BigQuery("Data Warehouse")
       
       source >> process >> dest

Kubernetes
----------

Cluster Architecture
~~~~~~~~~~~~~~~~~~~~

.. diagrams::
   :filename: k8s-cluster

   from diagrams import Diagram, Cluster
   from diagrams.k8s.compute import Pod, Deployment
   from diagrams.k8s.network import Service, Ingress
   
   with Diagram("Kubernetes Cluster", show=False):
       ing = Ingress("ingress")
       svc = Service("service")
       
       with Cluster("Deployment"):
           pods = [Pod("pod1"), Pod("pod2"), Pod("pod3")]
       
       ing >> svc >> pods

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_diagrams',
   ]
   
   diagrams_output_format = 'png'  # or 'svg'
   diagrams_output_dir = '_diagrams'

Advanced Options
~~~~~~~~~~~~~~~~

.. code-block:: python

   diagrams_default_options = {
       'direction': 'LR',  # Left to Right
       'show': False,
       'outformat': 'png',
   }

See Also
--------

- :doc:`../tutorials/packages/sphinx-diagrams` - Complete tutorial
- Diagrams library: https://diagrams.mingrammer.com/
- GitHub repository: https://github.com/sphinx-contrib/diagrams
