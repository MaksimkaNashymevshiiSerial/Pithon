m = int (input("Введите месяц: "))

if m < 3:
    print("Зима")
elif m < 6:
    print("Весна")
elif m < 9:
    print("Лето")
elif m < 11:
    print("Осень")
elif m < 13:
    print ("Зима")
else:
    print("Нет такого месяца!")
