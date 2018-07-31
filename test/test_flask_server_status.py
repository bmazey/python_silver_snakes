import unittest
import os
import src.application as speech
import flask


class TestRequestsPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = speech.get_app()
        cls.client = cls.app.test_client()

    def test_response(self):
        r = self.client.get('/hello')
        self.assertEqual(200, r.status_code, msg="Request to hello failed.")
        self.assertEqual({'hello': 'world'}, r.get_json(), msg="Unexpected response.")

    def test_sqlalchemy_audio(self):
        file = 'sample_ibm_conversion_computer.mp3'
        with open(os.path.join(os.path.dirname(__file__), "/ibm/resources/"+file), 'rb') as audio_file:
            aud = speech.Audio(filename=file, data=audio_file)
            speech.db.session.add(aud)
            speech.db.session.commit()


