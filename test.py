#add in functions from other file in directory with import

import unittest
from cpuUsage import application, cpuUsage, memUsage, disk_Usage, bandwidth_Usage

class TestCases(unittest.TestCase):
    
    #necessary b4 each test case

    def setUp(self):
        self.app = application
        self.app_context = self.app.app_context()
        self.app_context.push()


    # after each test case this was good practice to clean up 
    def tearDown(self):
        self.app_context.pop()

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

