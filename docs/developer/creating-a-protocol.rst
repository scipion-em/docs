.. _creating a protocol:

===================
Creating a protocol
===================


In Scipion, we define ``Protocol`` as a processing task that involves the
execution of several steps. Each step can execute Python code or call
external programs to perform specific sub-tasks. When designing a new
protocol, we should provide a clear definition of the protocol inputs
and outputs. The developer of a protocol also needs to take care of
necessary conversions between Scipion-objects to the program files and
parameters. Moreover, the results of the protocol execution should be
registered back as output in the form of Scipion-objects.

We are going to use a 2D classification protocol (maximum likelihood in
Xmipp) as an example to illustrate the development of a new protocol.
This small guide will cover the basics of creating a new protocol. In each
section we will provide links to more detailed information when needed.

Protocol Definition
===================

Overview
--------

The first step when developing a protocol is to select the protocol
class name. In this case it is ``XmippProtML2D``, following the
convention that all Xmipp protocol names will start by ``XmippProt`` (we
recommend a similar approach to name protocols from other EM plugins).
In this case our protocol descends from a base class ``ProtClassify2D``
which reflects the operation that this protocol performs.

The Python documentation string following the protocol class line will
serve as help for users. It is very useful to provide a short but
descriptive help message that will quickly give users a sense of
the protocol's function. If the protocol defines a ``_label`` class
property (``ml2d`` in this example), it will be used as a label to display the protocol in
menus. If not provided, the protocol class name will be used, but this
name is probably less meaningful to final users.

The protocol initialization function should receive the
keyword-arguments ( ```*kwargs`` ). The arguments should also be passed
to the base class initialization method. This function is the right
place to make variable initialization or similar things.

.. code-block:: python

    class XmippProtML2D(ProtClassify2D):
        """
        Perform (multi-reference) 2D-alignment using
        a maximum-likelihood ( *ML* ) target function.
        """
        _label = 'ml2d'

        def __init__(self, **kwargs):
            pass

        #--------------- DEFINE param functions ---------------

        def _defineParams(self, form):
            pass

        #--------------- INSERT steps functions ----------------

        def _insertAllSteps(self):
            pass

        #--------------- STEPS functions -----------------------

        def convertInputStep(self):
            pass

        def runMLStep(self, params):
            pass

        def createOutputStep(self):
            pass

        #--------------- INFO functions -------------------------

        def _validate(self):
            return []

        def _citations(self):
            return []

        def _summary(self):
            return []

        def _methods(self):
            return []

        #--------------- UTILS functions -------------------------

        ...


The code above illustrates the skeleton of a protocol class. There are
five main parts of the code:

* **Parameter definition**: Defines all the parameters that
  will appear in the GUI and that will be attributes of the protocol instance.
* **Steps list**: Prepares the list of steps that will be executed in
  order to complete the protocol.
* **Steps functions**: Contains the code that willbe executed (Python code
  or call to external programs)
* **Validation and info functions**: Decorates the protocol class by providing
  parameter validation and some useful information to the user.
* **Other utils functions**: Varies from protocol to
  protocol; it will contain helper functions to be used throughout the
  protocol code.

In the following sections we are going to more thoroughly explain each of these
parts in order to develop a fully functional protocol.


Defining Input Parameters
-------------------------

In the ``_defineParams(form)`` method, the protocol's form will be
populated with the input parameters (which also will be rendered
graphically). All these parameters will be available as the protocol's
attribute that can be used in the protocol steps.

All the parameters should have a unique name inside the protocol and
a type. There are two groups of parameters:

* **Simple parameters**: Basic input parameter types.
    * ``__StringParam__``: A basic string input (a textbox in the GUI)
    * ``__FloatParam__``: Floating point input value (a textbox in the GUI, but
      should have a floating point format)
    * ``__IntParam__``: An integer (a textbox in the GUI, but should have
      an integer format)
    * ``__BooleanParam__``: A boolean value, or True or False (a Yes/No
      question in the GUI)
    * ``__EnumParam__``: Also an integer input, but with a small number
      of possible choices (a combobox or a list in the GUI)
*  **Complex parameters**:
    * ``__PointerParam__``: Selects objects from the database
      (a text box with a search button in the GUI)
    * ``__RelationParam__``: similar to ``__PointerParam__``, but will select
      relationships instead of objects (mainly used for CTF browsing)
    * ``__ProtocolClassParam__``: similar to ``__PointerParam__``, but will select
      protocol classes (used for Workflows, under development)

Parameters can be added with the
``form.addParam(paramName, paramClass, **kwargs)`` method. ``paramClass``
should be one of the classes listed above and the ```*kwargs`` are passed to
the constructor. Valid options in the ```*kwargs`` dictionary are:

* **default** : Default parameter value
* **condition** : A string representing an expression (whose values are
  substituted later) that determines whether the parameter appears.
* **label** : A label message that will be displayed in the GUI
* **help** : Usually a more extended help message that will pop up after
  clicking on a help icon.
* **choices** : A list of strings with the display values for the combobox
  ( Only valid for ``__EnumParam__``)
* **display** : can be ``_EnumParam.DISPLAY__LIST__`` or
  ``_EnumParam.DISPLAY__COMBO__``, and defined the preferred display mode for
  GUI.( Only valid for`` __EnumParam__``)
* **pointerClass** : Class of the objects that will be
  selected from the database ( Only valid for ``__PointerParam__``)
* **pointerCondition** : A string expression to filter the
  selected objects from the database (such as ``aligned=True``, Only valid
  for ``__PointerParam__``)
* **allowsNull** : A boolean. If true, this parameter is not required (
  Only valid for ``__PointerParam__``)

To improve the organization of the input parameters, they can be grouped
into sections, groups, or lines.

* **Section**: The function :meth:`addSection<pyworkflow.protocol.params.Form.addSection>` will create
  a new section (that will be visualized as a new tab in the GUI), and all
  further calls to ``form.addParam`` will add parameters to that section.
* **Group**: The function :meth:`addGroup<pyworkflow.protocol.params.Form.addGroup>` will return a
  :class:`Group<pyworkflow.protocol.params.Group>` object that can also add parameters to it. The group will be
  displayed as a labeled frame in the GUI.
* **Line**: Another way of grouping is through :meth:`addLine(lineLabel)<pyworkflow.protocol.params.Form.addLine>`,
  which will return a :class:`Line<pyworkflow.protocol.params.Line>` object that can
  also contain other parameters. It will simply display those parameters in the same row.

.. code-block:: python

    def _defineParams(self, form):
        form.addSection(label='Params')
        group = form.addGroup('Input')
        group.addParam('inputParticles', PointerParam,
                       pointerClass='SetOfParticles',
                       label="Input particles", important=True,
                       help='Select the input images from the project.')
        group.addParam('doGenerateReferences', BooleanParam, default=True,
                      label='Generate references?',
                      help='If you set to *No*, you should provide references images'
                           'If *Yes*, the default generation is done by averaging'
                           'subsets of the input images. (less bias introduced)')
        group.addParam('numberOfReferences', IntParam, default=3,
                      condition='doGenerateReferences',
                      label='Number of references:',
                      help='Number of references to be generated.')
        group.addParam('inputReferences', PointerParam,
                      condition='not doGenerateReferences',
                      label="Reference image(s)",
                      pointerClass='SetOfParticles',
                      help='Image(s) that will serve as initial 2D references')

        form.addParam('doMlf', BooleanParam, default=False, important=True,
                      label='Use MLF2D instead of ML2D?')

        group = form.addGroup('ML-Fourier', condition='doMlf')
        ...
        form.addParallelSection(threads=2, mpi=4)


The line `form.addParallelSection(threads=2, mpi=4)` specifies the
number of threads and MPI that will be used by default in this protocol.
If not set, both thread and MPI are equal to 1. Setting thread or MPI
with a 0 value here will mean that it is not possible to use it and
will be hidden in the GUI. More about the parallelization of protocols
can be found in :doc:`Parallelization<protocol-parallelization`.

The above definition will generate a desktop GUI as shown in the
following figure:

.. figure:: /docs/images/guis/ml2d_form.png


Defining Steps
--------------

Another important function is ``_insertAllSteps``, in which the steps
that will be executed are defined. This function is only invoked before
a protocol starts to run and the following actions take place:

* The method ``protocol.run()`` is called
* The ``protocol._insertAllSteps()`` is called and a list of steps is populated (depending on the current
  parameters selection)
* The steps list is compared with previous steps lists in the database (if exists a previous execution) and,
* If in RESUME mode, it will try to continue from the last step that was completed
  successfully. (In RESTART mode it will start from the first step and
  output directory is cleaned)

It is important to note that no computing tasks should be performed in the ``_insertAllSteps``
function this should be done in the steps; see next section). This place is only to *DEFINE*
what needs to be done, not actually to do it.

The ``Step`` class represents the smallest execution unit that composes a
``Protocol``. The most used sub-classes of ``Step`` are:

* **FunctionStep** : Inserted using the function
  ``protocol._insertFunctionStep``. Any accessible function can be
  inserted; it could be a function of the protocol or an external
  function. The changes in the parameters passed to the function are used
  to detect step changes, so even when it may not be necessary to pass
  certain parameters, it is useful to pass them for detecting changes.
* **RunJobStep** : this step wraps a call to an external program and
  builds the necessary command line arguments. It can be inserted using
  ``protocol._insertRunJobStep``

In our example protocol, the ``_insertAllSteps`` function looks like:

.. code-block:: python

    def _insertAllSteps(self):
        self._insertFunctionStep('convertInputStep',
                                 self.inputParticles.get().getObjId())
        program = self._getMLProgram()
        params = self._getMLParams()
        self._insertRunJobStep(program, params)
        self._insertFunctionStep('createOutputStep')


This is a relatively simple case (but also a common one) in which only three
steps are inserted: ``convertInputStep``, ``runJobStep``,
``createOutputStep``. In this case, the steps run in the same order
in which they were inserted, but it is also possible to define a more complex
dependency graph between steps that can be executed in parallel (through
threads or MPI). You can read more about defining steps to be executed
in parallel in :doc:`Parallelization<parallelization>`.

Even when a protocol runs its steps without parallelization, one
particular step can take advantage of a multiprocessor and use MPI or
threads in a particular program command line.

Execution
=========

Converting Inputs
-----------------

It is common that one of the first steps in a protocol is
``convertInputStep``* whose main task is to convert from input Scipion
objects to files with the format that is appropriate for running a
particular program. In our example, we should convert the input
``SetOfParticles`` object into the metadata star file that is required
by all Xmipp programs that operates on particles. In this classification
protocol, it is also possible to provide a set of reference images.
This is also taken into account in the ``convertInputStep`` function and
also writes metadata for the references if needed.

.. code-block:: python

    def convertInputStep(self, inputId):
        """ Write the input images as a Xmipp metadata file. """
        writeSetOfParticles(self.inputParticles.get(),
                            self._getFileName('input_particles'))
        # If input references, also convert to xmipp metadata
        if not self.doGenerateReferences:
            writeSetOfParticles(self.inputReferences.get(),
                                self._getFileName('input_references'))


The ``writeSetOfParticles`` function iterates over each individual image
in the input ``SetOfParticles`` and adds a line to a valid STAR file
using the Xmipp MetaData class in Python. By the same logic, any other
file format could be generated when writting a ``convertInputStep``
function. Read more about iterating over a ``SetOfParticles`` and
querying its attributes in :doc:`Using Sets <using-sets>`.

Executing Programs
------------------

The second step function in this example is a ``runJobStep``. In this
case the program is ``xmipp_ml_align2d`` (or mlf in the Fourier case). The
command line argument for calling the program is prepared in the
``_getMLParams`` function.

.. code-block:: python

    def _getMLParams(self):
        """ Mainly prepare the command line for call ml(f)2d program"""
        params = ' -i %s --oroot %s' % (self._getFileName('input_particles'),
                                        self._getOroot())
        if self.doGenerateReferences:
            params += ' --nref %d' % self.numberOfReferences.get()
            self.inputReferences.set(None)
        else:
            params += ' --ref %s' % self._getFileName('input_references')
            self.numberOfReferences.set(self.inputReferences.get().getSize())

        ...

        if self.doMirror:
            params += ' --mirror'

        if self.doNorm:
            params += ' --norm'

        return params


As you can see, this function will concatenate the arguments passed to
the program in the command line. The arguments will vary depending on the
current selection of input parameters in the Scipion GUI. The same
approach can be followed when executing a program from any other
software package.

If we take a look at the output logs files after executing this
protocol, we can see a command line similar to the following:

.. code-block:: bash
    mpirun -np 2 -bynode `which xmipp_mpi_ml_align2d`
    -i Runs/000194_XmippProtML2D/tmp/input_particles.xmd
    --oroot Runs/000194_XmippProtML2D/ml2d_ --ref Runs/000194_XmippProtML2D/tmp/input_references.xmd
    --fast --thr 2 --iter 3 --mirror


Creating Outputs
----------------

At the end of a protocol execution, we want to register the results in
the Scipion project. This is the function of the ``createOutputStep``
method. It is the inverse operation of the
``convertInputStep``. It should read the files produced by the
protocol and create the Scipion objects that represent the output of the
protocol. It should also define the relationship between the newly created
output objects and the input.

In our case, the result of the protocol is a ``SetOfClasses2D``, which
is created by the following code:

.. code-block:: python

    def createOutputStep(self):
        imgSet = self.inputParticles.get()
        classes2DSet = self._createSetOfClasses2D(imgSet)
        readSetOfClasses2D(classes2DSet, self._getFileName('output_classes'))
        self._defineOutputs(outputClasses=classes2DSet)
        self._defineSourceRelation(imgSet, classes2DSet)
        if not self.doGenerateReferences:
            self._defineSourceRelation(self.inputReferences.get(), classes2DSet)


Here the job is done by the functions ``_createSetOfClasses2D`` and
``readSetOfClasses2D``. The first one creates an empty set of
classes, while the second is specific to Xmipp and populates the set
reading the classes' information from the Xmipp metadata outputs (STAR
files). More information about creating Scipion sets objects can be
found in link:UsingSets[Developers - Using Sets].

Additional Functions
====================

There are some functions that not are strictly required when
implementing a protocol. Nevertheless, they can provide useful
information to the final user. All these functions will return a list of
strings, which meaning is different in each case.

Validate and Warnings
---------------------

The ``_validate`` and ``_warnings`` methods will be called just before a
protocol is executed. Both could return a list of string messages,
meaning that are some errors (or possible errors) in the input
parameters. If the returned list is empty means that everything is fine
and the protocol can run. The ``_warnings`` will show the messages to
the user but give it the choice to continue or not. If there are errors
from the *``_validate``*, the protocol will not run. This can save time
to users because prevent simple errors that can be critical for the
protocol to run properly.

In our example, the ``_validate`` function is very simple. It checks that
the input particles have a CTF estimation if using maximum likelihood
in Fourier space. The ``_warnings`` method can be implemented in a
similar way.

.. code-block:: python

    def _validate(self):
        errors = []
        if self.doMlf:
            if not self.inputParticles.get().hasCTF():
                errors.append('Input particles does not have CTF information.\n'
                              'This is required when using ML in fourier space.')
        return errors



Citations, Summary and Methods
------------------------------

The ``_citations`` function is the way to provide references to the
methods used in the protocols. The returned list should contain the
keys of the citation reference. All the references for a specific
software package are listed in bibtex format in a file called
**bibtex.py**. Read more about this file in this guide to
:doc:`create a plugin <creating-a-plugin>`.

In this case, there is a reference for the whole protocol and some extra
references are added depending on whether some variants are activated. The
citation will be displayed in the GUI as links to each publication. They
can be shown using the |cite-icon| from the protocol
header in the form GUI or in the project windows in the **Methods** tab of
the selected protocol.

.. code-block:: python

    def _citations(self):
        cites = ['Scheres2005a']

        if self.doMlf:
            cites.append('Scheres2007b')

        elif self.doFast:
            cites.append('Scheres2005b')

        if self.doNorm:
            cites.append('Scheres2009b')

        return cites

The ``_summary`` function should provide a quick overview of a particular
protocol execution. It should check whether the protocol has not
finished its execution yet or, when finished, it has to provide some
brief information about the steps performed, outputs, quality, or any
other relevant information.

.. code-block:: python

    def _summary(self):
        summary = []
        nParticles = self.inputParticles.get().getSize()
        nReferences = self.numberOfReferences.get()
        summary.append('Number of input images: *%d*' % nParticles)
        summary.append('Classified into *%d* classes' % nReferences)

        if self.doMlf:
            summary.append('- Used a ML in _Fourier-space_')
        elif self.doFast:
            summary.append('- Used _fast_, reduced search-space approach')

        if self.doNorm:
            summary.append('- Refined _normalization_ for each experimental image')

        return summary

The ``_methods`` function should be implemented in a way similar to
``_summary`` but should provide more descriptive information about the
execution. The text should be thorough enough to be used as a template for
a ``_Materials`` and ``methods_`` section of a paper.


Extra Actions
=============

These should be done while developing and testing your protocol, not at the very end of the process.

Make the protocol available
---------------------------

If you want your protocol to appear in the project GUI to be used
(and you probably will), you may need to do some configuration setup.
The protocol classes that are available in Scipion are discovered
dynamically using Python reflection tools. So, when a new protocol class
is added, it is automatically available to the whole system. Such
configuration is needed if you want your protocol to appear in an
specific position in the protocol tree in the left pane of the
projects GUI. This is performed with the :ref:`protocols.conf file<protocols.conf>`.

Implement a Viewer
------------------

The ``Viewer`` class is the base for implementing visualization of
different kinds of objects. The same applies for visualizing protocols. The
viewers are also discovered dynamically, like the protocols are. They should
specify a ``_target`` property with a list of the object classes that the
viewer is able to handle.

The details for developing a new viewer will be described in
:doc:`How to develop Viewers <creating-a-viewer>`.


Writing Tests for your Protocol
-------------------------------

Writing tests is the best way to develop from the beginning. It will
help to cover different use cases of your functions (or protocols in
this case). It they are run automatically, they will help to detect bugs
introduced in future changes.

Here is the test for this protocol:

.. code-block:: python

    class TestXmippML2D(TestXmippBase):
        """This class check if the protocol to classify with ML2D
           in Xmipp works properly.
        """
        @classmethod
        def setUpClass(cls):
            setupTestProject(cls)
            TestXmippBase.setData('mda')
            cls.protImport = cls.runImportParticles(cls.particlesFn, 3.5)

        def test_ml2d(self):
            print "Run ML2D"
            protML2D = self.newProtocol(XmippProtML2D,
                                       numberOfReferences=2, maxIters=3,
                                       numberOfMpi=2, numberOfThreads=2)
            protML2D.inputParticles.set(self.protImport.outputParticles)
            self.launchProtocol(protML2D)

            self.assertIsNotNone(protML2D.outputClasses, "There was a problem with ML2D")


TODO
====

* Review all :doc: directives and add content to the empty ones


.. |cite-icon| image:: /docs/images/guis/cite_icon.png