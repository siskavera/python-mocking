import unittest
from unittest.mock import patch

from examples.pitfalls.weekday import is_weekday


class TestIsWeekday(unittest.TestCase):
    @patch("examples.pitfalls.weekday.is_weekday", return_value=False)
    def test_is_weekday(self, _):
        self.assertFalse(is_weekday())
