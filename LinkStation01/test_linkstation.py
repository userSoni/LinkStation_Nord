import unittest
from linkstation import LinkStation
from point import Point

class TestLinkStation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.station = LinkStation(0, 15, 25)
        cls.point = Point(10, 20)

    @classmethod
    def tearDownClass(cls):
        print('\ntearDownClass')

    def setUp(self):
        print('\nsetUp')

    def tearDown(self):
        print('\ntearDown')

    def test_get_power(self):
        print('test_get_power')

        self.assertEqual(self.station.get_power(self.point), 0)

if __name__ == '__main__':
    unittest.main()