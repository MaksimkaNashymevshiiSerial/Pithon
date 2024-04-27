import pandas as pd

data = pd.read_csv('city.csv', sep=',')
towns = data['city'].tolist()
towns = list(set(towns))
rus = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
for symbol in rus:
	print(symbol)
	count = 0
	for town in towns:
		if symbol == town[0].lower:
			count += 1
	print(count)