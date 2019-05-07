.. _scipion commands:

======================
Scipion commands
======================

.. contents:: Table of Contents

Configuration commands
========================

Cleaning projects
--------------------

In Scipion and Scipion Web, many projects can be created. Each project has a lifetime, and after that lifetime the project is suitable for deletion.

List outdated projects
~~~~~~~~~~~~~~~~~~~~~~~~~~
To get the list of outdated projects you can run:

.. code-block:: bash

    scipion run python scripts/clean_projects.py [USER DATA FOLDER]


[USER DATA FOLDER] : by default will be 'os.environ['SCIPION_USER_DATA']' ; otherwise, it must be a folder with some user data.

This will only the projects that are out of date.


Delete outdated projects
~~~~~~~~~~~~~~~~~~~~~~~~
To delete outdated projects, you can run:

.. code-block:: bash

    scipion run python scripts/clean_projects.py [USER DATA FOLDER] --delete

All outdated projects will be deleted.

NOTE: Deleting a project is basically deleting a project folder.


Dealing with projects settings
-------------------------------

You can list some project attributes with:

.. code-block:: bash

    scipion --config [SCIPION CONFIG FILE] run python scripts/config_project.py [PROJECT NAME]

Setting lifeTime
~~~~~~~~~~~~~~~~~

You can also make a project eternal:

.. code-block:: bash

    scipion --config [SCIPION CONFIG FILE] run python scripts/config_project.py [PROJECT NAME] lifeTime=None

Setting readOnly
~~~~~~~~~~~~~~~~~~~~

You can also make a project read-only:

.. code-block:: bash

    scipion --config [SCIPION CONFIG FILE] run python scripts/config_project.py [PROJECT NAME] readOnly=True

Both
~~~~~

Both at the same time:

.. code-block:: bash

    scipion --config [SCIPION CONFIG FILE] run python scripts/config_project.py [PROJECT NAME] readOnly=True  lifeTime=None







