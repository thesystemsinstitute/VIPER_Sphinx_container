Sphinx Click Tutorial
=====================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-click/>`_
   - `API Documentation <../../pdoc/sphinx_click/index.html>`_
   - `Manual <https://sphinx-click.readthedocs.io/>`_

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


Practical Examples
------------------

Overview
--------


Key Features
~~~~~~~~~~~~

- **Automatic Documentation**: Generate docs from Click decorators
- **Nested Commands**: Support for command groups
- **Options & Arguments**: Document all CLI options
- **Examples**: Include usage examples

Installation
------------

Using pip
~~~~~~~~~

Install the extension:

.. code-block:: bash

   pip install sphinx-click

Or add to your ``requirements.txt``:

.. code-block:: text

   sphinx-click
   sphinx>=5.0.0
   click>=7.0

Configuration
-------------

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

Example 1: Simple CLI
~~~~~~~~~~~~~~~~~~~~~

Document a simple Click CLI:

First, create a Click application:

.. code-block:: python

   # myapp/cli.py
   import click
   
   @click.command()
   @click.option('--count', default=1, help='Number of greetings.')
   @click.option('--name', prompt='Your name', help='The person to greet.')
   def hello(count, name):
       """Simple program that greets NAME for a total of COUNT times."""
       for _ in range(count):
           click.echo(f'Hello {name}!')
   
   if __name__ == '__main__':
       hello()

Then document it:

.. code-block:: rst

   CLI Reference
   =============
   
   .. click:: myapp.cli:hello
      :prog: myapp

Example 2: Command Groups
~~~~~~~~~~~~~~~~~~~~~~~~~~

Document command groups:

.. code-block:: python

   # myapp/cli.py
   import click
   
   @click.group()
   def cli():
       """My application CLI."""
       pass
   
   @cli.command()
   def init():
       """Initialize the application."""
       click.echo('Initialized!')
   
   @cli.command()
   @click.option('--verbose', is_flag=True, help='Verbose output')
   def deploy(verbose):
       """Deploy the application."""
       click.echo('Deploying...')

Document it:

.. code-block:: rst

   .. click:: myapp.cli:cli
      :prog: myapp
      :nested: full

Real-World Examples
-------------------

Example: Complete CLI Application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Full CLI application documentation:

.. code-block:: python

   # myapp/cli.py
   import click
   
   @click.group()
   @click.version_option(version='1.0.0')
   def cli():
       """MyApp - A comprehensive CLI tool."""
       pass
   
   @cli.group()
   def db():
       """Database management commands."""
       pass
   
   @db.command()
   @click.option('--drop', is_flag=True, help='Drop existing tables')
   def init(drop):
       """Initialize the database."""
       if drop:
           click.echo('Dropping tables...')
       click.echo('Initializing database...')
   
   @db.command()
   def migrate():
       """Run database migrations."""
       click.echo('Running migrations...')
   
   @cli.command()
   @click.argument('environment', type=click.Choice(['dev', 'staging', 'prod']))
   @click.option('--dry-run', is_flag=True, help='Perform a dry run')
   def deploy(environment, dry_run):
       """Deploy to specified environment."""
       mode = "DRY RUN" if dry_run else "LIVE"
       click.echo(f'Deploying to {environment} ({mode})...')
   
   @cli.command()
   @click.option('--format', type=click.Choice(['json', 'yaml']), default='json')
   @click.option('--output', type=click.File('w'), help='Output file')
   def config(format, output):
       """Show or export configuration."""
       click.echo(f'Configuration in {format} format')

Document it:

.. code-block:: rst

   MyApp CLI Documentation
   =======================
   
   Overview
   --------
   
   MyApp provides a comprehensive command-line interface for managing
   your application.
   
   Installation
   ------------
   
   .. code-block:: bash
   
      pip install myapp
   
   Quick Start
   -----------
   
   .. code-block:: bash
   
      # Initialize database
      myapp db init
      
      # Deploy to staging
      myapp deploy staging
      
      # Export configuration
      myapp config --format yaml --output config.yml
   
   Command Reference
   -----------------
   
   .. click:: myapp.cli:cli
      :prog: myapp
      :nested: full

Example: Selective Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Document specific commands:

.. code-block:: rst

   Database Commands
   =================
   
   .. click:: myapp.cli:db
      :prog: myapp db
      :nested: full
   
   Deployment Command
   ==================
   
   .. click:: myapp.cli:deploy
      :prog: myapp deploy
      :show-nested:

Example: With Usage Examples
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add usage examples to documentation:

.. code-block:: rst

   MyApp CLI Guide
   ===============
   
   Command Reference
   -----------------
   
   .. click:: myapp.cli:cli
      :prog: myapp
      :nested: full
   
   Usage Examples
   --------------
   
   Initialize Database
   ~~~~~~~~~~~~~~~~~~~
   
   .. code-block:: bash
   
      # Basic initialization
      myapp db init
      
      # Drop and reinitialize
      myapp db init --drop
   
   Deploy Application
   ~~~~~~~~~~~~~~~~~~
   
   .. code-block:: bash
   
      # Deploy to development
      myapp deploy dev
      
      # Dry run for production
      myapp deploy prod --dry-run
   
   Export Configuration
   ~~~~~~~~~~~~~~~~~~~~
   
   .. code-block:: bash
   
      # Display as JSON
      myapp config
      
      # Export to YAML file
      myapp config --format yaml --output settings.yml

Best Practices
--------------

Recommendations
~~~~~~~~~~~~~~~

- Add comprehensive docstrings to commands
- Document all options and arguments
- Use Click's help parameter effectively
- Include usage examples
- Keep CLI documentation synchronized with code

Common Patterns
~~~~~~~~~~~~~~~

Standard patterns for using sphinx-click:

1. **Full CLI Docs**: Document entire CLI with nested: full
2. **Command Groups**: Separate docs for command groups
3. **Examples**: Combine auto-docs with manual examples

Integration Tips
----------------

Working with Other Extensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

sphinx-click integrates well with:

- sphinx-argparse for argparse CLIs
- sphinx-typer for Typer CLIs
- sphinx.ext.autodoc for API documentation

Additional Resources
--------------------

- `PyPI Package <https://pypi.org/project/sphinx-click/>`_
- `Official Documentation <https://sphinx-click.readthedocs.io/>`_
- :doc:`Complete Tutorial <../tutorials/packages/sphinx-click>`
- `Click Documentation <https://click.palletsprojects.com/>`_
- :ref:`Package API Documentation <pdoc-sphinx-click>`
Next Steps
----------
- Explore the :doc:`tutorial <../tutorials/packages/sphinx-click>`
- Check the official documentation
- Try the examples in your own projects
- Customize for your specific needs

