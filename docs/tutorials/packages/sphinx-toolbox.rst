Sphinx Toolbox Tutorial
=======================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-toolbox/>`_
   - `API Documentation <../../pdoc/sphinx_toolbox/index.html>`_
   - `Manual <https://sphinx-toolbox.readthedocs.io/>`_
   - :doc:`Working Example <../../examples/sphinx-toolbox-example>`


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

Additional Resources
--------------------

- :doc:`Working Example <../../examples/sphinx-toolbox-example>`
- `PyPI Package <https://pypi.org/project/sphinx-toolbox/>`_
- `Official Documentation <https://sphinx-toolbox.readthedocs.io/>`_
