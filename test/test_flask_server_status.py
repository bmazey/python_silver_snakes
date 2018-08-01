import unittest
import wave
import os
import src.application as speech
import flask
import os


class TestRequestsPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = speech.get_app()
        cls.client = cls.app.test_client()
        cls.db = speech.get_db()

    def test_response(self):
        r = self.client.get('/audio')
        self.assertEqual(200, r.status_code, msg="Request to hello failed.")
        self.assertEqual({'hello': 'world'}, r.get_json(), msg="Unexpected response.")

    def test_sqlalchemy_audio(self):
        file = "/Users/alansun/Documents/columbia_summer/silver_snakes/src/ibm/resources/sample_ibm_conversion_computer.wav"
        with open(file, 'rb') as audio_file:
            aud = speech.Audio(data=audio_file.read())
            self.db.session.add(aud)
            self.db.session.commit()




