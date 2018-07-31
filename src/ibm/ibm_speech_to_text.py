from watson_developer_cloud import SpeechToTextV1
import pprint
import os


speech_to_text = SpeechToTextV1(url="https://stream.watsonplatform.net/speech-to-text/api",
                                username="091ec407-aedf-4d19-8d22-e5f86e25eaae",
                                password="RPqFM0b64WRn")  # security stuff...

files = ("sample_ibm_conversion_computer.mp3", "sample_ibm_conversion_human.mp3")
for file in files:
    with open(os.path.join(os.path.dirname(__file__), "resources/" + file), 'rb') as audio_file:
        speech_recognition_results = speech_to_text.recognize(  # loads the audio file in memory
            audio=audio_file,
            content_type='audio/mp3',
            timestamps=False,
            word_alternatives_threshold=0.9,
            keywords=['IBM', 'this', 'API'],  # key words that it looks out for
            keywords_threshold=0.5)  # using the recognize method to make a request and returns a json with translation
    pprint.pprint(speech_recognition_results)
    print('--------------------------------------------------------')
