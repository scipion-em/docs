.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _how-to-git:

============================================
How to migrate code from Scipion to a plugin
============================================

First of all, a new temporal repo must be cloned and this new repo will become
the plugin repo at the end. Therefore, we will name it according with the plugin
to be created

::

    cd
    git clone https://github.com/I2PC/scipion.git myPlugin
    cd myPlugin

Remove the remote tracking

::

    git remote rm origin

Checkout the branch where you code is. If you have not started to code, use `devel`

::

    git checkout devel

Let's suppose that you want to migrate the whole folder `pyworkflow/myFolder`.
Then, we delete all the rest files and their history, but keeping the `myFolder`
history (edit the following command according with your folder path and branch)

::

    git filter-branch --subdirectory-filter pyworkflow/myFolder -- devel

In this way, only the files into that folder (`myFolder` in this case) are kept
under the root repository path. Therefore, all that files should be moved to
the final destination. For the case of creating a Scipion plugin, this files
should end inside the plugin module (see the
`plugin structure <creating-a-plugin#file-tree>`_). Let's assume that `myFolder`
contains the protocols of the plugin, then we will place it at protocol's module

::

    mkdir -p myPlugin/protocols
    git mv -k * myPlugin/protocols

Additionally, you probably want to add some other files in order to
`create the plugin <creating-a-plugin#file-tree>`_. This can be done here or
after the first commit/push. Just, keep in mind to add all the new files to
the commit by (as usual)

::

    git add myFile1 myFile2 myFile3 ...

Finally, commit and push the new repository to where the repository will be
tracked

::

    git commit -am "First commit: taking protocols from Scipion's repo"
    git remote add origin pluginRepoUrl
    git push origin