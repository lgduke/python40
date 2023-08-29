from gtts import gTTS
text = "안녕하세요. 파이썬을 공부하는 중입니다."

tts = gTTS(text=text, lang='ko')
tts.save(r"P03_Txt-to-voice/hi.mp3")