Sphinx-UML Tutorial
===================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-uml/>`_
   - :doc:`See Working Example <../../examples/sphinx-uml-example>`


This tutorial demonstrates how to use sphinx-uml to create UML diagrams directly in your Sphinx documentation using PlantUML syntax.

What is Sphinx-UML?
-------------------

sphinx-uml is a Sphinx extension that integrates PlantUML for creating various UML diagrams:

- Class diagrams
- Sequence diagrams
- Use case diagrams
- Activity diagrams
- Component diagrams
- State diagrams
- Object diagrams
- Deployment diagrams
- Timing diagrams
- Network diagrams
- Inline diagram syntax
- SVG, PNG, and PDF output

Unlike sphinx-pyreverse which generates diagrams from code, sphinx-uml allows you to write diagrams directly in documentation.

Installation
------------

sphinx-uml is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinxcontrib.plantuml; print('Installed')"

**Note:** PlantUML requires Java, which may need to be installed separately.

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinxcontrib.plantuml',
   ]
   
   # PlantUML configuration
   plantuml = 'java -jar plantuml.jar'

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinxcontrib.plantuml']
   
   # PlantUML executable
   plantuml = 'java -jar /usr/local/bin/plantuml.jar'
   
   # Output format
   plantuml_output_format = 'svg'  # or 'png', 'pdf'
   
   # Include path for PlantUML files
   plantuml_include_path = ['_plantuml']
   
   # Batch processing
   plantuml_batch_size = 100
   
   # LaTeX output
   plantuml_latex_output_format = 'pdf'
   
   # Syntax options
   plantuml_syntax_error_image = True

Basic Usage
-----------

Inline UML Diagram
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. uml::
      
      @startuml
      Alice -> Bob: Hello
      Bob -> Alice: Hi!
      @enduml

External UML File
~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. uml:: diagrams/sequence.puml

With Caption
~~~~~~~~~~~~

.. code-block:: rst

   .. uml::
      :caption: User authentication sequence
      
      @startuml
      User -> System: Login
      System -> Database: Verify credentials
      Database -> System: OK
      System -> User: Access granted
      @enduml

Diagram Types
-------------

Class Diagram
~~~~~~~~~~~~~

.. code-block:: rst

   .. uml::
      :caption: Class relationships
      
      @startuml
      class User {
          +id: int
          +name: string
          +email: string
          +login()
          +logout()
      }
      
      class Admin {
          +permissions: list
          +grant_access()
      }
      
      class Guest {
          +session_id: string
      }
      
      User <|-- Admin
      User <|-- Guest
      @enduml

Sequence Diagram
~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. uml::
      :caption: API request flow
      
      @startuml
      participant Client
      participant API
      participant Database
      participant Cache
      
      Client -> API: GET /users/123
      API -> Cache: Check cache
      
      alt Cache hit
          Cache -> API: Return cached data
      else Cache miss
          API -> Database: Query user
          Database -> API: User data
          API -> Cache: Update cache
      end
      
      API -> Client: Return response
      @enduml

Activity Diagram
~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. uml::
      :caption: Order processing workflow
      
      @startuml
      start
      :Receive order;
      
      if (Stock available?) then (yes)
          :Process payment;
          if (Payment successful?) then (yes)
              :Ship order;
              :Send confirmation;
          else (no)
              :Cancel order;
              :Refund;
          endif
      else (no)
          :Notify customer;
          :Order on backorder;
      endif
      
      stop
      @enduml

State Diagram
~~~~~~~~~~~~~

.. code-block:: rst

   .. uml::
      :caption: Connection state machine
      
      @startuml
      [*] -> Disconnected
      
      Disconnected -> Connecting: connect()
      Connecting -> Connected: success
      Connecting -> Disconnected: failure
      
      Connected -> Disconnecting: disconnect()
      Disconnecting -> Disconnected: closed
      
      Connected -> Error: error
      Error -> Disconnected: reset
      @enduml

Component Diagram
~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. uml::
      :caption: System architecture
      
      @startuml
      package "Frontend" {
          [Web UI]
          [Mobile App]
      }
      
      package "Backend" {
          [API Gateway]
          [Auth Service]
          [User Service]
          [Order Service]
      }
      
      database "Database" {
          [PostgreSQL]
          [Redis Cache]
      }
      
      [Web UI] --> [API Gateway]
      [Mobile App] --> [API Gateway]
      [API Gateway] --> [Auth Service]
      [API Gateway] --> [User Service]
      [API Gateway] --> [Order Service]
      [User Service] --> [PostgreSQL]
      [Order Service] --> [PostgreSQL]
      [API Gateway] --> [Redis Cache]
      @enduml

Use Case Diagram
~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. uml::
      :caption: E-commerce use cases
      
      @startuml
      left to right direction
      
      actor Customer
      actor Admin
      
      rectangle "E-commerce System" {
          usecase "Browse Products" as UC1
          usecase "Add to Cart" as UC2
          usecase "Checkout" as UC3
          usecase "Manage Inventory" as UC4
          usecase "View Orders" as UC5
      }
      
      Customer --> UC1
      Customer --> UC2
      Customer --> UC3
      Admin --> UC4
      Admin --> UC5
      @enduml

Practical Examples
------------------

Example 1: API Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/api/authentication.rst``:

.. code-block:: rst

   Authentication Flow
   ===================
   
   Login Sequence
   --------------
   
   .. uml::
      :caption: User login process
      
      @startuml
      actor User
      participant "Web App" as Web
      participant "Auth API" as Auth
      participant "Database" as DB
      participant "Redis" as Cache
      
      User -> Web: Enter credentials
      Web -> Auth: POST /auth/login
      Auth -> DB: Verify user
      
      alt User exists and password correct
          DB -> Auth: User data
          Auth -> Auth: Generate JWT token
          Auth -> Cache: Store session
          Auth -> Web: Return token
          Web -> User: Redirect to dashboard
      else Invalid credentials
          DB -> Auth: User not found
          Auth -> Web: 401 Unauthorized
          Web -> User: Show error
      end
      @enduml
   
   Token Refresh
   -------------
   
   .. uml::
      :caption: JWT token refresh
      
      @startuml
      User -> API: Request with expired token
      API -> API: Validate token
      API -> User: 401 Token expired
      User -> API: POST /auth/refresh with refresh token
      API -> Cache: Verify refresh token
      Cache -> API: Token valid
      API -> API: Generate new JWT
      API -> User: New access token
      User -> API: Retry request with new token
      API -> User: Success
      @enduml

Example 2: System Architecture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/architecture.rst``:

.. code-block:: rst

   System Architecture
   ===================
   
   High-Level Overview
   -------------------
   
   .. uml::
      :caption: Microservices architecture
      
      @startuml
      !define RECTANGLE class
      
      cloud "Users" {
          actor Client
      }
      
      package "API Layer" {
          [API Gateway] as gateway
          [Load Balancer] as lb
      }
      
      package "Services" {
          [User Service] as user
          [Product Service] as product
          [Order Service] as order
          [Payment Service] as payment
      }
      
      package "Data Layer" {
          database "User DB" as userdb
          database "Product DB" as productdb
          database "Order DB" as orderdb
          queue "Message Queue" as mq
          [Cache] as cache
      }
      
      Client -> lb
      lb -> gateway
      gateway -> user
      gateway -> product
      gateway -> order
      gateway -> payment
      
      user -> userdb
      product -> productdb
      order -> orderdb
      payment -> mq
      gateway -> cache
      @enduml
   
   Data Flow
   ---------
   
   .. uml::
      :caption: Order processing flow
      
      @startuml
      start
      
      :User places order;
      :API Gateway receives request;
      
      fork
          :Validate user;
          :Check inventory;
      fork again
          :Calculate pricing;
          :Apply discounts;
      end fork
      
      if (All validations pass?) then (yes)
          :Create order record;
          :Process payment;
          
          if (Payment successful?) then (yes)
              :Update inventory;
              :Send confirmation email;
              :Trigger fulfillment;
          else (no)
              :Cancel order;
              :Refund if needed;
          endif
      else (no)
          :Return error to user;
      endif
      
      stop
      @enduml

Example 3: Database Schema
~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/database.rst``:

.. code-block:: rst

   Database Schema
   ===============
   
   Entity Relationships
   --------------------
   
   .. uml::
      :caption: Database ERD
      
      @startuml
      entity "User" as user {
          *id : integer
          --
          *email : varchar(255)
          *password_hash : varchar(255)
          name : varchar(100)
          created_at : timestamp
      }
      
      entity "Order" as order {
          *id : integer
          --
          *user_id : integer <<FK>>
          *status : varchar(50)
          total_amount : decimal(10,2)
          created_at : timestamp
      }
      
      entity "OrderItem" as item {
          *id : integer
          --
          *order_id : integer <<FK>>
          *product_id : integer <<FK>>
          quantity : integer
          price : decimal(10,2)
      }
      
      entity "Product" as product {
          *id : integer
          --
          *name : varchar(200)
          *price : decimal(10,2)
          description : text
          stock : integer
      }
      
      user ||--o{ order
      order ||--o{ item
      product ||--o{ item
      @enduml

Example 4: State Machine
~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/workflow.rst``:

.. code-block:: rst

   Order Workflow
   ==============
   
   Order States
   ------------
   
   .. uml::
      :caption: Order state transitions
      
      @startuml
      [*] -> Created : New order
      
      Created -> Validated : Validate
      Created -> Cancelled : Cancel
      
      Validated -> PaymentPending : Proceed to payment
      Validated -> Cancelled : Cancel
      
      PaymentPending -> Paid : Payment successful
      PaymentPending -> PaymentFailed : Payment failed
      PaymentPending -> Cancelled : Cancel
      
      PaymentFailed -> PaymentPending : Retry payment
      PaymentFailed -> Cancelled : Give up
      
      Paid -> Processing : Start processing
      Processing -> Shipped : Ship
      Shipped -> Delivered : Deliver
      
      Delivered -> [*] : Complete
      
      Cancelled -> [*] : Archive
      @enduml

Advanced Features
-----------------

Include External Files
~~~~~~~~~~~~~~~~~~~~~~

Create ``_plantuml/common.puml``:

.. code-block:: plantuml

   @startuml
   !define ENTITY class
   !define DATABASE database
   
   skinparam backgroundColor white
   skinparam classBackgroundColor lightblue
   @enduml

Use in documentation:

.. code-block:: rst

   .. uml::
      
      @startuml
      !include common.puml
      
      class MyClass {
          +attribute
          +method()
      }
      @enduml

Styling
~~~~~~~

.. code-block:: rst

   .. uml::
      
      @startuml
      skinparam backgroundColor #EEEBDC
      skinparam handwritten true
      
      class Foo {
          +field1
          +method1()
      }
      @enduml

Sprites and Icons
~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. uml::
      
      @startuml
      !include <aws/common>
      !include <aws/Storage/AmazonS3/AmazonS3>
      !include <aws/Database/AmazonRDS/AmazonRDS>
      
      AmazonS3(s3, "S3 Bucket", "")
      AmazonRDS(rds, "Database", "")
      
      s3 -> rds: Store
      @enduml

Docker Integration
------------------

With PlantUML Server
~~~~~~~~~~~~~~~~~~~~

``docker-compose.yml``:

.. code-block:: yaml

   version: '3.8'
   
   services:
     plantuml:
       image: plantuml/plantuml-server
       ports:
         - "8080:8080"
     
     docs:
       image: kensai-sphinx:latest
       volumes:
         - ./:/project
       depends_on:
         - plantuml
       environment:
         - PLANTUML_SERVER=http://plantuml:8080

Configure to use server:

.. code-block:: python

   # conf.py
   plantuml = 'http://localhost:8080/svg/'

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Build Docs with UML
   
   on: [push]
   
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Setup Java
           uses: actions/setup-java@v3
           with:
             distribution: 'temurin'
             java-version: '11'
         
         - name: Install PlantUML
           run: |
             wget https://github.com/plantuml/plantuml/releases/download/v1.2023.1/plantuml-1.2023.1.jar
             sudo mv plantuml-1.2023.1.jar /usr/local/bin/plantuml.jar
         
         - name: Build Docs
           run: |
             docker run --rm -v $(pwd):/project \
               -v /usr/local/bin/plantuml.jar:/usr/local/bin/plantuml.jar \
               kensai-sphinx:latest \
               sphinx-build -b html /project/docs /project/docs/_build/html

Best Practices
--------------

1. **Keep Diagrams Simple**
   
   Don't overcrowd diagrams - split complex ones

2. **Use Consistent Styling**
   
   Create reusable style definitions

3. **Version Control Diagrams**
   
   Store PlantUML source files, not just images

4. **Add Captions**
   
   Always include descriptive captions

5. **Use Meaningful Names**
   
   Name actors, classes, and components clearly

6. **Comment Complex Diagrams**
   
   Add comments in PlantUML source

Common Patterns
---------------

Standard Class Diagram
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. uml::
      
      @startuml
      class {{ ClassName }} {
          +publicAttribute
          -privateAttribute
          +publicMethod()
          -privateMethod()
      }
      @enduml

Troubleshooting
---------------

PlantUML Not Found
~~~~~~~~~~~~~~~~~~

**Solution:**

Install Java and PlantUML, or use PlantUML server

Diagrams Not Rendering
~~~~~~~~~~~~~~~~~~~~~~~

**Solution:**

Check PlantUML path:

.. code-block:: python

   plantuml = 'java -jar /path/to/plantuml.jar'

Syntax Errors
~~~~~~~~~~~~~

**Solution:**

Test diagrams at http://www.plantuml.com/plantuml/

Next Steps
----------

1. Install PlantUML or configure server
2. Create UML diagrams for your architecture
3. Document API flows with sequence diagrams
4. Add state machines for workflows
5. Generate class diagrams for data models

Additional Resources
--------------------

- :doc:`sphinx-pyreverse` - Generate UML from Python code
- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `PlantUML Documentation <https://plantuml.com/>`_
- `PlantUML Cheat Sheet <https://ogom.github.io/draw_uml/plantuml/>`_
