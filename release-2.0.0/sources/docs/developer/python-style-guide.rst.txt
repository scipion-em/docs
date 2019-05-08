.. _python-style-guide:

==================
Python Style Guide
==================

.. contents:: Table of Contents


Readability counts. One of Guido's key insights is that code is read
much more often than it is written.  The following suggestions of Python
style is a summary of the ones in `[PEP 8] <http://www.python.org/dev/peps/pep-0008//>`_


Blank lines
===========

* Separate top-level function and class definitions with two blank
  lines.
* Method definitions inside a class are separated by a single blank
  line.
* Extra blank lines may be used (sparingly) to separate groups of
  related functions.
* Use blank lines in functions, sparingly, to indicate logical
  sections. 

Avoid using spaces
====================

Immediately inside parentheses, brackets or braces:

.. code-block:: bash

    - YES: spam(ham[1], {eggs: 2})
    - NO:  spam( ham[ 1 ], { eggs: 2 } )

Immediately before a comma, semicolon, or colon:

.. code-block:: bash

    - YES: if x == 4: print x, y; x, y = y, x
    - NO:  if x == 4 : print x , y ; x , y = y , x

More than one space around an assignment (or other) operator to align it
with another.

.. code-block:: bash

    - YES:
    x = 1
    y = 1
    long_var = 3
    - NO:
    x             = 1
    y             = 1
    long_var = 3

Around the = sign when used to indicate a keyword argument or a default
parameter value..

.. code-block:: bash

    - YES:
    def complex(real, imag=0.0):
        return magic(r=real, i=imag)
    - NO:
    def complex(real, imag = 0.0):
        return magic(r = real, i = imag)

Use spaces
============

Surround binary operators with a single space (`, +`, `=, <, >, !`, <>,
<`, >`, in, not in, is, is not, etc.) If operators with different
priorities are used, consider adding whitespace around the operators
with the lowest priority(ies)

.. code-block:: bash
    YES:
    i = i + 1
    submitted += 1
    x = x*2 - 1
    hypot2 = x*x + y*y
    c = (a+b) * (a-b)
    - NO:
    i=i+1
    submitted +=1
    x = x * 2 - 1
    hypot2 = x * x + y * y
    c = (a + b) * (a - b)


Naming conventions
=====================

* `Package or module names`:
    * module
    * module_name
    * `Classes`:
    * CamelCase (usually nouns)

* `Methods`:
    * mixedCase (usually actions)

* `Constants`:
    * UPPER_WITH_UNDERSCORE

Use library functions
=======================

Use libraries functions whenever is possible. Avoid using system
commands.

.. code-block:: bash
    - YES:
    moveFile(sourceFile, destFile)
    cleanPatern(“*.log”)
    self._getExtraPath(“a”, “b”, “file.log”)
    - NO:
    runJob(“mv”, sourceFile + “ “ + destFile)
    runJob(“rm”, “*.log”)
    os.path.join(self.workingDir, “a/b/file.log”)
