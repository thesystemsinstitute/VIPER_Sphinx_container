Ansible-Sphinx Tutorial
=======================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/ansible-sphinx/>`_
   - `Manual <https://github.com/ansible-community/ansible-sphinx>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use ansible-sphinx to document Ansible playbooks, roles, and collections in Sphinx.

What is Ansible-Sphinx?
------------------------
ansible-sphinx is a Sphinx extension that provides:

- Ansible documentation generation
- Playbook documentation
- Role documentation
- Module documentation
- Task documentation
- Variable documentation
- Inventory documentation
- Auto-discovery of Ansible files
- YAML parsing
- Cross-referencing
- Collection support

This enables comprehensive documentation of Ansible automation directly from your playbooks and roles.

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

ansible-sphinx is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import ansible_sphinx; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``docs/conf.py``:

.. code-block:: python

   extensions = [
       'ansible_sphinx',
   ]
   
   # Ansible documentation paths
   ansible_playbook_dir = '../playbooks'
   ansible_role_dir = '../roles'

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['ansible_sphinx']
   
   # Paths to Ansible content
   ansible_playbook_dir = '../playbooks'
   ansible_role_dir = '../roles'
   ansible_collection_dir = '../collections'
   
   # Documentation options
   ansible_show_defaults = True
   ansible_show_vars = True
   ansible_show_handlers = True
   
   # Formatting
   ansible_format_tasks = True
   ansible_highlight_code = True


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

Basic Usage
-----------

Document a Role
~~~~~~~~~~~~~~~

.. code-block:: rst

   .. ansible-role:: webserver

This documents the webserver role from your roles directory.

Document a Playbook
~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. ansible-playbook:: deploy.yml

Document a Task
~~~~~~~~~~~~~~~

.. code-block:: rst

   .. ansible-task:: install-packages

   Web Server Role
   ===============
   
   This role installs and configures an Nginx web server.
   
   Role Documentation
   ------------------
   
   .. ansible-role:: webserver
   
   Variables
   ---------
   
   The following variables can be customized:
   
   .. list-table::
      :header-rows: 1
      
      * - Variable
        - Default
        - Description
      * - ``webserver_port``
        - 80
        - HTTP port
      * - ``webserver_user``
        - www-data
        - User running nginx
      * - ``webserver_worker_processes``
        - auto
        - Number of worker processes
   
   Deployment Playbook
   ===================
   
   This playbook deploys the web application to production servers.
   
   Playbook Details
   ----------------
   
   .. ansible-playbook:: deploy.yml
   
   Prerequisites
   -------------
   
   - Target servers running Ubuntu 20.04+
   - SSH access with sudo privileges
   - Application release available at releases.example.com
   
   Usage
   -----
   
   Run the playbook:
   
   .. code-block:: bash
      
      ansible-playbook playbooks/deploy.yml -i inventory/production
   
   Override version:
   
   .. code-block:: bash
      
      ansible-playbook playbooks/deploy.yml -e "app_version=2.0.0"
   
   Variables
   ---------
   
   .. list-table::
      :header-rows: 1
      
      * - Variable
        - Default
        - Description
      * - ``app_name``
        - myapp
        - Application name
      * - ``app_version``
        - 1.0.0
        - Version to deploy
      * - ``deploy_dir``
        - /var/www/myapp
        - Deployment directory

Example 3: Complete Ansible Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/ansible/index.rst``:

.. code-block:: rst

   Ansible Automation
   ==================
   
   This section documents our Ansible infrastructure automation.
   
   .. toctree::
      :maxdepth: 2
      :caption: Contents:
      
      playbooks
      roles
      inventory
      variables
   
   Overview
   --------
   
   Our Ansible automation includes:
   
   - **Playbooks** - Task orchestration
   - **Roles** - Reusable components
   - **Inventory** - Server organization
   - **Variables** - Configuration management
   
   Quick Start
   -----------
   
   1. Install Ansible:
   
      .. code-block:: bash
         
         pip install ansible
   
   2. Clone repository:
   
      .. code-block:: bash
         
         git clone https://github.com/example/ansible.git
         cd ansible
   
   3. Run a playbook:
   
      .. code-block:: bash
         
         ansible-playbook playbooks/deploy.yml -i inventory/production

``docs/ansible/roles.rst``:

.. code-block:: rst

   Ansible Roles
   =============
   
   Available Roles
   ---------------
   
   Web Server
   ~~~~~~~~~~
   
   .. include:: roles/webserver.rst
   
   Database
   ~~~~~~~~
   
   .. include:: roles/database.rst
   
   Load Balancer
   ~~~~~~~~~~~~~
   
   .. include:: roles/loadbalancer.rst

Example 4: Module Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``library/custom_deploy.py``:

.. code-block:: python

   #!/usr/bin/python
   # -*- coding: utf-8 -*-
   
   DOCUMENTATION = '''
   ---
   module: custom_deploy
   short_description: Deploy application
   description:
       - Deploys application with custom logic
       - Handles rollback on failure
   version_added: "1.0"
   author: "DevOps Team"
   options:
       app_name:
           description:
               - Name of the application
           required: true
           type: str
       version:
           description:
               - Version to deploy
           required: true
           type: str
       deploy_path:
           description:
               - Path to deploy to
           required: false
           default: /var/www
           type: path
   '''
   
   EXAMPLES = '''
   - name: Deploy application
     custom_deploy:
       app_name: myapp
       version: 1.0.0
       deploy_path: /opt/apps
   '''
   
   RETURN = '''
   changed:
       description: Whether deployment occurred
       type: bool
       returned: always
   message:
       description: Deployment status message
       type: str
       returned: always
   '''

``docs/modules/custom_deploy.rst``:

.. code-block:: rst

   Custom Deploy Module
   =====================
   
   .. ansible-module:: custom_deploy

Advanced Features
-----------------

Collection Documentation
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   ansible_collection_dir = '../collections'

.. code-block:: rst

   .. ansible-collection:: namespace.collection

Inventory Documentation
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Inventory Structure
   ===================
   
   .. ansible-inventory:: inventory/production

Task Filtering
~~~~~~~~~~~~~~

.. code-block:: rst

   .. ansible-role:: webserver
      :tasks: install-packages, configure-service

Docker Integration
------------------

Build Documentation
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     kensai-sphinx:latest \
     sphinx-build -b html /project/docs /project/docs/_build/html

With Ansible Installed
~~~~~~~~~~~~~~~~~~~~~~~

``Dockerfile.ansible-docs``:

.. code-block:: dockerfile

   FROM kensai-sphinx:latest
   
   # Install Ansible
   RUN pip install ansible ansible-core
   
   WORKDIR /project
   
   CMD ["sphinx-build", "-b", "html", "docs", "docs/_build/html"]

Build:

.. code-block:: bash

   docker build -f Dockerfile.ansible-docs -t ansible-docs .
   docker run --rm -v $(pwd):/project ansible-docs

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Build Ansible Documentation
   
   on: [push]
   
   jobs:
     docs:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Build Documentation
           run: |
             docker run --rm -v $(pwd):/project \
               kensai-sphinx:latest \
               sphinx-build -b html /project/docs /project/docs/_build/html
         
         - name: Verify Role Docs
           run: |
             # Check role documentation exists
             if [ ! -f docs/_build/html/roles/webserver.html ]; then
               echo "Role documentation not generated!"
               exit 1
             fi
         
         - name: Deploy
           uses: peaceiris/actions-gh-pages@v3
           with:
             github_token: ${{ secrets.GITHUB_TOKEN }}
             publish_dir: ./docs/_build/html

Best Practices
--------------

1. **Document Variables**
   
   Clear descriptions in defaults/main.yml

2. **Use Meta Info**
   
   Complete galaxy_info in meta/main.yml

3. **Tag Tasks**
   
   Organize with meaningful tags

4. **Add Examples**
   
   Show common usage patterns

5. **Keep Updated**
   
   Regenerate docs when roles change

6. **Cross-Reference**
   
   Link between playbooks and roles

Troubleshooting
---------------

Extension Not Found
~~~~~~~~~~~~~~~~~~~

**Solution:**

Verify installation:

.. code-block:: bash

   pip list | grep ansible-sphinx

Add to extensions:

.. code-block:: python

   extensions = ['ansible_sphinx']

Roles Not Documented
~~~~~~~~~~~~~~~~~~~~

**Solution:**

Check role path:

.. code-block:: python

   ansible_role_dir = '../roles'

Verify role structure is correct.

YAML Parse Errors
~~~~~~~~~~~~~~~~~

**Solution:**

Validate YAML syntax:

.. code-block:: bash

   ansible-playbook playbooks/deploy.yml --syntax-check

Variables Not Showing
~~~~~~~~~~~~~~~~~~~~~

**Solution:**

Enable variable documentation:

.. code-block:: python

   ansible_show_vars = True

Next Steps
----------

1. Configure ansible-sphinx
2. Document roles and playbooks
3. Add usage examples
4. Build and review
5. Deploy documentation


Practical Examples
------------------

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

Additional Resources
--------------------
- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `Ansible Documentation <https://docs.ansible.com/>`_
- `Ansible Galaxy <https://galaxy.ansible.com/>`_
- `ansible-sphinx Project <https://github.com/ansible-community/ansible-sphinx>`_
**Related Extensions**:
- :doc:`invoke-sphinx-example` - Invoke task documentation
- :doc:`myst-parser-example` - Markdown support
- :doc:`sphinx-copybutton-example` - Copy code buttons
**External Resources**:
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

