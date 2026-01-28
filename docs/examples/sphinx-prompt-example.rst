Sphinx-Prompt Example
=====================

This page demonstrates the **sphinx-prompt** extension for creating styled command prompts and input/output examples.

.. contents:: Contents
   :local:
   :depth: 2


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

See Also
--------

- :doc:`../tutorials/packages/sphinx-prompt` - Complete tutorial
- GitHub repository: https://github.com/sbrunner/sphinx-prompt
