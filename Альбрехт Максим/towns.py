import pandas as pd
data = pd.read_csv('city.csv', sep=',')
data = data.dropna(subset=['city'])
a = data['city'].value_counts().to_list
print(a)
towns = data['city'].tolist()
print(towns)
print(len(towns))
print(towns)

rus = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
count = {}
count_end = {}

for symbol in rus:
	count[symbol] = 0
	count_end[symbol] = 0
	for town in towns:
		if symbol.lower() == town[0].lower():
			count[symbol] += 1
		if symbol.lower() == town[len(town) - 1]:
			if symbol.lower() == 'ь':
				count_end[town[len(town) - 2].upper()] += 1
			else:
				count_end[symbol] += 1

print(count)
print("----------------------------------------")
print(count_end)