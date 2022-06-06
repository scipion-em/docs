.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _creating-a-monitor:

==================
Creating a monitor
==================

What is a monitor?
==================

A monitor is a non-GUI class which main action would be to do something,
periodically and notify any possible "listeners". All code presented in this guide is available in
our `docs repository <https://github.com/scipion-em/docs/tree/release-3.0.0/code_examples/monitor_tutorial>`_

Monitors anatomy
================

The base :class:`monitor class<pyworkflow.em.protocol.monitors.protocol_monitor.Monitor>` looks like this:

.. code-block:: python

    class Monitor():
        def __init__(self, **kwargs):
            # Where to store any data from this monitor
            self.workingDir = kwargs['workingDir']
            self.samplingInterval = kwargs.get('samplingInterval', None)
            self.monitorTime = kwargs.get('monitorTime', None)

            self._notifiers = []

            if kwargs.get('email', None) is not None:
                self._notifiers.append(kwargs['email'])

            if 'stdout' in kwargs:
                self._notifiers.append(PrintNotifier())

        def notify(self, title, message):
            for n in self._notifiers:
                if n: 
                    n.notify(title, message)

        def info(self, message):
            self.notify("INFO", message)

        def initLoop(self):
            """ To be defined in subclasses. """
            pass

        def loop(self):
            self.initLoop()
            timeout = time.time() + 60. * self.monitorTime   # interval minutes from now

            while True:
                finished = self.step()
                if (time.time() > timeout) or finished:
                    break
                time.sleep(self.samplingInterval)

        def step(self):
            """ To be defined in subclasses. """
            pass

        def addNotifier(self, notifier):
            self._notifiers.append(notifier)

The most important method of a monitor is

.. code-block:: python

        def step(self):
            """ To be defined in subclasses. """
            pass

In this base class it is not implemented, but if you want to develop a
monitor, you have to implement this method. The **step()** method will be
called from the **loop()** in a regular manner until a
**self.monitorTime** is reached or it is intentionally stopped.

Optionally, you can code an **initLoop()** method that will be called
before the loops start, suitable for some initializations.

Additionally, monitors follow an `observer
pattern <https://en.wikipedia.org/wiki/Observer_pattern>`__ where any
interested "listener/observer" could register and receive notifications
from the monitor.

Developing a disk space monitor
===============================

Let's start coding something. Let's create a python file in our tutorial
package and create there our new monitor class.

First iteration
---------------

1. Create a new folder called ``myfacility``, and inside it, a folder called ``protocols``.
2. Add a ``space_monitor.py`` file to ``<your-path>/myfacility/protocols``
3. Import :class:`Monitor<pyworkflow.em.protocol.monitors.protocol_monitor.Monitor>`
   base class, and define your new class based on ``Monitor``

.. code-block:: python

    from  pyworkflow.em.protocol.monitors import Monitor


    class SpaceMonitor(Monitor):
        """
        Monitor to monitor free space on the HD where scipion project is placed
        """

4. Implement the step method. This method should find the HD where the
   project is placed.

Import some modules at the top of the file (import section)

.. code-block:: python

    import os
    import collections

Add the following to the step method:

.. code-block:: python

        def step(self):
            """ Using the workingdir attribute has to find the HD and then get the
            available free space."""

            usage = disk_usage(self.workingDir)

            print(usage)

    # Taken from http://code.activestate.com/recipes/577972-disk-usage/
    def disk_usage(path):
        _ntuple_diskusage = collections.namedtuple('usage', 'total used free')

        st = os.statvfs(path)
        free = st.f_bavail * st.f_frsize
        total = st.f_blocks * st.f_frsize
        used = (st.f_blocks - st.f_bfree) * st.f_frsize
        return _ntuple_diskusage(total, used, free)

This is adding a new method ``disk_usage`` which receives a path and
uses it in the step method, printing it (temporarily).

5. Expose new monitor to the package: import the monitors in ``<your-path>/myfacility/protocols/__init__.py``

.. code-block:: python
    :caption: protocols/__init__.py

    from space_monitor import SpaceMonitor, ProtMonitorSpace

In addition, for Scipion to detect ``myfacility``, we need to add its container path to the ``PYTHONPATH``.
Remember to do this in your terminal before you test anything related with this tutorial.

.. code-block:: bash

    $ export PYTHONPATH=~/Desktop/scipion-em-myfacility:$PYTHONPATH

Testing first iteration
~~~~~~~~~~~~~~~~~~~~~~~

We are going now to add some tests to check our progress.

1. Add a tests folder to the package (``<your-path>/myfacility/tests``
2. Add an empty ``__init__.py`` to make it a module
3. Add ``test_monitor.py`` to the tests folder
4. Add the code below

.. code-block:: python
    :caption: tests/test_monitor.py

    import os
    from pyworkflow.tests import *
    from myfacility.protocols import SpaceMonitor

    # Test monitor functionality
    class TestMonitor(BaseTest):

        def test_monitor(self):

            # Instantiate the monitor
            spaceMonitor = SpaceMonitor(workingDir=os.getcwd())

            spaceMonitor.step()

5. Run the test. Take into account that ``PYTHONPATH`` needs to be set.

.. code-block:: bash

   scipion test myfacility.tests.test_monitor.TestMonitor

Output should look like this:

.. code-block:: shell

    Scipion  (2018-06-12)  ((HEAD detached at june_2018_course) b9d0e37)

    >>>>> python  scripts/run_tests.py myfacility.tests.test_monitor.TestMonitor
    Running tests....
    usage(total=245527773184, used=127268225024, free=105763827712)
    [ RUN   OK ] TestMonitor.test_monitor (0.001 secs)

    [==========] run 1 tests (0.001 secs)
    [  PASSED  ] 1 tests

The disk stats are printed on the screen. This is not a proper test
since it will never fail and there are no checks (assertions) but soon we
will add them.

2nd iteration: persist the values in a txt file
-----------------------------------------------

We need to persist/store the values, and the easiest approach here is to
write the values in a text file.

Test first
~~~~~~~~~~

Following a
`TDD <https://en.wikipedia.org/wiki/Test-driven_development>`__
approach, we will first modify the test to expect the new behaviour.
Since we are going to generate files, let's tell the monitor to use a
temporary folder instead of the ``os.getcwd()``. For this we need to
first import at the top mkdtemp function from tempfile
``from tempfile import mkdtemp`` and then use it when creating the
monitor in ``myfacility/tests/test_monitor.py`` file:

.. code-block:: python
    :caption: tests/test_monitor.py

    from tempfile import mkdtemp
    [ . . . . . ]
        def test_monitor(self):

            # Instantiate the monitor
            spaceMonitor = SpaceMonitor(workingDir=mkdtemp())

            spaceMonitor.step()

            # Check storage file exists
            fnStorageFile = spaceMonitor.getStorageFilePath()

            # Check that the file exists
            self.assertTrue(os.path.exists(fnStorageFile),
                            "Storage file %s not created." % fnStorageFile)

            # Check there are 2 lines (headers and first data line)
            num_lines = sum(1 for line in open(fnStorageFile,'r'))

            # Assert lines are 2
            self.assertEqual(2, num_lines,
                             "First step of the monitor does not "
                             "have the expected lines: %s" % 2)

Additionally, we have added some lines to:
* get the name of the storage file
* assert that it exists
* and test that it has 2 lines
* Since we haven't modified our Monitor yet this test should fail

.. code-block:: shell

    [   FAILED ] TestMonitor.test_monitor

    Traceback (most recent call last):
      File "/home/pablo/desarrollo/scipion/software/lib/python2.7/unittest/case.py", line 329, in run
        testMethod()
      File "/home/pablo/desarrollo/scipion/pyworkflow/em/packages/myfacility/tests/test_monitor.py", line 16, in test_monitor
        fnStorageFile = spaceMonitor.getStorageFilePath()
    AttributeError: SpaceMonitor instance has no attribute 'getStorageFilePath'

    [==========] run 1 tests (0.003 secs)
    [  FAILED  ] 1 tests
    [  PASSED  ] 0 tests

Our monitor does not have the ``getStorageFilePath()`` function.

Monitor second
~~~~~~~~~~~~~~

Let's implement what the test is expecting:

.. code-block:: python
    :caption: protocols/space_monitor.py

        def step(self):
            """ Using the workingdir attribute has to find the HD and then get the
            available free space."""

            usage = disk_usage(self.workingDir)

            self.storeUsageData(usage)

        def getStorageFilePath(self):
            return os.path.join(self.workingDir, 'space_usage.txt')

        def storeUsageData(self, usageData):

            fnStorageFile = self.getStorageFilePath()

            if not os.path.exists(fnStorageFile):
                fhStorage = open(fnStorageFile, "w")
                fhStorage.write("total\tused\tfree\n")
            else:
                fhStorage = open(fnStorageFile, "a")

            fhStorage.write("%s\t%s\t%s\n" % (usageData.total, usageData.used, usageData.free))

            fhStorage.close()

Note that we have:
1. Implemented the ``getStorageFilePath()`` method.
2. Implemented a ``storeUsageData()`` to store our usage data
3. In the ``step()`` function we have called the storage function: ``self.storeUsageData(usage)``

Using the Monitor
=================

What we have done is just a piece of "behaviour" it will calculate the
statistics of the HD where a certain folder (workingFolder) belongs. But
how can we start it from a Scipion project?

Protocol monitor
----------------

There is a special protocol (ProtMonitor) that is designed to have
monitors running. It can be found at
:class:`pyworkflow.em.protocol.monitors.protocol_monitor.ProtMonitor`. It inherits
from ``EMProtocol`` and defines several parameters: 

* ``inputProtocols``: Protocols to be monitored 
* ``samplingInterval``: Monitoring time interval between samples
* ``Mail params`` (Optional): All email params needed to send emails

Note that our case, monitoring the HD, does not require any specific
inputProtocol to monitor.

Additionally, this special protocol will create a "monitorStep" that any
"implementer" has to implement:

.. code-block:: python

        # -------------------------- INSERT steps functions -----------------------
        def _insertAllSteps(self):
            self._insertFunctionStep('monitorStep')

        # -------------------------- STEPS functions ------------------------------
        def monitorStep(self):
            pass

First iteration: Space monitor protocol
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's define a new Class for our Space Monitor Protocol at ``space_monitor.py``.
1. Import ProtMonitor and PrintNotifier at the top:
2. Import last version
3. Add our ProtMonitorSpace:

.. code-block:: python
    :caption: protocols/space_monitor.py

    from pyworkflow.em import ProtMonitor, PrintNotifier
    from pyworkflow import VERSION_2_0

    class ProtMonitorSpace(ProtMonitor):

        _label = 'monitor of HD space'
        _lastUpdateVersion = VERSION_2_0

        # Overwrite the monitor step function
        def monitorStep(self):

            # Instantiate a Space Monitor
            monitor = SpaceMonitor(workingDir=self._getExtraPath(),
                                   samplingInterval=self.samplingInterval.get(),
                                   monitorTime=100)

            monitor.addNotifier(PrintNotifier())
            monitor.loop()

4. Make our monitor to notify something, at the end of out
   SpaceMonitor.step() add ``self.notify("HD stats", str(usage))``

5. Expose the new protocol to Scipion. In  ``myfacility/protocols/__init__.py``
   add:

.. code-block:: python
    :caption: myfacility/protocols/__init__.py

    from space_monitor import SpaceMonitor, ProtMonitorSpace``

Now Scipion should be able to discover it and you should be able to run
it:

.. figure:: /docs/images/monitor_tutorial/spaceprotdiscovered.png

    We can find our new monitor if we search using Ctrl-F

.. figure:: /docs/images/monitor_tutorial/runningspacemonitor.png

    And we can run it!

So far this is OK, but:

* The output is hardly readable....we should convert bytes into GB (at least) to be human-friendly
* More important, there is only a Print notifier, so someone has to actively look at the logs.
* A plot might be useful to plot the HD stats.

2nd iteration: Space monitor protocol tweaks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Human-friendly output
^^^^^^^^^^^^^^^^^^^^^

1. Import ``from pyworkflow.utils import prettySize``
2. In the step function of SpaceMonitor, just before calling notify, convert the
   values and modify the notify call:

.. code-block:: python
    :caption: protocols/space_monitor.py

    from pyworkflow.utils import prettySize

    [ . . . ]

       self.storeUsageData(usage)

       # Stats line readable:
       free = prettySize(usage.free)
       total = prettySize(usage.total)
       used = prettySize(usage.used)

       self.notify("HD stats (%s)" % self.workingDir,
                   "Free: %s, Total: %s, Used: %s" % (free, total, used))```

Add an Email notifier... and remove the inputProtocols
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Let's tweak the parameters of the protocol:

Import params from em, like so:
``from pyworkflow.em import ProtMonitor, PrintNotifier, params``

.. code-block:: python
    :caption: protocols/space_monitor.py

    from pyworkflow.em import ProtMonitor, PrintNotifier, params

    [ . . . ]

        _label = 'monitor of HD space'
        _lastUpdateVersion = VERSION_2_0

        def _defineParams(self, form):
            """ Overwrite the standard define params """

            # This should define the inputProtocols and the sampling interval
            ProtMonitor._defineParams(self, form)

            # Remove the inputProtocols
            section = form.getSection('Input')
            section._paramList.remove('inputProtocols')

            # Add a threshold for the email notifier
            form.addParam('minimumFreeSpace', params.IntParam, default=500,
                          label="Minimum free space (GB)",
                          help="Notify by email or console when HD free space"
                               " drops below the minimum")

            self._sendMailParams(form)

        # Overwrite the monitor step function
        def monitorStep(self):

            # Instantiate a Space Monitor
            monitor = SpaceMonitor(self.minimumFreeSpace,
                                   workingDir=self._getExtraPath(),
                                   samplingInterval=self.samplingInterval.get(),
                                   monitorTime=100)

            monitor.addNotifier(PrintNotifier())

            # Create the email notifier
            email = self.createEmailNotifier()

            # If email option active
            if email is not None:
                monitor.addNotifier(email)

            monitor.loop()

We have added the ``_defineParams(self, form)`` method. There we have
called the ``ProtMonitor._defineParams(self, form)`` to have the default
parent params. Next thing is to delete the ``inputProtocols``. This wasn't
expected in our API, but python is flexible enough to make this happen:

.. code-block:: python
    :caption: protocols/space_monitor.py

            # Remove the inputProtocols
            section = form.getSection('Input')
            section._paramList.remove('inputProtocols')

Next thing is to add a ``minimumFreeSpace`` parameter to serve as a
threshold to send email in case free space goes below that threshold.
We also add the email notifications parameters with
``self._sendMailParams(form)``.

Secondly, we have also made some changes in the ``monitorStep()`` method. We
are passing the *minimumFreeSpace* value to the SpaceMonitor:

.. code-block:: python
    :caption: protocols/space_monitor.py

            # Instantiate a Space Monitor
            monitor = SpaceMonitor(self.minimumFreeSpace,
                                   workingDir=self._getExtraPath(),
                                   samplingInterval=self.samplingInterval.get(),
                                   monitorTime=100)

and finally, at the end we have requested for an EmailNotifier and added
it to the Monitor if condition apply. Our protocol looks ok, but our
monitor is not yet aware of the new parameter ``'minimumFreeSpace'`` and
is notifying in any loop.

-  Make SpaceMonitor to understand and react to 'minimumFreeSpace'

.. code-block:: python
    :caption: protocols/space_monitor.py

    class SpaceMonitor(Monitor):
    """
    Monitor to monitor free space on the HD where scipion project is placed
    """

    def __init__(self, minimumFreeSpace, **kwargs):
        Monitor.__init__(self, **kwargs)
        self.minimumFreeSpace = minimumFreeSpace

-  And modify the ``step()`` method of ``SpaceMonitor`` to take the threshold into account

.. code-block:: python
    :caption: protocols/space_monitor.py

       def step(self):
           """ Using the workingdir attribute has to find the HD and then get the
           available free space."""

           usage = disk_usage(self.workingDir)

           self.storeUsageData(usage)

           # Stats line readable:
           free = prettySize(usage.free)
           total = prettySize(usage.total)
           used = prettySize(usage.used)

           # Free space in GB
           freeGB = usage.free/(1024.0**3.0)

           # Notify only if free space is bellow the threshold in GB
           if freeGB < self.minimumFreeSpace:
               self.notify("WARNING: There is only %s left for %s" %
                           (free, self.workingDir),
                           "Free: %s, Total: %s, Used: %s, Threshold: %s" %
                           (free, total, used, self.minimumFreeSpace))

Don't forget the test!!
^^^^^^^^^^^^^^^^^^^^^^^

We haven't touched the monitor test and more important, we are not
testing the protocol.

Our test should be failing because we are not passing the
``minimumFreeSpace``. Let's do that:

* Update Monitor test: Replace (for simplicity) all content in ``test_monitor.py`` with:

.. code-block:: python
    :caption: tests/test_monitor.py

    import math
    from pyworkflow.tests import *
    from myfacility.protocols import SpaceMonitor, ProtMonitorSpace
    from myfacility.protocols.space_monitor import disk_usage
    from tempfile import mkdtemp

    # Test monitor functionality
    class TestMonitor(BaseTest):

        def test_monitor(self):

            # Get a tmp folder
            tmpFolder = mkdtemp()

            # Get freespace
            diskUsage = disk_usage(tmpFolder)
            freeSpaceInGB = diskUsage.free/(1024.0**3)

            # Round it to the "foor"
            freeSpaceInGB = math.floor(freeSpaceInGB)

            # Instantiate the monitor
            spaceMonitor = SpaceMonitor(freeSpaceInGB, workingDir=tmpFolder, stdout=True)
            testNotifier = TestNotifier()
            spaceMonitor.addNotifier(testNotifier)

            spaceMonitor.step()

            # Check storage file exists
            fnStorageFile = spaceMonitor.getStorageFilePath()

            # Check that the file exists
            self.assertTrue(os.path.exists(fnStorageFile),
                            "Storage file %s not created." % fnStorageFile)

            # Check there are 2 lines (headers and first data line)
            num_lines = sum(1 for line in open(fnStorageFile,'r'))

            # Assert lines are 2
            self.assertEqual(2, num_lines,
                             "First step of the monitor does not "
                             "have the expected lines: %s" % 2)

            # Check notifications are empty
            self.assertEqual(0, len(testNotifier.getNotifications()), "Notifications are not empty!")

            # Move the threshold to trigger notifications
            spaceMonitor.minimumFreeSpace = freeSpaceInGB + 1

            spaceMonitor.step()

            # Check there is a notification
            self.assertEqual(1, len(testNotifier.getNotifications()), "There isn't a notification")

    class TestNotifier():
        def __init__(self):
            self._notifications=[]

        def getNotifications(self):
            return self._notifications

        def notify(self, title, message):
            # Just store the message
            self._notifications.append(message)

We have used the ``diskUsage()`` method to get the free space of the HD
of the ``/tmp`` folder. We round it "down" and use that as the threshold for
the SpaceMonitor. After the first step there should not be any
notification. After the first assertions, we add another to check there
are no notifications. Secondly, we increase the threshold by one and
call for a second time ``step()``. This time, there should be a
notification.

Note that we have to make our own ``TestNotifier`` in order to check the
notifications. Something we should provide, but wasn't available in
Scipion today.

Add a test for the protocol monitor.
''''''''''''''''''''''''''''''''''''

We also have to test the protocol. You will need to import
ProtMonitorSpace and a ``wait`` function:

.. code-block:: python

    import math
    from pyworkflow.tests import *
    from pyworkflow.tests.test_utils import wait
    from myfacility.protocols import SpaceMonitor, ProtMonitorSpace
    from myfacility.protocols.space_monitor import disk_usage
    from tempfile import mkdtemp

Now add the code below inside the class ``TestMonitor`` right after
``self.assertEqual(1, len(testNotifier.getNotifications()), "There isn't a notification")``
and right above our custom ``class TestNotifier``

.. code-block:: python

    @classmethod
    def setUpClass(cls):
        setupTestProject(cls)


    def test_spacemonitor_protocol(self):
        prot = self.newProtocol(ProtMonitorSpace,
                                objLabel='HD free Space monitor',
                                samplingInterval=10)

        self.proj.launchProtocol(prot, wait=False)

        # Test that the spaceMonitor txt file is where expected
        spaceMon = SpaceMonitor(10, workingDir=prot._getExtraPath())
        txtPath = spaceMon.getStorageFilePath()

        # Wait for a minute maximum or if file exists
        wait(lambda: not os.path.exists(txtPath), timeout=15)

        self.assertTrue(os.path.exists(txtPath), "Space monitor txt file not "
                                                 "found at %s" % txtPath)

        # Stop the protocol. Do not wait for its timeout
        self.proj.stopProtocol(prot)

With the ``setUpClass()`` we are creating an empty Scipion project

Run the test:
``scipion test myfacility.tests.test_monitor.TestMonitor``.
In the ``test_spacemonitor_protocol`` we are creating one
``ProtMonitorSpace`` and launching it. Since we want to test the
existence of txt file, we make use of a temporary SpaceMonitor to get
the exact txt file at the extra folder of our protocol. We must give
some time to the monitor (15 secs) before checking the file existence,
thus ``wait(lambda: not os.path.exists(txtPath), timeout=15)``. Then, we
make the assertion and stop the protocol...since the only stop mechanism
it has is the default timeout (100 minutes).

You should get something like:

.. code-block:: bash

    ➜  ~ scipion test myfacility.tests.test_monitor.TestMonitor

    Scipion v2.0 (2019-03-15) Diocletian (release-2.0.0 584fbfa)

    >>>>> python  /home/yaiza/git/scipion/pyworkflow/apps/pw_run_tests.py "myfacility.tests.test_monitor.TestMonitor"
    Running tests....
    ('Creating project at: ', '/home/yaiza/ScipionUserData/projects/TestMonitor/project.sqlite')
    WARNING: There is only 185.83 GB left for /tmp/tmptRIM1E Free: 185.83 GB, Total: 217.91 GB, Used: 20.99 GB, Threshold: 186.0
    [ RUN   OK ] TestMonitor.test_monitor (0.001 secs)
    ** Running command: 'python /home/yaiza/git/scipion/scipion runprotocol pw_protocol_run.py "/home/yaiza/ScipionUserData/projects/TestMonitor" "Runs/000002_ProtMonitorSpace/logs/run.db" 2'

    Scipion v2.0 (2019-03-15) Diocletian (release-2.0.0 584fbfa)

    >>>>> python  /home/yaiza/git/scipion/pyworkflow/apps/pw_protocol_run.py "/home/yaiza/ScipionUserData/projects/TestMonitor" "Runs/000002_ProtMonitorSpace/logs/run.db" "2"
    Terminating child pid: 27553
    Terminating child pid: 27555
    Terminating child pid: 27562
    Terminating child pid: 27563
    Terminating process pid: None
    WARNING! Got None PID!!!
    [ RUN   OK ] TestMonitor.test_spacemonitor_protocol (2.304 secs)

    [==========] run 2 tests (3.099 secs)
    [  PASSED  ] 2 tests



