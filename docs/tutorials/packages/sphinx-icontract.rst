Sphinx Icontract Tutorial
=========================

.. note::

   **Package Resources:**

   - `PyPI Package <https://pypi.org/project/sphinx-icontract/>`_
   - `API Documentation <../../pdoc/sphinx_icontract/index.html>`_
   - `Manual <https://github.com/Parquery/sphinx-icontract>`_

.. contents:: Table of Contents
   :local:
   :depth: 2

This tutorial covers sphinx-icontract, a Sphinx extension that documents icontracts on functions and classes.

What is Sphinx Icontract?
-------------------------
Sphinx Icontract extends ``sphinx.ext.autodoc`` so contract conditions (preconditions, postconditions, invariants) are shown in generated documentation.

Installation
------------

Install via pip:

.. code-block:: bash

   pip install sphinx-icontract

Configuration
-------------

Enable the extension in ``conf.py`` alongside autodoc:

.. code-block:: python

   extensions = [
       "sphinx.ext.autodoc",
       "sphinx_icontract",
   ]

Basic Usage
-----------

Document a module with autodoc; contracts appear in the output automatically.

.. code-block:: restructuredtext

   .. automodule:: mymodule
      :members:
      :undoc-members:

Contracts defined with icontract decorators will be rendered in the documentation.

Advanced Features
-----------------

- Render implications from logical expressions (e.g., ``not A or B`` as $A \Rightarrow B$).
- Include custom error messages in contract descriptions.
- Support for class invariants.
- Document preconditions, postconditions, and invariants.
- LaTeX rendering for mathematical conditions.
- Integration with type hints.

Configuration Options
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # conf.py

   extensions = [
       "sphinx.ext.autodoc",
       "sphinx_icontract",
   ]

   # icontract configuration
   icontract_include_preconditions = True
   icontract_include_postconditions = True
   icontract_include_invariants = True
   icontract_render_implications = True  # Render "not A or B" as "A ⇒ B"

Examples
--------

Basic Contract Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Python source with contracts:

.. code-block:: python

   # mymodule/math_utils.py
   import icontract

   @icontract.require(lambda x: x >= 0, "x must be non-negative")
   @icontract.ensure(lambda result: result >= 0)
   def square_root(x: float) -> float:
       """Calculate the square root of a number.

       Args:
           x: The number to take the square root of.

       Returns:
           The square root of x.
       """
       return x ** 0.5

   @icontract.require(lambda a, b: b != 0, "divisor must not be zero")
   @icontract.ensure(lambda a, b, result: result * b == a)
   def divide(a: float, b: float) -> float:
       """Divide two numbers.

       Args:
           a: The dividend.
           b: The divisor.

       Returns:
           The quotient of a divided by b.
       """
       return a / b

Document with autodoc:

.. code-block:: restructuredtext

   Math Utilities
   ==============

   .. automodule:: mymodule.math_utils
      :members:
      :undoc-members:
      :show-inheritance:

The generated documentation will show:

.. code-block:: text

   square_root(x: float) → float
       Calculate the square root of a number.

       Precondition:
           x ≥ 0 ("x must be non-negative")

       Postcondition:
           result ≥ 0

       Args:
           x: The number to take the square root of.

       Returns:
           The square root of x.

Class Invariants
~~~~~~~~~~~~~~~~

.. code-block:: python

   # mymodule/account.py
   import icontract

   @icontract.invariant(lambda self: self.balance >= 0)
   class BankAccount:
       """A bank account with guaranteed non-negative balance.

       Invariant:
           balance ≥ 0
       """

       def __init__(self, initial_balance: float = 0.0) -> None:
           """Create a new bank account.

           Args:
               initial_balance: Starting balance (must be non-negative).
           """
           icontract.require(lambda: initial_balance >= 0)
           self.balance = initial_balance

       @icontract.require(lambda self, amount: amount > 0)
       @icontract.ensure(lambda self, amount, OLD: self.balance == OLD.balance + amount)
       def deposit(self, amount: float) -> None:
           """Deposit money into the account.

           Args:
               amount: Amount to deposit (must be positive).
           """
           self.balance += amount

       @icontract.require(lambda self, amount: 0 < amount <= self.balance)
       @icontract.ensure(lambda self, amount, OLD: self.balance == OLD.balance - amount)
       def withdraw(self, amount: float) -> None:
           """Withdraw money from the account.

           Args:
               amount: Amount to withdraw (must be positive and not exceed balance).
           """
           self.balance -= amount

       @icontract.require(lambda self, other, amount: 0 < amount <= self.balance)
       @icontract.ensure(
           lambda self, other, amount, OLD:
           self.balance == OLD.balance - amount and
           other.balance == OLD.other.balance + amount
       )
       def transfer(self, other: 'BankAccount', amount: float) -> None:
           """Transfer money to another account.

           Args:
               other: Target account.
               amount: Amount to transfer.
           """
           self.withdraw(amount)
           other.deposit(amount)

Complex Preconditions
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # mymodule/validators.py
   import icontract
   import re
   from typing import List, Optional

   EMAIL_REGEX = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')

   @icontract.require(
       lambda email: EMAIL_REGEX.match(email) is not None,
       "must be a valid email address"
   )
   @icontract.require(
       lambda email: len(email) <= 254,
       "email must not exceed 254 characters"
   )
   def validate_email(email: str) -> bool:
       """Validate an email address format.

       Args:
           email: The email address to validate.

       Returns:
           True if the email is valid.
       """
       return True

   @icontract.require(lambda items: len(items) > 0, "list must not be empty")
   @icontract.require(
       lambda items: all(isinstance(x, (int, float)) for x in items),
       "all items must be numeric"
   )
   @icontract.ensure(lambda items, result: min(items) <= result <= max(items))
   def calculate_average(items: List[float]) -> float:
       """Calculate the average of a list of numbers.

       Args:
           items: Non-empty list of numbers.

       Returns:
           The arithmetic mean.
       """
       return sum(items) / len(items)

   @icontract.require(
       lambda password: len(password) >= 8,
       "password must be at least 8 characters"
   )
   @icontract.require(
       lambda password: any(c.isupper() for c in password),
       "password must contain at least one uppercase letter"
   )
   @icontract.require(
       lambda password: any(c.islower() for c in password),
       "password must contain at least one lowercase letter"
   )
   @icontract.require(
       lambda password: any(c.isdigit() for c in password),
       "password must contain at least one digit"
   )
   def validate_password(password: str) -> bool:
       """Validate password strength.

       Args:
           password: The password to validate.

       Returns:
           True if the password meets all requirements.
       """
       return True

Old Values in Postconditions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # mymodule/collections.py
   import icontract
   from typing import TypeVar, List

   T = TypeVar('T')

   @icontract.ensure(lambda lst, item, OLD: len(lst) == len(OLD.lst) + 1)
   @icontract.ensure(lambda lst, item: lst[-1] == item)
   def append_item(lst: List[T], item: T) -> None:
       """Append an item to a list.

       Postconditions:
           - List length increases by 1
           - Last element is the appended item

       Args:
           lst: The list to modify.
           item: The item to append.
       """
       lst.append(item)

   @icontract.require(lambda lst: len(lst) > 0, "list must not be empty")
   @icontract.ensure(lambda lst, OLD, result: len(lst) == len(OLD.lst) - 1)
   @icontract.ensure(lambda result, OLD: result == OLD.lst[-1])
   def pop_item(lst: List[T]) -> T:
       """Remove and return the last item from a list.

       Args:
           lst: The list to modify (must be non-empty).

       Returns:
           The removed item.
       """
       return lst.pop()

Integration with Type Hints
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # mymodule/typed_utils.py
   import icontract
   from typing import Optional, Union
   from dataclasses import dataclass

   @dataclass
   @icontract.invariant(lambda self: self.min_value <= self.max_value)
   class Range:
       """A numeric range with guaranteed valid bounds.

       Invariant: min_value ≤ max_value
       """
       min_value: float
       max_value: float

       @icontract.require(lambda self, value: self.min_value <= value <= self.max_value)
       def contains(self, value: float) -> bool:
           """Check if value is within range.

           Args:
               value: Value to check (must be within bounds).

           Returns:
               Always True (precondition guarantees it).
           """
           return True

       @icontract.ensure(lambda self, result: result >= 0)
       def size(self) -> float:
           """Get the size of the range.

           Returns:
               The difference between max and min values.
           """
           return self.max_value - self.min_value

Complete Documentation Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: restructuredtext

   API Reference
   =============

   Math Utilities
   --------------

   .. automodule:: mymodule.math_utils
      :members:
      :undoc-members:
      :show-inheritance:

   Account Management
   ------------------

   .. automodule:: mymodule.account
      :members:
      :undoc-members:
      :show-inheritance:
      :special-members: __init__

   Validators
   ----------

   .. automodule:: mymodule.validators
      :members:
      :undoc-members:

   Contract Legend
   ---------------

   The following symbols are used in contract documentation:

   - **Precondition**: Conditions that must be true before calling the function
   - **Postcondition**: Conditions guaranteed to be true after the function returns
   - **Invariant**: Conditions that must always be true for a class instance
   - **OLD**: Refers to the value before the function was called

Additional Resources
--------------------

- `Manual <https://github.com/Parquery/sphinx-icontract>`_
- `PyPI <https://pypi.org/project/sphinx-icontract/>`_
- `API Documentation <../../pdoc/sphinx_icontract/index.html>`_
