import unittest
from unittest import mock

from swapi_client import SWAPIClient

# Moved to other file for readability
from test_data import full_api_luke_data

class TestSwapiClient(unittest.TestCase):
    def setUp(self):
        self.client = SWAPIClient()

    def tearDown(self):
        del self.client
    
    def test_get_swapi_data(self):
        # Arrange - Set up expectations and mocks
        expected_data = full_api_luke_data
        self.get_data_called = False
        
        def test_get_data(character_name): # Mock get_data, it is not under test. Also can use unittest.mock
            self.get_data_called = True
            return expected_data
        self.client.get_data = test_get_data

        # Act - Call the function under tests
        data = self.client.get_swapi_data()

        # Assert - Check that it did what we think
        self.assertTrue(self.get_data_called) # Structural Testing, since get_data is outside the scope of our unit
        self.assertEqual(data, expected_data)

    def test_swapi_client_handles_exception(self):
        # This test specs that the function should return an error 
        # object if the call fails, with the message attached
        # If it doesn't handle this case, the test will fail.
        expected_data = {"error": True, "message": "SWAPI Call Failed!"}

        # Example of mocking using the built-in library
        # https://docs.python.org/3/library/unittest.mock.html
        mock_get_data = mock.Mock(side_effect=Exception('SWAPI Call Failed!'))
        self.client.get_data = mock_get_data

        data = self.client.get_swapi_data()

        # Mocks have their own assertions!
        mock_get_data.assert_called_once()
        mock_get_data.assert_called_with("Luke Skywalker")
        self.assertEqual(data, expected_data)