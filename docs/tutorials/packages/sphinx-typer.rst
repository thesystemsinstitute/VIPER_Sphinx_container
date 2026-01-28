Sphinx Typer Tutorial
=====================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinxcontrib-typer/>`_

   - `Official Documentation <https://sphinxcontrib-typer.readthedocs.io/>`_

This tutorial demonstrates how to use sphinx-typer in your Sphinx documentation.

What is Sphinx Typer?
---------------------
sphinx-typer is a Sphinx extension that provides:

- Document Typer CLIs
- Easy integration with Sphinx
- Comprehensive configuration options
- Professional documentation output

sphinx-typer provides:

- Document Typer CLIs
- Integration with Sphinx documentation
- Flexible configuration options
- Professional output formatting

Key Features
~~~~~~~~~~~~

- **Type Hints**: Automatic documentation from type hints
- **Rich Output**: Support for rich console formatting
- **Nested Commands**: Command group documentation
- **Validation**: Document Typer's validation features


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


Complete configuration with all features:

.. code-block:: python

   extensions = ['sphinxcontrib.typer']
   
   # sphinxcontrib-typer is configured through directives

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


Practical Examples
------------------

Overview
--------


Key Features
~~~~~~~~~~~~

- **Type Hints**: Automatic documentation from type hints
- **Rich Output**: Support for rich console formatting
- **Nested Commands**: Command group documentation
- **Validation**: Document Typer's validation features

Installation
------------

Using pip
~~~~~~~~~

Install the extension:

.. code-block:: bash

   pip install sphinxcontrib-typer

Or add to your ``requirements.txt``:

.. code-block:: text

   sphinxcontrib-typer
   sphinx>=5.0.0
   typer>=0.6.0

Configuration
-------------

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinxcontrib.typer',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

Complete configuration with all features:

.. code-block:: python

   extensions = ['sphinxcontrib.typer']
   
   # sphinxcontrib-typer is configured through directives

Basic Usage
-----------

Example 1: Simple Typer CLI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a Typer application:

.. code-block:: python

   # myapp/cli.py
   import typer
   from typing import Optional
   
   app = typer.Typer()
   
   @app.command()
   def hello(
       name: str = typer.Argument(..., help="The name to greet"),
       count: int = typer.Option(1, help="Number of greetings"),
       polite: bool = typer.Option(False, "--polite", help="Add 'please'")
   ):
       """Greet someone with their name."""
       for _ in range(count):
           greeting = "Hello"
           if polite:
               greeting += " please"
           typer.echo(f"{greeting} {name}!")
   
   if __name__ == "__main__":
       app()

Document it:

.. code-block:: rst

   CLI Reference
   =============
   
   .. typer:: myapp.cli:app
      :prog: myapp
      :show-nested:

Example 2: Command Groups
~~~~~~~~~~~~~~~~~~~~~~~~~~

Typer application with subcommands:

.. code-block:: python

   # myapp/cli.py
   import typer
   from typing import Optional
   from pathlib import Path
   
   app = typer.Typer()
   db_app = typer.Typer()
   app.add_typer(db_app, name="db")
   
   @db_app.command()
   def init(
       drop: bool = typer.Option(False, help="Drop existing tables")
   ):
       """Initialize the database."""
       if drop:
           typer.echo("Dropping tables...")
       typer.echo("Initializing database...")
   
   @db_app.command()
   def migrate():
       """Run database migrations."""
       typer.echo("Running migrations...")
   
   @app.command()
   def deploy(
       environment: str = typer.Argument(..., help="Target environment"),
       dry_run: bool = typer.Option(False, help="Perform a dry run")
   ):
       """Deploy to specified environment."""
       mode = "DRY RUN" if dry_run else "LIVE"
       typer.echo(f"Deploying to {environment} ({mode})...")

Document it:

.. code-block:: rst

   .. typer:: myapp.cli:app
      :prog: myapp
      :show-nested:
      :make-sections:

Real-World Examples
-------------------

Example: Complete CLI Application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Full-featured Typer CLI:

.. code-block:: python

   # myapp/cli.py
   import typer
   from typing import Optional, List
   from pathlib import Path
   from enum import Enum
   
   app = typer.Typer(help="MyApp - A comprehensive CLI tool")
   
   class Environment(str, Enum):
       dev = "dev"
       staging = "staging"
       prod = "prod"
   
   class OutputFormat(str, Enum):
       json = "json"
       yaml = "yaml"
       toml = "toml"
   
   # Database commands
   db_app = typer.Typer(help="Database management commands")
   app.add_typer(db_app, name="db")
   
   @db_app.command()
   def init(
       drop: bool = typer.Option(False, "--drop", help="Drop existing tables"),
       seed: bool = typer.Option(False, "--seed", help="Seed with sample data"),
       verbose: bool = typer.Option(False, "--verbose", "-v", help="Verbose output")
   ):
       """
       Initialize the database.
       
       This command sets up the database schema and optionally
       seeds it with sample data.
       """
       if verbose:
           typer.echo("Verbose mode enabled")
       if drop:
           typer.echo("Dropping existing tables...")
       typer.echo("Creating tables...")
       if seed:
           typer.echo("Seeding database with sample data...")
       typer.secho("Database initialized successfully!", fg=typer.colors.GREEN)
   
   @db_app.command()
   def backup(
       output: Path = typer.Option(
           Path("backup.sql"),
           help="Output file for backup"
       ),
       compress: bool = typer.Option(False, help="Compress backup file")
   ):
       """Create a database backup."""
       typer.echo(f"Creating backup to {output}")
       if compress:
           typer.echo("Compressing backup...")
       typer.secho("Backup completed!", fg=typer.colors.GREEN)
   
   # Deployment commands
   @app.command()
   def deploy(
       environment: Environment = typer.Argument(..., help="Target environment"),
       version: Optional[str] = typer.Option(None, help="Version to deploy"),
       dry_run: bool = typer.Option(False, "--dry-run", help="Perform a dry run"),
       skip_tests: bool = typer.Option(False, "--skip-tests", help="Skip tests"),
   ):
       """
       Deploy application to specified environment.
       
       Deploys the application with optional version specification.
       Includes pre-deployment checks and validation.
       """
       mode = "DRY RUN" if dry_run else "LIVE"
       typer.echo(f"Deploying to {environment.value} ({mode})")
       
       if not skip_tests:
           typer.echo("Running tests...")
       
       if version:
           typer.echo(f"Deploying version: {version}")
       
       typer.secho(f"Deployment to {environment.value} completed!", fg=typer.colors.GREEN)
   
   # Configuration commands
   @app.command()
   def config(
       format: OutputFormat = typer.Option(OutputFormat.json, help="Output format"),
       output: Optional[Path] = typer.Option(None, help="Output file"),
       show_secrets: bool = typer.Option(False, help="Include secret values")
   ):
       """
       Display or export configuration.
       
       Shows current configuration in specified format.
       Can export to file for sharing or backup.
       """
       typer.echo(f"Configuration in {format.value} format")
       if show_secrets:
           typer.echo("⚠️  Including secret values!")
       if output:
           typer.echo(f"Exporting to {output}")
   
   @app.command()
   def version():
       """Show application version."""
       typer.echo("MyApp version 1.0.0")

Documentation:

.. code-block:: rst

   MyApp CLI Documentation
   =======================
   
   Overview
   --------
   
   MyApp provides a powerful command-line interface built with Typer,
   featuring type-safe commands and rich console output.
   
   Installation
   ------------
   
   .. code-block:: bash
   
      pip install myapp
   
   Features
   --------
   
   - Type-safe command arguments
   - Rich console output
   - Interactive prompts
   - Auto-completion support
   - Comprehensive validation
   
   Quick Start
   -----------
   
   .. code-block:: bash
   
      # Initialize database
      myapp db init --seed
      
      # Deploy to staging
      myapp deploy staging --version 1.0.0
      
      # Export configuration
      myapp config --format yaml --output config.yml
   
   Command Reference
   -----------------
   
   .. typer:: myapp.cli:app
      :prog: myapp
      :show-nested:
      :make-sections:

Example: With Usage Examples
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Combine auto-generated docs with examples:

.. code-block:: rst

   MyApp User Guide
   ================
   
   Command Reference
   -----------------
   
   .. typer:: myapp.cli:app
      :prog: myapp
      :show-nested:
   
   Common Tasks
   ------------
   
   Database Management
   ~~~~~~~~~~~~~~~~~~~
   
   .. code-block:: bash
   
      # Initialize fresh database
      myapp db init --drop --seed
      
      # Create backup
      myapp db backup --output backup.sql --compress
   
   Deployment
   ~~~~~~~~~~
   
   .. code-block:: bash
   
      # Test deployment
      myapp deploy staging --dry-run
      
      # Production deployment
      myapp deploy prod --version 2.0.0
   
   Configuration
   ~~~~~~~~~~~~~
   
   .. code-block:: bash
   
      # View configuration
      myapp config
      
      # Export as YAML
      myapp config --format yaml --output settings.yml

Best Practices
--------------

Recommendations
~~~~~~~~~~~~~~~

- Use type hints for all parameters
- Add comprehensive docstrings
- Use Enum for choice parameters
- Leverage Typer's rich output
- Include validation in type hints

Common Patterns
~~~~~~~~~~~~~~~

Standard patterns for using sphinx-typer:

1. **Full CLI Documentation**: Auto-generate complete CLI docs
2. **Type-safe Commands**: Use Enums and type hints
3. **Rich Examples**: Combine auto-docs with usage examples

Integration Tips
----------------

Working with Other Extensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

sphinx-typer integrates well with:

- sphinx-click for Click CLIs
- sphinx.ext.autodoc for API documentation
- Standard Sphinx extensions

Additional Resources
--------------------

- `PyPI Package <https://pypi.org/project/sphinxcontrib-typer/>`_
- `Official Documentation <https://sphinxcontrib-typer.readthedocs.io/>`_
- :doc:`Complete Tutorial <../tutorials/packages/sphinx-typer>`
- `Typer Documentation <https://typer.tiangolo.com/>`_
- :ref:`Package API Documentation <pdoc-sphinx-typer>`
Next Steps
----------
- Explore the :doc:`tutorial <../tutorials/packages/sphinx-typer>`
- Check the official documentation
- Try the examples in your own projects
- Customize for your specific needs

