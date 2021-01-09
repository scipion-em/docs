.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _faq:

==========================
Frequently Asked Questions
==========================

.. contents:: Frequently Asked Questions

Working with sets
=================

How can I switch to a different coarse/binning level for a set of particles?
----------------------------------------------------------------------------

You can use **Particles -> Picking -> scipion - extract coordinates** protocol
on your set of particles, then re-extract them with a different binning level
and continue the processing.


How to create a Set of Volumes from several volumes?
----------------------------------------------------

Go to **Sets -> scipion - join sets**. Then select each volume that you want to
include in the _SetOfVolumes_ and execute the protocol.
