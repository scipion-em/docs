.. _`sec:structurePrediction`:

Structure Prediction by Sequence Homology. Searching for Homologues
===================================================================

As we have mentioned above, in this tutorial we are going to use tools
that allow to predict the atomic structure from sequence homology.

Structure prediction by sequence homology only requires the sequence
itself of the specimen that we would like to model, from now ahead the ,
and the access to databases to seek structures or of homologous
molecules. The sequences of homologous molecules show statistically
significant similarity because they share common ancestry. Since the
sequence encodes the structural information, from high similar sequences
necessarily follows high similar structures. Structures from the nearest
homologous molecules will thus be preferred over remote relative ones.
Remark that molecules containing several domains usually require
independent searching for homologous templates of each domain. A small
review about sequence similarity searching can be found in
:raw-latex:`\citep{pearson2013}`, and in
:raw-latex:`\citep{kryshtafovych2018}` the assessment of current -based
modeling methods, many of them implemented as fully automated servers.
Modeling tools appropriate to search for remote homologous , folding
recognition and -free methods (), as well as :math:`de\ novo` modeling
tools, which besides sequences use the volume itself, have still to be
included in framework.

How to identify of the 
~~~~~~~~~~~~~~~~~~~~~~~

Similarity searching programs like () :raw-latex:`\citep{altschul1997}`,
available in https://blast.ncbi.nlm.nih.gov/Blast.cgi, use the (1) to
screen the structure-containing database (2). Selecting or excluding a
particular organism is an option (3). We usually start our searching
selecting the organism in which we are interested or the closest
evolutionarily related ones. If no similar sequences are found in these
organisms, unrelated organisms may be selected or no one at all.
Different searching algorithms are available (4) and one of them has to
be selected. After executing (5) a list of score-ordered is retrieved.

.. figure:: Images/Fig9.pdf
   :alt: Form of the similarity searching program .
   :name: fig:blastp
   :width: 80.0%

   Form of the similarity searching program .

Of course, the closest relatives to human subunits, structurally
characterized, will be their own structures contained in . However, in
this tutorial we are going to assume that in our example the closest
relatives to the human :math:`\alpha` and :math:`\beta` subunits are the
respective subunits (identity 49.3% and 45.21%) of the antarctic fish
:raw-latex:`\citep{camardella1992}`. The atomic structure associated to
this has accession code . Information about the structure can be checked
in https://www.rcsb.org/structure/1PBX. In general, it is a good idea to
read the information related with the , do it so and answer the
following questions: (Answers in appendix
`[app:solutions] <#app:solutions>`__;
**Question**\ `1 <#sec:structurePrediction>`__\ **\ \_1**)

.. container:: framed

   -  How was this structure obtained (X-ray diffraction, EM, NMR)?

   -  What resolution does it have?

   -  How many chains does it include?

| 
| : also incorporates the possibility of running the algoritnm, although
  with lower number of options than those shown in . Nevertheless, if
  you know that there are high similar homologous sequences with
  associated structure, you can skip this searching step “outside” and
  go to the next step to get directly your and your .
