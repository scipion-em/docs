.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _creating-a-new-webtool:

==========================
Creating a new webtool
==========================

Steps to create a new web tool:

. Add an entry point in the services page:
Go to webservice_projects.html and add an entry point for the new webtool.

* Create the webtool home page: We need to create the webtool home page.
* Create a python package for the webtool inside under pyworkflow/web/webtools/
* now, in the webtool package folder:
* in the  __init__.py add "from urls import urls"
* create urls.py based on other webtools an customize appropriately.
* create views.py based on other webtools an customize appropriately.
* For this you might need to create the test data: add your test data in the Test/__init__.py file and use it in the create project method.
* create the .js utils file based on other webtools an customize appropriately under <webtool_package>/resources/js/
* create the set of .html file based on other webtools an customize appropriately under <webtool_package>/templates
* add an import of your new views file (views.py) in the views_webtools.py
* Each webtool runs with its own config files for protocols.conf and hosts.conf. Although the protocol.conf will be created if it doesn't exists, the host.conf needs to be there. So copy a host.conf from other webtool and place it under ~/.config/scipion/[new web tool]/
