import src.tricks as tricks
import unittest

class TestLearnFunction(unittest.TestCase):
    # Tricks test cases start here
    def test_coerce_with_valid_input(self):
        result = tricks.coerce("42")
        self.assertEqual(result, 42)

    def test_coerce_with_invalid_input(self):
        result = tricks.coerce("invalid")
        self.assertEqual(result, "invalid")

    @unittest.mock.patch('builtins.open', unittest.mock.mock_open(read_data='1,2,3\n4,5,6\n'))
    def test_csv_parser(self):
        result = list(tricks.csv(file="example.csv"))
        expected_output = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(result, expected_output)
    # Tricks test cases end here