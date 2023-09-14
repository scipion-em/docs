.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _tomostreaming:

==================================================================================
Tutorial - Tomography streaming workflow
==================================================================================

.. contents:: Table of Contents

Introduction
============

This tutorial guide you in a streaming tomography acquisition using Scipion.
To achieve this goal, we will import the tilts as a movie in SPA, we will align
those wit the align protocols of SPA, we will compose the tilt serie and as the
last step we will generate the tomogram. All the steps running in streaming

Additional resources
====================

Here you can find some valuable resources to complement the contents described in the tutorial:

* `Full SPA processing video tutorial <https://scipion-em.github.io/docs/release-3.0.0/docs/user/single-particle-tutorials.html#full-spa-processing-video-tutorial>`_
* `Tomography in Scipion <https://scipion-em.github.io/docs/release-3.0.0/docs/user/tutorials/tomo/tomography-intro.html#tomography-intro>`_

Where to find the protocols?
============================

Protocols needed to perform the workflow are available in the following plugins:

* **scipion-em**
* **scipion-em-motioncor**
* **scipion-em-tomo**
* **scipion-em-aretomo**

Workflow protocols
==================

Importing and aligning movies as SPA
------------------------------------
We will import al the tilts as we were in Single Particle, that way we will use
the import movies protocol filling the form as common in SPA. Review the streaming
parameters to be sure that the protocol works with the microscope condition (time
to the next tilt (file timeout) and time to finish the acquisition (Timeout).
You have to take into account that the workflow we propose admit several tiltseriee.

When the movies are being imported, we will continue alinging those movies. You
can use the protocol to aling you consider, we propose on this workflow MotionCor,
but you have to take into account that you can not use batches because could deform the image.
Please set Number of patches as X=1 Y=1.

Composing tilt series
---------------------
To generate a tilt serie we have released the Compose Tilt Serie protocol, available
on scipion-em-tomo.

.. figure:: /docs/user/tutorials/tomo/Tomo_streaming/tomoStreamingCompose1.png
   :align: center
   :width: 600
   :alt: ComposeTiltSerie

Some parameters must be filled before launch the workflow:

* Input micrograph: Select as input the output of the align protocol
* Path with the *.mdoc file for each TiltSerie: Select the directory that contain the mdoc files of each tiltSerie. The protocol will read each tilt fromn those mdoc files.
* Streaming; Time for next tilt: elay (in seconds) until the next tilt is registered in the mdoc file. After timeout, if there is no new tilt, the tilt serie is considered as completed.Minimum time recomended 20 segs
* Streaming; Time for next TiltSerie: Interval of time (in seconds) after which, if no new tilt serie is detected, the protocol will end. The default value is high (30 min) to avoid the protocol finishes during the acq of the microscope. You can also stop it from right click and press STOP_STREAMING.

.. figure:: /docs/user/tutorials/tomo/Tomo_streaming/tomoStreamingCompose2.png
   :align: center
   :width: 600
   :alt: ComposeTiltSerie Srtreaming

Aligning tilts and generating tomograms
---------------------------------------
In order to generate a tomogram in streaming; in the time we have the tomogram
of a tilt series to process the acquisition, we have enhanced the Aretomo protocol
to manage the streaming process.
None of the parameters must be filled in other than the usual ones available in the Aretomo protocol.


Summary
=======
We have explained the workflow for managing a streaming acquisition. It requires only four protocols,
two of them belong to the SPA field and the other two to the tomography field.
The compose tilt series is a protocol designed ad-hoc for streaming tomography
and the AreTomo protocol has been enhanced to allow treaming.
In the future we plan to enable streaming tomography using other plugins such as IMOD.