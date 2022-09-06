.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _creating-streaming-protocol:

=============================
Creating a Streaming Protocol
=============================

Associated resources
====================
Here you can find resources associated with this content, like videos or presentations used in courses:

`Course presentation <https://docs.google.com/presentation/d/1S7o-9dq6BjGUN7K_w5GjsOO0W5vmCV-q2U2xgDRBiAM/present?usp=sharing>`_

Practice
========

Let's go to our template plugin folder (if you dot have it, visit `template plugin <https://github.com/scipion-em/scipion-em-template>`_ and clone and install it) folder and setup everything ready for the practice session:

.. code-block:: bash

   cd scipion-em-template
   git checkout master

We define a ``streaming protocol``  as a processing task that involves
execution of several steps like any other `Scipion protocol <../creating-a-protocol>`_,
but which input might change during the protocol execution. It is thus impossible to
plan all the steps ahead (difference between streaming and non streaming protocols).
The list of steps in a streaming protocol is dynamic, that is, they are added
as the input grows. These steps can even be parallelized. You can read more
about defining steps to be executed in parallel in `Parallelization <../parallelization>`_.

Here we will create a simple streaming protocol that connects to
`EMPIAR <https://www.ebi.ac.uk/pdbe/emdb/empiar/>`__ (Electron Microscopy
Public Image Archive), downloads a set of movies and registers them as outputs in parallel.

.. warning::
    This protocol is artificially streamified and will have problems with concurrency
    or in case of resuming after a failure. But for the sake of simplicity we are
    ignoring these problems.

The general idea of this protocol is as follows:

.. figure:: /docs/images/general/streaming_idea.png
   :width: 750
   :alt: Streaming Idea

In that sense, we need to implement the following steps:

1. Create a protocol GUI that takes as a parameter the ID of the EMPIAR dataset
   as well as a stopping criterion (in our case the number of movies to download).

   1.1. Create a protocol and specify that the steps are to be executed in parallel.

   1.2. Define the "parallel" section.

2. Create the steps to download and register the movies.

   2.1. Read the xml file corresponding to a specific EMPIAR dataset which contains important metadata (sampling rate, dimensions, ...).

   2.2. Download the movies until the stopping criteria is met (number of downloaded movies).

   2.3. Register the downloaded movies. This step is in streaming. We need to constantly check if new movies have been downloaded.


Defining the protocol class and the GUI
---------------------------------------

The GUI would be as the following figure shows:

.. figure:: /docs/images/general/streaming_protocol.png
   :width: 550
   :alt: Streaming Protocol

The following code contain the class definition and the protocol GUI implementation.

.. note:: 

         Remember import the protocolo inthe __init__.py file of the protocol folder of the plugin

.. code-block:: python

    import json
    import requests
    import ftplib
    import os
    import shutil

    from pwem.objects import Movie, SetOfMovies, Float, String, Set
    from pwem.protocols import EMProtocol
    from pyworkflow.protocol import params, Positive, STATUS_NEW, STEPS_PARALLEL
    import pyworkflow.utils as pwutils

    class EmpiarDownloader(EMProtocol):
        """
        Download a movie set from EMPIAR
        """
        _label = 'empiar downloader'
        _outputClassName = 'SetOfMovies' # Defining the output class
        registeredFiles = []             # saves the name of the movies that have been already registered
        _stepsCheckSecs = 3              # time in seconds to check the steps

        def __init__(self, **args):
            EMProtocol.__init__(self, **args)
            self.stepsExecutionMode = STEPS_PARALLEL # Defining that the protocol contain parallel steps

        def _defineParams(self, form):
            # 1) add a section

            # 2) add a parameter to capture the EMPIAR entry ID:
            # name --> entryId, StringParam, default value 10200, you choose the label
            # Ideally we want it in bold so it is "Important". Fill in the help.

            # 3) add another parameter to set a limit of downloaded files:
            # name-->amountOfImages, IntParam(, default to 1, choose the label and the help
            # It has to be positive (use "validators" argument, it expects a list of
            # pyworkflow.protocol.params.Validator, look for the Positive Validator)

            # 3) Add the parallel section defining the default number of threads and mpi to use
            form.addParallelSection(threads=3, mpi=1)

.. note::

        Note that in the ``__init__`` method, we are specifying
        **stepsExecutionMode** parameter, and in the ``_defineParams`` we are invoking
        **addParallelSection** method. This tells Scipion that the steps can be
        run in parallel (via threads or MPI)

At this point you should be able to find the protocol using **Ctrl+F**, open it and see the input parameters.

Create the steps to download and register the movie set
--------------------------------------------------------

First, we will implement the ``_insertAllSteps`` method to define the different steps.
The first step reads the dataset xml file from EMPIAR.

.. code-block:: python

        def _insertAllSteps(self):
            # insert a functionStep (readXmlFileStep) to read the xml file from EMPIAR entry

        def readXmlFileStep(self):
            # Call the method provided below to get some data from the empiar xml

            # Store returned values as "persistent" attributes: String, Integer, Float

            # Use _store method to write them

        def _summary(self):
            summary = []
            # Check if we have the any summary attribute (if readXmlStep has happened) (HINT: hasattr will do)
            # Add items to the summary list like:
            # "Title: %s" % getattr(self, 'title')
            # "Sampling rate: %s" % ??
            # How would you have more values in the summary? (HINT: return more values in readXmlFromEmpiar)

            return summary


We provide you the code that reads EMPIAR's xml:

.. code-block:: python

    def readXmlFromEmpiar(entryId):
            """
            Read the xml file of a specific dataset from EMPIAR repository
            """
            empiarXmlUrl = 'https://www.ebi.ac.uk/pdbe/emdb/empiar/api/entry/' + entryId  # URL of EMPIAR API

            xmlFile = requests.get(empiarXmlUrl, allow_redirects=True)               # getting the xml file
            content = (json.loads(xmlFile.content.decode('utf-8')))                  # extract the xml content
            empiarName = 'EMPIAR-' + entryId                                         # dataset name

            correspondingAuthor = content[empiarName]['corresponding_author']        # dataset authors
            organization = String(correspondingAuthor['author']['organization'])     # authors organization
            depositionDate = String(content[empiarName]['deposition_date'])          # dataset deposition date
            title = String(content[empiarName]['title'])                             # dataset title
            imageSets = content[empiarName]['imagesets']                             # dataset images information
            releaseDate = String(content[empiarName]['release_date'])                # dataset release date
            datasetSize = String(content[empiarName]['dataset_size'])                # dataset size
            empiarName = String(empiarName)
            samplingRate = Float(imageSets[0]['pixel_width'])                   # images sampling rate
            dataFormat = String(imageSets[0]['data_format'])                    # images format

            # You may want to return more elements
            return title, samplingRate


.. tip::

    All the values that we want to have in the summary (title, samplingRate, ...)
    have to be Scipion objects (String, Integer, ...) that automatically get persisted.
    
Now your protocol should be able to run. Try it now and get some information from the empiar entry **10200.**
Check that the summary looks good.

After the execution, the **Summary** panel could show the following information if you managed to store all values:

.. figure:: /docs/images/general/summary.png
   :width: 450
   :alt: Summary


After that, we'll add into ``_insertAllSteps`` method the second step. This step
will download the movies from the entry (``entryId``) ftp until the maximum number
specified (``amountOfImages``) is reached.

.. code-block:: python

        def _insertAllSteps(self):
            self._insertFunctionStep('readXmlFileStep')     # read the dataset xml file from EMPIAR
            self._insertFunctionStep('downloadImagesStep')  # download the movies and register them in parallel

        def downloadImagesStep(self):
            # Call the method provided below.
            # Make the download happen into the tmp folder (self._getTmpPath) of the protocol,
            # and the final folder has to be the extra folder (self._getExtraPath).
            pass

The code below should download the files from empiar:

.. code-block:: python

    def downloadImagesFromEmpiar(entryId, downloadFolder, finalFolder, limit=5):
        """
        This method connects to EMPIAR's ftp and downloads a set of images
        into a specific directory. Once image is downloaded it is moved to the final folder
        """
        # Connection information
        server = 'ftp.ebi.ac.uk'
        username = 'anonymous'
        password = ''

        # Directory information
        directory = '/empiar/world_availability/' + entryId + '/data/Movies'

        # Establish the connection
        ftp = ftplib.FTP(server)
        ftp.login(username, password)

        # Change to the proper directory
        ftp.cwd(directory)

        # Loop through the files and download each one individually into a specific
        # directory until the stopping criteria is met
        imagesCount = 1
        for filename in ftp.nlst():
            fileAbsPath = os.path.join(downloadFolder, filename)
            if not os.path.exists(fileAbsPath):
                fhandle = open(fileAbsPath, 'wb')
                print(pwutils.yellowStr('Getting: ' + filename), flush=True)
                ftp.retrbinary('RETR ' + filename, fhandle.write)
                fhandle.close()
                shutil.move(fileAbsPath, os.path.join(finalFolder,filename))
                imagesCount += 1
                if imagesCount > limit:
                    break
        ftp.close()


.. note:: We are aware that the code above will only work with entries having the files under a "data/Movies" folder.
          This works at least for 10200 entry and smarter ftp navigation is needed to work with all EMPIAR entries.

When the stopping criteria is not met, the file will go into the ``downloadFolder`` folder.
Once the download is finished the file is moved to the ``finalFolder`` folder.

Try to run the protocol now and check that the files are being downloaded and end up in the extra folder.
Check as well that the limit is taken into account.

.. note:: At this point, there isn't any code registering the movies in Scipion.

The dynamic part
---------------------------------------

Let's add the third step that will be used later to close the set, but for now we will leave it empty.

.. code-block:: python

        def closeSetStep(self):
            """ Close the registered set. """
            pass


Also add it to the ``_insertAllSteps`` method:

.. code-block:: python

        def _insertAllSteps(self):
            self.readXmlFile = self._insertFunctionStep('readXmlFileStep')        # read the dataset xml file from EMPIAR
            self.downloadImages = self._insertFunctionStep('downloadImagesStep')  # download the movies and register them in parallel
            self.closeSet = self._insertFunctionStep('closeSetStep', wait=True)   # close the registered set

.. important:: We need to set the ``wait`` parameter to ``True`` in order to
               wait until all previous steps are finished.

Up to this point, we have only defined the "static" steps of the protocol, but
we have not yet been registering each of the downloaded movies. Now comes the "dynamic part".

Let's add a new step method to register a single movie file in scipion.

.. code-block:: python

    def registerImageStep(self, file):
        """ Register an image taking into account a file path """
        # 1) create a Movie object with file as the location argument: see pwem.objects.data.Movie()

        # 2) set the movie sampling rate using the value obtained in the readXmlFromEmpiar step

        # 3) pass the movie to _addMovieToOutput
        self._addMovieToOutput(newImage)

    def _addMovieToOutput(self, movie):
        """ Creates the output set if it does not exists.
        Adds a movie to the set. """

        # Does the protocol have the attribute "outputMovies"?
        if hasattr(self, 'outputMovies'):
            # Append the movie object to the already existing output

        else:  # we do not have output yet. Probably first movie reported

            # 1) create a SetOfMovies using its create(path) method:
            # pass the path of the current protocol (hint: self._getPath())

            # 2) set the sampling rate same way as for individual movies: set.setSamplingRate()
            # NOTE: Scipion objects are wrappers to the actual python types. To get the python value use .get() method

            # 3) set the state of the movie set to "open" (set.setStreamState). Constant for the state is Set.STREAM_OPEN.

            # 4) append the movie to the new set

            # 5) define the outputs for the protocol (_defineOutputs). Be sure you use outputMovies as the name of the output

        # In both cases, write the movie set to the disk. set.write() --> set.sqlite

        # Save the protocol with the new status: protocol._store() --> run.db


So far we have added 2 new methods: ``_addMovieToOutput`` to add a movie object to a set (creating the set if it is missing) and
the ``registerImageStep`` that is creating a specific Movie object from a file and calling the first method.
But the ``registerImageStep`` is not being invoked by the protocol yet. Furthermore, somewhere, the missing yet code should be generating
one step per downloaded file.

The ``_stepsCheck`` method
__________________________

All protocols have a method called ``_stepsCheck``. The default implementation doesn't do anything.
Scipion executes the steps in a loop until all the steps are completed. During the execution of the steps
every 3 seconds (default value for ``Protocol._stepsCheckSecs``) ``_stepsCheck`` is invoked and therefore
has the chance to do some checks to see if more steps are needed.

In our case, we have to overwrite the empty ``_stepsCheck`` method, and insert as
many ``registerImageStep`` as new files appears in the extra folder.

Let's get our hands dirty..

.. code-block:: python

    def _stepsCheck(self):
        """ Adds as many registerImageStep steps as new files appears in the extra folder
        """
        # 1) Create a list to keep all new steps to be added (newSteps)

        # 2) If the size of registeredFiles (protocol level attribute) is < amountOfImages (parameter)

            # loop through the files in the extra path (HINT: os.listdir())

                # if the file is not in our registeredFiles list

                    # append it to registeredFiles list

                    # create a new step to register the new file
                    # use _insertFunctionStep with registerImageStep adding the parameter file, and
                    # self.readXmlFile as a prerequisite parameter of the first
                    # and store the returned value in a variable (newStep)

                    # append the newStep to the newSteps list declared at the beginning

        # 3) Let's update the closeSetStep
        # 3a) get the closeSetStep from the protocol
        # Hint: any step is accessible with self._steps[stepId-1] --> what we stored in insertAllSteps

        # 3b) add the newSteps list as prerequisites for the closeSetStep
        # Hint: use the addPrerequisites method of the closeSetStep.
        # Be sure you pass the list as *newSteps

        # 4) If the number of registered files is  >= amountOfImages

            # Launch the waiting closeSet step by setting the Step.setStatus(STATUS_NEW)

        # 5) Update the protocol steps using updateSteps()


Note that the new generated steps have to be added as a dependency (``prerequisites``
parameter) for the ``closeSetStep`` step.

.. note::

        The ``prerequisites`` parameter specifies a list of stepIDs (integers) that
        a step needs to wait for before it is launched. Any ``_insertFunctionStep`` method returns a stepID.

.. important::

        In order for these steps to be launched in parallel, the ``prerequisites``
        parameter for each of them must be specified.

At this point all is in place and output should be created. Run the protocol and verify that everything is fine.

Finally, we can implement the ``closeSetStep`` which should wait for all the
movies to be registered before it is executed. Here the only thing we will do is close the
set of the movies and save the protocol changes.

.. code-block:: python

    def closeSetStep(self):
        """ Close the registered set. """
        # 1) set the outputMovies streamState to the value SetOfMovies.STREAM_CLOSED using setStreamState method

        # 2) save the outputMovies using the write() method

        # 3) save the protocol: Hint: _store()

Now if you run the protocol again in debug mode (click Project -> Debug mode in the top left menu) and
click on **Steps** then the **Tree** button, the steps graph should look like this:

.. figure:: /docs/images/general/graph_steps.png
   :width: 650
   :alt: Graph Steps
