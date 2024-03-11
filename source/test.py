import unittest
from flask import Flask
from hello import app 

class APITestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = app
        self.app.testing = True 
        self.client = self.app.test_client() 

    def test_hello(self):
        response = self.client.get('/hi')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Привет')
        
    def test_goodbye(self):
        response = self.client.get('/bye')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Пока')

if __name__ == "__main__":
    unittest.main()