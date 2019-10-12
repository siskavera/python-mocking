import unittest
from unittest.mock import Mock


from examples.patching import dog

# First configure our mock
successful_response_mock = Mock()
successful_response_mock.status_code = 200
successful_response_mock.json.return_value = {
    "father": "Hutch",
    "mother": "Daisy"
}

get_mock = Mock(return_value=successful_response_mock)

# Monkey patch to replace requests in the module with our mock
dog.requests.get = get_mock


class TestDog(unittest.TestCase):
    def test_bark(self):
        fluffy = dog.Dog("Fluffy")

        self.assertEqual(fluffy.bark(), "Woof!")

    def test_get_pedigree(self):
        # given
        fluffy = dog.Dog("Fluffy")

        # when
        pedigree = fluffy.get_pedigree()

        # then
        self.assertDictEqual(pedigree, {"father": "Hutch", "mother": "Daisy"})
        get_mock.assert_called_once_with("http://www.dog-pedigree.com/Fluffy")
