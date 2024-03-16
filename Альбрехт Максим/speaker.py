# pip install pyttsx3
# pip install pypiwin32

import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', 100) # Скорость речи
engine.setProperty('volume', 0.9) # 0-1 Громкость
engine.say('Ahhh, zombie are attacking!')
engine.say('Аааа-аа, Зомби атакуют!')
#очищаем очередь и воспроизводим звук!
engine.runAndWait()