.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _plugin-manager:

==============
Plugin manager
==============

This page aims to introduce you to the usage of Scipion Plugin Manager,
which is a friendly application to manage everything related to the
installation of the Scipion plugins.

Where is it?
============

After launching Scipion from the command line ( ``./scipion`` ) we will
see the project manager window. Here we click on the Configuration menu
to select the Plugins option (Figure 1).

.. figure:: /docs/images/guis/scipion_config_menu.png
   :alt: Scipion projects manager

   Scipion projects manager

Figure 1. Scipion project manager

Plugin manager window
=====================

Now you will see the Plugin Manager interface (Figure 2).

.. figure:: /docs/images/guis/plugin_manager.png
   :alt: Plugin manager GUI

   Plugin manager GUI

Figure 2. Plugin manager

On the left we can see the list of all available plugins. The top right
panel displays information for the selected plugin loaded from Pypi,
such as name, version, release date, plugin description, url and the
authors.

Installing plugins
==================

At the beginning, all plugins are uninstalled and appear with the
**UNINSTALLED** icon ( |unchecked_icon| ). If you want to install any
plugin, you need to do the following two steps.

Step 1: Check the selected plugin
---------------------------------

We have two options:

-  Click on the UNINSTALLED icon |unchecked_icon|.
-  Right-click on the plugin name and select the **INSTALL** option |plugin_right_click|


In both cases, the icon of the selected plugin will change to **TO INSTALL**
(|install_icon|) and the operation is shown in the bottom right panel
on the **Operations** tab. We can select more than one plugin to install
(Figure 3)

.. figure:: /docs/images/guis/plugin_to_install.png
   :alt: plugin to install
   :name: figure-3-installing-plugins

   Figure 3. Installing plugins

Step 2: Execute all selected operations
---------------------------------------

Once all the operations have been selected, we will proceed to execute
them. For this, on the bottom right panel we have a tool bar with the
action |execute_all_operations|. This action **executes automatically
all operations** that we have selected. When you click on the icon, the
Plugin manager is locked until all operations have been executed. Once
all the operations have been executed, the status of the selected
plugins changes as shown in the Figure 4. The selected plugins will
appear as installed |installed_plugin|.

If there is an error in the installation process, the operation will
appear as not executed |error_icon, width=1|, otherwise it will appear
as executed |executed_operation|.

Before execute all operations, we can **cancel any operation** by
selecting it and clicking on the action |cancel_operations| or with a
right-click on the plugin name and selecting **Undo**
|undo_operations|. In the same way, we can change the number of
processors with which we want all the selected operations to be
executed. By default it is 4 processors.

.. figure:: /docs/images/guis/execute_operation.png

   Figure 4. Installed plugin

Until the Plugin manager executes everything, we can check the logs on
the **Output log** tab from the bottom right panel. The operations logs
will show up in the **Plugin.log** tab as the Figure 5 shows. If there
are errors, **Plugin.error** will show a detailed list of these.

.. figure:: /docs/images/guis/plugin_manager_logs.png

   Figure 5. Plugin manager logs

When a plugin is installed, the list of binaries is added to the plugin
on the tree in the left panel. If we want to show the list of binaries
we need to expand the plugin as shown in Figure 6. It is important to
mention that only the binaries that were defined by default in the
plugin will be installed. If we need to **install** other non-default
**binaries** of any plugin, we just need to do the same procedure we did
to install a plugin.

.. figure:: /docs/images/guis/binaries_list.png

    Figure 6. Scipion-em-grigoriefflab binaries

Uninstalling plugins
====================

In the same way that we install a set of plugins, we can uninstall them.
For this, we need to select an installed plugin and follow these steps.

Step 1: Uncheck the selected plugin
-----------------------------------

Again, we have two options:

-  Click on the INSTALLED icon |uninstalled_plugin|.
-  Right-click on the plugin name and select the **UNINSTALL** option

|uninstall_plugin_right_click|

In both cases, the selected plugin icon will change to **TO UNINSTALL**
icon (|uninstall_icon|) and the operation is shown in the bottom right
panel on the **Operations** tab. We can select more than one plugin to
uninstall (Figure 7)

|uninstall_plugins| Figure 7. Uninstalling plugins

Step 2: Execute all selected operations.
----------------------------------------

Same as Step 2 to `Install
Plugins <#step-2-execute-all-selected-operations>`__

Updating plugins
================

The Plugin Manager can detect when there are plugin updates available.
In this case, the name of the plugin is highlighted in bold and, in the
top right panel there will be information about the new version and how
to update the plugin (see Figure 8).

.. figure:: /docs/images/guis/updating_plugins.png
   :alt: uninstall_plugin

   Figure 8. Updating plugins

To update any plugin, we need to select an installed plugin, right-click
on the plugin name and select the **UPDATE** option:
|update_plugin_option|

In this case, the selected plugin icon will change to **TO UPDATE** icon
|update_icon| and the operation is shown in the bottom right panel on
the **Operations** tab (Figure 9)

.. figure:: /docs/images/guis/update_operation.png
   :alt: update plugin operation

   Figure 9. Uninstalling plugins

To execute the selected operation we just need to press the **execute
operation** icon |execute_all_operations| like **Install** or
**Uninstall** any plugin or binary

Plugin Manager Glossary
=======================

The Plugin Manager has a glossary of terms in the Help menu in the
toolbar. This interface shows the icons that are used and their meaning
as shown in the following figure.

.. figure:: /docs/images/guis/plugin_manager_help.png
   :alt: update plugin operation

   Figure 10. Glossary

.. |unchecked_icon| image:: /docs/images/guis/unchecked_icon.png
.. |plugin_right_click| image:: /docs/images/guis/plugin_manager_right_click.png
.. |install_icon| image:: /docs/images/guis/install_icon.png
.. |execute_all_operations| image:: /docs/images/guis/to_install_icon.png
.. |installed_plugin| image:: /docs/images/guis/checked_icon.png
.. |error_icon, width=1| image:: /docs/images/guis/error_icon.png
.. |executed_operation| image:: /docs/images/guis/installed.png
.. |cancel_operations| image:: /docs/images/guis/delete_operation_icon.png
.. |undo_operations| image:: /docs/images/guis/undo_icon.png
.. |uninstalled_plugin| image:: /docs/images/guis/checked_icon.png
.. |uninstall_plugin_right_click| image:: /docs/images/guis/uninstall_plugin.png
.. |uninstall_icon| image:: /docs/images/guis/uninstall_icon.png
.. |uninstall_plugins| image:: /docs/images/guis/uninstall_plugins_interface.png
.. |update_plugin_option| image:: /docs/images/guis/update_plugin_option.png
.. |update_icon| image:: /docs/images/guis/update_icon.png
