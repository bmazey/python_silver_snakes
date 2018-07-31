import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration = 1)
    print(r.energy_threshold)
    print("Chucking rate: ", source.CHUNK)
    print("format rate :", source.format)
    print("Say something!...")
    print(r.energy_threshold)
    r.energy_threshold += 280
    audio = r.listen(source)
    print ('say something')

    while True:
        audio = r.listen(source)
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")
            # instead of r.recognize_google(audio)
            print("Google Speech Recognition thinks you said " + r.recognize_google(audio, language='en-GB'))
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))