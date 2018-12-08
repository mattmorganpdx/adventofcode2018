from unittest import TestCase
from shared.utils import load_input
from .day07 import day07


class TestDay07(TestCase):
    def test_day07_example(self):
        test_array = load_input('day07/example')
        answer_1, answer_2 = day07(test_array)
        self.assertEqual('CABDFE', answer_1)
        self.assertEqual(None, answer_2)

    def test_day07_input(self):
        test_array = load_input('day07/input')
        answer_1, answer_2 = day07(test_array)
        self.assertEqual('MNQKRSFWGXPZJCOTVYEBLAHIUD', answer_1)
        self.assertEqual(None, answer_2)
