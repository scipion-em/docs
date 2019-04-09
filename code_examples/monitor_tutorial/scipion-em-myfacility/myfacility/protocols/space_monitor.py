import os
import collections

from pyworkflow.em.protocol.monitors import Monitor
from pyworkflow.utils import prettySize

class SpaceMonitor(Monitor):
    """
    Monitor to monitor free space on the HD where scipion project is placed
    """

    def __init__(self, minimumFreeSpace, **kwargs):
        Monitor.__init__(self, **kwargs)
        self.minimumFreeSpace = minimumFreeSpace

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
        freeGB = usage.free / (1024.0 ** 3.0)

        # Notify only if free space is bellow the threshold in GB
        if freeGB < self.minimumFreeSpace:
            self.notify("WARNING: There is only %s left for %s" %
                        (free, self.workingDir),
                        "Free: %s, Total: %s, Used: %s, Threshold: %s" %
                        (free, total, used, self.minimumFreeSpace))


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


from pyworkflow.em import ProtMonitor, PrintNotifier, params
from pyworkflow import VERSION_2_0

class ProtMonitorSpace(ProtMonitor):

    _label = 'monitor of HD space'
    _lastUpdateVersion = VERSION_2_0

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

# Taken from http://code.activestate.com/recipes/577972-disk-usage/
def disk_usage(path):
    _ntuple_diskusage = collections.namedtuple('usage', 'total used free')

    st = os.statvfs(path)
    free = st.f_bavail * st.f_frsize
    total = st.f_blocks * st.f_frsize
    used = (st.f_blocks - st.f_bfree) * st.f_frsize
    return _ntuple_diskusage(total, used, free)
