.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _facilities-API-demo:

=============
API workflows
=============

To create a Scipion workflow from a Python script, you only need to do 3 logical
steps:

1. `Create an empty project <facilities-api-demo#id1>`_.
2. `Create protocols <facilities-api-demo#id2>`_.
3. `Register that protocols to the project <facilities-api-demo#id3>`_.

In addition, we include an special mention in `how to set EM objects as protocol
inputs <facilities-api-demo#id4>`_.


0. Getting config and user parameters
=====================================

First of all, we need to get all the *config* and *user* parameters retrieved in
`previous steps <acquisition-simulation#id2>`_. We have stored all these
parameters in a dictionary that is gotten as argument by the main function script
located in this section (`acquisition_workflow.py <https://github.com/I2PC/em-facilities/
blob/master/usingAPI_demo/acquisition_workflow.py>`_).
In addition, we import the *UPPER_CASE* constants from `constants.py
<https://github.com/I2PC/em-facilities/blob/master/usingAPI_demo/constants.py>`_
to ensure that we use the same that in the wizard (`form_launcher.py
<https://github.com/I2PC/em-facilities/blob/master/usingAPI_demo/acquisition_workflow.py>`_)
and also to easy gat values from the `configDict` variable.

.. code-block:: python

    from constants import *

    def preprocessWorkflow(configDict):

        numCpus = (configDict.get(NUM_CPU) if configDict.get(NUM_CPU, 0)
                       else int(subprocess.Popen(['nproc','--all'],
                                                 stdout=subprocess.PIPE).stdout.read()))

Note that we are taking the number of CPUs from the `configDict` via the `NUM_CPU`
constant.

1. Creating a project
=====================

To create an empty project,

.. code-block:: python

    from pyworkflow.project import Manager
    manager = Manager()
    project = manager.createProject(configDict[PROJECT_NAME],
                                    location=configDict[SCIPION_PROJECT]

where `PROJECT_NAME` and `SCIPION_PROJECT` return the project name and
the project path, respectively.


2. Including protocols
======================

Once a project is created, we must fill it with protocols.

To be able to instance a protocol, it must be imported from the containing plugin
(or from Scipion). Here an example of importing the *Import Movies* and
the *Motioncor* protocols

.. code-block:: python

    from pyworkflow.em.protocol import ProtImportMovies
    import pyworkflow.utils as pwutils
    ProtMotionCorr = pwutils.importFromPlugin('motioncorr.protocols', 'ProtMotionCorr')

Notice that use the `pwutils.importFromPlugin()` function to import classes from
plugins in order to avoid uncontrolled errors if that plugin is not installed.

For instance, to create the *Import movies*

.. code-block:: python

    protImport = project.newProtocol(
                      ProtImportMovies,
                      objLabel='import movies',
                      importFrom=ProtImportMovies.IMPORT_FROM_FILES,
                      filesPath=configDict.get(DATA_FOLDER),
                      filesPattern=configDict.get(PATTERN),
                      amplitudeContrast=configDict.get(AMP_CONTR),
                      sphericalAberration=configDict.get(SPH_AB),
                      voltage=configDict.get(VOL_KV),
                      samplingRate=configDict.get(SAMPLING),
                      doseInitial=configDict.get(DOSE0, 0),
                      dosePerFrame=configDict.get(DOSEF, 0),
                      gainFile=gainFn,
                      dataStreaming=True,
                      timeout=configDict.get(TIMEOUT, 43200)  # 12h default
                      )

Notice that the first argument of the `project.newProtocol()` function is an
`EM-protocol <https://scipion-em.github.io/docs/api/pyworkflow.em.protocol.html
#pyworkflow-em-protocol-package>`_
object, corresponding to that protocol to be created (and imported above).
The following arguments are all those parameters to be set, where if a parameter
is not set, the default value is used.

3. Registering protocols
========================

Once a protocol is instanced, we should register it in two alternative ways:

* **Saving the protocol**:
    .. code-block:: python

        project.saveProtocol(protImport)

    This option is similar to create a *JSON* block when
    making Scipion's templates. In this way, the protocols do not run until the whole workflow will be launched after
    including all the protocols (see `launch an open workflows <acquisition-simulation.html#
    launch-an-open-workflows>`_). Thus, the output objects from protocols are not
    instanced yet and, then, no information can be gotten from them. Even though, they
    can be used for the next protocols with no inconvenience as we will see below.

* **Launching the protocol**:
    .. code-block:: python

        project.launchProtocol(protImport, wait=False)

    This option is to launch protocols as soon as we create them
    (similar to a manual processing). The drawback here is that we must take
    into account that all inputs have to be ready before launching a certain
    protocol. In this way, we must monitor the outputs of the protocols to
    prevent launching posterior protocols with empty inputs.

    Notice that we introduce `wait=False` to continue with the script.
    If `wait=True`, the script stops here until that protocol finishes.


These two options are noticeable different and we must take a procedure decision,
since we should do the same for all the protocols.


4. Setting EM objects as protocol inputs
========================================

We have seen how to set protocol parameters in the initialization arguments.
However, any protocol parameter (let's say parameter `input1` of protocol
`prot1`) can also be set as `prot1.input1.set(value)`. For instance,

.. code-block:: python

    protMotionCor = project.newProtocol(ProtMotionCorr)
    protMotionCor.doApplyDoseFilter.set(configDict.get(DOSEF, 0)>0)

where `protMotionCor` is initialized in the first line whereas in the second line
`doApplyDoseFilter` is set to `True` if the *dose per frame* introduced in
`the previous steps <acquisition-simulation#id2>`_ is bigger than 0 or
to `False`, instead.

At this point, we only have set `Scalar <https://scipion-em.github.io/docs/api/
pyworkflow.object.html#pyworkflow.object.Scalar>`_ objects or basic objects.
To set `EMSets <https://scipion-em.github.io/docs/api/pyworkflow.em.data.html
#pyworkflow.em.data.EMSet>`_ (SetOfMovies, SetOfMicrographs, SetOfCtfs,
SetOfParticles...) produced in previous protocols, we must take into account
that previous protocol may be not running yet (`it can be saved
<facilities-API-demo#registering-protocols>`_), then in that cases the output is
not created yet.
Therefore, we set the whole protocol as input parameter, while indicating which
object should be retrieved from that protocol, in the running time.
For instance,

.. code-block:: python

    protMotionCor.inputMovies.set(protImport)
    protMotionCor.inputMovies.setExtended('ouputMovies')

where the whole `protImport` protocol is attached to the
`protMotionCor.inputMovies` in the first line and the `outputMovies` is set as
an extension for this parameter, indicating that it will be gotten in the
running time.

If you decided to `launch protocols as soon as they are created
<facilities-API-demo#registering-protocols>`_, then a direct
assignation is possible as long as the object is ready

.. code-block:: python

    protMotionCor.inputMovies.set(protImport.outputMovies)

Notice that to use this `protImport` must have an attribute
called `outputMovies` if not, this line will break.

In this case, a waiting function to ensure that the `protImport.outputMovies`
is ready to be used becomes crucial. For instance

.. code-block:: python

    from time import sleep

    def waitOutput(protocol, outputAttributeName, checkNotEmpty=True, timeout=5000):
        """ Wait until the output is being generated by the protocol.
            Returns False if the TimeOut is reached or True, instead.
        """
        timeStep = 5.  # checking every 5 second

        def _loadProt():
            # Load the last version of the protocol from its own database
            prot2 = getProtocolFromDb(protocol.getProject().path,
                                      protocol.getDbPath(),
                                      protocol.getObjId())
            # Close DB connections
            prot2.getProject().closeMapper()
            prot2.closeMappers()
            return prot2

        counter = 1
        prot2 = _loadProt()

        while not prot2.hasAttribute(outputAttributeName):
            sleep(timeStep)
            prot2 = _loadProt()
            if counter > timeout/timeStep:
                return False
            counter += 1

        outputObject = prot2.getAttributeValue(outputAttributeName)
        while not outputObject is not None and not outputObject.getSize() > 0:
            sleep(timeStep)
            prot2 = _loadProt()
            if counter > timeout/timeStep:
                return False
            counter += 1

        # Update the protocol instance to get latest changes
        project._updateProtocol(protocol)

        return True

    # Waiting for a non empty ouput from MotioCor2 to continue
    waitOutput(protMotionCor, 'outputMicrographs')

    # Importing, creating and launching the gCTF protocol
    ProtGctf = pwutils.importFromPlugin('gctf.protocols', 'ProtGctf')
    protGCTF = project.newProtocol(ProtGctf,
                                   objLabel='gCTF estimation',
                                   gpuList=str(configDict.get(GCTF)))
    protCTF2.inputMicrographs.set(protMotionCor.outputMicrographs)
    project.launchProtocol(protGCTF, wait=False)

    # Waiting for at least one CTF estimation to continue
    waitOutput(protGCTF, 'outputCTF')


