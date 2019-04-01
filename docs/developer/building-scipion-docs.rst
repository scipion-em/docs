
.. _buildging-scipion-docs:

=====================
Building Scipion docs
=====================

Scipion's documentation is built using `Sphinx <http://www.sphinx-doc.org>`_ and hosted on
`GitHub pages <https://pages.github.com/>`_. Sphinx uses certain files like ``*.rst`` files and Sphinx's config
``conf.py`` to build the docs on HTML, which we can later copy to some server. In our case, we the different versions
of our docs on the `docs GitHub repository <https://github.com/scipion-em/docs>`_ . At the time of this writing we have
only one version, the branch ``release-2.0.0``, but we'll have more versions in the future.
The branch ``gh-pages`` contains the **built**
documentation for all versions (i.e. HTML files). When new commits are pushed to this branch,
https://scipion-em.github.io/docs/ will update and reflect them automatically.

On a high level, the docs have two main parts:

* The API docs, which are automatically generated from the code's docstrings using `sphinx-apidoc <https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html>`_.
  To build these, we need a working :doc:`installation of Scipion </docs/scipion-modes/install-from-sources>` in our machine.
* The general docs, which are manually generated content (e.g. guides, tutorials, etc).

Set-up
======

Sphinx virtualenv
-----------------

1. Clone the `Scipion docs repository <https://github.com/scipion-em/docs>`_. We'll clone to a folder
   called scipion-docs.

.. code-block:: bash

    $ git clone git@github.com:scipion-em/docs.git scipion-docs

3. Create a virtual environment in the directory of your choice (better not inside the repo dir) and activate it.

.. code-block:: bash

    $ virtualenv sphinx-env
    $ source sphinx-env/bin/activate
    (sphinx-env) $

4. Go to the repo dir (with your virtual environment activated) and install the pip requirements. Please note that
   ``sphinxcontrib-versioning`` is installed from a git fork, not from pypi - the current version available in pypi does NOT work.

.. code-block:: bash

    (sphinx-env) $ cd scipion-docs
    (sphinx-env) $ pip install -r requirements.txt

NOTE: we could skip the environment creation and install the requirements in Scipion's python.
However the installation of requirements will mess with some of the versions currently
available in Scipion's site-packages, so we recommend not messing with this and installing sphinx packages in a
separate virtualenv.

Generate API docs
-----------------

The api docs are contained in the folder ``api`` of the scipion docs repository. To update them, we need to run
``sphinx-apidoc``. Please note that this step is not necessary if you're just adding your own written ``.rst`` file.

We can set this up as a run configuration in PyCharm (Recommended):

.. image:: /docs/images/dev-tools/pycharm_apidoc_runconfig.png
   :alt: Scipion project manager


Or alternatively, run this in the command line inside ``scipion-docs`` repo dir:

.. code-block:: bash

    sphinx-apidoc -f -e -o api/ ~/git/scipion/pyworkflow ~/git/scipion/pyworkflow/tests/*

* ``-f`` forces to overwrite existing files
* ``-e`` generates one rst file per module
* ``api/`` put output files here
* ``~/git/scipion/pyworkflow`` is the source python code we want to generate docs for
* ``~/git/scipion/pyworkflow/tests/*`` avoid generating docs for files matching this pattern.


Make html
---------

This step is only used for testing purposes. Can be perfectly skipped. It is recommended to do it if you need to test some
local changes that you don't wish to commit just yet (which is good to avoid pushing tiny commits).
To test if we can generate the html files, run this inside ``scipion-docs``.
At the time of this writing, there are multiple errors and warnings. Sphinx will just generate whatever it can.
It is a good idea to work on reducing these errors and warnings :)

::

    (sphinx-env) $ scipion run make html

After this, we can open ``_build/html/index.html`` on a browser and see the built docs. At this point we won't have the
version support on the bottom left corner.


Build with sphinx-versioning
----------------------------

For this step all changes must be pushed to the remote repository, since sphinx-versioning doesn't take into account
local changes. The command used for this:

.. code-block:: bash

    (sphinx-env) $ scipion run /home/yaiza/sphinx-env/bin/sphinx-versioning build -r release-2.0.0 /home/yaiza/git/scipion-docs /home/yaiza/git/scipion_gh_pages

After executing this we should be able see the docs with version support by opening
``/home/yaiza/git/scipion_gh_pages/index.html`` with our browser.

We can also trigger this command with the following run configuration in PyCharm:

* **Script path**: ``/home/yaiza/git/scipion/scipion``
* **Parameters**: ``run /home/yaiza/sphinx-env/bin/sphinx-versioning build -r release-2.0.0 /home/yaiza/git/scipion-docs /home/yaiza/git/scipion_gh_pages``
* **Python interpreter**: The one from our ``sphinx-env``
* **Working directory**: Our ``scipion-docs`` repo dir


.. image:: /docs/images/dev-tools/pycharm_sphinxversion_build.png
   :alt: PyCharm run config for sphinx-version build

Push with sphinx-versioning
---------------------------
Once we are happy with the build, we can push our docs. For this we must run this command within our scipion-docs dir:

.. code-block:: bash

    (sphinx-env) $ scipion run /home/yaiza/sphinx-env/bin/sphinx-versioning push -r release-2.0.0 /home/yaiza/git/scipion-docs gh-pages .

The PyCharm run configuration is the same as before except for the parameters:

* **Parameters** : ``run /home/yaiza/sphinx-env/bin/sphinx-versioning push -r release-2.0.0
                     /home/yaiza/git/scipion-docs gh-pages .``

.. image:: /docs/images/dev-tools/pycharm_sphinxversion_push.png
   :alt: PyCharm run config for sphinx-version push

For more info on the params of sphinx-versioning you can run `sphinx-versioning --help` or check `sphinx-versioning docs
<https://robpol86.github.io/sphinxcontrib-versioning/v2.2.1/tutorial.html>`_.