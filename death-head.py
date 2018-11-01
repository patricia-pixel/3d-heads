from gtts import gTTS
from io import BytesIO
import random
import sys
import os

death_list = ["Why should I fear death? If I am, death is not. If death is, I am not. Why should I fear that which cannot exist when I do?"
"As I have not worried to be born, I do not worry to die.", "I do not fear death. I had been dead for billions and billions of years before I was born, and had not suffered the slightest inconvenience from it.",
"I feel monotony and death to be almost the same.", "The boundaries which divide Life from Death are at best shadowy and vague. Who shall say where the one ends, and where the other begins?"]
print(random.choice(death_list))

mp3_fp = BytesIO()
line = 1
for sentence in life_list:

    tts = gTTS(text=sentence, lang='en')
    tts.save("death-{}.mp3".format(line))
    line+=1
