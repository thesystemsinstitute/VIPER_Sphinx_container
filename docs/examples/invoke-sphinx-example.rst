invoke-sphinx - Working Example
=================================

This page demonstrates the capabilities of **invoke-sphinx**, a Sphinx extension that automatically generates documentation for Invoke tasks (Python task execution tool similar to Make).

.. note::

   **About invoke-sphinx**
   
   invoke-sphinx automatically extracts and documents Invoke tasks from your tasks.py files, creating comprehensive task reference documentation.
   
   - **Package**: invoke-sphinx
   - **Purpose**: Invoke task documentation
   - **Use Case**: Document project automation tasks
   - **Tutorial**: :doc:`../tutorials/packages/invoke-sphinx`

Overview
--------

invoke-sphinx parses Invoke task collections and generates formatted documentation showing task names, parameters, descriptions, and usage examples.

Key Features
~~~~~~~~~~~~

**Automatic Extraction**

- Task discovery from tasks.py
- Parameter documentation
- Default value extraction
- Help text integration

**Documentation Generation**

- Task reference pages
- Usage examples
- Parameter tables
- Task organization

**Integration**

- Sphinx cross-referencing
- Custom formatting
- Namespace support
- Collection grouping

Installation
------------

Basic Installation
~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   pip install invoke-sphinx invoke

The extension is already installed in this environment:

.. code-block:: python

   import invoke_sphinx
   import invoke
   print(f"invoke: {invoke.__version__}")
   print("invoke-sphinx available")

Configuration
-------------

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   # Enable the extension
   extensions = [
       'invoke_sphinx',
   ]
   
   # Invoke task file location
   invoke_tasks_module = 'tasks'  # Default: tasks.py in project root

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py - Advanced settings
   extensions = ['invoke_sphinx']
   
   # Task module configuration
   invoke_tasks_module = 'automation.tasks'
   
   # Documentation options
   invoke_show_defaults = True
   invoke_show_help = True
   invoke_show_signatures = True
   
   # Formatting
   invoke_task_header_level = 2
   invoke_include_private = False

Project Structure
-----------------

Typical Layout
~~~~~~~~~~~~~~

.. code-block:: text

   myproject/
   ├── tasks.py              # Invoke tasks
   ├── docs/
   │   ├── conf.py
   │   ├── index.rst
   │   └── tasks/
   │       └── reference.rst # Task documentation
   └── src/
       └── myapp/

Invoke Tasks File
~~~~~~~~~~~~~~~~~

**tasks.py**:

.. code-block:: python

   from invoke import task
   
   @task
   def build(ctx):
       """Build the project"""
       ctx.run("python setup.py build")
   
   @task
   def test(ctx, verbose=False):
       """Run tests
       
       Args:
           verbose: Enable verbose output
       """
       cmd = "pytest"
       if verbose:
           cmd += " -v"
       ctx.run(cmd)
   
   @task
   def clean(ctx):
       """Clean build artifacts"""
       ctx.run("rm -rf build/ dist/ *.egg-info")

Documenting Tasks
-----------------

Basic Task Documentation
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Task Reference
   ==============
   
   .. invoke-tasks::
   
   This automatically documents all tasks from tasks.py.

Specific Task
~~~~~~~~~~~~~

Document a single task:

.. code-block:: rst

   .. invoke-task:: build
   
   Builds the entire project from source.

Task with Parameters
~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. invoke-task:: test
   
   The test task accepts the following parameters:
   
   - ``verbose``: Enable verbose output (default: False)

Task Groups
~~~~~~~~~~~

Organize tasks by namespace:

.. code-block:: rst

   Build Tasks
   ===========
   
   .. invoke-tasks:: build
   
   Testing Tasks
   =============
   
   .. invoke-tasks:: test

Practical Examples
------------------

Development Tasks
~~~~~~~~~~~~~~~~~

**tasks.py**:

.. code-block:: python

   from invoke import task
   
   @task
   def install(ctx, dev=False):
       """Install project dependencies
       
       Args:
           dev: Install development dependencies
       """
       cmd = "pip install -e ."
       if dev:
           cmd += "[dev]"
       ctx.run(cmd)
   
   @task
   def format(ctx, check=False):
       """Format code with black
       
       Args:
           check: Only check, don't modify files
       """
       cmd = "black"
       if check:
           cmd += " --check"
       cmd += " src/ tests/"
       ctx.run(cmd)
   
   @task
   def lint(ctx):
       """Run linters"""
       ctx.run("flake8 src/")
       ctx.run("mypy src/")
   
   @task(pre=[format, lint])
   def check(ctx):
       """Run all checks"""
       print("All checks passed!")

**Documentation** (tasks_reference.rst):

.. code-block:: rst

   Development Tasks
   =================
   
   .. invoke-tasks::
   
   Common Workflows
   ----------------
   
   **Setup development environment**:
   
   .. code-block:: bash
   
      invoke install --dev
   
   **Before committing**:
   
   .. code-block:: bash
   
      invoke check

Deployment Tasks
~~~~~~~~~~~~~~~~

**tasks.py**:

.. code-block:: python

   from invoke import task
   
   @task
   def deploy(ctx, env='staging', version=None):
       """Deploy application
       
       Args:
           env: Target environment (staging/production)
           version: Version to deploy (default: latest)
       """
       if version is None:
           version = "latest"
       
       print(f"Deploying {version} to {env}...")
       ctx.run(f"ansible-playbook -i inventory/{env} deploy.yml "
               f"--extra-vars 'version={version}'")
   
   @task
   def rollback(ctx, env='staging'):
       """Rollback to previous version
       
       Args:
           env: Target environment
       """
       ctx.run(f"ansible-playbook -i inventory/{env} rollback.yml")
   
   @task
   def status(ctx, env='staging'):
       """Check deployment status
       
       Args:
           env: Environment to check
       """
       ctx.run(f"ansible all -i inventory/{env} -m service "
               f"-a 'name=myapp state=started'")

**Documentation**:

.. code-block:: rst

   Deployment Tasks
   ================
   
   .. invoke-tasks::
   
   Deployment Workflow
   -------------------
   
   1. **Deploy to staging**:
   
      .. code-block:: bash
      
         invoke deploy --env=staging
   
   2. **Verify deployment**:
   
      .. code-block:: bash
      
         invoke status --env=staging
   
   3. **Deploy to production**:
   
      .. code-block:: bash
      
         invoke deploy --env=production --version=1.2.3
   
   4. **Rollback if needed**:
   
      .. code-block:: bash
      
         invoke rollback --env=production

Documentation Tasks
~~~~~~~~~~~~~~~~~~~

**tasks.py**:

.. code-block:: python

   from invoke import task
   
   @task
   def docs_build(ctx, clean=False):
       """Build documentation
       
       Args:
           clean: Clean before building
       """
       if clean:
           ctx.run("cd docs && make clean")
       ctx.run("cd docs && make html")
   
   @task
   def docs_serve(ctx, port=8000):
       """Serve documentation locally
       
       Args:
           port: Port to serve on
       """
       ctx.run(f"cd docs/_build/html && python -m http.server {port}")
   
   @task
   def docs_deploy(ctx):
       """Deploy documentation to GitHub Pages"""
       ctx.run("cd docs && make html")
       ctx.run("ghp-import -p docs/_build/html")

Task Namespaces
---------------

Organizing with Namespaces
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**tasks.py**:

.. code-block:: python

   from invoke import Collection, task
   
   @task
   def build_docs(ctx):
       """Build documentation"""
       ctx.run("make html")
   
   @task
   def serve_docs(ctx):
       """Serve documentation"""
       ctx.run("python -m http.server")
   
   # Create namespace
   docs_ns = Collection('docs')
   docs_ns.add_task(build_docs, 'build')
   docs_ns.add_task(serve_docs, 'serve')
   
   @task
   def test_unit(ctx):
       """Run unit tests"""
       ctx.run("pytest tests/unit")
   
   @task
   def test_integration(ctx):
       """Run integration tests"""
       ctx.run("pytest tests/integration")
   
   test_ns = Collection('test')
   test_ns.add_task(test_unit, 'unit')
   test_ns.add_task(test_integration, 'integration')
   
   # Root namespace
   ns = Collection()
   ns.add_collection(docs_ns)
   ns.add_collection(test_ns)

**Documentation**:

.. code-block:: rst

   Task Reference
   ==============
   
   Documentation Tasks
   -------------------
   
   .. invoke-tasks:: docs
   
   Testing Tasks
   -------------
   
   .. invoke-tasks:: test

Advanced Features
-----------------

Pre and Post Tasks
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from invoke import task
   
   @task
   def clean(ctx):
       """Clean build directory"""
       ctx.run("rm -rf build/")
   
   @task
   def compile(ctx):
       """Compile source code"""
       ctx.run("gcc -o app src/*.c")
   
   @task(pre=[clean], post=[compile])
   def build(ctx):
       """Build project (clean, build, compile)"""
       print("Building project...")

Default Tasks
~~~~~~~~~~~~~

.. code-block:: python

   from invoke import Collection, task
   
   @task(default=True)
   def help(ctx):
       """Show help (default task)"""
       ctx.run("invoke --list")
   
   ns = Collection()
   ns.add_task(help)

Task Dependencies
~~~~~~~~~~~~~~~~~

.. code-block:: python

   @task
   def install_deps(ctx):
       """Install dependencies"""
       ctx.run("pip install -r requirements.txt")
   
   @task
   def setup_db(ctx):
       """Setup database"""
       ctx.run("python manage.py migrate")
   
   @task(pre=[install_deps, setup_db])
   def setup(ctx):
       """Complete project setup"""
       print("Setup complete!")

Configuration
~~~~~~~~~~~~~

.. code-block:: python

   from invoke import task, Collection
   
   @task
   def deploy(ctx):
       """Deploy using configured values"""
       host = ctx.config.deploy.host
       user = ctx.config.deploy.user
       ctx.run(f"ssh {user}@{host} 'deploy.sh'")
   
   ns = Collection()
   ns.add_task(deploy)
   
   # Configure defaults
   ns.configure({
       'deploy': {
           'host': 'example.com',
           'user': 'deployer'
       }
   })

Best Practices
--------------

Task Documentation
~~~~~~~~~~~~~~~~~~

Write comprehensive docstrings:

.. code-block:: python

   @task
   def deploy(ctx, env='staging', version=None, dry_run=False):
       """Deploy application to specified environment
       
       This task deploys the application to the target environment
       using Ansible playbooks. It supports versioning and dry-run
       mode for testing.
       
       Args:
           env: Target environment (staging, production)
           version: Version to deploy (default: latest)
           dry_run: Run without making changes
       
       Examples:
           Deploy latest to staging:
               invoke deploy
           
           Deploy specific version to production:
               invoke deploy --env=production --version=1.2.3
           
           Test deployment without changes:
               invoke deploy --dry-run
       """
       # Implementation...

Task Organization
~~~~~~~~~~~~~~~~~

Structure tasks logically:

.. code-block:: python

   # tasks/__init__.py
   from invoke import Collection
   from . import build, test, docs, deploy
   
   ns = Collection()
   ns.add_collection(build)
   ns.add_collection(test)
   ns.add_collection(docs)
   ns.add_collection(deploy)

Error Handling
~~~~~~~~~~~~~~

.. code-block:: python

   @task
   def test(ctx, warn=True):
       """Run tests (continue on failure if warn=True)"""
       result = ctx.run("pytest", warn=warn)
       if result.failed and not warn:
           raise Exit("Tests failed!", code=1)

Troubleshooting
---------------

Tasks Not Found
~~~~~~~~~~~~~~~

Check module path:

.. code-block:: python

   # conf.py
   import sys
   import os
   
   # Add project root to path
   sys.path.insert(0, os.path.abspath('..'))
   
   invoke_tasks_module = 'tasks'

Import Errors
~~~~~~~~~~~~~

Ensure Invoke is installed:

.. code-block:: bash

   pip install invoke invoke-sphinx

.. code-block:: python

   # Verify installation
   python -c "import invoke; print(invoke.__version__)"

Integration Examples
--------------------

CI/CD Integration
~~~~~~~~~~~~~~~~~

**GitHub Actions**:

.. code-block:: yaml

   name: CI
   
   on: [push]
   
   jobs:
     test:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v2
         - uses: actions/setup-python@v2
         - name: Install dependencies
           run: pip install invoke
         - name: Run checks
           run: invoke check

Makefile Alternative
~~~~~~~~~~~~~~~~~~~~

Replace Make with Invoke:

.. code-block:: python

   # tasks.py - Drop-in Make replacement
   from invoke import task
   
   @task
   def all(ctx):
       """Build everything (like 'make all')"""
       ctx.run("invoke build test")
   
   @task
   def clean(ctx):
       """Clean (like 'make clean')"""
       ctx.run("rm -rf build/ *.pyc")

See Also
--------

**Related Extensions**:

- :doc:`ansible-sphinx-example` - Ansible documentation
- :doc:`sphinx-autodoc-defaultargs-example` - Python autodoc
- :doc:`sphinx-prompt-example` - Command prompts

**External Resources**:

- `Invoke Documentation <https://www.pyinvoke.org/>`_
- `Task Organization <https://docs.pyinvoke.org/en/stable/concepts/namespaces.html>`_

Summary
-------

invoke-sphinx provides Invoke task documentation:

**Key Capabilities**:

✅ Automatic task extraction
✅ Parameter documentation
✅ Namespace support
✅ Usage example generation
✅ Cross-referencing

**Common Use Cases**:

- Project automation docs
- Build system documentation
- Deployment task reference
- Development workflow docs
- CI/CD task documentation

Perfect for documenting Python-based automation tasks in your Sphinx documentation.
