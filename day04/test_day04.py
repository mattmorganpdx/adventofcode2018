from unittest import TestCase
from shared.utils import load_input
from .day04 import day04


class TestDay04(TestCase):
    def test_day04_example(self):
        test_array = load_input('day04/example')
        day04_value_1, day04_value_2 = day04(test_array)
        self.assertEqual(240, day04_value_1)
        self.assertEqual(4455, day04_value_2)

    def test_day04_input(self):
        test_array = load_input('day04/input')
        day04_value_1, day04_value_2 = day04(test_array)
        self.assertEqual(84834, day04_value_1)
        self.assertEqual(53427, day04_value_2)
