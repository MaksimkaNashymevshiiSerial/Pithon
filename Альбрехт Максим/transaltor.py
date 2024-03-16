from tkinter import *
import requests
import pyttsx3

engine = pyttsx3.init()

def translation():
	url = "https://google-translator-unlimited.p.rapidapi.com/translate"
	payload = {
		"texte": "Текст для перевода",
		"to_lang": "ru"
	}
	headers = {
		"content-type": "application/x-www-form-urlencoded",
		"X-RapidAPI-Key": "3b0104cbb9msh5044457194d79c0p17451ejsn8c4b4a9ba415",
		"X-RapidAPI-Host": "google-translator-unlimited.p.rapidapi.com"
	}
		id_engine = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"
	if (rBtn.get() == 1):
		payload['to_lang'] = "en"
		id_engine = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"

	engine.setProperty('voice', id_engine)
	txt = pole.get('0.0', END)
	poleTranslate.delete('1.0', END)
	payload['texte'] = txt
	response = requests.post(url, data=payload, headers=headers)
	a = response.json()
	txt = a['translation_data']['translation']
	poleTranslate.insert('1.0', txt)

root = Tk()
rBtn = IntVar()
root.title("Переводчик")
root.geometry('730x450')
root.resizable(width=False, height=False)

pole = Text(root, width=80, height=10, font='Arial, 13')
pole.pack(pady=10)
alg01 = Radiobutton(root, text='Перевод на Русский Язык',
	variable=rBtn, value=0, font='Artal, 10')
alg01.place(x=50, y=25)
Btn = Button(root, text='Перевести', command=translation)
Btn.pack()
alg02 = Radiobutton(root, text='English translation',
	variable=rBtn, value=1, font='Artal, 12')
alg02.place(x=450, y=205)

poleTranslate = Text(root, width=80, height=10, font='Arial, 13')
poleTranslate.pack(pady=10)

root.mainloop()