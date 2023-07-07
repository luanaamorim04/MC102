gen = input()
n = len(gen)

def reverter(s, i, j):
	i = min(i, len(s)-1)
	j = min(j, len(s)-1)
	x = s[0:i]
	x += s[i:j+1] [::-1]
	x += s[j+1:len(s)]
	return x

def transpor(s, i, j, k):
	i = min(i, len(s)-1)
	j = min(j, len(s)-1)
	k = min(k, len(s)-1)
	x = s[0:i]
	x += s[j+1:k+1]
	x += s[i:j+1]
	x += s[k+1:len(s)]
	return x

def combinar(s, s2, i):
	i = min(i, len(s)-1)
	x = s[0:i]
	x += s2
	x += s[i:len(s)]
	return x

def concatenar(s, s2):
	return s + s2

def remover(s, i, j):
	i = min(i, len(s)-1)
	j = min(j, len(s)-1)
	return s[0:i] + s[j+1:len(s)]

def transpor_e_reverter(s, i, j, k):
	i = min(i, len(s)-1)
	j = min(j, len(s)-1)
	k = min(k, len(s)-1)
	s = reverter(s, i, j)
	s = reverter(s, j+1, k)
	return s

def buscar(s, s2):
	resp = 0
	i = 0
	while i < (len(s) - len(s2) + 1):
		if s[i:(i+len(s2))] == s2:
			resp += 1
			i += (len(s2) - 1)
		i += 1
	print(resp)
	return resp

def buscar_bidirecional(s, s2):
	resp = 0
	i = 0
	while i < (len(s) - len(s2) + 1):
		if s[i:(i+len(s2))] == s2:
			resp += 1
			i += (len(s2) - 1)
		i += 1

	i = 0
	s = reverter(s, 0, len(s))
	while i < (len(s) - len(s2) + 1):
		if s[i:(i+len(s2))] == s2:
			resp += 1
			i += (len(s2) - 1)
		i += 1
	print(resp)

def mostrar(s):
	print(s)

op = input().split()

while op[0] != "sair":
	if op[0] == "reverter":
		gen = reverter(gen, int(op[1]), int(op[2]))
	elif op[0] == "transpor":
		gen = transpor(gen, int(op[1]), int(op[2]), int(op[3]))
	elif op[0] == "combinar":
		gen = combinar(gen, op[1], int(op[2]))
	elif op[0] == "concatenar":
		gen = concatenar(gen, op[1])
	elif op[0] == "transpor_e_reverter":
		gen = transpor_e_reverter(gen, int(op[1]), int(op[2]), int(op[3]))
	elif op[0] == "buscar":
		buscar(gen, op[1])
	elif op[0] == "buscar_bidirecional":
		buscar_bidirecional(gen, op[1])
	elif op[0] == "mostrar":
		mostrar(gen)
	elif op[0] == "remover":
		gen = remover(gen, int(op[1]), int(op[2]))

	n = len(gen)
	op = input().split()
