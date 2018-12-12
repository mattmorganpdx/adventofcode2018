from unittest import TestCase
from .day11 import get_power_level


class TestGet_power_level(TestCase):
    def test_get_power_level(self):
        self.assertEqual(4, get_power_level((3, 5), sn=8))
        self.assertEqual(-5, get_power_level((122, 79), sn=57))
        self.assertEqual(0, get_power_level((217, 196), sn=39))
        self.assertEqual(4, get_power_level((101, 153), sn=71))

