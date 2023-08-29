from gtts import gTTS
from playsound import playsound
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

print(__file__)
print(os.path.abspath(__file__))

file_path="mytext.txt"

try:
    with open(file_path, 'rt', encoding="UTF8") as f :
        read_file = f.read()
        

    tts = gTTS(text=read_file, lang='ko')
    tts.save(r"mytext.mp3")

    playsound("mytext.mp3")
except FileNotFoundError:
    print("FileNotFoundError occured")