import unittest
import audio_detection.src.short_audio_file.py


class TestName(unittest.TestCase):
    def test_detect_words(self):
        assert audio_detection.src.short_audio_file.transcribe_file('Its over Anakin! I have the high ground!.mp3') == 'Its over Anakin. I have the high ground.'
