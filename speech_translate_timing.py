import time
import speech_recognition
import tempfile
from gtts import gTTS
from pygame import mixer
def listenTo():
    r = speech_recognition.Recognizer()

    with speech_recognition.Microphone() as source:
        # print("Please wait. Calibrating microphone for 3 sec...") 
        # listen for 3 seconds and create the ambient noise energy level 
        # r.adjust_for_ambient_noise(source, duration=1)
        r.adjust_for_ambient_noise(source)
        print("Say something in Chinese:")
        audio = r.listen(source)
    try:
        return r.recognize_google(audio, language='zh-TW')
    except speech_recognition.UnknownValueError:
        print("Google Speech Recognition not understand audio") 
        return "沒有聽到聲音"  
    except speech_recognition.RequestError as e:
        print("No response from Google Speech Recognition service: {0}".format(e))
        return "跳出程式"


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
while True:
    audio_source= listenTo()

    print(audio_source)
    if (audio_source == '跳出程式'):  # speak"跳出程式" to exit the program
        break
    result = translator.translate(audio_source, lang).text
    print(result)
    speak(result, lang) 
    str_leng =len(result)
    # print('str_leng=',str_leng)
    delay_sec= str_leng // 10
    time.sleep(delay_sec)
    
