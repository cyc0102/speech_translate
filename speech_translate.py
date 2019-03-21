import time
import speech_recognition
import tempfile
from gtts import gTTS
from pygame import mixer
def listenTo():
    r = speech_recognition.Recognizer()

    with speech_recognition.Microphone() as source:
        print("Please wait. Calibrating microphone for 3 sec...") 
         #listen for 3 seconds and create the ambient noise energy level 
        r.adjust_for_ambient_noise(source, duration=3)
        print("Say something in Chinese:")
        audio = r.listen(source)

    return r.recognize_google(audio, language='zh-TW')


def speak(sentence, lang):
    mixer.init()
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts = gTTS(text=sentence, lang=lang)
        tts.save("{}.mp3".format(fp.name))
        mixer.music.load('{}.mp3'.format(fp.name))
        mixer.music.play()

from googletrans import Translator
translator = Translator()
# translator.translate('大家好', dest='en').text    
lang = 'en'
#print("Say something in Chinese:")
audio_source= listenTo()

print(audio_source)

result = translator.translate(audio_source, lang).text
print(result)
speak(result, lang) 
time.sleep(7)
