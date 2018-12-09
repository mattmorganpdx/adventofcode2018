from unittest import TestCase
from shared.utils import load_input
from .day08 import day08


class TestDay08(TestCase):
    def test_day08_example(self):
        test_array = load_input('day08/example')
        answer_1, answer_2 = day08(test_array)
        self.assertEqual(138, answer_1)
        self.assertEqual(66, answer_2)

    def test_day08_input(self):
        test_array = load_input('day08/input')
        answer_1, answer_2 = day08(test_array)
        self.assertEqual(40036, answer_1)
        self.assertEqual(21677, answer_2)
