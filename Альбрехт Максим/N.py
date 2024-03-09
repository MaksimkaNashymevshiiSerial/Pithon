# числа от 0 до n
n = int(input('Введите n:'))
k = int(input('Введите k:'))
#for a in range(n+1):
#   print(a)
sum = 0
# Сумма чисел от n до k
for a in range(n, k+1):
    sum +=a
    print("Промежуточный результат +", a ,":" , sum)
print('Итого:',sum)

