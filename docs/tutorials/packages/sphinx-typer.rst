Sphinx Typer Tutorial
=====================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinxcontrib-typer/>`_
   - :doc:`See Working Example <../../examples/sphinx-typer-example>`
   - `Official Documentation <https://sphinxcontrib-typer.readthedocs.io/>`_

This tutorial demonstrates how to use sphinx-typer in your Sphinx documentation.

What is Sphinx Typer?
---------------------

sphinx-typer is a Sphinx extension that provides:

- Document Typer CLIs
- Easy integration with Sphinx
- Comprehensive configuration options
- Professional documentation output

Installation
------------

sphinx-typer is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinxcontrib.typer; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``docs/conf.py``:

.. code-block:: python

   extensions = [
       'sphinxcontrib.typer',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinxcontrib.typer']
   
   # Configuration options
   # typer extension uses directives

Basic Usage
-----------

Getting Started
~~~~~~~~~~~~~~~

Document a Typer CLI:

.. code-block:: rst

   .. typer:: mypackage.cli:app
      :prog: myapp
      :show-nested:

Document Commands
~~~~~~~~~~~~~~~~~

Document specific commands:

.. code-block:: rst

   .. typer:: mypackage.cli:app
      :prog: myapp
      :commands: deploy, config

Common Use Cases
----------------

Full CLI Documentation
~~~~~~~~~~~~~~~~~~~~~~

Document complete Typer CLI:

.. code-block:: rst

   .. typer:: myapp.cli:app
      :prog: myapp
      :show-nested:
      :make-sections:

Command Documentation
~~~~~~~~~~~~~~~~~~~~~

Document individual commands:

.. code-block:: rst

   .. typer:: myapp.cli:deploy_command
      :prog: myapp deploy

Advanced Features
-----------------

Type Hints
~~~~~~~~~~

Typer automatically uses type hints for documentation.

Rich Formatting
~~~~~~~~~~~~~~~

Leverage Typer's rich console output:

.. code-block:: rst

   .. typer:: myapp.cli:app
      :prog: myapp
      :show-nested:

Best Practices
--------------

Tips and Guidelines
~~~~~~~~~~~~~~~~~~~

- Use type hints for all parameters
- Add comprehensive docstrings
- Document all commands
- Include usage examples
- Leverage Typer's automatic validation

Troubleshooting
---------------

Common Issues
~~~~~~~~~~~~~

**Issue**: CLI not found

**Solution**: Ensure the Typer app path is correct.

**Issue**: Type hints not showing

**Solution**: Check that type hints are properly defined.

Additional Resources
--------------------

- :doc:`Working Example <../../examples/sphinx-typer-example>`
- `PyPI Package <https://pypi.org/project/sphinxcontrib-typer/>`_
- `Official Documentation <https://sphinxcontrib-typer.readthedocs.io/>`_
