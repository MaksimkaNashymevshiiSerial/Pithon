names = []
for idx in range (5):
    names.append(input("Введите строку: "))
print(names)

str = ''

for idx in range(5):
    if len(str) < len(names[idx]):
        str = names[idx]
print("Самая длинная строка: ", str)
