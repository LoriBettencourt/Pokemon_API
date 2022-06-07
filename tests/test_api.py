import unittest
import json

from main import app

# Best Practice: Create "tests" subdirectory of project folder to unit test code
class ApiTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    # Check if route returns all results at strings
    def test_api_get(self):
        response = self.app.get('/api/v1/pokemon')
        result = json.loads(response.data)

        self.assertEqual(150, result["count"])
        self.assertEqual(str, type(result["results"][0]['name']))        
        self.assertEqual(200, response.status_code)

if __name__ == '__main__':
    unittest.main()