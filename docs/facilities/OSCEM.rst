.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo


.. _oscem:

============================
OSCEM
============================

OSC-EM (Open Standards Community for EM)
-----------------------------------------
.. figure:: /docs/images/facilities/OSCEM.png
   :width: 200
   :alt: scipion logo


OSC-EM is a community-driven effort to standardize metadata across the full lifecycle
of electron microscopy (EM) experiments by defining a common schema that spans data
acquisition, processing, and deposition.

The core metadata schema is developed in `OSCEM_Schemas` on `GitHub <https://github.com/osc-em/oscem-schemas>`_
This schema is authored in **LinkML**, which allows modular definition of experimental
components—such as “sample,” “instrument,” “processing,” and more—and supports export
to multiple formats (JSON Schema, JSON-LD, OWL, RDF) to ensure wide interoperability.

OSC-EM aims for strong semantic alignment by reusing existing ontologies when possible:
for example, it integrates terms from the CryoEM Ontology, the PDBx/mmCIF dictionary,
the Helmholz EM Glossary, and the NeXus-FAIRmat NXem format.
Metadata extraction tools have been developed to work with common acquisition software
(e.g., SerialEM, Thermo Fisher EPU), generating JSON files compliant with the OSC-EM schema.

To facilitate data sharing and deposition, OSC-EM also provides a converter from its JSON
metadata to the mmCIF format used by repositories like the EM Data Bank (EMDB) and
the Protein Data Bank (PDB).

The ``scipion-em-facilities`` plugin allows running the OSCEM protocol, which generates
the complete OSCEM metadata schema for each acquisition session.
