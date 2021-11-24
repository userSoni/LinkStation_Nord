import unittest
from device import Device
from linkstation import LinkStation

class TestLinkStation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.station = [
            LinkStation(21, 0, 15),
            LinkStation(25, 0, 10),
            LinkStation(100, 35, 0)
        ]
        

    @classmethod
    def tearDownClass(cls):
        print('\ntearDownClass')

    def setUp(self):
        print('\nsetUp')

    def tearDown(self):
        print('\ntearDown')

    def test_get_ispower(self):
        print('test_ispower')

        device = Device(20, 30)
        self.assertEqual(device.get_ispower(self.station), 0)

    def test_not_get_ispower(self):
        print('test_ispower')

        device = Device(21, 13)
        self.assertEqual(device.get_ispower(self.station), 0)

if __name__ == '__main__':
    unittest.main()