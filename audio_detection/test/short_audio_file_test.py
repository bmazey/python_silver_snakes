import unittest
from audio_detection.src.short_audio_file import transcribe_file


class Test(unittest.TestCase):
    def test_detect_words(self):
        with open(r'C:\Users\zande\PycharmProjects\python_silver_snakes\audio_files\anakin.mp3', 'rb') as audio_file:
            assert transcribe_file(audio_file) == 'Its over Anakin. I have the high ground.'
