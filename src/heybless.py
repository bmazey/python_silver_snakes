import os
from scipy.io import wavfile

print(os.path.dirname(__file__))
file = os.path.join("/Users/alansun/Documents/columbia_summer/silver_snakes/src/ibm/resources/sample_ibm_conversion_computer.wav")
with open(file,'rb') as audio_file:
    print(audio_file.read())