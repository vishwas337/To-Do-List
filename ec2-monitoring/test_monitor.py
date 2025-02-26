import unittest
from monitor_ec2 import check_instance_health 

class TestEC2Monitoring(unittest.TestCase):
    def test_health_check(self):
        # Mock response for testing (requires boto3 or mock library, e.g., unittest.mock)
        # This is a placeholder—modify based on real EC2 instance or mock data
        self.assertTrue(check_instance_health('i-0d59564bb36cabe93'))  #  instance ID

if __name__ == "__main__":
    unittest.main()
