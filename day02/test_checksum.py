from unittest import TestCase
from shared.utils import load_input
from .day02 import checksum


class TestChecksum(TestCase):
    def test_checksum_example(self):
        test_array = [
            "abcdef",
            "bababc",
            "abbcde",
            "abcccd",
            "aabcdd",
            "abcdee",
            "ababab"]
        checksum_value, common_letters = checksum(test_array)
        self.assertEqual(12, checksum_value)
        self.assertEqual(None, common_letters)

    def test_checksum_input(self):
        test_array = load_input('day02/input')
        checksum_value, common_letters = checksum(test_array)
        self.assertEqual(7192, checksum_value)
        self.assertEqual(list('mbruvapghxlzycbhmfqjonsie'), common_letters)

