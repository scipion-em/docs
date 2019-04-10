
# **************************************************************************
# *
# * Authors:     Yaiza Rancel (yrancel@cnb.csic.es)
# *
# * Unidad de  Bioinformatica of Centro Nacional de Biotecnologia , CSIC
# *
# * This program is free software; you can redistribute it and/or modify
# * it under the terms of the GNU General Public License as published by
# * the Free Software Foundation; either version 2 of the License, or
# * (at your option) any later version.
# *
# * This program is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# * GNU General Public License for more details.
# *
# * You should have received a copy of the GNU General Public License
# * along with this program; if not, write to the Free Software
# * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA
# * 02111-1307  USA
# *
# *  All comments concerning this program package may be sent to the
# *  e-mail address 'scipion@cnb.csic.es'
# *
# **************************************************************************

import math
from pyworkflow.tests import *
from pyworkflow.tests.test_utils import wait
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
        freeSpaceInGB = diskUsage.free / (1024.0 ** 3)

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
        num_lines = sum(1 for line in open(fnStorageFile, 'r'))

        # Assert lines are 2
        self.assertEqual(2, num_lines,
                         "First step of the monitor does not "
                         "have the expected lines: %s" % 2)

        # Check notifications are empty
        self.assertEqual(0, len(testNotifier.getNotifications()), "Notifiactions are not empty!")

        # Move the threshold to trigger notifications
        spaceMonitor.minimumFreeSpace = freeSpaceInGB + 1

        spaceMonitor.step()

        # Check there is a notification
        self.assertEqual(1, len(testNotifier.getNotifications()), "There isn't a notification")

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


class TestNotifier():
    def __init__(self):
        self._notifications = []

    def getNotifications(self):
        return self._notifications

    def notify(self, title, message):
        # Just store the message
        self._notifications.append(message)