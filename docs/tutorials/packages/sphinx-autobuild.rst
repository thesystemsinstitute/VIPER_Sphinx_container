Sphinx-Autobuild Tutorial
==========================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-autobuild/>`_
   - `Official Documentation <https://sphinx-autobuild.readthedocs.io/>`_
   - :doc:`See Working Example <../../examples/sphinx-autobuild-example>`


This tutorial demonstrates how to use sphinx-autobuild to automatically rebuild and reload your documentation during development.

What is Sphinx-Autobuild?
--------------------------

sphinx-autobuild is a development tool that provides:

- Automatic documentation rebuild
- Live browser reload
- Watch file changes
- Built-in web server
- Instant preview
- Hot reloading
- Multiple file format support
- Ignore patterns
- Custom build commands
- Development mode optimization

This dramatically speeds up the documentation writing workflow.

Installation
------------

sphinx-autobuild is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinx_autobuild; print('Installed')"

Configuration
-------------

Basic Usage
~~~~~~~~~~~

No configuration needed! Just run:

.. code-block:: bash

   sphinx-autobuild docs docs/_build/html

This starts a server at ``http://127.0.0.1:8000`` that auto-rebuilds on file changes.

Advanced Options
~~~~~~~~~~~~~~~~

.. code-block:: bash

   sphinx-autobuild docs docs/_build/html \
     --port 8080 \
     --host 0.0.0.0 \
     --ignore "*.tmp" \
     --ignore "*.swp" \
     --open-browser \
     --delay 1 \
     --watch ../mypackage

Basic Usage
-----------

Start Development Server
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   cd your-project
   sphinx-autobuild docs docs/_build/html

Open ``http://127.0.0.1:8000`` in your browser. Edit any RST file and watch it reload automatically!

Custom Port
~~~~~~~~~~~

.. code-block:: bash

   sphinx-autobuild docs docs/_build/html --port 8080

Open Browser Automatically
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   sphinx-autobuild docs docs/_build/html --open-browser

Practical Examples
------------------

Example 1: Standard Development Setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create ``dev.sh``:

.. code-block:: bash

   #!/bin/bash
   # Development server script
   
   sphinx-autobuild docs docs/_build/html \
     --port 8000 \
     --host 0.0.0.0 \
     --open-browser \
     --ignore "*.tmp" \
     --ignore "*.swp" \
     --ignore "*~" \
     --watch mypackage

Make it executable and run:

.. code-block:: bash

   chmod +x dev.sh
   ./dev.sh

Example 2: Docker Development
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docker-compose.yml``:

.. code-block:: yaml

   version: '3.8'
   
   services:
     docs:
       image: kensai-sphinx:latest
       command: sphinx-autobuild /project/docs /project/docs/_build/html --host 0.0.0.0
       volumes:
         - .:/project
       ports:
         - "8000:8000"
       environment:
         - PYTHONUNBUFFERED=1

Run with:

.. code-block:: bash

   docker-compose up docs

Access at ``http://localhost:8000``

Example 3: Watch Source Code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Watch both docs and source code for changes:

.. code-block:: bash

   sphinx-autobuild docs docs/_build/html \
     --watch mypackage \
     --watch README.md \
     --watch CHANGELOG.md

Useful when you have:
- Docstrings in source code
- README included in docs
- Auto-generated API documentation

Example 4: Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create ``Makefile``:

.. code-block:: makefile

   .PHONY: dev clean serve
   
   # Development server with live reload
   dev:
   	sphinx-autobuild docs docs/_build/html \
   		--port 8000 \
   		--host 0.0.0.0 \
   		--open-browser \
   		--ignore "*.tmp" \
   		--ignore "*.swp" \
   		--ignore "*~" \
   		--ignore "*.pyc" \
   		--watch mypackage \
   		--delay 1 \
   		--re-ignore "_build/.*" \
   		--re-ignore ".git/.*"
   
   # Production build
   build:
   	sphinx-build -b html docs docs/_build/html
   
   # Clean build artifacts
   clean:
   	rm -rf docs/_build
   
   # Serve without auto-rebuild
   serve:
   	python -m http.server -d docs/_build/html 8000

Run development server:

.. code-block:: bash

   make dev

Example 5: Multiple Builders
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``watch_all.sh``:

.. code-block:: bash

   #!/bin/bash
   
   # Terminal 1: HTML builder
   sphinx-autobuild docs docs/_build/html --port 8000 &
   
   # Terminal 2: Markdown builder
   sphinx-autobuild docs docs/_build/markdown \
     -b markdown --port 8001 &
   
   # Terminal 3: Linkcheck
   while true; do
     sphinx-build -b linkcheck docs docs/_build/linkcheck
     sleep 300  # Check every 5 minutes
   done &
   
   wait

Advanced Features
-----------------

Custom Ignore Patterns
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   sphinx-autobuild docs docs/_build/html \
     --ignore "*.tmp" \
     --ignore "*.bak" \
     --re-ignore "_build/.*" \
     --re-ignore ".git/.*"

Custom Delay
~~~~~~~~~~~~

.. code-block:: bash

   # Wait 2 seconds before rebuilding
   sphinx-autobuild docs docs/_build/html --delay 2

Pre and Post Build Commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create ``conf.py`` hook:

.. code-block:: python

   # conf.py
   import subprocess
   
   def setup(app):
       # Run before build
       app.connect('builder-inited', lambda app: 
           subprocess.run(['python', 'generate_api.py']))
       
       # Run after build
       app.connect('build-finished', lambda app, exception:
           subprocess.run(['python', 'post_process.py']))

Watch External Files
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   sphinx-autobuild docs docs/_build/html \
     --watch ../README.md \
     --watch ../CHANGELOG.md \
     --watch ../mypackage

Custom Builder
~~~~~~~~~~~~~~

.. code-block:: bash

   # Use different builder
   sphinx-autobuild docs docs/_build/html -b singlehtml

Multiple Sphinx Options
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   sphinx-autobuild docs docs/_build/html \
     -D language=en \
     -D version=1.0 \
     -A project_name="My Project" \
     -t production

Docker Integration
------------------

Interactive Development
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm -it \
     -v $(pwd):/project \
     -p 8000:8000 \
     kensai-sphinx:latest \
     sphinx-autobuild /project/docs /project/docs/_build/html --host 0.0.0.0

``Dockerfile.dev``:

.. code-block:: dockerfile

   FROM kensai-sphinx:latest
   
   WORKDIR /project
   
   # Install dev dependencies
   RUN pip install sphinx-autobuild watchdog
   
   # Expose port
   EXPOSE 8000
   
   # Default command
   CMD ["sphinx-autobuild", "docs", "docs/_build/html", "--host", "0.0.0.0"]

Build and run:

.. code-block:: bash

   docker build -f Dockerfile.dev -t sphinx-dev .
   docker run --rm -it -v $(pwd):/project -p 8000:8000 sphinx-dev

VS Code Integration
-------------------

``.vscode/tasks.json``:

.. code-block:: json

   {
     "version": "2.0.0",
     "tasks": [
       {
         "label": "Sphinx Autobuild",
         "type": "shell",
         "command": "sphinx-autobuild",
         "args": [
           "docs",
           "docs/_build/html",
           "--open-browser"
         ],
         "problemMatcher": [],
         "isBackground": true,
         "presentation": {
           "reveal": "always",
           "panel": "new"
         }
       }
     ]
   }

Run with: ``Ctrl+Shift+B`` → "Sphinx Autobuild"

Best Practices
--------------

1. **Use Ignore Patterns**
   
   Ignore temp files and build artifacts:
   
   .. code-block:: bash
   
      --ignore "*.tmp" --ignore "*.swp"

2. **Watch Source Code**
   
   Monitor docstrings:
   
   .. code-block:: bash
   
      --watch mypackage

3. **Optimize Delay**
   
   Balance responsiveness vs rebuild frequency

4. **Use Docker for Isolation**
   
   Consistent environment

5. **Create Scripts**
   
   Save common commands

6. **Monitor Performance**
   
   Large projects may need longer delays

Troubleshooting
---------------

Port Already in Use
~~~~~~~~~~~~~~~~~~~

**Solution:**

Use different port:

.. code-block:: bash

   sphinx-autobuild docs docs/_build/html --port 8080

Or kill existing process:

.. code-block:: bash

   # Linux/Mac
   lsof -ti:8000 | xargs kill
   
   # Windows PowerShell
   Get-Process -Id (Get-NetTCPConnection -LocalPort 8000).OwningProcess | Stop-Process

Rebuilds Too Frequent
~~~~~~~~~~~~~~~~~~~~~

**Solution:**

Increase delay:

.. code-block:: bash

   sphinx-autobuild docs docs/_build/html --delay 3

Browser Not Reloading
~~~~~~~~~~~~~~~~~~~~~

**Solution:**

Check browser console for errors. Clear cache:

.. code-block:: bash

   # Hard reload in browser
   Ctrl+Shift+R  # Windows/Linux
   Cmd+Shift+R   # Mac

Changes Not Detected
~~~~~~~~~~~~~~~~~~~~

**Solution:**

Explicitly watch directories:

.. code-block:: bash

   sphinx-autobuild docs docs/_build/html --watch mypackage

Build Errors
~~~~~~~~~~~~

**Solution:**

Check Sphinx output in terminal. Fix errors before autobuild continues.

Performance Issues
~~~~~~~~~~~~~~~~~~

**Solution:**

Exclude large directories:

.. code-block:: bash

   sphinx-autobuild docs docs/_build/html \
     --ignore "_build/*" \
     --ignore ".git/*"

Next Steps
----------

1. Install sphinx-autobuild
2. Create development script
3. Configure ignore patterns
4. Watch source code directories
5. Integrate with editor

Additional Resources
--------------------

- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `Sphinx Autobuild Documentation <https://github.com/executablebooks/sphinx-autobuild>`_
- `Live Server Guide <https://www.sphinx-doc.org/en/master/tutorial/deploying.html>`_
