.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _release-notes:

=======================
Release-notes
=======================

.. contents:: Table of Contents


v2.0 (2019-05-16) Diocletian
============================

Release Notes
-------------
We are pleased to announce the new major release of version Scipion 2.0.
It is available for download on Linux `here <http://scipion.i2pc.es/download_form>`_

Scipion is now a plugin framework. This will speed up the release of new packages
or new updates without the need of releasing a new Scipion version.

We added several new features, made improvements and fixed bugs.
We are also very happy to see the Scipion development becoming more distributed.
The main developers team is in Madrid, but now core developers are also in
Stockholm, Montreal and Cambridge. We will be really happy to have more people
on-board, come and join us!

Key changes for version 2.0 are:
--------------------------------

* Pluginization: each EM package is now a plugin developed and updated
  independently from Scipion core. This is a first step towards making Scipion
  even more modular and easy to use and install for both users and developers.
  The new repository hosting official plugins is now `here <https://github.com/scipion-em>`_

  For your convenience we have developed a Plugin Manager which provides an easy
  GUI to manage plugins and associated binaries. We already have over 30 plugins
  including several new ones, such as 3DFSC, CryoEF, Cryolo, EMPIAR depositor
  and others. For more information on each plugin consult its corresponding
  repo and/ or developers.

* Almost all existing EM packages were updated, such as RELION3, EMAN2.21,
  Gctf 1.18, SPIDER 25.02, Motioncor2-1.2.1 and others.

* Model building tools from CCP4, Chimera, Phenix and powerfit have been added.
* Several improvements for streaming: multi-GPU jobs distribution, more protocols supporting batch processing, jobs scheduling, new XMIPP streaming protocols (movie maxshift, ctf consensus, GL2D classification on GPU etc.)
* Multiple workflow usability and GUI improvements as well as bug fixes for several tasks.
* For developers and facility managers we now have a slack workspace where you can easily reach other developers and facility staff to get a quick feedback: https://scipion.slack.com/. Contact us at scipion@cnb.csic.es for an invitation.

Streaming
----------
1. New protocol from Xmipp to trigger data (movies, micrographs, particles...) only when a certain among of that data is reached, in three modes: in batches, full streaming, from streaming to static.
2. Xmipp Movie Alignment is updated to work on GPU and to do local Alignmen by means of an splines fit.
3. New protocol to select/discard movies on-the-fly depending on the shift jumps between frames or/and the total travel drift.
4. Batch support for CTF estimation protocols.
5. CTF selection and CTF discrepancy from Xmipp are merged on the CTF consensus in order to select/discard CTFs on-the-fly depending on three assertions types: common parameters (defocus range, resolution, astigmatism...), Xmipp criteria and discrepancy with an auxiliar CTF estimation.
6. New protocol from Xmipp to automatically estimate the particle size.
7. CRYOLO automatic picking from Sphire now is available.
8. Now the protocol extract coordinates is ready to follow streaming processing.
9. New protocol to eliminate/select empty particles/classes in streaming processing.
10. New GL2D protocol from Xmipp for 2D classificantion in streaming mode in two modes: static (when a particle is assigned to a class, it remains there), full streaming (continuosly updating the classes and re-assigning particles).
11. More streaming methods available...

New protocols & package updates
--------------------------------
1. EMPIAR depositor.
2. Cryolo picker from SPHIRE.
3. EMAN2 updated to 2.21, new protocols added: new boxer (interactive and autopicker), ctf_auto, refine 2d and ref2d bispectra, tilt validation.
4. Relion 3.0 and associated protocols.
5. SPIDER 25.02: projection matching refinement without defocus groups (“gold-standard”).
6. Grigoriefflab: ctftilt program added.
7. XMIPP 3.19.04: align volume and particles, center particles, compare angles, GL2D (streaming and static), consensus classes 3D, 2D kmeans clustering, CTF consensus, deep consensus picking, deep denoising, directional ResDir, eliminate empty classes/particles, extract unit cell, generate reprojections, local MonoTomo, metaprotocol heterogeneity, movie maxshift, particle boxsize, screen deep learning, significant heterogeneity, swarm consensus intial volumes, split volume, trigger data…
8. Motioncor2: updated to version 1.2.1, added gain rotation/flip options. Motioncor/dosefgpu is deprecated.
9. New 3D FSC (https://github.com/nysbc/Anisotropy) and cryoEF (https://www.mrc-lmb.cam.ac.uk/crusso/cryoEF/) protocols.
10. Locscale: computes contrast-enhanced cryo-EM maps by local amplitude scaling using a reference model
11. New model building module, including several protocols from different packages: extract unit cell protocol (XMIPP) to isolate the smallest asymmetrical subunit of the map; Chimera model from template, to get the initial structure from a sequence based on Modeler web server and sequence homology, and other Chimera-derived protocols to handle structures and perform intermediate operations, such as Chimera operate and Chimera restore-session, as well as the operator protocol of Atomstructutils; Chimera rigid fit and Powerfit protocols allow to accomplish rigid fitting of structures in maps; Coot refinement and Refmac protocols, from CCP4, and real space refinement protocol, from Phenix, implement the process of flexible fitting and refinement; EMRinger and MolProbity Phenix protocols have been added to validate the final structure generated; the analysis of this structure is simplified with superpose pdbs protocol, from Phenix, and Chimera contacts protocol, that computes interactions among structure chains; the Scipion protocol export to EMDB has been modified to facilitate the submission of map and its derived structure.

Other improvements and bug fixes
--------------------------------
1. Protocol tree is now auto-generated from protocols.conf of each plugin.
2. HTML report of streaming monitor polished: added phase shift, time series
   plot of CTF parameters, load thumbnails only on request
   (`#1963 <https://github.com/I2PC/scipion/issues/1963>`_,
   `#1460 <https://github.com/I2PC/scipion/issues/1460>`_,
   `#1443 <https://github.com/I2PC/scipion/issues/1443>`_,
   `#1366 <https://github.com/I2PC/scipion/issues/1366>`_).
3. Added functions to restart/continue project workflow.
4. Scheduling has been improved dealing better with exceptions and non streaming protocols.
5. Protocols output refactored: now the can output/input scalar objects. Discovering outputs have been sped up (`#1810 <https://github.com/I2PC/scipion/issues/1810>`_).
6. Added QueueStepExecutor: an alternative way to execute jobs in a queue system that sends only the actual package command (e.g. relion_refine) instead of the whole protocol run (`#1807 <https://github.com/I2PC/scipion/issues/1807>`_).
7. More versatile way to blacklist files during import: by regular expressions, by date, set exclusion or just a plain black list (`#1702 <https://github.com/I2PC/scipion/issues/1702>`_).
8. Gctf refinement protocol is now split into multiple steps (`#1748 <https://github.com/I2PC/scipion/issues/1748>`_).
9. Deprecation of motioncor1, igbmc gEMpicker, cryoem, ctffind3 (in progress, `#1813 <https://github.com/I2PC/scipion/issues/1813>`_).
10. Libtiff updated to version 4 to support files over 4Gb from SerialEM (`#1837 <https://github.com/I2PC/scipion/issues/1837>`_).
11. MRC 4-bit support (`#1401 <https://github.com/I2PC/scipion/issues/1401>`_).
12. Add run ID to input list of objects (`#928 <https://github.com/I2PC/scipion/issues/928>`_).
13. Gain reference files can be used in dm4 format directly (`#1000 <https://github.com/I2PC/scipion/issues/1000>`_).

    ...

And many more minor features and bug fixes! ;)


v1.2.1 (2018-10-01) Claudio
===========================

Release Note
-------------

We are pleased to announce another release of Scipion, v1.2.1 is now available! We added several new features, made improvements and fixed bugs, specially for on-the-fly data processing.

We are also very happy to see the Scipion development becoming more distributed. The main developers team is in Madrid, but now core developers are also in Stockholm, Montreal and Cambridge. We will be really happy to have more people on-board, come and join us!

For the next release, we are going for a more strong “pluginization”, to make the whole platform more easy to maintain and the development more agile. Stay tuned and keep an eye!

New for Streaming
------------------

* Allow protocols to run in multiple GPUs (e.g Gctf and Gautomatch)
* Protocols can now wait for other protocols to finish before starting (internal scheduling)
* Allow some protocols to "wait" and work in "batch" mode to reduce the IO operations in fast protocols (while checking for updates in the stream).
* Schedule batch of 2D classification jobs one after each other (protocol '2d streamer')

New protocols
---------------
* `Local sharpening protocol in Xmipp <https://github.com/I2PC/scipion-em-xmipp/wiki/XmippProtLocSharp>`_
* Added cryomethods package added from McGill developers.

* New volume selector protocol: produces and selects the best initial map automatically.

* Relion protocol to center averages (center of mass in relion_image_handler)
* Protocol to export particles in Relion format (both .star file and stacks)

Other improvements and bug fixes
----------------------------------
* Monores Xmipp protocol to estimate local resolution has been accelerated.
* Allow to merge sets with different attributes
* Use double-click to select in Dialogs (more intuitive)
* Allow to quickly rename a protocol label (rigth-click -> Rename option)
* CTFModel now allows to have phaseShift information as part of the model
* Picking wizard now allows to pick all micrographs at once (more efficient in some programs)
* Bug fixed in Relion particles-extraction when using not integer scale
* Fixed bug in Relion autopick protocol when downscaling in streaming
* Allow to provide references for 2D and 3D classification
* Allow to pass the calibrated pixel size in Relion postprocess protocol
* Relion auto-pick can use batch steps
* Relion extract-particles re-factored, now in with batch mode and unified with non-streaming.
* Mask 3D protocol was updated (labels and help) and test added
* Re-factoring Gautomatch to use bad coords in streaming
* Update and test Motioncor2-1.1.0 (mainly update help for new options)


v1.2 (2018-04-03) Caligula
==========================

Release note
------------
We are very pleased to announce the release of a new version of `Scipion <http://scipion.i2pc.es/>`_. We have put our efforts in improving the Streaming functionality to work better in facilities. We have also updated some EM packages versions and done some bug-fixing and enhancements.

New features
-------------
Picking and particle extraction in streaming
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
We have pushed our streaming capabilities until particle extraction, this means
that all pickings (not manual one of course) can run in streaming mode and the
particle extraction can be done also on the fly. Yep...we are getting closer to
have 2D classification and rough initial model on the fly.

HTML Summary report redesigned
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
We have revisited our HTML report and have polished it. We've added a table
with details and images per micrograph/ctf, a defocus coverage chart and a
resolution histogram. Check the latest
version `[here] <http://scipion.cnb.csic.es/scipionbox/lastHTMLReport/>`_

Improved CTF model
~~~~~~~~~~~~~~~~~~~~~~
We have added phase shift, max. resolution and CTF fit quality as global
parameters to our Scipion CTF model. Old package-specific parameters are still
kept for compatibility with previous versions.

EM Packages
~~~~~~~~~~~
* Added Relion v2.1.0 support: several new options in refinement & classification
  protocols, new local resolution, initial model and symmetry expansion protocols,
  refactored particle polishing protocol
* Added dark/gain reference correction to Unblur protocol
* Motioncor2 package updated to version 1.0.5. Also, now input tif files are
  read directly by the program without any conversion. Moreover, we have fixed the
  bug causing wrong drift plots.

Others
~~~~~~
* New protocol (*xmipp3 - ctf selection*) to make a selection of meaningful CTFs
  based on the defocus values, the astigmatism, and the resolution
* New protocol (*scipion - average frames*) for computing raw frame averages
  (for simple diagnosis, nothing else)
* New protocol (*scipion - picking difference*) to compute the difference
  between a reference SetOfPartices and another set (usually a negative reference).
* Further improvements of streaming protocols:

    * Do not import files that are already imported (when continuing or restarting a stopped/failed streaming protocol)
    * Possibility to schedule jobs that link to previous unfinished ones (still in development, now available only when you import a Scipion workflow - json file)

* Improved the performance during input set selection, especially when a lot of SetOfClasses2D/3D where generated by several runs of Relion
* Python version updated to 2.7.14
* New scripts:

    * *create_project.py* script to create a project from a Scipion workflow file (json),
    * *schedule_project.py* to schedule all protocols given a project name (already existing project)
    * *edit_workflow.py* allows to edit a json workflow using the same project GUI

* File browser now has shortcuts as well as Search function and keyboard navigation
* Shorting protocol names: now when you copy a protocol, the new name will be *oldName (copy N)*, where N is a number

v1.1 (2017-06-14) Balbino
=========================

Release note
-------------

We are very pleased to announce the release of a new version
of `Scipion <http://scipion.i2pc.es>`_. It’s been over a year since the previous
and first version and we have been working on 3 main goals for this release:

* Consolidation: We put and will always put our best effort into making Scipion a robust and reliable software. We have improved performance, usability and fixed multiple bugs.
* EM packages integration: We have updated several EM packages to their latest versions (relion 2.0.4) and added new ones (motioncor2, gctf, gautomatch, …). Single movie alignment protocol (as in Scipion 1.0) has been split into several ones for each program.
* Streaming capabilities: To speed up first preprocessing steps we have enabled Scipion to work in “streaming mode”, allowing users to compute aligned movies and estimate CTF as soon as a movie or micrograph comes out of the microscope PC.

New features
=============

EM Packages
-----------

Xmipp
~~~~~~
Xmipp has also been greatly improved and many new methods have been added. Please see link: `xmipp release notes <xmipp-release-notes>`_  for details.

`Ethan picker <http://www.sciencedirect.com/science/article/pii/S1047847700942795>`_
Automated detection of spherical particles from electron micrographs.

`gAutomatch <http://www.mrc-lmb.cam.ac.uk/kzhang/Gautomatch/>`_
GPU-accelerated particle picking program developed by K. Zhang allows template-based and “gaussian-blob”  (no references) picking. All advanced parameters (exclusive picking, filtering etc.) are available.

`gCTF <http://www.mrc-lmb.cam.ac.uk/kzhang/Gctf/>`_
GPU-accelerated program for CTF determination, refinement and evaluation. At this moment movie options, CTF refinement for particles and tilt refinement options are not supported yet.

`Imagic <https://www.imagescience.de/smi.html>`_
We have added Imagic MSA classification method. Further information is available from our link:https://github.com/I2PC/scipion/wiki/ImagicProtMSA[wiki].

`Localized reconstruction <https://github.com/OPIC-Oxford/localrec/wiki>`_
A general method for the localized three-dimensional reconstruction of substructures bound to a larger particle. After determination of the particle orientations via conventional methods, local areas corresponding to the subunits ('subparticles') can be extracted and treated as single particles.

`magDistortion <http://grigoriefflab.janelia.org/magdistortion>`_
This program from Grigorieff’s lab allows to estimate and correct magnification distortions in electron micrographs. Correction is also available for particle coordinates. Hint: results of this protocol can be used for motion correction with motioncor2!

`Motioncor2 <http://msg.ucsf.edu/em/software/motioncor2.html>`_
Completely re-written (after motioncorr/dosefgpu) software from D. Agard lab allows anisotropic beam-induced motion correction at single pixel level across the whole frame using GPUs. Options for dose filtering, correction of magnification distortion and saving movie stacks are available.

`Relion 2.0 <http://www2.mrc-lmb.cam.ac.uk/relion/index.php/Main_Page>`_
We have updated Relion to its latest available version (2.0.4). You can benefit
from the substantial reduction of computing time using Relion with your GPUs.
But do not worry if you don’t have GPU, you can also use Relion on CPUs. We have
also added new relion extract particle protocol and refactored the picking
protocol. Moreover, new protocols for particle sorting, 3D mask creation,
projection subtraction and CTF export to STAR file were added.

Streaming
~~~~~~~~~
Streaming processing allows to overlap data acquisition with the first steps of
digital image processing. Protocols adapted for streaming can be executed even
if the algorithm that produces the data that is going to be used as input has
only produced part of the output dataset.

Import movies
~~~~~~~~~~~~~
Movies can now be imported in “streaming” mode. Also, individual frames can be
used as input and stacked on-the-fly, making the movies available for later
protocols immediately.

Movie alignment
~~~~~~~~~~~~~~~
All movie alignment protocols are able to use movies in streaming
(motioncorr, motioncor2, xmipp-opticalflow, xmipp-crosscorrelation, unblur).

CTF estimation
~~~~~~~~~~~~~~
ctffind3, ctffind4, gCTF are now able to work in streaming mode.

Monitors
~~~~~~~~
We have designed monitors to follow the status of several running protocols within a Scipion project. They can track and plot values for “system status” (cpu, memory, swap), ctf values (defocusU, defocusV). Alerts can be setup to email the microscopist/user when certain values rise above/below a custom threshold.

HTML Report
~~~~~~~~~~~~~
The summary monitor generates an HTML report that summarizes the status of the system and the data being processed, plotting the defoci and system data.

Scipion box wizard
~~~~~~~~~~~~~~~~~~~
This wizard creates a folder structure for your project and can be customized to reflect different microscope or camera setups. You can choose what preprocessing steps you would like to do during movie streaming.

Consolidation
~~~~~~~~~~~~~
We have also done a lot of work to consolidate Scipion, improving the usability and adding small features to make Scipion a better and more robust software:


* Extract coordinates protocol can now apply shifts to the particle coordinates.
* Scipion install script now provides a possibility to choose package version for installation.
* Export bibliographic references into bibtext file.
* Notebook: write project notes in your favourite text editor.
* `Labels <labels>`_: any protocol can now be labelled with a name and/or color. This helps to orient within a protocol tree in large projects. (Use Ctrl+T to loop through modes)
* Age mode: Coloring the boxes by “age”, the younger the bluest. (Use Ctrl+T to loop through modes)
* Zooming and panning a project’s protocol tree (Use “Shift + mouse wheel”)
* `Linear picking mode <linear-picking>`_, eraser size modification are now available in xmipp particle picker.
* Project import: besides import/export of workflows, now it is also possible to import whole projects, e.g. from another computer.
* `Collect statistics <collecting-statistics>`_: we collect and analyze usage statistics information to better understand the usage of the different protocols and prioritize maintenance and support. You can choose to enable or disable the collection of information at any time.
* New scripts: create movie stacks, mirror directory, scipion box wizard.
* Sort objects in browse windows: now all objects can be sorted by name, info or creation date. Useful when you have a lot of different object sets.
* Highlight direct connections of selected protocols.
* Several performance improvements to decrease project loading time.
* Improved movie model: added initial dose (pre-exposure) and dose per frame.


v1.0.1 (2016-06-30)
====================
* Several protocol fixes:

    * Fixed bug when creating the output for Frealign (in some cases some information from input particles was not properly propagated)
    * Fixed some bugs in movie alignment protocols (summovie and unblur) and tests added
    * Some minor bugs fixed in Relion protocols
    * Bugs fixed in Resmap protocol when using two half volumes

* Fixed several bugs in Spider protocols:

    * converting input particles with alignment
    * wrong regular expression for replacing some variables in script template
    * parsing of the resulting dendrogram
    * some additional validations and removed unused code

* Bugfixes and inprovements in Xmipp protocols:

    * Protocols screen-classes merged into one: compare-reprojections
    * Complete refactoring of operate-particles and operate-volumes protocols (previously called 2D and 3D calculator).  Tests added

* Picking and Viewer:

    * Warning if particles are picked in a temporary folder and the SetOfParticles was not created
    * Improved implementation of assign-tiltpairs protocol in Xmipp and some refactoring of picking methods
    * Fixed bug that caused GUI to freeze sometimes
    * Some bugs fixed when displaying and exporting particles
    * Sorting arrows displayed after sorting by a column. Hourglass displayed while sorting.
    * Some bug fixed when creating subset from classes

* Other fixes or improvements:

    * ImageHandler's methods convert and writeStack now accepts alignment parameters
    * Fixed bug when displaying Movies summary (sqlite files were not closed)
    * Fixed bug when spawning Eman process to write particles
    * Added REMOTE_MESA_LIB environment var for using OpenGL in remote desktops
    * Created a LegacyProtocol class to read deprecated protocols
    * Cleanup in some tests and added new ones for core classes or functions

v1.0.0 (2016-02-20) Augusto
============================

* Allows to combine several EM software packages (~ 100 protocols):

  * All protocols from Xmipp
  * Most of protocols from Relion
  * MDA protocols from Spider
  * Some protocols from Eman2/Sparx
  * From Grigorieff lab: CTFFIND, FREALIGN, unblur and summovie.
  * A few tools from Bsoft
  * ResMap, gEMpicker, dogpicker, motioncorr

* Full tracking and reproducibility:

  * Display runs as a list or a tree.
  * Inspect the parameters of a previous run
  * Repeat one or several runs
  * Export/Import a workflow template

* Data analysis:
  * Visualization and operation with Sets. (Particles, Micrographs, CTFs, etc)
  * Visualization of Volumes
  * Resolution and angular distribution plots


`Legacy release note <legacy-release-notes>`_
