numbers = [12, 14, 16, 1, ['Dog', 'Cat'], 3]
fruits =  ['Apple', 'Banana','Orange',numbers,'Grape']
print(numbers)
print(fruits)
print(fruits[1])
print(fruits[0])
print(fruits[3][2])
fruits[0]='Watermelon'
print(fruits)
print(fruits[-1])
print("*" * 16)
for fruit in fruits:
    print(fruit)
l = len(fruits)
for idx in range(l):
    print(idx, '-', fruits[idx])
