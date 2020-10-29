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

.. warning::
    This protocol is artificially streamified and will have problems with of concurrency
    or in case of resuming it after a failure. But for the shake of simplicity, we are
    we are ignoring this "secondary" problems.

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
        registeredFiles = []               # saves the name of the movies that have been already registered
        _stepsCheckSecs = 3              # time in seconds to check the steps


        def __init__(self, **args):
            EMProtocol.__init__(self, **args)
            self.stepsExecutionMode = STEPS_PARALLEL # Defining that the protocol contain parallel steps

        def _defineParams(self, form):
            # add a section

            # add a parameter to capture the EMPIAR entry ID:
            # name --> entryId, String param, default value 10200, you choose the label
            # Ideally we want it in bold is "important", and fill the help.

            # add another parameter to set a limit of downloaded files:
            # name-->amountOfImages, Integer param , default to 1, choose the label and the help
            # it has to be positive (use "validators" argument, it expects a list of
            # pyworkflow.protocol.params.Validator, look for the Positive Validator)

            # Parallel section defining the number of threads and mpi to use
            form.addParallelSection(threads=3, mpi=1)


.. note::

        Note that in the ``__init__`` method, we are specifying
        stepsExecutionMode parameter, and in the _defineParams we are invoking
        addParallelSection method. This is telling scipion that the steps can be
        run in parallel (threads or mpi)

At this point you should be able to find the protocol using Ctrl+F and open it and see the unused parameters.

Create the steps to download and register the movie set
--------------------------------------------------------

First, we implement the ``_insertAllSteps`` method to define the different steps.
The first step read the dataset xml file from EMPIAR.

.. code-block:: python

        def _insertAllSteps(self):
            # insert a functionStep (readXmlFileStep) to read the xml file from EMPIAR entry

        def readXmlFileStep(self):

            # Call the method provided bellow to get some data from the empiar xml


            # Store returned values as "persistent" attributes: String, Integer, Float


            # Use _store method to write them

        def _summary(self):
            summary = []

            # Check we have the any summary attribute (readXmlStep has happened) (HINT: hasattr will do)

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

            xmlFile = requests.get(empiarXmlUrl, allow_redirects=True)               # getting the xml file
            content = (json.loads(xmlFile.content.decode('utf-8')))                  # extract the xml content
            empiarName = 'EMPIAR-' + entryId                                         # dataset name

            correspondingAuthor = content[empiarName]['corresponding_author']         # dataset authors
            organization = String(correspondingAuthor['author']['organization']) # authors organization
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


Now your protocol should be able to run, try it now, and get some information from the empiar entry xml. Check the summary looks good.

After the execution, the Summary panel could show the following information if you manage to store all values:


.. figure:: /docs/images/general/summary.png
   :width: 450
   :alt: Summary


.. tip::

    All the values that we want to have in the summary (title, samplingRate, ...)
    have to be those from Scipion (String, Integer, ...) that automatically get persisted.

After that, we'll add into ``_insertAllSteps`` method the second step. This step
will download the movies from the entry (``entryId``) ftp until the amount
specified (``amountOfImages``) is reached.

.. code-block:: python

        def _insertAllSteps(self):

            self._insertFunctionStep('readXmlFileStep')        # read the dataset xml file from EMPIAR
            self._insertFunctionStep('downloadImagesStep')  # download the movies and register them in paralell

        def downloadImagesStep(self):
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

Let's add a third step that will be used later to close the set, but for now we will leave it empty.

.. code-block:: python

        def closeSetStep(self):
            """
            Close the registered set
            """
            pass


and add it into ``_insertAllSteps`` method:

.. code-block:: python

        def _insertAllSteps(self):
            self.readXmlFile = self._insertFunctionStep('readXmlFileStep')        # read the dataset xml file from EMPIAR
            self.downloadImages = self._insertFunctionStep('downloadImagesStep')  # download the movies and register them in pararell
            self.closeSet = self._insertFunctionStep('closeSetStep', wait=True)   # close the registered dataset set

.. important:: We need to set the ``wait`` parameter to ``True`` in order to
               wait until the protocol decides when all work is done.

Up to this point, we have only defined the "static" steps of the protocol, but
we have not yet been registering each of the downloaded movies and introduced this
``wait=True`` for the ``closeSetStep``. Now it comes the "dynamic part".

Let's add a new step method to register a single movie file in scipion.

.. code-block:: python

    def registerImageStep(self, file):
        """
        Register an image taking into account a file path
        """
        # Create a Movie object having file as the location: see pwem.objects.data.Movie()


        # Set the movie sampling rate with the sampling rate obtained in the readXmlFromEmpiar step


        # Pass the movie to _addMovieToOutput
        self._addMovieToOutput(newImage)

    def _addMovieToOutput(self, movie):
        """
        Returns the output set if not available create an empty one
        """

        # Do we have the attribute "outputMovies"?
        if hasattr(self, 'outputMovies'): # the output is defined

            # Append the "movie" passed to the already existing output


        # ... we do not have output yet. Probably first movie reported
        else:

            # Create the SetOfMovies using its create(path) method: pass the path of the protocol (hint: self._getPath())


            # set the sampling rate: set.setSamplingRate() passing the stored sampling rate from the readXmlFromEmpiarStep
            # NOTE: Scipion objects are wrappers to actual python types. To get the python value use .get() method


            # set the set .streamState to open (set.setStreamState). Constant for the state is at Set.STREAM_OPEN.


            # append the movie to the new set just created


            # define the output in the protocol (_defineOutputs). Be sure you use outputMovies as the name of the output


        # In both cases, write the set to the disk. set.write() --> set.sqlite


        # Save the protocol with the new  status: protocol._store() --> run.db


So far we have added 2 new methods: one to add a movie object to a set (creating the set if it is missing) and
another , the ``registerImageStep`` that is creating a specific Movie object from a file and calling the first one.
But the ``registerImageStep`` is not being invoked. Furthermore, somewhere, the missing code, should be generating
one step per downloaded file.

The ``_stepCheck`` method
_________________________

All protocols have a method called ``_stepCheck``. The default implementation doesn't do anything.
Scipion executes the steps in a loop until all the steps are completed. During the execution of the steps,
every 3 seconds (default value for ``Protocol._stepsCheckSecs``) ``_stepCheck`` is invoked and therefore
has the chance to do some checks and see if more steps are needed.

In our case, we have to overwrite the empty ``_stepCheck`` method, and insert as
many ``registerImageStep`` as new files appears in extra folder.

Let's get our hands dirty

.. code-block:: python

    def _stepsCheck(self):
        """ Adds as many registerImageStep as new files appears in the extra folder
        """

        # Declare a list to keep all new steps added this call (newSteps)


        # If the size of registeredFiles (object level attribute) is < amountOfImages (parameter)


            # loop through the files in the extra path


                # if the file is not annotated our registeredFiles list


                    # Append it to registeredFiles list


                    # Create a new step to register the new file (item of this loop)
                    # use _insertFunctionStep with registerImageStep, file, and
                    # self.readXmlFile as a prerequisite
                    # and store the returned value in a variable (newStep)


                    # append the newStep to the newSteps list declared at the beginning


            # Let's update the closeSetStep
            # Get the closeSetStep store it in closeSetStep
            # Hint: the list of steps are accessible with self._steps[stepId-1] --> what we stored in insertAllSteps


            # Add the new steps as prerequisites for the closeSetStep (to keep a coherent Step tree)
            # Use the addPrerequisites method of the closeSetStep.
            # Be sure you pass the list as parameters *newSteps


            # If we have reached the limit of files (amountOfImages) compared with registeredFiles


                # Free up the waiting closeSet step by setting the Step.setStatus(STATUS_NEW)
                # Not waiting anymore


            # Update the protocol steps using updateSteps()


Note that when the new generated steps have to be added as a dependency (``prerequisites``
parameter) of ``closeSetStep`` step.

.. note::

        The ``prerequisites`` parameter specifies a list of step identifiers (integers) that
        a step needs to wait for before it is launched:

.. important::

        In order for these processes to be launched in parallel, the ``prerequisites``
        parameter of each of them must be specified. Not passing the parameter
        will default to be dependent of the previous step, closeSetStep that is waiting!.


At this point all is in place and output should be created. Run the protocol and verify all is fine.

Finally, we can implement ``closeSetStep``, which should wait for all the
movies to be registered before it is executed. Here the only thing we will do is close the
set of the movies and save the protocol changes.

Following the three steps outlined within the following method, complete the code:

.. code-block:: python

    def closeSetStep(self):
        """
        Close the registered set
        """
        # Set the outputMovies streamState using setStreamState method with the value SetOfMovies.STREAM_CLOSED


        # Save the outputMovies using the write() method


        # Save the protocol: Hint: _store()

The dependencies steps graph should look like this:

.. figure:: /docs/images/general/graph_steps.png
   :width: 650
   :alt: Graph Steps

