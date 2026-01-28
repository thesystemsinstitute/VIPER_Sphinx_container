Sphinx-UML Example
==================

This page demonstrates the **sphinx-uml** extension for creating UML diagrams using PlantUML syntax directly in Sphinx documentation.

.. contents:: Contents
   :local:
   :depth: 2


Class Diagrams
--------------

Simple Class
~~~~~~~~~~~~

.. uml::

   @startuml
   class User {
       +String username
       +String email
       +void login()
       +void logout()
   }
   @enduml

Inheritance
~~~~~~~~~~~

.. uml::

   @startuml
   abstract class Animal {
       #String name
       +void eat()
       +{abstract} void makeSound()
   }
   
   class Dog extends Animal {
       +void makeSound()
       +void fetch()
   }
   
   class Cat extends Animal {
       +void makeSound()
       +void purr()
   }
   @enduml

Relationships
~~~~~~~~~~~~~

.. uml::

   @startuml
   class Customer {
       +String name
       +String address
   }
   
   class Order {
       +Date orderDate
       +Double total
   }
   
   class Product {
       +String name
       +Double price
   }
   
   Customer "1" --> "*" Order : places
   Order "*" --> "*" Product : contains
   @enduml

Sequence Diagrams
-----------------

Basic Sequence
~~~~~~~~~~~~~~

.. uml::

   @startuml
   actor User
   participant "Web Server" as Server
   participant "Database" as DB
   
   User -> Server: HTTP Request
   activate Server
   
   Server -> DB: Query
   activate DB
   DB --> Server: Results
   deactivate DB
   
   Server --> User: HTTP Response
   deactivate Server
   @enduml

Authentication Flow
~~~~~~~~~~~~~~~~~~~

.. uml::

   @startuml
   actor User
   participant Frontend
   participant "Auth Service" as Auth
   participant Database
   
   User -> Frontend: Enter credentials
   Frontend -> Auth: POST /login
   activate Auth
   
   Auth -> Database: Verify credentials
   activate Database
   Database --> Auth: User found
   deactivate Database
   
   Auth -> Auth: Generate token
   Auth --> Frontend: Return token
   deactivate Auth
   
   Frontend --> User: Login successful
   @enduml

API Call Flow
~~~~~~~~~~~~~

.. uml::

   @startuml
   participant Client
   participant Gateway
   participant "Service A" as A
   participant "Service B" as B
   participant Cache
   
   Client -> Gateway: API Request
   Gateway -> Cache: Check cache
   alt Cache hit
       Cache --> Gateway: Cached data
   else Cache miss
       Gateway -> A: Request data
       A -> B: Get details
       B --> A: Return details
       A --> Gateway: Processed data
       Gateway -> Cache: Store data
   end
   Gateway --> Client: Response
   @enduml

Activity Diagrams
-----------------

Simple Flow
~~~~~~~~~~~

.. uml::

   @startuml
   start
   :Read input;
   if (Valid input?) then (yes)
       :Process data;
       :Generate output;
   else (no)
       :Show error;
   endif
   stop
   @enduml

Order Processing
~~~~~~~~~~~~~~~~

.. uml::

   @startuml
   start
   :Receive order;
   :Check inventory;
   
   if (Items available?) then (yes)
       :Reserve items;
       :Process payment;
       if (Payment successful?) then (yes)
           :Confirm order;
           :Ship items;
       else (no)
           :Release items;
           :Notify customer;
       endif
   else (no)
       :Notify out of stock;
   endif
   
   stop
   @enduml

Parallel Activities
~~~~~~~~~~~~~~~~~~~

.. uml::

   @startuml
   start
   :Start deployment;
   fork
       :Build application;
   fork again
       :Run tests;
   fork again
       :Security scan;
   end fork
   :Deploy to production;
   stop
   @enduml

State Diagrams
--------------

Order States
~~~~~~~~~~~~

.. uml::

   @startuml
   [*] --> Created
   Created --> Paid : payment received
   Paid --> Shipped : items dispatched
   Shipped --> Delivered : received by customer
   Delivered --> [*]
   
   Created --> Cancelled : cancel order
   Paid --> Cancelled : refund processed
   Cancelled --> [*]
   @enduml

Connection States
~~~~~~~~~~~~~~~~~

.. uml::

   @startuml
   [*] --> Disconnected
   Disconnected --> Connecting : connect()
   Connecting --> Connected : success
   Connecting --> Disconnected : timeout
   Connected --> Disconnected : disconnect()
   Connected --> Reconnecting : connection lost
   Reconnecting --> Connected : reconnect success
   Reconnecting --> Disconnected : give up
   @enduml

Component Diagrams
------------------

System Architecture
~~~~~~~~~~~~~~~~~~~

.. uml::

   @startuml
   package "Frontend" {
       [Web UI]
       [Mobile App]
   }
   
   package "Backend" {
       [API Gateway]
       [Auth Service]
       [Business Logic]
   }
   
   package "Data" {
       [Database]
       [Cache]
   }
   
   [Web UI] --> [API Gateway]
   [Mobile App] --> [API Gateway]
   [API Gateway] --> [Auth Service]
   [API Gateway] --> [Business Logic]
   [Business Logic] --> [Database]
   [Business Logic] --> [Cache]
   @enduml

Microservices
~~~~~~~~~~~~~

.. uml::

   @startuml
   cloud "Load Balancer" {
   }
   
   package "User Service" {
       [User API]
       [User DB]
   }
   
   package "Order Service" {
       [Order API]
       [Order DB]
   }
   
   package "Payment Service" {
       [Payment API]
       [Payment DB]
   }
   
   [Load Balancer] --> [User API]
   [Load Balancer] --> [Order API]
   [Load Balancer] --> [Payment API]
   
   [Order API] --> [User API] : verify user
   [Order API] --> [Payment API] : process payment
   @enduml

Use Case Diagrams
-----------------

E-commerce System
~~~~~~~~~~~~~~~~~

.. uml::

   @startuml
   left to right direction
   actor Customer
   actor Admin
   
   rectangle "E-commerce System" {
       usecase "Browse Products" as UC1
       usecase "Add to Cart" as UC2
       usecase "Checkout" as UC3
       usecase "Manage Products" as UC4
       usecase "View Orders" as UC5
   }
   
   Customer --> UC1
   Customer --> UC2
   Customer --> UC3
   Customer --> UC5
   Admin --> UC4
   Admin --> UC5
   @enduml

Banking System
~~~~~~~~~~~~~~

.. uml::

   @startuml
   actor Customer
   actor Teller
   actor Manager
   
   package "Banking System" {
       usecase "Check Balance" as UC1
       usecase "Withdraw Money" as UC2
       usecase "Deposit Money" as UC3
       usecase "Open Account" as UC4
       usecase "Close Account" as UC5
       usecase "Approve Loan" as UC6
   }
   
   Customer --> UC1
   Customer --> UC2
   Customer --> UC3
   Teller --> UC2
   Teller --> UC3
   Teller --> UC4
   Manager --> UC5
   Manager --> UC6
   @enduml

Object Diagrams
---------------

Instance Relationships
~~~~~~~~~~~~~~~~~~~~~~

.. uml::

   @startuml
   object User1 {
       username = "john_doe"
       email = "john@example.com"
   }
   
   object Order1 {
       orderDate = "2024-01-15"
       total = 99.99
   }
   
   object Order2 {
       orderDate = "2024-01-20"
       total = 149.99
   }
   
   User1 --> Order1
   User1 --> Order2
   @enduml

Timing Diagrams
---------------

Protocol Timing
~~~~~~~~~~~~~~~

.. uml::

   @startuml
   robust "Client" as C
   robust "Server" as S
   
   @0
   C is Idle
   S is Waiting
   
   @100
   C is Sending
   S is Waiting
   
   @200
   C is Waiting
   S is Processing
   
   @300
   C is Receiving
   S is Sending
   
   @400
   C is Idle
   S is Waiting
   @enduml

Deployment Diagrams
-------------------

Infrastructure
~~~~~~~~~~~~~~

.. uml::

   @startuml
   node "Web Server" {
       [Nginx]
       [Application]
   }
   
   node "App Server 1" {
       [Service Instance 1]
   }
   
   node "App Server 2" {
       [Service Instance 2]
   }
   
   database "PostgreSQL" {
       [Primary DB]
   }
   
   database "Redis" {
       [Cache]
   }
   
   [Nginx] --> [Service Instance 1]
   [Nginx] --> [Service Instance 2]
   [Service Instance 1] --> [Primary DB]
   [Service Instance 2] --> [Primary DB]
   [Service Instance 1] --> [Cache]
   [Service Instance 2] --> [Cache]
   @enduml

Configuration Examples
----------------------

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinxcontrib.plantuml',
   ]
   
   # PlantUML configuration
   plantuml = 'java -jar /path/to/plantuml.jar'
   plantuml_output_format = 'svg'

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # PlantUML settings
   plantuml_latex_output_format = 'pdf'
   plantuml_epstopdf = '/usr/bin/epstopdf'
   
   # Syntax highlighting
   plantuml_syntax_error_image = True
   
   # Include path
   plantuml_include_path = ['_diagrams/includes']

Custom Styling
~~~~~~~~~~~~~~

.. code-block:: python

   # Custom PlantUML configuration
   plantuml_batch_size = 100
   
   # Default options
   plantuml_default_config = '''
   skinparam backgroundColor #FFFFFF
   skinparam classBackgroundColor #E8F4F8
   skinparam classBorderColor #333333
   '''

Practical Examples
------------------

MVC Pattern
~~~~~~~~~~~

.. uml::

   @startuml
   package "Model" {
       class User
       class Product
       class Order
   }
   
   package "View" {
       class UserView
       class ProductView
       class OrderView
   }
   
   package "Controller" {
       class UserController
       class ProductController
       class OrderController
   }
   
   UserController --> User
   UserController --> UserView
   ProductController --> Product
   ProductController --> ProductView
   OrderController --> Order
   OrderController --> OrderView
   @enduml

REST API Design
~~~~~~~~~~~~~~~

.. uml::

   @startuml
   participant Client
   participant "API Gateway" as Gateway
   participant "Resource Server" as Resource
   participant Database
   
   Client -> Gateway: GET /api/users
   Gateway -> Resource: Forward request
   Resource -> Database: SELECT * FROM users
   Database --> Resource: Return data
   Resource --> Gateway: JSON response
   Gateway --> Client: 200 OK
   
   Client -> Gateway: POST /api/users
   Gateway -> Resource: Forward request
   Resource -> Database: INSERT INTO users
   Database --> Resource: Success
   Resource --> Gateway: JSON response
   Gateway --> Client: 201 Created
   @enduml

Error Handling
~~~~~~~~~~~~~~

.. uml::

   @startuml
   start
   :Execute operation;
   
   if (Success?) then (yes)
       :Return result;
   else (no)
       if (Retryable error?) then (yes)
           if (Retry count < max?) then (yes)
               :Increment retry count;
               :Wait backoff time;
               :Execute operation;
           else (no)
               :Log error;
               :Return failure;
           endif
       else (no)
           :Log error;
           :Return failure;
       endif
   endif
   
   stop
   @enduml

Advanced Features
-----------------

Sprites and Icons
~~~~~~~~~~~~~~~~~

.. uml::

   @startuml
   !include <awslib/AWSCommon>
   !include <awslib/Compute/EC2>
   !include <awslib/Database/RDS>
   !include <awslib/Storage/S3>
   
   EC2(web, "Web Server", "")
   RDS(db, "Database", "")
   S3(storage, "File Storage", "")
   
   web --> db
   web --> storage
   @enduml

Notes and Comments
~~~~~~~~~~~~~~~~~~

.. uml::

   @startuml
   class User {
       +username: String
       +email: String
   }
   
   note right of User
       User class represents
       registered users in
       the system
   end note
   
   class Order
   
   note "Orders are linked to users" as N1
   User .. N1
   N1 .. Order
   @enduml

See Also
--------

- :doc:`../tutorials/packages/sphinx-uml` - Complete tutorial
- PlantUML documentation: https://plantuml.com/
- GitHub repository: https://github.com/sphinx-contrib/plantuml
