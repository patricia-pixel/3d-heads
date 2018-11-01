from gtts import gTTS
from io import BytesIO
import random
import sys
import os

love_list = ["Love is that condition in which the happiness of another person is essential to your own."
"Being deeply loved by someone gives you strength, while loving someone deeply gives you courage.",
"Love is like a spice. It can sweeten your life - however, it can spoil it, too.",
"Your task is not to seek for love, but merely to seek and find all the barriers within yourself that you have built against it.",
"There is always some madness in love. But there is also always some reason in the madness"]
print(random.choice(love_list))

mp3_fp = BytesIO()
line = 1
for sentence in life_list:

    tts = gTTS(text=sentence, lang='en')
    tts.save("love-{}.mp3".format(line))
    line+=1
