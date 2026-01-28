Ansible-Sphinx Tutorial
=======================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/ansible-sphinx/>`_
   - :doc:`See Working Example <../../examples/ansible-sphinx-example>`


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

Practical Examples
------------------

Example 1: Documenting Ansible Roles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Role structure:

.. code-block:: text

   roles/
   └── webserver/
       ├── tasks/
       │   └── main.yml
       ├── handlers/
       │   └── main.yml
       ├── templates/
       │   └── nginx.conf.j2
       ├── defaults/
       │   └── main.yml
       ├── vars/
       │   └── main.yml
       └── meta/
           └── main.yml

``roles/webserver/tasks/main.yml``:

.. code-block:: yaml

   ---
   # Web server installation and configuration
   
   - name: Install nginx
     apt:
       name: nginx
       state: present
     tags:
       - packages
       - webserver
   
   - name: Configure nginx
     template:
       src: nginx.conf.j2
       dest: /etc/nginx/nginx.conf
       mode: '0644'
     notify: restart nginx
   
   - name: Start nginx service
     service:
       name: nginx
       state: started
       enabled: yes

``roles/webserver/defaults/main.yml``:

.. code-block:: yaml

   ---
   # Default variables for webserver role
   
   webserver_port: 80
   webserver_user: www-data
   webserver_worker_processes: auto
   webserver_keepalive_timeout: 65

``roles/webserver/meta/main.yml``:

.. code-block:: yaml

   ---
   galaxy_info:
     author: DevOps Team
     description: Install and configure Nginx web server
     license: MIT
     min_ansible_version: 2.9
     platforms:
       - name: Ubuntu
         versions:
           - focal
           - jammy
   
   dependencies: []

``docs/roles/webserver.rst``:

.. code-block:: rst

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
   
   Example Usage
   -------------
   
   .. code-block:: yaml
      
      - hosts: webservers
        roles:
          - role: webserver
            webserver_port: 8080
   
   Tags
   ----
   
   - ``packages`` - Package installation tasks
   - ``webserver`` - Web server configuration

Example 2: Playbook Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``playbooks/deploy.yml``:

.. code-block:: yaml

   ---
   - name: Deploy web application
     hosts: webservers
     become: yes
     
     vars:
       app_name: myapp
       app_version: 1.0.0
       deploy_dir: /var/www/{{ app_name }}
     
     tasks:
       - name: Create deployment directory
         file:
           path: "{{ deploy_dir }}"
           state: directory
           mode: '0755'
       
       - name: Download application
         get_url:
           url: "https://releases.example.com/{{ app_name }}-{{ app_version }}.tar.gz"
           dest: "/tmp/{{ app_name }}.tar.gz"
       
       - name: Extract application
         unarchive:
           src: "/tmp/{{ app_name }}.tar.gz"
           dest: "{{ deploy_dir }}"
           remote_src: yes
       
       - name: Install dependencies
         pip:
           requirements: "{{ deploy_dir }}/requirements.txt"
           virtualenv: "{{ deploy_dir }}/venv"
       
       - name: Restart application
         systemd:
           name: "{{ app_name }}"
           state: restarted

``docs/playbooks/deploy.rst``:

.. code-block:: rst

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

Additional Resources
--------------------

- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `Ansible Documentation <https://docs.ansible.com/>`_
- `Ansible Galaxy <https://galaxy.ansible.com/>`_
- `ansible-sphinx Project <https://github.com/ansible-community/ansible-sphinx>`_
