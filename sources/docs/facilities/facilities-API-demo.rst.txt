.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _facilities-API-demo:

=============
API workflows
=============

**This is a draft**

The `usingAPI-demo/form_launcher.py <https://github.com/I2PC/em-facilities/blob/8a31f7f5eed3dc73443266272c40b1da6432135d/usingAPI_demo/form_launcher.py#L396-L447>`_
creates an empty project by means of

.. code-block:: python

    manager = Manager()
    project = manager.createProject(projName, location=scipionProjPath)

then, we fill the project with protocols by function

.. code-block:: python

    preprocessWorkflow(project, dataPath, self.configDict)

which is in
`usingAPI-demo/form_launcher.py <https://github.com/I2PC/em-facilities/blob/master/usingAPI_demo/acquisition_workflow.py>`_

For instance, to create the *Import movies*

.. code-block:: python

    protImport = project.newProtocol(
                      ProtImportMovies,
                      objLabel='import movies',
                      importFrom=ProtImportMovies.IMPORT_FROM_FILES,
                      filesPath=dataPath,
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

Notice that the first argument of the `project.newProtocol` function is a
`EM-protocol <https://scipion-em.github.io/docs/api/pyworkflow.em.protocol.html#pyworkflow-em-protocol-package>`_
subclass corresponding to that protocol to be created, and the following
arguments are all those parameters to be set. If a parameter is not
set, the default value is used.

Alternativelly, a protocol parameter can be set as follow

.. code-block:: python

    protMotionCor = project.newProtocol(ProtMotionCorr)
    protMotionCor.set(protImport.outputMovies)

Notice that to use this `protImport` must have an attribute
called `outputMovies` if not, this line will break.








Then every protocol can be saved by

.. code-block:: python

    project.saveProtocol(protImport)

or launched

.. code-block:: python

    project.launchProtocol(protImport)
