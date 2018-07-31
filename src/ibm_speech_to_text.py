from watson_developer_cloud import SpeechToTextV1
import pprint

speech_to_text = SpeechToTextV1(url="https://stream.watsonplatform.net/speech-to-text/api",
                                username="091ec407-aedf-4d19-8d22-e5f86e25eaae",
                                password="RPqFM0b64WRn")  # security stuff...

with open("resources/sample_ibm_conversion_computer.mp3", 'rb') as audio_file:  # loads the audio files into memory
    speech_recognition_results = speech_to_text.recognize(
        audio=audio_file,
        content_type='audio/mp3',
        timestamps=False,
        word_alternatives_threshold=0.9,
        keywords=['IBM', 'this', 'API'],
        keywords_threshold=0.5)  # using the recognize method to make a request and returns a json with translation
pprint.pprint(speech_recognition_results)
