.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _parallelization:

===============
Parallelization
===============

By default, each function step is executed just after the previous one
is fully completed. If you would like to execute any steps on parallel
you have to add an extra parameter called ``prerequisites``. This parameters
will identify the dependent id, i.e. the id of the previous step which
has to be completed before executing this step.

Here you can see an example which tries to illustrate how to create a
parallel step:

.. code-block:: python

         ....

         def _insertAllSteps(self):
            ....
            self._insertFunctionStep('downloadMoviesStep')
            self._insertFunctionStep('closeSetStep', wait=True)

        def downloadMoviesStep(self):
            """
            Download a set of movies located an a specific path
            """
            path = '/home/user/images/'
            readXmlFileStep = self._insertFunctionStep("readXmlFileStep")
            depStepsList = [] # Store all steps ids, final step closeSetStep depends on all of them
            # Move for a directory finding files to add
            for file in os.listdir(path):
                if file not in self.registerFiles:
                    self.registerFiles.append(file)
                    # Make estimation steps independent
                    newStep = self._insertFunctionStep('registerImageStep',
                                                         file, prerequisites=[readXmlFileStep])
                    depStepsList.append(newStep)
                # Updating the total of protocol steps
                self.updateSteps()

        ....

``readXmlFileStep`` is executed just after the previous step is completed.
On the other hand, ``registerImageStep`` is executed  _number_of_files_ times.
All these executions are performed on parallel because they only depend on
``readXmlFileStep`` (id of the ``readXmlFileStep`` function). If we do not
provide the ``prerequisites`` parameter, each ``registerImageStep`` execution
would depend on the previous ``registerImageStep`` execution and therefore they
would not be executed in parallel.

Two details to take into account when creating a protocol where some of its
steps are in parallel, are the following:

* In the protocol ``__init__`` definition add the following instruction:

.. code-block:: python

    def __init__(self, **args):
        ....
        self.stepsExecutionMode = STEPS_PARALLEL
        ....

* In the protocol ``_defineParams`` method  add the parallelization section defining
  the number of threads and mpi to use.

.. code:: python

    def _defineParams(self, form):
        ....
        form.addParallelSection(threads=2, mpi=1)
        ...

