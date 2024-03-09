def list_action(a,b,z):
    if len(a)!= len(b):
        return False
    c = a
    if z == "*":
        for idx in range(len(a)):
            c[idx] = a[idx] * b[idx]
    elif z == "+":
        for idx in range(len(a)):
            c[idx] = a[idx] + b[idx]
    elif z == "-":
        for idx in range(len(a)):
            c[idx] = a[idx] - b[idx]
    elif z == "/":
        for idx in range(len(a)):
            if b[idx] == 0:
                c[idx] == math.inf
            else:
                c[idx] = a[idx] / b[idx]
    else:
        return False
    
    return c
        

print(list_action([4, 8, 6],[2,0,2],"/"))
