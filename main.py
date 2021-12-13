#!/usr/bin/python3

from gtts import gTTS
from pygame._sdl2 import get_num_audio_devices, get_audio_device_name
from pygame import mixer
import os

mixer.init(devicename="Null Output")

while True:
	text = input("> ")
	gtts = gTTS(text=text, lang="en", slow=False, tld="co.uk")
	gtts.save("audio.mp3")
	mixer.music.load("audio.mp3")
	mixer.music.play()
	print(f"\n{text}\n")
	# mixer.quit()
	os.system("rm audio.mp3")
  