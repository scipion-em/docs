.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _introduction-scipion-web:

===========================
Introduction to Scipion web
===========================

.. contents:: Table of Contents

Introduction to Django Web Framework
====================================

Django is a free and open source web application framework, written in
Python, that follows the model–view–controller architectural pattern.
It is maintained by the Django Software Foundation (DSF).

The core Django MVC framework consists of an object-relational mapper
that mediates between data models (defined as Python classes) and a
relational database ("Model"); a system for processing requests with a
web template system ("View") and a regular-expression-based URL
dispatcher ("Controller").


Model-View-Controller into the Django
--------------------------------------

To understand the right works for the templates in Django, firstly, it
is necessary to explain the model-view-controller pattern applied to
Django.

.. figure:: /docs/images/wd/DjangoGeneral.png
   :align: center
   :width: 500
   :alt: DjangoGeneral.png

To render a template Django, follow these steps:

1.  When a user using a web browser tries to explore a page hosted inside
    Django, the request reaches the Django view.
2.  The view file interacts with the model to get the data necessary.
3.  The logic of the model obtains the data with its core mechanism
    developed. Normally the model gets the data from a database.
4.  When the view has all the data, it uses the specified template
    replacing the elements with the data obtained from the model.
5.  The template renders the response back to the web browser.


Django setup
~~~~~~~~~~~~

Django settings reside in web/pages/settings.py

URL mappings are defined in web/pages/urls.py

Web app structure
~~~~~~~~~~~~~~~~~

As usual, the best option is to look directly at the code (in
pyworkflow/web). Here we include a general overview:

* static content comes from the "static" directory. You need to run "python
  manage.py collectstatic" to actually populate the directory with the
  required files
* pages

  * resources

  * templates

  * urls.py

* app: actual application code (models, views...)
* manage.py: "a thin wrapper around django-admin.py that takes care of
  two things for you before delegating to django-admin.py" (puts your
  project’s package on sys.path and sets the DJANGO_SETTINGS_MODULE
  variable) . For a list of manage.py commands and more details, visit
  https://docs.djangoproject.com/en/1.6/ref/django-admin/

Additional Information
-----------------------

* `Django Official Documentation <http://docs.djangoproject.com/>`_: Current
  and detailed documentation on nearly every aspect of Django. It includes
  a version selector for information pertaining to specific versions of
  Django.
* `The Django Book <http://djangobook.com/>`_: Released under the GNU Free
  Documentation License.
* `Django Packages <https://www.djangopackages.com/>`_: A directory of reusable apps, sites, tools, and more for Django projects.
* `Django Basics <http://mherman.org/blog/2012/12/30/django-basics/>`_: Installing Django and Setting Up a Project and an App


Structure of templates HTML inside Scipion
==========================================

The templates are an important piece inside the Django framework
structure; here the MVC diagram is applied to the Scipion code.

MVC diagram applied to the scipion code
------------------------------------------

.. figure:: /docs/images/wd/diagramMVC.png
   :align: center
   :alt: diagramMVC

Templates diagram
-----------------

The template architecture is organized inside Scipion code as follows:

General templates
~~~~~~~~~~~~~~~~~

.. figure:: /docs/images/wd/diagram_templates.png
   :align: center
   :alt: diagram_templates

This templates can be found under 'web/pages/templates' folder.

* _base__grid.html__: template base with a static style.
* _base__flex__: template base with a flexible style.
* __header.html__: common header for base templates, contains the Scipion
  logo and different views
* __footer.html__: common footer for base templates with additional
  interest links.
* __projects.html__: this template extends from base_grid and shows a
  list of the available projects to work with.
* _project__content.html__: this template extends from base_flex and
  shows the content of a project with two run views (graph or list), also a
  tree with the protocols.
* __hosts.html__: this template extends from base_grid and shows the
  different hosts defined to be used to launch protocols and interact with
  them.
* _tree_prot__view.html__: a sub-template which contains the
  protocol tree with the different protocols to use in the project, the
  content can be customized and be chosen.
* _run_table__graph.html__: a sub-template which contains the run
  table list and the run graph with the protocol entries for a project,
  also contains a toolbar to interact with them.
* __form.html__: the protocol form with different options and structured
  dynamically.
* _header__form.html__: this template represents the header of the
  protocol form.
* _content__form.html__: this template is a dynamic form used to change
  different variables and options while a protocol is being edited prior to the
  run.
* _content_group__form.html__: it is similar to _content__form.html__
  but used to render groups.

Wizard templates
~~~~~~~~~~~~~~~~~

.. figure:: /docs/images/wd/diagram_templates_wiz.png
   :align: center
   :alt: diagram_templates_wiz

* _wiz__base.html__: template base with a static style used just for
  wizard templates. All the others wizard templates extend from this base
  template and redefine specific parts.
* _wiz__bandpass.html__: wizard template used to execute a Fourier
  filter for a list of particles.
* _wiz__ctf.html__: wizard template to preview the low and high
  frequencies for PSD image converted for a micrograph from a list.
* _wiz__downsampling.html__: wizard template to preview a
  downsampled image with a downsampling factor for a micrograph from a
  list.
* _wiz__gaussian.html__: wizard template used to execute a Gaussian
  filter for a list of particles.
* _wiz_filter__spider.html__: wizard template used to execute a Spider
  filter for a list of particles.
* _wiz_particle__mask.html__: wizard template to preview the radius
  of a particle for a list of 100 particles.
* _wiz_particle_mask__radii.html__: wizard template to preview an
  inner and outer radius of a particle for a list of 100 particles.
* _wiz_volume__mask.html__: wizard template to preview the radius of
  a volume for a list of 100 volumes.
* _wiz_volume_mask__radii.html__: wizard template to preview an
  inner and outer radius of a volume for a list of 100 volumes.

Showj templates
~~~~~~~~~~~~~~~

.. figure:: /docs/images/wd/diagram_templates_showj.png
   :align: center
   :alt: diagram_templates_showj


* _showj__base.html__: template base with a flex style used just for
  showj templates.
* _showj__column.html__: showj template to visualize single row metadata
  (particularly ctf metadata)
* _showj__gallery.html__: showj template to visualize metadata as a
  gallery of images
* _showj__table.html__: showj template to visualize metadata as plain
  text
* _showj_volume__astex.html__: showj template to visualize metadata
  volume with astex viewer applet
* _showj_volume__chimera.html__: showj template to visualize metadata
  volume with headless chimera. Chimera will generate a webGL html page
  that will be rendered. Headless chimera installation is required.

Creating a new template file
------------------------------

The location for the Scipion templates folder is
**pyworkflow/web/pages/templates/**, so new template files should be put there.

The names chosen for new templates (name and url) should have
underscores and should not be in `[CamelCase] <http://en.wikipedia.org/wiki/CamelCase>`_ format, like for
example: *new_template_to_be_added.html*

The new templates created must be added to the *pyworkflow/web/pages/urls.py* file, following the next example:

.. code-block:: bash

     urlpatterns = patterns(
        url(r'^new_url/$', 'location of the new template'),
        # The '$' symbol after the url means that url could set arguments
    )

Django templates use HTML language, but also have a new Django
language with interesting functionalities to use the potential of the
framework, allowing the access and interaction with the data model information. To take a look
at this new language, visit `[The Django template language] <https://docs.djangoproject.com/en/1.4/topics/templates/>`_.

Structure diagram of JavaScript libraries inside Scipion
========================================================

The architecture for javascript libraries organized inside the Scipion code
is next:

.. figure:: /docs/images/wd/diagram_libraries.png
   :align: center
   :alt: diagram_libraries


Template Libraries
-------------------

* _graph__utils.js__: Graph methods and variables to use with jsPlumb
  plugin, used with the template _run_table__graph.html__.
* _host__utils.js__: Methods to manage the template __hosts.html__.
* _project_content__utils.js__: Methods used in the
  _project__content.html__ template. Toolbar functions and manage tabs.
* _project__utils.js__: Methods used in the _project.html_ template.
* _protocol_form__utils.js__: Methods to manage the protocol form,
  template __form.html__.
* __utils.js__: Generic library with commons methods used in different
  templates.
* _wizard__utils.js__: Methods to manage wizards in the protocol forms.

Showj Libraries
------------------

* __colReorder.js__: Library to allow columns to be reordered in a
  DataTable.
* __colReorderWithResize.js__: Library to allow columns to be reordered
  in a DataTable with an automatic resize.
* __transpose.js__: Library to transpose (rotate) a table around the
  diagonal axis, turning columns into rows and vice versa.
* `waypoint.min.js <http://imakewebthings.com/jquery-waypoints/>`_:
  Waypoints is a jQuery plugin that makes easy to execute a function
  whenever you scroll to an element. Used to load dynamically the images
  in the showj.

jQuery Libraries
-------------------

* `jquery.js <http://jquery.com/>`_: jQuery is a fast, small, and
  feature-rich JavaScript library. It makes things like HTML document
  traversal and manipulation, event handling, animation, and Ajax much
  simpler with an easy-to-use API that works across a multitude of
  browsers.
* `jquery-ui.js <http://jqueryui.com/>`_: jQuery UI is a curated set of
  user interface interactions, effects, widgets, and themes built on top
  of the jQuery JavaScript Library.
* `jquery.dataTables.js <http://datatables.net/>`_: DataTables is a
  plug-in for the jQuery Javascript library. It is a highly flexible tool,
  based upon the foundations of progressive enhancement, which will add
  advanced interaction controls to any HTML table.
* `jquery.hoverIntent.minified.js <http://cherne.net/brian/resources/jquery.hoverIntent.html>`_:
  hoverIntent is a plug-in that attempts to determine the user's intent
  with mouse movement. It is similar to jQuery's hover method.
* `jquery.jeditable.js <http://plugins.jquery.com/jeditable/>`_: Edit in
  place (inline edit) plugin with possibility to create your own input
  types.
* `jquery.jlayout.js <http://www.bramstein.com/projects/jlayout/>`_: The
  jLayout JavaScript library provides layout algorithms for laying out
  components.
* __jlayout.border.js__: Auxiliary methods to use with the jLayout
  library.
* `jquery.sizes.js <http://www.bramstein.com/projects/jsizes/>`_: JSizes
  is a small plugin for the jQuery JavaScript library which adds
  convenient methods for querying and setting some size related CSS values.
* `jquery.treeview.js <http://bassistance.de/jquery-plugins/jquery-plugin-treeview/>`_:
  Lightweight and flexible transformation of an unordered list into an
  expandable and collapsable tree, great for unobtrusive navigation
  enhancements. Supports both location and cookie based persistence.
* `jquery.cookie.js <http://plugins.jquery.com/cookie/>`_: A simple,
  lightweight jQuery plugin for reading, writing and deleting cookies.

Tools Libraries
------------------

jsPlumb
~~~~~~~~

jsPlumb provides means for a developer to visually connect elements on
their web pages. It uses SVG in modern browsers, and VML on IE 8 and
below. Can be used with jQuery, MooTools or YUI3 (or another library of
your choice if you feel like implementing an adapter for it).

The template _run_table__graph.html__ provides a graph view for the
protocol runs using the potential of the jsPlumb.

More information about its uses can be found `[here] <https://jsplumbtoolkit.com/demos.html>`_


Messi.js
~~~~~~~~

Messi is a jQuery plugin to show clean, elegant messages in a simple
way. With Messi you will avoid to use default JavaScript alert
notifications or new windows to provide extended information to the
user. Display text, html content, images and ajax requests with 5 KB
code.

To get more information about how to use Messi.js, go `[here] <https://messijs.github.io/MessiJS>`_


Raphael JS
~~~~~~~~~~

Raphael is a small JavaScript library that should simplify your work
with vector graphics on the web. If you want to create your own specific
chart or image crop and rotate widget, for example, you can achieve it
simply and easily with this library. Raphael uses the SVG W3C
Recommendation and VML as a base for creating graphics. This means every
graphical object you create is also a DOM object, so you can attach
JavaScript event handlers or modify them later. Raphael’s goal is to
provide an adapter that will make drawing vector art compatible
cross-browser and easy. Raphael currently supports Firefox 3.0+, Safari
3.0+, Chrome 5.0+, Opera 9.5+ and Internet Explorer 6.0+.

It is used by the wizards in Scipion, getting the potential to paint
circles and images dynamically in a given canvas.

To get more information about how to use it, visit this `[link] <http://raphaeljs.com/>`_


Adding a new JavaScript library
-------------------------------

Sometimes, the use of new libraries is necessary and the organization and
location of these files is not controlled. To avoid this, you have
to follow this: We'll take the example of the jQuery library. If we
want add jQuery into the project, first, you have to
download the specific files. Inside the folder
*`pyworkflow/web/pages/resources/js/`* you have to create a subfolder
with your specific library name, for this case
*`pyworkflow/web/pages/resources/js/jquery/`* and put there the files to
use your library correctly.


Creating a new JavaScript file
------------------------------

Suppose that we want to create a new JavaScript file to interact with
some template. The first step is: to create a file (named, for example
**`file_script_utils.js`**) into the folder
**`pyworkflow/web/pages/resources/js/`**. The name of the file has to
be referred to in the template that needs it. This file should have the
following general structure:

\1. License (for example `[GNU] <http://gnu.org>`_) 1. General
description for the file functionalities. 1. List of attributes and
brief description. 1. List of the methods and brief description
(optional example usages). 1. Implementation of the attributes and
methods (`[CamelCase] <http://en.wikipedia.org/wiki/CamelCase>`_ used for
names)


Structure example for a new JavaScript file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    /*****************************************************************************
     * DESCRIPTION:
     * Methods used to do a lot of things.
     *
     * ATTRIBUTES LIST:
     * var attr1
     *    ->  Description of the attr1
     *
     * var attr2
     *    ->  Description of the attr2
     *
     * METHODS LIST:
     *
     * // *** Tag for agroup some methods *** //
     * function auxMethod1(elm1, elm2)
     * 	->	Function to do something with the parameters passed by arguments.
     *              Return a new element.
     *              Usage example: auxMethod1(elm1, elm2)
     *
    /** ATTRIBUTES ****************************************************************/

    var attr1="";
    var attr2="";

    /** METHODS ******************************************************************/

    function auxMethod1(elm1, elm2){
      /*
       * Comment similar than the first one to describe the function functionalities.
       * Function to do something with the parameters passed by arguments.
       * Return a new element.
       */
      var elm3 = elm1 + elm2
      // comment to describe what we do
      return elm3;
    }



Cascading Style Sheets (CSS)
==============================

The organization chosen by the CSS files has to be explained taking the template
pages as a reference.


.. figure:: /docs/images/wd/diagram_css.png
   :align: center
   :width: 600
   :alt: CSS diagram

* *_general__style.css*: Common styles used in all the templates.
* *_general_style_basegrid.css*: This file provides a static
  structure for the templates that include it.
* *_general_style_baseflex.css*: This file provides a flexible
  structure for the templates that include it.
* *jquery-ui.css*: Style file used by the jQuery UI library.
* *font-awesome.min.css*: Style file where is defined the 'awesome'
  theme for the fonts and icons.
* *messi.css*: File that define the popups showed by the messi.js
  library.
* *_projects__style.css*: CSS file associated with the _projects.html_
  template.
* *_project_contentstyle.css*: CSS file associated with the
  *_projectscontent.html* template.
* *form.css*: CSS file associated with the _form.html_ template.
* *_showj__style.css*: CSS file associated with the _showj.html_ template.
* *_jquery-uismoothness.css*: This style file defines the table
  appearance for tables and columns in the showj visualizer.
* *_wizardstyle.css*: This style file defines the appearance for the
  wizards that are based in the *_wizbase.html* template.

Creating a new CSS file
-------------------------

Suppose that we want to create a new CSS file to interact with some
template. The first step is: to create a file (named, for example
**`new_file_style.css`**) under the folder
**`pyworkflow/web/pages/resources/css/`**. The name of the file has to
be referred to in the template that needs it. This file should have the
following general structure:

.. code-block:: bash

    # Brief description for the file.

    # General CSS for common uses into the template.

    # CSS for specific structures inside the template, like for example: TOP, RIGHT, LEFT, BOTTOM,...

    # Specific CSS for parts into the template, like for example TABLE, LIST, TREE,...

    # CSS overwritten, if we need it.

