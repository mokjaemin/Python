from typing import Text
from speech_recognition import *
import time
from pyautogui import *
import clipboard
import keyboard
import pyaudio
from gtts import gTTS
import playsound



def jamin_mic():
    recognizer = Recognizer()
    mic = Microphone()

    with mic as source:
        print("무엇을 도와드릴까요? :")
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio, language='ko')
            print(text)

        except:
            print("인식하지 못했어요")

    return text

def speak(text):
    tts = gTTS(text=text, lang='ko')
    filename = 'voice.wav'
    tts.save(filename)
    playsound.playsound(filename)





speak("안녕 재민")
# jamin_mic()



