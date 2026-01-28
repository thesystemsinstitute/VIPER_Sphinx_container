Sphinx-Prompt Tutorial
======================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-prompt/>`_
   - `API Documentation <../../pdoc/sphinx_prompt/index.html>`_
   - `Manual <https://sphinx-prompt.readthedocs.io/>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinx-prompt to create formatted command-line prompts and shell examples in your documentation.

What is Sphinx-Prompt?
-----------------------
sphinx-prompt is a Sphinx extension that provides:

- Formatted shell prompts
- Multiple shell types (bash, cmd, powershell, python)
- Syntax highlighting
- Copy-friendly output
- Customizable prompts
- Language-specific styling
- Auto-numbering
- Continuation support
- Output display
- Works with sphinx-copybutton

This makes it easy to create consistent, professional-looking shell examples.

The sphinx-prompt extension provides directives for creating command-line prompts with proper styling for shells, REPLs, and interactive sessions.


Installation
------------

sphinx-prompt is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinx_prompt; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_prompt',
   ]

Integration with Copybutton
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = [
       'sphinx_prompt',
       'sphinx_copybutton',
   ]
   
   # Copybutton will automatically handle prompt stripping


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Basic Setup
~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx-prompt',
   ]

Custom Styles
~~~~~~~~~~~~~

.. code-block:: python

   prompt_default_language = 'bash'
   prompt_default_prompt = '$'

Basic Usage
-----------

Bash Prompt
~~~~~~~~~~~

.. code-block:: rst

   .. prompt:: bash
   
      ls -la
      cd myproject
      python main.py

Python Prompt
~~~~~~~~~~~~~

.. code-block:: rst

   .. prompt:: python
   
      import numpy as np
      data = np.array([1, 2, 3])
      print(data.mean())

PowerShell Prompt
~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. prompt:: powershell
   
      Get-ChildItem
      Set-Location C:\Projects
      python script.py

   Installation
   ============
   
   Using pip
   ---------
   
   .. prompt:: bash $
   
      pip install mypackage
      pip install mypackage[all]
   
   Using conda
   -----------
   
   .. prompt:: bash $
   
      conda install -c conda-forge mypackage
   
   From Source
   -----------
   
   .. prompt:: bash $
   
      git clone https://github.com/user/mypackage.git
      cd mypackage
      pip install -e .
   
   Verify Installation
   -------------------
   
   .. prompt:: python >>>
   
      import mypackage
      print(mypackage.__version__)
      mypackage.test()

Example 2: Quick Start Guide
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/quickstart.rst``:

.. code-block:: rst

   Quick Start
   ===========
   
   Setup
   -----
   
   Create a new project:
   
   .. prompt:: bash $
   
      mkdir myproject
      cd myproject
      python -m venv venv
   
   Activate virtual environment:
   
   On Linux/Mac:
   
   .. prompt:: bash $
   
      source venv/bin/activate
   
   On Windows:
   
   .. prompt:: powershell >
   
      .\venv\Scripts\Activate.ps1
   
   Install dependencies:
   
   .. prompt:: bash $
   
      pip install -r requirements.txt
   
   Basic Usage
   -----------
   
   Interactive Python session:
   
   .. prompt:: python >>>
   
      from mylib import Client
      client = Client(api_key="your-key")
      data = client.fetch_data()
      print(len(data))
   
   Run the application:
   
   .. prompt:: bash $
   
      python app.py --port 8000

Example 3: Docker Commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/docker.rst``:

.. code-block:: rst

   Docker Usage
   ============
   
   Build Image
   -----------
   
   .. prompt:: bash $
   
      docker build -t myapp:latest .
      docker tag myapp:latest myapp:1.0.0
   
   Run Container
   -------------
   
   Basic run:
   
   .. prompt:: bash $
   
      docker run -d -p 8000:8000 myapp:latest
   
   With volume mounts:
   
   .. prompt:: bash $
   
      docker run -d \
        -v $(pwd)/data:/app/data \
        -v $(pwd)/config:/app/config \
        -p 8000:8000 \
        myapp:latest
   
   Interactive shell:
   
   .. prompt:: bash $
   
      docker run -it --rm myapp:latest /bin/sh
   
   Docker Compose
   --------------
   
   .. prompt:: bash $
   
      docker-compose up -d
      docker-compose logs -f
      docker-compose down

Example 4: Development Workflow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/development.rst``:

.. code-block:: rst

   Development Guide
   =================
   
   Clone and Setup
   ---------------
   
   .. prompt:: bash $
   
      git clone https://github.com/user/project.git
      cd project
      python -m venv venv
      source venv/bin/activate
      pip install -e .[dev]
   
   Running Tests
   -------------
   
   .. prompt:: bash $
   
      pytest
      pytest tests/test_api.py -v
      pytest --cov=mypackage --cov-report=html
   
   Code Quality
   ------------
   
   Format code:
   
   .. prompt:: bash $
   
      black mypackage/
      isort mypackage/
   
   Type checking:
   
   .. prompt:: bash $
   
      mypy mypackage/
   
   Linting:
   
   .. prompt:: bash $
   
      flake8 mypackage/
      pylint mypackage/
   
   Build Documentation
   -------------------
   
   .. prompt:: bash $
   
      cd docs
      make html
      python -m http.server -d _build/html

Advanced Features
-----------------

Custom Prompts
~~~~~~~~~~~~~~

.. code-block:: rst

   .. prompt:: bash [user@host]$
   
      echo "Custom prompt"
      pwd

Multi-line Commands
~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. prompt:: bash $
   
      docker run --rm \
        -v $(pwd):/project \
        -w /project \
        myimage:latest \
        command

Show Output
~~~~~~~~~~~

.. code-block:: rst

   .. prompt:: bash $ auto
   
      echo "Hello, World!"
      Hello, World!
      ls -l
      total 16
      -rw-r--r-- 1 user user 1234 Jan 1 12:00 file.txt

Numbered Prompts
~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. prompt:: python >>> auto
   
      for i in range(3):
      ...     print(i)
      0
      1
      2

Multiple Languages
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Bash:
   
   .. prompt:: bash $
   
      python script.py
   
   PowerShell:
   
   .. prompt:: powershell >
   
      python script.py
   
   CMD:
   
   .. prompt:: cmd >
   
      python script.py

Language-Specific Prompts
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. prompt:: bash $,#
   
      $ echo "User command"
      User command
      # echo "Root command"
      Root command

Modifiers
~~~~~~~~~

.. code-block:: rst

   .. prompt:: bash $ auto
      :prompts: $, >>>
   
      $ python
      >>> import sys
      >>> print(sys.version)
      3.11.0

Docker Integration
------------------

Build Documentation
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     kensai-sphinx:latest \
     sphinx-build -b html /project/docs /project/docs/_build/html

Test Prompts
~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     -p 8000:8000 \
     kensai-sphinx:latest \
     sh -c "sphinx-build -b html /project/docs /project/docs/_build/html && \
            python -m http.server -d /project/docs/_build/html"

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Build Documentation
   
   on: [push]
   
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Build Docs
           run: |
             docker run --rm -v $(pwd):/project \
               kensai-sphinx:latest \
               sphinx-build -b html /project/docs /project/docs/_build/html
         
         - name: Deploy
           uses: peaceiris/actions-gh-pages@v3
           with:
             github_token: ${{ secrets.GITHUB_TOKEN }}
             publish_dir: ./docs/_build/html

Best Practices
--------------

1. **Use Consistent Prompts**
   
   Pick one style and stick with it:
   
   .. code-block:: rst
   
      .. prompt:: bash $

2. **Show Both Input and Output**
   
   Use ``auto`` modifier when helpful

3. **Combine with Copybutton**
   
   Users can copy commands easily

4. **Match Your OS**
   
   Use appropriate shell for your platform

5. **Break Long Commands**
   
   Use backslashes for readability

6. **Add Context**
   
   Explain what commands do

Troubleshooting
---------------

Prompt Not Showing
~~~~~~~~~~~~~~~~~~

**Solution:**

Check extension is loaded:

.. code-block:: python

   extensions = ['sphinx_prompt']

Wrong Syntax Highlighting
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Solution:**

Specify correct language:

.. code-block:: rst

   .. prompt:: bash
   
   Not:
   
   .. prompt:: shell

Copy Button Copying Prompt
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Solution:**

sphinx-copybutton should auto-detect sphinx-prompt. If not, configure:

.. code-block:: python

   copybutton_prompt_text = r">>> |\.\.\. |\$ "

Multi-line Not Working
~~~~~~~~~~~~~~~~~~~~~~

**Solution:**

Use continuation character:

.. code-block:: rst

   .. prompt:: bash $
   
      docker run --rm \
        -v $(pwd):/app \
        myimage

Next Steps
----------

1. Enable sphinx-prompt
2. Choose appropriate shell types
3. Create consistent examples
4. Test with sphinx-copybutton
5. Document all CLI commands


Practical Examples
------------------

Basic Usage
-----------

Bash Prompt
~~~~~~~~~~~

.. prompt:: bash $

   ls -la
   cd myproject
   python script.py

Python REPL
~~~~~~~~~~~

.. prompt:: python >>>

   x = 10
   y = 20
   print(x + y)

PowerShell
~~~~~~~~~~

.. prompt:: powershell PS>

   Get-Process
   Set-Location C:\Projects
   python.exe script.py

Advanced Features
-----------------

Custom Prompts
~~~~~~~~~~~~~~

.. prompt:: bash [user@host]$

   whoami
   hostname
   pwd

With Output
~~~~~~~~~~~

.. prompt:: bash $
   :prompts: $, >

   echo "Hello"
   Hello
   cat file.txt
   > File contents here

Multi-line Commands
~~~~~~~~~~~~~~~~~~~

.. prompt:: bash $

   python -c "
   import sys
   print(sys.version)
   "

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx-prompt',
   ]

Custom Styles
~~~~~~~~~~~~~

.. code-block:: python

   prompt_default_language = 'bash'
   prompt_default_prompt = '$'

Examples
--------

Docker Commands
~~~~~~~~~~~~~~~

.. prompt:: bash $

   docker build -t myapp:latest .
   docker run -p 8000:8000 myapp:latest

Git Workflow
~~~~~~~~~~~~

.. prompt:: bash $

   git add .
   git commit -m "Update documentation"
   git push origin main

Package Installation
~~~~~~~~~~~~~~~~~~~~

.. prompt:: bash $

   pip install sphinx
   pip install sphinx-prompt
   pip list


Practical Examples
------------------

Basic Usage
-----------

Bash Prompt
~~~~~~~~~~~

.. prompt:: bash $

   ls -la
   cd myproject
   python script.py

Python REPL
~~~~~~~~~~~

.. prompt:: python >>>

   x = 10
   y = 20
   print(x + y)

PowerShell
~~~~~~~~~~

.. prompt:: powershell PS>

   Get-Process
   Set-Location C:\Projects
   python.exe script.py

Advanced Features
-----------------

Custom Prompts
~~~~~~~~~~~~~~

.. prompt:: bash [user@host]$

   whoami
   hostname
   pwd

With Output
~~~~~~~~~~~

.. prompt:: bash $
   :prompts: $, >

   echo "Hello"
   Hello
   cat file.txt
   > File contents here

Multi-line Commands
~~~~~~~~~~~~~~~~~~~

.. prompt:: bash $

   python -c "
   import sys
   print(sys.version)
   "

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx-prompt',
   ]

Custom Styles
~~~~~~~~~~~~~

.. code-block:: python

   prompt_default_language = 'bash'
   prompt_default_prompt = '$'

Examples
--------

Docker Commands
~~~~~~~~~~~~~~~

.. prompt:: bash $

   docker build -t myapp:latest .
   docker run -p 8000:8000 myapp:latest

Git Workflow
~~~~~~~~~~~~

.. prompt:: bash $

   git add .
   git commit -m "Update documentation"
   git push origin main

Package Installation
~~~~~~~~~~~~~~~~~~~~

.. prompt:: bash $

   pip install sphinx
   pip install sphinx-prompt
   pip list


Practical Examples
------------------

Basic Usage
-----------

Bash Prompt
~~~~~~~~~~~

.. prompt:: bash $

   ls -la
   cd myproject
   python script.py

Python REPL
~~~~~~~~~~~

.. prompt:: python >>>

   x = 10
   y = 20
   print(x + y)

PowerShell
~~~~~~~~~~

.. prompt:: powershell PS>

   Get-Process
   Set-Location C:\Projects
   python.exe script.py

Advanced Features
-----------------

Custom Prompts
~~~~~~~~~~~~~~

.. prompt:: bash [user@host]$

   whoami
   hostname
   pwd

With Output
~~~~~~~~~~~

.. prompt:: bash $
   :prompts: $, >

   echo "Hello"
   Hello
   cat file.txt
   > File contents here

Multi-line Commands
~~~~~~~~~~~~~~~~~~~

.. prompt:: bash $

   python -c "
   import sys
   print(sys.version)
   "

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx-prompt',
   ]

Custom Styles
~~~~~~~~~~~~~

.. code-block:: python

   prompt_default_language = 'bash'
   prompt_default_prompt = '$'

Examples
--------

Docker Commands
~~~~~~~~~~~~~~~

.. prompt:: bash $

   docker build -t myapp:latest .
   docker run -p 8000:8000 myapp:latest

Git Workflow
~~~~~~~~~~~~

.. prompt:: bash $

   git add .
   git commit -m "Update documentation"
   git push origin main

Package Installation
~~~~~~~~~~~~~~~~~~~~

.. prompt:: bash $

   pip install sphinx
   pip install sphinx-prompt
   pip list

Additional Resources
--------------------
- :doc:`sphinx-copybutton` - Add copy buttons
- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `Sphinx Prompt Documentation <https://sbrunner.github.io/sphinx-prompt/>`_
- :doc:`../tutorials/packages/sphinx-prompt` - Complete tutorial
- GitHub repository: https://github.com/sbrunner/sphinx-prompt

