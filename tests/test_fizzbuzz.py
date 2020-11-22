import unittest
from src.fizzbuzz import fizzbuzz_1_to_number, fizzbuzz


class TestFizzBuzz(unittest.TestCase):

    def test_boundaries(self):
        # fizzbuzz_1_to_number takes an input which is greater than 0
        output = fizzbuzz_1_to_number(0)
        self.assertEqual(len(output), 0, msg="Length of output is 0 if input is 0")

        output = fizzbuzz_1_to_number(-1)
        self.assertEqual(len(output), 0, msg="Length of output is 0 if input is negative")

    def test_len_input_matches_len_output(self):
        input_number = 10
        output = fizzbuzz_1_to_number(input_number)

        self.assertEqual(len(output), input_number, msg="Length of output is equal to input number")

    def test_single_number(self):
        test_cases = [
            (1, "1"),
            (3, "fizz"),
            (5, "buzz"),
            (15, "fizzbuzz"),
        ]

        for input_number, expected_output in test_cases:
            output = fizzbuzz(input_number)
            self.assertEqual(expected_output, output, msg="fizzbuzz give good result for 1, 3, 5, 15")