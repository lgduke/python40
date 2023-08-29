from gtts import gTTS
from playsound import playsound
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

print(__file__)
print(os.path.abspath(__file__))

text = "안녕하세요. 2번 파이썬을 공부하는 중입니다."

tts = gTTS(text=text, lang='ko')
tts.save(r"hi2.mp3")

playsound("hi2.mp3")