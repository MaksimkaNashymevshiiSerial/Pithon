a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))

if a < b < c:
    print("Меньшее число: a")
elif b < a < c:
    print("Меньшее число: b")
elif c < a < b:
    print("Меньшее число: c")
else:
    print("Они равны")
    
