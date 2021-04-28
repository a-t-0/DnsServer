import unittest
import numpy as np
from src import main


class TestMain(unittest.TestCase):
    """Object used to test the asking user when to train."""

    def __init__(self, *args, **kwargs):
        """Initialises the test class."""
        super().__init__(*args, **kwargs)

    def test_add_two(self):
        actual_result = main.add_two(3)
        expected_result = 5
        self.assertEqual(expected_result, actual_result)
