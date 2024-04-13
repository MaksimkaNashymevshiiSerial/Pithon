import telebot
import random

bot = telebot.TeleBot('7180757450:AAHKF_9iws9kVMj4xGodc1AAXfcKYHu_YW0')
flag = False
secret = 0

@bot.message_handler(content_types=
	['text', 'document', 'audio'])

def get_text_messages(message):
	global flag
	global secret

	print(message)
	body = message.text
	if body == 'Привет':
		bot.send_message(message.from_user.id,
			"Привет!, поиграем? </br> Напиши /help для получения правил!")
	elif body =="/help":
		bot.send_message(message.from_user.id,
			"Для запуска игры напиши /secret_number")
	elif body =="/secret_number":
		flag = "secret_number"
		secret = random.randrange(0, 100)
		bot.send_message(message.from_user.id,
			"Вы выбрали игру: Угадай число! Я загадал число от 0 до 100 ... попробуй угадать!")
	elif flag == "secret_number":
		if  int(body) > secret:
			bot.send_message(message.from_user.id,
				"Ваше число меньше")
		elif int(body) < secret:
			bot.send_message(message.from_user.id,
				"Ваше число больше")
		else:
			bot.send_message(message.from_user.id,
				"Это победа, ты молодец, Пользователь)")

	else:
		bot.send_message(message.from_user.id,
			"Для начала напиши /help")

bot.polling(none_stop=True, interval=0)