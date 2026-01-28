Invoke-Sphinx Tutorial
=======================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/invoke-sphinx/>`_
   - :doc:`See Working Example <../../examples/invoke-sphinx-example>`


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

Practical Examples
------------------

Example 1: Simple Documentation Build
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``tasks.py``:

.. code-block:: python

   from invoke import task
   
   @task
   def docs(c):
       """Build HTML documentation."""
       c.run('sphinx-build -b html docs docs/_build/html')
   
   @task
   def docs_clean(c):
       """Clean documentation build."""
       c.run('rm -rf docs/_build')

Usage:

.. code-block:: bash

   # Build docs
   invoke docs
   
   # Clean
   invoke docs-clean

Example 2: Multi-Builder Tasks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``tasks.py``:

.. code-block:: python

   from invoke import task
   
   DOCS_DIR = 'docs'
   BUILD_DIR = 'docs/_build'
   
   @task
   def docs_html(c):
       """Build HTML documentation."""
       c.run(f'sphinx-build -b html {DOCS_DIR} {BUILD_DIR}/html')
   
   @task
   def docs_pdf(c):
       """Build PDF documentation."""
       c.run(f'sphinx-build -b latex {DOCS_DIR} {BUILD_DIR}/latex')
       c.run(f'cd {BUILD_DIR}/latex && make')
   
   @task
   def docs_epub(c):
       """Build EPUB documentation."""
       c.run(f'sphinx-build -b epub {DOCS_DIR} {BUILD_DIR}/epub')
   
   @task
   def docs_man(c):
       """Build man pages."""
       c.run(f'sphinx-build -b man {DOCS_DIR} {BUILD_DIR}/man')
   
   @task(docs_html, docs_pdf, docs_epub)
   def docs_all(c):
       """Build all documentation formats."""
       print("All documentation formats built!")

Usage:

.. code-block:: bash

   invoke docs-html
   invoke docs-pdf
   invoke docs-all

Example 3: Advanced Build Workflow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``tasks.py``:

.. code-block:: python

   from invoke import task
   import os
   from pathlib import Path
   
   DOCS_DIR = Path('docs')
   BUILD_DIR = DOCS_DIR / '_build'
   SOURCE_DIR = Path('src')
   
   @task
   def docs_clean(c):
       """Clean documentation build directory."""
       if BUILD_DIR.exists():
           c.run(f'rm -rf {BUILD_DIR}')
           print(f"✓ Cleaned {BUILD_DIR}")
   
   @task
   def docs_apidoc(c):
       """Generate API documentation from source."""
       api_dir = DOCS_DIR / 'api'
       c.run(f'sphinx-apidoc -f -o {api_dir} {SOURCE_DIR}')
       print(f"✓ Generated API docs in {api_dir}")
   
   @task
   def docs_spell(c):
       """Check spelling in documentation."""
       c.run(f'sphinx-build -b spelling {DOCS_DIR} {BUILD_DIR}/spelling')
       print("✓ Spell check complete")
   
   @task
   def docs_linkcheck(c):
       """Check external links in documentation."""
       c.run(f'sphinx-build -b linkcheck {DOCS_DIR} {BUILD_DIR}/linkcheck')
       print("✓ Link check complete")
   
   @task(pre=[docs_clean, docs_apidoc])
   def docs_build(c, builder='html'):
       """Build documentation with specified builder."""
       c.run(f'sphinx-build -b {builder} {DOCS_DIR} {BUILD_DIR}/{builder}')
       print(f"✓ Built {builder} documentation")
   
   @task
   def docs_serve(c, port=8000):
       """Serve documentation locally."""
       html_dir = BUILD_DIR / 'html'
       if not html_dir.exists():
           print("Building documentation first...")
           docs_build(c)
       
       c.run(f'python -m http.server {port} --directory {html_dir}')
   
   @task
   def docs_watch(c):
       """Watch for changes and rebuild."""
       try:
           c.run(f'sphinx-autobuild {DOCS_DIR} {BUILD_DIR}/html --port 8000')
       except KeyboardInterrupt:
           print("\n✓ Stopped watching")
   
   @task(pre=[docs_build, docs_spell, docs_linkcheck])
   def docs_test(c):
       """Run all documentation tests."""
       print("✓ All documentation tests passed")

Usage:

.. code-block:: bash

   # Full workflow
   invoke docs-build
   
   # Check spelling
   invoke docs-spell
   
   # Check links
   invoke docs-linkcheck
   
   # Run all tests
   invoke docs-test
   
   # Watch mode
   invoke docs-watch

Example 4: Release Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``tasks.py``:

.. code-block:: python

   from invoke import task
   import datetime
   from pathlib import Path
   
   @task
   def docs_version(c):
       """Update version in documentation."""
       # Read version from setup.py or __init__.py
       result = c.run('python setup.py --version', hide=True)
       version = result.stdout.strip()
       
       # Update conf.py
       conf_file = Path('docs/conf.py')
       content = conf_file.read_text()
       content = content.replace(
           'version = ',
           f"version = '{version}'\n# "
       )
       conf_file.write_text(content)
       
       print(f"✓ Updated version to {version}")
   
   @task
   def docs_changelog(c):
       """Generate changelog from git."""
       today = datetime.date.today().strftime('%Y-%m-%d')
       
       # Get git log
       result = c.run(
           'git log --pretty=format:"- %s (%an, %ar)" --since="1 month ago"',
           hide=True
       )
       
       changelog = f"""
   Changelog - {today}
   {'=' * (len(today) + 12)}
   
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

Additional Resources
--------------------

- :doc:`sphinx-autobuild` - Auto-rebuild on changes
- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `Invoke Documentation <https://www.pyinvoke.org/>`_
- `Task Automation Guide <https://www.pyinvoke.org/concepts/invoking-tasks.html>`_
