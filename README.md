# python-client-and-lib
Example of a .py that runs on its own for unit testing, but is also imported by
a client .py script.

This is a silly example. None of the code does anything useful.

client_code.py
--------------
*Concept:* client_code.py represents the script using the library.

*This example:* the client calls *addlib.add5( )*.

addlib.py
---------
*Concept:* addlib.py represents some script you want to use as a library.

*This example:* the library defines *add5( )*.

The library is meant to be imported.
But before it was a working a library, it had to be developed/tested.
This meant running the script on its own to see its unit test results.
I wrote the unit tests to drive development of the silly "add5()" function.
    
These are the unit test results you will see if you run *addlib.py*:
--------------------------------------------------------------------
  ```txt
  add5() adds 5 to a number.
  Tests:
  ------
  ..ss
  ----------------------------------------------------------------------
  Ran 4 tests in 0.000s

  OK (skipped=2)
  ```

