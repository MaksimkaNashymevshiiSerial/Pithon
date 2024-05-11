import telebot
import random
import pandas as pd

data = pd.read_csv('city.csv', sep=',')
data = data.dropna(subset=['city'])
towns = data['city'].tolist()
towns = list(set(towns))
user_town = []
my_towns = []
cur_town = '@'
last_letter = ''
error_count = 0

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
	global towns
	global my_towns
	global cur_town
	global last_letter
	global error_count

	print(message)
	body = message.text
	if body == 'Привет':
		bot.send_message(message.from_user.id,
			"Привет!, поиграем? </br> Напиши /help для получения правил!")
	elif body =="/help":
		bot.send_message(message.from_user.id,
			"Для запуска игры напиши /secret_number"
			"\n Для запуска генератора паролей /passwd"
			"\n Для запуска игры города /city")
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
			flag = False
	elif body =="/city":
		bot.send_message(message.from_user.id,
			"Привет!, давай сыграем в города России!"
			 "\n Называем города на последнюю букву предыдущего города"
			 "\n Можешь начинать!"
			 "\n Если не знаешь города, скажи: Сдаюсь")
		flag = "city"
		error_count = 0
		my_towns = []
	elif flag == 'city':
		find_town = False
		if body == 'Сдаюсь':
			flag = False
			bot.send_message(message.from_user.id,
			"Жаль, а я еще знаю города...")
		elif (body not in towns):
			bot.send_message(message.from_user.id,
			"Не надо обманывать меня! Такого города нет!")
			error_count += 1
		elif (body not in my_towns and
			 body[0].lower() == last_letter.lower() or cur_town == '@'):
			if body[-1].lower() == 'ь':
				last_letter = body[-2].lower()
			elif body[-1].lower() == 'й' or body[-1].lower() == 'ы':
				last_letter = 'и'
			else:
				last_letter = body[-1].lower()

			my_towns.append(body)
			towns.remove(body)
			for town in towns:
				if town[0].lower() == last_letter: 
					find_town = True
					bot.send_message(message.from_user.id, town)
					if town[-1].lower() == 'ь':
						last_letter = town[-2].lower()
					elif town[-1].lower() == 'ы' or town[-1].lower() == 'й':
						last_letter == 'и'
					else:
						last_letter = town[-1].lower()
					bot.send_message(message.from_user.id, "Тебе город на букву: " +
						 last_letter.upper())
					i = 0
					for town in towns:
						if last_letter == town[0].lower():
							i += 1
					bot.send_message(message.from_user.id, "Я знаю еще: " + str(i) +
							" городов на букву " + last_letter + "!")
					if i == 0:
						bot.send_message(message.from_user.id, "Ты проиграл, городов на букву: " +
							last_letter + " больше нет")
						bot.send_message(message.from_user.id, "Ты допустил: " +
							str(error_count) + " ошибок")
						flag = False
						bot.send_message(message.from_user.id, "Для начала напиши /help")
					cur_town = town
					my_towns.append(town)
					towns.remove(town)
					break
		else:
			bot.send_message(message.from_user.id, "Играешь не по правилам! Тебе на: " + last_letter.upper())
			error_count += 1
			bot.send_message(message.from_user.id, "Ты допустил: " + str(error_count) +
				" ошибок")
		if body =='/exit':
			flag = False
			bot.send_message(message.from_user.id, "Для начала напиши /help")
	else:
		bot.send_message(message.from_user.id,
			"Для начала напиши /help")

bot.polling(none_stop=True, interval=0)