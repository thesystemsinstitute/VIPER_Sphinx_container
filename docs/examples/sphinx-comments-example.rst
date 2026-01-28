Sphinx Comments Example
=======================

.. note::

   **Package**: sphinx-comments  
   **Purpose**: Comments in documentation  
   **Tutorial**: See :doc:`../tutorials/packages/sphinx-comments` for complete tutorial

This page demonstrates **sphinx-comments** - Comments in documentation.

.. contents:: Contents
   :local:
   :depth: 3

Overview
--------


Key Features
~~~~~~~~~~~~

- **Comment Integration**: Add comments to documentation pages
- **Multiple Systems**: Support for various comment systems
- **Easy Setup**: Simple configuration
- **Moderation**: Comment moderation support

Installation
------------

Using pip
~~~~~~~~~

Install the extension:

.. code-block:: bash

   pip install sphinx-comments

Or add to your ``requirements.txt``:

.. code-block:: text

   sphinx-comments
   sphinx>=5.0.0

Configuration
-------------

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_comments',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

Complete configuration with all features:

.. code-block:: python

   extensions = ['sphinx_comments']
   
   # Package-specific configuration
   comments_config = {
       'utterances': {
           'repo': 'username/repository',
           'issue-term': 'pathname',
           'label': 'documentation',
           'theme': 'github-light',
       },
       'disqus': {
           'shortname': 'your-disqus-shortname',
       },
       'hypothesis': True,
   }

Basic Usage
-----------

Example 1: Utterances Comments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use GitHub Utterances:

.. code-block:: rst

   My Documentation Page
   =====================
   
   Content goes here...
   
   Comments
   --------
   
   .. comments::
      :config: utterances

Example 2: Disqus Comments
~~~~~~~~~~~~~~~~~~~~~~~~~~

Use Disqus comments:

.. code-block:: rst

   .. comments::
      :config: disqus

Real-World Examples
-------------------

Example: Blog-style Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Enable comments on tutorial pages:

.. code-block:: python

   # In conf.py
   comments_config = {
       'utterances': {
           'repo': 'myorg/docs',
           'issue-term': 'pathname',
           'label': '💬 comments',
           'theme': 'preferred-color-scheme',
       }
   }

Then in RST:

.. code-block:: rst

   Tutorial: Getting Started
   =========================
   
   This tutorial explains...
   
   [Tutorial content]
   
   Discussion
   ----------
   
   .. comments::

Example: Conditional Comments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Enable comments only on certain pages:

.. code-block:: python

   # In conf.py
   def setup(app):
       app.add_config_value('enable_comments', False, 'html')

Then in specific pages:

.. code-block:: rst

   .. only:: enable_comments
   
      .. comments::

Example: Custom Styling
~~~~~~~~~~~~~~~~~~~~~~~

Style the comments section:

.. code-block:: css

   /* In _static/custom.css */
   .comments-section {
       margin-top: 2em;
       padding-top: 2em;
       border-top: 2px solid #e0e0e0;
   }
   
   .utterances {
       max-width: 100%;
   }

Best Practices
--------------

Recommendations
~~~~~~~~~~~~~~~

- Enable comments on appropriate pages
- Set up moderation
- Use clear labels for issues
- Test comment system
- Follow privacy regulations

Common Patterns
~~~~~~~~~~~~~~~

Standard patterns for using sphinx-comments:

1. **Tutorial Comments**: Enable on tutorial pages
2. **Blog Posts**: Comments on blog-style documentation
3. **FAQ**: Allow questions and answers

Integration Tips
----------------

Working with Other Extensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

sphinx-comments integrates well with:

- Standard Sphinx themes
- Custom documentation layouts
- Blog and tutorial systems

Additional Resources
--------------------

- :doc:`Complete Tutorial <../tutorials/packages/sphinx-comments>`
- `PyPI Package <https://pypi.org/project/sphinx-comments/>`_
- `Utterances <https://utteranc.es/>`_
- `Disqus <https://disqus.com/>`_
- :ref:`Package API Documentation <pdoc-sphinx-comments>`

Next Steps
----------

- Explore the :doc:`tutorial <../tutorials/packages/sphinx-comments>`
- Check the official documentation
- Try the examples in your own projects
- Customize for your specific needs
