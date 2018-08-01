import speech_recognition as sr

def audio_to_text():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print(r.energy_threshold)
        print("Chucking rate: ", source.CHUNK)
        print("format rate :", source.format)
        print("Say something!...")
        audio = r.listen(source)
        print('say something')

        while True:
            audio = r.listen(source)
            try:
                string = r.recognize_google(audio, language='en-GB')
                return string
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
                exit()