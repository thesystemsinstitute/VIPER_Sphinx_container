Sphinx-Autodoc-TOML Tutorial
============================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-autodoc-toml/>`_
   - `API Documentation <../../pdoc/sphinx_autodoc_toml/index.html>`_
   - `Manual <https://github.com/calvingiles/autodoc-toml>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinx-autodoc-toml to generate documentation from TOML configuration files.

What is Sphinx-Autodoc-TOML?
-----------------------------
sphinx-autodoc-toml is a Sphinx extension that enables:

- Document TOML configuration files
- Auto-generate config documentation
- Show configuration schemas
- Display default values
- Document pyproject.toml
- Tool configuration documentation
- Environment variable mapping
- Validation rules display
- Configuration examples
- Settings reference generation

This is perfect for documenting application configuration, pyproject.toml files, and TOML-based settings.

The sphinx-autodoc-toml extension automatically extracts documentation from pyproject.toml configuration files.


Installation
------------

sphinx-autodoc-toml is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm viper-sphinx:latest python -c "import sphinx_autodoc_toml; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_autodoc_toml',
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinx_autodoc_toml']
   
   # TOML autodoc configuration
   autodoc_toml_default_file = 'pyproject.toml'
   autodoc_toml_show_types = True
   autodoc_toml_show_defaults = True
   
   # Display options
   autodoc_toml_table_style = 'grid'  # grid, simple, plain
   autodoc_toml_show_examples = True
   autodoc_toml_syntax_highlight = True
   
   # Processing options
   autodoc_toml_preserve_comments = True
   autodoc_toml_expand_env_vars = False
   autodoc_toml_validate_schema = True


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Basic Setup
~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_autodoc_toml',
   ]
   
   toml_autodoc_file = 'pyproject.toml'

Options
~~~~~~~

.. code-block:: python

   toml_autodoc_sections = ['project', 'build-system', 'tool.pytest']

Basic Usage
-----------

Document pyproject.toml
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. autotoml:: pyproject.toml
      :section: tool.poetry

Document Configuration File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. autotoml:: config.toml
      :show-types:
      :show-defaults:

Show Specific Section
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. autotoml:: settings.toml
      :section: database

   Project Configuration
   =====================
   
   This project uses ``pyproject.toml`` for configuration.
   
   Poetry Configuration
   --------------------
   
   Project metadata and dependencies:
   
   .. autotoml:: ../../pyproject.toml
      :section: tool.poetry
      :show-defaults:
   
   Black Configuration
   -------------------
   
   Code formatting settings:
   
   .. autotoml:: ../../pyproject.toml
      :section: tool.black
   
   Example ``pyproject.toml``:
   
   .. code-block:: toml
      
      [tool.black]
      line-length = 88
      target-version = ['py311']
      include = '\.pyi?$'
   
   MyPy Configuration
   ------------------
   
   Type checking settings:
   
   .. autotoml:: ../../pyproject.toml
      :section: tool.mypy

Example 2: Application Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``config/settings.toml``:

.. code-block:: toml

   # Application Settings
   
   [app]
   name = "MyApp"
   version = "1.0.0"
   debug = false
   secret_key = "${SECRET_KEY}"  # Environment variable
   
   [app.features]
   enable_api = true
   enable_admin = true
   enable_cache = true
   max_upload_size = 10485760  # 10MB in bytes
   
   [database]
   # Database connection settings
   host = "localhost"
   port = 5432
   database = "myapp"
   username = "postgres"
   password = "${DB_PASSWORD}"
   pool_size = 10
   max_overflow = 20
   echo = false
   
   [database.options]
   # Additional database options
   connect_timeout = 30
   command_timeout = 60
   ssl_mode = "prefer"
   
   [cache]
   # Cache configuration
   backend = "redis"
   host = "localhost"
   port = 6379
   db = 0
   password = "${REDIS_PASSWORD}"
   default_timeout = 300
   
   [logging]
   # Logging configuration
   level = "INFO"
   format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
   file = "logs/app.log"
   max_bytes = 10485760
   backup_count = 5
   
   [security]
   # Security settings
   allowed_hosts = ["example.com", "www.example.com"]
   cors_origins = ["https://example.com"]
   session_timeout = 3600
   csrf_enabled = true

``docs/configuration/settings.rst``:

.. code-block:: rst

   Application Settings
   ====================
   
   Settings are configured using TOML files.
   
   Application Settings
   --------------------
   
   .. autotoml:: ../../config/settings.toml
      :section: app
      :show-defaults:
      :show-types:
   
   Database Configuration
   ----------------------
   
   .. autotoml:: ../../config/settings.toml
      :section: database
   
   Connection String Format:
   
   .. code-block:: text
      
      postgresql://username:password@host:port/database
   
   Environment Variables:
   
   - ``DB_PASSWORD``: Database password
   
   Cache Configuration
   -------------------
   
   .. autotoml:: ../../config/settings.toml
      :section: cache
   
   Supported backends:
   
   - ``redis``: Redis cache
   - ``memcached``: Memcached
   - ``memory``: In-memory cache
   
   Logging Configuration
   ---------------------
   
   .. autotoml:: ../../config/settings.toml
      :section: logging
   
   Log levels:
   
   - ``DEBUG``: Detailed debugging information
   - ``INFO``: General information messages
   - ``WARNING``: Warning messages
   - ``ERROR``: Error messages
   - ``CRITICAL``: Critical errors

Example 3: Tool Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``tools.toml``:

.. code-block:: toml

   [tool.pytest]
   minversion = "7.0"
   addopts = "-ra -q --strict-markers --cov=myproject"
   testpaths = ["tests"]
   python_files = "test_*.py"
   python_classes = "Test*"
   python_functions = "test_*"
   
   [tool.coverage]
   [tool.coverage.run]
   source = ["myproject"]
   omit = ["*/tests/*", "*/migrations/*"]
   
   [tool.coverage.report]
   exclude_lines = [
       "pragma: no cover",
       "def __repr__",
       "raise AssertionError",
       "raise NotImplementedError",
   ]
   
   [tool.isort]
   profile = "black"
   line_length = 88
   multi_line_output = 3
   include_trailing_comma = true
   
   [tool.pylint]
   max-line-length = 88
   disable = [
       "C0111",  # missing-docstring
       "R0903",  # too-few-public-methods
   ]

``docs/development/tools.rst``:

.. code-block:: rst

   Development Tools Configuration
   ===============================
   
   Testing Configuration
   ---------------------
   
   .. autotoml:: ../../tools.toml
      :section: tool.pytest
   
   Running tests:
   
   .. code-block:: bash
      
      pytest
   
   Coverage Configuration
   ----------------------
   
   .. autotoml:: ../../tools.toml
      :section: tool.coverage
   
   Generate coverage report:
   
   .. code-block:: bash
      
      pytest --cov=myproject --cov-report=html
   
   Import Sorting
   --------------
   
   .. autotoml:: ../../tools.toml
      :section: tool.isort
   
   Sort imports:
   
   .. code-block:: bash
      
      isort myproject/

Advanced Features
-----------------

Schema Validation
~~~~~~~~~~~~~~~~~

Define TOML schema:

.. code-block:: python

   # docs/conf.py
   autodoc_toml_schema = {
       'database': {
           'host': {'type': 'string', 'required': True},
           'port': {'type': 'integer', 'default': 5432},
           'database': {'type': 'string', 'required': True},
       }
   }

Custom Formatting
~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. autotoml:: config.toml
      :format: table
      :show-comments:
      :show-types:

Multiple Sections
~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. autotoml:: settings.toml
      :sections: app, database, cache

Inline TOML
~~~~~~~~~~~

.. code-block:: rst

   .. toml-doc::
      
      [server]
      host = "0.0.0.0"
      port = 8000

Docker Integration
------------------

Build Documentation
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     viper-sphinx:latest \
     sphinx-build -b html /project/docs /project/docs/_build/html

Validate TOML
~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     viper-sphinx:latest \
     python -c "import tomli; tomli.load(open('config.toml', 'rb'))"

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Build Configuration Docs
   
   on:
     push:
       paths:
         - '**/*.toml'
         - 'docs/**'
   
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Validate TOML Files
           run: |
             docker run --rm -v $(pwd):/project \
               viper-sphinx:latest \
               sh -c "for f in /project/**/*.toml; do \
                        python -c 'import tomli; tomli.load(open(\"$f\", \"rb\"))' \
                      done"
         
         - name: Build Documentation
           run: |
             docker run --rm -v $(pwd):/project \
               viper-sphinx:latest \
               sphinx-build -b html /project/docs /project/docs/_build/html

Best Practices
--------------

1. **Comment Your TOML**
   
   Add explanatory comments:
   
   .. code-block:: toml
   
      # Database connection settings
      [database]
      host = "localhost"  # Database server

2. **Use Sections**
   
   Organize settings logically

3. **Document Environment Variables**
   
   List required env vars

4. **Provide Examples**
   
   Show example configurations

5. **Validate Files**
   
   Check TOML syntax

6. **Version Configuration**
   
   Track config changes

Troubleshooting
---------------

TOML Parse Error
~~~~~~~~~~~~~~~~

**Solution:**

Validate TOML syntax:

.. code-block:: bash

   python -c "import tomli; tomli.load(open('config.toml', 'rb'))"

File Not Found
~~~~~~~~~~~~~~

**Solution:**

Check path relative to conf.py:

.. code-block:: rst

   .. autotoml:: ../../config.toml

Section Not Found
~~~~~~~~~~~~~~~~~

**Solution:**

Verify section name:

.. code-block:: rst

   .. autotoml:: config.toml
      :section: tool.myapp

Next Steps
----------

1. Create TOML configuration files
2. Add autotoml directives
3. Document all settings
4. Provide usage examples
5. Validate TOML syntax


Practical Examples
------------------

Basic Usage
-----------

Project Metadata
~~~~~~~~~~~~~~~~

.. toml-autodoc:: pyproject.toml
   :section: project

This documents the [project] section including name, version, description, and dependencies.

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_autodoc_toml',
   ]
   
   toml_autodoc_file = 'pyproject.toml'

Options
~~~~~~~

.. code-block:: python

   toml_autodoc_sections = ['project', 'build-system', 'tool.pytest']

Examples
--------

Dependencies
~~~~~~~~~~~~

.. toml-autodoc:: pyproject.toml
   :section: project.dependencies

Build System
~~~~~~~~~~~~

.. toml-autodoc:: pyproject.toml
   :section: build-system


Practical Examples
------------------

Basic Usage
-----------

Project Metadata
~~~~~~~~~~~~~~~~

.. toml-autodoc:: pyproject.toml
   :section: project

This documents the [project] section including name, version, description, and dependencies.

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_autodoc_toml',
   ]
   
   toml_autodoc_file = 'pyproject.toml'

Options
~~~~~~~

.. code-block:: python

   toml_autodoc_sections = ['project', 'build-system', 'tool.pytest']

Examples
--------

Dependencies
~~~~~~~~~~~~

.. toml-autodoc:: pyproject.toml
   :section: project.dependencies

Build System
~~~~~~~~~~~~

.. toml-autodoc:: pyproject.toml
   :section: build-system


Practical Examples
------------------

Basic Usage
-----------

Project Metadata
~~~~~~~~~~~~~~~~

.. toml-autodoc:: pyproject.toml
   :section: project

This documents the [project] section including name, version, description, and dependencies.

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_autodoc_toml',
   ]
   
   toml_autodoc_file = 'pyproject.toml'

Options
~~~~~~~

.. code-block:: python

   toml_autodoc_sections = ['project', 'build-system', 'tool.pytest']

Examples
--------

Dependencies
~~~~~~~~~~~~

.. toml-autodoc:: pyproject.toml
   :section: project.dependencies

Build System
~~~~~~~~~~~~

.. toml-autodoc:: pyproject.toml
   :section: build-system

Additional Resources
--------------------
- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `TOML Specification <https://toml.io/>`_
- `Poetry Documentation <https://python-poetry.org/>`_
- :doc:`../tutorials/packages/sphinx-autodoc-toml` - Complete tutorial
- pyproject.toml: https://peps.python.org/pep-0621/
- GitHub repository: https://github.com/sphinx-contrib/autodoc-toml

