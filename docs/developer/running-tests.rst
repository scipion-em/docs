.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _running-tests:

==================
Running Tests
==================

Scipion discovers all tests using the following command:

::

    ./scipion3 tests

This command creates a list with Scipion's own tests as well as the tests of
the installed plugins:

::

     ......
        >>>> cistem
     scipion3 tests cistem.tests.test_protocols_cistem_movies
       scipion3 tests cistem.tests.test_protocols_cistem_movies.TestUnblur
     scipion3 tests cistem.tests.test_protocols_cistem
       scipion3 tests cistem.tests.test_protocols_cistem.TestRefine2D
       scipion3 tests cistem.tests.test_protocols_cistem.TestFindParticles
       scipion3 tests cistem.tests.test_protocols_cistem.TestCtffind4
    >>>> relion
     scipion3 tests relion.tests.test_workflow_relion3
       scipion3 tests relion.tests.test_workflow_relion3.TestWorkflowRelion3Betagal
     scipion3 tests relion.tests.test_protocols_relion3
       scipion3 tests relion.tests.test_protocols_relion3.TestRelion31ImportParticles
       scipion3 tests relion.tests.test_protocols_relion3.Relion3TestMultiBody
       scipion3 tests relion.tests.test_protocols_relion3.Relion3TestMotioncor
       scipion3 tests relion.tests.test_protocols_relion3.Relion3TestAssignOptics
     .....

This command shows all tests with the following order:
`<module_name>.<tests_folder>.<test_file>.<test_class_derived_from_BaseTest>`

To list the tests filtering by a pattern we can use the following command:

::

    ./scipion3 tests --grep <pattern>

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


To execute an Scipion test just type:

::

    $ ./scipion3 tests <test>

`test` case from string identifier (module, class or callable)

for example:

::
    ./scipion3 tests cryosparc2.tests.test_utils
    ./scipion3 tests cryosparc2.tests.test_utils.TestUtils
    ./scipion3 tests cryosparc2.test.test_utils.TestUtils.testSamplingRateConvertion


the last script produces the following output:

::

        Running tests....
        [ RUN   OK ] TestUtils.testSamplingRateConvertion (0.000 secs)

        [==========] run 1 tests (0.000 secs)
        [  PASSED  ] 1 tests


The other commands that can be used are shown below:

::

    usage: ./scipion3 test [-h] [--run | --show] [--pattern PATTERN]
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


We can also combine the parameters of this command to run more
than one test, for example:

::

   ./scipion3 test --grep cryosparc --run

and all the tests that match the pattern "cryosparc" will be
executed automatically.
