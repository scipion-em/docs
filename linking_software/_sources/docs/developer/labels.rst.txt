.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _labels:

==========
Labels
==========

Labels and graph visualization improvements
============================================

We have added labels to our main Scipion project window. We hope it will help you to locate and identify easily the protocols inside your big projects. You will be able to create labels and assign a name and a color to them. Then, you can assign one or more labels to each protocol.

.. figure:: https://cloud.githubusercontent.com/assets/785633/14885342/28ab1edc-0d4b-11e6-971c-40ab3d2c6244.png
   :align: center
   :width: 800
   :alt: Labels feature.

Create labels
-------------
To create a label you can use the window menu called Project >> Manage project labels. Additionally you can right click on a protocol box and then click on "Assign label".
Both actions will pop up the labels window that will allow you to edit, create or delete labels. A label is form of 2 attributes, a name and a color.

Visualization mode
-------------------
Now, you can activate the "label visualization mode" by pressing *Ctrl+t* or clicking on menu Project>>Toggle color mode. This view will color the protocols based on its labels. If you click *Ctrl+t* again, now the protocols are colored by age (the younger the bluest). To go back to the standard color mode (box colored by status) press *Ctrl+t* again.


Assign labels
-------------
To assign labels you need first to select one or more protocol boxes. Once selected, right click on one of them. A context menu should appear offering you the "Assign labels". Click on that menu and the "labels" dialog should appear. Select all the labels you want to assign to all the selected protocols and click OK.

If a protocol has no label, the box will be grey. If a protocol has one label assigned, the full box will be colored with the label's color. If otherwise (more than one label), a colored line per label will be shown for each label assigned to that protocol.

Note that you can edit or even add labels on the same moment of the assignment.