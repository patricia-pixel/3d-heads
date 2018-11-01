from gtts import gTTS
from io import BytesIO
import random
import sys
import os

life_list = ["life is not a problem to be solved but a reality to be experienced","life has no remote. Get up and change it yourself",
"Life contains but two tragedies. One is not to get your heart’s desire; the other is to get it.",
"To live is the rarest thing in the world. Most people exist, that is all.", "The unexamined life is not worth living"]
print(random.choice(life_list))

mp3_fp = BytesIO()
line = 1
for sentence in life_list:

    tts = gTTS(text=sentence, lang='en')
    tts.save("life-{}.mp3".format(line))
    line+=1
