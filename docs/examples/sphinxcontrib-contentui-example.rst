Sphinxcontrib Contentui Example
================================

.. note::

   **Package**: sphinxcontrib-contentui  
   **Purpose**: UI components for content  
   **Tutorial**: See :doc:`../tutorials/packages/sphinxcontrib-contentui` for complete tutorial

This page demonstrates **sphinxcontrib-contentui** - UI components for content.

.. contents:: Contents
   :local:
   :depth: 3

Overview
--------

What is sphinxcontrib-contentui?
---------------------------------

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

Using pip
~~~~~~~~~

Install the extension:

.. code-block:: bash

   pip install sphinxcontrib-contentui

Or add to your ``requirements.txt``:

.. code-block:: text

   sphinxcontrib-contentui
   sphinx>=5.0.0

Configuration
-------------

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

Example 1: Tabbed Code Examples
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Display code in multiple languages:

.. code-block:: rst

   Installation
   ============
   
   .. tab-container::
   
      .. tab-item:: pip
      
         .. code-block:: bash
         
            pip install mypackage
      
      .. tab-item:: conda
      
         .. code-block:: bash
         
            conda install mypackage
      
      .. tab-item:: Source
      
         .. code-block:: bash
         
            git clone https://github.com/user/mypackage
            cd mypackage
            pip install -e .

Example 2: Collapsible Sections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create expandable content:

.. code-block:: rst

   Frequently Asked Questions
   ==========================
   
   .. toggle::
      :title: How do I install this?
   
      Install using pip:
      
      .. code-block:: bash
      
         pip install mypackage
   
   .. toggle::
      :title: Where can I find examples?
   
      Check the examples directory or visit our documentation.

Real-World Examples
-------------------

Example: Multi-platform Instructions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Platform-specific documentation:

.. code-block:: rst

   Getting Started
   ===============
   
   Choose your operating system:
   
   .. tab-container::
      :new-group:
   
      .. tab-item:: Linux
      
         Installation on Linux:
         
         .. code-block:: bash
         
            sudo apt-get install dependencies
            pip install mypackage
         
         Configuration:
         
         Edit ``/etc/mypackage/config.yml``
      
      .. tab-item:: macOS
      
         Installation on macOS:
         
         .. code-block:: bash
         
            brew install dependencies
            pip install mypackage
         
         Configuration:
         
         Edit ``~/Library/Application Support/mypackage/config.yml``
      
      .. tab-item:: Windows
      
         Installation on Windows:
         
         .. code-block:: powershell
         
            choco install dependencies
            pip install mypackage
         
         Configuration:
         
         Edit ``%APPDATA%\mypackage\config.yml``

Example: API Examples in Multiple Languages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Show API usage across languages:

.. code-block:: rst

   API Usage
   =========
   
   .. tab-container::
   
      .. tab-item:: Python
      
         .. code-block:: python
         
            from myapi import Client
            
            client = Client(api_key="your-key")
            result = client.get_data()
            print(result)
      
      .. tab-item:: JavaScript
      
         .. code-block:: javascript
         
            const Client = require('myapi');
            
            const client = new Client({apiKey: 'your-key'});
            const result = await client.getData();
            console.log(result);
      
      .. tab-item:: curl
      
         .. code-block:: bash
         
            curl -H "Authorization: Bearer your-key" \
                 https://api.example.com/data

Example: FAQ with Toggle
~~~~~~~~~~~~~~~~~~~~~~~~~

Collapsible FAQ section:

.. code-block:: rst

   Troubleshooting
   ===============
   
   .. toggle::
      :title: My build is failing, what should I do?
      :open:
   
      First, check the build logs:
      
      .. code-block:: bash
      
         make clean
         make html
      
      Common issues:
      
      - Missing dependencies
      - Configuration errors
      - Syntax errors in RST files
   
   .. toggle::
      :title: How do I customize the theme?
   
      Create a custom CSS file in ``_static/custom.css`` and add:
      
      .. code-block:: python
      
         html_static_path = ['_static']
         html_css_files = ['custom.css']

Example: Nested Tabs
~~~~~~~~~~~~~~~~~~~~

Complex nested tab structure:

.. code-block:: rst

   Framework Examples
   ==================
   
   .. tab-container::
   
      .. tab-item:: Web Frameworks
      
         .. tab-container::
         
            .. tab-item:: Django
            
               Django example code...
            
            .. tab-item:: Flask
            
               Flask example code...
      
      .. tab-item:: Testing Frameworks
      
         .. tab-container::
         
            .. tab-item:: pytest
            
               pytest example code...
            
            .. tab-item:: unittest
            
               unittest example code...

Best Practices
--------------

Recommendations
~~~~~~~~~~~~~~~

- Use tabs for related content alternatives
- Keep tab labels short and clear
- Use toggle for optional/advanced content
- Test responsive behavior
- Don't over-nest tabs

Common Patterns
~~~~~~~~~~~~~~~

Standard patterns for using sphinxcontrib-contentui:

1. **Multi-language Code**: Tabs for different programming languages
2. **Platform-specific**: Tabs for different operating systems
3. **FAQ**: Toggle for question/answer pairs

Integration Tips
----------------

Working with Other Extensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

sphinxcontrib-contentui integrates well with:

- Standard Sphinx themes
- Code highlighting extensions
- Custom documentation layouts

Additional Resources
--------------------

- :doc:`Complete Tutorial <../tutorials/packages/sphinxcontrib-contentui>`
- `PyPI Package <https://pypi.org/project/sphinxcontrib-contentui/>`_
- `Official Documentation <https://sphinxcontrib-contentui.readthedocs.io/>`_
- :ref:`Package API Documentation <pdoc-sphinxcontrib-contentui>`

Next Steps
----------

- Explore the :doc:`tutorial <../tutorials/packages/sphinxcontrib-contentui>`
- Check the official documentation
- Try the examples in your own projects
- Customize for your specific needs
