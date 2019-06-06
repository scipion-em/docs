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

Launching workflows
-------------------

Scipion can launch streaming workflows in several ways. The most basic one is
achieved creating an empty project to start a new workflow with an *Import Movies*
protocol pointing to the microscope’s deposition directory. Since we want to process
the movies that are currently located at that directory but, also, those movies
that are continuously arriving, we must activate the streaming mode in the streaming tab as
shown in the figure below. Afterwards, the rest of the protocols can be
added to the workflow in the same way that in the non streaming workflows,
but now all the protocols will wait for new data to process.

.. figure:: /docs/images/streaming-tab.png
   :align: center
   :width: 900
   :alt: streaming tab

Tthe two main parameters associated to the streaming mode are:

* **Timeout**: The time to wait after not receiving new images to close the acquisition.
* **File timeout**: Scipion is checking if a new file is growing up. If it do not change after this time, Scipion will consider that it is ready to be imported.

Usually the general *timeout* is a huge value (43,200 seconds = 12 hours) in
order to prevent ending the acquisition in an eventual acquisition issue at the microscope side.
Therefore, EM operator has this time to solve the issue.

When we know that the acquisition is finished, we can manually stop the processing
by selecting the *Import > right-click > STOP STREAMING*.

The procedure of creating manual workflows might be tedious for a facility,
where the same workflow will be usually employed for most users (or a small
number of different workflows).
For this reason, Scipion is able to automatically launch whole workflows by means of (at least)
3 ways:

* Launching static templates.
* Launching dynamic templates.
* Launching Python scripts using the Scipion's API.

Static templates
================

You can design a workflow by using Scipion as usual. Add an import, add some
processing protocols, add the summary monitor... When you are happy with your
workflow, you can export it by selecting all protocols that you want to export
(*ctrl+click* to select more than one) and, then, click the *Export* button at top.
You can save it as a template (a JSON file) at any directory on your system.

.. figure:: /docs/images/export-and-exportUpload-button.png
   :align: center
   :width: 900
   :alt: export workflows

Additionally, Scipion has a public workflows repository at http://workflows.scipion.i2pc.es.
The workflows are classified in different categories, such as **Data Collection**,
2D classification, 3D classification, Model Building... If you click a certain
workflow, you can see a preview of that workflow at left side. Use the *mouse-wheel*
to zoom in/out, *click and drag* an empty zone to move and click on a box/protocol
to inspect the internal parameters. You can download a certain workflow to any
directory on you system. In addition, anyone can upload workflows (without any
log up) by selecting all the protocols in your Scipion's project
and by clicking *Export & Upload*.

In order to launch any template (downloaded or made by yourself), open Scipion
and create an empty project. Then, you can import the workflow in *Project >
Import Workflow* and browsing to where the template is stored/downloaded
(Scipion's templates are *JSON* files). As the template is opened, the workflow
is loaded to the project as *saved* protocols. At this point, you can check/modify
any parameter of a certain protocol by opening the protocol form by *right-click > Edit*.
When you are happy with all the parameters, store the protocol by clicking **Save**
(do **not** click Execute/Schedule). When you are happy with all protocols,
select the *Import* protocol, *right-click > Restart workflow*.
Then, the *Import* should start to import data and the rest of the protocols should
change to the *Schedule* mode. A scheduled protocol is waiting for ready
inputs. Therefore, when all inputs become ready for it, that protocol should
automatically start to process the incoming data.

Alternatively, a JSON template can be launched from the command line as follow

.. code-block:: bash

    scipion python pyworkflow/project/scripts/create.py name="myAcquisition" workflow="path/to/your/workflow.json"
    scipion python pyworkflow/project/scripts/schedule.py myAcquisition
    scipion project myAcquisition

where the first command creates the project, the second starts the processing and
the third opens the Scipion GUI to see the project.

Dynamic templates
=================

Usually, we always must set the same parameters that are specific of each acquisition
such as, deposition path, gain image path, dose per frame, particle size...
Then, in order to avoid manually editing this parameters using the procedure
explained for the static templates (previous section), Scipion has a mode to
open modified templates in such a way that an initial form is launched asking
for that specific parameters at once.

To see a demo of this you just have to run:

.. code-block:: bash

    scipion demo

This will pop up a small wizard like the one below ready to go.

.. figure:: https://user-images.githubusercontent.com/785633/33311258-87304f44-d424-11e7-844a-8360708fa7ed.png
   :align: center
   :alt: Cryo EM Streaming demo wizard


You can fill the form according to your data or just leave all the displayed
fields untouched since it goes right with the test data. Once you click on the
*Start demo* button Scipion should appear with the new project loaded and running in
streaming mode.

*Import movies* should already be importing files and the rest are scheduled. As soon as there
is any input available, the protocols will start processing it and making it
available for the next protocol in line. Also, the *Monitor summary* is
monitoring the progress and generating an HTML report with the outcome of the data.

**(\*) Requirements for the demo**:

To run the demo as it is, you need to have installed:

* scipion-em-motioncorr
* scipion-em-grigoriefflab
* scipion-em-eman

.. code-block:: bash

    scipion installp -p scipion-em-motioncorr -p scipion-em-grigoriefflab scipion-em-eman2

*Notice that motioncor2 needs GPU acceleration.*

In addition, the demo use either the jmbFalconMovies dataset for v1.2-Caligula
version or the relion13_tutorial dataset for later versions (also for devel branch).
Thus, you can download the dataset that you need by

.. code-block:: bash

    scipion testdata --download jmbFalconMovies relion13_tutorial


**Adding custom dynamic templates**

The dynamic template explained above is just an example, but you can create your
custom dynamic templates according with your preferences, the system requirements...
using static templates (explained in the previous section above) as a starting
points to create the dynamic ones. A Scipion's template is a *JSON* file, which
are composed by a list of all the protocols in the workflow.
In the figure below, we have highlight the *Import movies* protocol with a blue
box, where are listed in all the internal parameters/fields for the import.

.. figure:: /docs/images/custom-scipion-demo.png
   :align: center
   :width: 900
   :alt: custom scipion demo

In a common *JSON* file, all fields are made of key-value pairs where *key*
(what is before ':') is always a *string* and the *value* (what is after ':')
can be a *string* ("something coated"), a *number*, a
*Boolean* (true or false) or *null* (`more info <https://www.json.org>`_).
Additionally, we have created a syntax to add dynamic fields to that *JSON* file. Then, to add a
dynamic field, you just have to substitute the value (what is after the ':') of
a certain field for a string starting and ending by '~', and with three strings
separated by '|', something like

.. code-block:: bash

    "~label|defaultValue|typeValue~"

where *label* is the name of the filed in the form, *defaultValue* is the
default value inserted in the field and *typeValue* is a number fixing the type of the value
(0 for *strings*, 1 for *booleans*, 2 for *paths*, 3 for *integers*, and 4 for *floats*).

In the figure above, there are three examples for the *filesPath*, *dosePerFrame*
and *gainFile* fields. Notice that the type for the *filesPath* field is set to
2, which means *path*, then Scipion will check that this path exists before starting
to process. *gainFile* is set to 0 (*string*) to allow an empty value (to skip
using a gain image if not needed). Finally, the 4 (*float* type) set to the *dosPerFrame* allows to
introduce non integer values.

When you are happy with the modified *JSON* file, you must save it to

.. code-block:: bash

    $SCIPION_HOME/pyworkflow/templates

where *$SCIPION_HOME* is where you have installed Scipion. The extension of the
file must be **.json.template**.

When more than one dynamic template is in the *$SCIPION_HOME/pyworkflow/templates*
directory, then running

.. code-block:: bash

    scipion demo

opens a menu to choose the dynamic template to launch

.. figure:: /docs/images/multiple-choice-scipion-demo.png
   :align: center
   :width: 900
   :alt: multiple choise scipion demo


Using Scipion's API
===================

A Scipion's project can be created, designed (adding protocols) and launched by
a Python script by using the `Scipion's API <https://scipion-em.github.io/docs/api/pyworkflow.html>`_.

We have a repository destined to share Scipion's code used in
`EM-facilities <https://github.com/I2PC/em-facilities>`_.
Specially, we have an example of creating a Scipion's project using the API
`here <https://github.com/I2PC/em-facilities/blob/master/usingAPI_demo/acquisition_workflow.py>`_.
This code is loaded by the `form_launcher.py` at same directory and it can be run
by

.. code-block:: bash

    scipion python $EM_FACILITIES/usingAPI_demo/form_launcher.py [scipionbox.conf]

where the optional *scipionbox.conf* parameter is a config file that will be read
in order to retrieve some configuration parameters. If not provided, a default
file in the same directory is used.
