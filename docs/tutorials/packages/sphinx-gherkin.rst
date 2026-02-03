Sphinx Gherkin Tutorial
=======================

.. note::

   **Package Resources:**

   - `PyPI Package <https://pypi.org/project/sphinx-gherkin/>`_
   - `API Documentation <../../pdoc/sphinx_gherkin/index.html>`_
   - `Manual <https://cblegare.gitlab.io/sphinx-gherkin>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial introduces sphinx-gherkin, a Sphinx extension for documenting Gherkin features.

What is Sphinx Gherkin?
-----------------------
Sphinx Gherkin provides a domain for Gherkin features so you can reference scenarios and steps in your docs.

Installation
------------

Install via pip:

.. code-block:: bash

   pip install sphinx-gherkin

Configuration
-------------

Enable the extension in ``conf.py``:

.. code-block:: python

   extensions = [
       "sphinx_gherkin",
   ]

Basic Usage
-----------

Include feature files and reference them in your documentation.

The Gherkin Domain
~~~~~~~~~~~~~~~~~~

sphinx-gherkin provides a ``gherkin`` domain with directives for documenting BDD scenarios:

.. code-block:: restructuredtext

   .. gherkin:feature:: User Authentication
      :file: features/auth.feature

      Feature for user login and registration workflows.

   .. gherkin:scenario:: Successful Login
      :feature: User Authentication

      Scenario verifying users can log in with valid credentials.

   .. gherkin:step:: Given the user is on the login page

      Navigate to the application login page.

Cross-Referencing
~~~~~~~~~~~~~~~~~

Reference Gherkin elements throughout your documentation:

.. code-block:: restructuredtext

   See :gherkin:feature:`User Authentication` for the complete login workflow.

   The :gherkin:scenario:`Successful Login` scenario covers the happy path.

   This implements :gherkin:step:`Given the user is on the login page`.

Advanced Features
-----------------

- Cross-reference Gherkin items through the domain.
- Integrate with Sphinx TOCs for feature navigation.
- Support for tags and scenario outlines.
- Background step documentation.

Configuration Options
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py

   extensions = ["sphinx_gherkin"]

   # Gherkin configuration
   gherkin_sources = ["features"]  # Directory containing .feature files
   gherkin_step_registry = True    # Enable step registry
   gherkin_show_tags = True        # Display tags in output

Examples
--------

Complete Feature Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a feature file ``features/login.feature``:

.. code-block:: gherkin

   @authentication @critical
   Feature: User Login
     As a registered user
     I want to log into the application
     So that I can access my account

     Background:
       Given the application is running
       And the database is seeded

     @smoke
     Scenario: Successful login with valid credentials
       Given I am on the login page
       When I enter my email "user@example.com"
       And I enter my password "secret123"
       And I click the login button
       Then I should be redirected to the dashboard
       And I should see "Welcome back"

     @edge-case
     Scenario: Login fails with invalid password
       Given I am on the login page
       When I enter my email "user@example.com"
       And I enter my password "wrongpassword"
       And I click the login button
       Then I should see "Invalid credentials"
       And I should remain on the login page

     Scenario Outline: Login with different user types
       Given I am on the login page
       When I log in as a <user_type> user
       Then I should see the <dashboard> dashboard

       Examples:
         | user_type | dashboard     |
         | admin     | Admin         |
         | editor    | Content       |
         | viewer    | Read-Only     |

Document the feature in RST:

.. code-block:: restructuredtext

   Authentication Features
   =======================

   .. gherkin:feature:: User Login
      :file: features/login.feature
      :tags: authentication, critical

      Complete documentation for the user login feature, covering
      successful authentication, error handling, and role-based access.

   Scenarios
   ---------

   .. gherkin:scenario:: Successful login with valid credentials
      :feature: User Login
      :tags: smoke

      Verifies that users with valid credentials can access their accounts.
      This is a critical smoke test scenario.

   .. gherkin:scenario:: Login fails with invalid password
      :feature: User Login
      :tags: edge-case

      Ensures proper error handling when authentication fails.

Step Registry
~~~~~~~~~~~~~

Document step definitions for reuse:

.. code-block:: restructuredtext

   Step Definitions
   ================

   Navigation Steps
   ----------------

   .. gherkin:step:: I am on the login page
      :type: Given

      Navigates to ``/login`` and waits for page load.

      **Implementation:**

      .. code-block:: python

         @given("I am on the login page")
         def step_impl(context):
             context.browser.get(context.base_url + "/login")
             context.browser.wait_for_element("#login-form")

   .. gherkin:step:: I should be redirected to the dashboard
      :type: Then

      Verifies URL change and dashboard element presence.

   Action Steps
   ------------

   .. gherkin:step:: I enter my email {email}
      :type: When

      Enters email in the login form.

      :param email: User's email address

   .. gherkin:step:: I click the login button
      :type: When

      Submits the login form.

Integrated API Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Combine Gherkin documentation with Python step implementations:

.. code-block:: restructuredtext

   Login Step Implementations
   ==========================

   Feature Reference
   -----------------

   See :gherkin:feature:`User Login` for the complete scenario definitions.

   Python Implementation
   ---------------------

   .. code-block:: python

      # steps/login_steps.py
      from behave import given, when, then

      @given("I am on the login page")
      def step_on_login_page(context):
          """Navigate to login page.

          See :gherkin:step:`I am on the login page` for usage.
          """
          context.page = LoginPage(context.browser)
          context.page.navigate()

      @when('I enter my email "{email}"')
      def step_enter_email(context, email):
          """Enter email in form.

          See :gherkin:step:`I enter my email {email}` for usage.
          """
          context.page.enter_email(email)

      @then('I should see "{message}"')
      def step_verify_message(context, message):
          """Verify message is displayed."""
          assert message in context.page.get_messages()

   Test Results Integration
   ------------------------

   Link test results to documentation:

   .. code-block:: restructuredtext

      .. note::

         :gherkin:scenario:`Successful login with valid credentials`
         passed in CI build #1234 (2 minutes ago).

Complete Project Structure
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text

   my-project/
   ├── features/
   │   ├── login.feature
   │   ├── registration.feature
   │   └── steps/
   │       ├── login_steps.py
   │       └── common_steps.py
   ├── docs/
   │   ├── conf.py
   │   ├── index.rst
   │   └── features/
   │       ├── index.rst
   │       ├── login.rst
   │       └── registration.rst
   └── pyproject.toml

Additional Resources
--------------------

- `Manual <https://cblegare.gitlab.io/sphinx-gherkin>`_
- `PyPI <https://pypi.org/project/sphinx-gherkin/>`_
- `API Documentation <../../pdoc/sphinx_gherkin/index.html>`_
