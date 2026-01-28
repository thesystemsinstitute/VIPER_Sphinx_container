Sphinx Terraform Tutorial
=========================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-terraform/>`_
   - :doc:`See Working Example <../../examples/sphinx-terraform-example>`

This tutorial demonstrates how to use sphinx-terraform in your Sphinx documentation.

What is Sphinx Terraform?
--------------------------

sphinx-terraform is a Sphinx extension that provides:

- Terraform documentation support
- Easy integration with Sphinx
- Comprehensive configuration options
- Professional documentation output

Installation
------------

sphinx-terraform is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinx_terraform; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``docs/conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_terraform',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinx_terraform']
   
   # Configuration options
   terraform_sources = ['terraform/']
   terraform_docs_path = 'docs/terraform'

Basic Usage
-----------

Getting Started
~~~~~~~~~~~~~~~

Document Terraform modules:

.. code-block:: rst

   .. terraform-module:: mymodule
      :path: terraform/modules/mymodule

Document Resources
~~~~~~~~~~~~~~~~~~

Document Terraform resources:

.. code-block:: rst

   .. terraform-resource:: aws_instance
      :provider: aws

Common Use Cases
----------------

Module Documentation
~~~~~~~~~~~~~~~~~~~~

Document Terraform modules automatically:

.. code-block:: rst

   .. terraform-module:: vpc
      :source: terraform/modules/vpc
      :show-variables:
      :show-outputs:

Provider Documentation
~~~~~~~~~~~~~~~~~~~~~~

Document cloud provider resources:

.. code-block:: rst

   .. terraform-provider:: aws
      :version: "~> 4.0"

Advanced Features
-----------------

Auto-generate Docs
~~~~~~~~~~~~~~~~~~

Automatically generate module documentation:

.. code-block:: python

   # In conf.py
   terraform_auto_generate = True
   terraform_module_paths = ['terraform/modules']

Variable Tables
~~~~~~~~~~~~~~~

Display variable tables:

.. code-block:: rst

   .. terraform-variables:: mymodule

Best Practices
--------------

Tips and Guidelines
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Keep Terraform code documented
- Use clear variable descriptions
- Document module dependencies
- Include usage examples
- Test documentation builds

Troubleshooting
---------------

Common Issues
~~~~~~~~~~~~~

**Issue**: Module not found

**Solution**: Check module path configuration.

**Issue**: Variables not showing

**Solution**: Ensure variables are properly defined in Terraform files.

Additional Resources
--------------------

- :doc:`Working Example <../../examples/sphinx-terraform-example>`
- `PyPI Package <https://pypi.org/project/sphinx-terraform/>`_
