
.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _customize-html-report:

=========================
How to Customiza the Activity Reports
=========================

.. :contents:: Table of Contents

Intro
-----
There is a type of protocols called monitors which are used to produce live analysis plots, generate reports or raise alerts when some problems are detected. A monitor example is the **CTF-monitor**, that checks the computed defocus values for each micrograph as they are generated. **CTF-monitor** may raise an alert if the defocus values are above or below certain thresholds. An special case of this monitors is the **monitor summary** which encapsulates the **CTF Monitor**, the **system monitor** and the **movie gain monitor** and continuosly creates a report.

In this section, we will focus on the technical details regarding how these reports are generated and the options we have to customize them. 

Implementation
--------------

 The above mentioned summary has been implemente in two diferent flavours:  The first one uses pure HTML while the second one takes advantage of `Grafana <https://grafana.com/>` (an open source analytics and monitoring framework). For those facilities with a HTML server already installed the HTML solution will be easier to implement although less configurable. Examples of monitors reports generated in *HTML* format can be seen at
`http://scipion.cnb.csic.es/scipionbox/lastHTMLReport/ <http://scipion.cnb.csic.es/scipionbox/lastHTMLReport/>`_ while in URL `http://scipion.cnb.csic.es:3000/lastHTMLReport/ <http://scipion.cnb.csic.es:3000/lastHTMLReport/>`_ you can see a Grafana based report. Note that those facilities which already use a LIMS-like solution (laboratory information management system) may find the Grafana based solution easier to customize in order to integrate their LIMS system with scipion.

Implementation detail of the different monitor report system may be found in the follwing two links:

* `Pure HTML based <customize_report_html>`
* `Grafana, Influxdb based <customize_report_grafana>`

