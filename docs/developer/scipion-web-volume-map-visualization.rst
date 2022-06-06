.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _scipion-web-volume-map-visualization:

=====================================
Scipion web volume map visualization
=====================================

Objectives
==========

Scipion web client environment can have some limitations compared to the
desktop client environment. One of these hypothetical limitations is the
possibility of using client machine tools to visualize some Scipion
files.

In volume visualization, it is possible to use some tools
that allow the user to open and interact with volumes in a web client. Here,
we will see several alternative ways to do so:


Open Astex viewer
=================

`Open Astex Viewer <http://openastexviewer.net/web/>`_ is a Java molecular
graphics program that assists in structure-based drug design. It can be
used as an applet in a web page or as a desktop application.


Advantages
----------
1. We are familiar with Open Astex Viewer because we have another project in the
   laboratory that uses it: `PeppeR <http://pepper.cnb.csic.es/das/PeppeR/>`_.
2. It can be displayed as an applet in a web page.
3. It can be customized.
4. It allows interaction.


Disadvantages
--------------

1. When it is displayed as an applet it has all the disadvantages of an
   applet.
2. When it is used as an applet it has some restrictions that we
   will see below in the Installation section.

Installation
-------------

We are not going to use the Open Astex Viewer jar published on their
official web page because we have detected some problems with it, so we
will use `EMDB jar <http://www.ebi.ac.uk/pdbe/entry/applets/OpenAstexViewer.jar>`_.

Since we are working with Django, the installation is referred in to this
framework.

1. Place jar file in the Django static folder (Django: STATIC_ROOT = 'static').

2. In the html code include the applet code (here is an example):

.. code-block:: bash

    <applet
           width="600px" height="600px" name="av"
           archive="{{ STATIC_URL }}astex/OpenAstexViewer.jar"
           codebase=".."
           code="MoleculeViewerApplet.class">
           <param name="script"
                 value="map load volMap '{{volLink}}' {{form.volType.value}} {{form.threshold.value}};
                        map volMap contour 0 solid on;
                        radius 50;
                        center map volMap;
                        view -background lightgrey;
                        map volMap -reread true;">
    </applet>

*NOTES*

Jar and script file paths must be defined using a "static" value set in
Django "settings.py" file. To load the applet you can add a parameter (HTML element) called "script" and set it to the script code you want to use or you can use a "scriptfile" parameter and set its value to the script file path.

Script file and volume maps must be placed in jar location sub-folders and
volume files path must follow "/staticUrl/path" format.

Problems
-----------

Continuous conflicts with java navigator and installed JRE versions.

Now we get errors executing commands in the visualizer after loading it
(even in 3demloupe web).

Chimera
--------

`UCSF Chimera <http://www.cgl.ucsf.edu/chimera/>`_ is a program for interactive
visualization and analysis of molecular structures and related data.
This program has an export option where you can export a volume path as
a webGL page; this functionality will allow us to visualize volume maps
in a web page.

Advantages
-----------

1. It does not use an applet; it is html, css and javascript code.
2. It has no restrictions.


Disadvantages
-------------

1. It must be installed on the server machine.
2. It does not allow complex interactions.

Installation
---------------

1. We must install a headless Chimera version; this version is for servers or other places where we do not need a user GUI, and it avoids   some problems for our operations.

2. Our code must open Chimera, load the volume map, export it, take the needed code from exported file, and add it to our html code. Here is an example code:

.. code-block:: bash

    p = Popen(['chimera', '--start', 'ReadStdin', volPath], stdout=PIPE, stdin=PIPE, stderr=PIPE) # Read problems section. This has changed.
    outputHtmlFile = '/home/ballotelli/tmpDir/test.html'
    threshold = exampleThreshold
    stdout_data = p.communicate(input='volume #0 level ' + str(threshold) + '; export format WebGL ' + outputHtmlFile + '; stop')[0]
    f = open(outputHtmlFile)
    chimeraHtml = f.read().decode('string-escape').decode("utf-8").split("</html>")[1]

We are going to look at each line function:

. Execute Chimera, telling it to run ReadStdin utility upon starting (to read commands from Stdin) and passing the file to open.

. Define a temporal html file path for the webGL exportation.

. Define an initial threshold value.

. Execute Chimera commands to apply a threshold to the volume, export to a webGL html file, and close Chimera.

. Open the exported file to read it.

. Extract the html code that we need. After this you can include this html in your page, adding more static code (code that is always the same) taken from the exported file that is needed for the correct webGL visualization.

Problems
--------

1. With an incorrect threshold we will see a black result. With a very
  bad threshold we will not see anything.

2. After some use, ReadStdin utility command has been
  removed because we had some problems, but we must know it. Now we use
  this instruction:

.. code-block:: bash

    p = Popen(['chimera', inputVolume], stdout=PIPE, stdin=PIPE, stderr=PIPE)

