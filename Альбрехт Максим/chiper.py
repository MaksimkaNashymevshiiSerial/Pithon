def form_dict():
	d = {}
	iter = 32
	for i in range(32, 127):
		d[iter] = chr(i)
		iter += 1
	return d
print(form_dict())

def encode_val(word):
	list_code = []
	length = len(word)
	d = form_dict()
	for w in range(length):
		for value in d:
			if word[w] == d[value]:
				list_code.append(value)
		return list_code

print(encode_val("Hello World!!!?"))
print(encode_val("Привет!!!"))
