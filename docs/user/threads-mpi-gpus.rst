.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo


.. _threadsmpigpus:

============
Introduction
============

Scipion integrates many different software. Additionally it adds some internal protocols like "import" protocols or
generic tools like the variety of sub-setting protocols. Each of them defines a specific execution plan that may or
may not allow for running its own internal steps in parallel.The execution plan is a list of **steps** that may have
dependencies among them.

Simplest execution plan
-----------------------

The simplest protocols in terms of execution plan might be the "import" ones. They usually define a single step execution plan and therefore without any dependency.
These protocols do not show the parallelization section/parameters as we will show latter.


.. figure:: /docs/images/guis/executed_import_particles.png
    :alt: Import particles protocol

    The "import particles" protocol is a single step protocol. There is no chance to parallelize nor an opportunity to
    define dependencies.


The execution plan is the first thing that happens when a protocol is executed and therefore only can be seen in
running, failed or finished protocols.

To show the execution plan of a protocol in any of the above mentioned status you can press "Shift + s" in the project.



.. figure:: /docs/images/guis/simplest-exec-plan.png
    :alt: Execution plan of the Import particles protocol

    Simplest execution plan. Just one step defined.


Serial execution plan
_____________________

A serial execution plan is a set of steps that are run one after another. They are usually linear but there could
be cases where there are branches. But in any case 2 steps are NEVER running at the same time.

.. figure:: /docs/images/guis/serial-exec-plan.png
    :alt: Serial execution plan, in this case, step 1 and 2 could be run in parallel but the protocol does NOT offer
          threads to do so.

    Serial execution plan, in this case, step 1 and 2 could be run in parallel but the protocol does NOT offer threads to do so.



Parallelization
_______________

Parallelization is a technique that allows to run code at the same time (concurrently. There are 2 different ways
to parallelize a protocol in Scipion and it is decided by the developer: Scipion parallelization or 3rd party
parallelization. Parallelization is typically done using "Threads" or MPIs or both. Scipion parallelization is
only done by Threads.

3rd party parallelization
.........................

In this case the software Scipion integrates is already parallelized and typically it just needs to know how many
threads or MPI you want to use. In these cases the protocol window in Scipion shows the "parallel section" parameters
with thread and/or mpis but the execution plan (steps) are serial. The only difference with the serial execution plan
is that a certain step with call the "3rd party program" with some arguments that will tell that program to create
threads or MPIs. It is the external software the one that deals with parallelization not Scipion.

.. figure:: /docs/images/guis/external-parallelization.png
    :alt: Relion refine form and execution plan showing a serial step layout.

    Relion refine form and execution plan showing a serial step layout. Nevertheless, the form offer the field threads
    and MPI that are handled by relion

Scipion parallelization
.......................

In this case is Scipion who is doing the parallelization. The execution plan (steps) can run in parallel providing the
dependencies are met. These protocols show "Scipion threads" in the form and the execution plan should show 2 or more
branches which steps could be running at the same time.

.. figure:: /docs/images/guis/scipion-exec-plan.png
    :alt: Screenshots of aretomo form and execution plan.

    Aretomo (cryo electron tomography method) is parallelized using Scipion threads. The execution plan shows step
    1 is independent from step 2 and could run in parallel at the same time. When step 2 finishes, step 3 could while
    step 1 is still active.


----
GPUs
----
Some of the latest method use GPU acceleration. A machine/node could have GPUs installed and you may want to use one,
two or more of them. The way you specify which GPU/s to use is by its GPU ID: a number from 0 to n being n the number
of GPUs in the machine -1. If the protocol integrated allow for GPU acceleration, then you should see a field in its
form. See "Aretomo" image above have 0 in the *GPU IDs* field. This mean that aretomo will use GPU 0 for any of its steps
that may require a GPU.

Now, depending of the execution plan of the protocol, same GPU could be used in parallel at the same time. This could
be what you actually want or maybe you want to prevent this in the case of the integrated methods "need" a dedicated
GPU and does not like sharing it with "others".


.. note:: You can specify more than 1 GPUs separating them by commas or spaces: 0 1 2 or 0,1,2


Serial execution and GPUs
.........................
This is probably the simplest case. In a serial execution plan, there is NO parallelization so which ever value you enter
in the "GPUs ID" field will be used in any step.

3rd party parallelization and GPUs
..................................
This case is very much like the previous one. Since Scipion is not doing the parallelization whatever is in
the GPU filed is passed to the software integrated.

Scipion parallelization ans GPUs
................................
These case allow for more combinations. Let's start with the simplest case. You want all steps that may be running at
the same time to use the same GPU (GPU=0). Let's assume we have specify 3 threads in "Scipion threads" field. This is
1 thread for the main process and then 2 threads for processing steps.
Since we have 2 slots for threads we need 2 "slots" for GPUs. This is 0,0 or 0 0.

.. note:: If you specify write just 0 then Scipion will interpret there is only 1 slots for GPU processing so steps
    defined to use GPU will not run at the same time and parallelization of these GPU steps will not happen.

If you have 2 GPUs for the 2 threads (0 and 3, e.g.) available and you want/need to assign one per thread you can just
do: "0,3".

If you have 4 more GPUs available (0,1,2,3) you could also specify all of them and Scipion will spread evenly the GPUs
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



Void GPUs
.........
To provide more flexibility in the GPU definition we have created void GPUs. This is basically the number 99 (hope you
don't have a machine with that amount of GPUs) ;-).

If you enter that value as a GPU id it will be removed an the GPU slot will have one less GPUs.

If you enter 3 "Scipion threads" (2 for processing) and "0 1 2 99", then the fist GPU slot will serve 0 and 1 GPU and
the second will have just 2.

This will allow to use 3 GPUs (2 + 1) in method that could use 1 or 2 GPUs but you only have 3 GPUs available


GPUs in clusters
................
Scipion is unaware fo the GPU resources when running in HPC mode. Therefore, GPUs id are renumbered always starting
from 0. It does not matter if you enter "2 4 7".. it will end up being "0 1 2". It is the queue engine the one responsible
of "re-mapping" GPUs so for the program GPU 0 actually means GPU 2.

