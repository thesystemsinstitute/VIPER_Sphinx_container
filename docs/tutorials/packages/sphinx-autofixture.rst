Sphinx-Autofixture Tutorial
===========================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-autofixture/>`_
   - `API Documentation <../../pdoc/sphinx_autofixture/index.html>`_
   - `Manual <https://github.com/sphinx-contrib/autofixture>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinx-autofixture to automatically document pytest fixtures in your Sphinx documentation.

What is Sphinx-Autofixture?
----------------------------
sphinx-autofixture is a Sphinx extension that provides:

- Pytest fixture documentation
- Automatic fixture discovery
- Scope documentation
- Parameter documentation
- Fixture dependencies
- Usage examples
- Cross-referencing
- Test documentation
- Conftest integration
- Plugin fixture support

This enables comprehensive documentation of your test fixtures alongside regular code documentation.

What is sphinx-autofixture?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

sphinx-autofixture is a Sphinx extension that automatically documents test fixtures, making it easy to:

- Document pytest fixtures
- Generate fixture reference pages
- Show fixture dependencies
- Display fixture scopes and parameters
- Create comprehensive test documentation

Key Features
~~~~~~~~~~~~

- **Automatic Fixture Discovery**: Find and document all fixtures
- **Dependency Visualization**: Show fixture dependency graphs
- **Scope Documentation**: Display fixture scope information
- **Parameter Documentation**: Document parametrized fixtures
- **Type Annotations**: Show fixture return types
- **Usage Examples**: Generate fixture usage examples
- **Cross-References**: Link between fixtures and tests
- **Multiple Sources**: Support conftest.py and fixture files


Installation
------------

sphinx-autofixture is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinx_autofixture; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``docs/conf.py``:

.. code-block:: python

   extensions = [
       'sphinx.ext.autodoc',
       'sphinx_autofixture',
   ]
   
   # Fixture documentation
   autofixture_docstring_style = 'sphinx'

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinx.ext.autodoc', 'sphinx_autofixture']
   
   # Fixture discovery
   autofixture_search_path = ['../tests']
   autofixture_conftest_dirs = ['../tests', '../tests/unit']
   
   # Display options
   autofixture_show_scope = True
   autofixture_show_params = True
   autofixture_show_dependencies = True
   
   # Formatting
   autofixture_docstring_style = 'sphinx'  # or 'google', 'numpy'
   autofixture_group_by_scope = True


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

Basic Usage
-----------

Document a Fixture
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. autofixture:: db_session

This documents the ``db_session`` fixture.

Document Multiple Fixtures
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. autofixture:: conftest
      :fixtures: db_session, api_client, temp_dir

Document by Scope
~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. autofixture:: conftest
      :scope: session

   Test Fixtures
   =============
   
   Database Fixtures
   -----------------
   
   Our test suite provides fixtures for database testing.
   
   Engine Fixture
   ~~~~~~~~~~~~~~
   
   .. autofixture:: db_engine
   
   Session Fixture
   ~~~~~~~~~~~~~~~
   
   .. autofixture:: db_session
   
   Usage Example
   ~~~~~~~~~~~~~
   
   .. code-block:: python
      
      def test_create_user(db_session):
          """Test user creation."""
          user = User(name='John Doe', email='john@example.com')
          db_session.add(user)
          db_session.commit()
          
          assert user.id is not None
          assert db_session.query(User).count() == 1

Example 2: API Client Fixtures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``tests/conftest.py``:

.. code-block:: python

   import pytest
   from myapp.client import APIClient
   
   @pytest.fixture(scope='session')
   def api_base_url():
       """
       Base URL for API testing.
       
       :return: Test API base URL
       """
       return 'http://localhost:8000/api'
   
   @pytest.fixture(scope='session')
   def api_token():
       """
       Authentication token for API testing.
       
       Generates a test token valid for the session.
       
       :return: JWT authentication token
       """
       return 'test-token-123'
   
   @pytest.fixture
   def api_client(api_base_url, api_token):
       """
       Authenticated API client for testing.
       
       :param api_base_url: Base URL fixture
       :param api_token: Authentication token fixture
       :return: Configured API client instance
       :rtype: APIClient
       
       The client is pre-configured with authentication
       and points to the test server.
       
       Example:
           >>> def test_get_user(api_client):
           ...     response = api_client.get('/users/1')
           ...     assert response.status_code == 200
       """
       client = APIClient(base_url=api_base_url, token=api_token)
       return client

``docs/testing/api-fixtures.rst``:

.. code-block:: rst

   API Testing Fixtures
   ====================
   
   Configuration Fixtures
   ----------------------
   
   .. autofixture:: api_base_url
   
   .. autofixture:: api_token
   
   Client Fixture
   --------------
   
   .. autofixture:: api_client
   
   Complete Example
   ----------------
   
   .. code-block:: python
      
      def test_user_endpoints(api_client):
          # Create user
          response = api_client.post('/users', {
              'name': 'Test User',
              'email': 'test@example.com'
          })
          assert response.status_code == 201
          user_id = response.json()['id']
          
          # Get user
          response = api_client.get(f'/users/{user_id}')
          assert response.status_code == 200
          assert response.json()['name'] == 'Test User'

Example 3: File System Fixtures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``tests/conftest.py``:

.. code-block:: python

   import pytest
   from pathlib import Path
   import tempfile
   import shutil
   
   @pytest.fixture
   def temp_dir():
       """
       Temporary directory for testing.
       
       Creates a temporary directory that is automatically
       cleaned up after the test completes.
       
       :return: Path to temporary directory
       :rtype: pathlib.Path
       
       Example:
           >>> def test_file_operations(temp_dir):
           ...     test_file = temp_dir / 'test.txt'
           ...     test_file.write_text('Hello')
           ...     assert test_file.exists()
       """
       temp_path = Path(tempfile.mkdtemp())
       yield temp_path
       shutil.rmtree(temp_path)
   
   @pytest.fixture
   def sample_file(temp_dir):
       """
       Sample text file for testing.
       
       :param temp_dir: Temporary directory fixture
       :return: Path to sample file
       :rtype: pathlib.Path
       
       Creates a file with sample content in the temp directory.
       """
       file_path = temp_dir / 'sample.txt'
       file_path.write_text('Sample content\nLine 2\nLine 3')
       return file_path

``docs/testing/file-fixtures.rst``:

.. code-block:: rst

   File System Fixtures
   ====================
   
   .. autofixture:: temp_dir
   
   .. autofixture:: sample_file

Example 4: Parametrized Fixtures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``tests/conftest.py``:

.. code-block:: python

   import pytest
   
   @pytest.fixture(params=['sqlite', 'postgresql', 'mysql'])
   def database_type(request):
       """
       Database type parameter fixture.
       
       Tests using this fixture will run once for each
       database type.
       
       :param request: Pytest request object
       :return: Database type string
       
       Supported values:
           - 'sqlite': SQLite database
           - 'postgresql': PostgreSQL database
           - 'mysql': MySQL database
       """
       return request.param
   
   @pytest.fixture(params=[1, 10, 100])
   def batch_size(request):
       """
       Batch size parameter for testing.
       
       :param request: Pytest request object
       :return: Batch size integer
       """
       return request.param

``docs/testing/parametrized.rst``:

.. code-block:: rst

   Parametrized Fixtures
   =====================
   
   .. autofixture:: database_type
      :show-params: true
   
   .. autofixture:: batch_size
      :show-params: true

Example 5: Complete Test Suite Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/testing/index.rst``:

.. code-block:: rst

   Testing Documentation
   =====================
   
   .. toctree::
      :maxdepth: 2
      
      fixtures
      writing-tests
      running-tests
   
   Available Fixtures
   ------------------
   
   Session-Scoped Fixtures
   ~~~~~~~~~~~~~~~~~~~~~~~
   
   .. autofixture:: conftest
      :scope: session
   
   Function-Scoped Fixtures
   ~~~~~~~~~~~~~~~~~~~~~~~~
   
   .. autofixture:: conftest
      :scope: function
   
   All Fixtures
   ~~~~~~~~~~~~
   
   .. autofixture:: conftest
      :show-scope: true
      :show-dependencies: true

Advanced Features
-----------------

Custom Docstring Parsing
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   def custom_fixture_parser(fixture):
       """Custom fixture documentation parser."""
       doc = {
           'name': fixture.__name__,
           'scope': fixture.scope,
           'params': getattr(fixture, 'params', []),
       }
       return doc
   
   autofixture_parser = custom_fixture_parser

Fixture Dependency Graph
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. autofixture-graph:: conftest
      :depth: 2

This generates a dependency graph showing fixture relationships.

Filtering Fixtures
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. autofixture:: conftest
      :exclude: _*, internal_*

Group by Module
~~~~~~~~~~~~~~~

.. code-block:: rst

   .. autofixture-modules::
      :modules: tests.unit, tests.integration

Docker Integration
------------------

Build with Fixture Docs
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     kensai-sphinx:latest \
     sphinx-build -b html /project/docs /project/docs/_build/html

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Build Test Documentation
   
   on: [push]
   
   jobs:
     docs:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Install Package and Tests
           run: |
             pip install -e .
             pip install pytest
         
         - name: Build Documentation
           run: |
             docker run --rm \
               -v $(pwd):/project \
               kensai-sphinx:latest \
               sphinx-build -b html /project/docs /project/docs/_build/html
         
         - name: Verify Fixture Docs
           run: |
             if ! grep -q "autofixture" docs/_build/html/testing/fixtures.html; then
               echo "Fixture documentation not found!"
               exit 1
             fi
         
         - name: Deploy
           uses: peaceiris/actions-gh-pages@v3
           with:
             github_token: ${{ secrets.GITHUB_TOKEN }}
             publish_dir: ./docs/_build/html

Best Practices
--------------

1. **Document Fixtures Well**
   
   Clear docstrings with examples

2. **Show Dependencies**
   
   Help users understand relationships

3. **Include Scope**
   
   Important for understanding lifecycle

4. **Provide Examples**
   
   Show how to use fixtures

5. **Keep Organized**
   
   Group by module or purpose

6. **Update Regularly**
   
   Keep docs in sync with fixtures

Troubleshooting
---------------

Fixtures Not Found
~~~~~~~~~~~~~~~~~~

**Solution:**

Check search path:

.. code-block:: python

   autofixture_search_path = ['../tests']

Verify pytest can find fixtures:

.. code-block:: bash

   pytest --fixtures

Missing Dependencies
~~~~~~~~~~~~~~~~~~~~

**Solution:**

Ensure pytest is installed:

.. code-block:: bash

   pip install pytest

Import Errors
~~~~~~~~~~~~~

**Solution:**

Add tests to Python path:

.. code-block:: python

   import sys
   sys.path.insert(0, os.path.abspath('../tests'))

Docstring Not Parsed
~~~~~~~~~~~~~~~~~~~~

**Solution:**

Check docstring style:

.. code-block:: python

   autofixture_docstring_style = 'sphinx'

Next Steps
----------

1. Configure autofixture
2. Document fixtures with docstrings
3. Create fixture documentation pages
4. Add usage examples
5. Deploy documentation


Practical Examples
------------------

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


Practical Examples
------------------

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


Practical Examples
------------------

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

Additional Resources
--------------------
- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `pytest Fixtures <https://docs.pytest.org/en/stable/fixture.html>`_
- `pytest Documentation <https://docs.pytest.org/>`_
Related Extensions
~~~~~~~~~~~~~~~~~~
- :doc:`sphinx-autodoc-example` - Python autodoc
- :doc:`pytest-doctestplus-example` - Enhanced doctest
- Pytest documentation: https://docs.pytest.org/
External Resources
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

