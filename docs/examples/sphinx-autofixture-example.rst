Sphinx-Autofixture Example
==========================

.. note::

   **Package**: sphinx-autofixture  
   **Purpose**: Automatically document test fixtures and pytest fixtures  
   **Tutorial**: See :doc:`../tutorials/packages/sphinx-autofixture` for complete tutorial

This page demonstrates the **sphinx-autofixture** extension for automatically generating documentation for pytest fixtures and test utilities.

.. contents:: Contents
   :local:
   :depth: 3


Installation
------------

Using pip
~~~~~~~~~

Install the extension:

.. code-block:: bash

   pip install sphinx-autofixture

Or add to your ``requirements.txt``:

.. code-block:: text

   sphinx-autofixture>=1.1.0
   pytest>=6.0.0

Configuration
-------------

Basic Configuration
~~~~~~~~~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_autofixture',
       'sphinx.ext.autodoc',
       # ... other extensions
   ]
   
   # Basic fixture documentation
   autofixture_enabled = True
   autofixture_conftest_path = ['tests/conftest.py']

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

Complete configuration with all options:

.. code-block:: python

   # Fixture Discovery
   autofixture_enabled = True
   autofixture_conftest_path = [
       'tests/conftest.py',
       'tests/fixtures/common.py',
       'tests/fixtures/database.py',
   ]
   autofixture_exclude_patterns = ['*.internal', '_*']
   
   # Documentation Options
   autofixture_show_scope = True
   autofixture_show_dependencies = True
   autofixture_show_parameters = True
   autofixture_show_source = True
   autofixture_show_usage = True
   
   # Dependency Graph
   autofixture_generate_graph = True
   autofixture_graph_format = 'svg'  # 'svg', 'png', 'pdf'
   autofixture_graph_direction = 'TB'  # 'TB', 'LR', 'BT', 'RL'
   
   # Display Options
   autofixture_format = 'detailed'  # 'detailed', 'compact', 'table'
   autofixture_group_by = 'scope'   # 'scope', 'file', 'name'
   autofixture_sort_by = 'name'     # 'name', 'scope', 'file'
   
   # Type Annotations
   autofixture_show_types = True
   autofixture_resolve_types = True
   
   # Examples
   autofixture_generate_examples = True
   autofixture_example_format = 'pytest'  # 'pytest', 'doctest'
   
   # Cross-References
   autofixture_generate_refs = True
   autofixture_ref_prefix = 'fixture-'

Directives
----------

autofixture Directive
~~~~~~~~~~~~~~~~~~~~~

Document a single fixture:

.. code-block:: rst

   .. autofixture:: database
      :show-scope: true
      :show-dependencies: true
      
      Database connection fixture.

With All Options
~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. autofixture:: user_factory
      :show-scope: true
      :show-dependencies: true
      :show-parameters: true
      :show-source: true
      :show-usage: true
      :show-type: true
      
      Factory fixture for creating test users.

autofixturelist Directive
~~~~~~~~~~~~~~~~~~~~~~~~~

Document multiple fixtures:

.. code-block:: rst

   .. autofixturelist::
      :conftest: tests/conftest.py
      :group-by: scope
      :format: detailed
      
      All fixtures from conftest.py.

autofixturegroup Directive
~~~~~~~~~~~~~~~~~~~~~~~~~~

Document related fixtures:

.. code-block:: rst

   .. autofixturegroup:: Database Fixtures
      :fixtures: db, db_session, db_transaction
      :show-dependencies: true
      
      Database-related fixtures.

autofixturegraph Directive
~~~~~~~~~~~~~~~~~~~~~~~~~~

Show fixture dependency graph:

.. code-block:: rst

   .. autofixturegraph::
      :fixtures: app, client, authenticated_user
      :format: svg
      :direction: TB
      
      Dependency graph for application fixtures.

Roles
-----

Fixture References
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Use the :fixture:`database` fixture in your tests.
   
   The :fixture:`user_factory` creates test users.
   
   See :fixture:`authenticated_client` for API testing.

Practical Examples
------------------

Complete Fixture Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**File**: ``tests/fixtures.rst``

.. code-block:: rst

   Test Fixtures
   =============
   
   This page documents all pytest fixtures available in the test suite.
   
   .. autofixturelist::
      :conftest: tests/conftest.py
      :group-by: scope
      :format: detailed
      :show-dependencies: true
      
      Complete fixture reference.

Fixture with Source
~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Database Fixture
   ================
   
   .. autofixture:: database
      :show-scope: true
      :show-source: true
      :show-type: true
      
      Provides a database connection for tests.
   
   Example Usage
   -------------
   
   .. code-block:: python
   
      def test_user_creation(database):
          user = User.create(database, name="Test User")
          assert user.id is not None

Parametrized Fixture
~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Browser Fixture
   ===============
   
   .. autofixture:: browser
      :show-parameters: true
      :show-scope: true
      
      Provides different browser instances for testing.
   
   This fixture is parametrized to run tests across multiple browsers:
   
   - Chrome
   - Firefox
   - Safari
   
   Usage Example
   -------------
   
   .. code-block:: python
   
      def test_homepage(browser):
          browser.get("https://example.com")
          assert "Example" in browser.title

Fixture Dependencies
~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Application Fixtures
   ====================
   
   Dependency Graph
   ----------------
   
   .. autofixturegraph::
      :fixtures: app, client, authenticated_user
      :format: svg
      
      Shows how fixtures depend on each other.
   
   Base Application
   ----------------
   
   .. autofixture:: app
      :show-scope: true
      
      Creates Flask application instance.
   
   Test Client
   -----------
   
   .. autofixture:: client
      :show-dependencies: true
      
      Provides test client (depends on app fixture).
   
   Authenticated User
   ------------------
   
   .. autofixture:: authenticated_user
      :show-dependencies: true
      
      Creates logged-in user (depends on app and client).

Grouped Fixtures
~~~~~~~~~~~~~~~~

.. code-block:: rst

   Fixture Reference
   =================
   
   Session Fixtures
   ----------------
   
   .. autofixturelist::
      :scope: session
      :format: table
      
      Fixtures with session scope.
   
   Module Fixtures
   ---------------
   
   .. autofixturelist::
      :scope: module
      :format: table
      
      Fixtures with module scope.
   
   Function Fixtures
   -----------------
   
   .. autofixturelist::
      :scope: function
      :format: compact
      
      Fixtures with function scope.

Sample Fixtures
---------------

Basic Fixture
~~~~~~~~~~~~~

.. code-block:: python

   # tests/conftest.py
   import pytest
   
   @pytest.fixture
   def sample_data():
       """Provide sample test data.
       
       Returns:
           dict: Sample data dictionary with test values.
       """
       return {
           'name': 'Test User',
           'email': 'test@example.com',
           'age': 30
       }

Fixture with Scope
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   @pytest.fixture(scope='session')
   def database():
       """Create database connection (session scope).
       
       This fixture creates a database connection that persists
       for the entire test session.
       
       Yields:
           Database: Database connection object.
       """
       db = Database.connect()
       yield db
       db.close()

Parametrized Fixture
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   @pytest.fixture(params=['chrome', 'firefox', 'safari'])
   def browser(request):
       """Provide browser instances (parametrized).
       
       This fixture is parametrized to run tests with different browsers.
       
       Args:
           request: pytest request object with parameter.
       
       Yields:
           WebDriver: Browser driver instance.
       """
       driver = get_driver(request.param)
       yield driver
       driver.quit()

Dependent Fixture
~~~~~~~~~~~~~~~~~

.. code-block:: python

   @pytest.fixture
   def authenticated_client(app, client):
       """Provide authenticated test client.
       
       This fixture depends on both app and client fixtures.
       
       Args:
           app: Flask application instance.
           client: Test client instance.
       
       Returns:
           FlaskClient: Authenticated test client.
       """
       with client.session_transaction() as session:
           session['user_id'] = create_test_user(app).id
       return client

Factory Fixture
~~~~~~~~~~~~~~~

.. code-block:: python

   @pytest.fixture
   def user_factory(database):
       """Factory for creating test users.
       
       Provides a factory function for creating multiple test users
       within a single test.
       
       Args:
           database: Database connection fixture.
       
       Returns:
           Callable: Factory function that creates users.
       """
       users = []
       
       def make_user(**kwargs):
           user = User.create(database, **kwargs)
           users.append(user)
           return user
       
       yield make_user
       
       # Cleanup
       for user in users:
           user.delete()

Advanced Features
-----------------

Fixture Introspection
~~~~~~~~~~~~~~~~~~~~~

Document fixture metadata:

.. code-block:: rst

   .. autofixture:: complex_fixture
      :show-scope: true
      :show-autouse: true
      :show-params: true
      :show-ids: true
      
      Complex fixture with detailed metadata.

Custom Formatting
~~~~~~~~~~~~~~~~~

Create custom fixture documentation templates:

**File**: ``_templates/autofixture.html``

.. code-block:: html+jinja

   <div class="fixture-doc">
     <h3 class="fixture-name">{{ fixture.name }}</h3>
     
     <div class="fixture-metadata">
       <span class="scope">Scope: {{ fixture.scope }}</span>
       {% if fixture.params %}
       <span class="params">Parameters: {{ fixture.params|length }}</span>
       {% endif %}
     </div>
     
     <div class="fixture-docstring">
       {{ fixture.docstring }}
     </div>
     
     {% if fixture.dependencies %}
     <div class="fixture-dependencies">
       <h4>Dependencies:</h4>
       <ul>
         {% for dep in fixture.dependencies %}
         <li><a href="#{{ dep }}">{{ dep }}</a></li>
         {% endfor %}
       </ul>
     </div>
     {% endif %}
     
     {% if fixture.source %}
     <div class="fixture-source">
       <h4>Source Code:</h4>
       <pre><code>{{ fixture.source }}</code></pre>
     </div>
     {% endif %}
   </div>

Fixture Collections
~~~~~~~~~~~~~~~~~~~

Organize fixtures into collections:

.. code-block:: rst

   Database Fixtures
   =================
   
   .. autofixturegroup:: Database
      :fixtures: db, db_session, db_transaction, db_cursor
      :show-graph: true
      
      All database-related fixtures.
   
   User Fixtures
   =============
   
   .. autofixturegroup:: Users
      :fixtures: user, admin_user, user_factory
      :show-dependencies: true
      
      User management fixtures.

Best Practices
--------------

Fixture Documentation
~~~~~~~~~~~~~~~~~~~~~

1. **Clear Docstrings**: Write comprehensive fixture docstrings
2. **Type Annotations**: Use type hints for return values
3. **Scope Documentation**: Explain why specific scopes are used
4. **Dependency Clarity**: Document fixture dependencies

Example:

.. code-block:: python

   @pytest.fixture(scope='module')
   def api_client(base_url: str) -> APIClient:
       """Create API client for testing.
       
       This fixture creates an API client that persists for the
       entire test module, reducing setup overhead.
       
       Args:
           base_url: Base URL fixture providing API endpoint.
       
       Returns:
           APIClient: Configured API client instance.
       
       Example:
           >>> def test_api_endpoint(api_client):
           ...     response = api_client.get('/users')
           ...     assert response.status_code == 200
       """
       client = APIClient(base_url)
       return client

Organization
~~~~~~~~~~~~

Organize fixture documentation logically:

.. code-block:: text

   docs/
   ├── testing/
   │   ├── index.rst              # Testing overview
   │   ├── fixtures.rst           # All fixtures
   │   ├── fixtures/
   │   │   ├── database.rst       # Database fixtures
   │   │   ├── api.rst            # API fixtures
   │   │   ├── users.rst          # User fixtures
   │   │   └── utilities.rst      # Utility fixtures
   │   └── examples.rst           # Test examples
   └── conf.py

Maintenance
~~~~~~~~~~~

Keep fixture documentation current:

.. code-block:: python

   # conf.py
   
   # Validate fixture documentation
   autofixture_validate = True
   autofixture_warn_missing_docs = True
   
   # Auto-update on changes
   autofixture_auto_rebuild = True

Troubleshooting
---------------

Fixtures Not Found
~~~~~~~~~~~~~~~~~~

**Problem**: Fixtures not appearing in documentation

**Solution**:

.. code-block:: python

   # Check conftest paths
   autofixture_conftest_path = [
       'tests/conftest.py',
       'tests/**/conftest.py',  # Recursive
   ]
   
   # Include fixture files
   autofixture_fixture_files = [
       'tests/fixtures/*.py',
   ]
   
   # Clear exclude patterns
   autofixture_exclude_patterns = []

Missing Dependencies
~~~~~~~~~~~~~~~~~~~~

**Problem**: Fixture dependencies not showing

**Solution**:

.. code-block:: python

   # Enable dependency detection
   autofixture_show_dependencies = True
   autofixture_detect_dependencies = True
   
   # Ensure pytest is importable
   import sys
   sys.path.insert(0, os.path.abspath('..'))

Graph Generation Fails
~~~~~~~~~~~~~~~~~~~~~~

**Problem**: Dependency graphs not generating

**Solution**:

.. code-block:: bash

   # Install graphviz
   pip install graphviz
   
   # Ensure graphviz system package installed
   # Ubuntu/Debian:
   sudo apt-get install graphviz
   
   # macOS:
   brew install graphviz

.. code-block:: python

   # conf.py
   autofixture_graph_format = 'svg'
   autofixture_graphviz_output_format = 'svg'

Integration Examples
--------------------

With Sphinx-Autodoc
~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Test Module
   ===========
   
   .. automodule:: tests.test_users
      :members:
   
   Fixtures Used
   -------------
   
   .. autofixturelist::
      :used-by: tests.test_users
      
      Fixtures used by this test module.

With Doctest
~~~~~~~~~~~~

.. code-block:: rst

   .. autofixture:: calculator
      :show-usage: true
      :example-format: doctest
      
      Simple calculator fixture.
      
      >>> def test_addition(calculator):
      ...     assert calculator.add(2, 3) == 5

With Coverage Reports
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   
   # Track fixture usage
   autofixture_track_usage = True
   autofixture_generate_coverage = True
   
   # Report unused fixtures
   autofixture_warn_unused = True

See Also
--------

Related Extensions
~~~~~~~~~~~~~~~~~~

- :doc:`sphinx-autodoc-example` - Python autodoc
- :doc:`pytest-doctestplus-example` - Enhanced doctest
- Pytest documentation: https://docs.pytest.org/

External Resources
~~~~~~~~~~~~~~~~~~

- pytest fixtures: https://docs.pytest.org/en/stable/fixture.html
- pytest-factoryboy: https://github.com/pytest-dev/pytest-factoryboy

Summary
-------

sphinx-autofixture provides comprehensive fixture documentation:

- **Automatic Discovery**: Find and document all fixtures
- **Rich Metadata**: Scope, dependencies, parameters
- **Dependency Graphs**: Visualize fixture relationships
- **Multiple Formats**: Detailed, compact, table views
- **Type Information**: Return type documentation
- **Usage Examples**: Show how to use fixtures
- **Integration**: Works with autodoc and pytest

Perfect for documenting test infrastructure and making fixtures discoverable for your testing team.
