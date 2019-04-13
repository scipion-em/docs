.. _parallelization:

===============
Parallelization
===============

By default, each function step is executed just after the previous one
is fully completed. If you would like to execute any steps on parallel
you have to add an extra parameter called prerequisites. This parameters
will identify the dependent id, i.e. the id of the previous step which
has to be completed before executing this step.

Here you can see an example which tries to illustrate how to create a
parallel step:

.. code-block::python

  bestVolumesStepId = self._insertFunctionStep("getBestVolumes")

  deps = [] # Store all steps ids, final step createOutput depends on all of them

  # Refine the best volumes
  for n in range(self.numVolumes.get()):
      fnBase = 'proposedVolume%05d' % n
      fnRoot = self._getPath(fnBase)

      # Simulated annealing
      self._insertFunctionStep('reconstruct', fnRoot, prerequisites=[bestVolumesStepId])
      # Make estimation steps independent


``getBestVolumes`` is executed just after the previous step is completed.
On the other hand, ``reconstruct`` is executed _numVolumes_ times. All
these executions are performed on parallel because they only depend on
``bestVolumesStepId`` (id of the ``getBestVolumes`` function). If we do not
provide the ``prerequisites`` parameter, each ``reconstruct`` execution
would depend on the previous ``reconstruct`` execution and therefore they
would not be executed in parallel.

**TO DO**: mention how to use something like this is in
**`_defineParams`**:

..code:: python

    form.addParallelSection(threads=0, mpi=4)

