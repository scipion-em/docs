.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _running-tests:

==================
Running Tests
==================

There are many test runners available for Python. The one built into the Python
standard library is called `unittest`. The principles of unittest are easily
portable to other frameworks. **BaseTest** is a Scipion class that inherits
from that library which contains tools for testing our code and it is precisely
the one used for such purposes.


Basic example
-------------

Here is a short script (`named test_utils.py`) to test a methods that calculate a
new sampling rate of a set of particles that has been downsampled:

.. code-block:: python

        import unittest

        class TestUtils(unittest.TestCase):

            def testSamplingRateConvertion(self):

                sr = calculateNewSamplingRate((2, 2, 2), 4, (4, 4, 4))
                self.assertEqual(sr, 8, "Wrong sampling rate conversion 1")

             def calculateNewSamplingRate(newDims, previousSR, previousDims):
                   pX = previousDims[0]
                   nX = newDims[0]
                   return previousSR*pX/nX

        if __name__ == '__main__':
            unittest.main()

Note that the class TestUtils derived from `unittest.TestCase`. if we use
`BaseTest` class, the code will be this:

.. code-block:: python

        from pyworkflow.tests import BaseTest

        class TestUtils(BaseTest):
             ....................

        if __name__ == '__main__':
            unittest.main()

The final block shows a simple way to run the tests. The unittest module can be
used from the command line to run tests from modules, classes or even individual
test methods:

.. code-block:: bash

        python -m unittest test_utils
        python -m unittest test_utils.TestUtils
        python -m unittest test_utils.TestUtils.testSamplingRateConvertion

When run from the command line, the above script produces an output that looks
like this:

.. code-block:: bash

        ...
        ----------------------------------------------------------------------
        Ran 1 tests in 0.000s

        OK


Running tests with Scipion
--------------------------

Scipion discovers all tests using the following command:

::

    ./scipion3 test


The other commands that can be used are shown below:

::

    usage: ./scipion3 tests [-h] [--run | --show] [--pattern PATTERN]
                            [--grep GREP [GREP ...]] [--skip SKIP [SKIP ...]]
                            [--log [LOG]] [--mode {modules,classes,onlyclasses,all}]
                            [TEST [TEST ...]]

    Run or show the selected tests. Tests can be selected by giving the "case", or
    by giving the paths and file pattern to use for searching them.

    positional arguments:
      TEST                  test case from string identifier (module, class or
                            callable)

    optional arguments:
      -h, --help            show this help message and exit
      --run                 run the selected tests
      --show                show available tests
      --pattern PATTERN     pattern for the files that will be used in the tests
      --grep GREP [GREP ...]
                            only show/run tests containing the provided words
      --skip SKIP [SKIP ...]
                            skip tests that contains these words
      --log [LOG]           Generate logs files with the output of each test.
      --mode {modules,classes,onlyclasses,all}
                            how much detail to give in show mode

example:

::

    ./scipion3 test --grep cryosparc

     scipion3 tests cryosparc2.tests.test_utils
       scipion3 tests cryosparc2.tests.test_utils.TestUtils
     scipion3 tests cryosparc2.tests.test_protocols_cryosparc2
       scipion3 tests cryosparc2.tests.test_protocols_cryosparc2.TestCryosparcSharppening
       scipion3 tests cryosparc2.tests.test_protocols_cryosparc2.TestCryosparcParticlesSubtract
       scipion3 tests cryosparc2.tests.test_protocols_cryosparc2.TestCryosparcNonUniformRefine3D
       scipion3 tests cryosparc2.tests.test_protocols_cryosparc2.TestCryosparcLocalRefine
       scipion3 tests cryosparc2.tests.test_protocols_cryosparc2.TestCryosparcLocalCtfRefinement
       scipion3 tests cryosparc2.tests.test_protocols_cryosparc2.TestCryosparcGlobalCtfRefinement
       scipion3 tests cryosparc2.tests.test_protocols_cryosparc2.TestCryosparcClassify2D
       scipion3 tests cryosparc2.tests.test_protocols_cryosparc2.TestCryosparc3DRefinement
       scipion3 tests cryosparc2.tests.test_protocols_cryosparc2.TestCryosparc3DInitialModel
       scipion3 tests cryosparc2.tests.test_protocols_cryosparc2.TestCryosparc3DClassification

This command shows all tests that matching with the pattern "cryosparc" with the
following order: <module_name>.<tests_folder>.<test_file>.<test_class_derived_from_BaseTest>

To execute an Scipion test just type:

::

    $ ./scipion3 tests cryosparc2.tests.test_utils.TestUtils

and above script produces the following output:

::

        Running tests....
        [ RUN   OK ] TestUtils.testSamplingRateConvertion (0.000 secs)

        [==========] run 1 tests (0.000 secs)
        [  PASSED  ] 1 tests


and all the defined tests within the class TestUtils will be run automatically.


