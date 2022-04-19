Import Input data
=================

Taking advantage of software framework, we are going to import the above
indicated input data using protocols and . Details about the parameters
of these two protocols are shown in Appendices
`[app:importVolume] <#app:importVolume>`__ and
`[app:importSequence] <#app:importSequence>`__, respectively.

.. figure:: Images/Fig61.pdf
   :alt: framework with import workflow.
   :name: fig:scipion_workflow_import_1
   :width: 95.0%

   framework with import workflow.

(Note: The notation means that the step is shown in figure number X and
there will be an arrow labeled with “a” marking the region of interest.)

Volume
------

First open the protocol ( (1)), fill in the form and execute it (2), and
finally you may visualize the volume (3).

As you can see, when we import a map we directly assign its sampling
rate and its origin of coordinates. If for any reason we have to work
with other maps previously generated during the reconstruction process
that do not have the desired sampling and origin, we can use the
auxiliar protocol , detailed in Appendix
`[app:asignOrigAndSampling] <#app:asignOrigAndSampling>`__, to assign
them.

.. figure:: Images/Fig4.pdf
   :alt: Importing the volume in .
   :name: fig:import_volume
   :width: 95.0%

   Importing the volume in .

By default :raw-latex:`\citep{Goddard2018}` is used for visualization.
Clicking in the viewer menu ( (1)), shows the 3D map and the :math:`x`
(red), :math:`y` (yellow) and :math:`z` (blue) axes.

.. figure:: Images/Fig5.pdf
   :alt: Volume visualized with .
   :name: fig:chimera_visualization_volume
   :width: 95.0%

   Volume visualized with .

Sequences
---------

The sequences of :math:`\alpha` and :math:`\beta` subunits will be
independently downloaded from . First of all, open the form of protocol
( (1)), then complete the form to download protein with accession code ,
execute the process (2), and finally visualize the sequence (3) in a
text editor. The sequence will appear in format as it has been written
above. Follow the same protocol to download with accession code .

.. figure:: Images/Fig6.pdf
   :alt: Importing a sequence in .
   :name: fig:import_sequence
   :width: 95.0%

   Importing a sequence in .
