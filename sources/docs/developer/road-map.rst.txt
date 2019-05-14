.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _road-map:

====================
Scipion roadmap 2018
====================

We have planned the next achievements for the next year: Scipion 2018 release.

Facilities running Scipion in streaming, and HAPPY
--------------------------------------------------
We want to have more facilities, 10?, running scipion in streaming

Pluginization:
--------------

We want to make each of the EM packages a plugin, and therefore releasing them from Scipion release cycle.

* Divide and conquer strategy
* Each EM package would be a plugin:

    * Binaries
    * Configuration
    * Tests
    * Scipion wrappers

* Independent releases, no need for new scipion release
* Plugin repository -version control


More agile workflow management
-------------------------------

* Relax execution constraints: children blocking parent?
* run all workflow
* rerun all
* Link nodes without output yet
