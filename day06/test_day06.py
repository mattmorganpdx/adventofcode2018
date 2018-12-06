from unittest import TestCase
from shared.utils import load_input
from .day06 import day06


class TestDay06(TestCase):
    def test_day06_example(self):
        test_array = load_input('day06/example')
        answer_1, answer_2 = day06(test_array, 32)
        self.assertEqual(17, answer_1)
        self.assertEqual(16, answer_2)

    def test_day06_input(self):
        test_array = load_input('day06/input')
        answer_1, answer_2 = day06(test_array, region_size=10000)
        self.assertEqual(4171, answer_1)
        self.assertEqual(39545, answer_2)

