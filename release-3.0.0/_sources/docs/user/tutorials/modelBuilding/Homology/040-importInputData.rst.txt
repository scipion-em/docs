.. _`importInputData`:

Import Input data
=================

Taking advantage of *Scipion* software framework, we are going to import the above
indicated input data using protocols **import volumes** and **import sequence**. Details about the parameters
of these two protocols are shown in Appendices :ref:`Import volumes <app:importVolume>` and :ref:`Import sequence <app:importSequence>`, respectively.

.. figure:: Images/Fig61.svg
   :alt: *Scipion* framework with import workflow.
   :name: model_building_scipion_workflow_import_1
   :align: center
   :width: 95.0%

   *Scipion* framework with import workflow.

(``NOTE:`` In the following we will use the notation **Fig. X (a)** to reffer to the figure number X and there will be an arrow labeled with “a” pointing to the region of interest.)

Volume
------

First open the **import volumes** protocol (:numref:`model_building_import_volume` (1)), fill in the form and execute it (2), and
finally you may visualize the volume (3).

As you can see, when we import a map we directly assign its sampling
rate and its origin of coordinates. If for any reason we have to work
with other maps previously generated during the reconstruction process
that do not have the desired sampling and origin, we can use the
auxiliar protocol **assign orig & sampling**, detailed in Appendix :ref:`Assign origin and sampling <app:asignOrigAndSampling>`, to assign them.

.. figure:: Images/Fig4.svg
   :alt: Importing the volume in *Scipion*.
   :name: model_building_import_volume
   :align: center
   :width: 95.0%

   Importing the volume in *Scipion*.

*ChimeraX* :cite:p:`Goddard2018` is used for visualization by default .
Clicking in the viewer menu (:numref:`model_building_visualization_volume` (1)), shows the 3D map and the :math:`x`
(red), :math:`y` (yellow) and :math:`z` (blue) axes.

.. figure:: Images/Fig5.svg
   :alt: Volume visualized with *ChimeraX*.
   :name: model_building_visualization_volume
   :align: center
   :width: 95.0%

   Volume visualized with *ChimeraX*.

.. _`section_import_seq`:

Sequences
---------

The sequences of *Hgb* :math:`\alpha` and :math:`\beta` subunits will be
independently downloaded from `UniprotKB <https://www.uniprot.org>`_. First of all, open the form of **import sequence** protocol (:numref:`model_building_import_sequence` (1)), then complete the form to download *HBA_HUMAN* protein with *UniprotKB* accession code *P69905*,
execute the process (2), and finally visualize the sequence (3) in a
text editor. The sequence will appear in *fasta* format as it has been written
above. Follow the same protocol to download *HBB_HUMAN* with accession code *P68871*.

.. figure:: Images/Fig6.svg
   :alt: Importing a *UniprotKB* sequence in *Scipion*.
   :name: model_building_import_sequence
   :align: center
   :width: 95.0%

   Importing a sequence in *Scipion*.
