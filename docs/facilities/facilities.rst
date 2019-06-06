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

On top of that, we have added the concept of monitors, the special protocols
that constantly check how the execution of other protocols is going. We have
developed several GUIs that are refreshed periodically and produce a graphical
summary (e.g, CTF defocus values, system load etc). A summary is also generated
in HTML format that can be easily copied to a public website to provide access
for external users.

To see the HTML summary report from Scipion you must launch the *Summary monitor*
protocol (or select it if it is already in the workflow), click on the
*Analyze results* button (down-right) and, then, click on the "Open HTML report"
button. A browser will show you something
like `this <http://scipion.cnb.csic.es/scipionbox/lastHTMLReport/>`_.

The *HTML report* can be customized following `this guide <customize-html-report>`_.

Learn `how to create and launch streaming workflows <facilities-workflows>`_.