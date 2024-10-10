.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo


.. _threadsmpigpus:

============
Introduction
============

Scipion integrates many different software. Additionally, it has some internal protocols like "import" protocols or
generic tools like various sub-setting protocols. Any protocol defines a specific execution plan that may or
may not allow to run its internal steps in parallel. The execution plan is a list of **steps** that may have
dependencies.

Simplest execution plan
-----------------------

The simplest protocols in terms of execution plan might be the "import" ones. They usually define a single-step execution plan and do not have any dependencies.
These protocols do not show the parallelization section/parameters as we will show later.


.. figure:: /docs/images/guis/executed_import_particles.png
    :alt: Import particles protocol

    The "import particles" protocol is a single-step protocol. There is no chance to parallelize nor an opportunity to
    define dependencies.


The execution plan is the first thing that happens when a protocol is executed and therefore can only be seen for
running, failed or finished protocols. To show the execution plan of a protocol you can press "Shift + s" in the project.



.. figure:: /docs/images/guis/simplest-exec-plan.png
    :alt: Execution plan of the Import particles protocol

    Simplest execution plan. Just one step defined.


Serial execution plan
_____________________

A serial execution plan is a set of steps that run one after another. They are usually linear but there could
be cases where there are branches. But in any case, 2 steps are NEVER running simultaneously.

.. figure:: /docs/images/guis/serial-exec-plan.png
    :alt: Serial execution plan: in this case, steps 1 and 2 could run in parallel but the protocol does NOT offer
          threads to do so.

    Serial execution plan: in this case, steps 1 and 2 could be run in parallel but the protocol does NOT offer threads to do so.



Parallelization
_______________

Parallelization is a technique that allows to run code concurrently. There are 2 different ways
to parallelize a protocol in Scipion which is decided by the developer: Scipion parallelization or 3rd party
parallelization. Parallelization is typically done using "Threads" or "MPIs" or both. Scipion parallelization is
only done by Threads.

3rd party parallelization
.........................

In this case, the software Scipion integrates is already parallelized and typically it just needs to know how many
threads or MPI you want to use. The protocol window in Scipion shows the "parallel section" parameters
with thread and/or MPIs but the execution plan (steps) are serial. The only difference is that a certain step will 
call the "3rd party program" with some arguments that will tell that program to create
threads or MPIs. It is the external software the one that deals with parallelization, not Scipion.

.. figure:: /docs/images/guis/external-parallelization.png
    :alt: Relion refine form and execution plan showing a serial step layout.

    Relion refine protocol form and execution plan showing a serial step layout. Nevertheless, the form displays a parallel section with threads
    and MPIs that are handled by Relion

Scipion parallelization
.......................

In this case, Scipion is doing the parallelization. The execution plan (steps) can run in parallel providing the
dependencies are met. These protocols show "Scipion threads" in the form and the execution plan should show 2 or more
branches where steps could be running at the same time.

.. figure:: /docs/images/guis/scipion-exec-plan.png
    :alt: Screenshots of Aretomo form and execution plan.

    Aretomo (cryo-electron tomography method) is parallelized using Scipion threads. The execution plan shows the step
    1 is independent from step 2 and could run in parallel at the same time. When step 2 finishes, step 3 can start while
    step 1 is still active.


----
GPUs
----
Some of the programs can use GPU acceleration. A machine/node could have GPUs installed and you may want to use one,
two or more of them. The way to specify GPU/s to use is by GPU ID: a number starting from 0.
If the protocol supports GPU acceleration, then you should see a corresponding field in the form. 
See "Aretomo" image above has 0 in the *GPU IDs* field. This means that aretomo will use GPU 0 for any of its steps
that may require a GPU.

Now, depending on the execution plan of the protocol, same GPU could be used in parallel at the same time. This could
be what you actually want, or maybe you want to prevent this in case the program "needs" a dedicated
GPU and does not like sharing it with "other" GPUs.


.. note:: You can specify more than 1 GPUs separating them by either commas or spaces: "0 1 2" or "0,1,2"


Serial execution and GPUs
.........................
This is probably the simplest case. In a serial execution plan there is NO parallelization, so whichever value you enter
in the "GPUs ID" field will be used in any step.

3rd party parallelization and GPUs
..................................
This case is very much like the previous one. Since Scipion is not doing the parallelization whatever is entered in
the GPU field is passed to the software.

Scipion parallelization ans GPUs
................................
This case can be used in multiple scenarios. Let's start with the simplest example. You want all steps that can run in parallel
to use the same GPU (GPU ID 0). Let's assume we have specified 3 threads in the "Scipion threads" field. One thread is required 
for the main process and 2 threads are for the processing steps. 2 processing threads need 2 "slots" for GPUs. This can be done by setting GPU IDs to "0,0" or "0 0".

.. note:: If you just set GPU IDs = 0 then Scipion will interpret this as only 1 available slot for GPU processing and parallelization will not happen.

If you have 2 GPUs (GPU IDs 0 and 3) and 2 processing threads available and you want/need to assign one GPU per thread you can just
set GPU IDs to "0,3".

If you have 4 GPUs (GPU IDs 0,1,2,3) and 2 processing threads you could specify all GPU IDs (0,1,2,3), and then Scipion will spread the GPUs evenly
among the processing threads: 0,1 for one thread and 2,3 for the other.

Here is table summarizing some common cases:

.. list-table:: Threads and GPUs cases
   :widths: 25 25 50 50
   :header-rows: 1

   * - Scipion threads
     - Processing threads
     - GPUs Id
     - GPU slots
   * - 4
     - 3
     - 0
     - 1 (0)
   * - 3
     - 2
     - 2,4
     - 2 (2 and 4)
   * - 2
     - 1
     - 3,4,5
     - 1 (3,4,5)
   * - 3
     - 2
     - 2,4,2,4
     - 2 (2,4 and 2,4)
   * - 5
     - 4
     - 0,1,2,3
     - 4 (each GPU gets one thread)



Void GPUs
.........
To provide more flexibility in the GPU definition we have created a "void" GPU. This GPU has ID 99 (hope you
don't have a machine with that amount of GPUs) ;-).

If you enter that value as a GPU ID, the corresponding GPU slot will have one less GPU.

If you enter "Scipion threads" = 3 (2 processing threads) and GPU IDs = "0 1 2 99", then the first thread will use GPUs 0 and 1, and
the second thread will use just GPU 2.

This method allows to utilise 3 GPUs (2 + 1) in a program that could use one or two GPUs but you have 3 GPUs available


GPUs in clusters
................
When submitting jobs to a queuing system, Scipion is unaware of the GPU resources available in the queue. In this case, GPU IDs entered
in the protocol form are always renumbered to start from 0. It does not matter if you enter "2 4 7" etc., it will always end up as "0 1 2". 
The queue manager takes responsibility for "remapping" GPUs to the correct IDs.

