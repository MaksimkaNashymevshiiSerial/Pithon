numbers = [12, 14, 16, 1, 6, 3, 335, 23, 12, 13, 124, 13]
print(numbers)
for idx in range(0, len(numbers),2):
    print(idx, ':', numbers[idx])
    
for idx in range(1, len(numbers),2):
    print(idx, ':', numbers[idx])

N = int(input('Введите число N: '))
M = int(input('Введите число M: '))
numbers2 = []
if N % 2 == 1:
    N += 1
for idx in range (N, M + 1, 2):
    numbers2.append(idx)
print(numbers2)

