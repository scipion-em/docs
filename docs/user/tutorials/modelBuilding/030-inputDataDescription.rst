Input data description
======================

Map
---

| Modeling means atomic interpretation of a map. This map can be the
  result of our own reconstruction process or can be obtained from a
  database. In this tutorial we use the haemoglobin map *EMD-3488*, that
  can be downloaded from *PDBE*
  (http://www.ebi.ac.uk/pdbe/entry/emdb/EMD-3488) (:numref:`model_building_PDBE`).

| WARNING in case you use your own map obtained from cryo-EM images:
  Take into account that cryo-EM 3D maps benefit significantly of an
  “optimizing” step, normally referred to as “sharpening” or “density
  improvement“, that tends to increase signal at medium/high resolution.
  Therefore, we recommend to sharp the map before tracing the atomic
  model. Either two *Scipion* protocols consecutively applied, 
  **xmipp3-local MonoRes** :cite:p:`vilas2018` and **xmipp3-localdeblur sharpening** :cite:p:`ramirez2018`,
  or the protocol **xmipp3-deepEMhancer** :cite:p:`Sanchez-Garcia2020.06.12.148296`,
  allow map sharpening. Details about the parameters of these protocols
  are shown in Appendices :ref:`Local MonoRes <app_localMonoRes>`, :ref:`Local Deblur <app:localDeblurSharpening>` and :ref:`DeepEMhancer <app:deepEMhancerSharpening>`, respectively.

.. figure:: Images/Fig3.svg
   :alt: Downloading the volume from *PDBe*.
   :name: model_building_PDBE
   :align: center
   :width: 95.0%

   Downloading the volume from *PDBe*.

Once downloaded the volume, unpack it (command line: ``gunzip
emd-3488.map.gz``) and save it in your tutorial folder.

Sequences
---------

The sequences of *Hgb* :math:`\alpha` and :math:`\beta` subunits are
included in *UniProtKB*. Accession numbers are *P69905* and *P68871*,
respectively. Next, we show both sequences in fasta format:

   ::

      >sp|P69905|HBA_HUMAN Haemoglobin subunit alpha
      MVLSPADKTNVKAAWGKVGAHAGEYGAEALERMFLSFPTTKTYFPHFDLSHGSAQVKGHG
      KKVADALTNAVAHVDDMPNALSALSDLHAHKLRVDPVNFKLLSHCLLVTLAAHLPAEFTP
      AVHASLDKFLASVSTVLTSKYR

      >sp|P68871|HBB_HUMAN Haemoglobin subunit beta
      MVHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPK
      VKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFG
      KEFTPPVQAAYQKVVAGVANALAHKYH

These protein sequences were determined by direct translation from the
experimental sequence obtained from complementary *DNA (cDNA)*, i.e.,
*DNA* synthesized or retro-transcribed from messenger *RNA (mRNA)*. In
this way, it is quite unlikely that these sequences include
post-translational modifications. Although methionine is added with the
translation *Met-tRNA* initiation factor, the removal of methionine
aminoacid from the N-terminus of a polypeptide is a common
post-translational modification. Since *Met* appears at the N-terminal
end of both proteins, we can predict that these are not the polypeptide
mature forms and *Met* will be removed in the mature ones that are
present in the atomic structures.

Those two sequences can be retrieved from *UniProtKB* using *Scipion* **import sequence**  protocol,
which allows direct downloading from the database.
