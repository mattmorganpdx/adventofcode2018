from unittest import TestCase
from shared.utils import load_input
from .day12 import day12


class TestDay12(TestCase):
    def test_day12_example(self):
        test_data = load_input('day12/example')
        answer_1, answer_2 = day12(test_data)
        self.assertEqual(325, answer_1)

    def test_day12_input(self):
        test_data = load_input('day12/input')
        answer_1, answer_2 = day12(test_data)
        # 2658 too low
        self.assertEqual(3230, answer_1)
        #self.assertEqual(None, answer_2)
