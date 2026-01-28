Sphinx Toolbox Tutorial
=======================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-toolbox/>`_
   - `API Documentation <../../pdoc/sphinx_toolbox/index.html>`_
   - `Manual <https://sphinx-toolbox.readthedocs.io/>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinx-toolbox in your Sphinx documentation.

What is Sphinx Toolbox?
-----------------------
sphinx-toolbox is a Sphinx extension that provides:

- Collection of Sphinx extensions
- Easy integration with Sphinx
- Comprehensive configuration options
- Professional documentation output

sphinx-toolbox provides:

- Collection of Sphinx extensions
- Integration with Sphinx documentation
- Flexible configuration options
- Professional output formatting

Key Features
~~~~~~~~~~~~

- **Configuration Documentation**: Document config values
- **Enhanced Autodoc**: More autodoc features
- **Code Enhancements**: Better code blocks
- **GitHub Integration**: GitHub-related features


Installation
------------

sphinx-toolbox is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinx_toolbox; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``docs/conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_toolbox',
       'sphinx_toolbox.more_autodoc',
       'sphinx_toolbox.code',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = [
       'sphinx_toolbox',
       'sphinx_toolbox.more_autodoc',
       'sphinx_toolbox.more_autosummary',
       'sphinx_toolbox.documentation_summary',
       'sphinx_toolbox.tweaks.param_dash',
       'sphinx_toolbox.confval',
       'sphinx_toolbox.code',
   ]
   
   # Configuration options
   github_username = 'your-username'
   github_repository = 'your-repo'


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_toolbox',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

Complete configuration with all features:

.. code-block:: python

   extensions = [
       'sphinx_toolbox',
       'sphinx_toolbox.more_autodoc',
       'sphinx_toolbox.more_autosummary',
       'sphinx_toolbox.documentation_summary',
       'sphinx_toolbox.tweaks.param_dash',
       'sphinx_toolbox.tweaks.latex_layout',
       'sphinx_toolbox.tweaks.latex_toc',
       'sphinx_toolbox.github',
       'sphinx_toolbox.sidebar_links',
       'sphinx_toolbox.confval',
       'sphinx_toolbox.code',
   ]
   
   # GitHub integration
   github_username = 'your-username'
   github_repository = 'your-repo'
   
   # Other options
   documentation_summary = 'My Project Documentation'

Basic Usage
-----------

Getting Started
~~~~~~~~~~~~~~~

Use various toolbox directives:

.. code-block:: rst

   .. confval:: setting_name
      :type: str
      :default: "default value"
      
      Description of the setting.

Enhanced Autodoc
~~~~~~~~~~~~~~~~

Use enhanced autodoc features:

.. code-block:: rst

   .. autoclasssumm:: mymodule.MyClass
      :autosummary-sections: Methods

Common Use Cases
----------------

Configuration Values
~~~~~~~~~~~~~~~~~~~~

Document configuration values:

.. code-block:: rst

   .. confval:: max_connections
      :type: int
      :default: 100
      :required: False
      
      Maximum number of database connections.

Code Blocks
~~~~~~~~~~~

Enhanced code blocks:

.. code-block:: rst

   .. code-block:: python
      :linenos:
      :emphasize-lines: 2,3
      
      def example():
          # This is highlighted
          return "Hello"

Advanced Features
-----------------

Documentation Summary
~~~~~~~~~~~~~~~~~~~~~

Add documentation summary:

.. code-block:: rst

   .. documentation-summary::
      :meta:

More Autodoc
~~~~~~~~~~~~

Enhanced autodoc features:

.. code-block:: rst

   .. autoclasssumm:: mymodule.MyClass
      :autosummary-members:

Best Practices
--------------

Tips and Guidelines
~~~~~~~~~~~~~~~~~~~

- Use appropriate toolbox extensions
- Document configuration values
- Enhance autodoc output
- Use code highlighting features
- Keep extensions updated

Troubleshooting
---------------

Common Issues
~~~~~~~~~~~~~

**Issue**: Directive not found

**Solution**: Ensure the specific toolbox extension is enabled.

**Issue**: Formatting issues

**Solution**: Check directive syntax and options.


Practical Examples
------------------

Overview
--------


Key Features
~~~~~~~~~~~~

- **Configuration Documentation**: Document config values
- **Enhanced Autodoc**: More autodoc features
- **Code Enhancements**: Better code blocks
- **GitHub Integration**: GitHub-related features

Installation
------------

Using pip
~~~~~~~~~

Install the extension:

.. code-block:: bash

   pip install sphinx-toolbox

Or add to your ``requirements.txt``:

.. code-block:: text

   sphinx-toolbox
   sphinx>=4.0.0

Configuration
-------------

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_toolbox',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

Complete configuration with all features:

.. code-block:: python

   extensions = [
       'sphinx_toolbox',
       'sphinx_toolbox.more_autodoc',
       'sphinx_toolbox.more_autosummary',
       'sphinx_toolbox.documentation_summary',
       'sphinx_toolbox.tweaks.param_dash',
       'sphinx_toolbox.tweaks.latex_layout',
       'sphinx_toolbox.tweaks.latex_toc',
       'sphinx_toolbox.github',
       'sphinx_toolbox.sidebar_links',
       'sphinx_toolbox.confval',
       'sphinx_toolbox.code',
   ]
   
   # GitHub integration
   github_username = 'your-username'
   github_repository = 'your-repo'
   
   # Other options
   documentation_summary = 'My Project Documentation'

Basic Usage
-----------

Example 1: Configuration Values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Document configuration settings:

.. code-block:: rst

   Configuration Reference
   =======================
   
   .. confval:: database_url
      :type: str
      :required: True
      
      Database connection URL.
      
      Example:
      
      .. code-block:: python
      
         database_url = "postgresql://localhost/mydb"
   
   .. confval:: debug
      :type: bool
      :default: False
      
      Enable debug mode for development.
   
   .. confval:: max_workers
      :type: int
      :default: 4
      :required: False
      
      Maximum number of worker processes.

Example 2: Enhanced Autodoc
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use enhanced autodoc features:

.. code-block:: rst

   API Reference
   =============
   
   .. autoclasssumm:: myapp.core.Engine
      :autosummary-members:
      :autosummary-sections: Methods, Properties
   
   .. automodulesumm:: myapp.utils
      :autosummary-members:

Real-World Examples
-------------------

Example: Complete Configuration Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Document all configuration options:

.. code-block:: rst

   Configuration Guide
   ===================
   
   Database Settings
   -----------------
   
   .. confval:: db_host
      :type: str
      :default: "localhost"
      
      Database server hostname.
   
   .. confval:: db_port
      :type: int
      :default: 5432
      
      Database server port.
   
   .. confval:: db_name
      :type: str
      :required: True
      
      Database name to connect to.
   
   .. confval:: db_pool_size
      :type: int
      :default: 10
      
      Connection pool size.
      
      .. note::
         Adjust based on your application's concurrency needs.
   
   Application Settings
   --------------------
   
   .. confval:: app_name
      :type: str
      :required: True
      
      Application name displayed in UI.
   
   .. confval:: secret_key
      :type: str
      :required: True
      
      Secret key for cryptographic operations.
      
      .. warning::
         Never commit this to version control!
   
   .. confval:: allowed_hosts
      :type: List[str]
      :default: []
      
      List of allowed host/domain names.

Example: API Documentation with Summaries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Enhanced API documentation:

.. code-block:: rst

   API Documentation
   =================
   
   Core Classes
   ------------
   
   .. autoclasssumm:: myapp.core.Application
      :autosummary-members:
      :autosummary-sections: Methods, Properties, Class Methods
   
   Detailed Documentation
   ----------------------
   
   .. autoclass:: myapp.core.Application
      :members:
      :inherited-members:
      :show-inheritance:
   
   Utility Functions
   -----------------
   
   .. automodulesumm:: myapp.utils
      :autosummary-members:
      :autosummary-exclude-members: _private_function

Example: Code Examples with Enhancements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Enhanced code blocks:

.. code-block:: rst

   Usage Examples
   ==============
   
   Basic Usage
   -----------
   
   .. code-block:: python
      :linenos:
      :emphasize-lines: 3,4
      :caption: Basic application setup
      
      from myapp import Application
      
      app = Application(config='production')
      app.run()
   
   Advanced Configuration
   ----------------------
   
   .. code-block:: python
      :linenos:
      :emphasize-lines: 5-8
      :caption: Custom configuration
      
      from myapp import Application, Config
      
      config = Config(
          db_host='localhost',
          db_port=5432,
          debug=True,
          log_level='DEBUG'
      )
      
      app = Application(config=config)
      app.run()

Example: GitHub Integration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add GitHub links and badges:

.. code-block:: rst

   Project Information
   ===================
   
   .. documentation-summary::
      :meta:
   
   .. sidebar-links::
      :github:
      :pypi: mypackage
   
   Links
   -----
   
   - :github:repo:`Source Code <>`
   - :github:issue:`Report Issues <>`
   - :github:pull:`Pull Requests <>`

Example: Complete Project Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Full project documentation using toolbox:

.. code-block:: rst

   MyProject Documentation
   =======================
   
   .. documentation-summary::
      :meta:
   
   .. sidebar-links::
      :github:
      :pypi: myproject
   
   Installation
   ------------
   
   .. code-block:: bash
      :caption: Install from PyPI
      
      pip install myproject
   
   Configuration
   =============
   
   Required Settings
   -----------------
   
   .. confval:: api_key
      :type: str
      :required: True
      
      Your API key for authentication.
   
   Optional Settings
   -----------------
   
   .. confval:: timeout
      :type: int
      :default: 30
      
      Request timeout in seconds.
   
   .. confval:: retry_count
      :type: int
      :default: 3
      
      Number of retries for failed requests.
   
   API Reference
   =============
   
   Main Classes
   ------------
   
   .. autoclasssumm:: myproject.Client
      :autosummary-members:
   
   .. autoclass:: myproject.Client
      :members:
      :show-inheritance:
   
   Examples
   ========
   
   Quick Start
   -----------
   
   .. code-block:: python
      :linenos:
      :caption: Quick start example
      
      from myproject import Client
      
      client = Client(api_key="your-key")
      result = client.fetch_data()
      print(result)

Best Practices
--------------

Recommendations
~~~~~~~~~~~~~~~

- Use confval for all configuration options
- Add type and default information
- Use autoclasssumm for API overviews
- Enhance code blocks with captions and line numbers
- Integrate GitHub links where appropriate

Common Patterns
~~~~~~~~~~~~~~~

Standard patterns for using sphinx-toolbox:

1. **Config Docs**: Use confval directive for settings
2. **API Summaries**: Use autoclasssumm for overviews
3. **Code Examples**: Enhance with line numbers and highlighting

Integration Tips
----------------

Working with Other Extensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

sphinx-toolbox integrates well with:

- sphinx.ext.autodoc for API documentation
- sphinx.ext.napoleon for docstring parsing
- Theme extensions for enhanced styling

Additional Resources
--------------------

- `PyPI Package <https://pypi.org/project/sphinx-toolbox/>`_
- `Official Documentation <https://sphinx-toolbox.readthedocs.io/>`_
- :doc:`Complete Tutorial <../tutorials/packages/sphinx-toolbox>`
- :ref:`Package API Documentation <pdoc-sphinx-toolbox>`
Next Steps
----------
- Explore the :doc:`tutorial <../tutorials/packages/sphinx-toolbox>`
- Check the official documentation
- Try the examples in your own projects
- Customize for your specific needs

