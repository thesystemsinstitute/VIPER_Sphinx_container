Sphinxemoji Example
===================

This page demonstrates the **sphinxemoji** extension for adding emoji support to Sphinx documentation.

.. contents:: Contents
   :local:
   :depth: 2


Basic Emoji Usage
-----------------

Text Role
~~~~~~~~~

Inline emoji using the ``:emoji:`` role:

- I :emoji:`heart` Python!
- :emoji:`rocket` Launch successful!
- :emoji:`warning` Be careful!
- :emoji:`check_mark` Task completed
- :emoji:`fire` Hot feature!

Common Emoji
~~~~~~~~~~~~

Emotions and People
^^^^^^^^^^^^^^^^^^^

- :emoji:`smile` Happy
- :emoji:`laughing` Funny
- :emoji:`heart_eyes` Love it
- :emoji:`thinking_face` Thinking
- :emoji:`tada` Celebration

Objects and Symbols
^^^^^^^^^^^^^^^^^^^

- :emoji:`computer` Coding
- :emoji:`book` Documentation
- :emoji:`bulb` Idea
- :emoji:`lock` Security
- :emoji:`key` Authentication

Nature and Weather
^^^^^^^^^^^^^^^^^^

- :emoji:`sunny` Clear day
- :emoji:`cloud` Cloudy
- :emoji:`zap` Lightning
- :emoji:`snowflake` Winter
- :emoji:`seedling` Growth

Technical Emoji
---------------

Programming
~~~~~~~~~~~

- :emoji:`bug` Bug report
- :emoji:`wrench` Configuration
- :emoji:`gear` Settings
- :emoji:`package` Package
- :emoji:`inbox_tray` Download
- :emoji:`outbox_tray` Upload

Version Control
~~~~~~~~~~~~~~~

- :emoji:`git` Git
- :emoji:`octocat` GitHub
- :emoji:`branch` Branch
- :emoji:`tag` Release tag
- :emoji:`merge` Merge

Development Status
~~~~~~~~~~~~~~~~~~

- :emoji:`construction` Work in progress
- :emoji:`white_check_mark` Done
- :emoji:`x` Failed
- :emoji:`hourglass` Pending
- :emoji:`recycle` Refactoring

Documentation Emoji
-------------------

Admonitions
~~~~~~~~~~~

.. note::
   :emoji:`information_source` This is informational content

.. warning::
   :emoji:`warning` This action is potentially dangerous

.. danger::
   :emoji:`no_entry` Do not proceed without reading

.. tip::
   :emoji:`bulb` Pro tip: Use emoji sparingly for best effect

Headers with Emoji
~~~~~~~~~~~~~~~~~~

Section Example :emoji:`books`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Content with contextual emoji in the header.

Installation :emoji:`package`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Step-by-step installation guide.

Configuration :emoji:`wrench`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Configuration options and settings.

Code Examples with Emoji
-------------------------

Python Code :emoji:`snake`
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python
   :caption: example.py

   # :emoji:`bug` Debug function
   def debug_info():
       """Print debug information :emoji:`information_source`"""
       print("Debug mode enabled")
   
   # :emoji:`rocket` Main function
   def main():
       """Launch the application :emoji:`fire`"""
       print("Starting...")

Lists with Emoji
----------------

Feature List
~~~~~~~~~~~~

- :emoji:`check_mark` Fast performance
- :emoji:`check_mark` Easy to use
- :emoji:`check_mark` Well documented
- :emoji:`x` Not production ready
- :emoji:`construction` Work in progress

Step-by-Step Guide
~~~~~~~~~~~~~~~~~~

1. :emoji:`one` Clone the repository
2. :emoji:`two` Install dependencies
3. :emoji:`three` Configure settings
4. :emoji:`four` Run the application
5. :emoji:`five` Deploy to production

Tables with Emoji
-----------------

Status Table
~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 30 20 50

   * - Feature
     - Status
     - Notes
   * - Authentication
     - :emoji:`white_check_mark`
     - Fully implemented
   * - Caching
     - :emoji:`construction`
     - In development
   * - Testing
     - :emoji:`x`
     - Not started
   * - Documentation
     - :emoji:`books`
     - Ongoing

Priority Indicators
~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 40 20 40

   * - Task
     - Priority
     - Owner
   * - Fix critical bug
     - :emoji:`fire` High
     - John
   * - Update docs
     - :emoji:`arrow_up` Medium
     - Jane
   * - Code review
     - :emoji:`arrow_down` Low
     - Team

Configuration
-------------

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

Practical Examples
------------------

Release Notes
~~~~~~~~~~~~~

Version 2.0.0 :emoji:`rocket`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**New Features** :emoji:`sparkles`

- :emoji:`zap` Improved performance
- :emoji:`art` Better UI/UX
- :emoji:`globe_with_meridians` i18n support

**Bug Fixes** :emoji:`bug`

- :emoji:`wrench` Fixed configuration issues
- :emoji:`lock` Security patches

**Breaking Changes** :emoji:`boom`

- API endpoint changes
- Database schema updates

API Documentation
~~~~~~~~~~~~~~~~~

Authentication :emoji:`lock`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   # :emoji:`key` Get authentication token
   def get_token(username, password):
       """
       Authenticate user and return token
       
       :emoji:`warning` Store tokens securely!
       """
       pass

Error Handling :emoji:`x`
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   try:
       process_data()
   except ValueError:
       # :emoji:`bug` Log the error
       logger.error("Invalid data")
   except Exception:
       # :emoji:`fire` Critical error
       logger.critical("Unknown error")

Best Practices
--------------

When to Use Emoji
~~~~~~~~~~~~~~~~~

**Good Uses** :emoji:`thumbsup`

- Status indicators
- Quick visual cues
- Section markers
- Feature lists

**Avoid** :emoji:`thumbsdown`

- Overuse in body text
- Professional/formal docs
- Accessibility concerns
- Critical information

Accessibility
~~~~~~~~~~~~~

.. note::
   :emoji:`wheelchair` Always provide text alternatives for emoji:
   
   - Use descriptive text alongside emoji
   - Don't rely solely on emoji for meaning
   - Consider screen reader compatibility

See Also
--------

- :doc:`../tutorials/packages/sphinxemoji` - Complete tutorial
- GitHub repository: https://github.com/sphinx-contrib/emojicodes
- Emoji cheat sheet: https://www.webfx.com/tools/emoji-cheat-sheet/
