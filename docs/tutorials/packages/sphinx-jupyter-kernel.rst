Sphinx-Jupyter-Kernel Tutorial
===============================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-jupyter-kernel/>`_
   - `API Documentation <../../pdoc/sphinx_jupyter_kernel/index.html>`_
   - `Manual <https://github.com/Armienn/sphinx-jupyter-kernel>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinx-jupyter-kernel to execute code examples using Jupyter kernels during documentation builds.

What is Sphinx-Jupyter-Kernel?
-------------------------------
sphinx-jupyter-kernel is a Sphinx extension that provides:

- Execute code with Jupyter kernels
- Multiple language support
- Kernel management
- Code cell execution
- Output capture
- Interactive examples
- Kernel restart control
- Session persistence
- Variable sharing between cells
- Support for IPython magics

This allows you to run code examples in Python, R, Julia, and other languages during documentation builds.

The sphinx-jupyter-kernel extension allows you to execute code blocks in your Sphinx documentation using Jupyter kernels, enabling live code execution and output display for multiple programming languages.


Installation
------------

sphinx-jupyter-kernel is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinx_jupyter_kernel; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_jupyter_kernel',
   ]
   
   # Default kernel
   jupyter_kernel_name = 'python3'

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinx_jupyter_kernel']
   
   # Kernel configuration
   jupyter_kernel_name = 'python3'
   jupyter_execute_kwargs = {
       'timeout': 60,
       'allow_errors': False,
   }
   
   # Kernel restart options
   jupyter_restart_kernel_between_files = False
   jupyter_restart_kernel_between_cells = False
   
   # Output configuration
   jupyter_execute_default_kernel = 'python3'
   jupyter_execute_notebooks = 'auto'  # auto, always, never, cache

Basic Usage
-----------

Execute Python Code
~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
      
      import numpy as np
      import matplotlib.pyplot as plt
      
      x = np.linspace(0, 2*np.pi, 100)
      y = np.sin(x)
      
      plt.plot(x, y)
      plt.title('Sine Wave')
      plt.show()

Hide Code
~~~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
      :hide-code:
      
      # Setup code (hidden)
      import matplotlib.pyplot as plt
      plt.style.use('seaborn')

Hide Output
~~~~~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
      :hide-output:
      
      # This runs but output is hidden
      setup_database()

   Python Tutorial
   ===============
   
   Introduction
   ------------
   
   Let's start with basic Python.
   
   Variables and Types
   -------------------
   
   .. jupyter-execute::
      
      # Basic variables
      x = 10
      y = 20
      result = x + y
      print(f"Result: {result}")
   
   You can use the variables in subsequent cells:
   
   .. jupyter-execute::
      
      # Variables persist between cells
      result * 2
   
   Data Structures
   ---------------
   
   .. jupyter-execute::
      
      # Lists
      numbers = [1, 2, 3, 4, 5]
      
      # List comprehension
      squared = [n**2 for n in numbers]
      print(squared)
   
   .. jupyter-execute::
      
      # Dictionaries
      person = {
          'name': 'John',
          'age': 30,
          'city': 'New York'
      }
      
      for key, value in person.items():
          print(f"{key}: {value}")
   
   Functions
   ---------
   
   .. jupyter-execute::
      
      def factorial(n):
          """Calculate factorial of n."""
          if n <= 1:
              return 1
          return n * factorial(n - 1)
      
      # Test the function
      for i in range(1, 6):
          print(f"{i}! = {factorial(i)}")

Example 2: Data Visualization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/visualization.rst``:

.. code-block:: rst

   Data Visualization
   ==================
   
   Setup
   -----
   
   First, import required libraries:
   
   .. jupyter-execute::
      :hide-output:
      
      import numpy as np
      import matplotlib.pyplot as plt
      import pandas as pd
      import seaborn as sns
      
      # Set style
      sns.set_style('whitegrid')
      plt.rcParams['figure.figsize'] = (10, 6)
   
   Basic Plots
   -----------
   
   Line Plot
   ~~~~~~~~~
   
   .. jupyter-execute::
      
      x = np.linspace(0, 10, 100)
      y1 = np.sin(x)
      y2 = np.cos(x)
      
      plt.plot(x, y1, label='sin(x)')
      plt.plot(x, y2, label='cos(x)')
      plt.xlabel('x')
      plt.ylabel('y')
      plt.title('Trigonometric Functions')
      plt.legend()
      plt.grid(True)
      plt.show()
   
   Scatter Plot
   ~~~~~~~~~~~~
   
   .. jupyter-execute::
      
      # Generate random data
      np.random.seed(42)
      x = np.random.randn(100)
      y = 2*x + np.random.randn(100)
      
      plt.scatter(x, y, alpha=0.5)
      plt.xlabel('X')
      plt.ylabel('Y')
      plt.title('Scatter Plot')
      plt.show()
   
   Advanced Visualizations
   -----------------------
   
   Heatmap
   ~~~~~~~
   
   .. jupyter-execute::
      
      # Create correlation matrix
      data = pd.DataFrame({
          'A': np.random.randn(100),
          'B': np.random.randn(100),
          'C': np.random.randn(100),
          'D': np.random.randn(100),
      })
      
      # Calculate correlations
      corr = data.corr()
      
      # Plot heatmap
      sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)
      plt.title('Correlation Heatmap')
      plt.show()

Example 3: Machine Learning Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/ml-example.rst``:

.. code-block:: rst

   Machine Learning Example
   ========================
   
   Data Preparation
   ----------------
   
   .. jupyter-execute::
      
      from sklearn.datasets import load_iris
      from sklearn.model_selection import train_test_split
      from sklearn.ensemble import RandomForestClassifier
      from sklearn.metrics import classification_report, confusion_matrix
      import pandas as pd
      
      # Load data
      iris = load_iris()
      X, y = iris.data, iris.target
      
      # Split data
      X_train, X_test, y_train, y_test = train_test_split(
          X, y, test_size=0.3, random_state=42
      )
      
      print(f"Training samples: {len(X_train)}")
      print(f"Test samples: {len(X_test)}")
   
   Model Training
   --------------
   
   .. jupyter-execute::
      
      # Train model
      model = RandomForestClassifier(n_estimators=100, random_state=42)
      model.fit(X_train, y_train)
      
      # Evaluate
      train_score = model.score(X_train, y_train)
      test_score = model.score(X_test, y_test)
      
      print(f"Training accuracy: {train_score:.3f}")
      print(f"Test accuracy: {test_score:.3f}")
   
   Predictions
   -----------
   
   .. jupyter-execute::
      
      # Make predictions
      y_pred = model.predict(X_test)
      
      # Classification report
      print(classification_report(y_test, y_pred, 
                                    target_names=iris.target_names))
   
   Confusion Matrix
   ----------------
   
   .. jupyter-execute::
      
      # Confusion matrix
      cm = confusion_matrix(y_test, y_pred)
      
      # Plot
      sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                  xticklabels=iris.target_names,
                  yticklabels=iris.target_names)
      plt.title('Confusion Matrix')
      plt.ylabel('True Label')
      plt.xlabel('Predicted Label')
      plt.show()

Example 4: API Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/api-examples.rst``:

.. code-block:: rst

   API Examples
   ============
   
   Setup Client
   ------------
   
   .. jupyter-execute::
      :hide-output:
      
      from mylib import Client
      
      # Initialize (use demo mode for docs)
      client = Client(api_key='demo', demo_mode=True)
   
   Fetch Data
   ----------
   
   .. jupyter-execute::
      
      # Get users
      users = client.get_users(limit=5)
      
      # Display
      import pandas as pd
      df = pd.DataFrame(users)
      print(df)
   
   Create Resource
   ---------------
   
   .. jupyter-execute::
      
      # Create new user
      new_user = client.create_user(
          name="John Doe",
          email="john@example.com"
      )
      
      print(f"Created user: {new_user['id']}")

Advanced Features
-----------------

Custom Kernel
~~~~~~~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
      :kernel: ir
      
      # R code
      data <- c(1, 2, 3, 4, 5)
      mean(data)

Error Handling
~~~~~~~~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
      :raises: ValueError
      
      # This will raise an error
      raise ValueError("Example error")

Linenos
~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
      :linenos:
      
      def fibonacci(n):
          if n <= 1:
              return n
          return fibonacci(n-1) + fibonacci(n-2)
      
      print([fibonacci(i) for i in range(10)])

Emphasize Lines
~~~~~~~~~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
      :emphasize-lines: 3,5
      
      import numpy as np
      
      data = np.random.randn(100)  # Emphasized
      
      mean = data.mean()           # Emphasized
      std = data.std()

Session Management
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   
   # Restart kernel between files
   jupyter_restart_kernel_between_files = True
   
   # Restart between cells
   jupyter_restart_kernel_between_cells = False

Docker Integration
------------------

Build with Jupyter Kernel
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     kensai-sphinx:latest \
     sphinx-build -b html /project/docs /project/docs/_build/html

Install Additional Kernels
~~~~~~~~~~~~~~~~~~~~~~~~~~~

``Dockerfile``:

.. code-block:: dockerfile

   FROM kensai-sphinx:latest
   
   # Install R kernel
   RUN apk add --no-cache R R-dev
   RUN R -e "install.packages('IRkernel')"
   RUN R -e "IRkernel::installspec(user = FALSE)"
   
   # Install Julia kernel
   RUN apk add --no-cache julia
   RUN julia -e 'using Pkg; Pkg.add("IJulia")'

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Build Executable Docs
   
   on: [push]
   
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Setup Python
           uses: actions/setup-python@v4
           with:
             python-version: '3.11'
         
         - name: Install Dependencies
           run: |
             pip install sphinx sphinx-jupyter-kernel ipykernel
             pip install -r requirements.txt
         
         - name: Build Documentation
           run: |
             sphinx-build -b html docs docs/_build/html
         
         - name: Deploy
           uses: peaceiris/actions-gh-pages@v3
           with:
             github_token: ${{ secrets.GITHUB_TOKEN }}
             publish_dir: ./docs/_build/html

Best Practices
--------------

1. **Keep Examples Simple**
   
   Focus on demonstrating one concept

2. **Use Demo Mode**
   
   Don't require real API keys

3. **Set Timeouts**
   
   Prevent long-running cells

4. **Handle Errors**
   
   Use ``:raises:`` for expected errors

5. **Organize Code**
   
   Use hidden setup cells

6. **Test Locally**
   
   Ensure all cells execute

Troubleshooting
---------------

Kernel Not Found
~~~~~~~~~~~~~~~~

**Solution:**

Install and register kernel:

.. code-block:: bash

   pip install ipykernel
   python -m ipykernel install --user

Execution Timeout
~~~~~~~~~~~~~~~~~

**Solution:**

Increase timeout:

.. code-block:: python

   jupyter_execute_kwargs = {
       'timeout': 120,
   }

Import Errors
~~~~~~~~~~~~~

**Solution:**

Install required packages:

.. code-block:: bash

   pip install -r requirements.txt

Memory Issues
~~~~~~~~~~~~~

**Solution:**

Restart kernel between files:

.. code-block:: python

   jupyter_restart_kernel_between_files = True

Variables Not Persisting
~~~~~~~~~~~~~~~~~~~~~~~~~

**Solution:**

Ensure kernel isn't restarting between cells:

.. code-block:: python

   jupyter_restart_kernel_between_cells = False

Next Steps
----------

1. Install jupyter kernel
2. Add jupyter-execute directives
3. Write executable examples
4. Test documentation build
5. Deploy interactive docs


Practical Examples
------------------

Basic Configuration
-------------------

Setup
~~~~~

.. code-block:: python

   # conf.py
   extensions = [
       'sphinx_jupyter_kernel',
   ]
   
   # Specify kernel
   jupyter_kernel_name = 'python3'

Kernel Selection
~~~~~~~~~~~~~~~~

.. code-block:: python

   # Available kernels
   jupyter_kernel_name = 'python3'   # Python
   # jupyter_kernel_name = 'ir'      # R
   # jupyter_kernel_name = 'julia'   # Julia
   # jupyter_kernel_name = 'bash'    # Bash

Code Block Execution
--------------------

Python Code
~~~~~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
   
      import numpy as np
      
      x = np.array([1, 2, 3, 4, 5])
      print(f"Sum: {x.sum()}")
      print(f"Mean: {x.mean()}")

Hidden Input
~~~~~~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
      :hide-code:
   
      import matplotlib.pyplot as plt
      
      plt.plot([1, 2, 3], [1, 4, 9])
      plt.title('Simple Plot')
      plt.show()

Hidden Output
~~~~~~~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
      :hide-output:
   
      # This code runs but output is hidden
      result = expensive_computation()

Code with Options
-----------------

Line Numbers
~~~~~~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
      :linenos:
   
      def fibonacci(n):
          if n <= 1:
              return n
          return fibonacci(n-1) + fibonacci(n-2)
      
      print([fibonacci(i) for i in range(10)])

Emphasized Lines
~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
      :emphasize-lines: 3,5
   
      import pandas as pd
      
      df = pd.DataFrame({'A': [1, 2, 3]})
      
      result = df.sum()
      print(result)

Caption
~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
      :caption: Data Processing Example
   
      data = [1, 2, 3, 4, 5]
      processed = [x * 2 for x in data]
      print(processed)

Multiple Kernels
----------------

Per-Block Kernel
~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
      :kernel: python3
   
      print("Python code")

   .. jupyter-execute::
      :kernel: bash
   
      echo "Bash command"

Kernel Configuration
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   jupyter_execute_kernels = {
       'python3': {
           'kernel_name': 'python3',
           'config': {'InlineBackend.figure_format': 'svg'}
       },
       'julia': {
           'kernel_name': 'julia-1.9'
       }
   }

Persistent State
----------------

Shared State
~~~~~~~~~~~~

Code blocks share kernel state:

.. code-block:: rst

   .. jupyter-execute::
   
      # First block
      x = 10
      y = 20

   .. jupyter-execute::
   
      # Second block - uses variables from first block
      z = x + y
      print(f"Result: {z}")

Reset Kernel
~~~~~~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
      :restart:
   
      # This runs in a fresh kernel
      x = 100

Plotting and Visualization
---------------------------

Matplotlib
~~~~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
   
      import matplotlib.pyplot as plt
      import numpy as np
      
      x = np.linspace(0, 2*np.pi, 100)
      y = np.sin(x)
      
      plt.figure(figsize=(10, 4))
      plt.plot(x, y)
      plt.title('Sine Wave')
      plt.xlabel('x')
      plt.ylabel('sin(x)')
      plt.grid(True)
      plt.show()

Interactive Plots
~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
   
      import plotly.graph_objects as go
      
      fig = go.Figure(data=go.Scatter(
          x=[1, 2, 3, 4],
          y=[10, 11, 12, 13]
      ))
      fig.show()

Seaborn
~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
   
      import seaborn as sns
      import pandas as pd
      
      df = pd.DataFrame({
          'x': range(10),
          'y': [i**2 for i in range(10)]
      })
      
      sns.scatterplot(data=df, x='x', y='y')

Data Science Examples
---------------------

Pandas DataFrames
~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
   
      import pandas as pd
      
      df = pd.DataFrame({
          'Name': ['Alice', 'Bob', 'Charlie'],
          'Age': [25, 30, 35],
          'City': ['NYC', 'LA', 'Chicago']
      })
      
      df

NumPy Arrays
~~~~~~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
   
      import numpy as np
      
      # Create array
      arr = np.random.rand(3, 3)
      print("Random array:")
      print(arr)
      
      # Statistics
      print(f"\nMean: {arr.mean():.2f}")
      print(f"Std: {arr.std():.2f}")

Machine Learning
~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
   
      from sklearn.datasets import load_iris
      from sklearn.tree import DecisionTreeClassifier
      
      # Load data
      iris = load_iris()
      X, y = iris.data, iris.target
      
      # Train model
      clf = DecisionTreeClassifier()
      clf.fit(X[:100], y[:100])
      
      # Predict
      predictions = clf.predict(X[100:105])
      print(f"Predictions: {predictions}")
      print(f"Actual: {y[100:105]}")

Error Handling
--------------

Allow Errors
~~~~~~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
      :raises:
   
      # This code will error but won't stop the build
      result = 1 / 0

Expected Exceptions
~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
   
      try:
          value = undefined_variable
      except NameError as e:
          print(f"Caught error: {e}")

Advanced Configuration
----------------------

Execution Timeout
~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   jupyter_execute_kwargs = {
       'timeout': 60,  # seconds
   }

Figure Format
~~~~~~~~~~~~~

.. code-block:: python

   # Output format for plots
   jupyter_execute_default_kernel = {
       'config': {
           'InlineBackend.figure_format': 'svg'  # or 'png', 'pdf'
       }
   }

Working Directory
~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Execute in specific directory
   jupyter_execute_kwargs = {
       'cwd': './code_examples',
   }

Custom Templates
~~~~~~~~~~~~~~~~

.. code-block:: python

   # Custom cell templates
   jupyter_execute_cell_template = """
   .. code-block:: {{ language }}
      {% if emphasize_lines %}
      :emphasize-lines: {{ emphasize_lines }}
      {% endif %}
      
      {{ code }}
   """

Practical Examples
------------------

Tutorial Documentation
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Getting Started
   ===============
   
   First, import the library:
   
   .. jupyter-execute::
   
      import mypackage
   
   Create a client instance:
   
   .. jupyter-execute::
   
      client = mypackage.Client()
      client.connect()
   
   Now you can use it:
   
   .. jupyter-execute::
   
      result = client.process_data([1, 2, 3])
      print(result)

API Examples
~~~~~~~~~~~~

.. code-block:: rst

   API Reference
   =============
   
   process_data(data, method='auto')
   ----------------------------------
   
   Process input data using specified method.
   
   **Example:**
   
   .. jupyter-execute::
   
      from mypackage import process_data
      
      data = [1, 2, 3, 4, 5]
      result = process_data(data, method='fast')
      print(result)

Cookbook
~~~~~~~~

.. code-block:: rst

   Recipes
   =======
   
   Data Loading
   ------------
   
   .. jupyter-execute::
   
      import pandas as pd
      
      df = pd.read_csv('data.csv')
      print(df.head())
   
   Data Cleaning
   -------------
   
   .. jupyter-execute::
   
      # Remove duplicates
      df_clean = df.drop_duplicates()
      
      # Handle missing values
      df_clean = df_clean.fillna(0)
      
      print(f"Cleaned: {len(df_clean)} rows")

Best Practices
--------------

Code Organization
~~~~~~~~~~~~~~~~~

1. Import statements in first code block
2. Build up state progressively
3. Use meaningful variable names
4. Include comments for clarity

Output Management
~~~~~~~~~~~~~~~~~

1. Hide setup code with ``:hide-code:``
2. Keep output concise
3. Use print statements strategically
4. Clear large outputs when not needed

Performance
~~~~~~~~~~~

1. Set appropriate timeouts
2. Cache expensive computations
3. Use small datasets for examples
4. Consider using ``:hide-output:`` for slow code

Integration Tips
----------------

With nbsphinx
~~~~~~~~~~~~~

.. code-block:: python

   # Use both extensions
   extensions = [
       'nbsphinx',
       'sphinx_jupyter_kernel',
   ]

With autodoc
~~~~~~~~~~~~

.. code-block:: rst

   .. autofunction:: mypackage.process
   
   **Example usage:**
   
   .. jupyter-execute::
   
      from mypackage import process
      process([1, 2, 3])

With MyST
~~~~~~~~~

.. code-block:: python

   # conf.py
   extensions = [
       'myst_parser',
       'sphinx_jupyter_kernel',
   ]

Troubleshooting
---------------

Kernel Not Found
~~~~~~~~~~~~~~~~

.. code-block:: bash

   # List available kernels
   jupyter kernelspec list
   
   # Install kernel
   python -m ipykernel install --user --name mykernel

Import Errors
~~~~~~~~~~~~~

.. code-block:: python

   # Ensure packages are installed in kernel environment
   jupyter_execute_kwargs = {
       'kernel_setup': [
           'pip install numpy pandas matplotlib'
       ]
   }

Memory Issues
~~~~~~~~~~~~~

.. code-block:: python

   # Limit memory usage
   jupyter_execute_kwargs = {
       'timeout': 30,
       'shutdown_kernel': 'always',
   }


Practical Examples
------------------

Basic Configuration
-------------------

Setup
~~~~~

.. code-block:: python

   # conf.py
   extensions = [
       'sphinx_jupyter_kernel',
   ]
   
   # Specify kernel
   jupyter_kernel_name = 'python3'

Kernel Selection
~~~~~~~~~~~~~~~~

.. code-block:: python

   # Available kernels
   jupyter_kernel_name = 'python3'   # Python
   # jupyter_kernel_name = 'ir'      # R
   # jupyter_kernel_name = 'julia'   # Julia
   # jupyter_kernel_name = 'bash'    # Bash

Code Block Execution
--------------------

Python Code
~~~~~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
   
      import numpy as np
      
      x = np.array([1, 2, 3, 4, 5])
      print(f"Sum: {x.sum()}")
      print(f"Mean: {x.mean()}")

Hidden Input
~~~~~~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
      :hide-code:
   
      import matplotlib.pyplot as plt
      
      plt.plot([1, 2, 3], [1, 4, 9])
      plt.title('Simple Plot')
      plt.show()

Hidden Output
~~~~~~~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
      :hide-output:
   
      # This code runs but output is hidden
      result = expensive_computation()

Code with Options
-----------------

Line Numbers
~~~~~~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
      :linenos:
   
      def fibonacci(n):
          if n <= 1:
              return n
          return fibonacci(n-1) + fibonacci(n-2)
      
      print([fibonacci(i) for i in range(10)])

Emphasized Lines
~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
      :emphasize-lines: 3,5
   
      import pandas as pd
      
      df = pd.DataFrame({'A': [1, 2, 3]})
      
      result = df.sum()
      print(result)

Caption
~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
      :caption: Data Processing Example
   
      data = [1, 2, 3, 4, 5]
      processed = [x * 2 for x in data]
      print(processed)

Multiple Kernels
----------------

Per-Block Kernel
~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
      :kernel: python3
   
      print("Python code")

   .. jupyter-execute::
      :kernel: bash
   
      echo "Bash command"

Kernel Configuration
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   jupyter_execute_kernels = {
       'python3': {
           'kernel_name': 'python3',
           'config': {'InlineBackend.figure_format': 'svg'}
       },
       'julia': {
           'kernel_name': 'julia-1.9'
       }
   }

Persistent State
----------------

Shared State
~~~~~~~~~~~~

Code blocks share kernel state:

.. code-block:: rst

   .. jupyter-execute::
   
      # First block
      x = 10
      y = 20

   .. jupyter-execute::
   
      # Second block - uses variables from first block
      z = x + y
      print(f"Result: {z}")

Reset Kernel
~~~~~~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
      :restart:
   
      # This runs in a fresh kernel
      x = 100

Plotting and Visualization
---------------------------

Matplotlib
~~~~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
   
      import matplotlib.pyplot as plt
      import numpy as np
      
      x = np.linspace(0, 2*np.pi, 100)
      y = np.sin(x)
      
      plt.figure(figsize=(10, 4))
      plt.plot(x, y)
      plt.title('Sine Wave')
      plt.xlabel('x')
      plt.ylabel('sin(x)')
      plt.grid(True)
      plt.show()

Interactive Plots
~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
   
      import plotly.graph_objects as go
      
      fig = go.Figure(data=go.Scatter(
          x=[1, 2, 3, 4],
          y=[10, 11, 12, 13]
      ))
      fig.show()

Seaborn
~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
   
      import seaborn as sns
      import pandas as pd
      
      df = pd.DataFrame({
          'x': range(10),
          'y': [i**2 for i in range(10)]
      })
      
      sns.scatterplot(data=df, x='x', y='y')

Data Science Examples
---------------------

Pandas DataFrames
~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
   
      import pandas as pd
      
      df = pd.DataFrame({
          'Name': ['Alice', 'Bob', 'Charlie'],
          'Age': [25, 30, 35],
          'City': ['NYC', 'LA', 'Chicago']
      })
      
      df

NumPy Arrays
~~~~~~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
   
      import numpy as np
      
      # Create array
      arr = np.random.rand(3, 3)
      print("Random array:")
      print(arr)
      
      # Statistics
      print(f"\nMean: {arr.mean():.2f}")
      print(f"Std: {arr.std():.2f}")

Machine Learning
~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
   
      from sklearn.datasets import load_iris
      from sklearn.tree import DecisionTreeClassifier
      
      # Load data
      iris = load_iris()
      X, y = iris.data, iris.target
      
      # Train model
      clf = DecisionTreeClassifier()
      clf.fit(X[:100], y[:100])
      
      # Predict
      predictions = clf.predict(X[100:105])
      print(f"Predictions: {predictions}")
      print(f"Actual: {y[100:105]}")

Error Handling
--------------

Allow Errors
~~~~~~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
      :raises:
   
      # This code will error but won't stop the build
      result = 1 / 0

Expected Exceptions
~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
   
      try:
          value = undefined_variable
      except NameError as e:
          print(f"Caught error: {e}")

Advanced Configuration
----------------------

Execution Timeout
~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   jupyter_execute_kwargs = {
       'timeout': 60,  # seconds
   }

Figure Format
~~~~~~~~~~~~~

.. code-block:: python

   # Output format for plots
   jupyter_execute_default_kernel = {
       'config': {
           'InlineBackend.figure_format': 'svg'  # or 'png', 'pdf'
       }
   }

Working Directory
~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Execute in specific directory
   jupyter_execute_kwargs = {
       'cwd': './code_examples',
   }

Custom Templates
~~~~~~~~~~~~~~~~

.. code-block:: python

   # Custom cell templates
   jupyter_execute_cell_template = """
   .. code-block:: {{ language }}
      {% if emphasize_lines %}
      :emphasize-lines: {{ emphasize_lines }}
      {% endif %}
      
      {{ code }}
   """

Practical Examples
------------------

Tutorial Documentation
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Getting Started
   ===============
   
   First, import the library:
   
   .. jupyter-execute::
   
      import mypackage
   
   Create a client instance:
   
   .. jupyter-execute::
   
      client = mypackage.Client()
      client.connect()
   
   Now you can use it:
   
   .. jupyter-execute::
   
      result = client.process_data([1, 2, 3])
      print(result)

API Examples
~~~~~~~~~~~~

.. code-block:: rst

   API Reference
   =============
   
   process_data(data, method='auto')
   ----------------------------------
   
   Process input data using specified method.
   
   **Example:**
   
   .. jupyter-execute::
   
      from mypackage import process_data
      
      data = [1, 2, 3, 4, 5]
      result = process_data(data, method='fast')
      print(result)

Cookbook
~~~~~~~~

.. code-block:: rst

   Recipes
   =======
   
   Data Loading
   ------------
   
   .. jupyter-execute::
   
      import pandas as pd
      
      df = pd.read_csv('data.csv')
      print(df.head())
   
   Data Cleaning
   -------------
   
   .. jupyter-execute::
   
      # Remove duplicates
      df_clean = df.drop_duplicates()
      
      # Handle missing values
      df_clean = df_clean.fillna(0)
      
      print(f"Cleaned: {len(df_clean)} rows")

Best Practices
--------------

Code Organization
~~~~~~~~~~~~~~~~~

1. Import statements in first code block
2. Build up state progressively
3. Use meaningful variable names
4. Include comments for clarity

Output Management
~~~~~~~~~~~~~~~~~

1. Hide setup code with ``:hide-code:``
2. Keep output concise
3. Use print statements strategically
4. Clear large outputs when not needed

Performance
~~~~~~~~~~~

1. Set appropriate timeouts
2. Cache expensive computations
3. Use small datasets for examples
4. Consider using ``:hide-output:`` for slow code

Integration Tips
----------------

With nbsphinx
~~~~~~~~~~~~~

.. code-block:: python

   # Use both extensions
   extensions = [
       'nbsphinx',
       'sphinx_jupyter_kernel',
   ]

With autodoc
~~~~~~~~~~~~

.. code-block:: rst

   .. autofunction:: mypackage.process
   
   **Example usage:**
   
   .. jupyter-execute::
   
      from mypackage import process
      process([1, 2, 3])

With MyST
~~~~~~~~~

.. code-block:: python

   # conf.py
   extensions = [
       'myst_parser',
       'sphinx_jupyter_kernel',
   ]

Troubleshooting
---------------

Kernel Not Found
~~~~~~~~~~~~~~~~

.. code-block:: bash

   # List available kernels
   jupyter kernelspec list
   
   # Install kernel
   python -m ipykernel install --user --name mykernel

Import Errors
~~~~~~~~~~~~~

.. code-block:: python

   # Ensure packages are installed in kernel environment
   jupyter_execute_kwargs = {
       'kernel_setup': [
           'pip install numpy pandas matplotlib'
       ]
   }

Memory Issues
~~~~~~~~~~~~~

.. code-block:: python

   # Limit memory usage
   jupyter_execute_kwargs = {
       'timeout': 30,
       'shutdown_kernel': 'always',
   }


Practical Examples
------------------

Basic Configuration
-------------------

Setup
~~~~~

.. code-block:: python

   # conf.py
   extensions = [
       'sphinx_jupyter_kernel',
   ]
   
   # Specify kernel
   jupyter_kernel_name = 'python3'

Kernel Selection
~~~~~~~~~~~~~~~~

.. code-block:: python

   # Available kernels
   jupyter_kernel_name = 'python3'   # Python
   # jupyter_kernel_name = 'ir'      # R
   # jupyter_kernel_name = 'julia'   # Julia
   # jupyter_kernel_name = 'bash'    # Bash

Code Block Execution
--------------------

Python Code
~~~~~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
   
      import numpy as np
      
      x = np.array([1, 2, 3, 4, 5])
      print(f"Sum: {x.sum()}")
      print(f"Mean: {x.mean()}")

Hidden Input
~~~~~~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
      :hide-code:
   
      import matplotlib.pyplot as plt
      
      plt.plot([1, 2, 3], [1, 4, 9])
      plt.title('Simple Plot')
      plt.show()

Hidden Output
~~~~~~~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
      :hide-output:
   
      # This code runs but output is hidden
      result = expensive_computation()

Code with Options
-----------------

Line Numbers
~~~~~~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
      :linenos:
   
      def fibonacci(n):
          if n <= 1:
              return n
          return fibonacci(n-1) + fibonacci(n-2)
      
      print([fibonacci(i) for i in range(10)])

Emphasized Lines
~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
      :emphasize-lines: 3,5
   
      import pandas as pd
      
      df = pd.DataFrame({'A': [1, 2, 3]})
      
      result = df.sum()
      print(result)

Caption
~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
      :caption: Data Processing Example
   
      data = [1, 2, 3, 4, 5]
      processed = [x * 2 for x in data]
      print(processed)

Multiple Kernels
----------------

Per-Block Kernel
~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
      :kernel: python3
   
      print("Python code")

   .. jupyter-execute::
      :kernel: bash
   
      echo "Bash command"

Kernel Configuration
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   jupyter_execute_kernels = {
       'python3': {
           'kernel_name': 'python3',
           'config': {'InlineBackend.figure_format': 'svg'}
       },
       'julia': {
           'kernel_name': 'julia-1.9'
       }
   }

Persistent State
----------------

Shared State
~~~~~~~~~~~~

Code blocks share kernel state:

.. code-block:: rst

   .. jupyter-execute::
   
      # First block
      x = 10
      y = 20

   .. jupyter-execute::
   
      # Second block - uses variables from first block
      z = x + y
      print(f"Result: {z}")

Reset Kernel
~~~~~~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
      :restart:
   
      # This runs in a fresh kernel
      x = 100

Plotting and Visualization
---------------------------

Matplotlib
~~~~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
   
      import matplotlib.pyplot as plt
      import numpy as np
      
      x = np.linspace(0, 2*np.pi, 100)
      y = np.sin(x)
      
      plt.figure(figsize=(10, 4))
      plt.plot(x, y)
      plt.title('Sine Wave')
      plt.xlabel('x')
      plt.ylabel('sin(x)')
      plt.grid(True)
      plt.show()

Interactive Plots
~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
   
      import plotly.graph_objects as go
      
      fig = go.Figure(data=go.Scatter(
          x=[1, 2, 3, 4],
          y=[10, 11, 12, 13]
      ))
      fig.show()

Seaborn
~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
   
      import seaborn as sns
      import pandas as pd
      
      df = pd.DataFrame({
          'x': range(10),
          'y': [i**2 for i in range(10)]
      })
      
      sns.scatterplot(data=df, x='x', y='y')

Data Science Examples
---------------------

Pandas DataFrames
~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
   
      import pandas as pd
      
      df = pd.DataFrame({
          'Name': ['Alice', 'Bob', 'Charlie'],
          'Age': [25, 30, 35],
          'City': ['NYC', 'LA', 'Chicago']
      })
      
      df

NumPy Arrays
~~~~~~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
   
      import numpy as np
      
      # Create array
      arr = np.random.rand(3, 3)
      print("Random array:")
      print(arr)
      
      # Statistics
      print(f"\nMean: {arr.mean():.2f}")
      print(f"Std: {arr.std():.2f}")

Machine Learning
~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
   
      from sklearn.datasets import load_iris
      from sklearn.tree import DecisionTreeClassifier
      
      # Load data
      iris = load_iris()
      X, y = iris.data, iris.target
      
      # Train model
      clf = DecisionTreeClassifier()
      clf.fit(X[:100], y[:100])
      
      # Predict
      predictions = clf.predict(X[100:105])
      print(f"Predictions: {predictions}")
      print(f"Actual: {y[100:105]}")

Error Handling
--------------

Allow Errors
~~~~~~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
      :raises:
   
      # This code will error but won't stop the build
      result = 1 / 0

Expected Exceptions
~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
   
      try:
          value = undefined_variable
      except NameError as e:
          print(f"Caught error: {e}")

Advanced Configuration
----------------------

Execution Timeout
~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   jupyter_execute_kwargs = {
       'timeout': 60,  # seconds
   }

Figure Format
~~~~~~~~~~~~~

.. code-block:: python

   # Output format for plots
   jupyter_execute_default_kernel = {
       'config': {
           'InlineBackend.figure_format': 'svg'  # or 'png', 'pdf'
       }
   }

Working Directory
~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Execute in specific directory
   jupyter_execute_kwargs = {
       'cwd': './code_examples',
   }

Custom Templates
~~~~~~~~~~~~~~~~

.. code-block:: python

   # Custom cell templates
   jupyter_execute_cell_template = """
   .. code-block:: {{ language }}
      {% if emphasize_lines %}
      :emphasize-lines: {{ emphasize_lines }}
      {% endif %}
      
      {{ code }}
   """

Practical Examples
------------------

Tutorial Documentation
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Getting Started
   ===============
   
   First, import the library:
   
   .. jupyter-execute::
   
      import mypackage
   
   Create a client instance:
   
   .. jupyter-execute::
   
      client = mypackage.Client()
      client.connect()
   
   Now you can use it:
   
   .. jupyter-execute::
   
      result = client.process_data([1, 2, 3])
      print(result)

API Examples
~~~~~~~~~~~~

.. code-block:: rst

   API Reference
   =============
   
   process_data(data, method='auto')
   ----------------------------------
   
   Process input data using specified method.
   
   **Example:**
   
   .. jupyter-execute::
   
      from mypackage import process_data
      
      data = [1, 2, 3, 4, 5]
      result = process_data(data, method='fast')
      print(result)

Cookbook
~~~~~~~~

.. code-block:: rst

   Recipes
   =======
   
   Data Loading
   ------------
   
   .. jupyter-execute::
   
      import pandas as pd
      
      df = pd.read_csv('data.csv')
      print(df.head())
   
   Data Cleaning
   -------------
   
   .. jupyter-execute::
   
      # Remove duplicates
      df_clean = df.drop_duplicates()
      
      # Handle missing values
      df_clean = df_clean.fillna(0)
      
      print(f"Cleaned: {len(df_clean)} rows")

Best Practices
--------------

Code Organization
~~~~~~~~~~~~~~~~~

1. Import statements in first code block
2. Build up state progressively
3. Use meaningful variable names
4. Include comments for clarity

Output Management
~~~~~~~~~~~~~~~~~

1. Hide setup code with ``:hide-code:``
2. Keep output concise
3. Use print statements strategically
4. Clear large outputs when not needed

Performance
~~~~~~~~~~~

1. Set appropriate timeouts
2. Cache expensive computations
3. Use small datasets for examples
4. Consider using ``:hide-output:`` for slow code

Integration Tips
----------------

With nbsphinx
~~~~~~~~~~~~~

.. code-block:: python

   # Use both extensions
   extensions = [
       'nbsphinx',
       'sphinx_jupyter_kernel',
   ]

With autodoc
~~~~~~~~~~~~

.. code-block:: rst

   .. autofunction:: mypackage.process
   
   **Example usage:**
   
   .. jupyter-execute::
   
      from mypackage import process
      process([1, 2, 3])

With MyST
~~~~~~~~~

.. code-block:: python

   # conf.py
   extensions = [
       'myst_parser',
       'sphinx_jupyter_kernel',
   ]

Troubleshooting
---------------

Kernel Not Found
~~~~~~~~~~~~~~~~

.. code-block:: bash

   # List available kernels
   jupyter kernelspec list
   
   # Install kernel
   python -m ipykernel install --user --name mykernel

Import Errors
~~~~~~~~~~~~~

.. code-block:: python

   # Ensure packages are installed in kernel environment
   jupyter_execute_kwargs = {
       'kernel_setup': [
           'pip install numpy pandas matplotlib'
       ]
   }

Memory Issues
~~~~~~~~~~~~~

.. code-block:: python

   # Limit memory usage
   jupyter_execute_kwargs = {
       'timeout': 30,
       'shutdown_kernel': 'always',
   }

Additional Resources
--------------------
- :doc:`nbsphinx` - Jupyter Notebook integration
- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `Jupyter Kernels <https://github.com/jupyter/jupyter/wiki/Jupyter-kernels>`_
- `IPython Documentation <https://ipython.readthedocs.io/>`_
- :doc:`../tutorials/packages/sphinx-jupyter-kernel` - Complete tutorial
- :doc:`nbsphinx-example` - nbsphinx extension
- GitHub repository: https://github.com/jupyter/jupyter-sphinx

