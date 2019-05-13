.. _gpu-params-standardization:

===================================================
GPU parameters standardization in Scipion protocols
===================================================

Overview
--------

This entry is intended for Scipion developers and explains the basic ideas behind the GPU parameters standardization among different protocols. Computing with GPUs has increasingly being used by different programs for CryoEM image processing. So, after introducing many GPU-based Scipion protocols, we have realized that similar parameters are named different and in some protocols, we couldn't use multiple GPUs. So, the ideas explained here addressed mainly the following two related issues:

* Name in a similar way GPUs related params
* Allow that multiple GPUs can be used in some protocols

Standardization of GPU parameters
----------------------------------

We propose the introduction of the following parameters (name constants defined
in `constanst.py <https://github.com/delarosatrevin/scipion/blob/cd1001579cdd4d53cbd4b8c666ead06c84e0303c/pyworkflow/protocol/constants.py#L67>`_):

* USE_GPU: a boolean parameter to ask if use the GPU or not in this protocol. Some programs only run in GPU, so the protocol should not define this parameter and the use of the GPU is compulsory.
* GPU_LIST: a string parameter that define the list of GPU IDs that will be used by the protocol.

The use of those parameter is not forced right now for GPU protocols.This will
allow to progressively modify the protocols but keep them working as expected
in the meantime. When these parameters are defined, some functions are available
in the `Protocol class <https://github.com/delarosatrevin/scipion/blob/cd1001579cdd4d53cbd4b8c666ead06c84e0303c/pyworkflow/protocol/protocol.py#L625>`_

When the GPU_LIST param is used, then it will be displayed on the top of the protocol form together with other common execution parameters (see image below).

.. figure:: /docs/images/scipion-gpu-form.png
   :alt: Scipion GPU Form


The value of these parameters can be used as usual to form the command line of a given program. But if you want to enable execution in multiple GPUs/threads (handled by the Scipion execution engine), the special %(GPU)s should be used. Keep reading next section to know more details.

Execution on multiple GPUs/threads
----------------------------------

When a protocol use the STEPS_PARALLEL execution mode, Scipion provides an automatic parallelization of the steps using either MPI or Threads. Now this can be combined with the GPU_LIST (only for threads, not tested with MPIs).

Apart from using the STEPS_PARALLEL mode, the command line should use a special mark: %(GPU)s. This value will be later replaced by the StepsExecutor with the value of the GPU(s) assigned to a given step. For example, in the MotionCor2 protocol, the command line should be modified as shown below:

Before:

.. code-block:: bash

    args += '-gpu %s' % self.gpuList.get()

After:

.. code-block:: bash

    args += '-gpu %(GPU)s'

For example, in MotionCor2...if the user set 3 threads and GPU List = 0 1, then thread 0 will be master and thread 1 will use GPU 0 and thread 2 in GPU 1. If the user set 5 threads, then two threads will run on GPU 0 and two threads in GPU 1 (which is not recommended with the new version of MC2). If 3 threads and 0 1 2 3 GPUs, then again 1 master and thread 1 will have GPUs 0 1 and thread 2 GPUs 2 3.



