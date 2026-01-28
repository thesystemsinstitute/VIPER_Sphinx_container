Sphinx-Jupyter-Kernel Example
==============================

This page demonstrates the **sphinx-jupyter-kernel** extension for executing code blocks using Jupyter kernels.

.. contents:: Contents
   :local:
   :depth: 2

Overview
--------

The sphinx-jupyter-kernel extension allows you to execute code blocks in your Sphinx documentation using Jupyter kernels, enabling live code execution and output display for multiple programming languages.

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

See Also
--------

- :doc:`../tutorials/packages/sphinx-jupyter-kernel` - Complete tutorial
- :doc:`nbsphinx-example` - nbsphinx extension
- GitHub repository: https://github.com/jupyter/jupyter-sphinx
