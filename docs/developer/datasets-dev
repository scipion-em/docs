.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _datasets-dev:

=========
DataSets
=========

In order to `create and run Scipion tests <writing-tests>`_ , we provide a set
of DataSets that can be used for such purposes. They are hosted on the
institution's servers and when invoked from Scipion, they are downloaded
locally to be used by the tests. Each one is contained by volumes, stack of
particles, micrographs, movies, etc ...

The dataset list can be displayed with the following command:

::

    ./scipion3 testdata --list


The datasets can be downloaded using the following command:


::

    ./scipion3 testdata --download <dataset_name>

Then, the data found within the datasets folders could be used to perform the tests.

The downloaded dataset folder by default is locate in:

.. code-block:: bash

    $ ~/<scipion_folder>/data/tests/

but we can download in another place changing in the Scipion config file the
`SCIPION_TESTS` variable.

The rest of the options, we can be displayed using the `-h` parameter.

::

    ./scipion3 testdata -h


Another way to use the datasets that are provided by Scipion, is to let the tests
themselves take responsibility for downloading them and then select the data
that will be used by the test. In that sence, Scipion provide a class named
**DataSet** which is responsible for download and handle the datasets.

-----------------------------------
Add your own DataSet (if necessary)
-----------------------------------

If you need an additional dataset you can do this and host it where ever you want/can.
Let's assume you need a new dataset...

* usually you work first locally until you are happy with your data set.
* Decide where to host it and upload it. For that scipion3 will:
* Generate a ``MANIFEST`` file
* rsync it to your server, you will need to provide a login info (like user@server.com, and a remote folder location.
* type something like:

.. code-block:: bash

    scipion3 testdata --upload myplugin123_testdata -l user@server.com -rf /path/at/the/server/for/your/datasets


Please note that the dataset name must be unique, so better prefix it with the plugin name. ``-l`` is the login for your
server and ``-rf`` is the remote folder where to rsync your files.

* Refer to it in your tests, at you tests ``folder/__init__.py``:

.. code-block:: python

  DataSet(name='myplugin123_testdata',
          folder='myplugin123_testdata',
          files={
                 'file1': 'file1.txt'
                 ...},
          url='http://wwww.server.com/datasets')

NOTE: url parameter should be a valid url where your dataset is being published.
TIP: I haven't tried, but doing the upload yourself, to generate the MANIFEST and then adding your datasets + MANIFEST
to github might also work if you later point to the gitraw url?? (disclaimer...has not been tested.)




