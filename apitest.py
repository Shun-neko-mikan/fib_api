import unittest
import json
from api import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_fibonacci_1(self):
        response = self.app.get('/fib?n=10')
        data = json.loads(response.data)
        self.assertEqual(data['result'], 55)

    def test_fibonacci_2(self):
        response = self.app.get('/fib?n=99')
        data = json.loads(response.data)
        self.assertEqual(data['result'], 218922995834555169026)
    
    def test_bad_request(self):
        response = self.app.get('/fib?n=abc')
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()