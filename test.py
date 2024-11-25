#add in functions from other file in directory with import

import unittest
from cpuUsage import cpuUsage, memUsage, disk_Usage, bandwidth_Usage

#yt test case class as param

class TestCases(unittest.TestCase):
    def test_cpuUsage(self):

        result = cpuUsage()
        self.assertIn("CurrentCPU_Usage", result.json) 
        self.assertIn("CPUStatus", result.json)

    def test_memUsage(self):

        result = memUsage()
        self.assertIn("TotalMemory", result.json)
        self.assertIn("MemoryUsagePercentage", result.json)

    def test_disk_Usage(self):
        result = disk_Usage()
        self.assertIn("TotalDiskSpace", result.json)
        self.assertIn("DiskUsagePercentage", result.json)

    def test_bandwidth_Usage(self):
        result = bandwidth_Usage()
        self.assertIn("TotalBandwidthUsed", result.json)

if __name__ == "__main__":
    unittest.main()

