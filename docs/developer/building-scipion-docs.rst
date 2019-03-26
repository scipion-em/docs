
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

0. :doc:`Install Scipion </docs/scipion-modes/install-from-sources>`

1. Clone the `Scipion docs repository <https://github.com/scipion-em/docs>`_. We'll clone to a folder
   called scipion-docs.

.. code-block:: bash

    $ git clone git@github.com:scipion-em/docs.git scipion-docs

2. Create a virtual environment in the directory of your choice (better not inside the repo dir) and activate it.

.. code-block:: bash

    $ virtualenv sphinx-env
    $ source sphinx-env/bin/activate
    (sphinx-env) $

3. Go to the repo dir (with your virtual environment activated) and install the pip requirements.

.. code-block:: bash

    (sphinx-env) $ cd scipion-docs
    (sphinx-env) $ pip install -r requirements.txt

Scipion's environment variables
-------------------------------

4. Set environment variables to emulate Scipion's environment. We have to do this because in order to build the api
   docs, Sphinx actually imports the modules. Without these variables, many modules will fail to import. We need:
   ``SCIPION_HOME``, ``LD_LIBRARY_PATH``, ``SCIPION_SHORT_VERSION``. To export these variables, we can use the following
   command:

.. code-block:: bash

    (sphinx-env) $ $(scipion printenv | grep SCIPION_HOME)
    (sphinx-env) $ $(scipion printenv | grep LD_LIBRARY_PATH)
    (sphinx-env) $ $(scipion printenv | grep SCIPION_SHORT_VERSION)

