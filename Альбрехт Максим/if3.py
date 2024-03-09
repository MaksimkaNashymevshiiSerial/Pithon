age = int(input("Введите ваш возраст:"))
if age < 10:
    print("Возраст состоит из одной цифры")
elif age < 18:
    print("Вы школьник")
elif age < 23:
    print("Вы студент")
elif age >= 100:
    print("Вы долгожитель")
elif age >= 65:
    print("Вы пенсионер")
else:
    print("Вы наверное работаете")

    
