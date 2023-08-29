import googletrans

translator = googletrans.Translator()

str1 = "행복하세요"
result1 = translator.translate(str1, dest='en', src='auto')
print(f"행복하세요 ==> {result1.text}")

str1 = "I am happy"
result1 = translator.translate(str1, dest='ko', src='en')
print(f"I am happy ==> {result1.text}")
