Sphinx Comments Tutorial
========================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-comments/>`_
   - `API Documentation <../../pdoc/sphinx_comments/index.html>`_
   - `Manual <https://github.com/sphinx-contrib/comments>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinx-comments in your Sphinx documentation.

What is Sphinx Comments?
-------------------------
sphinx-comments is a Sphinx extension that provides:

- Comments in documentation
- Easy integration with Sphinx
- Comprehensive configuration options
- Professional documentation output

sphinx-comments provides:

- Comments in documentation
- Integration with Sphinx documentation
- Flexible configuration options
- Professional output formatting

Key Features
~~~~~~~~~~~~

- **Comment Integration**: Add comments to documentation pages
- **Multiple Systems**: Support for various comment systems
- **Easy Setup**: Simple configuration
- **Moderation**: Comment moderation support


Installation
------------

sphinx-comments is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm viper-sphinx:latest python -c "import sphinx_comments; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``docs/conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_comments',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinx_comments']
   
   # Configuration options
   comments_config = {
       'utterances': {
           'repo': 'username/repo',
           'issue-term': 'pathname',
       }
   }


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

Getting Started
~~~~~~~~~~~~~~~

Enable comments on pages:

.. code-block:: rst

   .. comments::

Common Use Cases
----------------

Page Comments
~~~~~~~~~~~~~

Add comments section to specific pages:

.. code-block:: rst

   Documentation Page
   ==================
   
   Content here...
   
   .. comments::
      :config: utterances

Advanced Features
-----------------

Custom Comment Systems
~~~~~~~~~~~~~~~~~~~~~~

Configure different comment systems:

.. code-block:: python

   # In conf.py
   comments_config = {
       'utterances': {
           'repo': 'username/repo',
           'theme': 'github-light',
       },
       'disqus': {
           'shortname': 'your-disqus-shortname',
       }
   }

Best Practices
--------------

Tips and Guidelines
~~~~~~~~~~~~~~~~~~~

- Enable comments selectively
- Moderate comments regularly
- Configure appropriate comment system
- Test comment integration
- Follow privacy guidelines

Troubleshooting
---------------

Common Issues
~~~~~~~~~~~~~

**Issue**: Comments not showing

**Solution**: Check configuration and ensure comment system is properly set up.

**Issue**: Authentication errors

**Solution**: Verify repository access and authentication settings.


Practical Examples
------------------

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

- `PyPI Package <https://pypi.org/project/sphinx-comments/>`_
- :doc:`Complete Tutorial <../tutorials/packages/sphinx-comments>`
- `Utterances <https://utteranc.es/>`_
- `Disqus <https://disqus.com/>`_
- :ref:`Package API Documentation <pdoc-sphinx-comments>`
Next Steps
----------
- Explore the :doc:`tutorial <../tutorials/packages/sphinx-comments>`
- Check the official documentation
- Try the examples in your own projects
- Customize for your specific needs

