Sphinx-ToJupyter Tutorial
=========================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinx-tojupyter/>`_
   - `API Documentation <../../pdoc/sphinx_tojupyter/index.html>`_
   - `Manual <https://github.com/QuantEcon/sphinx-tojupyter>`_
   - :doc:`Working Example <../../examples/sphinx-tojupyter-example>`


.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinx-tojupyter to convert your Sphinx documentation to Jupyter notebooks.

What is Sphinx-ToJupyter?
--------------------------

sphinx-tojupyter is a Sphinx extension that enables:

- Convert RST documentation to Jupyter notebooks
- Create executable documentation
- Interactive code examples
- Tutorial generation
- Workshop material creation
- Educational content
- Reproducible documentation
- Code cell extraction
- Markdown conversion
- Metadata preservation

This is perfect for creating interactive tutorials, educational materials, and executable documentation from your Sphinx docs.


The sphinx-tojupyter extension converts RST documentation into executable Jupyter notebooks, preserving code blocks, narrative text, and formatting.

Installation
------------

sphinx-tojupyter is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinx_tojupyter; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_tojupyter',
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinx_tojupyter']
   
   # Jupyter notebook configuration
   jupyter_conversion_mode = 'all'  # 'all' or 'code'
   jupyter_write_metadata = True
   jupyter_static_file_path = ['_static']
   
   # Kernel configuration
   jupyter_kernels = {
       'python3': {
           'kernelspec': {
               'display_name': 'Python 3',
               'language': 'python',
               'name': 'python3'
           },
           'language_info': {
               'name': 'python',
               'version': '3.11'
           }
       }
   }
   
   # Default kernel
   jupyter_default_kernel = 'python3'
   
   # Output options
   jupyter_execute_notebooks = False
   jupyter_execute_default_kernel = 'python3'
   jupyter_generate_html = True
   jupyter_download_nb = True
   jupyter_download_nb_image = True
   
   # Code block options
   jupyter_include_stderr = True
   jupyter_include_output = True
   jupyter_allow_html_only = False
   
   # Conversion options
   jupyter_drop_tests = True
   jupyter_drop_solutions = False
   jupyter_lang_synonyms = ['ipython', 'python']
   
   # Target formats
   jupyter_target_html = True
   jupyter_target_pdf = False
   jupyter_target_latex = False


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Basic Setup
~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinx_tojupyter',
   ]
   
   jupyter_conversion_mode = 'all'  # 'all', 'code', or 'markdown'
   jupyter_output_dir = '_jupyter'

Advanced Options
~~~~~~~~~~~~~~~~

.. code-block:: python

   jupyter_kernels = {
       'python3': {
           'kernelspec': {
               'display_name': "Python 3",
               'language': "python",
               'name': "python3"
           }
       }
   }
   
   jupyter_execute_notebooks = True
   jupyter_allow_errors = False

Cell Metadata
~~~~~~~~~~~~~

.. code-block:: python

   jupyter_cell_metadata = {
       'tags': ['remove-cell', 'hide-input'],
       'slideshow': {'slide_type': 'slide'},
   }

Basic Usage
-----------

Enable Jupyter Builder
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   sphinx-build -b jupyter docs docs/_build/jupyter

Convert Specific Pages
~~~~~~~~~~~~~~~~~~~~~~

Use the ``jupyter`` directive to mark convertible sections:

.. code-block:: rst

   .. jupyter::
      
      This content will be converted to a notebook.

Mark Code Cells
~~~~~~~~~~~~~~~

.. code-block:: rst

   .. code-block:: python
      
      # This becomes a code cell
      print("Hello, Jupyter!")

Mark Markdown Cells
~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Regular RST content becomes markdown cells.

   Python Basics Tutorial
   ======================
   
   This tutorial covers Python fundamentals.
   
   Introduction
   ------------
   
   Python is a versatile programming language.
   
   Variables and Types
   -------------------
   
   Let's start with variables:
   
   .. code-block:: python
      
      # Define variables
      name = "Alice"
      age = 30
      height = 1.65
      
      print(f"{name} is {age} years old")
   
   Python has several built-in types:
   
   - Integers: ``42``
   - Floats: ``3.14``
   - Strings: ``"Hello"``
   - Booleans: ``True`` / ``False``
   
   Lists and Loops
   ---------------
   
   Working with lists:
   
   .. code-block:: python
      
      # Create a list
      numbers = [1, 2, 3, 4, 5]
      
      # Loop through list
      for num in numbers:
          print(num * 2)
      
      # List comprehension
      squares = [x**2 for x in numbers]
      print(squares)
   
   Exercise
   --------
   
   .. admonition:: Exercise
      
      Create a list of your favorite fruits and print each one.
   
   .. code-block:: python
      
      # Your solution here
      fruits = ["apple", "banana", "orange"]
      
      for fruit in fruits:
          print(f"I like {fruit}")
   
   Functions
   ---------
   
   Defining and calling functions:
   
   .. code-block:: python
      
      def greet(name, greeting="Hello"):
          """Greet someone with a custom message."""
          return f"{greeting}, {name}!"
      
      # Call the function
      print(greet("Alice"))
      print(greet("Bob", "Hi"))
   
   Summary
   -------
   
   You've learned:
   
   - Variables and types
   - Lists and loops
   - Functions
   
   Next Steps
   ----------
   
   Continue with :doc:`python-advanced` for more topics.

Build the notebook:

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     kensai-sphinx:latest \
     sphinx-build -b jupyter /project/docs /project/docs/_build/jupyter

Example 2: Data Analysis Tutorial
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/tutorials/data-analysis.rst``:

.. code-block:: rst

   Data Analysis with Pandas
   =========================
   
   Learn data analysis using pandas and matplotlib.
   
   Setup
   -----
   
   Import required libraries:
   
   .. code-block:: python
      
      import pandas as pd
      import matplotlib.pyplot as plt
      import numpy as np
      
      # Set display options
      pd.set_option('display.max_rows', 10)
   
   Loading Data
   ------------
   
   Create a sample dataset:
   
   .. code-block:: python
      
      # Create sample data
      data = {
          'date': pd.date_range('2026-01-01', periods=100),
          'sales': np.random.randint(100, 1000, 100),
          'customers': np.random.randint(10, 100, 100),
          'region': np.random.choice(['North', 'South', 'East', 'West'], 100)
      }
      
      df = pd.DataFrame(data)
      print(df.head())
   
   Basic Analysis
   --------------
   
   Calculate summary statistics:
   
   .. code-block:: python
      
      # Summary statistics
      print(df.describe())
      
      # Group by region
      regional_sales = df.groupby('region')['sales'].agg(['sum', 'mean', 'count'])
      print(regional_sales)
   
   Visualization
   -------------
   
   Create plots:
   
   .. code-block:: python
      
      # Sales over time
      plt.figure(figsize=(10, 6))
      plt.plot(df['date'], df['sales'])
      plt.title('Sales Over Time')
      plt.xlabel('Date')
      plt.ylabel('Sales')
      plt.xticks(rotation=45)
      plt.tight_layout()
      plt.show()
      
      # Sales by region
      plt.figure(figsize=(8, 6))
      regional_sales['sum'].plot(kind='bar')
      plt.title('Total Sales by Region')
      plt.ylabel('Total Sales')
      plt.tight_layout()
      plt.show()
   
   Advanced Analysis
   -----------------
   
   Calculate moving average:
   
   .. code-block:: python
      
      # 7-day moving average
      df['sales_ma7'] = df['sales'].rolling(window=7).mean()
      
      # Plot original and moving average
      plt.figure(figsize=(12, 6))
      plt.plot(df['date'], df['sales'], label='Daily Sales', alpha=0.5)
      plt.plot(df['date'], df['sales_ma7'], label='7-Day MA', linewidth=2)
      plt.title('Sales with Moving Average')
      plt.legend()
      plt.tight_layout()
      plt.show()
   
   Exercise
   --------
   
   .. admonition:: Exercise
      
      Calculate the total customers per region and create a pie chart.
   
   .. code-block:: python
      
      # Solution
      regional_customers = df.groupby('region')['customers'].sum()
      
      plt.figure(figsize=(8, 8))
      plt.pie(regional_customers, labels=regional_customers.index, autopct='%1.1f%%')
      plt.title('Customer Distribution by Region')
      plt.show()

Example 3: Machine Learning Tutorial
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/tutorials/ml-intro.rst``:

.. code-block:: rst

   Introduction to Machine Learning
   =================================
   
   Build your first machine learning model.
   
   Import Libraries
   ----------------
   
   .. code-block:: python
      
      from sklearn.datasets import load_iris
      from sklearn.model_selection import train_test_split
      from sklearn.ensemble import RandomForestClassifier
      from sklearn.metrics import accuracy_score, classification_report
      import pandas as pd
   
   Load Dataset
   ------------
   
   .. code-block:: python
      
      # Load iris dataset
      iris = load_iris()
      X = iris.data
      y = iris.target
      
      # Create DataFrame
      df = pd.DataFrame(X, columns=iris.feature_names)
      df['target'] = y
      df['species'] = df['target'].map({
          0: 'setosa',
          1: 'versicolor',
          2: 'virginica'
      })
      
      print(df.head(10))
      print(f"\nDataset shape: {df.shape}")
   
   Split Data
   ----------
   
   .. code-block:: python
      
      # Split into train and test sets
      X_train, X_test, y_train, y_test = train_test_split(
          X, y, test_size=0.2, random_state=42
      )
      
      print(f"Training set: {X_train.shape}")
      print(f"Test set: {X_test.shape}")
   
   Train Model
   -----------
   
   .. code-block:: python
      
      # Create and train model
      model = RandomForestClassifier(n_estimators=100, random_state=42)
      model.fit(X_train, y_train)
      
      print("Model trained!")
   
   Evaluate
   --------
   
   .. code-block:: python
      
      # Make predictions
      y_pred = model.predict(X_test)
      
      # Calculate accuracy
      accuracy = accuracy_score(y_test, y_pred)
      print(f"Accuracy: {accuracy:.2%}")
      
      # Detailed report
      print("\nClassification Report:")
      print(classification_report(y_test, y_pred, 
                                  target_names=iris.target_names))
   
   Feature Importance
   ------------------
   
   .. code-block:: python
      
      # Get feature importance
      importance = pd.DataFrame({
          'feature': iris.feature_names,
          'importance': model.feature_importances_
      }).sort_values('importance', ascending=False)
      
      print(importance)

Advanced Features
-----------------

Custom Cell Metadata
~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. jupyter-execute::
      :hide-code:
      
      # This code cell will be hidden
      import setup_functions

.. code-block:: rst

   .. jupyter-execute::
      :hide-output:
      
      # Output will be hidden
      results = expensive_computation()

Multiple Kernels
~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   jupyter_kernels = {
       'python3': {...},
       'julia': {
           'kernelspec': {
               'display_name': 'Julia',
               'language': 'julia',
               'name': 'julia'
           }
       }
   }

Notebook Metadata
~~~~~~~~~~~~~~~~~

.. code-block:: python

   jupyter_metadata = {
       'language_info': {
           'name': 'python',
           'version': '3.11'
       },
       'title': 'Tutorial Notebook'
   }

Download Links
~~~~~~~~~~~~~~

Add download links in HTML output:

.. code-block:: python

   jupyter_download_nb = True
   jupyter_download_nb_image = True

Docker Integration
------------------

Convert to Notebooks
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     kensai-sphinx:latest \
     sphinx-build -b jupyter /project/docs /project/docs/_build/jupyter

Execute Notebooks
~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     kensai-sphinx:latest \
     jupyter nbconvert --execute --inplace \
       /project/docs/_build/jupyter/*.ipynb

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Build Jupyter Notebooks
   
   on:
     push:
       paths:
         - 'docs/tutorials/**'
   
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Build Notebooks
           run: |
             docker run --rm -v $(pwd):/project \
               kensai-sphinx:latest \
               sphinx-build -b jupyter /project/docs /project/docs/_build/jupyter
         
         - name: Test Notebooks
           run: |
             docker run --rm -v $(pwd):/project \
               kensai-sphinx:latest \
               sh -c "cd /project/docs/_build/jupyter && \
                      jupyter nbconvert --execute --inplace *.ipynb"
         
         - name: Upload Notebooks
           uses: actions/upload-artifact@v3
           with:
             name: notebooks
             path: docs/_build/jupyter/*.ipynb

Best Practices
--------------

1. **Keep Cells Small**
   
   One concept per code cell

2. **Add Explanations**
   
   Markdown cells between code

3. **Test Notebooks**
   
   Execute to verify they work

4. **Include Setup**
   
   Import statements at the top

5. **Use Clear Variable Names**
   
   Self-documenting code

6. **Add Exercises**
   
   Interactive learning

Common Patterns
---------------

Tutorial Template
~~~~~~~~~~~~~~~~~

.. code-block:: rst

   {{ Tutorial Title }}
   ====================
   
   Introduction
   ------------
   
   Explain the concept.
   
   Setup
   -----
   
   .. code-block:: python
      
      # Import libraries
      import library
   
   Section 1
   ---------
   
   Explanation.
   
   .. code-block:: python
      
      # Code example
      code()
   
   Exercise
   --------
   
   .. admonition:: Exercise
      
      Task description
   
   .. code-block:: python
      
      # Solution
      solution()

Troubleshooting
---------------

Conversion Fails
~~~~~~~~~~~~~~~~

**Solution:**

Check syntax:

.. code-block:: bash

   sphinx-build -b jupyter docs docs/_build/jupyter -v

Kernel Not Found
~~~~~~~~~~~~~~~~

**Solution:**

Install kernel:

.. code-block:: bash

   python -m ipykernel install --user --name=python3

Code Cells Not Executing
~~~~~~~~~~~~~~~~~~~~~~~~~

**Solution:**

Enable execution:

.. code-block:: python

   jupyter_execute_notebooks = True

Missing Images
~~~~~~~~~~~~~~

**Solution:**

Copy static files:

.. code-block:: python

   jupyter_static_file_path = ['_static']

Next Steps
----------

1. Convert existing tutorials to notebooks
2. Create interactive documentation
3. Add exercises and solutions
4. Test notebooks in CI/CD
5. Distribute notebooks to users

Additional Resources
--------------------

- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `Jupyter Documentation <https://jupyter.org/documentation>`_
- `nbsphinx <https://nbsphinx.readthedocs.io/>`_
- `Jupyter Book <https://jupyterbook.org/>`_
