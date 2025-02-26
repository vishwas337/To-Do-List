import unittest
from monitor_ec2 import check_instance_health  # Adjust import based on your script

class TestEC2Monitoring(unittest.TestCase):
    def test_health_check(self):
        # Mock response for testing (requires boto3 or mock library, e.g., unittest.mock)
        # This is a placeholder—modify based on real EC2 instance or mock data
        self.assertTrue(check_instance_health('i-09b1b6b9e3abe88c2'))  #  instance ID

if __name__ == "__main__":
    unittest.main()
