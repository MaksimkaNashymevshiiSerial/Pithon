import pyttsx3

engine = pyttsx3.init()
# Получаем голоса установленные в системе
voices = engine.getProperty('voices')

#Выводим свойства языков
for voice in voices:
	print('----------------')
	print(f'Имя: {voice.name}')
	print(f'ID: {voice.id}') 
	print(f'Язык(и): {voice.languages}')
	print(f'Пол: {voice.gender}')
	print(f'Возраст: {voice.age}')