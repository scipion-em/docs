.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _facilities:

====================
Streaming Processing
====================

For facilities
---------------
When we develop these functionalities we are thinking about facilities.
Currently, scipion is being used every day in several facilities in Europe,
and more are joining from US and Canada. If you are running a Cryo EM facility
and want more info, please link:Contact-Us[Contact us]. We will be happy to
help you run Scipion there.


Streaming processing
--------------------

In the last months, we have been working on an extension of Scipion to process
data in streaming, i.e, at the same time movies (or micrographs) are coming
from the microscope PC. This allows to overlap computing time with the
acquisition (reducing computational needs) and also to detect problems at
early stages. This idea is implemented in different labs mainly by using
custom-made scripts. The advantage of our Scipion solution is that you have
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
for external users. See an example `here <http://scipion.cnb.csic.es/scipionbox/lastHTMLReport/>`_.

Launching the demo
------------------
*NOTE: This information is only available since v1.2-Caligula version.*

Requirements
-------------

To run the demo as it is, you need to have installed:

* scipion-em-motioncorr

* scipion-em-grigoriefflab

* scipion-em-eman

.. code-block:: bash

    scipion installp -p scipion-em-motioncorr -p scipion-em-grigoriefflab scipion-em-eman2

``Notice that motioncor2 needs GPU acceleration.``

In addition, the demo use either the jmbFalconMovies dataset for v1.2-Caligula version or the relion13_tutorial dataset for later versions (also for devel branch). Thus, you can download the dataset that you need by

.. code-block:: bash

    scipion testdata --download jmbFalconMovies relion13_tutorial


Usage
------

After installing all the requirements you just have to run:

.. code-block:: bash

    scipion demo

This will pop up a small wizard like the one below ready to go.

.. figure:: https://user-images.githubusercontent.com/785633/33311258-87304f44-d424-11e7-844a-8360708fa7ed.png
   :align: center
   :alt: Cryo EM Streaming demo wizard


You can leave all the displayed data untouched since it goes right with the test data. Once you click on the "Start demo" button scipion should appear with the new project loaded running in streaming mode:

.. figure:: https://user-images.githubusercontent.com/785633/32671892-61e856fc-c649-11e7-88bf-a161e2f3e2d1.png
   :align: center
   :alt: Cryo EM workflow in streaming

Import is already importing files and the rest are scheduled. As soon as there is any input available, the protocols will start processing it and making it available for the next protocol in line.

The "Monitor summary" is monitoring the progress and generating an HTML report with the outcome of the data.

To see the HTML summary report from Scipion you must first select (click) on the Summary monitor box, and once it is selected, click on the "Analyze result" button (down-right). A window like this will pop up:

.. figure:: https://user-images.githubusercontent.com/785633/33026513-e0c59966-ce10-11e7-9850-2a4bda805247.png
   :align: center
   :alt: Summary monitor results window


Then click on the "Open HTML report" button. A browser will show you something like (link:http://scipion.cnb.csic.es/scipionbox/lastHTMLReport/[this])


Kicking off scipion in your pipeline
-------------------------------------

There are a couple of useful scripts that might be useful to start scipion right after the acquisition has started. In summary, you may want to somehow follow this steps:

1. Ask for some basic input: In our experience, so far, there is still the need of asking the user/microscopist for some basic data before Kicking off scipion. This is the case for sampling rate, or dose or even based on the flexibiliy you want to offer in your pipeline many other options like "use Gctf" or "use CTFfind4" or both....this is really up to you and Scipion does not implement any of this.
   The mechanism to ask for is not part of scipion, although there are some sample scripts that could be useful as an staring point, but we doubt that will be perfect as they are for your case. You will need to adapt them to your needs. The demo script (scripts/scipionbox_wizard_demo.py) might be the simplest one and does not require any config file, but it is very tied to demo purposes. Other scripts are similar to real scripts used in facilities, like (scripts/cipionbox_wizard_scilifelab.py) and are based on TK GUI. In some other facilities, the have a webserver eith an HTML form to request for this data. It is really up to your pipeline design. Alternatively, it can be done by modifying some fields of an existing JSON template in order to launch a form to be filled by the user. The syntax to replace a static field to a form field is as follow: replace any value of the JSON file by

    .. code-block:: bash

        ~label|defaultValue|typeValue~

   where 'label' is what will be shown in the form, 'defaultValue' will be the default value and 'typeValue' is an integer fixing the type of the value (0 for a string, 1 for a path, 2 for a boolean, 3 for an integer, and 4 for a float). Then, the form can be launched by

    .. code-block:: bash

        scipion python scripts/scipionbox_preprocess_basic.py path/to/workflow.json

2. Create the project using the input: the second step would be to use those values captured and create a scipion project accordingly. In this case you have 2 options:

   * *A*.- Use SCIPION as an API to create the project following your pipeline design. This is the case for: https://github.com/delarosatrevin/scipion-session or https://github.com/azazellochg/scipion-session-lmb

   * *B*.- Generate a "json" file, usually based on a template, that will be completed with the data requested in the previous step. This is the case of the demo script(scripts/scipionbox_wizard_demo.py). Is in this case that, once you have your "workflow.json" you can run a script to create the project based on that workflow like:

        .. code-block:: bash

            scipion python scripts/create_project.py name="session1234" workflow="path/to/your/workflow.json"

3. The final step would be to "Start" all protocols to kick off the processing: For the *B* case, there is another script that will do that:

    .. code-block:: bash

        scipion python scripts/schedule_project.py name="session1234"+

If using scipion as an API, you may want to Start the protocols at the same step (*A* case)

After this, you will have Scipion up and running actively looking for new acquisitions and following the steps in your customized workflow.


If you look for inspiration, you can find workflow examples in the scipion workflows repository: http://workflows.scipion.i2pc.es/
