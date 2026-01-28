Sphinx Click Tutorial
=====================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-click/>`_
   - `API Documentation <../../pdoc/sphinx_click/index.html>`_
   - `Manual <https://sphinx-click.readthedocs.io/>`_
   - :doc:`Working Example <../../examples/sphinx-click-example>`


.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinx-click in your Sphinx documentation.

What is Sphinx Click?
----------------------

sphinx-click is a Sphinx extension that provides:

- Document Click CLIs
- Easy integration with Sphinx
- Comprehensive configuration options
- Professional documentation output

sphinx-click provides:

- Document Click CLIs
- Integration with Sphinx documentation
- Flexible configuration options
- Professional output formatting

Key Features
~~~~~~~~~~~~

- **Automatic Documentation**: Generate docs from Click decorators
- **Nested Commands**: Support for command groups
- **Options & Arguments**: Document all CLI options
- **Examples**: Include usage examples
Installation
------------

sphinx-click is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinx_click; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``docs/conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_click',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinx_click']
   
   # Configuration options
   # sphinx-click uses directives, minimal configuration needed


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_click',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

Complete configuration with all features:

.. code-block:: python

   extensions = ['sphinx_click']
   
   # sphinx-click is configured through directives
   # No global configuration needed

Basic Usage
-----------

Getting Started
~~~~~~~~~~~~~~~

Document a Click CLI:

.. code-block:: rst

   .. click:: mypackage.cli:main
      :prog: myapp
      :nested: full

Document Commands
~~~~~~~~~~~~~~~~~

Document specific commands:

.. code-block:: rst

   .. click:: mypackage.cli:deploy
      :prog: myapp deploy
      :show-nested:

Common Use Cases
----------------

Full CLI Documentation
~~~~~~~~~~~~~~~~~~~~~~

Document complete CLI application:

.. code-block:: rst

   .. click:: myapp.cli:cli
      :prog: myapp
      :nested: full
      :commands: deploy, config, status

Command Groups
~~~~~~~~~~~~~~

Document command groups:

.. code-block:: rst

   .. click:: myapp.commands:database
      :prog: myapp db
      :nested: short

Advanced Features
-----------------

Custom Options
~~~~~~~~~~~~~~

Control output detail:

.. code-block:: rst

   .. click:: myapp.cli:main
      :prog: myapp
      :show-nested:
      :nested: full

Nested Commands
~~~~~~~~~~~~~~~

Show nested command structure:

.. code-block:: rst

   .. click:: myapp.cli:cli
      :prog: myapp
      :nested: full
      :commands: db, user, config

Best Practices
--------------

Tips and Guidelines
~~~~~~~~~~~~~~~~~~~

- Document all CLI commands
- Use clear command descriptions
- Include examples
- Document all options and arguments
- Keep CLI help up-to-date

Troubleshooting
---------------

Common Issues
~~~~~~~~~~~~~

**Issue**: CLI not found

**Solution**: Ensure the module path is correct and Click is installed.

**Issue**: Commands not showing

**Solution**: Check nested and commands options.

Additional Resources
--------------------

- :doc:`Working Example <../../examples/sphinx-click-example>`
- `PyPI Package <https://pypi.org/project/sphinx-click/>`_
- `Official Documentation <https://sphinx-click.readthedocs.io/>`_
