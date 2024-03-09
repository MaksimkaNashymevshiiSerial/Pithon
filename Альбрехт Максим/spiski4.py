names = ['Ivan', 'Alex', 'Petr', 'Max']
print(names)

names.insert(0, 'Olga')
print(names)

names.insert(10, 'Maria')
print(names)

names.insert(9, 'Elena')
print(names)

names.remove(4, 'Olga')
print(names)

names.remove('Olga')
print(names)

names.sort()
print(names)

names.sort(reverse=True)
print(names)
