import unittest
from src.app.common.interval import Interval

class TestInterval(unittest.TestCase):

    def test_initialization(self):
        # Test initialization with default values
        interval = Interval()
        self.assertEqual(interval.start, 0)
        self.assertEqual(interval.end, 0)

    def test_specific_interval(self):
        # Test initialization with specific start and end
        interval = Interval(s=5, e=10)
        self.assertEqual(interval.start, 5)
        self.assertEqual(interval.end, 10)
