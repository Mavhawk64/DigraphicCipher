alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def word_to_2d_int_arr(word):
	arr = [[]]
	j = 0
	for i in word:
		if i == ' ':
			arr.append([])
			j += 1
		else:
			arr[j].append(alphabet.index(i))
	arr = arr[:-1]
	return arr

def arr_to_word(arr):
	word = ''
	for i in arr:
		word += alphabet[i[0]] + alphabet[i[1]] + ' '
	word = word[:-1]
	return word

def encrypt(word,a,b,c,d):
	# C1 = aP1 + bP2
	# C2 = cP1 + dP2
	word = word.replace(' ','')
	arr = list(word)
	i = len(arr)-1
	while i >= 0:
		if i % 2 == 1:
			arr[i] += ' '
		i -= 1
	word = ''.join(arr)
	arr = word_to_2d_int_arr(word)
	# print(arr)
	for i in range(0,len(arr)):
		# [7, 4]
		p1 = arr[i][0] # 7
		p2 = arr[i][1] # 4
		c1 = a * p1 + b * p2
		c2 = c * p1 + d * p2
		c1 %= 26
		c2 %= 26
		arr[i] = [c1,c2]
	word = arr_to_word(arr)
	return word

def decrypt(word,a,b,c,d):
	# P1 = inv(a*d-b*c) * (d*C1-b*C2) mod 26
	# P2 = inv(a*d-b*c) * (a*C2-c*C1) mod 26
	v = inv(a*d-b*c,26)
	word = word.replace(' ','')
	word = encrypt(word,v*d,-v*b,-v*c,v*a)
	return word
def inv(x,m):
	for i in range(1,m):
		if (x*i) % m == 1:
			return i
	return 0

print(decrypt('KKTCARKARS',3,1,2,3))
print(inv(7,26))