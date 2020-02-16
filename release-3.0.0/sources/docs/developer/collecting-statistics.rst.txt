.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _collecting-statistics:

==========================
Collecting statistics
==========================

If activate by the user, Scipion will collect information on the usage of the different protocols and send the information to the developer's team. We collect and analyze this information to better understand the usage of the different protocols and prioritize maintenance and support. You can choose to enable or disable the collection of information at any time.

.. contents:: On this page:


Enabling or Disabling the Collection of Information
---------------------------------------------------

You can enable or disable the collection of information at any time. If you wish to modify the default preference edit the file
$HOME/.config/scipion/scipion.conf and set the variable
SCIPION_NOTIFY to True/False is you wish to activate/deactive the collection of information.


Information collected
------------------------

The information we collect is anonymous and cannot be used to identify you or
your data. In addition to the data sent, the http header is used to guess
`the country in which Scipion has been installed <http://scipion.i2pc.es/report_protocols/scipionUsage/>`_.
If activated, Scipion will transmit just the name of the protocols used without including
the parameters. The following line is an example of the data transmitted.

.. code-block:: bash

    ["ProtImportVolumes", "XmippProtConvertPdb", "XmippProtCropResizeVolumes",
    "XmippProtConvertPdb", "ProtImportVolumes", "XmippProtCreateMask3D",
    "XmippProtMaskVolumes"]

If you want to know the information sent regarding a particular project you may
check the projects Logs directory. There, you will find a file called
**data.log** with all the information sent.


Mechanism Used to Send Information
----------------------------------

Scipion tries to connect once per day with one of our  webservice (at present installed
at URL: http://scipion.i2pc.es/) and reports all the protocols used since the last connection. The process is run in the background and will not try to reconnect if it fails.

Usage Statistics
-----------------
At URL http://scipion.i2pc.es/report_protocols/protocolTable/ you may see the usage statistic that has been collected since this service has been activated. Protocols at the top of this table will receive prioritized support

