.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _creating-a-basic-plugin-from-template:

================================================
Creating a basic plugin from scipion-em-template
================================================

Associated resources
====================
Here you can find resources associated with this content, like videos or presentations used in courses:

* `Course presentation <https://docs.google.com/presentation/d/1sACaNZFgH0qWeXE6BLUWEDW3cjYTS4kbojrKvvRp78s/edit?usp=sharing>`_

* `Introduction to template plugin <introduction-to-template-plugin>`.

Cloning and installing scipion-em-template
==========================================

.. code-block::

    cd desired/location
    git clone -b course1_exBase https://github.com/scipion-em/scipion-em-template.git
    cd scipion3/location
    ./scipion3 installp -p scipion-em-template/location --devel

Check if the plugin works correctly
===================================
Follow these steps:

1. Open a new terminal and move to Scipion3’s directory:

.. code-block::

    cd scipion3/dir/

2. Execute Scipion3:

.. code-block::

    ./scipion3

3. Click on Create Project, type a name for it and then click on Create.

.. figure:: /docs/images/dev/template_practice/practice1_create_project.png
   :alt: create Scipion3 project

4. Look for your plugin protocol, and double click  on it. A window like this should appear:

.. figure:: /docs/images/dev/template_practice/practice1_hello_world_protocol_gui.png
   :alt: Hello world protocol gui

5. Click on the **wand** icon, choose **Hola Mundo** and click on **Select** button.

.. figure:: /docs/images/dev/template_practice/practice1_protocol_gui_walkthrough.png
   :alt: Hello world protocol walkthrough

6. Edit parameter **Time** value to **5** and click on **Execute** button.

.. figure:: /docs/images/dev/template_practice/practice1_protocol_gui_execution.png
   :alt: Hello world protocol execution

7. Once the execution is finished, your project should look like this (observe the information displayed below in the
   summary tab).

.. figure:: /docs/images/dev/template_practice/practice1_project_gui_summary.png
   :alt: project gui summary

8. Check also tabs Methods and Output Log. The last one, in subtab run.stdout shows the prints carried out by the
   protocol and detailed information about the protocol execution.

.. figure:: /docs/images/dev/template_practice/practice1_project_gui_log.png
   :alt: project gui log

9. Check pointer parameter functionality: right click on the protocol box and select **Copy**.

.. figure:: /docs/images/dev/template_practice/practice1_project_gui_copy_protocol.png
   :alt: project gui copy protocol

10. Update the values for parameter **Message** and **Times** to the ones shown and click on the **magnifier** icon.

.. figure:: /docs/images/dev/template_practice/practice1_protocol_gui_2nd_walkthrough.png
   :alt: protocol gui second walkthrough

11. **Select the item** that appears on the list and click on **Select**. Finally, click on **Execute** button on the
    protocol window.

.. figure:: /docs/images/dev/template_practice/practice1_pointer_select_object.png
   :alt: protocol gui pointer select object

12. Observe now in the summary area that the input value stored from the previous execution is shown, and that it has
    been used in the counter calculation.

.. figure:: /docs/images/dev/template_practice/practice1_project_gui_summary_II.png
   :alt: project gui summary second

*Conclusion*:

Protocol **MyPluginPrefixHelloWorld** receives 3 inputs:

* Message, which can be manually introduced or selected from a list of predefined options via a wizard.

* Times, to specify how many times the message will be printed.

* Previous count, optional parameter to be updated with a pointer which takes into account the number of times the
  message has been printed in a previous execution.

Convert template plugin into a calculator
=========================================

*Note*: if you get stuck in any of the exercises, the solution is provided via git branch in each of them. Due to the
exercises are consecutive, so you can move to the branch needed and continue. For example, if you got stuck in exercise
3 and want to continue, simply move to the branch which contains the solution of exercise 2 to get a check point from
where continue.

To begin the practice, launch PyCharm

Then, Click on File > Open and select your plugin. Follow these steps:

1. Move your plugin protocol on the protocols list to view **Practice1** list, section **PracticeDay1**, in protocol
   group **MyGroup**, under the name of **My first protocol** (*Hint*: file **protocols.conf**). Result should look like
   this:

.. figure:: /docs/images/dev/template_practice/practice1_ex1.png
   :alt: exercise 1

   Solution:

.. code-block::

    cd scipion-em-template/location
    git checkout -b course1_ex1

2. Edit the wizard (file wizards.py) to change the greetings into operations: **Sum, Substract, Multiply, Divide**.

   *Hint*: to make the wizard description be coherent with the new operational behaviour, update the wizard window
   title and wizard window message from **‘Greetings from the world’** to **‘My calculator operations’** and
   **‘Select one of the greetings’** to **‘Select one of the operations’**. This must be done in the dialog definition
   (line **dlg = dialog.ListDialog(form.root, "Greetings from the world", provider,  "Select one of the operations"**).

   *Important*: if variable name greetings is renamed, use the same name as the input in the provider definition,
   e. g., if greetings variable is renamed to myoperations (line **operations = [String(' …)**, then line **provider =
   ListTreeProviderString(greetings)** must be updated to **provider = ListTreeProviderString(myoperations)**.

   Result should look like this:

.. figure:: /docs/images/dev/template_practice/practice1_ex2.png
   :alt: exercise 2

   *Note*: Message field shows, when opening the protocol GUI, default value isn’t one of the four ones introduced in
   the wizard. This will be fixed in the next exercise.

   Solution:

.. code-block::

    cd scipion-em-template/location
    git checkout -b course1_ex2

3. In protocols.py, update field Message to **Operation**, and its default value to **Sum**. Update also the parameter
   name to **operation** and the help to **‘Operation which will be applied.’**.

   *Hint*: **form.addParam** method attributes are:
        *  Parameter name: name internally used in the code to refer to that parameter as a **protocol attribute**.
        *  Data type.
        *  Attributes whit syntax attributeName=attributeValue, e. g. label=’Message’.

   *Important*: the wizard’s target was the old field name must be updated to the new one. To do that, in file
   wizards.py, update line **_targets = [(MyPluginPrefixHelloWorld, ['message'])]** to **_targets =
   [(MyPluginPrefixHelloWorld, ['operation'])]**. Also, the wizard output must point to the new parameter, so update line
   **form.setVar('message', dlg.values[0].get())** to **form.setVar(‘operation’, dlg.values[0].get())**.

   Result should look like:

.. figure:: /docs/images/dev/template_practice/practice1_ex3.png
   :alt: exercise 3

   Solution:

.. code-block::

    cd scipion-em-template/location
    git checkout -b course1_ex3

4. Now, update **Times** parameter to **Operand 1**, with a default value of **1**, parameter name to **operand1** and
   its help to **‘First operand considered in the selected operation.’**.

   *Hint*: because result of division operation may be decimal, data type must be **objects.Float**.

   Again, result should look like:

.. figure:: /docs/images/dev/template_practice/practice1_ex4.png
   :alt: exercise 4

   Solution:

.. code-block::

    cd scipion-em-template/location
    git checkout -b course1_ex4

5. Do the same with parameter **Previous count**: its new label will be **Operand 2**, with a default value of **1**,
   parameter name **operand2** and its help **‘Second operand considered in the selected operation.’**.

   *Hint 1*: the new behaviour of this parameter doesn’t require to allow pointers nor null values.

   *Hint 2*: to make a parameter be bold on the protocol GUI, set the parameter attribute named important to true
   (important=True).

   *Hint 3*: read the hint of point 4. It also applies to operand2.

   Result should look like this:

.. figure:: /docs/images/dev/template_practice/practice1_ex5.png
   :alt: exercise 5

   *Note*: Observe that the magnifier icon is no longer present because this parameter isn’t longer allowing pointers.

   Solution:

.. code-block::

    cd scipion-em-template/location
    git checkout -b course1_ex5

6. In protocols.py, type the operating method and customize the info functions.

   To do that, follow these steps:

        6.1  Insert **‘Calculate’** step, which will be called when protocol’s Execute button is pressed: replace the
             line used to insert the previous greetingsStep,  **self._insertFunctionStep('greetingsStep')**, by
             **self._insertFunctionStep(‘calculateStep’)**.

        6.2  Replace the method **greetingsStep** by a new one called **calculateStep**.

             *Hint*: get operands and operation values from the GUI with **self.[PARAM_NAME].get()** and then write the
             operation cases with **if** command. Result of the operation must be stored in a protocol attribute, e. g.,
             **self.result**, which must be of type float.

        6.3  Update output step, so the result is registered and thus available to be used, for example, in the info
             methods.

             *Hint*: use protocol inherited method **self._defineOutputs** to do that.

             *Important*: to make a **variable value be registered, it must be casted to a Scipion data type**. In this
             case, **self.result** should be casted to type **params.Float**.

        6.4  Finally, in terms of customizing the info functions by adapting them to the new functionality, we’ll focus
             only in **_summary** method. Thus, you can comment or delete the method **_methods**. Then, update the
             summary message which will be displayed so it shows the operation selected, both operands and the result.

   Result should look like:

.. figure:: /docs/images/dev/template_practice/practice1_ex6.png
   :alt: exercise 6

   Solution:

.. code-block::

    cd scipion-em-template/location
    git checkout -b course1_ex6
