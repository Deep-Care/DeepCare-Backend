import io
import os

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

def change_speech_to_text(speech_sample):
# Instantiates a client

    client = speech.SpeechClient()

    # The name of the audio file to transcribe
    file_name = os.path.join(os.path.dirname(__file__),'resources', 'audioSad.flac')
    ## file_name = speech_samples

    # Loads the audio into memory
    with io.open(file_name, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)

    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=44100,
        language_code='en-US')

    # Detects speech in the audio file
    response = client.recognize(config, audio)

    text_string = ""

    for result in response.results:
        print('Transcript: {}'.format(result.alternatives[0].transcript))
        text_string = text_string + result.alternatives[0].transcript

    return text_string
