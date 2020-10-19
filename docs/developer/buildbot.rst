.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _buildbot:

=================================
Buildbot
=================================

BuildBot is a system to automate the compile/test cycle required by most
software projects to validate code changes. By automatically rebuilding and
testing the tree each time something has changed, build problems are pinpointed
quickly, before other developers are inconvenienced by the failure.

From early stages in the development of Scipion, we have included a number of
automatic tests into this tool that executes periodically those tests. Those
executions can be examined in http://scipion-test.cnb.csic.es:9980/#/

Our buildbot architecture consists of a single **buildmaster** and one **worker**
connected in a star topology. The buildmaster makes all decisions about what,
when, and how to build. It sends commands to be run on the worker, which
simply execute the commands and return the results. (certain steps involve
more local decision making, where the overhead of sending a lot of commands
back and forth would be inappropriate, but in general the buildmaster is
responsible for everything).

.. figure:: /docs/images/buildbot/buildbot_architecture.png
   :width: 250
   :alt: System Architecture
   :name: System Architecture

The worker runs on a separate machine where the master runs. This machine connect
to the buildmaster over a TCP connection. The TCP connections are initiated by
the worker and accepted by the buildmaster, but commands and results travel both
ways within this connection. The buildmaster is always in charge, so all
commands travel exclusively from the buildmaster to the worker.

The buildmaster constist of several pieces:


.. figure:: /docs/images/buildbot/build_master01.png
   :width: 250
   :alt: Build Master
   :name: Build Master

All of our repositories are on GIT. These repositories are constantly being
modified. All **Changes** are fed to the **Schedulers** which decide when builds
should be performed. They collect Changes into **BuildRequests**, which are
then queued for delivery to **Builders** until a worker is available. The
Builders control exactly how each build is performed (with a series of
**BuildSteps**, configured in a **BuildFactory**). Each Build is run on a single
worker.

Currently, our code is divided into three main branches which are tested by
buildbot:

* **support**: represents the stable code of the release 2.0.0 of Scipion (Diocletian)
* **production**: represents the stable code of release 3.0.0 (???????)
* **devel**: represents the code in development of the release 3.0.0.

For that reason, we have three `BuildFactorys` that are in charge of
automatically executing the code of the aforementioned branches:

* **supportBuilGroupFactory**: this BuildFactorys is automatically released on Sundays.
* **productionBuildGroupFactory**: this BuildFactorys is automatically released on Saturday.
* **develBuildGroupFactory**: this BuildFactorys is automatically released on Monday, Wednesday and Friday.


.. figure:: /docs/images/buildbot/build_master02.png
   :width: 250
   :alt: Complete Build Master
   :name: Complete Build Master


Adding your plugin in Buildbot
------------------------------

In order to include a Scipion plugin within buildbot and have it tested, the
following steps must be followed:


1. Make sure the plugin is on one Version Control System like GIT (to test in devel mode).
2. Make sure the plugin is on Pypi (to test in production mode).
3. :ref:`Contact white Scipion Team <contact-us>`_ in order to include it into Buildbot.




