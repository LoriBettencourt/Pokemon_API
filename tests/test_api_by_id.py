import unittest
import json

from main import app

# Best Practice: Create "tests" subdirectory of project folder to unit test code
class ApiTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    # Check if ID specific route returns the correct Pokemon name, as a string, without error
    def test_api_get(self):
        route_by_id = '/api/v1/pokemon/3'
        response = self.app.get(route_by_id)
        result = json.loads(response.data)

        self.assertEqual(str, type(result['name'])) 
        self.assertEqual("venusaur", result["name"])       
        self.assertEqual(200, response.status_code)

if __name__ == '__main__':
    unittest.main()
        
