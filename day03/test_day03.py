from unittest import TestCase
from shared.utils import load_input
from .day03 import find_spots


class TestDay03(TestCase):
    def test_day03_input(self):
        test_array = load_input('day03/input')
        day3_value, claim_id = find_spots(test_array)
        self.assertEqual(121259, day3_value)
        self.assertEqual('#239', claim_id)
