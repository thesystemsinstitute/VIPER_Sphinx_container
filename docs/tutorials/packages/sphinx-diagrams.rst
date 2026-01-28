Sphinx-Diagrams Tutorial
========================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-diagrams/>`_
   - `API Documentation <../../pdoc/sphinx_diagrams/index.html>`_
   - `Manual <https://sphinxcontrib-diagrams.readthedocs.io/>`_
   - :doc:`Working Example <../../examples/sphinx-diagrams-example>`


.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinx-diagrams to create cloud architecture diagrams, infrastructure diagrams, and system architecture visualizations using Python code.

What is Sphinx-Diagrams?
-------------------------

sphinx-diagrams integrates the Diagrams library with Sphinx to provide:

- Cloud architecture diagrams (AWS, Azure, GCP, Kubernetes)
- Infrastructure as code diagrams
- System architecture visualization
- Network topology diagrams
- On-premise infrastructure
- Data flow diagrams
- Microservices architecture
- Programming language logos and icons
- Container and orchestration diagrams

Uses Python code to define diagrams, making them version-controllable and easy to maintain.


The sphinx-diagrams extension integrates the Diagrams library to create cloud architecture diagrams, network diagrams, and system design visualizations.

Installation
------------

sphinx-diagrams is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import diagrams; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_diagrams',
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinx_diagrams']
   
   # Diagrams configuration
   diagrams_output_format = 'png'  # png, jpg, pdf, dot
   diagrams_output_dir = '_static/diagrams'
   diagrams_graphviz_dot = '/usr/bin/dot'
   
   # Rendering options
   diagrams_default_graph_attrs = {
       'fontsize': '45',
       'bgcolor': 'transparent',
   }
   
   diagrams_default_node_attrs = {
       'fontsize': '13',
       'height': '1.2',
   }
   
   diagrams_default_edge_attrs = {
       'fontsize': '10',
   }
   
   # Display options
   diagrams_cache_diagrams = True
   diagrams_include_source = True


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

Basic Usage
-----------

Simple Diagram Directive
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. diagrams::
      :filename: architecture
      
      from diagrams import Diagram
      from diagrams.aws.compute import EC2
      from diagrams.aws.database import RDS
      
      with Diagram("Simple Architecture"):
          EC2("Web Server") >> RDS("Database")

Inline Diagram
~~~~~~~~~~~~~~

.. code-block:: rst

   .. diagrams::
      
      from diagrams import Cluster, Diagram
      from diagrams.aws.network import ELB
      from diagrams.aws.compute import EC2
      
      with Diagram("Load Balanced Web"):
          lb = ELB("Load Balancer")
          lb >> [EC2("web1"), EC2("web2"), EC2("web3")]

Custom Filename
~~~~~~~~~~~~~~~

.. code-block:: rst

   .. diagrams::
      :filename: my-infrastructure
      :format: png
      
      from diagrams import Diagram
      # diagram code

   AWS Infrastructure
   ==================
   
   Our production infrastructure on AWS.
   
   Web Application Architecture
   -----------------------------
   
   .. diagrams::
      :filename: aws-web-app
      
      from diagrams import Diagram, Cluster
      from diagrams.aws.compute import EC2, ECS
      from diagrams.aws.database import RDS, ElastiCache
      from diagrams.aws.network import ELB, Route53
      from diagrams.aws.storage import S3
      
      with Diagram("Web Application", show=False):
          dns = Route53("DNS")
          lb = ELB("Load Balancer")
          
          with Cluster("Application"):
              app_servers = [
                  EC2("App 1"),
                  EC2("App 2"),
                  EC2("App 3")
              ]
          
          with Cluster("Database"):
              db_primary = RDS("Primary")
              db_replica = RDS("Replica")
              cache = ElastiCache("Redis")
          
          storage = S3("Static Files")
          
          dns >> lb >> app_servers
          app_servers >> db_primary
          db_primary >> db_replica
          app_servers >> cache
          app_servers >> storage
   
   Microservices Architecture
   ---------------------------
   
   .. diagrams::
      :filename: aws-microservices
      
      from diagrams import Diagram, Cluster
      from diagrams.aws.compute import EKS, Lambda
      from diagrams.aws.database import Dynamodb
      from diagrams.aws.integration import SQS, SNS
      from diagrams.aws.network import APIGateway
      
      with Diagram("Microservices on EKS", show=False):
          api = APIGateway("API Gateway")
          
          with Cluster("Kubernetes Cluster"):
              with Cluster("Services"):
                  svc1 = EKS("User Service")
                  svc2 = EKS("Order Service")
                  svc3 = EKS("Payment Service")
          
          queue = SQS("Queue")
          topic = SNS("Notifications")
          db = Dynamodb("DynamoDB")
          processor = Lambda("Event Processor")
          
          api >> [svc1, svc2, svc3]
          svc2 >> queue >> processor
          processor >> topic
          [svc1, svc2, svc3] >> db

Example 2: Kubernetes Deployment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/kubernetes/architecture.rst``:

.. code-block:: rst

   Kubernetes Architecture
   =======================
   
   Application Deployment
   ----------------------
   
   .. diagrams::
      :filename: k8s-deployment
      
      from diagrams import Diagram, Cluster
      from diagrams.k8s.network import Ingress, Service
      from diagrams.k8s.compute import Deployment, Pod
      from diagrams.k8s.storage import PV, PVC
      from diagrams.k8s.podconfig import ConfigMap, Secret
      
      with Diagram("Kubernetes Application", show=False, direction="TB"):
          ingress = Ingress("Ingress")
          
          with Cluster("Namespace: production"):
              svc = Service("Service")
              
              with Cluster("Deployment"):
                  pods = [
                      Pod("Pod 1"),
                      Pod("Pod 2"),
                      Pod("Pod 3")
                  ]
              
              config = ConfigMap("Config")
              secret = Secret("Secrets")
              
              pvc = PVC("Volume Claim")
              pv = PV("Volume")
          
          ingress >> svc >> pods
          pods >> [config, secret]
          pvc - pv
          pods >> pvc
   
   Complete Stack
   --------------
   
   .. diagrams::
      :filename: k8s-full-stack
      
      from diagrams import Diagram, Cluster
      from diagrams.k8s.clusterconfig import HPA
      from diagrams.k8s.compute import Deployment
      from diagrams.k8s.network import Service, Ingress
      from diagrams.onprem.database import PostgreSQL
      from diagrams.onprem.inmemory import Redis
      from diagrams.onprem.monitoring import Prometheus, Grafana
      
      with Diagram("Full Stack", show=False):
          ingress = Ingress("ingress")
          
          with Cluster("Application"):
              svc = Service("service")
              deployment = Deployment("deployment")
              hpa = HPA("autoscaler")
              
              deployment - hpa
          
          with Cluster("Data Layer"):
              db = PostgreSQL("postgres")
              cache = Redis("redis")
          
          with Cluster("Monitoring"):
              metrics = Prometheus("prometheus")
              dashboard = Grafana("grafana")
          
          ingress >> svc >> deployment
          deployment >> db
          deployment >> cache
          deployment >> metrics >> dashboard

Example 3: Data Pipeline
~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/data/pipeline.rst``:

.. code-block:: rst

   Data Processing Pipeline
   ========================
   
   ETL Pipeline
   ------------
   
   .. diagrams::
      :filename: data-pipeline
      
      from diagrams import Diagram, Cluster, Edge
      from diagrams.aws.analytics import Kinesis, EMR, Athena
      from diagrams.aws.storage import S3
      from diagrams.aws.integration import SQS
      from diagrams.aws.database import Redshift
      from diagrams.onprem.analytics import Spark
      
      with Diagram("Data Pipeline", show=False, direction="LR"):
          sources = [
              Kinesis("Stream 1"),
              Kinesis("Stream 2"),
              SQS("Queue")
          ]
          
          with Cluster("Processing"):
              raw = S3("Raw Data")
              emr = EMR("EMR Cluster")
              processed = S3("Processed")
          
          warehouse = Redshift("Data Warehouse")
          query = Athena("Query Engine")
          
          sources >> raw >> emr >> processed
          processed >> warehouse
          processed >> query
   
   Real-time Analytics
   -------------------
   
   .. diagrams::
      :filename: realtime-analytics
      
      from diagrams import Diagram, Cluster
      from diagrams.aws.analytics import KinesisDataStreams, KinesisDataFirehose
      from diagrams.aws.compute import Lambda
      from diagrams.aws.database import ElastiCache, DynamoDB
      from diagrams.aws.storage import S3
      from diagrams.onprem.analytics import Tableau
      
      with Diagram("Real-time Analytics", show=False):
          stream = KinesisDataStreams("Data Stream")
          
          with Cluster("Processing"):
              lambda1 = Lambda("Processor 1")
              lambda2 = Lambda("Aggregator")
              cache = ElastiCache("Cache")
          
          with Cluster("Storage"):
              dynamodb = DynamoDB("Hot Data")
              firehose = KinesisDataFirehose("Firehose")
              s3 = S3("Cold Storage")
          
          viz = Tableau("Dashboard")
          
          stream >> lambda1 >> lambda2
          lambda2 >> [cache, dynamodb]
          stream >> firehose >> s3
          [cache, dynamodb, s3] >> viz

Advanced Features
-----------------

Custom Direction
~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. diagrams::
      
      from diagrams import Diagram
      
      # Left to right
      with Diagram("LR", direction="LR", show=False):
          pass
      
      # Top to bottom
      with Diagram("TB", direction="TB", show=False):
          pass

Edge Labels and Styles
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. diagrams::
      
      from diagrams import Diagram, Edge
      from diagrams.aws.compute import EC2
      from diagrams.aws.database import RDS
      
      with Diagram("Edges", show=False):
          web = EC2("Web")
          db = RDS("DB")
          
          web >> Edge(label="SQL", color="blue") >> db
          web << Edge(label="Results", style="dashed") << db

Clusters and Groups
~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. diagrams::
      
      from diagrams import Diagram, Cluster
      from diagrams.aws.compute import EC2
      from diagrams.aws.network import VPC
      
      with Diagram("VPC", show=False):
          with Cluster("VPC 10.0.0.0/16"):
              with Cluster("Public Subnet"):
                  web = [EC2("web1"), EC2("web2")]
              
              with Cluster("Private Subnet"):
                  app = [EC2("app1"), EC2("app2")]

Programming Language Icons
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. diagrams::
      
      from diagrams import Diagram, Cluster
      from diagrams.programming.language import Python, JavaScript, Go
      from diagrams.programming.framework import React, Django, FastAPI
      
      with Diagram("Tech Stack", show=False):
          with Cluster("Frontend"):
              JavaScript("JS") >> React("React")
          
          with Cluster("Backend"):
              Python("Python") >> [Django("Django"), FastAPI("FastAPI")]
          
          with Cluster("Services"):
              Go("Golang")

On-Premise Infrastructure
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. diagrams::
      
      from diagrams import Diagram, Cluster
      from diagrams.onprem.compute import Server
      from diagrams.onprem.network import Nginx
      from diagrams.onprem.database import MySQL
      from diagrams.onprem.monitoring import Prometheus
      
      with Diagram("On-Prem", show=False):
          lb = Nginx("Load Balancer")
          
          with Cluster("Application Servers"):
              apps = [Server("app1"), Server("app2")]
          
          db = MySQL("Database")
          monitor = Prometheus("Monitoring")
          
          lb >> apps >> db
          apps >> monitor

Docker Integration
------------------

Build Diagrams
~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     kensai-sphinx:latest \
     sphinx-build -b html /project/docs /project/docs/_build/html

Generate Single Diagram
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     kensai-sphinx:latest \
     python -c "
   from diagrams import Diagram
   from diagrams.aws.compute import EC2
   
   with Diagram('test', show=False, outformat='png'):
       EC2('Server')
   "

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Build Architecture Docs
   
   on:
     push:
       paths:
         - 'docs/architecture/**'
   
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Install Graphviz
           run: sudo apt-get install -y graphviz
         
         - name: Build Documentation
           run: |
             docker run --rm -v $(pwd):/project \
               kensai-sphinx:latest \
               sphinx-build -b html /project/docs /project/docs/_build/html
         
         - name: Upload Diagrams
           uses: actions/upload-artifact@v3
           with:
             name: diagrams
             path: docs/_build/html/_static/diagrams/

Best Practices
--------------

1. **Use Clusters for Organization**
   
   Group related components

2. **Meaningful Names**
   
   Use descriptive node labels

3. **Consistent Direction**
   
   Choose LR or TB and stick to it

4. **Edge Labels**
   
   Annotate data flow and protocols

5. **Version Control**
   
   Diagrams are code - commit them!

6. **Modular Diagrams**
   
   One diagram per concept/layer

Common Patterns
---------------

Three-Tier Architecture
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from diagrams import Diagram, Cluster
   from diagrams.aws.compute import EC2
   from diagrams.aws.database import RDS
   from diagrams.aws.network import ELB
   
   with Diagram("Three-Tier", show=False):
       lb = ELB("LB")
       
       with Cluster("Web Tier"):
           web = [EC2("web1"), EC2("web2")]
       
       with Cluster("App Tier"):
           app = [EC2("app1"), EC2("app2")]
       
       with Cluster("DB Tier"):
           db = RDS("database")
       
       lb >> web >> app >> db

Troubleshooting
---------------

Graphviz Not Found
~~~~~~~~~~~~~~~~~~

**Solution:**

Install Graphviz:

.. code-block:: bash

   # In Dockerfile
   RUN apk add --no-cache graphviz

Diagram Not Rendering
~~~~~~~~~~~~~~~~~~~~~

**Solution:**

Check syntax and show=False:

.. code-block:: python

   with Diagram("Name", show=False):
       # code

Missing Icons
~~~~~~~~~~~~~

**Solution:**

Check available providers:

.. code-block:: python

   from diagrams import providers
   print(providers)

Large Diagram Files
~~~~~~~~~~~~~~~~~~~

**Solution:**

Use SVG format:

.. code-block:: python

   diagrams_output_format = 'svg'

Next Steps
----------

1. Create architecture diagrams for your infrastructure
2. Document data flows
3. Visualize microservices
4. Add diagrams to API documentation
5. Keep diagrams updated with code

Additional Resources
--------------------

- :doc:`btd.sphinx.graphviz` - Graphviz integration
- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `Diagrams Documentation <https://diagrams.mingrammer.com/>`_
- `Graphviz Documentation <https://graphviz.org/documentation/>`_
