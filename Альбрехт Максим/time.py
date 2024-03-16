from datetime import datetime, date, time
import pyttsx3
import time

ru_voice = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"
engine = pyttsx3.init()
engine.setProperty('voice', ru_voice)

def say_time(msg):
	engine.say(msg)
	engine.runAndWait()

while True:
	time_checker = datetime.now()
	if time_checker.second == 0:
		say_time(f'Сыктыкарское время {time_checker.hour} часов {time_checker.minute}')
		