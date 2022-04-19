.. _`sec:structurePrediction`:

Structure Prediction by Sequence Homology. Searching for Homologues
===================================================================

As we have mentioned above, in this tutorial we are going to use tools
that allow to predict the atomic structure from sequence homology.

Structure prediction by sequence homology only requires the sequence
itself of the specimen that we would like to model, from now ahead the *target sequence*,
and the access to databases to seek structures or *templates* of homologous
molecules. The sequences of homologous molecules show statistically
significant similarity because they share a common ancestry. Since the
sequence encodes the structural information, from high similar sequences
necessarily follows high similar structures. Structures from the nearest
homologous molecules will thus be preferred over remote relative ones.
Remark that molecules containing several domains usually require
independent searching for homologous templates of each domain. A small
review about sequence similarity searching can be found in :cite:p:`pearson2013`, and in :cite:p:`kryshtafovych2018` the assessment of current *template*-based
modeling methods, many of them implemented as fully automated servers.
Modeling tools appropriate to search for remote homologous *templates*, folding
recognition and *template*-free methods (*ab initio*), as well as :math:`de\ novo` modeling
tools, which besides sequences use the volume itself, have still to be
included in the *Scipion* framework.

How to identify *templates* of the *target sequence*
~~~~~~~~~~~~~~~~~~~~~~~

Similarity searching programs like *BLAST* (:numref:`model_building_blastp`) :cite:p:`altschul1997`,
available in `BLAST <https://blast.ncbi.nlm.nih.gov/Blast.cgi>`_, use the *target sequence* (1) to
screen the structure-containing database *PDB* (2). Selecting or excluding a
particular organism is an option (3). We usually start our searching
selecting the organism in which we are interested or the closest
evolutionarily related ones. If no similar sequences are found in these
organisms, unrelated organisms may be selected or no one at all.
Different searching algorithms are available (4) and one of them has to
be selected. After executing *BLAST* (5) a list of score-ordered *templates* is retrieved.

.. figure:: Images/Fig9.svg
   :alt: Form of the similarity searching program *BLAST*.
   :name: model_building_blastp
   :align: center
   :width: 80.0%

   Form of the similarity searching program *BLAST*.

Of course, the closest relatives to human *Hgb* subunits, structurally
characterized, will be their own structures contained in *PDB-5NI1*. However, in
this tutorial we are going to assume that in our example the closest
relatives to the human :math:`\alpha` and :math:`\beta` subunits are the
respective *Hgb* subunits (identity 49.3% and 45.21%) of the antarctic fish *Pagothenia bernacchii* :cite:p:`camardella1992`. The atomic structure associated to
this *template* has *PDB* accession code *1PBX*. Information about the structure can be checked
in `1PBX <https://www.rcsb.org/structure/1PBX>`_. In general, it is a good idea to
read the information related with the *template*, do it so and answer the
following questions: (Answers in appendix :ref:`Solutions <app:solutions>`;
**Question**\ `1 <sec:structurePrediction>`_\ **\ \_1**)

::

   -  How was this structure obtained (X-ray diffraction, EM, NMR)?

   -  What resolution does it have?

   -  How many chains does it include?

| 
| ``NOTE:`` *ChimeraX* also incorporates the possibility of running the *BLAST* algoritnm, although
  with lower number of options than those shown in :numref:`model_building_blastp`. Nevertheless, if
  you know that there are high similar homologous sequences with
  associated structure, you can skip this searching step “outside” *Scipion* and
  go to the next step to get directly your *template* and your *target model*.
