.. _general-style:

===========================
General Style
===========================

Branding Guidelines
====================

Logo
-----

Refer to the original link:Artwork[Artwork] page


Image&media
-----------

Icons
~~~~~

The icon set used in the project is `Font Awesome <http://fontawesome.io/>`_.
Font Awesome is fully open source and is GPL compatible. In
the web the icons are defined through a css class while in the desktop
app any new icon has to be generated from the `Font Awesome Cheatsheet <http://fontawesome.io/cheatsheet/>`_. In order to
generate these icons you will have to install the FontAwesome.otf and
copy&paste the icons in Photoshop. A brief explanation can be found in
the link aforementioned.

Typography
-----------

The default font type and family to be used is Helvetica. Font sizes and
decorations can be used to emphasize when required (using bold and/or
italics). The default size is 11 and the font style is plain. However if
needed it can be changed to emphasize, as well.

Color Palette
--------------

These are the main colors you should use in Scipion. Although you can
find some other colors in Scipion they are usually used with purpose
design. Therefore you should not use these or any other new colors
unless it was extremely necessary.

.. figure:: https://github.com/I2PC/scipion/wiki/images/colors.png
   :align: center
   :width: 699
   :height: 50
   :alt: colors

Firebrick (b22222): Red color for background label

F3CBCB: Very light red for row selection

EAEBFF: Very light blue for even rows

EAEBEC: Light grey for background color in form, protocol, table header
and west container

F2F2F2: Very light grey for odd rows, input background, etc

6E6E6E: Very dark grey for project title, tubes, etc

Messages
========

Error messages
--------------

The message must explain the error cause or description and give some
hints to solve the problem. In case a non expected or non controlled
error happens and none hint can be given, the message must give some
information contact and optionally a technical description instead. The
title of the window must provide a general description telling at least
the task that has caused the problem.

*Format 1:*

* Title: General Description
* First Paragraph: Error cause or description
* Second Paragraph: Hints to solve the error

*Format 2:*

* Title: General Description
* First Paragraph: Error cause
* Second Paragraph: Information contact
* Third Paragraph*: Technical Description

*Example 1:*

* Title: Open Project Failure
* First Paragraph: No project found
* Second Paragraph: Select a project to load.

*Example 2:*

* Title: Save Project Failure
* First Paragraph: Communication error with the database
* Second Paragraph: Try it later or contact your db administrator
  <email>


Warning messages
----------------

The warning message will be used to warn about an action that can be
performed although it is not recommended.

*Format 1:*

* Title: General Description
* First Paragraph: Warn cause and a explanation giving the reason why it
  is not recommended
* Second Paragraph: Hints about how to change this status

*Example 1:*

* Title: Delete Read Permission Warning
* First Paragraph: You are going to remove the read permission for
  <name>. <name> will not be able to access the project.
* Second Paragraph: If you want to change permissions, go to
  File>Properties.

Information messages
--------------------

The information message will be used to inform about an action.

*Format 1:*

* Title: General Description
* First Paragraph: Information for user.

*Example 1:*

* Title: Save Project Success
* First Paragraph: Project "Scipion Project" was successfully created.

Confirmation messages
---------------------

The confirmation message will be used to ask about an action to be
performed.

*Format 1:*

* Title: General Description
* First Paragraph: Information about an action.
* Second Paragraph: Question to perform o not to perform the action.

*Example 1:*

* Title: The project name already exists
* First Paragraph: There is another project named "Scipion Project".
* Second Paragraph: Do you want to create the project anyway?.

Messages
~~~~~~~~

Popup messages code is centralized in utils.js and are based on
javascript messi library. Depending on the kind of message you would
like to show you will have to call:

* Info and help messages -> infoPopup
* Warning message -> warningPopup
* Error message -> errorPopup

Further information describing input and output parameter and
functionality can be found in utils.js file.

Buttons
=======

Buttons classes can be found in the general_style.css: btn(general class
for all buttons), buttonGrey, buttonRed, etc. Most of the bottom will
use buttonGrey class however if you want to highlight one or some
buttons in a button menu you can use the buttonRed class.

Buttons are declared as a href with btn and button color class
associated. It can also contains an icon inside. Go to code for several
example.
