from unittest import TestCase
from shared.utils import load_input
from .day05 import day05


class TestDay05(TestCase):
    def test_day05_example(self):
        test_array = load_input('day05/example')
        day05_value_1, day05_value_2 = day05(test_array)
        self.assertEqual(10, day05_value_1)
        self.assertEqual(4, day05_value_2)

    def test_day05_input(self):
        test_array = load_input('day05/input')
        day05_value_1, day05_value_2 = day05(test_array)
        self.assertEqual(11946, day05_value_1)
        self.assertEqual(4240, day05_value_2)
