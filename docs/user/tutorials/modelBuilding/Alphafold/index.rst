Predicting initial models with Alphafold
========================================

AlphaFold network predicts the 3D coordinates of all heavy atoms for a given protein using mainly the primary amino acid sequence and aligned sequences of homologues as inputs. 

In this tutorial we show how to generate AlphaFold models of your sequence and rebuild them using the 3D density map. We use the approach described in the `phenix web site <https://phenix-online.org/documentation/reference/alphafold.html>`_ and summarized as:


* Get inital AlphaFold model
* Trim the model and break it into rigid domains
* Dock your models (cryo-EM) to place them in the right places in your map or unit cell.
* Fill in the missing parts of your models.

Contents
--------
.. toctree::
   :maxdepth: 1
   :numbered:

   005-versionhistory
   007-requirements
   010-introduction
   initialModel
   breakRigidDomains
   dock
   fill
