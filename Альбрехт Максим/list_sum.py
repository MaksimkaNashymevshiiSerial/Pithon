a = [10, 9, 8]
b = [*a, 7, 6, 5, 4]
c = [1, 2, 3, *a]
print(b)
print(c)

def sum(*args):
	s = 0
	for item in args:
		s += item
	return s

print(sum(2,6))
print(sum(1, 2, 3, 4, 5, 6, 7, 8, 9))