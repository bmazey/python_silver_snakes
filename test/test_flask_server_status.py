import unittest
from src.application import get_app
import flask


class TestRequestsPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = get_app()
        cls.client = cls.app.test_client()

    def test_response(self):
        r = self.client.get('/hello')
        self.assertEqual(200, r.status_code, msg="Request to hello failed.")
        self.assertEqual({'hello': 'world'}, r.get_json(), msg="Unexpected response.")

    def test_sqlalchemy_audio(self):
        pass

