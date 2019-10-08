import unittest
from unittest.mock import patch, Mock

from examples.pitfalls.weekday import greet_if_weekday


successful_response_mock = Mock()
successful_response_mock.status_code = 200
successful_response_mock.json.return_value = {
    "greeting": "Have a great day at work!",
}


# Arguments are ordered backwards
@patch("examples.pitfalls.weekday.is_weekday")
@patch("examples.pitfalls.weekday.requests.get")
class TestGreeting(unittest.TestCase):

    def test_weekday(self, requests_get_mock, is_weekday_mock):
        requests_get_mock.return_value = successful_response_mock
        is_weekday_mock.return_value = True

        self.assertEqual("Have a great day at work!", greet_if_weekday())
