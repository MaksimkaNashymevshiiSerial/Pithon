import telebot
import random

bot = telebot.TeleBot('7180757450:AAHKF_9iws9kVMj4xGodc1AAXfcKYHu_YW0')
flag = False
secret = 0
count = 0

def random_symbol(st, count):
	res = ''
	for i in range(count):
		res = res + random.choice(list(st))
	return res

@bot.message_handler(content_types=
	['text', 'document', 'audio'])

def get_text_messages(message):
	global flag
	global secret
	global count

	print(message)
	body = message.text
	if body == 'Привет':
		bot.send_message(message.from_user.id,
			"Привет!, поиграем? </br> Напиши /help для получения правил!")
	elif body =="/help":
		bot.send_message(message.from_user.id,
			"Для запуска игры напиши /secret_number"
			"\n Для запуска генератора паролей /passwd")
	elif body =="/secret_number":
		flag = "secret_number"
		count = 0
		secret = random.randrange(0, 100)
		bot.send_message(message.from_user.id,
			"Вы выбрали игру: Угадай число! Я загадал число от 0 до 100 ... попробуй угадать!")
	elif body =="/passwd":
		lowercase = 'qwertyuiopasdfghjklzxcvbnm'
		digit = '1234567890'
		uppercase = 'QWERTYUIOPASDFGHJKLZXCVBNM'
		lowercase_count = 4
		digit_count = 2
		uppercase_count = 3
		punctuation = '!@#$%^&*()_+"№;%:?*='
		punctuation_count = 2
		passwd = random_symbol(lowercase, lowercase_count)
		passwd = passwd + random_symbol(digit, digit_count)
		passwd = passwd + random_symbol(uppercase, uppercase_count)
		passwd = passwd + random_symbol(punctuation, punctuation_count)
		l = list(passwd)
		random.shuffle(l)
		passwd = ''.join(l)
		bot.send_message(message.from_user.id, passwd)

	elif flag == "secret_number":
		count += 1
		if  int(body) > secret:
			bot.send_message(message.from_user.id,
				"Ваше число меньше, Попыток: " + str(count))
		elif int(body) < secret:
			bot.send_message(message.from_user.id,
				"Ваше число больше, Попыток: " + str(count))
		else:
			bot.send_message(message.from_user.id,
				"Это победа, ты молодец, Пользователь), Попыток: " + str(count))

	else:
		bot.send_message(message.from_user.id,
			"Для начала напиши /help")

bot.polling(none_stop=True, interval=0)