Sphinxemoji Tutorial
====================

.. note::
   
   **Package Resources:**
   
   - `PyPI Package <https://pypi.org/project/sphinxemoji/>`_
   - `API Documentation <../../pdoc/sphinxemoji/index.html>`_
   - `Manual <https://sphinxemoji.readthedocs.io/>`_
   - :doc:`Working Example <../../examples/sphinxemoji-example>`


.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial demonstrates how to use sphinxemoji to add emoji support to your Sphinx documentation.

What is Sphinxemoji?
--------------------

sphinxemoji is a Sphinx extension that provides:

- Emoji rendering in documentation
- Multiple emoji syntaxes
- GitHub emoji codes support
- Unicode emoji support
- Custom emoji definitions
- Inline emoji display
- Cross-platform compatibility
- No external dependencies
- Fast rendering
- Works with all themes

This makes documentation more engaging and easier to read.


The sphinxemoji extension provides emoji support using GitHub-style emoji codes and Unicode emoji characters in reStructuredText documents.

Installation
------------

sphinxemoji is already installed in this container. To verify:

.. code-block:: bash

   docker run --rm kensai-sphinx:latest python -c "import sphinxemoji; print('Installed')"

Configuration
-------------

Basic Setup
~~~~~~~~~~~

Add to your ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinxemoji.sphinxemoji',
   ]

Advanced Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   extensions = ['sphinxemoji.sphinxemoji']
   
   # Emoji configuration
   sphinxemoji_style = 'twemoji'  # twemoji, noto, or google
   
   # Custom emoji definitions
   sphinxemoji_custom = {
       'custom_emoji': '🎯',
       'company_logo': '🏢',
   }


Additional Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Basic Setup
~~~~~~~~~~~

Add to ``conf.py``:

.. code-block:: python

   extensions = [
       'sphinxemoji.sphinxemoji',
   ]

Custom Emoji
~~~~~~~~~~~~

Define custom emoji mappings:

.. code-block:: python

   sphinxemoji_custom = {
       'custom_logo': '🏢',
       'custom_icon': '⚡',
   }

Style Configuration
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Emoji rendering style
   sphinxemoji_style = 'twemoji'  # or 'unicode'

Basic Usage
-----------

GitHub Emoji Codes
~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   This is a rocket :rocket: emoji.
   
   Click the star :star: to favorite!
   
   Warning :warning: please read carefully.

Unicode Emoji
~~~~~~~~~~~~~

.. code-block:: rst

   Direct Unicode: 🚀 📚 ⭐
   
   You can also use actual emoji characters.

Inline Emoji
~~~~~~~~~~~~

.. code-block:: rst

   The process is :thumbsup: and works :ok_hand:.

   Getting Started :rocket:
   ------------------------
   
   Welcome to our project! Let's get you started quickly.
   
   Installation :package:
   ----------------------
   
   Install via pip:
   
   .. code-block:: bash
   
      pip install mypackage
   
   :heavy_check_mark: Done! You're ready to go.
   
   Quick Start :zap:
   -----------------
   
   1. :one: Import the library
   2. :two: Create a client
   3. :three: Start building!
   
   .. code-block:: python
   
      from mylib import Client
      
      client = Client()  # :tada:
      result = client.process()  # :sparkles:
   
   Common Tasks :wrench:
   ---------------------
   
   Configuration :gear:
   ~~~~~~~~~~~~~~~~~~~~
   
   Configure your settings:
   
   .. code-block:: python
   
      config = {
          'api_key': 'your-key',  # :key:
          'timeout': 30,  # :hourglass:
          'retry': True,  # :repeat:
      }
   
   Data Processing :bar_chart:
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   
   Process your data efficiently:
   
   - :arrow_forward: Load data
   - :recycle: Transform
   - :floppy_disk: Save results
   
   Troubleshooting :sos:
   ---------------------
   
   Having issues? Check these common problems:
   
   :x: **Error: Connection failed**
   
   Solution: Check your network connection :globe_with_meridians:
   
   :heavy_check_mark: **Success!**
   
   Everything working? Great! :thumbsup:

Example 2: API Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/api/reference.rst``:

.. code-block:: rst

   API Reference :books:
   =====================
   
   Core Classes :package:
   ----------------------
   
   Client :satellite:
   ~~~~~~~~~~~~~~~~~~
   
   Main API client for interacting with the service.
   
   .. code-block:: python
   
      class Client:
          """API Client :rocket:"""
          
          def connect(self):
              """Establish connection :link:"""
              pass
          
          def disconnect(self):
              """Close connection :x:"""
              pass
   
   Methods :wrench:
   ~~~~~~~~~~~~~~~~
   
   **GET Requests** :arrow_down:
   
   Fetch data from the API.
   
   **POST Requests** :arrow_up:
   
   Send data to the API.
   
   **DELETE Requests** :wastebasket:
   
   Remove resources.
   
   Status Codes :traffic_light:
   -----------------------------
   
   - :heavy_check_mark: ``200 OK`` - Success
   - :warning: ``400 Bad Request`` - Invalid input
   - :x: ``404 Not Found`` - Resource not found
   - :no_entry: ``403 Forbidden`` - Access denied
   - :fire: ``500 Server Error`` - Internal error

Example 3: Tutorial with Emoji
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/tutorial.rst``:

.. code-block:: rst

   Step-by-Step Tutorial :mortar_board:
   ====================================
   
   Prerequisites :clipboard:
   -------------------------
   
   Before starting, ensure you have:
   
   - :heavy_check_mark: Python 3.11+
   - :heavy_check_mark: pip installed
   - :heavy_check_mark: Basic Python knowledge
   
   Step 1: Installation :inbox_tray:
   ----------------------------------
   
   Install the package:
   
   .. code-block:: bash
   
      pip install mypackage
   
   :tada: Installation complete!
   
   Step 2: Configuration :gear:
   -----------------------------
   
   Create your configuration file:
   
   .. code-block:: python
   
      # config.py
      API_KEY = "your-key-here"  # :key:
      DEBUG = True  # :bug:
      LOG_LEVEL = "INFO"  # :page_facing_up:
   
   :bulb: **Tip:** Keep your API keys secure!
   
   Step 3: First Program :memo:
   -----------------------------
   
   Create your first program:
   
   .. code-block:: python
   
      from mypackage import Client
      
      # Initialize client :rocket:
      client = Client(api_key=API_KEY)
      
      # Fetch data :chart_with_upwards_trend:
      data = client.get_data()
      
      # Process results :gear:
      results = process(data)
      
      # Save output :floppy_disk:
      save(results)
      
      print("Done! :checkered_flag:")
   
   :star2: Congratulations! You've created your first program.
   
   Next Steps :footprints:
   -----------------------
   
   Where to go from here:
   
   1. :book: Read the full documentation
   2. :computer: Try advanced examples
   3. :busts_in_silhouette: Join our community
   4. :octocat: Contribute on GitHub

Example 4: Release Notes
~~~~~~~~~~~~~~~~~~~~~~~~~

``docs/changelog.rst``:

.. code-block:: rst

   Changelog :notebook:
   ====================
   
   Version 2.0.0 :rocket:
   ----------------------
   
   Released: 2024-01-15
   
   **New Features** :sparkles:
   
   - :heavy_plus_sign: Added new API endpoints
   - :zap: Improved performance by 50%
   - :lock: Enhanced security features
   - :art: New theme support
   
   **Bug Fixes** :bug:
   
   - :wrench: Fixed connection timeout issue
   - :adhesive_bandage: Corrected type annotations
   - :hammer: Resolved memory leak
   
   **Breaking Changes** :warning:
   
   - :boom: Removed deprecated ``old_method()``
   - :rotating_light: Changed default configuration
   
   **Deprecations** :skull:
   
   - :no_entry_sign: ``legacy_api()`` will be removed in v3.0
   
   Version 1.5.0 :package:
   -----------------------
   
   Released: 2023-12-01
   
   **Improvements** :chart_with_upwards_trend:
   
   - :rocket: Faster data processing
   - :books: Better documentation
   - :white_check_mark: More test coverage

Advanced Features
-----------------

Custom Emoji
~~~~~~~~~~~~

.. code-block:: python

   # conf.py
   sphinxemoji_custom = {
       'myproject': '🎯',
       'success': '✅',
       'failure': '❌',
   }

Then use in RST:

.. code-block:: rst

   :myproject: Welcome to our project!
   
   :success: Test passed
   :failure: Test failed

Emoji in Tables
~~~~~~~~~~~~~~~

.. code-block:: rst

   .. list-table:: Features
      :header-rows: 1
   
      * - Feature
        - Status
        - Notes
      * - API Access
        - :heavy_check_mark:
        - Fully supported
      * - File Upload
        - :construction:
        - In development
      * - Export
        - :x:
        - Not available

Emoji in Admonitions
~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   .. note:: :bulb:
      
      This is an important tip!
   
   .. warning:: :warning:
      
      Be careful with this setting!
   
   .. tip:: :star:
      
      Pro tip: Use keyboard shortcuts!

Emoji Lists
~~~~~~~~~~~

.. code-block:: rst

   Supported Platforms:
   
   - :apple: macOS
   - :penguin: Linux
   - :window: Windows
   
   Programming Languages:
   
   - :snake: Python
   - :gem: Ruby
   - :coffee: Java
   - :zap: JavaScript

Docker Integration
------------------

Build Documentation
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     kensai-sphinx:latest \
     sphinx-build -b html /project/docs /project/docs/_build/html

Preview with Emoji
~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm \
     -v $(pwd):/project \
     -p 8000:8000 \
     kensai-sphinx:latest \
     sh -c "sphinx-build -b html /project/docs /project/docs/_build/html && \
            python -m http.server -d /project/docs/_build/html"

CI/CD Integration
-----------------

GitHub Actions
~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Build Docs with Emoji
   
   on: [push]
   
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Build Documentation
           run: |
             docker run --rm -v $(pwd):/project \
               kensai-sphinx:latest \
               sphinx-build -b html /project/docs /project/docs/_build/html
         
         - name: Deploy
           uses: peaceiris/actions-gh-pages@v3
           with:
             github_token: ${{ secrets.GITHUB_TOKEN }}
             publish_dir: ./docs/_build/html

Best Practices
--------------

1. **Use Sparingly**
   
   Don't overuse emoji - keep it professional

2. **Be Consistent**
   
   Use same emoji for same meaning:
   
   - :heavy_check_mark: = Success
   - :x: = Error
   - :warning: = Warning

3. **Test Rendering**
   
   Check emoji display on different devices

4. **Provide Text Alternatives**
   
   Don't rely solely on emoji for meaning

5. **Consider Accessibility**
   
   Screen readers may not handle emoji well

6. **Use Common Emoji**
   
   Stick to widely-recognized emoji

Common Emoji Reference
----------------------

**Status Indicators:**

- :heavy_check_mark: ``:heavy_check_mark:`` - Success
- :x: ``:x:`` - Failure
- :warning: ``:warning:`` - Warning
- :construction: ``:construction:`` - Work in progress

**Actions:**

- :rocket: ``:rocket:`` - Launch, deploy
- :package: ``:package:`` - Package, module
- :wrench: ``:wrench:`` - Tool, utility
- :gear: ``:gear:`` - Configuration

**Documentation:**

- :book: ``:book:`` - Documentation
- :memo: ``:memo:`` - Note, text
- :page_facing_up: ``:page_facing_up:`` - Page
- :books: ``:books:`` - Library

**Development:**

- :bug: ``:bug:`` - Bug
- :sparkles: ``:sparkles:`` - New feature
- :art: ``:art:`` - Design
- :zap: ``:zap:`` - Performance

Troubleshooting
---------------

Emoji Not Rendering
~~~~~~~~~~~~~~~~~~~

**Solution:**

Check extension is enabled:

.. code-block:: python

   extensions = ['sphinxemoji.sphinxemoji']

Wrong Emoji Displayed
~~~~~~~~~~~~~~~~~~~~~

**Solution:**

Use exact emoji code from GitHub:

.. code-block:: rst

   :rocket: not :ship:

Build Errors
~~~~~~~~~~~~

**Solution:**

Escape special characters:

.. code-block:: rst

   Use \:colon\: to show literal :colon:

Next Steps
----------

1. Enable sphinxemoji extension
2. Choose appropriate emoji
3. Test rendering
4. Maintain consistency
5. Don't overuse!

Additional Resources
--------------------

- :doc:`../sphinx-basics` - Learn Sphinx fundamentals
- `GitHub Emoji Cheat Sheet <https://github.com/ikatyang/emoji-cheat-sheet>`_
- `Emojipedia <https://emojipedia.org/>`_
