numbers2 = []
sum = 0
for idx in range (5):
    numbers2.append(int(input("Введите число: ")))
print(numbers2)

for idx in range (5):
    sum += numbers2[idx]

print("Среднее арифметическое: ", sum / 5)
