.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _acquisition_simulation_project_for_the_ISC_course:

==================================================
Acquisition simulation project for the ISC course
==================================================


Acquisition simulation demo
----------------------------

In order to simulate a cryo-em acquisition we will run an script that, firstly, it takes movies from a data set, one by one every minute, to deposit it to the ``~/microDepositions`` folder and, secondly, it launches a Scipion pre-processing workflow to analyze the acquisition simulation in that folder.

To do that, double click to the shortcut 'Acquisition Demo' or, alternatively, go to a terminal and run

::

    sh ~/em-facilities/script.sh

This will open a form to set up the preprocessing workflow.

All the parameters in the ``Pre-processing`` section are optional and the default values are fine enough for the demo data set. However you can play setting the parameters in some way. For instance:

 * We know that the sample belongs to the ``d2`` symmetry group and this will be used to estimate the initial model, however one can introduce any other symmetry group.
 * The movies have 16 frames, thus you cat skip some of them by indicating a certain ``Frames range``.
 * The **manual picking is skipped** since we set an ``estimated particle size`` of ``250`` A, getting in this way a fully automatic workflow. However, if the estimated particle size is not know, a Manual picking is launched.
 * We can add optional protocols to estimate an initial volume such as ``Xmipp Ransac`` and/or `Eman Initial Volume` then, if some is selected, the workflow will include the ``Xmipp swarm`` protocol that finds a consensus initial volume. Note that ``Xmipp Significance`` is always used to perform an initial model.

For the **GPU usage** section, if you are running an AWS machine, you can run any of GPU protocol. Note that since all the workflow will be running at the same time in parallel, only one GPU id can be attached to one protocol.
Alternatively, if you are running Scipion in a VirtualBox machine you are not able to use GPU acceleration, therefore remain all the GPU ids at ``-1``.

Now, we are able to start the simulation acquisition by clicking on **Create New Session**.

A Scipion window should open, showing a project according to the parameters introduced in the form (it can take around 10s). A Scipion project is made of a tree of individual boxes that we call ``protocols``. Every protocol performs a single operation such as align movies, estimate CTFs, pick particles...

This project is fully scheduled, so after a while, the ``Import Movies`` protocol will start to take movies and the data will flow down to the child protocols as it is ready to be processed.

The project is continuously changing as data is flowing, then Scipion automatically updates the status of every protocol periodically. However, you can manually update the whole project by clicking on ``Refresh`` at top-right corner.

After a while, some movies will be aligned. We can see how the aligned movies looks by clicking on the ``Xmipp - corr. align.`` or ``MotionCor2 - align movies`` protocol and then, clicking on the red button ``Analyze Results``.

Afterwards, the CTF is estimated by two protocols (CTFfind4 and Xmipp) and, then, the ``Xmipp - CTF consensus`` performs a CTF quality evaluation in 3 different ways:

 * General criteria: Asserts if the defocus is in a certain range and if the astigmatism and the estimated resolution is below a certain threshold.
 * Xmipp criteria: Asserts several quality values assigned by Xmipp
 * Consensus criteria: Compare the two CTF estimations and check their compatibility.

We can view the results of every protocol by clicking on it's box and then, clicking on the red button ``Analyze Results``. Also, Scipion has implemented a ``Summary Monitor`` protocol that creates a HTML report that summarize all the relevant parameters to follow the acquisition from any web browser. You can see it by clicking on the ``Analyze Results`` > ``Open HTM Report``.

At this point, if you fixed a particle size in the form, the ``Eman - Sparx auto-pick`` have automatically picked some particles.  Alternatively, if no particle size has provided, the ``Xmipp - manual-picking`` is waiting to by launched. To launch it, ``right-click`` on the box and ``Execute``. Now, two windows are opened, one showing a micrograph and other listing the available micrographs and some parameters. Please, set a particle box size to about ``70`` pixels and pick some particles on the micrograph. Then, you can `Activate Training` to pass to a semiautomatic mode where multiple particle are automatically picked and you can refine it by adding new particles clicking and/or deleting by `shift+click` on a box. Once you are happy with the picking, click `+Coordinate` to save the results. Then, execute the `auto-picking` and the ``consensus pickings`` protocols in order to continue with the workflow.

After extracting the particles, we perform a pruning to clean a bit the particles set following statistic analysis. Note that since the statistical analysis needs a certain among of particles, we include a trigger protocol that waits until a certain number of particles is reached to automatically continue with the workflow.

Since the 2D classifications protocols need a certain among of particles and a static input, the `trigger data to classify` waits until a certain number of particles is reach to release a closed set of particles to fed the classifiers.

Until here, the acquisition takes from 5 minutes to 10 minutes for the 10 demo movies. However, due to the limited resources that we have in VirtualBox, we are not able to continue with the classification and the initial model estimation in an optimal way (it will take 3-5 hours). However, we can open an already processed project to see how it would have continue. Therefore, close the project by clicking on the ``Project`` > ``Exit``.


Acquisition simulation project
------------------------------

To open the already processed project, launch Scipion from the shortcut and choose the 'Acquisition_Simulation' project, then a Scipion window should be opened showing the project.

In this project, we have labeled/colored the protocols by sections. You can change the color mode by ``Project`` > ``Toogle color mode`` or ``ctrl+t``. Even, you can add/edit labels clicking on ``Project`` > ``Manage project labels`` or ``right-click`` on a protocol and click ``labels`` to attach a label to a protocol.

In this case, two particles picking have been used, the ``Eman - Sparx auto-pick`` and the ``Xmipp - manual-picking``. And two ``consensus pickings`` have been performed, one with the junction of the two pickings (OR) and other with all those particles that coincides in both pickers (AND).

Since the 2D-classifyers work with a static set of particles, the ``Xmipp - triger data to classify`` ensures that a certain among of particles is ready and then, a closed set of particles is given to fed the classifiers. We have added two independent methods to classify, one from Relion and the other from Xmipp.

The ``Auto-class selection`` takes those averages that seems fine to be used to fed the initial model protocols. Then, the ``Xmipp - swarm init. vol.`` performs a consensus between the ``Eman - initial vol.``, ``Xmipp - Recons. significans`` and ``Xmipp - Ransac`` to give an initial volume.

Finally, to keep monitoring the incoming particles coming from the new acquired movies, ``Scipion - streamer`` is launching several ``Relion - 2D classifying`` in batches.
