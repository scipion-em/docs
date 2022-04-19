.. _`app:chimeraMapSubtraction`:

ChimeraX Map Subtraction protocol
=================================

-based protocol designed to subtract two maps. These two maps can be two
density maps experimentally obtained or derived from different
computations, including the generation of a density map from an atomic
structure. In the context of the modeling workflow this protocol helps
to find out unmodeled densities in a map as a whole or in a specific
part of it. In addition, wrong modeled regions can be also identified
with this protocol since the atomic structure could doesn’t fit to the
density map.

-  Requirements to run this protocol and visualize results:

   -  plugin:

   -  plugin:

-  menu: ( (A))

   .. figure:: Images_appendix/Fig309.pdf
      :alt: Protocol . A: Protocol location in menu. B: Protocol form to
      subtract two maps. C: Param option . D: Protocol form to subtract
      an atomic structure from a map. All possible params are shown.
      :name: fig:app_protocol_map_subtract_1
      :width: 85.0%

      Protocol . A: Protocol location in menu. B: Protocol form to
      subtract two maps. C: Param option . D: Protocol form to subtract
      an atomic structure from a map. All possible params are shown.

-  | Protocol form parameters ( (B,C,D)):
   | section:

   -  : Include here any map previously downloaded or generated in that
      you would like to use as minuend of the subtraction operation.

   -  : Two possibilities are allowed:

      -  : Between minuend and subtrahend maps, and you’ll obtain the
         difference. WARNING: Both maps have to be perfectly aligned.

      -  : The voxel region of the subtrahend greater than a certain
         level will be masked ( (C)). The default level is although can
         be modified with the param . If no level is supplied, will
         compute that level value.

   -  : Select the subtrahend of the subtraction operation. Two
      possibilities are allowed:

      -  : Any map previously downloaded or generated in . WARNING: The
         sampling rate of this map should be identical to the
         subtrahend’s.

      -  : Previously downloaded or generated in . By selecting this
         option many new params will interrogate about the
         structure-derived map that you would like to generate ( (D)).

         -  : This is a tricky param and a uniform rule cannot be
            followed since, although its value is related with the
            minuend map resolution obtained by computing the in the
            reconstruction process, local variations of this resolution
            seem to be involved. As a general rule, start with a
            resolution value half of the one obtained by the and check
            your results. Then test other resolution values closer to
            the one computed by the and compare the results with the
            previous one. At the end select the resolution that
            maximizes the difference between the minuend and the
            subtrahend.

         -  : Select the atomic structure in the workflow to generate
            the called .

         -  : In case you are interested in generate the sustrahend from
            the input atomic structure as a whole, answer to this
            question. However, answer if you want to derive that map
            from a specific chain of the atomic structure. If this is
            the case, a new param () will interrogate you about the
            specific chain that you can select with the help of the
            wizard on the right.

         -  | : Select to answer this question in case you’d like to
              count on a control of density levels to identify the
              differential density. The aim of this control is identify
              the density of the removed residues in the differential
              map. However, be cautious about discarding other densities
              that could appear in lower resolution areas and have
              density levels slightly different that the control one.
              After running the program the graphics window will open
              and the atomic structure won’t show the removed residues.
              To make easier the localization of this area, ten residues
              both upstream and downstream of the removed aminoacids
              will be highlighted.
            | Additional params to interrogate about the residues to be
              removed are , and . A wizard on the right helps to select
              this three elements. WARNING: In case you have already
              selected a specific chain of the structure to generate the
              , this chain will appear by default in the param since the
              selection of a different chain wouldn’t make sense.

         -  : In case your input atomic structure to derive the
            subtrahend corresponds to the asymmetric unit and you’d like
            to have the whole atomic structure or at least several
            adjacent asymmetric units together with the input one,
            select the option . Otherwise, the subtrahend derived map
            will only correspond to the asymmetric unit. All symmetries
            will be available
            (https://www.cgl.ucsf.edu/chimerax/docs/user/commands/sym.html).
            In case you select symmetries cyclic or dihedral, an
            additional param will interrogate you about the . Pay
            attention to the param , set to by default. This is the
            distance (in Å) from the center of the input asymmetric unit
            to the center of additional allowed asymmetric units, in
            order to select only the closer ones. You should probably
            modify the default value to regenerate big maps by applying
            symmetry.

         -  : Select the option if you want to limit the input minuend
            to a certain area around the atomic structure. This is the
            option recommended if you have a big starting map and you’d
            like to substract a much smaller subtrahend
            structure-derived map since the visualization of results
            will be much easier. An additional param, asks you about the
            distance around the input structure used to crop the input .
            is the default value. The -generated map is called .

      -  : Additional atomic structures previously downloaded or
         obtained in can be included here to help you identify
         particular areas of the map or structure. Then, those
         structures are only informative and won’t be used to generate
         the subtrahend map.

      -  : parameter to clean the background of the differential map by
         applying a filter in order to maximize the differences between
         the minuend and the subtrahend maps, since the differential map
         usually results quite blurry. This will always appear together
         with the when the graphics window opens. To filter the
         differential map you can choose between two different filters,
         (with variable width) and based on the .

-  Protocol execution:

   | Adding specific volume label is recommended in section, at the form
     top. To add the label, open the protocol form, press the pencil
     symbol at the right side of box, complete the label in the new
     opened window, press OK, and finally, close the protocol. This
     label will be shown in the output summary content (see below). If
     you want to run again this protocol, do not forget to set to the .
   | Press the red button at the form bottom.
   | After executing the protocol the graphics window will open and show
     the different inputs (maps and atomic structures), as well as the
     maps generated by the commands such as , , and . Most of the
     outputs are already saved in , however you can perform any
     operation of your preference and save the new results before
     closing . Common commands of -communication are allowed in this
     case: , and .

-  Visualization of protocol results:

   | After exiting the protocol, press and the :math:`ChimeraX` graphics
     window will open with every saved elements, inputs and outputs,
     which might be distinct acording to the inputs. In addition to
     items mentioned in the previous paragraph, the atomic structure
     without the removed residues used as a control, called will be also
     shown overlapping the input structure.
   | By pressing the left black arrow shown in the the saved maps can be
     also opened with :math:`ShowJ`, the default viewer that shows each
     map’s (https://github.com/I2PC/scipion/wiki/ShowJ).

-  Summary content:

   -  | Protocol output (below framework):
      | For each map: ;
      | .
      | For each atomic structure: ;
      | ).

   -  | box:
      | :
      | List of output map names

USE CASES
~~~~~~~~~

-  | 
   | Aim: Run the workflow depicted in (A). The output of protocols 1, 2
     and 3 can be seen in the viewer by pressing .

   -  | In the (B) appears the whole adenovirus map, output of protocol
        1. To visualize this map write in the command line:
      | and adjust level densities according to level indicated in the
        shown .

   -  | In the (C) the extracted asymmetric unit is shown, overlapped to
        the whole map, as output of protocol 2. To visualize these maps,
        in addition to the previous command line and the adjustment of
        map levels indicated below, modify the transparency of the whole
        map writing:

   -  | Finally, the (D) details the atomic structure of the biological
        asymmetric unit obtained by modeling as output of protocol 3 ().
        Select and to change to ribbons the view of the structure. The
        overlapping of this structure to the geometrical map asymmetric
        unit allows to observe the area (5, dotted blue circle) where
        the penton is located and we will try to see a remnant density.
        To visualize the map, write in the command line:

   .. figure:: Images_appendix/Fig310.pdf
      :alt: (A) workflow showing protocols 1, 2, 3 and 4. (B) Adenovirus
      HAdV-F41 map image. (C) Map geometrical asymmetric unit extracted
      from the adenovirus map. (D) Adenovirus atomic structure of the
      biological asymmetric unit overlapped to the geometrical map unit.
      :name: fig:app_usecase_mapsubtract_1

      (A) workflow showing protocols 1, 2, 3 and 4. (B) Adenovirus
      HAdV-F41 map image. (C) Map geometrical asymmetric unit extracted
      from the adenovirus map. (D) Adenovirus atomic structure of the
      biological asymmetric unit overlapped to the geometrical map unit.

   To look for remnant densities in the penton area we have to complete
   the protocol with the indicated params (. Remark that in this case we
   have selected half of input resolution (4 Å) although other values
   could be tested. The only chain of the penton in the atomic structure
   of the asymmetric structure is the chain , inside the dotted blue
   circle of (D), and 8 residues will be removed as a control of density
   levels. In addition, icosahedral symmetry will be applied to the
   selected chain in order to complete the five units of the penton. In
   order to visualize better the map difference, a map fraction around
   the atomic structure is selected.

   .. figure:: Images_appendix/Fig311.pdf
      :alt: Completing the protocol to find renmant densities in the
      penton area of the adenovirus map.
      :name: fig:app_usecase_mapsubtract_2

      Completing the protocol to find renmant densities in the penton
      area of the adenovirus map.

   Protocol execution: Follow the general procedure shown above
   (Protocol execution section) and the graphics window will open. At
   this point several maps and atomic structures will be shown, as the
   panel indicates ( (C, top)). Have a look to each map and structure to
   identify them and play with the density levels to maximize the
   differences between the input restricted to the penton area () and
   the penton atomic structure-derived map (). The images A and B show
   the difference in the penton side (A) and upper (B) views,
   respectively, according to the density level observed on the panel
   (C, middle). Red arrows point at the densities associated to the
   removed residues used as a density control. The adjacent ten residues
   to the removed ones upstream and downstream are green-highlighted.
   The penton upper view (B) was obtained opening the main menu ( and
   setting the view as indicated (C, botton). From these results we can
   conclude that a remnant density in the upper part of the penton, if
   exits, it is not so evident.

   .. figure:: Images_appendix/Fig312.pdf
      :alt: (A) Side view of the adenovirus penton atomic structure
      (magenta) and the gaussian filtered difference map (grey). (B)
      Upper view. (C) From top to bottom, panel, panel, specified for
      the gaussian filtered difference map, and panel, respectively.
      :name: fig:app_usecase_mapsubtract_3

      (A) Side view of the adenovirus penton atomic structure (magenta)
      and the gaussian filtered difference map (grey). (B) Upper view.
      (C) From top to bottom, panel, panel, specified for the gaussian
      filtered difference map, and panel, respectively.

   With the exception of the input adenovirus biological asymmetric unit
   atomic structure, the rest of elements shown in the graphics window
   will also appear in the viewer that opens pressing . Consider then
   the possibility of performing additional operations and saving them
   with the command before closing the graphics window. After exiting
   the protocol you can visualize your results.

-  | 
   | Aim: Run the workflow depicted in (A) to inspect for remnant
     densities around the area covered by the hexons in the biological
     asymmetric unit area of the adenovirus map (A, 6). The output of
     all protocols can be seen in the viewer by pressing .

   -  In the (B, C, D) you also have the output of protocols 1, 2 and 3.

   -  | The output of the protocol 4 shows the atomic structure of human
        adenovirus HAdV-C5. Select and to change to ribbons the view of
        the structure. This structure was fitted to the map asymmetric
        unit of adenovirus HAdV-F41 by using the protocol (6) and the
        result of this oputput, overlapped to the geometrical map
        asymmetric unit, is shown in (B). To visualize this map write in
        the command line:
      | and adjust level densities according to level indicated in the
        shown ( (D)). Select and to change to ribbons the view of the
        structure.

   -  The output of protocol 5 details some small chains of residues
      previously traced in the remnant density of the adenovirus
      HAdV-F41. They are used as a control to be sure that we identify
      new densities previously unmodeled. Since they are very small we
      have depicted them selecting and overlapped to the geometrical map
      asymmetric unit ( (C) with the same transparency and map
      adjustment shown in (B).

   .. figure:: Images_appendix/Fig314.pdf
      :alt: (A) workflow showing protocols 1-7. (B) HAdV-F41 adenovirus
      geometrical map asymmetric unit (grey) and, fitted to it, the
      atomic structure of the biological asymmetric unit atomic
      structure of HAdV-C5 adenovirus (colored). (C) HAdV-F41 adenovirus
      geometrical map asymmetric unit (grey) and some small aminoacid
      chains previously traced in the remnant density, imported in the
      protocol 5 (colored). (D) Level of density selected to visualize
      the map in B and C.
      :name: fig:app_usecase_mapsubtract_4

      (A) workflow showing protocols 1-7. (B) HAdV-F41 adenovirus
      geometrical map asymmetric unit (grey) and, fitted to it, the
      atomic structure of the biological asymmetric unit atomic
      structure of HAdV-C5 adenovirus (colored). (C) HAdV-F41 adenovirus
      geometrical map asymmetric unit (grey) and some small aminoacid
      chains previously traced in the remnant density, imported in the
      protocol 5 (colored). (D) Level of density selected to visualize
      the map in B and C.

   | To look for remnant densities in the area of hexons we have to
     complete the protocol with the indicated params (. As in the
     previous use case, we have selected half of input resolution (4 Å)
     although other values could be tested.
   | Taking into account that the remnant densitities could be quite
     inconspicuous we are going to use two different controls this time.
     One of them will be, as in the previous use case, the deletion of 5
     residues of hexon chain , in a region presumed to be quite close to
     the remnant density that we are looking for. The second control
     will be some small aminoacid chains previously traced in the
     remnant density since we’d like to discriminate between this
     density and other new one and unmodeled. These extra small chains
     have to be included in the form param .
   | Although this time we do not have to consider a specific chain or
     applying symmetry, since we have to look for a chain similar to
     HAdV-C5 adenovirus chain , it is quite recommendable to include in
     the form param the structure 6B1T fitted to the geometrical map
     asymmetric unit, as shown in (B), and obtained from protocol 6 (A).

   .. figure:: Images_appendix/Fig313.pdf
      :alt: Completing the protocol to find renmant densities in the
      biological asymmetric unit area of the adenovirus map.
      :name: fig:app_usecase_mapsubtract_5

      Completing the protocol to find renmant densities in the
      biological asymmetric unit area of the adenovirus map.

   | Protocol execution: Follow the general procedure shown above
     (Protocol execution section) and the graphics window will open. At
     this point several maps and atomic structures will be shown, as the
     panel indicates ( (A, bottom)), except the . Have a look to each
     map and structure to identify them and play with the density levels
     to maximize the differences between the input () and the atomic
     structure-derived map (). The (A) show the difference obtained. The
     zoom in on the framed area displays in detail the difference
     considering two different map levels (B and C). To have this view,
     besides select the molecules to show according to the panel (A,
     bottom), write in command line:
   | HAdV-C5 adenovirus chain can be visualized as .

   The result, described in , doesn’t demonstrate a clear continuous
   density in the proximity of the HAdV-C5 adenovirus chain . Although
   not very evident, it could be there. Then we cannot conclude that it
   doesn’t exit, only that we were unable to identify it.

   .. figure:: Images_appendix/Fig315.pdf
      :alt: (A) Gaussian filtered difference map (grey) of adenovirus
      HAdV-F41 asymmetric unit (top) and panel of items loaded in
      including the (bottom). (B) Zoom in on the subtracted area with
      the map density level indicated in the below . (C) Idem with a
      higher cleaning of the background. The red arrow points at the
      control density. The green arrow points at the HAdV-C5 adenovirus
      chain . The purple arrow points at one of the adenovirus HAdV-F41
      small chains previously traced.
      :name: fig:app_usecase_mapsubtract_6

      (A) Gaussian filtered difference map (grey) of adenovirus HAdV-F41
      asymmetric unit (top) and panel of items loaded in including the
      (bottom). (B) Zoom in on the subtracted area with the map density
      level indicated in the below . (C) Idem with a higher cleaning of
      the background. The red arrow points at the control density. The
      green arrow points at the HAdV-C5 adenovirus chain . The purple
      arrow points at one of the adenovirus HAdV-F41 small chains
      previously traced.
