Invoke-Sphinx Tutorial
=======================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/invoke-sphinx/>`_
   - `API Documentation <../../pdoc/invoke_sphinx/index.html>`_
    - `Manual <https://invoke-sphinx.readthedocs.io>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use invoke-sphinx to integrate Invoke task automation with Sphinx documentation builds.

What is Invoke-Sphinx?
-----------------------
invoke-sphinx is a Sphinx extension that provides:

- Invoke task integration
- Build automation
- Custom build commands
- Task documentation
- Command-line interface
- Multi-builder support
- Watch mode integration
- Clean/build workflows
- Custom task definitions
- Project automation

This simplifies documentation builds using Python's Invoke task automation framework.

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

invoke-sphinx is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import invoke_sphinx; print('Installed')"

Prerequisites
-------------

Invoke must be installed:

.. code-block:: bash

   pip install invoke

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Create ``tasks.py`` in your project root:

.. code-block:: python

   from invoke import task
   from invoke_sphinx import build, clean
   
   @task
   def docs(c):
       """Build documentation."""
       build(c, 'html')

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

``tasks.py``:

.. code-block:: python

   from invoke import task
   from invoke_sphinx import build, clean, serve
   
   # Configuration
   DOCS_DIR = 'docs'
   BUILD_DIR = 'docs/_build'
   
   @task
   def docs_clean(c):
       """Clean documentation build."""
       clean(c, DOCS_DIR, BUILD_DIR)
   
   @task
   def docs_html(c):
       """Build HTML documentation."""
       build(c, 'html', sourcedir=DOCS_DIR, builddir=BUILD_DIR)
   
   @task
   def docs_pdf(c):
       """Build PDF documentation."""
       build(c, 'latexpdf', sourcedir=DOCS_DIR, builddir=BUILD_DIR)
   
   @task(pre=[docs_clean])
   def docs_rebuild(c):
       """Clean and rebuild documentation."""
       build(c, 'html', sourcedir=DOCS_DIR, builddir=BUILD_DIR)
   
   @task
   def docs_serve(c, port=8000):
       """Serve documentation locally."""
       serve(c, port=port, root=f'{BUILD_DIR}/html')
   
   @task
   def docs_watch(c):
       """Watch and rebuild documentation."""
       build(c, 'html', sourcedir=DOCS_DIR, builddir=BUILD_DIR, watch=True)


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

Basic Usage
-----------

Build Documentation
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   invoke docs

List Available Tasks
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   invoke --list

Clean Build
~~~~~~~~~~~

.. code-block:: bash

   invoke docs-clean

   Recent Changes
   --------------
   
   {result.stdout}
   """
       
       changelog_file = Path('docs/changelog.rst')
       changelog_file.write_text(changelog)
       
       print(f"✓ Generated changelog")
   
   @task(pre=[docs_version, docs_changelog, docs_clean])
   def docs_release(c):
       """Build release documentation."""
       # Build all formats
       c.run('invoke docs-build --builder html')
       c.run('invoke docs-build --builder pdf')
       
       # Package documentation
       c.run('tar -czf docs-release.tar.gz docs/_build/')
       
       print("✓ Release documentation ready")

Example 5: Docker Integration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``tasks.py``:

.. code-block:: python

   from invoke import task
   
   DOCKER_IMAGE = 'kensai-sphinx:latest'
   
   @task
   def docs_docker_build(c):
       """Build documentation in Docker container."""
       c.run(f'''
           docker run --rm \\
               -v $(pwd):/project \\
               {DOCKER_IMAGE} \\
               sphinx-build -b html /project/docs /project/docs/_build/html
       ''')
       print("✓ Built documentation in Docker")
   
   @task
   def docs_docker_serve(c, port=8000):
       """Serve documentation from Docker."""
       c.run(f'''
           docker run --rm \\
               -v $(pwd):/project \\
               -p {port}:{port} \\
               {DOCKER_IMAGE} \\
               sh -c "cd /project/docs/_build/html && python -m http.server {port}"
       ''')
   
   @task
   def docs_docker_shell(c):
       """Open shell in documentation Docker container."""
       c.run(f'''
           docker run --rm -it \\
               -v $(pwd):/project \\
               {DOCKER_IMAGE} \\
               sh
       ''')

Advanced Features
-----------------

Task Dependencies
~~~~~~~~~~~~~~~~~

.. code-block:: python

   @task(pre=[docs_clean, docs_apidoc])
   def docs_build(c):
       """Build docs after cleaning and generating API docs."""
       pass

Task Parameters
~~~~~~~~~~~~~~~

.. code-block:: python

   @task
   def docs_build(c, builder='html', jobs=1):
       """Build with custom builder and parallel jobs."""
       c.run(f'sphinx-build -b {builder} -j {jobs} docs docs/_build/{builder}')

Conditional Execution
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from pathlib import Path
   
   @task
   def docs_build(c):
       """Build documentation if needed."""
       build_dir = Path('docs/_build/html')
       
       if not build_dir.exists():
           c.run('sphinx-build -b html docs docs/_build/html')
       else:
           print("Documentation already built")

Docker Integration
------------------

Build in Container
~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Run invoke tasks in Docker
   docker run --rm -v $(pwd):/project \
     kensai-sphinx:latest \
     invoke docs-build

With Invoke Installed
~~~~~~~~~~~~~~~~~~~~~~

``Dockerfile.docs``:

.. code-block:: dockerfile

   FROM kensai-sphinx:latest
   
   # Install Invoke
   RUN pip install invoke
   
   WORKDIR /project
   
   # Copy tasks
   COPY tasks.py .
   
   CMD ["invoke", "docs-build"]

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Build Documentation
   
   on: [push]
   
   jobs:
     docs:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Set up Python
           uses: actions/setup-python@v4
           with:
             python-version: '3.11'
         
         - name: Install dependencies
           run: |
             pip install invoke sphinx
         
         - name: Build documentation
           run: invoke docs-build
         
         - name: Test documentation
           run: invoke docs-test
         
         - name: Deploy
           uses: peaceiris/actions-gh-pages@v3
           with:
             github_token: ${{ secrets.GITHUB_TOKEN }}
             publish_dir: ./docs/_build/html

GitLab CI
~~~~~~~~~

.. code-block:: yaml

   docs:
     image: python:3.11
     script:
       - pip install invoke sphinx
       - invoke docs-build
     artifacts:
       paths:
         - docs/_build/html

Best Practices
--------------

1. **Clear Task Names**
   
   Use descriptive names with prefixes

2. **Add Docstrings**
   
   Document what each task does

3. **Use Dependencies**
   
   Chain tasks with pre/post

4. **Handle Errors**
   
   Add error checking and messages

5. **Make Idempotent**
   
   Tasks should be safe to re-run

6. **Provide Defaults**
   
   Sensible default parameters

Troubleshooting
---------------

Invoke Not Found
~~~~~~~~~~~~~~~~

**Solution:**

Install Invoke:

.. code-block:: bash

   pip install invoke

Task Not Running
~~~~~~~~~~~~~~~~

**Solution:**

Check task name:

.. code-block:: bash

   invoke --list

Verify function decorator:

.. code-block:: python

   @task  # Must have decorator
   def docs_build(c):
       pass

Build Fails
~~~~~~~~~~~

**Solution:**

Check paths are correct:

.. code-block:: python

   DOCS_DIR = 'docs'  # Relative to tasks.py

Run with verbose output:

.. code-block:: bash

   invoke docs-build --echo

Docker Issues
~~~~~~~~~~~~~

**Solution:**

Check volume mount:

.. code-block:: bash

   docker run --rm -v $(pwd):/project ...

Verify working directory in container.

Next Steps
----------

1. Create tasks.py file
2. Define documentation tasks
3. Test tasks locally
4. Integrate with CI/CD
5. Document workflow


Practical Examples
------------------

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

Additional Resources
--------------------
- :doc:`sphinx-autobuild` - Auto-rebuild on changes
- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `Invoke Documentation <https://www.pyinvoke.org/>`_
- `Task Automation Guide <https://www.pyinvoke.org/concepts/invoking-tasks.html>`_
**Related Extensions**:
- :doc:`ansible-sphinx-example` - Ansible documentation
- :doc:`sphinx-autodoc-defaultargs-example` - Python autodoc
- :doc:`sphinx-prompt-example` - Command prompts
**External Resources**:
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

