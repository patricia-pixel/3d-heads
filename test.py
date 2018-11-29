from gtts import gTTS
from io import BytesIO
import random, sys, os, json
import subprocess as sub

keywords = ["love", "life", "death"]

text = raw_input("What type of quote do you want to listen to: ")

parsed = text.split(" ")

for word in parsed:
    if word in keywords:
        print("\n{}\n".format(word))
        with open('{}.json'.format(word)) as json_data:
            d = json.load(json_data)
            print(d)
            continue

tts = gTTS(text=picked, lang='en')
tts.save("temp.mp3")

p = sub.Popen(['mpg321', './temp.mp3'])
output, errors = p.communicate()
