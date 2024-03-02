def form_dict():
	d = {}
	iter = 32
	for i in range(32, 127):
		d[iter] = chr(i)
		iter += 1
	return d
#print(form_dict())

def encode_val(word):
	list_code = []
	length = len(word)
	d = form_dict()
	for w in range(length):
		for value in d:
			if word[w] == d[value]:
				list_code.append(value)
	return list_code

#print(encode_val("Hello World!!!?"))
#print(encode_val("Привет!!!"))

def comparator(value, key):
	len_key = len(key)
	dic = {}
	iter = 0
	full = 0

	for i in value:
		dic[full]= [i, key[iter]]
		full += 1
		iter +=1
		if (iter >= len_key):
			iter = 0
	return dic
#print(comparator("Hello word!!!", "key"))
# Hello word!!!
# keykeykeykeyk

def full_encode(value, key):
	dic = comparator(value, key)
	lis = []
	d = form_dict()

	for v in dic:
		go = (dic[v][0] + dic[v][1]) % len(d)
		lis.append(go)
	return lis
#print(full_encode(encode_val("Hello word!!!"),
	#encode_val("key")))

def full_decode(value, key):
	dic = comparator(value, key)
	lis = []
	d = form_dict()

	for v in dic:
		go = (dic[v][0] - dic[v][1] + len(d)) % len (d)
		lis.append(go)
	return lis

def decode_val(list_in):
	list_code = []
	len_list = len(list_in)
	d = form_dict()
	for i in range(len_list):
		for value in d:
			if list_in[i] == value:
				list_code.append(d[value])
	return list_code
print(decode_val(full_encode(encode_val("Hello Word!"),
	encode_val("key"))))

word = "Hello Word!!!"
key = "1234"
print("Слово: ", word)
print("Ключ: ", key)
key_encoded = encode_val(key)
value_encoded = encode_val(word)

print("Слово: ", value_encoded)
print("key: ", key_encoded)

shifre = full_encode(value_encoded, key_encoded)
print("Шифр:", ''.join(decode_val(shifre)))

decoded = full_decode(shifre, key_encoded)
print('Decoded list', decoded)
decoded_word_list = decode_val(decoded)
print("Начальное слово:", ''.join(decoded_word_list))