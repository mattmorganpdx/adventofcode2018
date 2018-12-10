from unittest import TestCase
from .day09 import day09


class TestDay09(TestCase):
    def test_day09_example(self):
        answer_1 = day09(9, 25)
        self.assertEqual(32, answer_1)
        answer_1 = day09(10, 1618)
        self.assertEqual(8317, answer_1)
        answer_1 = day09(13, 7999)
        self.assertEqual(146373, answer_1)
        answer_1 = day09(17, 1104)
        self.assertEqual(2764, answer_1)
        answer_1 = day09(21, 6111)
        self.assertEqual(54718, answer_1)
        answer_1 = day09(30, 5807)
        self.assertEqual(37305, answer_1)

    def test_day09_input(self):
        answer_1 = day09(404, 71852)
        self.assertEqual(434674, answer_1)
        answer_2 = day09(404, 7185200)
        #137m
        self.assertEqual(3653994575, answer_2)
