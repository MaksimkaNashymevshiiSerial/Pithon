numbers = []
from random import randint

for idx in range (20):
    numbers.append(randint(15,30))
    print(numbers)
sum = 0
for idx in range (20):
    sum += numbers[idx]
print(numbers)
print("Среднее арифметическое: ", sum / 20)
