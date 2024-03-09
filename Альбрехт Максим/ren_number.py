from random import randint
k = randint(1,10)
count = 1
n = int(input("Твоё число:"))
while n !=k:
    print("Не угадал!")
    n = int(input("Твоё число:"))
    count +=1
print("Молодец, угадал за попыток:", count)
