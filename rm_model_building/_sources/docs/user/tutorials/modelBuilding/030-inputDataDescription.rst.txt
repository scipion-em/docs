Input data description
======================

Map
---

| Modeling means atomic interpretation of a map. This map can be the
  result of our own reconstruction process or can be obtained from a
  database. In this tutorial we use the haemoglobin map , that can be
  downloaded from (http://www.ebi.ac.uk/pdbe/entry/emdb/EMD-3488) ().
| WARNING in case you use your own map obtained from cryo-EM images:
  Take into account that cryo-EM 3D maps benefit significantly of an
  “optimizing” step, normally referred to as “sharpening” or “density
  improvement“, that tends to increase signal at medium/high resolution.
  Therefore, we recommend to sharp the map before tracing the atomic
  model. Either two protocols consecutively applied,
  :raw-latex:`\citep{vilas2018}` and :raw-latex:`\citep{ramirez2018}`,
  or the protocol :raw-latex:`\citep{Sanchez-Garcia2020.06.12.148296}`,
  allow map sharpening. Details about the parameters of these protocols
  are shown in Appendices `[app:localMonoRes] <#app:localMonoRes>`__,
  `[app:localDeblurSharpening] <#app:localDeblurSharpening>`__ and
  `[app:deepEMhancerSharpening] <#app:deepEMhancerSharpening>`__,
  respectively.

.. figure:: {Images/Fig3}
   :alt: Downloading the volume from .
   :name: fig:PDBE
   :width: 95.0%

   Downloading the volume from .

Once downloaded the volume, unpack it (command line: ) and save it in
your tutorial folder.

Sequences
---------

The sequences of :math:`\alpha` and :math:`\beta` subunits are included
in . Accession numbers are and , respectively. Next, we show both
sequences in fasta format:

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
experimental sequence obtained from complementary , i.e., synthesized or
retro-transcribed from messenger . In this way, it is quite unlikely
that these sequences include post-translational modifications. Although
methionine is added with the translation initiation factor, the removal
of methionine aminoacid from the N-terminus of a polypeptide is a common
post-translational modification. Since appears at the N-terminal end of
both proteins, we can predict that these are not the polypeptide mature
forms and will be removed in the mature ones that are present in the
atomic structures.

Those two sequences can be retrieved from using   protocol, which allows
direct downloading from the database.
