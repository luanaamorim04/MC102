op = input()
chave = 1
if (op == '+' or op == '-'):
	chave = 0
marca = input()
idx = 0
flag = 0
marcas = []
linhas = []
tot = []
vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']

def indice(last, marca):
	for i in range(last, len(tot)):
		if (marca == "numero" and (tot[i] in num)):
			return i
		elif (marca == "vogal" and (tot[i] in vogais)):
			return i
		elif (marca == "consoante" and (tot[i] in consoantes)):
			return i
		elif (tot[i] == marca):
			return i
	return len(tot)


def opera(a, b):
	if (op == '-'):
		return a-b
	if (op == '+'):
		return a+b
	if (op == '*'):
		return a*b
	if (op == '/'):
		return a//b

while (not marca.isnumeric()):
	marcas.append(marca)
	marca = input()

marca = int(marca)
while marca:
	tmp = input()
	linhas.append(tmp)
	tot += tmp
	marca -= 1

for i in marcas:
	idx = indice(idx, i)
	if (flag):
		chave = opera(chave, idx)
	else:
		chave = idx
	flag = 1

print(chave)

for linha in linhas:
	for i in linha:
		letra = (ord(i) + chave)
		letra = 32 + ((letra - 32) % 95)
		print(chr(letra), end='')
	print()


# print((88 + chave) % 127)




