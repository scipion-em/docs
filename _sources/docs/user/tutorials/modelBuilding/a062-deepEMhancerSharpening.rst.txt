.. _`app:deepEMhancerSharpening`:

DeepEMhancer Sharpening protocol
================================

Protocol designed to apply :math:`DeepEMhancer`, the automatic map
postprocessing method that sharpens and masks part of the noise at
medium/high resolution :cite:p:`Sanchez-Garcia2020.06.12.148296`, in *Scipion*. Detailed
information of this method can be also obtained `here <https://github.com/rsanchezgarc/deepEMhancer>`_.

-  Requirements to run this protocol and visualize results:

   -  *Scipion* plugin: **scipion-em**

   -  *Scipion* plugin: **scipion-em-xmipp**

   -  *Scipion* plugin: **scipion-em-chimera**

-  | *Scipion* menu:
   | *Model building -> Preprocess map* (:numref:`model_building_app_deepEMhancer_1` (A))

   .. figure:: Images_appendix/Fig303.svg
      :alt: Protocol **xmipp3-deepEMhancer**. A: Protocol location in *Scipion* menu. B: Protocol form.
      :name: model_building_app_deepEMhancer_1
      :align: center
      :width: 90.0%

      Protocol **xmipp3-deepEMhancer**. A: Protocol location in *Scipion* menu. B: Protocol form.

-  Protocol form parameters (:numref:`model_building_app_deepEMhancer_1` (B)):

   -  *Would you like to use half maps?*: Although the result will be
      the same if you decide to use half maps or a non-sharpened
      non-masked map, a way to ensure that you have selected the right
      input map is providing half maps. Then, using half maps is the
      preferred option over a non-sharpened non-masked map. In addition,
      the algorithm has been trained with half maps. The first step
      performed by the protocol is to compute the average map. Then,
      select *Yes* whenever you can provide half maps, otherwise be sure
      you have the right average map, usually generated during the
      reconstruction process (map refinement). However, the algorithm
      does not work correctly using post-processed maps. So try to not
      use postprocessed maps. Since the two half maps can be obtained
      directly as independent maps or being associated to the average
      map, if you select *Yes* a new question will appear:

      -  *Are the half maps included in the volume?*: Select *Yes* if
         your input average map has the two half maps associated. If
         this is the case, complete the next form param. Otherwise, you
         should provide both half maps as independent preexisting
         objects. To add those half maps a couple of form params will
         apper to fill in with each half map:

         -  *Volume Half 1*

         -  *Volume Half 2*

   -  *Input Volume*: Unsharpened unmasked electron density map
      previously downloaded or generated in *Scipion*.

   -  *Input normalization*: We need apply normalization to accomodate
      the intensity values of the map to the specific range of values of
      the trained neural network. Three possible normalization methods
      are suggested:

      -  *Automatic normalization*: Default normalization mode that
         forces the noise average to be zero and the standard deviation 0.1 in an spheric shell around the specimen. Since then noise always displays a similar distribution, the network gets
         easier to distinguish noise from signal. This method usually
         works correctly in almost any case. Exceptions could be very
         long specimens (fiber proteins) or those having big empty
         spaces (big viruses).

      -  *Normalization from statistics*: Similar to the first one,
         though in this case users provide their own statistics of the
         noise (average and standard deviation). Using *ChimeraX*
         could be a good option to compute statistics of the noise such
         as min and max values, mean, standard deviation from the mean
         (SD) and root-mean-square deviation from zero (RMS) (*Chimera* command
         line ``measure mapstats`` with the option ``subregion`` as indicated in `CHIMERAX commands <https://www.cgl.ucsf.edu/chimerax/docs/user/commands/measure.html#mapstats>`_.

      -  *Normalization from binary mask*: Select this option only if
         your input map is a masked map, which otherwise is not
         recomendable when this algorithm is used. The binary mask
         assigns 1 to the specimen and 0 to the remaining density.

   -  *Model power*: Deep learning model to use, three options are
      available:

      -  *tight target*: This default model is a equidistant balanced
         solution that works properly for maps that show resolution
         areas between 3.8 and 6 Å (wide range of resolution values).

      -  *highRes*: This model allows a deep sharpening and it is recommended for high resolution maps (lower than 4 Å).
         (``NOTE:`` In case your map shows a high heterogeneity with parts of high resolution, as well as areas of low resolution, using *tight target* and *highRes* is recommendable, studying which areas are better sharpened by each model).

      -  *wide target*: This is the most conservative model. It is
         recommended when you have areas in which signal and noise are
         almost identical. Whereas *tight target* and *highRes* might
         delete those regions considering them only noise, *wide target*
         will surely preserve them.

   -  *Remove small CC after processing*: Advanced param that improves
      the sharpening result by removing small connected components
      (usually noise). The default value of this param is *No* because
      the improvement usually does not make up for the additional time
      and computational resources invested.

   -  *Batch size*: Since :math:`DeepEMhancer` processes maps by
      dividing them in portions or smaller cubes that will be sent to
      GPUs, the value of batch size indicates the number of cubes that
      GPUs can simoultaneously process. Increase or reduce the default
      number according to the performance of the GPUs.

-  | Protocol execution:
   | Adding specific map/structure label is recommended in *Run name*
     section, at the form top. To add the label, open the protocol form,
     press the pencil symbol at the right side of *Run name* box,
     complete the label in the new opened window, press OK and, finally,
     close the protocol. This label will be shown in the output summary
     content (see below). If you want to run again this protocol, do not
     forget to set to *Restart* the *Run mode*.

   | ``REMARK:`` In this case you have the option *GPU IDs* that you have
     to complete according to your GPU core indexes. 

   | Press the *Execute* red button at the form bottom.

-  Visualization of protocol results:

   | After executing the protocol, press *Analyze Results* and *ChimeraX* graphics
     window will be opened by default. Both the input map(s) and the
     sharpened map generated by :math:`DeepEMhancer`
     (*deepPostProcess.mrc*) are referred to the origin of coordinates
     in *ChimeraX*. To show the relative position of atomic structure and electron
     density volume, the three coordinate axes are represented; X axis
     (red), Y axis (yellow), and Z axis (blue). Coordinate axes, input
     volume, and sharpened map are model numbers *#1*, *#2* , and *#3*,
     respectively, in *ChimeraX Model Panel*. In case that half maps have been
     included, the respective additional model numbers will be applied.

   | The possibility of visualizing the sharpened map by slices with `ShowJ <https://scipion-em.github.io/docs/docs/user/showJ>`_ is also opened as commonly in *Scipion*, selecting in the *Output* of the *Summary* box, black arrow *xmipp3 - deepEMhancer -> Volume*, the right mouse option *Open with DataViewer*.

-  Summary content:

   -  | Protocol output (below *Scipion* framework):
      | *xmipp3 - deepEMhancer -> Volume*;
      | Volume (x, y, and z dimensions, sampling rate).

   -  | *SUMMARY* box:
      | *Input*: type of map
      | *Normalization*: normalization method.
