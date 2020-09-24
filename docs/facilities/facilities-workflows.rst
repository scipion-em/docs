.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _facilities-workflows:

===================
Streaming workflows
===================

Scipion can launch streaming workflows in several ways. The most basic one is
achieved creating an empty project to start a new workflow with an *Import Movies*
protocol pointing to the microscope’s deposition directory. Since we want to
process the movies that are currently located at that directory but, also, those
movies that are continuously arriving, we must activate the streaming mode in
the streaming tab as shown in the figure below. Afterwards, the rest of the
protocols can be added to the workflow in the same way that in the non streaming
workflows (from the protocols tree at left of finding them with *ctrl+F*),
but now all the protocols will wait for new data to process.

.. figure:: /docs/images/streaming-tab.png
   :align: center
   :width: 300
   :alt: streaming tab

The two main parameters associated to the streaming mode are:

* **Timeout**: The time to wait, after not receiving new images, to close the acquisition.
* **File timeout**: Scipion is checking if a new file is growing up.
  If it do not change after this time, Scipion will consider it is ready to be imported.

Usually the general *timeout* is a huge value (43,200 seconds = 12 hours) in
order to prevent ending the acquisition in an eventual acquisition issue at the
microscope side.
In other words, this is the time you have to resume the acquisition after and
eventual pause.

When we know that the acquisition is finished, we can manually stop the online
processing, by selecting the *Import Movies > right-click > STOP STREAMING*.
Then, all protocols will be finishing, as soon as all the last data is processed.

As any Scipion project, the directory is placed at

.. code-block:: bash

    $SCIPION_USER_DATA/projects/myAcquisitionProject

(where ``$SCIPION_USER_DATA`` usually is ``~/ScipionUserData`` and
``myAcquisitionProject`` is the project name) and it is a self contained
project-directory. Thus, one can export/import a project started in
the facility computer in his/her own computer, just by coping the
project-directory to his/her own ``$SCIPION_USER_DATA/projects``.
Take into account that this directory usually does **NOT contain
the raw movies** to save disk space (this behavior can be modified in the
*Import Movies* protocol).

The procedure of creating manual workflows by adding every protocol to use it
(described above) might be tedious for a facility, where the same workflow will
be usually employed for most users (or a few of different workflows).
For this reason, Scipion is able to automatically launch whole workflows by
means of (at least) 3 ways:

* Launching `static templates <#static-templates>`_.
* Launching `dynamic templates <#creating-custom-dynamic-templates>`_.
* Launching `dynamic templates from command line <#launching-dynamic-templates-from-command-line>`_.
* Launching `Python scripts using the Scipion's API <#using-scipion-s-api>`_.


Static templates
----------------

You can design a workflow by using Scipion GUI as usual. Adding an import,
attaching some processing protocols, including the summary monitor...
When you are happy with your workflow, you can export it by selecting all
protocols you want to export (*ctrl+click* to select more than one)
and, then, click the *Export* button at top.
You can save it as a template (a *JSON* file) at any directory on your system.

.. figure:: /docs/images/export-and-exportUpload-button.png
   :align: center
   :width: 350
   :alt: export workflows

Additionally, Scipion has a public workflows repository at
http://workflows.scipion.i2pc.es.
The workflows are classified in different categories, such as **Data Collection**,
2D classification, 3D classification, Model Building... If you click on a certain
workflow, you can see a preview of that workflow. Use the *mouse-wheel* to zoom
in/out, *click and drag* in an empty zone to move and click on a box/protocol
to inspect the internal parameters. You can download a certain workflow to any
directory on you system. In addition, anybody can upload workflows (without any
log up) by selecting all the protocols in the Scipion's project
and by clicking *Export & Upload*.

In order to launch any template (as described above: downloaded or made by yourself),
open Scipion and create an empty project. Then, you can import the workflow with
*Project > Import Workflow* at the menu bar on top and browsing to where the
template is stored/downloaded (Scipion's templates are *JSON* files).
As the template is opened, the workflow is loaded to the project as *saved*
protocols. At this point, you can check/modify any parameter of a certain
protocol by opening the protocol form by *right-click > Edit* or *double-click*.
When you are happy with all the parameters, store the protocol by clicking
**Save** (do **not** click Execute/Schedule).
When you are happy with all protocols, select the *Import* protocol,
*right-click > Restart workflow*.
Then, the *Import* should start to import data and the rest of the protocols
should change to the *Schedule* mode. A scheduled protocol is waiting for ready
inputs, i.e. when all inputs become ready for it, that protocol should
automatically start to process the incoming data changing to the *Running* mode.

Alternatively, a *JSON* template can be launched from the command line as follow

.. code-block:: bash

    scipion3 python -m pyworkflow.project.scripts.create name="myAcquisition" workflow="path/to/your/workflow.json"
    scipion3 python -m pyworkflow.project.scripts.schedule myAcquisition
    scipion3 project myAcquisition

where the first command creates the project named *myAcquisition*
from the ``workflow.json`` file (in this case), the second starts
the processing of the project named *myAcquisition*
and the third opens the Scipion GUI to see the project named *myAcquisition*.


Dynamic templates
-----------------

Usually, we always must set the same parameters that are specific for each
acquisition, such as deposition path, gain image path, dose per frame, particle
size...
Then, in order to avoid manually editing this parameters by opening every protocol
in which belongs (using the procedure explained for the static templates in the
previous section), Scipion has a mode to open modified templates in such a way
that a wizard is launched asking for all that specific parameters, at once.

To see a demo of this you just have to run

.. code-block:: bash

    scipion3 template

(``scipon3 demo`` makes exactly the same than the command above)

This will pop up a small wizard like the one below

.. figure:: https://user-images.githubusercontent.com/785633/33311258-87304f44-d424-11e7-844a-8360708fa7ed.png
   :align: center
   :alt: Cryo EM Streaming demo wizard


You can fill the form according to your data or just leave all the displayed
fields untouched since it goes right with the test data (\*see requirements below).
As you click on the *Start demo* button, Scipion should appear with the new
project loaded and running in streaming mode.

*Import movies* should already be importing files, whereas the rest should be
scheduled. As soon as there is any input available for each protocol, that protocol
will start processing it and making it available for the next protocol in line.
Also, the *Monitor summary* should be monitoring the progress and generating an
*HTML* report with the outcome of the data.

**(\*) Requirements for the demo**:

To run the demo as it is, you need to have installed

* scipion-em-motioncorr
* scipion-em-grigoriefflab
* scipion-em-eman2

.. code-block:: bash

    scipion installp -p scipion-em-motioncorr -p scipion-em-grigoriefflab scipion-em-eman2

*Notice that motioncor2 needs GPU acceleration.*

In addition, the demo use either the jmbFalconMovies dataset for v1.2-Caligula
version or the relion13_tutorial dataset for later versions (also for devel branch).
Thus, you can download the dataset that you need by

.. code-block:: bash

    scipion testdata --download jmbFalconMovies relion13_tutorial


Creating custom dynamic templates
=================================

The dynamic template explained above is just an example, but you can create your
custom dynamic templates according with your preferences,
system requirements/availability... using static templates
(explained in the previous section above) as a starting
points to create the dynamic ones.

A Scipion's template is a *JSON* file, which
are composed by a list of all the protocols in the workflow.
In the figure below, we have highlight with a blue box
the *Import movies* protocol part,
where it has listed inside all the internal parameters/fields for
the *Import movies*, such as its label, the files path where to
find the movies, the microscope's spherical aberration, the
dose per frame applied... (underlined in yellow)

In a common *JSON* file, all fields are made of *key:value* pairs where *key*
(what is before ':') is always a *string* and the *value* (what is after ':')
can be a *string* ("something coated"), *number*,
*boolean* (true or false), *list*, *dictionary*, *null*...
(`read more info about JSON files <https://www.json.org>`_).

.. figure:: /docs/images/custom-scipion-demo.png
   :align: center
   :width: 900
   :alt: custom scipion demo

Notice that environ variables are allowed in any template parameter
by means of the ``%(VAR)s`` casting.
For instance, in the ``filesPath`` parameter,
the ``%(HOME)s`` that will be replaced with the ``$HOME`` environ variable.

Additionally, we have created an easy syntax to add dynamic fields to that
*JSON* file, which will fed the wizard showed in the previous section.
Then, to add a dynamic field, you only must replace the value
(what is after the ':') of a certain parameter with a string starting and
ending by '~', enclosing four fields separated by '|'.
That's something like

::

    anyField: "~label|defaultValue|typeValue|cmdId~"

where *label* is the field's name displayed in the wizard form,
*defaultValue* is the default value inserted in that wizard field and
*typeValue* is a number which forces the type of the final value according to

* 0 for *strings*
* 1 for *booleans*
* 2 for *paths*
* 3 for *integers*
* 4 for *floats*.

Moreover, Scipion 3 incorporates a new feature in order to be able
to launch dynamic templates with a single command line
using the optional fourth field (*cmdId*).
See the `next section below <#launching-dynamic-templates-from-command-line>`_.

In the figure above, there are some examples such as *filesPath*,
*spherical aberration*, *amplitude contrast*, *sampling rate*...
(follow the arrows to see their behavior).
In this case all them belongs to the same protocol.
However there is no restriction in this way and, thus, you can add a dynamic
field to any parameter to any protocol.

Notice that the type for the *filesPath* field is set to 2 (meaning *path*),
then Scipion will check if this path exists before starting to process. Instead,
*gainFile* is set to 0 (*string*) to allow an empty value to skip
using a gain image if not needed. Finally, the 4 (*float* type) set to the
*dosePerFrame* allows to introduce non integer values.

When you are happy with the modified *JSON* file, you can save it wherever you
consider and, then you can launch it with

.. code-block:: bash

    scipion3 tamplate /path/to/myDynamicTpl.json.template

However, if dynamic templates are saved in such a way like

.. code-block:: bash

    $SCIPION_HOME/config/myDynamicTpl.json.template

(where ``$SCIPION_HOME`` is where you have installed Scipion), Scipion will
automatically discover them. The extension of this files have to be
**.json.template**. You can make as dynamic templates as you want
by storing them in the mentioned directory with certain different file name,
as long as they finishes with **.json.template**.

When more than one dynamic template are found in the
``$SCIPION_HOME/config`` directory, the command

.. code-block:: bash

    scipion template

opens an additional menu to choose the dynamic template to use.

.. figure:: /docs/images/multiple-choice-scipion-demo.png
   :align: center
   :width: 400
   :alt: multiple choice scipion demo

Launching dynamic templates from command line
=============================================

The optional forth field in the dynamic templates
(**cmdId** in the `example above <#creating-custom-dynamic-templates>`_)
is an identifier to assign a given value during
a launch through the command line.

For instance, the following command

::

    scipion3 template /path/to/myDynamicTpl.json.template sa=2 ac=0.1 dose=1.2

will load the ``/path/to/myDynamicTpl.json.template`` by parsing the
*spherical aberration* (sa), the *amplitude contrast* (ac) and
the *dose per frame* (dose) according to the passed values.

If all dynamic parameters are parsed in the command line,
then the workflow is automatically triggered. Instead, if some
parameters remains unset, a wizard similar to that described
in the previous section asks for them is launched.

Using Scipion's API
-------------------

A Scipion's project can be created, designed (adding protocols) and launched by
a Python script using the :ref:`Scipion's API <Scipion-API>`.

We have a repository destined to share Scipion's scripts potentially useful in
`EM-facilities <https://github.com/I2PC/em-facilities>`_.
Specially, we have an example of `creating a Scipion2 project using the API <https://github.com/I2PC/em-facilities/blob/master/usingAPI_demo/acquisition_workflow.py>`_.
See the `acquisition simulation (for Scipion2) <acquisition-simulation-scipion2>`_ section to learn how
to use this script.

Go to `API workflows <facilities-API-demo>`_ to see in detail how to make
projects with a Python script.