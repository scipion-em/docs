.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _facilities:

====================
Streaming Processing
====================

For facilities
---------------
Currently, scipion is being used every day in several facilities in Europe, US,
Canada, Israel and Australia. If you are running a Cryo EM facility and want more
info, please `contatct us <scipion@i2pc.com>`_. We will be happy to help you run
Scipion there. Also, we have a `Slack <https://scipion.slack.com>`_ framework to
maintain a direct communication channel.

.. figure:: /docs/images/facilities_map.png
   :align: center
   :width: 900
   :alt: facilities map

Streaming processing
--------------------

Scipion is able to process data in streaming, i.e, at the same time movies
(or micrographs) are coming from the microscope PC. It can also be called
on-the-fly processing. This allows to overlap computing time with the
acquisition (reducing computational needs) and also to detect problems at
early stages. This idea is implemented in different labs mainly by using
custom-made scripts, but also it can be implemented using templates in a very
easy way. The advantage of our Scipion solution is that you have
the usual flexibility to choose what operations to do and the traceability to
re-do some of the steps later. It is basically the same Scipion interface with
one key change: the output is produced as soon as the first element is
available, and it is later updated with new output elements. This allows
concatenating several operations before the first one is completed.

Learn `how to create, import, export and launch streaming workflows <facilities-workflows>`_.

Scipion v.2.0 - Diocletian `updates/introduce a big number of streaming tools
<release-notes#streaming>`_. We review and analyze in deep the use and the
combination of these on-the-fly tools and protocols for facilities in the
`D. Maluenda et.al. 'Flexible workflows for on-the-fly electron microscopy
single particle image processing using Scipion' Acta Cryst. (2019). Dxx, yy-zz
<linkToPaper>`_ paper.

On top of that, we have paid special attention to the data flow management with
the `Trigger data <https://github.com/I2PC/scipion-em-xmipp/blob/648ebe3a4f8dc2f3022332c080fb3d300d273bd7/
xmipp3/protocols/protocol_trigger_data.py#L41-L53>`_ protocol, the `Movie max shift
<https://github.com/I2PC/scipion-em-xmipp/blob/648ebe3a4f8dc2f3022332c080fb3d300d273bd7/
xmipp3/protocols/protocol_movie_max_shift.py#L43-L53>`_ protocol, the
`CTF consensus <https://github.com/I2PC/scipion-em-xmipp/blob/648ebe3a4f8dc2f3022332c080fb3d300d273bd7/
xmipp3/protocols/protocol_ctf_consensus.py#L49-L51>`_ protocol, the
`Extract coordinates <https://github.com/I2PC/scipion/blob/d1a60f69960d1079bbbecde5bf3f5f4017b36927/
pyworkflow/em/protocol/protocol_extract_coordinates.py#L44-L49>`_ protocol in
streaming and `2D classification <https://github.com/I2PC/scipion-em-xmipp/blob/648ebe3a4f8dc2f3022332c080fb3d300d273bd7/
xmipp3/protocols/protocol_classification_gpuCorr_semi.py#L68-L70>`_ protocol in
streaming.

In addition, we have work more in the concept of consensus protocols, for
merging and combining different approach (from different EM softwares) to do the
same tasks, in order to get an improved result based on that different results.
The consensus protocols family are for *CTF estimation*, *Picking*,
*Initial Volume* and *3D classes*, so far.

Moreover, we are also working in the monitor protocols, the special protocols
that constantly check how the execution of other protocols is going. We have
developed several GUIs that are refreshed periodically and produce a graphical
summary (e.g, CTF estimated values, system load, etc).
This summary is generated in *HTML* format to be easily copied to a
`public website <http://scipion.cnb.csic.es/scipionbox/lastHTMLReport/>`_.
Learn `how to customize the HTML report <customize-html-report>`_ according to
your facilities' needs.

Finally, this `tutorial focused on streaming processing <facilities-tutorial>`_
simulates a cryo-EM acquisition in order to sum up all the available facilities
tools.
