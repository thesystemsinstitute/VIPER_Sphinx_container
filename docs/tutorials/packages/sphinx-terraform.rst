Sphinx Terraform Tutorial
=========================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-terraform/>`_
   - `Manual <https://github.com/sphinx-contrib/terraform>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinx-terraform in your Sphinx documentation.

What is Sphinx Terraform?
--------------------------
sphinx-terraform is a Sphinx extension that provides:

- Terraform documentation support
- Easy integration with Sphinx
- Comprehensive configuration options
- Professional documentation output

sphinx-terraform provides:

- Terraform documentation support
- Integration with Sphinx documentation
- Flexible configuration options
- Professional output formatting

Key Features
~~~~~~~~~~~~

- **Module Documentation**: Automatic Terraform module documentation
- **Resource Documentation**: Document Terraform resources
- **Variable Tables**: Display input/output variables
- **Provider Support**: Multi-cloud provider support


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


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_terraform',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

Complete configuration with all features:

.. code-block:: python

   extensions = ['sphinx_terraform']
   
   # Package-specific configuration
   terraform_sources = ['terraform/', 'modules/']
   terraform_docs_path = 'docs/terraform'
   terraform_auto_generate = True
   terraform_module_paths = [
       'terraform/modules',
       'terraform/environments',
   ]

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


Practical Examples
------------------

Overview
--------


Key Features
~~~~~~~~~~~~

- **Module Documentation**: Automatic Terraform module documentation
- **Resource Documentation**: Document Terraform resources
- **Variable Tables**: Display input/output variables
- **Provider Support**: Multi-cloud provider support

Installation
------------

Using pip
~~~~~~~~~

Install the extension:

.. code-block:: bash

   pip install sphinx-terraform

Or add to your ``requirements.txt``:

.. code-block:: text

   sphinx-terraform
   sphinx>=5.0.0

Configuration
-------------

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_terraform',
       # ... other extensions
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

Complete configuration with all features:

.. code-block:: python

   extensions = ['sphinx_terraform']
   
   # Package-specific configuration
   terraform_sources = ['terraform/', 'modules/']
   terraform_docs_path = 'docs/terraform'
   terraform_auto_generate = True
   terraform_module_paths = [
       'terraform/modules',
       'terraform/environments',
   ]

Basic Usage
-----------

Example 1: Document a Module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Document Terraform module:

.. code-block:: rst

   VPC Module
   ==========
   
   .. terraform-module:: vpc
      :path: terraform/modules/vpc
      :show-variables:
      :show-outputs:
      :show-resources:

Example 2: Variable Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Display module variables:

.. code-block:: rst

   Module Variables
   ================
   
   .. terraform-variables:: vpc
   
   Module Outputs
   ==============
   
   .. terraform-outputs:: vpc

Real-World Examples
-------------------

Example: AWS Infrastructure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Document AWS infrastructure:

.. code-block:: rst

   AWS Infrastructure
   ==================
   
   VPC Module
   ----------
   
   .. terraform-module:: vpc
      :source: terraform/modules/vpc
   
   Variables:
   
   .. terraform-variables:: vpc
      :module-path: terraform/modules/vpc
   
   Outputs:
   
   .. terraform-outputs:: vpc
      :module-path: terraform/modules/vpc
   
   EC2 Instance Module
   -------------------
   
   .. terraform-module:: ec2
      :source: terraform/modules/ec2
      :show-examples:

Example: Multi-cloud Setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Document multi-cloud infrastructure:

.. code-block:: rst

   Multi-cloud Infrastructure
   ===========================
   
   AWS Resources
   -------------
   
   .. terraform-provider:: aws
      :version: "~> 4.0"
   
   .. terraform-module:: aws-network
      :path: terraform/aws/network
   
   Azure Resources
   ---------------
   
   .. terraform-provider:: azurerm
      :version: "~> 3.0"
   
   .. terraform-module:: azure-network
      :path: terraform/azure/network
   
   GCP Resources
   -------------
   
   .. terraform-provider:: google
      :version: "~> 4.0"
   
   .. terraform-module:: gcp-network
      :path: terraform/gcp/network

Example: Complete Module Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Full module documentation:

.. code-block:: rst

   Kubernetes Cluster Module
   ==========================
   
   Overview
   --------
   
   This module creates a production-ready Kubernetes cluster.
   
   .. terraform-module:: k8s-cluster
      :path: terraform/modules/k8s-cluster
   
   Usage Example
   -------------
   
   .. code-block:: hcl
   
      module "k8s_cluster" {
        source = "./modules/k8s-cluster"
        
        cluster_name    = "production"
        node_count      = 3
        machine_type    = "n1-standard-4"
        region          = "us-central1"
      }
   
   Input Variables
   ---------------
   
   .. terraform-variables:: k8s-cluster
   
   Output Values
   -------------
   
   .. terraform-outputs:: k8s-cluster
   
   Resources Created
   -----------------
   
   .. terraform-resources:: k8s-cluster

Best Practices
--------------

Recommendations
~~~~~~~~~~~~~~~

- Document all module variables with descriptions
- Provide usage examples
- Document outputs clearly
- Keep module documentation up-to-date
- Include version requirements

Common Patterns
~~~~~~~~~~~~~~~

Standard patterns for using sphinx-terraform:

1. **Module Docs**: Complete module documentation with vars/outputs
2. **Provider Docs**: Document provider configurations
3. **Examples**: Include practical usage examples

Integration Tips
----------------

Working with Other Extensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

sphinx-terraform integrates well with:

- Standard Sphinx extensions
- Cloud infrastructure documentation
- DevOps documentation workflows

Additional Resources
--------------------

- `PyPI Package <https://pypi.org/project/sphinx-terraform/>`_
- :doc:`Complete Tutorial <../tutorials/packages/sphinx-terraform>`
- `Terraform Documentation <https://www.terraform.io/docs>`_
- :ref:`Package API Documentation <pdoc-sphinx-terraform>`
Next Steps
----------
- Explore the :doc:`tutorial <../tutorials/packages/sphinx-terraform>`
- Check the official documentation
- Try the examples in your own projects
- Customize for your specific needs

