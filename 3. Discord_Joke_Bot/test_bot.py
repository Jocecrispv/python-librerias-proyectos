import unittest
from unittest.mock import patch
from api import obtener_chiste  # Import the function we want to test

# Define a test case class that inherits from unittest.TestCase
class TestAPI(unittest.TestCase):

    @patch('api.requests.get')
    def test_chiste_espanol_una_parte(self, mock_get):
        """
        Test case: Spanish joke (single-part).
        We mock the API response to simulate a joke with only one part.
        """
        # Simulate a successful API response (status 200)
        mock_get.return_value.status_code = 200
        
        # Simulate the JSON returned by the API (single joke)
        mock_get.return_value.json.return_value = {
            "type": "single",
            "joke": "¿Qué le dice un .GIF a un .JPEG? Anímate viejo."
        }

        # Call the function under test
        chiste = obtener_chiste("es")

        # Assert that the function returns the expected joke
        self.assertEqual(chiste["joke"], "¿Qué le dice un .GIF a un .JPEG? Anímate viejo.")

    @patch('api.requests.get')
    def test_chiste_ingles_dos_partes(self, mock_get):
        """
        Test case: English joke (two-part).
        We mock the API response to simulate a joke with setup + delivery.
        """
        # Simulate a successful API response (status 200)
        mock_get.return_value.status_code = 200

        # Simulate the JSON returned by the API (two-part joke)
        mock_get.return_value.json.return_value = {
            "type": "twopart",
            "setup": "What do you call a group of 8 Hobbits?",
            "delivery": "A Hobbyte."
        }

        # Call the function under test
        chiste = obtener_chiste("en")

        # Assert that the function returns both setup and delivery correctly
        self.assertEqual(chiste["setup"], "What do you call a group of 8 Hobbits?")
        self.assertEqual(chiste["delivery"], "A Hobbyte.")

# This allows running the tests directly from the command line:
# python -m unittest test_file.py
if __name__ == '__main__':
    unittest.main()
