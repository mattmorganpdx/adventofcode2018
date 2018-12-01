from unittest import TestCase
from .day01 import calibrate


class TestCalibrate(TestCase):
    def test_calibrate_example(self):
        test_array = ["+1", "- 2", "+ 3", "+ 1"]
        frequency = calibrate(test_array)[0]
        self.assertEqual(3, frequency)

    def test_calibrate_input(self):
        test_array = load_input()
        frequency, first_repeat = calibrate(test_array)
        self.assertEqual(454, frequency)
        self.assertEqual(566, first_repeat)


def load_input():
    lines = list()
    with open('day01/input', "r") as f:
        for line in f.readlines():
            lines.append(line.strip())
    return lines
