import unittest
from unittest.mock import Mock, patch

from examples.patching import dog


successful_response_mock = Mock()
successful_response_mock.status_code = 200
successful_response_mock.json.return_value = {
    "father": "Hutch",
    "mother": "Daisy"
}


class TestDog(unittest.TestCase):
    # Using patch with full path
    @patch("examples.patching.dog.requests")
    def test_get_profile_patch(self, mock_requests):
        # given
        mock_requests.get.return_value = successful_response_mock
        fluffy = dog.Dog("Fluffy")

        # when
        profile = fluffy.get_profile()

        # then
        self.assertDictEqual(profile, {"father": "Hutch", "mother": "Daisy"})
        mock_requests.get.assert_called_once_with("http://www.dogbook.com/Fluffy")

    # Using patch on an already imported object
    @patch.object(dog, "requests")
    def test_get_profile_patch_object(self, mock_requests):
        # given
        fluffy = dog.Dog("Fluffy")
        mock_requests.get.return_value = successful_response_mock

        # when
        profile = fluffy.get_profile()

        # then
        self.assertDictEqual(profile, {"father": "Hutch", "mother": "Daisy"})
        mock_requests.get.assert_called_once_with("http://www.dogbook.com/Fluffy")

    # Patch as a context manager
    def test_get_profile_patch_context_manager(self):
        # given
        fluffy = dog.Dog("Fluffy")
        with patch.object(dog, "requests") as mock_requests:
            mock_requests.get.return_value = successful_response_mock

            # when
            profile = fluffy.get_profile()

        # then TODO Check why it works out of context
        self.assertDictEqual(profile, {"father": "Hutch", "mother": "Daisy"})
        mock_requests.get.assert_called_once_with("http://www.dogbook.com/Fluffy")


# Manual patch management
class TestDogWithPatcher(unittest.TestCase):
    def setUp(self):
        self.requests_patch = patch.object(dog, "requests")
        self.requests_mock = self.requests_patch.start()
        self.requests_mock.get.return_value = successful_response_mock

    def tearDown(self):
        self.requests_patch.stop()

    def test_get_profile(self):
        # given
        fluffy = dog.Dog("Fluffy")

        # when
        profile = fluffy.get_profile()

        # then
        self.assertDictEqual(profile, {"father": "Hutch", "mother": "Daisy"})
        self.requests_mock.get.assert_called_once_with("http://www.dogbook.com/Fluffy")


# No input argument needed with a pre-configured Mock passed to patch
class TestDogWithMockNoArgument(unittest.TestCase):
    @patch("examples.patching.dog.requests.get", Mock(return_value=successful_response_mock))
    def test_get_profile(self):
        # given
        fluffy = dog.Dog("Fluffy")

        # when
        profile = fluffy.get_profile()

        # then
        self.assertDictEqual(profile, {"father": "Hutch", "mother": "Daisy"})
