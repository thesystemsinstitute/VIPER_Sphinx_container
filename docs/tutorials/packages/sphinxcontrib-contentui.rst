Sphinxcontrib Contentui Tutorial
=================================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinxcontrib-contentui/>`_
   - `API Documentation <../../pdoc/sphinxcontrib_contentui/index.html>`_
   - `Manual <https://sphinxcontrib-contentui.readthedocs.io/>`_
   - :doc:`Working Example <../../examples/sphinxcontrib-contentui-example>`


.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinxcontrib-contentui in your Sphinx documentation.

What is Sphinxcontrib Contentui?
---------------------------------

sphinxcontrib-contentui is a Sphinx extension that provides:

- UI components for content
- Easy integration with Sphinx
- Comprehensive configuration options
- Professional documentation output

sphinxcontrib-contentui provides:

- UI components for content
- Integration with Sphinx documentation
- Flexible configuration options
- Professional output formatting

Key Features
~~~~~~~~~~~~

- **Tabs**: Create tabbed content
- **Toggle**: Collapsible sections
- **Panels**: Organized content panels
- **Responsive**: Mobile-friendly components
Installation
------------

sphinxcontrib-contentui is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinxcontrib.contentui; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``docs/conf.py``:

.. code-block:: python

   extensions = [
       'sphinxcontrib.contentui',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinxcontrib.contentui']
   
   # Configuration options
   # Add package-specific configuration here


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinxcontrib.contentui',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

Complete configuration with all features:

.. code-block:: python

   extensions = ['sphinxcontrib.contentui']
   
   # Package-specific configuration
   # contentui options can be configured here

Basic Usage
-----------

Getting Started
~~~~~~~~~~~~~~~

Create tabs:

.. code-block:: rst

   .. tab-container::
   
      .. tab-item:: Python
      
         .. code-block:: python
         
            print("Hello, World!")
      
      .. tab-item:: JavaScript
      
         .. code-block:: javascript
         
            console.log("Hello, World!");

Common Use Cases
----------------

Code Examples in Tabs
~~~~~~~~~~~~~~~~~~~~~~

Display code in multiple languages:

.. code-block:: rst

   .. tab-container::
      :new-group:
   
      .. tab-item:: Python
      
         Code here
      
      .. tab-item:: Java
      
         Code here

Collapsible Content
~~~~~~~~~~~~~~~~~~~

Create collapsible sections:

.. code-block:: rst

   .. toggle::
   
      Hidden content that can be expanded

Advanced Features
-----------------

Nested Tabs
~~~~~~~~~~~

Create nested tab structures:

.. code-block:: rst

   .. tab-container::
   
      .. tab-item:: Level 1
      
         .. tab-container::
         
            .. tab-item:: Level 2
            
               Content

Best Practices
--------------

Tips and Guidelines
~~~~~~~~~~~~~~~~~~~

- Use tabs for related content
- Keep tab labels clear
- Organize content logically
- Test on different devices
- Use appropriate nesting levels

Troubleshooting
---------------

Common Issues
~~~~~~~~~~~~~

**Issue**: Tabs not rendering

**Solution**: Check JavaScript is loaded and syntax is correct.

**Issue**: Styling issues

**Solution**: Review CSS and ensure proper theme integration.

Additional Resources
--------------------

- :doc:`Working Example <../../examples/sphinxcontrib-contentui-example>`
- `PyPI Package <https://pypi.org/project/sphinxcontrib-contentui/>`_
- `Official Documentation <https://sphinxcontrib-contentui.readthedocs.io/>`_
