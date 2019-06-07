.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _acquisition-simulation:

=======================
Tutorial for Facilities
=======================

This tutorial try to put into practice the previous facilities sections
by means of a demo which simulates a cryo-EM acquisition.

The demo will be made of the following 5 logical steps:

1. `Taking movies from a data set to deposit it in a simulated deposition
   directory <acquisition-simulation#id1>`_, one by one every a certain
   time step.
2. `Launching a wizard <acquisition-simulation#id2>`_ asking for some
   parameters that the user can set.
3. `Creating the workflow <acquisition-simulation#id3>`_ according to that user and config parameters.
4. `Launching and opening that workflow <acquisition-simulation#id4>`_.
5. `Customize the HTML report <customize-html-report>`_.

Notice that these 4 steps are independent one each other. In addition,
each of them can be done in different ways and, this demo wants to be just an
example of how to do them. However, we will give hints of alternative procedures.

To be able to run this acquisition demo, a set of scripts from our
`em-facilities script-sharing repository <https://github.com/I2PC/em-facilities>`_
are needed, thus

.. code-block:: bash

    git clone https://github.com/I2PC/em-facilities


0. Config file
--------------

First of all, it is very useful to have a file where to store some parameters
which usually remains constant for a certain configuration/system/PC/facility.
We call this file as **config file**.

For this acquisition demo, the
`usingAPI-demo/scipionbox.conf <https://github.com/I2PC/em-facilities/blob/master/usingAPI_demo/scipionbox.conf>`_
file in the cloned repository contains

.. code-block:: bash

    [GLOBAL]
    DEPOSITION_PATH = ~/microDepositions
    PATTERN = *.mrcs
    GAIN_PAT = gain.mrc
    SCIPION_PROJECT = ~/ScipionUserData/projects
    SIMULATION = True
    RAWDATA_SIM = ~/ScipionUserData/testData/betagalMovies
    NUM_CPU = 64

    [MICROSCOPE]
    AMP_CONTR = 0.1
    SPH_AB = 2.7
    VOL_KV = 300
    SAMPLING = 0.637
    TIMEOUT = 1*60
    INV_CONTR = True
    PARTS2CLASS = 3000

We can see two sections *Global* and *Microscope* getting the following parameters.

* *Global*:
    * *DEPOSITION_PATH*: Where Scipion will find movies
    * *PATTERN*: The bash pattern that all movies have to match to be imported
    * *GAIN_PAT*: The bash pattern that the gain must match to be used (it must
      also be at the *deposition path*)
    * *SCIPION_PROJECT*: Where to store the Scipion project
    * *SIMULATION*: If `True`, a simulation is perform by means of copying files
      from *RAWDATA_SIM* to *DEPOSITION_PATH* every certain time. If `False`, no
      simulation is done and *DEPOSITION_PATH* is expected to be automatically full.
    * *RAWDATA_SIM*: A data set to be used for the simulation (if `True` in the
      previous point)
    * *NUM_CPU*: Number of CPUs to optimize the workflow

* *MICROSCOPE*:
    * *AMP_CONTR*: Amplitude contrast of the microscope.
    * *SPH_AB*: Spherical aberration of the microscope (in *mm*).
    * *VOL_KV*: Working microscope voltage (in *kV*).
    * *SAMPLING*: Sampling rate (in *A/px*).
    * *TIMEOUT*: General time out for the streaming mode and, if *SIMULATION* is
      `True`, the simulated acquisition rate (in *s*).
    * *INV_CONTR*: If `True` a contrast inversion is done before picking.
      If `False`, no inversion of contrast is done.
    * *PARTS2CLASS*: Number of particles to wait before to perform a 2D classification
      of a first batch.

If you think that some of this parameters are not so constant, you could not
include it and, then ask for it in posterior step (in the second step of this
tutorial). Also, here we have include some workflow dependent parameter such as
the *PART2CLASS*. You are free to put more or less parameters here, just have
in mind that are parameters rarely change from one acquisition to the next.


1. Acquisition simulation
-------------------------

This point is just to periodically get movies. Nothing else. If you intend to
run in a real acquisition, you can skip this point.

The script `usingAPI-demo/simulate_acquisition.py <https://github.com/I2PC/em-facilities/blob/master/usingAPI_demo/simulate_acquisition.py>`_
in the cloned repository

.. code-block:: bash

    Usage: simulate_acquisition.py INPUT_PATTERN OUTPUT_FOLDER [GAIN_FILE] [DELAY]

            INPUT_PATTERN: input pattern matching input files.
            OUTPUT_FOLDER: where to create the output links.
            [GAIN_FILE, default None]: gain file will be linked at the beginning
            [DELAY, default 30]: delay in seconds between file appearance

makes symbolic links of those files matching *INPUT_PATTERN* to *OUTPUT_FOLDER*
every *DELAY* seconds. If a *GAIN_FILE* is found, it is linked first.


2. Wizard for user parameters
-----------------------------

Every acquisition have singularities from the others. They can be from the sample,
from the user preferences, from the EM operator preferences, from the resources
availability or, even, from the microscope state. Then, we should have some
flexibility to process the sample, but first of all, we need to know this
singularities.

In this demo, we have re-used the GUI code in Scipion for creating a wizard to
ask for all these parameters that can be different from one acquisition to the
other. We refer to that parameters as *user parameters*. However, every facility
can develop its own way to retrieve these (or others) parameters.

That code of this wizard can be found in
`usingAPI-demo/form_launcher.py <https://github.com/I2PC/em-facilities/blob/master/usingAPI_demo/form_launcher.py>`_
in the cloned repository.

We have design this script in four logical steps:

* `Reading the config file <https://github.com/I2PC/em-facilities/blob/8a31f7f5eed3dc73443266272c40b1da6432135d/usingAPI_demo/form_launcher.py#L470-L510>`_.
* `Creating the wizard window using some Scipion-tKinter classes as base <https://github.com/I2PC/em-facilities/blob/8a31f7f5eed3dc73443266272c40b1da6432135d/usingAPI_demo/form_launcher.py#L49-L133>`_.
* `Filling the wizard with the fields <https://github.com/I2PC/em-facilities/blob/8a31f7f5eed3dc73443266272c40b1da6432135d/usingAPI_demo/form_launcher.py#L135-L230>`_.
* `Retrieving the parameters <https://github.com/I2PC/em-facilities/blob/8a31f7f5eed3dc73443266272c40b1da6432135d/usingAPI_demo/form_launcher.py#L235-L394>`_.

The wizard can be launched by running

.. code-block:: bash

    scipion python em-facilities/usingAPI-demo/form_launcher.py

.. figure:: /docs/images/facilities-API-wizard.png
   :align: center
   :width: 900
   :alt: facilities API wizard


All the default values in the **Pre-processing** section (also in the *scipionbox.conf*)
are thought to be use with the beta-galactosidase sample (EMPIAR 10061).
However, you can play setting the parameters in some way or adjusting them
to your single data.

For instance:

* We know that this sample belongs to the `d2` **symmetry group** and
  this will be used to estimate the initial model, however one can introduce any
  other symmetry group.
* This movies have 16 frames, thus you cat skip some of them by indicating a
  certain **Frames range**.
* If a certain **Number of mics to manual pick** is set, the workflow will wait
  until this number is reach before launching the manual picker. In 0 is set,
  only automatic picking is done and the particle size is estimated by Xmipp.
* We can add optional protocols, such as *Optical flow* to do a high order local
  movie alignment, Eman2-Sparx to automatic picking, or adding more initial
  volume reconstruction methods to the *Xmipp swarm init. vol. consesus* protocol,
  such as *Xmipp Ransac* and/or *Eman Initial Volume*.
  Note that *Xmipp Significance* is always used to estimate the initial model.

For the **GPU usage** section, note that all the workflow will be running at the
same time in parallel, then only one GPU id can be attached to one protocol.

Now, we are able to start the simulation acquisition by clicking on
**Create New Session**.


3. Creating custom workflows
----------------------------

Once we know all the parameters that will be used, we must create the workflow
accordingly. At this point there are two options:

* Fill a *JSON* file with all the protocols parameters accordingly with the
  previous section.
* Use the Scipion's API to create a new project and adding every protocol
  accordingly to the previous section.

You can code a script to fill a *JSON* according to what Scipion expect.
Although, a good option to go with the *JSON* way is to choose a certain
*JSON* file from a stored set according to the user answers.

However, in this tutorial we have choose to develop a Python script using the
Scipion's API to create the project and to add all the protocols according to
the wizard described in the previous section.

See `how to create workfows with the API <facilities-API-demo>`_ to continue.


4. Launch an open projects
--------------------------

Launch a project
================

See `launching JSON workflows <facilities-workflows.html#static-templates>`_ if
you crated a JSON file.

If the protocols included in the workflow made in the previous section are save
instead of launched, we must to launch the whole workflow at once by

.. code-block:: bash

    scipion python $SCIPION_HOME/pyworkflow/project/scripts/schedule.py projectName

where `projectName` is the name of the project made in the previous section.
Alternatively, the whole workflow can also be launch from the GUI by selecting
the `Import` and *right-click > Restart workflow*.

Note that if the protocols have been launched during the workflow creation, this
step must be skipped.

Open a project
==============

To open a project you can either open Scipion GUI and choose the project from the
project window or just run

.. code-block:: bash

    scipion project projectName


5. Customize the HTML report
----------------------------

This section is in `this specific page <customize-html-report>`_.



