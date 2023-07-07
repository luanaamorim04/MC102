n = int(input())
m = 0
tab = []
tmp = []
linha = []
pa = 1
pb = 1
la = 1
lb = 1
flag = 0
limpa = 0

def pos(a, b):
	return a*(m+2) + b

def imprime(a, b):
	for i in range(1, n+1):
		for j in range(1, m+1):
			if i == a and j == b:
				print('r', end='')
			else:
				print(tab[pos(i, j)], end='')
			if (j < m):
				print(' ', end = '')
		print()

def arruma(a, b):
	tab[pos(a, b)] = '.'

def limpando(pa, pb):
	if tab[pos(pa, pb-1)] == 'o':
		return [0, -1]
	elif tab[pos(pa-1, pb)] == 'o':
		return [-1, 0]
	elif tab[pos(pa, pb+1)] == 'o':
		return [0, 1]
	elif tab[pos(pa+1, pb)] == 'o':
		return [1, 0]
	
	return [0, 0]

def volta(a0, b0, a1, b1):
	if (b0 != b1):
		return [0, 1 if b0 < b1 else -1]
	elif (a0 != a1):
		return [1 if a0 < a1 else -1, 0]

for i in range(n):
	tmp += ['.']
	a = input().split()
	m = len(a)
	tmp += a
	tmp += ['.']
	tab += tmp

for i in range(m+2):
	linha.append('.')

tab = linha + tmp + linha

# esq cima dir baixo
arruma(1, 1)

while (pa != n or (pb != m if pa&1 == 1 else pb != 1)) or limpa == 1:
	imprime(pa, pb)
	print()
	flag = 0
	if limpa == 0:
		limpa = 1
		if tab[pos(pa, pb-1)] == 'o':
			if (pa&1) == 0:
				limpa = 0
			pb -= 1
		elif tab[pos(pa-1, pb)] == 'o':
			pa -= 1
		elif tab[pos(pa, pb+1)] == 'o':
			if (pa&1) == 1:
				limpa = 0
			pb += 1
		elif tab[pos(pa+1, pb)] == 'o':
			if (pa&1 == 1 and pb == m) or (pa&1 == 0 and pb == 1):
				limpa = 0
			pa += 1
		else:
			pb += (-1 if pa&1 == 0 else 1)
			pa += (1 if (pb==0 or pb>m) else 0)
			pb = max(pb, 1)
			pb = min(pb, m)
			limpa = 0
		if limpa == 0:
			la = pa 
			lb = pb
		arruma(pa, pb)
	else:
		prox = limpando(pa, pb)
		pa += prox[0]
		pb += prox[1]
		if (prox == [0, 0]):
			prox = volta(pa, pb, la, lb)
			pa += prox[0]
			pb += prox[1]
			if (pa == la and pb == lb):
				limpa = 0
		arruma(pa, pb)

imprime(pa, pb)
print()

while (pa != n or pb != m):
	prox = volta(pa, pb, n, m)
	pa += prox[0]
	pb += prox[1]
	imprime(pa, pb)
	print()



