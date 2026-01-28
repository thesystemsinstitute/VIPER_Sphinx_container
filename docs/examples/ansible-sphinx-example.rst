ansible-sphinx - Working Example
=================================

This page demonstrates the capabilities of **ansible-sphinx**, a Sphinx extension for documenting Ansible roles, playbooks, and collections with specialized directives and auto-documentation features.

.. note::

   **About ansible-sphinx**
   
   ansible-sphinx provides directives and tools specifically designed for Ansible documentation, making it easy to document playbooks, roles, modules, and collections within Sphinx.
   
   - **Package**: ansible-sphinx
   - **Purpose**: Ansible documentation in Sphinx
   - **Use Case**: Documenting Ansible automation projects
   - **Tutorial**: :doc:`../tutorials/packages/ansible-sphinx`

Overview
--------

ansible-sphinx extends Sphinx with Ansible-specific documentation capabilities, understanding YAML playbooks, roles, and inventory structures.

Key Features
~~~~~~~~~~~~

**Ansible Integration**

- Playbook documentation
- Role documentation
- Module reference
- Collection documentation

**Auto-Documentation**

- Automatic role extraction
- Task listing
- Variable documentation
- Handler documentation

**YAML Support**

- Syntax highlighting
- Structure validation
- Cross-referencing
- Examples rendering

Installation
------------

Basic Installation
~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   pip install ansible-sphinx

The extension is already installed in this environment:

.. code-block:: python

   import ansible_sphinx
   print(f"ansible-sphinx available")

Configuration
-------------

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   # Enable the extension
   extensions = [
       'ansible_sphinx',
   ]
   
   # Ansible documentation settings
   ansible_roles_path = '../roles'
   ansible_playbooks_path = '../playbooks'

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py - Advanced settings
   extensions = ['ansible_sphinx']
   
   # Path configuration
   ansible_roles_path = ['../roles', '../galaxy_roles']
   ansible_playbooks_path = '../playbooks'
   ansible_collections_path = '../collections'
   
   # Documentation options
   ansible_show_task_details = True
   ansible_show_handlers = True
   ansible_show_defaults = True
   
   # Formatting
   ansible_yaml_lexer = 'yaml+jinja'

Documenting Roles
-----------------

Role Structure
~~~~~~~~~~~~~~

Standard Ansible role structure:

.. code-block:: text

   roles/
   └── webserver/
       ├── README.md
       ├── meta/
       │   └── main.yml
       ├── defaults/
       │   └── main.yml
       ├── vars/
       │   └── main.yml
       ├── tasks/
       │   └── main.yml
       ├── handlers/
       │   └── main.yml
       ├── templates/
       │   └── nginx.conf.j2
       └── files/
           └── index.html

Role Documentation Directive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. ansible-role:: webserver
      :path: ../roles/webserver

This automatically documents:

- Role metadata
- Variables (defaults and vars)
- Tasks
- Handlers
- Dependencies

Manual Role Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Webserver Role
   ==============
   
   .. ansible-role:: webserver
   
   Description
   -----------
   
   Installs and configures Nginx web server.
   
   Variables
   ---------
   
   .. ansible-var:: webserver_port
      :type: int
      :default: 80
      
      Port for the web server to listen on.
   
   .. ansible-var:: webserver_document_root
      :type: string
      :default: /var/www/html
      
      Document root directory.

Documenting Playbooks
----------------------

Playbook Example
~~~~~~~~~~~~~~~~

**playbook.yml**:

.. code-block:: yaml

   ---
   - name: Configure web servers
     hosts: webservers
     become: yes
     
     vars:
       app_name: myapp
       app_version: 1.0.0
     
     tasks:
       - name: Install Nginx
         apt:
           name: nginx
           state: present
       
       - name: Start Nginx
         service:
           name: nginx
           state: started
           enabled: yes

Playbook Documentation
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Web Server Deployment
   =====================
   
   .. ansible-playbook:: deploy_webserver.yml
      :path: ../playbooks
   
   This playbook deploys and configures web servers.

Task Documentation
~~~~~~~~~~~~~~~~~~

Document individual tasks:

.. code-block:: rst

   .. ansible-task:: Install Nginx
      :module: apt
      
      Installs the Nginx package using the apt module.
      
      .. code-block:: yaml
      
         - name: Install Nginx
           apt:
             name: nginx
             state: present
             update_cache: yes

Module Documentation
--------------------

Custom Module
~~~~~~~~~~~~~

.. code-block:: rst

   My Custom Module
   ================
   
   .. ansible-module:: my_custom_module
      :path: ../library
   
   Custom module for specific functionality.
   
   Parameters
   ~~~~~~~~~~
   
   .. ansible-option:: name
      :type: str
      :required: yes
      
      Name of the resource to manage.
   
   .. ansible-option:: state
      :type: str
      :choices: present, absent
      :default: present
      
      Desired state of the resource.

Module Examples
~~~~~~~~~~~~~~~

.. code-block:: rst

   Examples
   --------
   
   .. code-block:: yaml
   
      # Create a resource
      - name: Create resource
        my_custom_module:
          name: myresource
          state: present
      
      # Remove a resource
      - name: Remove resource
        my_custom_module:
          name: myresource
          state: absent

Documenting Variables
----------------------

Variable Reference
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Variables
   =========
   
   .. ansible-var:: database_host
      :type: string
      :required: yes
      
      Hostname or IP address of the database server.
   
   .. ansible-var:: database_port
      :type: int
      :default: 5432
      
      Port number for database connections.
   
   .. ansible-var:: database_name
      :type: string
      :required: yes
      
      Name of the database to connect to.

defaults/main.yml Example
~~~~~~~~~~~~~~~~~~~~~~~~~~

**defaults/main.yml**:

.. code-block:: yaml

   ---
   # Web server configuration
   webserver_port: 80
   webserver_ssl_port: 443
   webserver_document_root: /var/www/html
   
   # Application settings
   app_environment: production
   app_debug: false

Documentation:

.. code-block:: rst

   Default Variables
   =================
   
   .. ansible-defaults:: webserver
      :path: ../roles/webserver

Inventory Documentation
-----------------------

Inventory Structure
~~~~~~~~~~~~~~~~~~~

.. code-block:: ini

   [webservers]
   web1.example.com
   web2.example.com
   
   [databases]
   db1.example.com
   
   [production:children]
   webservers
   databases
   
   [production:vars]
   env=production

Inventory Documentation
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Production Inventory
   ====================
   
   .. ansible-inventory:: production
      :path: ../inventory
   
   This inventory defines the production environment hosts.

Collection Documentation
-------------------------

Collection Structure
~~~~~~~~~~~~~~~~~~~~

.. code-block:: text

   collections/
   └── ansible_collections/
       └── mycompany/
           └── myapp/
               ├── plugins/
               ├── roles/
               ├── playbooks/
               └── docs/

Collection Documentation
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   MyApp Collection
   ================
   
   .. ansible-collection:: mycompany.myapp
      :path: ../collections/ansible_collections
   
   This collection provides modules and roles for MyApp deployment.

Practical Examples
------------------

Complete Role Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Database Role
   =============
   
   .. ansible-role:: postgresql
   
   Installs and configures PostgreSQL database server.
   
   Requirements
   ------------
   
   - Debian/Ubuntu or RHEL/CentOS
   - Python 3.6+
   - Ansible 2.9+
   
   Role Variables
   --------------
   
   .. ansible-var:: postgresql_version
      :type: string
      :default: "14"
      
      PostgreSQL major version to install.
   
   .. ansible-var:: postgresql_data_dir
      :type: string
      :default: /var/lib/postgresql/data
      
      Data directory location.
   
   Example Playbook
   ----------------
   
   .. code-block:: yaml
   
      - hosts: databases
        roles:
          - role: postgresql
            postgresql_version: "14"
            postgresql_data_dir: /data/postgresql
   
   Dependencies
   ------------
   
   None.

Multi-Play Playbook
~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Application Deployment
   ======================
   
   .. ansible-playbook:: deploy_app.yml
   
   Complete application deployment playbook.
   
   Plays
   -----
   
   1. **Prepare infrastructure**
      
      .. code-block:: yaml
      
         - name: Prepare servers
           hosts: all
           tasks:
             - name: Update packages
               apt:
                 update_cache: yes
   
   2. **Deploy application**
      
      .. code-block:: yaml
      
         - name: Deploy app
           hosts: webservers
           roles:
             - application
   
   3. **Configure monitoring**
      
      .. code-block:: yaml
      
         - name: Setup monitoring
           hosts: all
           roles:
             - monitoring

Best Practices
--------------

Documentation Structure
~~~~~~~~~~~~~~~~~~~~~~~

Organize Ansible documentation:

.. code-block:: text

   docs/
   ├── index.rst
   ├── roles/
   │   ├── index.rst
   │   ├── webserver.rst
   │   └── database.rst
   ├── playbooks/
   │   ├── index.rst
   │   ├── deployment.rst
   │   └── maintenance.rst
   └── modules/
       ├── index.rst
       └── custom_modules.rst

Role README Integration
~~~~~~~~~~~~~~~~~~~~~~~

Include role README files:

.. code-block:: rst

   .. include:: ../../roles/webserver/README.md
      :parser: myst_parser.sphinx_

YAML Examples
~~~~~~~~~~~~~

Use proper YAML formatting:

.. code-block:: rst

   .. code-block:: yaml+jinja
   
      ---
      - name: Configure application
        hosts: "{{ target_hosts }}"
        vars:
          app_config:
            name: myapp
            version: "{{ app_version }}"
        tasks:
          - name: Deploy configuration
            template:
              src: config.j2
              dest: /etc/myapp/config.yml

Cross-Referencing
~~~~~~~~~~~~~~~~~

Link between Ansible components:

.. code-block:: rst

   The :ansible-role:`webserver` role uses the 
   :ansible-var:`webserver_port` variable and calls the
   :ansible-handler:`restart nginx` handler.

Integration Patterns
--------------------

Galaxy Integration
~~~~~~~~~~~~~~~~~~

Document Galaxy roles:

.. code-block:: rst

   Installing from Galaxy
   ======================
   
   .. code-block:: bash
   
      ansible-galaxy install mycompany.myrole
   
   .. ansible-role:: mycompany.myrole
      :galaxy: yes

Version Documentation
~~~~~~~~~~~~~~~~~~~~~

Document version-specific features:

.. code-block:: rst

   .. versionadded:: 2.0
      Support for SSL configuration
   
   .. versionchanged:: 2.1
      Default port changed from 8080 to 80
   
   .. deprecated:: 2.2
      The `legacy_mode` variable is deprecated

CI/CD Documentation
~~~~~~~~~~~~~~~~~~~

Document pipeline integration:

.. code-block:: rst

   CI/CD Integration
   =================
   
   .. code-block:: yaml
   
      # .gitlab-ci.yml
      test:
        script:
          - ansible-playbook --syntax-check site.yml
          - ansible-lint roles/*/
          - ansible-playbook --check site.yml

Troubleshooting
---------------

Role Not Found
~~~~~~~~~~~~~~

Check path configuration:

.. code-block:: python

   # conf.py
   import os
   
   ansible_roles_path = os.path.abspath('../roles')
   print(f"Looking for roles in: {ansible_roles_path}")

Syntax Highlighting
~~~~~~~~~~~~~~~~~~~

Ensure YAML highlighting works:

.. code-block:: python

   # conf.py
   extensions = ['sphinx.ext.autodoc']
   
   # Use YAML+Jinja lexer
   ansible_yaml_lexer = 'yaml+jinja'

See Also
--------

**Related Extensions**:

- :doc:`invoke-sphinx-example` - Invoke task documentation
- :doc:`myst-parser-example` - Markdown support
- :doc:`sphinx-copybutton-example` - Copy code buttons

**External Resources**:

- `Ansible Documentation <https://docs.ansible.com/>`_
- `Ansible Galaxy <https://galaxy.ansible.com/>`_
- `YAML Syntax <https://yaml.org/>`_

Summary
-------

ansible-sphinx provides specialized Ansible documentation:

**Key Capabilities**:

✅ Automated role documentation
✅ Playbook integration
✅ Variable reference generation
✅ Module documentation
✅ Collection support

**Common Use Cases**:

- Ansible role documentation
- Playbook guides
- Custom module reference
- Collection documentation
- Infrastructure as Code docs

Essential for teams documenting Ansible automation projects within Sphinx.
