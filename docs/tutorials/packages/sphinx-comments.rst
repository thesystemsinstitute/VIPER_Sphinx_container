Sphinx Comments Tutorial
========================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-comments/>`_
   - :doc:`See Working Example <../../examples/sphinx-comments-example>`

This tutorial demonstrates how to use sphinx-comments in your Sphinx documentation.

What is Sphinx Comments?
-------------------------

sphinx-comments is a Sphinx extension that provides:

- Comments in documentation
- Easy integration with Sphinx
- Comprehensive configuration options
- Professional documentation output

Installation
------------

sphinx-comments is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinx_comments; print('Installed')"

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

Additional Resources
--------------------

- :doc:`Working Example <../../examples/sphinx-comments-example>`
- `PyPI Package <https://pypi.org/project/sphinx-comments/>`_
