.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _creating-streaming-protocol:

=============================
Creating a Streaming Protocol
=============================

We define a ``Streaming Protocol``  as a processing task that involves the
execution of several steps like any other `Scipion protocol <creating-a-protocol>`_,
but, some execution steps work in parallel. You can read more about defining steps to be executed
in parallel in `Parallelization <parallelization>`_.

We will create a simple protocol that connects to
`EMPIAR <https://www.ebi.ac.uk/pdbe/emdb/empiar/>`__ (Electron Microscopy
Public Image Archive) and downloads a set of Movies and in parallel it will
register them in Scipion.

The general idea of this protocol is as follow:

.. figure:: /docs/images/general/streaming_idea.png
   :width: 250
   :alt: Streaming Idea

In that sence, we will implement the following steps:

1. Create a protocol GUI that admits as a parameter the ID of the EMPIAR dataset
   as well as a stopping criterion (in our case the number of movies to download).

   1.1. Specify that the protocol contain steps in parallel.

   1.2. Define the parallel section.


2. Create the steps to download and register the movie set.

   2.1. Read the xml file corresponding to a specific EMPIAR dataset which contains vital information about this movies dataset (sampling rate, dimension, ...).

   2.2. Download one by one movies until a stop criteria is met (amount of download movies).

   2.3. Register the downloaded movies. This step is in parallel with steps 2.


Defining the protocol class and the GUI
---------------------------------------

The following code contain the class definition and the protocol GUI implementation.
Note that into the ``__init__`` method, the parameter to especify that the protocol
contain steps in parallel is defined. On the other hand, the parallel section is inserted
into the protocol GUI.

.. code-block:: python

    class EmpiarDownloader(EMProtocol):
    """
    Download movies sets from EMPIAR
    """
    _label = 'empiar downloader'
    _outputClassName = 'SetOfMovies' # Defining the output class
    registerFiles = []               # saves the name of the movies that have been downloaded

    def __init__(self, **args):
        EMProtocol.__init__(self, **args)
        self.stepsExecutionMode = STEPS_PARALLEL # Defining that the protocol contain parallel steps

    def _defineParams(self, form):
        form.addSection(label='Entry')
        form.addParam('entryID', params.StringParam, default='10200', # EMPIAR dataset ID
                      label='EMPIAR ID',
                      important=True,
                      allowsNull=False,
                      help='EMPIAR entry ID')
        form.addParam('amountOfImages', params.IntParam, # Stop criteria
                      default=5,
                      label='Amount of Images',
                      validators=[Positive],
                      help='Time that the protocol will be running expressed in seconds')
        form.addParallelSection(threads=2, mpi=1) # Parallel section defining the number of threads and mpi to use

The GUI would be as the following figure shows:

.. figure:: /docs/images/general/streaming_protocol.png
   :width: 250
   :alt: Streaming Protocol



Create the steps to download and register the movie set
--------------------------------------------------------

First, we implement the ``_insertAllSteps`` method to define the diferente steps.

.. code-block:: python

        def _insertAllSteps(self):
            self.readXmlFile = self._insertFunctionStep('readXmlFileStep')        # read the dataset xml file from EMPIAR
            self.downloadImages = self._insertFunctionStep('downloadImagesStep')  # download the movies and register them in pararell
            self.closeSet = self._insertFunctionStep('closeSetStep', wait=True)   # close the registered dataset set


After thats, we'll implement and explain each of steps line by line.

.. code-block:: python

        def readXmlFileStep(self):
            """
            Read the xml file of a specific dataset from EMPIAR repository
            """
            xmlFileName = self.entryID.get()                                                  # dataset ID
            empiarXmlUrl = 'https://www.ebi.ac.uk/pdbe/emdb/empiar/api/entry/' + xmlFileName  # URL of EMPIAR API
            try:
                xmlFile = requests.get(empiarXmlUrl, allow_redirects=True)                    # getting the xml file
                content = (json.loads(xmlFile.content.decode('utf-8')))                       # extract the xml content
                empiarName = 'EMPIAR-' + xmlFileName                                          # dataset name
                self.corresponingAuthor = content[empiarName]['corresponding_author']         # dataset authors
                self.organization = String(self.corresponingAuthor['author']['organization']) # authors organization
                self.depositionDate = String(content[empiarName]['deposition_date'])          # dataset deposition date
                self.title = String(content[empiarName]['title'])                             # dataset title
                self.imageSets = content[empiarName]['imagesets']                             # dataset images information
                self.releaseDate = String(content[empiarName]['release_date'])                # dataset release date
                self.datasetSize = String(content[empiarName]['dataset_size'])                # dataset size
                self.empiarName = String(empiarName)
                self.samplingRate = Float(self.imageSets[0]['pixel_width'])                   # images sampling rate
                self.dataFormat = String(self.imageSets[0]['data_format'])                    # images format

                self._store(self)
            except Exception as ex:
                self.setFailed(msg="There was an error downloading the EMPIAR raw "
                                   "images: %s!!!" %ex)


        def downloadImagesStep(self):
            """
            This method connect to EMPIAR repository and download a set of images
            into a specific directory
            """
            # Connection information
            server = 'ftp.ebi.ac.uk'
            username = 'anonymous'
            password = ''

            # Directory information
            directory = '/empiar/world_availability/' + self.entryID.get() + '/data/Movies'

            # Establish the connection
            ftp = ftplib.FTP(server)
            ftp.login(username, password)

            # Change to the proper directory
            ftp.cwd(directory)

            # Loop through files and download each one individually into a specific
            # directory until the stop criteria met
            imagesCount = 1
            for filename in ftp.nlst():
                fileAbsPath = os.path.join(self._getTmpPath(), filename)
                if not os.path.exists(fileAbsPath):
                    fhandle = open(fileAbsPath, 'wb')
                    print(pwutils.yellowStr('Getting: ' + filename), flush=True)
                    ftp.retrbinary('RETR ' + filename, fhandle.write)
                    fhandle.close()
                    shutil.move(fileAbsPath, self._getExtraPath(filename))
                    imagesCount += 1
                    if imagesCount > self.amountOfImages.get():
                        break
            ftp.close()


        def closeSetStep(self):
            """
            Close the registered set
            """
            self.outputMovies.setStreamState(SetOfMovies.STREAM_CLOSED)
            self.outputMovies.write()
            self._store()


Now, we must register each movies that has been downloaded. In that sense, for
each movie that is downloaded, a new step will be created and it will be
launched in parallel.

In order for these processes to be launched in parallel, the ``prerequisites``
parameter of each of them must be specified (it must be empty or with IDs of
previous steps on which they depend). In this case


.. code-block:: python

        def _stepsCheck(self):
            """ Input movie set can be loaded or None when checked for new inputs
                If None, we load it.
                To allow streaming register a movies we need to detect a new
                movie ready to register into the extra path folder
                Add as prerequisites(registerImageStep) to the last step(closeSetStep)
            """
            depStepsList = []
            if len(self.registerFiles) < self.amountOfImages.get():
                for file in os.listdir(self._getExtraPath()):
                    if file not in self.registerFiles:
                        self.registerFiles.append(file)
                        lastSteps = self._insertFunctionStep('registerImageStep',
                                                             file,
                                                             prerequisites=[self.readXmlFile])
                        depStepsList.append(lastSteps)

                    if len(self.registerFiles) >= self.amountOfImages.get():
                        self._steps[self.closeSet].setStatus(STATUS_NEW)
                        self._steps[self.closeSet].addPrerequisites(*depStepsList)

                self.updateSteps()

        def registerImageStep(self, file):
            """
            Register an image taking into account a file path
            """
            newImage = Movie(location=self._getExtraPath(file))
            newImage.setSamplingRate(self.samplingRate.get())
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







