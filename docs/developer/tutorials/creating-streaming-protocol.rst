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

`Course presentation <https://docs.google.com/presentation/d/1S7o-9dq6BjGUN7K_w5GjsOO0W5vmCV-q2U2xgDRBiAM/edit?usp=sharing>`_

Practice
========
We define a ``streaming protocol``  as a processing task that involves the
execution of several steps like any other `Scipion protocol <../creating-a-protocol>`_,
but, the inputs might appear during the protocol execution. Is impossible to
plan all the steps (difference between streaming and non streaming protocols).
The list of steps in a streaming protocol is dynamic, that is, they are added
as the input grows. These steps can even be parallelized. You can read more
about defining steps to be executed in parallel in `Parallelization <../parallelization>`_.

We will create a simple streaming protocol that connects to
`EMPIAR <https://www.ebi.ac.uk/pdbe/emdb/empiar/>`__ (Electron Microscopy
Public Image Archive), downloads a set of movies and in parallel it will
register them as outputs.

The general idea of this protocol is as follow:

.. figure:: /docs/images/general/streaming_idea.png
   :width: 750
   :alt: Streaming Idea

In that sense, we will implement the following steps:

1. Create a protocol GUI that admits as a parameter the ID of the EMPIAR dataset
   as well as a stopping criterion (in our case the number of movies to download).

   1.1. Create a protocol specifying that contains steps in parallel.

   1.2. Define the parallel section.


2. Create the steps to download and register the movie set.

   2.1. Read the xml file corresponding to a specific EMPIAR dataset which contains vital information about this movies dataset (sampling rate, dimensions, ...).

   2.2. Download movies until a stop criteria is met (amount of download movies).

   2.3. Register the downloaded movies. This step is in streaming. Constantly check if new movies have been downloaded


Defining the protocol class and the GUI
---------------------------------------

The GUI would be as the following figure shows:

.. figure:: /docs/images/general/streaming_protocol.png
   :width: 550
   :alt: Streaming Protocol

The following code contain the class definition and the protocol GUI implementation.

.. code-block:: python

    import json
    import requests
    import ftplib
    import os
    import shutil

    from pwem.objects import Movie, SetOfMovies, Float
    from pwem.protocols import EMProtocol
    from pyworkflow.protocol import (params, Positive, String, STATUS_NEW,
                                     STEPS_PARALLEL)
    import pyworkflow.utils as pwutils

    class EmpiarDownloader(EMProtocol):
        """
        Download movies sets from EMPIAR
        """
        _label = 'empiar downloader'
        _outputClassName = 'SetOfMovies' # Defining the output class
        registerFiles = []               # saves the name of the movies that have been downloaded
        _stepsCheckSecs = 3              # time in seconds to check the steps


        def __init__(self, **args):
            EMProtocol.__init__(self, **args)
            self.stepsExecutionMode = STEPS_PARALLEL # Defining that the protocol contain parallel steps

        def _defineParams(self, form):
            # add a section

            # add a parameter to capture the EMPIAR entry ID:
            # name --> entryId, String param, default value 10200, you choose the label
            # Ideally we want it in bold is "important", it should not be empty, and fill the help.

            # add another parameter to set a limit of downloaded files:
            # name-->amountOfImages, Integer param , default to 5, choose the label and the help
            # it has to be positive (use "validators" argument, it expects a list of
            # pyworkflow.protocol.params.Validator, look for teh Positive Validator)

            # Parallel section defining the number of threads and mpi to use
            form.addParallelSection(threads=3, mpi=1)


.. note::

        Note that in the ``__init__`` method, we are specifying
        stepsExecutionMode parameter, and in the _defineParams we are invoking
        addParallelSection method.

Create the steps to download and register the movie set
--------------------------------------------------------

First, we implement the ``_insertAllSteps`` method to define the different steps.
The first step read the dataset xml file from EMPIAR.

.. code-block:: python

        def _insertAllSteps(self):
            # insert a functionStep (readXmlFileStep) to read the xml file from EMPIAR entry

        def readXmlFileStep():

            # Call the method provided bellow to get some data from the empiar xml

            # Store returned values as "persistent" attributes: String, Integer, Float
            # Use _store method to write them

        def _summary(self):
            summary = []

            # Check we have the attributes (readXmlStep has happened) (HINT: hasattr will do)

                # Add items to the summary list like:
                # "Title: %s" % ??
                # "Sampling rate: %s" % ??
                # How would you have more values in the summary? (HINT: return more values in readXmlFromEmpiar)

            return summary

we provide you the code that reads EMPIAR's xmls:

.. code-block:: python

    def readXmlFromEmpiar(entryId):
            """
            Read the xml file of a specific dataset from EMPIAR repository
            """
            empiarXmlUrl = 'https://www.ebi.ac.uk/pdbe/emdb/empiar/api/entry/' + entryId  # URL of EMPIAR API

            xmlFile = requests.get(empiarXmlUrl, allow_redirects=True)                    # getting the xml file
            content = (json.loads(xmlFile.content.decode('utf-8')))                       # extract the xml content
            empiarName = 'EMPIAR-' + xmlFileName                                          # dataset name

            corresponingAuthor = content[empiarName]['corresponding_author']         # dataset authors
            organization = String(self.corresponingAuthor['author']['organization']) # authors organization
            depositionDate = String(content[empiarName]['deposition_date'])          # dataset deposition date
            title = String(content[empiarName]['title'])                             # dataset title
            imageSets = content[empiarName]['imagesets']                             # dataset images information
            releaseDate = String(content[empiarName]['release_date'])                # dataset release date
            datasetSize = String(content[empiarName]['dataset_size'])                # dataset size
            empiarName = String(empiarName)
            samplingRate = Float(self.imageSets[0]['pixel_width'])                   # images sampling rate
            dataFormat = String(self.imageSets[0]['data_format'])                    # images format

            # You may want to return more elements
            return title, samplingRate


Now your protocol should be able to run, try it now, and get some information from the empiar entry xml. Check the summary looks good.

After the execution, the Summary panel could show the following information if you manage to store all values:


.. figure:: /docs/images/general/summary.png
   :width: 450
   :alt: Summary


.. tip::

    All the values that we want to have in the summary (title, samplingrate, ...)
    have to be those from Scipion (String, Integer, ...) that automatically get persisted.

After that, we'll add into ``_insertAllSteps`` method the second step. This step
will download the movies from the entry (``entryId``) ftp until the amount
specified (``amountOfImages``) is reached.

.. code-block:: python

        def _insertAllSteps(self):
            self._insertFunctionStep('readXmlFileStep')        # read the dataset xml file from EMPIAR

            self._insertFunctionStep('downloadImagesStep')  # download the movies and register them in pararell

        def downloadImagesStep():
            # Call the method provided bellow.
            # Make the download happen on the tmp folder of the protocol and the final folder to be the extra folder

The code bellow should download files from empiar:

.. code-block:: python

        def downloadImagesFromEmpiar(entryId, downloadFolder, finalFolder, limit=5):
            """
            This method connect to EMPIAR repository and download a set of images
            into a specific directory, once image is downloaded is moved to the final folder
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

            # Loop through files and download each one individually into a specific
            # directory until the stop criteria met
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
          This works for at least 10200 entry and a smarter ftp navigation is needed to work with all EMPIAR entries.

While the stopping criteria is not met, it will be downloading files to the
``downloadFolder`` folder. Once the download is finished it is moved to the ``finalFolder`` folder.

Try to run it now and check that the files are being downloaded and end up in the extra folder. Check as well that the limit is taken into account.

.. note:: At this point, there isn't any code registering the movies in Scipion.

Let's at third step consists of closing the movie set that has been registered in
Scipion. The definition of this step is as follow:

.. code-block:: python

        def closeSetStep(self):
            """
            Close the registered set
            """
            pass

Note that at this moment, ``closeSetStep`` has not implementation. The reason is that we hasn't created
the set of movies yet.

However, we will add it into ``_insertAllSteps`` method:

.. code-block:: python

        def _insertAllSteps(self):
            self.readXmlFile = self._insertFunctionStep('readXmlFileStep')        # read the dataset xml file from EMPIAR
            self.downloadImages = self._insertFunctionStep('downloadImagesStep')  # download the movies and register them in pararell
            self.closeSet = self._insertFunctionStep('closeSetStep', wait=True)   # close the registered dataset set

.. important:: We need to set the ``wait`` parameter to ``True`` in order to
               wait until all movies have been registered.

Up to this point, we have only defined the “static” steps of the protocol, but
we have not yet been registering each of the downloaded movies. For that, we
must create a new step that guarantees the registration of all movies. Next we
define the method where we will have to carry out the steps that are commented.

.. code-block:: python

        def registerImageStep(self, file):
            """
            Register an image taking into account a file path
            """
            # Create a Movie into the protocol extra folder
            # Set the movie sampling rate with the sampling rate obtained in the readXmlFromEmpiar step
            self._addMovieToOutput(newImage)

        def _addMovieToOutput(self, movie):
            """
            Returns the output set if not available create an empty one
            """
            if hasattr(self, 'outputMovies'): # the output is defined
                outputSet = self.outputMovies
                outputSet.append(movie)
            else:
                outputSet = SetOfMovies.create(self._getPath())
                outputSet.setSamplingRate(self.samplingRate.get())
                outputSet.setStreamState(outputSet.STREAM_OPEN)
                outputSet.append(movie)
                self._defineOutputs(outputMovies=outputSet)
            outputSet.write()
            self._store()


Now, this process should be checking given a reasonable time if there are new
movies in the download directory. In that sense, for each movie that is downloaded,
a new step will be created and it will be launched in parallel. At the same time
the number of steps of the protocol will be updated.

How do we make this happen?

When a protocol is launched, a check can be made of each of its steps. The
method that is in charge of doing this operation is the ``_stepsCheck`` method,
which when the protocol does not work in streaming it is not necessary to
define it because the input is static. In the case of streaming protocols, an
implementation can be done. In our case we will use this method to check if
there are new movies. If so, then we generate a new step to register it and at
the same time, this new step is added as a dependency (``prerequisites``
parameter) to ``closeSetStep`` step.

.. note::

        The ``prerequisites`` parameter specifies a list of steps that it needs to
        wait for in order to be launched.

.. important::

        In order for these processes to be launched in parallel, the ``prerequisites``
        parameter of each of them must be specified (it must be empty. In the case that
        we specify IDs as prerequisites, the step will not be executed until the steps
        that respond to the IDs have finished).

.. code-block:: python

        def _stepsCheck(self):
            """ Input movie set can be loaded or None when checked for new inputs
                If None, we load it.
                To allow streaming register a movies, we need to detect a new
                movie ready to register into the extra path folder.
                prerequisites parameter is empty
            """
            depStepsList = []
            if len(self.registerFiles) < self.amountOfImages.get():
                for file in os.listdir(self._getExtraPath()):
                    if file not in self.registerFiles:
                        self.registerFiles.append(file)
                        # Creating a new step to register the new movie
                        lastSteps = self._insertFunctionStep('registerImageStep',
                                                             file,
                                                             prerequisites=[])
                        depStepsList.append(lastSteps)
                        # adding as prerequisites the new step to closeSetStep
                        self._steps[self.closeSet-1].addPrerequisites(*depStepsList)

                    if len(self.registerFiles) >= self.amountOfImages.get(): # The closeSetStep is ready to launch
                        self._steps[self.closeSet].setStatus(STATUS_NEW)

                # Updating the protocol steps
                self.updateSteps()

As we could see in the previous code, we check if there are new files in the
download directory and for each one of them we create a new step. At the same
time we are adding it as a prerequisite to the ``closeSetStep`` step.


Finally, we can do an implementation of ``closeSetStep``, which would wait for all the
movies to be registered to launch. Here the only thing we will do is close the
set of the movies and save the protocol changes.

Following the three steps outlined within the following method, complete the code:

.. code-block:: python

        def closeSetStep(self):
            """
            Close the registered set
            """
            # 1. Set the outputMovies streamState using setStreamState method with the value SetOfMovies.STREAM_CLOSED
            # 2. Save the outputMovies using the write() method
            # 3. Save the protocol

The dependencies steps graph should look like this:

.. figure:: /docs/images/general/graph_steps.png
   :width: 650
   :alt: Graph Steps

