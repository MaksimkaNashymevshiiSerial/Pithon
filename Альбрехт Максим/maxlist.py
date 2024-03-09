import random

def findMax(lst):
    maxx = lst[0]
    for item in lst:
        if maxx < item:
            maxx = item
    return maxx

def makeList(n):
    lst = []
    for i in range(n):
        lst.append(random.randint(1,100))
    return lst
l = makeList(10)
print(l)
m = findMax(l)
print(m)
        
