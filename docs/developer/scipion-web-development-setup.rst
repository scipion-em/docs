.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _scipion-web-development-setup:

======================================
Scipion web development setup
======================================

Scipion web requires you to have Scipion installed in the server. For that you
will need to `install Scipion <https://scipion-em.github.io/docs/docs/scipion-modes/install-from-sources.html>`_.
After this you should have Python, Django and all the modules required to run Scipion web.

Django scripts need write permission in ``$SCIPION_HOME``

Matplotlib
==========

Matplotlib also needs write permission (by default, to ``~/.matplotlib``)

Matplotlib also needs to deafult to Agg backend:

from scipion folder:

.. code-block:: bash

    cp software/lib/python2.7/site-packages/matplotlib-1.3.1-py2.7-linux-x86_64.egg/matplotlib/mpl-data/matplotlibrc ~/.matplotlib/
    vi ~/.matplotlib/matplotlibrc

    Set --> backend      : agg

    save it

Webtools setup
================

You will need to set up your machine to be able to run the web-tools, so far
you will need to create some folders and add some files to those folders

Create web tools folders
-------------------------

Open a console a run these commands

.. code-block:: bash
    mkdir ~/.config/scipion/myfirstmap
    mkdir ~/.config/scipion/myresmap
    mkdir ~/.config/scipion/movies

You will also need to have a host.conf file on each of those folders, let's copy
the main one from scipion.

From the $SCIPION_HOME:

.. code-block:: bash

     cp config/hosts.conf ~/.config/scipion/myfirstmap/
     cp config/hosts.conf ~/.config/scipion/myresmap/
     cp config/hosts.conf ~/.config/scipion/movies/

Create a /services folder for the movie alignment project samples and give it x
permissions:

.. code-block:: bash

    sudo mkdir /services
    sudo chmod 777 /services

Install necessary packages
--------------------------

.. code-block:: bash

    $SCIPION_HOME/scipion install eman2.12 resmap pytz

Define "Thread and MPI" options per protocol (Optional but recommended)
------------------------------------------------------------------------

You can additionally force how each of the protocol of the webtools should run in terms of "Thread and MPI".

Add the configuration as a "section" in $SCIPION_HOME/config/scipion.conf.
An example of this configuration could look like this.

.. code-block:: bash

    [WEB_PROTOCOLS]
    XmippProtRansac = {"useQueue": 0, "numberOfThreads": 4, "numberOfMpi": 1, "queueParams" : ["cpu", {"JOB_MEMORY": "8192", "JOB_TIME": "72"}]}
    EmanProtInitModel = {"useQueue": 0, "numberOfThreads": 4, "numberOfMpi": 1, "queueParams" : ["cpu", {"JOB_MEMORY": "8192", "JOB_TIME": "72"}]}
    XmippProtReconstructSignificant = {"useQueue": 0, "numberOfThreads": 1, "numberOfMpi": 4, "queueParams" : ["cpu", {"JOB_MEMORY": "8192", "JOB_TIME": "72"}]}
    XmippProtAlignVolumeForWeb = {"useQueue": 0, "numberOfThreads": 4, "numberOfMpi": 1, "queueParams" : ["cpu", {"JOB_MEMORY": "8192", "JOB_TIME": "72"}]}
    ProtMovieAlignment = {"useQueue": 0, "numberOfThreads": 1, "numberOfMpi": 1, "queueParams" : ["gpu", {"JOB_MEMORY": "8192", "JOB_TIME": "72"}]}
    XmippProtCreateMask3D = {"useQueue": 0, "numberOfThreads": 1, "numberOfMpi": 1, "queueParams" : ["cpu", {"JOB_MEMORY": "8192", "JOB_TIME": "72"}]}
    ProtResMap = {"useQueue": 0, "numberOfThreads": 1, "numberOfMpi": 1, "queueParams" : ["cpu", {"JOB_MEMORY": "8192", "JOB_TIME": "72"}]}

Run the webserver
===================

If it is the first time you start the server you first need to run:

.. code-block:: bash

    ./scipion webserver collectstatic

The recommended procedure is to setup a replica of the production
environment on your development machine. Actually it takes little work,
and you will be doing the test in the same environment as production.


To generate the database that Django will use (used when uploading a file), run

.. code-block:: bash

    ./scipion webserver syncdb

The simplest way to test your installation is to run Scipion in web-server mode:

.. code-block:: bash

    ./scipion webserver


After this you should have it running at http://localhost:8000/webtools/

(Note: the script starts the web server listening to 0.0.0.0, so it
might be accessible from other computers too)

Other useful commands
=====================

To list all available Django commands,

.. code-block:: bash

    ./scipion webserver help

You can run any Django command if you type it after webserver: useful for collectstatic content.

.. code-block:: bash

    ./scipion webserver <Django command>