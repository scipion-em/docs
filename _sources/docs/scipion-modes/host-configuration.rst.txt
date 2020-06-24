.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _host-configuration:

==================
Host configuration
==================

In Scipion the configuration file ``scipion/config/hosts.conf`` contains
some properties of the execution machine. (In a future release we are
planning to allow more than one machine to be configured and used to
launch jobs). This configuration file is particularly important for
clusters that use a Queue System. In this scenario, it is common that
users should write a submission script to launch jobs to the cluster. In
Scipion the submission scripts are generated from a template (that is
setup once by the system administrator) and the users no longer need to
care about it. In the following sections you can find the definition of
those parameters and also some examples that you can use as a starting
point.


Parameters:
===========

MPI command
-----------

::

    [localhost]
    PARALLEL_COMMAND = mpirun -np %_(JOB_NODES)d -bynode %_(COMMAND)s


This variable reflects how to run programs using MPI in you computer.
This variable should be set even if you are not using a cluster (for
example in a multi-core machine). ``JOB_NODES`` will be replaced by the
number of MPI selected by the user in the form and the ``COMMAND`` with the
job launched by Scipion. This two should not be modified. In this
example we are using two parameters of MPI in our computer: ``--np`` and
``--bynode=``.


Queue System
------------


When you run a protocol with ``Use queue = Yes`` the actual job
description file is created in the logs directory. For example,
``ScipionUserData/projects/MyProject/Runs/000162_ProtCTFFind/logs/3162.job``.
You can take a look at this file to see if everything is properly
defined (according to the requirements of your queue system) Following
is a description of each of the variables:

::

    NAME = SLURM
    MANDATORY = 4

With the NAME variable you can specify the name of your Queue System
(only a descriptive variable) that should not be empty. ``MANDATORY`` can be
set to an integer number, it specify the number of processors from which
is mandatory to launch the jobs through the queue. (NOTE: ``MANDATORY = 0``
means no restriction, old configuration use False which is equivalent to
0)

::

    SUBMIT_PREFIX = run

The ``SUBMIT_PREFIX`` var is optional. It adds a prefix to the generated
submit script, for example: ``run178.job``. The default is to use only the
id as 178.job, but this causes problems in some clusters.

::

    SUBMIT_COMMAND = sbatch %_(JOB_SCRIPT)s
    CANCEL_COMMAND = scancel %_(JOB_ID)s
    CHECK_COMMAND = squeue -j %_(JOB_ID)s


The previous variables are used to specify how to submit, cancel and
check jobs, respectively. In this case ``JOB_ID`` will be provided by
Scipion as well as the generated job file (``JOB_SCRIPT``). The examples
here are from Slurm, for Torque/PBS the commands are:
``qsub, qdel, qstatus``.

::

    SUBMIT_TEMPLATE =

The ``SUBMIT_TEMPLATE`` variable contains the template that will be used to
generate the job script file. It can contains some special variables
that will be replaced by Scipion. Some of this variables can be specific
to your own queues and system, that should be defined in the ``QUEUES``
variable. It is important that the lines of the template should be
indented so there are correctly associated to this variable. See the
examples in the next sections.

::

    QUEUES = {
        "myslurmqueue": [
            ["JOB_MEMORY", "8192", "Memory (MB)", "Select amount of memory (in megabytes) for this job"],
            ["JOB_TIME", "120", "Time (hours)", "Select the time expected (in hours) for this job"],
            ["GPU_COUNT", "1", "Number of GPUs", "Select the number of GPUs if protocol has been set up to use them"],
            ["QUEUE_FOR_JOBS", "N", "Use queue for jobs", "Send individual jobs to queue"]]
        ]
    }

The ``QUEUES`` variable should contain the different queues that can be
used. It should be written as a JSON dictionary, where the key is the
queue name and the value is a list of parameters. Each parameter is
composed by a list of 4 values:

 1. Variable Name, that can be used in the template to be replaced
 2. The default value The variable
 3. The variable label that will be shown to the users in the GUI
 4. A help message that users can use to know the meaning of this queue parameter.

Keep in mind that the parameters defined here (like ``JOB_TIME``, in the example) will be returned from the GUI
dialog as a string. Hence, in the template you will need to declare them as string (%s), even if they are integers (%d).
See the Torque example (``JOB_HOURS`` parameter).

The ``GPU_COUNT`` variable is only needed if the queue is configured to manage GPUs (for instance in slurm).

The ``QUEUE_FOR_JOBS`` variable is needed if you want to give the possibility to submit single jobs to the queue (by default Scipion submits the whole protocol run to the queue as a single job). The other variable involved in this mode is JOB_DONE_REGEX which is used to check for finished jobs. If unset (not in the config) then jobs are considered finished when the CHECK_COMMAND returns nothing (for instance, slurm). If the batch system returns some string that needs to be parsed to check the job status then use this variable to specify the regular expression to check for finished jobs. This check is done every 3 seconds making this kind of submission slower for fast jobs.

::

    QUEUES_DEFAULT = {"JOB_GPUS": "0" }

The ``QUEUES_DEFAULT`` variable is optional. It is only useful if you have
configured more than one queue, and some of the queue have distinct
parameters than the others. In this case, you need to provide a default
value (to be used in the template script) when other queues are
selected. The values must be set with the Key = Value inside braces.


Example configurations
======================

Example for `Slurm <http://slurm.schedmd.com/slurm.html>`__
-----------------------------------------------------------

`Here <https://thehatteronline.com/2014/11/18/turn-your-workstation-into-a-mini-grid-with-slurm>`__
you can find a very simple tutorial about installing Slurm in Ubuntu.

::

    [localhost]
    PARALLEL_COMMAND = mpirun -np %_(JOB_NODES)d -bynode %_(COMMAND)s
    NAME = SLURM
    MANDATORY = False
    SUBMIT_COMMAND = sbatch %_(JOB_SCRIPT)s
    CANCEL_COMMAND = scancel %_(JOB_ID)s
    CHECK_COMMAND = squeue -h -j %_(JOB_ID)s
    SUBMIT_TEMPLATE = #!/bin/bash
        ### Inherit all current environment variables
        #SBATCH --export=ALL    
        ### Job name
        #SBATCH -J %_(JOB_NAME)s
        ### Outputs (we need to escape the job id as %_j)
        #SBATCH -o %_(JOB_LOGS)s.out
        #SBATCH -e %_(JOB_LOGS)s.err
        ### Partition (queue) name
        ### if the system has only 1 queue, it can be omited
        ### if you want to specify the queue, ensure the name in the scipion dialog matches
        ### a slurm partition, then leave only 1 # sign in the next line
        ##### SBATCH -p %_(JOB_QUEUE)s

        ### Specify time, number of nodes (tasks), cores and memory(MB) for your job
        #SBATCH --time=%_(JOB_TIME)s:00:00 --ntasks=%_(JOB_NODES)d --cpus-per-task=%_(JOB_THREADS)d --mem=%_(JOB_MEMORY)s           --gres=gpu:%_(GPU_COUNT)s
        # Use as working dir the path where sbatch was launched
        WORKDIR=$SLURM_SUBMIT_DIR

        #################################
        ### Set environment varible to know running mode is non interactive
        export XMIPP_IN_QUEUE=1

        cd $WORKDIR
        # Make a copy of node file
        echo $SLURM_JOB_NODELIST > %_(JOB_NODEFILE)s
        # Calculate the number of processors allocated to this run.
        NPROCS=`wc -l < $SLURM_JOB_NODELIST`
        # Calculate the number of nodes allocated.
        NNODES=`uniq $SLURM_JOB_NODELIST | wc -l`

        ### Display the job context
        echo Running on host `hostname`
        echo Time is `date`
        echo Working directory is `pwd`
        echo Using ${NPROCS} processors across ${NNODES} nodes
        echo NODE LIST - config:
        echo $SLURM_JOB_NODELIST
        echo CUDA_VISIBLE_DEVICES: $CUDA_VISIBLE_DEVICES
        #################################
        # echo '%_(JOB_COMMAND)s' >> /tmp/slurm-jobs.log
        %_(JOB_COMMAND)s
        find "$SLURM_SUBMIT_DIR" -type f -user $USER -perm 644 -exec chmod 664 {} +

    QUEUES = {
        "tesla": [["JOB_MEMORY", "8192", "Memory (MB)", "Select amount of memory (in megabytes) for this job"],
                  ["JOB_TIME", "120", "Time (hours)", "Select the time expected (in hours) for this job"],
                  ["GPU_COUNT", "1", "Number of GPUs", "Select the number of GPUs if protocol has been set up to use them"],
                  ["QUEUE_FOR_JOBS", "N", "Use queue for jobs", "Send individual jobs to queue"]],
        "geforce": [["JOB_MEMORY", "8192", "Memory (MB)", "Select amount of memory (in megabytes) for this job"],
                    ["JOB_TIME", "120", "Time (hours)", "Select the time expected (in hours) for this job"],
                    ["GPU_COUNT", "1", "Number of GPUs", "Select the number of GPUs if protocol has been set up to use them"],
                    ["QUEUE_FOR_JOBS", "N", "Use queue for jobs", "Send individual jobs to queue"]],
        "quadro": [["JOB_MEMORY", "8192", "Memory (MB)", "Select amount of memory (in megabytes) for this job"],
                   ["JOB_TIME", "120", "Time (hours)", "Select the time expected (in hours) for this job"],
                   ["GPU_COUNT", "1", "Number of GPUs", "Select the number of GPUs if protocol has been set up to use them"],
                   ["QUEUE_FOR_JOBS", "N", "Use queue for jobs", "Send individual jobs to queue"]]
    }



Example for Torque-PBS
----------------------

::

    [localhost]
    PARALLEL_COMMAND = mpirun -np %_(JOB_NODES)d -bynode %_(COMMAND)s
    NAME = PBS/TORQUE
    MANDATORY = False
    SUBMIT_COMMAND = qsub %_(JOB_SCRIPT)s
    SUBMIT_TEMPLATE = #!/bin/bash
            ### Inherit all current environment variables
            #PBS -V
            ### Job name
            #PBS -N %_(JOB_NAME)s
            ### Queue name
            ###PBS -q %_(JOB_QUEUE)s
            ### Standard output and standard error messages
            #PBS -k eo
            ### Specify the number of nodes and thread (ppn) for your job.
            #PBS -l nodes=%_(JOB_REAL_NODES)s:ppn=%_(CPUS_PER_NODE)s
            ### Tell PBS the anticipated run-time for your job, where walltime=HH:MM:SS
            #PBS -l walltime=%_(JOB_HOURS)s:00:00
            # Memory per node
            #PBS -l mem=%_(JOB_MEM)sg
            # Use as working dir the path where qsub was launched
            WORKDIR=$PBS_O_WORKDIR
            #################################
            ### Set environment varible to know running mode is non interactive
            export XMIPP_IN_QUEUE=1
            ### Switch to the working directory;
            cd $WORKDIR
            # Make a copy of PBS_NODEFILE
            cp $PBS_NODEFILE %_(JOB_NODEFILE)s
            # Calculate the number of processors allocated to this run.
            NPROCS=`wc -l < $PBS_NODEFILE`
            # Calculate the number of nodes allocated.
            NNODES=`uniq $PBS_NODEFILE | wc -l`
            ### Display the job context
            echo Running on host `hostname`
            echo Time is `date`
            echo Working directory is `pwd`
            echo Using ${NPROCS} processors across ${NNODES} nodes
            echo PBS_NODEFILE:
            cat $PBS_NODEFILE
            #################################
            %_(JOB_COMMAND)s
    CANCEL_COMMAND = canceljob %_(JOB_ID)s
    CHECK_COMMAND = qstat %_(JOB_ID)s
    QUEUES = { "mypbsqueue": [ ["JOB_HOURS", "120", "Time (hours)", "Select the expected job time"], ["JOB_REAL_NODES", "1", "Nodes", "How many nodes the job needs"], ["CPUS_PER_NODE", "8", "CPUs", "How many CPUs/node to use"], ["JOB_MEM", "16", "Memory (GB)", "Define the memory per node for the job"] ] }



Example for SGE
---------------

This example is based on a config originally adapted by `HPC@POLITO <http://www.hpc.polito.it/>`_ .

::

    [localhost]
    PARALLEL_COMMAND = mpirun
    MANDATORY = False
    NAME = SGE
    CANCEL_COMMAND = /opt/sge6/bin/linux-x64/qdel %_(JOB_ID)s
    CHECK_COMMAND = /opt/sge6/bin/linux-x64/qstat -j %_(JOB_ID)s
    SUBMIT_COMMAND = /opt/sge6/bin/linux-x64/qsub %_(JOB_SCRIPT)s
    SUBMIT_TEMPLATE = #!/bin/bash
        ###====================================================###
        #$ -V
        #$ -S /bin/bash
        #$ -cwd ### Use the current working directory
        #$ -N scipion%_(JOB_NAME)s ### Job name
        #$ -q %_(JOB_QUEUE)s ### Queue name
        #$ -pe %_(JOB_PE)s %_(JOB_SLOTS)s
        #$ -j y ### Merge stdin and stdout
        ###=======================================================#
        #$ -l h_rt=%_(JOB_HOURS)s:00:00 ### Max run Time
        #$ -l vf=%_(JOB_MAX_MEM)sG
        ###=====================================================###

        %_(JOB_COMMAND)s

    QUEUES = {
            "ogequeue": [
                 ["JOB_QUEUE","all.q","Queue Name:","Select the target queue"],
                 ["JOB_SLOTS","16","Total cores:","(MPI tasks x threads)"],
                 ["JOB_PE","orte", "Parallel Environment (PE):","Select the OGE Parallel Environment)"],
                 ["JOB_HOURS","120", "Hours:","Maximum amount of time allowed for this job"],
                 ["JOB_MAX_MEM","64","Mem(GB/node):","Set the memory per node that this job needs"]
              ]
        }
