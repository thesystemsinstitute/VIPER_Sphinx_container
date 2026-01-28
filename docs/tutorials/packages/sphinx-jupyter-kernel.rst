Sphinx-Jupyter-Kernel Tutorial
===============================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-jupyter-kernel/>`_
   - :doc:`See Working Example <../../examples/sphinx-jupyter-kernel-example>`


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

Practical Examples
------------------

Example 1: Interactive Tutorial
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/tutorial.rst``:

.. code-block:: rst

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

Additional Resources
--------------------

- :doc:`nbsphinx` - Jupyter Notebook integration
- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `Jupyter Kernels <https://github.com/jupyter/jupyter/wiki/Jupyter-kernels>`_
- `IPython Documentation <https://ipython.readthedocs.io/>`_
