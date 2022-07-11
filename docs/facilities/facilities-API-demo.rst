.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _facilities-API-demo:

=============
API workflows
=============

To create Scipion workflows from Python scripts, you only need to do a few logical
steps:

#. `Creating a project`_
#. `Creating some protocols`_
#. `Adding protocols to the project`_

In addition, we include an special mention in `how to set EM objects as protocol
inputs<Setting EM objects as protocol inputs>`_.


Creating a project
==================

To create an empty project, you only must use the `Manager.createProject()
<../../api/pyworkflow/pyworkflow.project.manager.html#pyworkflow.project.manager.Manager.createProject>`_ method

.. code-block:: python

    from pyworkflow.project import Manager

    manager = Manager()
    project = manager.createProject(configDict[PROJECT_NAME],
                                    location=configDict[SCIPION_PROJECT]

where ``PROJECT_NAME`` and ``SCIPION_PROJECT`` constants return the project name and
the project path from the ``configDict``, respectively.


Creating some protocols
=======================

Once a project is created, we must fill it with protocols.

To be able to instance a protocol, it must be imported from the containing plugin
(or from Scipion). Here an example of importing the `Import Movies
<../../api/pwem/pwem.protocols.protocol_import.micrographs.html#pwem.protocols.protocol_import.micrographs.ProtImportMovies>`_ protocol
from Scipion and the `Motioncor <https://github.com/scipion-em/scipion-em-motioncorr/blob/
master/motioncorr/protocols/protocol_motioncorr.py>`_ protocol from the
`scipion-em-motioncor <https://github.com/scipion-em/scipion-em-motioncorr>`_
plugin.

.. code-block:: python

    import pyworkflow.utils as pwutils

    from pyworkflow.em.protocol import ProtImportMovies
    ProtMotionCorr = pwutils.importFromPlugin('motioncorr.protocols', 'ProtMotionCorr')

Notice that we use the `pwutils.importFromPlugin() <../../api/pyworkflow/pyworkflow.plugin.html#pyworkflow.plugin.Domain.importFromPlugin>`_
method to import classes from plugins in order to avoid uncontrolled errors
if that plugin is not installed in the current Scipion.

To create a protocol, the `Project <../../api/pyworkflow/pyworkflow.project.project.html#pyworkflow.project.project.Project>`_ class has
a method to make new protocols.
For instance, for the *Import movies*

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

Notice that the first argument of the `project.newProtocol() <../../api/pyworkflow/pyworkflow.project.project.html#pyworkflow.project.project.Project.newProtocol>`_
method is an `EM-protocol <../../api/pwem/pwem.protocols.protocol.html#pwem.protocols.protocol.EMProtocol>`_
subclass, corresponding to that protocol to be created (and imported above).
The following arguments are all those `form parameters <../../api/pyworkflow/pyworkflow.protocol.params.html#pyworkflow.protocol.params.FormElement>`_
defined by `the protocol <../../api/pwem/pwem.protocols.protocol_import.micrographs.html#pwem.protocols.protocol_import.micrographs.ProtImportMicBase>`_ using the
`addParam() <../../api/pyworkflow/pyworkflow.protocol.params.html#pyworkflow.protocol.params.ElementGroup.addParam>`_ method.
If a parameter is not set, the default value is used.

Adding protocols to the project
===============================

Once a protocol is instanced, we should register it, which means writing it in
disk at the data bases. This can be done in two **alternative** ways:

* **Saving the protocol** using the `project.saveProtocol() <../../api/pyworkflow/pyworkflow.project.project.html#pyworkflow.project.project.Project.saveProtocol>`_
  method:

  .. code-block:: python

        project.saveProtocol(protImport)

  This option is conceptually similar to create a *JSON* block when making
  `Scipion's templates <facilities-workflows.html#id1>`_
  Therefore, that protocol does not run until the whole workflow will be
  launched after including all the rest protocols.
  Thus, the output objects from the saved protocols are not created yet and,
  then, no information can be gotten from them. Even though, they
  can be used for the next protocols with no inconvenience as we will see below.

* **Launching the protocol** using the `project.launchProtocol() <../../api/pyworkflow/pyworkflow.project.project.html#pyworkflow.project.project.Project.launchProtocol>`_
  method:

  .. code-block:: python

        project.launchProtocol(protImport, wait=False)

  This option is to launch the protocol as soon as we register it
  (conceptually similar to a manual processing using the GUI).
  The drawback here is that we must take into account that all inputs have to
  be ready before launching a certain protocol.
  In this way, we must monitor the outputs of the protocols to prevent launching
  posterior protocols with empty inputs.

  Notice that we introduce `wait=False` to continue with the script.
  If `wait=True`, the script stops here until that protocol finishes and this
  doesn't make sense for streaming processing.


These two options are noticeable different and we must take a procedure decision,
since we should do the same for all the protocols.


Setting EM objects as protocol inputs
=====================================

We have seen how to set protocol parameters in the initialization arguments.
However, the `set(value) <../../api/pyworkflow/pyworkflow.object.html#pyworkflow.object.Object.set>`_ method sets a value to any protocol parameter.
For instance,

.. code-block:: python

    protMotionCor = project.newProtocol(ProtMotionCorr)
    protMotionCor.doApplyDoseFilter.set(configDict.get(DOSEF, 0)>0)

where `protMotionCor <https://github.com/scipion-em/scipion-em-motioncorr/blob/
d9397a6dd5c9493a67b08d08f8c2af1e8f580c61/motioncorr/protocols/
protocol_motioncorr.py#L50-L55>`_ is initialized in the first line whereas the
`doApplyDoseFilter <https://github.com/scipion-em/scipion-em-motioncorr/blob/d9397a6dd5c9493a67b08d08f8c2af1e8f580c61/
motioncorr/protocols/protocol_motioncorr.py#L167-L171>`_ is set to ``True`` if
the *dose per frame* introduced by the user is bigger than 0 or
to ``False``, instead.

Until here, we only have set `Scalar <../../api/pyworkflow/pyworkflow.object.html#pyworkflow.object.Scalar>`_ objects or `Built-in Python Types <https://docs.python.org/2.7/library/stdtypes.html>`_.
However, usually we want to use `EMSets outputs <../../api/pwem/pwem.objects.data.html#pwem.objects.data.EMSet>`_
(`SetOfMicrographs <../../api/pwem/pwem.objects.data.html#pwem.objects.data.SetOfMicrographsBase>`_,
`SetOfCtfs <../../api/pwem/pwem.objects.data.html#pwem.objects.data.SetOfCTF>`_,
`SetOfCoordinates <../../api/pwem/pwem.objects.data.html#pwem.objects.data.SetOfCoordinates>`_,
`SetOfParticles <../../api/pwem/pwem.objects.data.html#pwem.objects.data.SetOfParticles>`_,
`SetOfClasses <../../api/pwem/pwem.objects.data.html#pwem.objects.data.SetOfClasses>`_...) from previous protocols as input
for next protocols. At this point, we must take into
account that previous protocols may be not running yet (see `Adding protocols to the project`_). Then, in that cases, the previous
outputs are not created yet. Therefore it cannot be passed as value in the
`set(value) <../../api/pyworkflow/pyworkflow.object.html#pyworkflow.object.Object.set>`_ method. To fix this situations,
we set the whole protocol as input parameter, while indicating which
object should be retrieved in the running time from that protocol by means of
the `setExtended() <../../api/pyworkflow/pyworkflow.object.html#pyworkflow.object.Pointer.setExtended>`_ method. For instance,

.. code-block:: python

    protMotionCor.inputMovies.set(protImport)
    protMotionCor.inputMovies.setExtended('ouputMovies')

where the whole ``protImport`` protocol is attached to the
``protMotionCor.inputMovies`` in the first line and the ``outputMovies`` is set as
an extension for this parameter, indicating that it will be gotten in the
running time.

If you decided to launch protocols as soon as they are created when `adding protocols to the project`_, then a direct
assignation is possible as long as the object is ready

.. code-block:: python

    protMotionCor.inputMovies.set(protImport.outputMovies)

Notice that to use this, ``protImport`` must have an attribute
called ``outputMovies`` if not, this line will break.

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

    # Waiting for a non empty output from MotioCor2 to continue
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


