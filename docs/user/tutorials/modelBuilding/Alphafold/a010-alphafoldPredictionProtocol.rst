.. _`app:alphafoldPredictionProtocol`:

AlphaFold2 Initial Model Prediction protocol
===========================================

*ChimeraX*-based protocol designed to get AlphaFold2 :cite:p:`jumper2021` atomic structure predictions. Although included in the **scipion-em-chimera** plugin, the protocol **chimerax-alphafold prediction** allows to use, in addition to *ChimeraX* `tools <https://www.rbvi.ucsf.edu/chimerax/data/alphafold-nov2021/af_sbgrid.html>`_, the *PHENIX* `options <https://phenix-online.org/documentation/reference/alphafold.html>`_ to access to Google Colab notebook system.

-  | Requirements to run this protocol and visualize results:

   -  | *Scipion* plugin: **scipion-em**

   -  | *Scipion* plugin: **scipion-em-chimera**

-  | *Scipion* menu: *Model building -> Initial model* (:numref:`model_building_app_protocol_alphafold_prediction_1` (A))

   .. figure:: Images_appendices/Fig6_alphaFoldPrediction.svg
      :alt: Protocol **chimerax-alphafold prediction**. A: Protocol location in *Scipion* menu. B: Protocol form to retrieve AlphaFold2 structure predictions from EMDB (identical sequence). C: Protocol form to retrieve AlphaFold2 structure predictions from EMDB (homologous sequence) D: Protocol form to predict atomic structures using Google Colab notebooks to run AlphaFold2. E: Protocol form to predict atomic structures running AlphaFold2 in your own computer.
      :name: model_building_app_protocol_alphafold_prediction_1
      :align: center
      :width: 100.0%

      Protocol **chimerax-alphafold prediction**. A: Protocol location in *Scipion* menu. B: Protocol form to retrieve AlphaFold2 structure predictions from EMDB (identical sequence). C: Protocol form to retrieve AlphaFold2 structure predictions from EMDB (homologous sequence). D: Protocol form to predict atomic structures using Google Colab notebooks to run AlphaFold2. E: Protocol form to predict atomic structures running AlphaFold2 in your own computer.

-  | Protocol form parameters (:numref:`model_building_app_protocol_alphafold_prediction_1` (B, C, D, E)):

   | *Input* section:

   -  | *Source to retrieve the AlphaFold2 model*: 
      | Click to select one of the next four options:

   	-  | *EBI Database (identical sequence)*: The `AlphaFold Protein Structure Database <https://alphafold.ebi.ac.uk/>`_ has been developed by DeepMind and EMBL-EBI with the aim of providing researchers with the AlphaFold2 predictions for the human proteome and other key organisms. They plan to extent the database to the majority of catalogued proteins. This work is still in progress and many proteins included as UniProt IDs have already been predicted and those predictions are freely available to the scientific community. To retrieve one of those protein predictions, write the alphanumerical code of the respective UniProt entry (:numref:`model_building_app_protocol_alphafold_prediction_1` (B):

		-  | *UniProt name/ID*

		   | The protocol will fail if the written code doesn't exist in UniProt DB or if  despite being a valid UniProt ID, the prediction has not been included in the *AlphaFold Protein Structure Database* yet.

        -  | *EBI Database (homologous sequence)*: For all those cases in which the AlphaFold2 prediction hasn't been included in the *AlphaFold Protein Structure Database* yet, the protocol **chimerax-alphafold prediction** gives the oportunity of retrieving the prediction performed for the most similar protein, identified through BLAST searching taking advantage of *ChimeraX*. Selecting this option you'll be interrogated about (:numref:`model_building_app_protocol_alphafold_prediction_1` (C):

		-  | *Reference sequence*: Protein sequence to perform the BLAST searching. This sequence has been previously imported to *Scipion* by using the protocol :ref:`Import sequence <app:importSequence>`.

		-  | *similarity-matrix*: Advanced param to select one of the `substitution matrices <https://www.ncbi.nlm.nih.gov/blast/html/sub_matrix.html>`_ to assign a score to any couple of residues in the alignment.

		-  | *cutoff*: Advanced param to select the maximum statistic value required to include a retrieved element in the hit list.

		-  | *Hide help popup window*: With this param you can choose between hide (*YES*) or show (*NO*) a help message to select and save the atomic structure using the *ChimeraX* command `scipionwrite <help:user/commands/scipionwrite.html>`_. Selecting *YES* that help information will be shown also in red bold in the *ChimeraX* GUI (Log). Take into account that you might not retrieve any homologous structure. Check the box *Blast Protein Results* on the right. An empty box means no homologous structures retrieved for a particular substitution matrix and cutoff value.
	
	-  | *Google  Colab*: In case no AlphaFold2 predictions can be retrieved from *EBI Database* (considering both identical and homologous sequences) the user has the opportunity to generate his/her own prediction taking advantage of two different Google Colaboratory notebooks that allows the user to run the program for free in the Google cloud. There are, nevertheless, some limitations in the computing resources that can be used. In particular, there is a daily limit and the GPUs assigned by Google Colab might not have enough memory for predicting the structure of long sequences.

	-  | *Local AlphaFold*:


