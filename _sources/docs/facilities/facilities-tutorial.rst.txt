.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _facilities-tutorial:

===================
Facilities Tutorial
===================


(*TODO: Put here a tutorial for launching the
``scipion3 template $EMFACILITIES_HOME/template/to_2Dclassification_DoseWeithed.json.template [parameters]``*)













Making a custom protocol
------------------------

We aim to introduce a few concepts that we think will give any IT/developer a good set of resources to adapt Scipion to you facility setup. Scipion scope is confined to Image processing but in a facilities context, there are other actors in place that Scipion might need to adapt or even communicate. For that, we need to launch Scipion at some point in the facility pipeline or customize part of its outputs, or even send/grab information from a LIMS/ERP system that handles visits/sessions or sample information. We will go through 3 main concepts and learn how to create new element into Scipion:

* Developing a Protocol

  * `Create a Basic Protocol <https://scipion-em.github.io/docs/docs/developer/creating-a-protocol.html>`_

   Things to do here common to the rest:

    * create a package: em/packages/myfacility

* [Streamifying a protocol]
* `Developing a monitor <https://scipion-em.github.io/docs/docs/developer/creating-a-monitor.html>`_
* `The Summary monitor and report customization <https://scipion-em.github.io/docs/docs/developer/customize-html-report.html>`_
