import unittest
from src.application import get_app
import flask


class TestRequestsPage(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.app = get_app()
        self.client = self.app.test_client()

    def test_response(self):
        r = self.client.get('/hello')
        self.assertEqual(200, r.status_code)


