.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _creating-tests-for-template-calculator:

========================================
Creating tests for the calculator plugin
========================================

In this tutorial, it is explained how to write tests for a protocol, concretely for the calculator protocol writen from
scipion-em-template in the tutorial for basic plugin creation.

Associated resources
====================
Here you can find resources associated with this content:

* `Creating a basic plugin from scipion-em-template <creating-a-basic-plugin-from-template>`_.
* `Datasets presentation <https://docs.google.com/presentation/d/15Lni4PqI4L_podo_EO8Zq_XldPTjcGjaUp48JUok6xQ/edit?usp=sharing>`_
* `Writing and running tests presentation <https://docs.google.com/presentation/d/1jDoFa_78mtF1pT_SPe1sTjHKp3KUKzTmLoWG7_341nA/edit?usp=sharing>`_
* `Writing tests in Scipion3 <../writing-tests>`_.

Tutorial Data
=============
You can begin this tutorial using the result of the basic plugin creation tutorial or directly clone it. For the second
option, these are commands which has to be executed:

If you currently have installed scipion-em-template in Scipion3:

.. code-block::

    cd scipion-em-template/location
    git checkout -b course1_ex6

Else:

.. code-block::

    cd desired/location
    git clone -b course1_ex6 https://github.com/scipion-em/scipion-em-template.git
    cd scipion3/location
    ./scipion3 installp -p scipion-em-template/location --devel

Test Dataset
============

First of all, a test can use a dataset or not, depending on the test design/needs. A dataset is a predefined batch of
files that your test need to load in order to launch your protocol (e. g. a micrograph mrc file in a test of a protocol
to import micrographs) or to feed some of your protocol inputs (e. g. a coordinates file and a tomogram file).

As a quick overview of the protocol which is going to be used in this tutorial, it is a basic calculator, with three
required inputs: operation, which can be chosen from a list of four (Sum, Substract, Multiply and Divide) and two
numeric operands. Figure below shows how its GUI looks like, and the corresponding protocol code:

.. figure:: /docs/images/dev/template_practice/practice1_intro_frontend_gui_code_II.png
   :alt: intro protocol gui vs code

Thus, this protocol doesn't need any dataset, because the data required are just a string (operation) and two floats
(the operands). Nevertheless, a simply dataset has been created for these tests in order to illustrate how to work with
it if needed.

The dataset consists on a directory named devCourse, which contains a subdirectory named calculator (other
subdirectories or even other datasets can be generated to satisfy the different protocols' tests data requirements), in
which there are two text files:

* operand1: contains only one line with number 12.
* operand1: the same but with number 3.14159265359.

They will be read and parsed in the tests to generate the required operands.

Where are datasets located?
===========================

All the datasets are stored in directory **[SCIPION_HOME]/data/tests**. Existing datasets will be downloaded there.

Create a dataset
================

To begin the practice, the dataset described above must be created in the expected location.

Associate datasets to plugin tests
==================================

Datasets must be declared in file **__init__.py** located in the tests folder. Thus, the first step will consists on
create the test directory inside the plugin directory and the corresponding __init__.py file. The following figure
shows how must it be done.

.. figure:: /docs/images/dev/template_test_practice/template_test_init_dataset.png
   :alt: Test dataset in test init

Observe that the **name** and **folder** attributes have the same value. This is because in this case the dataset and
the main folder have the same name. On the other hand, attribute **files** is used to have direct access to specific
files inside the dataset via DataSet method **getFile**.

Writing the tests
=================

1. In the tests folder, create a file named **test_protocol_myCalculator.py**, and open it.

2. Create a test class named **TestProtocolMyCalculator** inheriting from **BaseTest**, in **pyworkflow.tests**.

3. Inside that class, create the set up class method, used to prepare the test execution environment. It has to be
   named **setUpClass**, and has to:

    3.1 Set up for test project (*Hint*: method **setupTestProject** in  **pyworkflow.tests** ).

    3.2 Get, from dataset **devCourse**, files **operand1** and **operand2** and parse them to get the values from
    them. They must be two float, one per file (12 and 3.14159265359, respectively).

    3.3 Store operand1 value in a class attribute named **cls.op1** and do the same for operand2 in **cls.op2**.

4. Write four tests, one for each operation offered by the calculator protocol (Sum, Substract, Multiply and Divide).
   Each test must:

    4.1  Create a calculator protocol object with the attributes operation, operand1 and operand2.

         *Hint*: To do that, check **BaseTest** method **newProtocol**.

    4.2  Execute the protocol created.

         *Hint*: use method **launchProtocol** from **BaseTest**.

    4.3  Get protocol output. It is stored in a protocol attribute named **result**.

    4.4  Validate the value obtained. To do that, create an assertion, e. g. **assertTrue**, contained, again in
    **BaseTest**. The validation has to check if the result obtained is different to the result of the operation
    specified by the test in a quantity lower or equal than a tolerance of 1e-6.

.. note:: do not hesitate to write as many auxiliary methods for code centralization.

.. note:: it is recommended to create a file constants.py inside the plugin and declare there the operation names for
          the calculator.

Executing the tests
===================

To run the tests, execute, in a terminal from the Scipion3 folder:

If you want to execute all the tests contained in your python file:

.. code-block::

    ./scipion3 tests myplugin.tests

If you want to execute a group of tests contained in that python file, and inside it, contained in a specific test
   class (there can be more than one), in this case, test_protocol_myCalculator:

.. code-block::

    ./scipion3 tests myplugin.tests.test_protocol_myCalculator

If you want to execute only one test from a file and a determined test class inside that file, e.g, testMultiply:

.. code-block::

    ./scipion3 tests myplugin.tests.test_protocol_myCalculator.testMultiply

Using the first option, result obtained should look like this.

.. figure:: /docs/images/dev/template_test_practice/tutorial_template_test_execution_result.png
   :alt: test execution result

Observe that it looks for the specified dataset. If it isn't locally present, it is downloaded from a server.

Show the test project
=====================

Each test class generates a project in Scipion3 with it's same name. In our case, it will be named
**TestProtocolMyCalculator**. All protocols created within the same class share the same project.
To check that, execute, in a terminal from Scipion3 directory:

.. code-block::

    ./scipion3 last

Which will automatically open last project executed. It should look like this:

.. figure:: /docs/images/dev/template_test_practice/tutorial_template_test_scipion_last.png
   :alt: test execution resulting project

Observe that there is a box per test. They can be directly labelled from the test using protocol method
**setObjLabel**.

Solutions
=========

To get the solutions, simply move to the branch specified below:

.. code-block::

    cd scipion-em-template/location
    git checkout -b course1_test
