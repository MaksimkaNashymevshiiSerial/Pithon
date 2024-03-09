a = int(input("Введите сторону a: ")) 
b = int(input("Введите сторону b: ")) 
c = int(input("Введите сторону c: ")) 
 
if a >= b+c or b >= a+c or c >= a+b: 
    print("NO") 
else: 
    print("YES")
