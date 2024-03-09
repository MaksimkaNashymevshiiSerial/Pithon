# Создать скрипт просит ввести 5 чисел и добавить их в список
print('Введите 5 чисел')
numbers = []
for i in range(5):
    a = int(input('Введите целое число: '))
    numbers.append(a)
print(numbers)
