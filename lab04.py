d = int(input()) 

for t in range(1, d+1):
	m = int(input())
	mapa = dict()
	at = dict()
	invalido = list()
	nao = list()
	dogs = list()
	total = list()
	briga = 0
	while m > 0:
		par = input().split();
		mapa.setdefault(par[0], []).append(par[1])
		mapa.setdefault(par[1], []).append(par[0])
		m -= 1;

	atividade = input().split();
	for i in range(0, len(atividade), 2):
		at[atividade[i]] = int(atividade[i+1]);

	n = int(input())
	while n:
		par = input().split()
		total.append(par[0])
		if at.get(par[1]) == None:
			invalido.append(par[0])
		elif at[par[1]] > 0:
			at[par[1]] -= 1
			dogs.append(par[0])
		else:
			nao.append(par[0])
		n -= 1

	
	for i in range(len(total)):
		mapa.setdefault(total[i], [])
		for j in range(i+1, len(total)):
			if total[j] in mapa[total[i]]:
				briga += 1;

	print("Dia: " + str(t))
	print("Brigas: " + str(briga))
	if len(dogs) > 0:
		print("Animais atendidos: ", end='')
		for i in range(len(dogs)-1):
			print(dogs[i], end=', ')
		print(dogs[len(dogs)-1]);

	if len(nao) > 0:
		print("Animais não atendidos: ", end='')
		for i in range(len(nao)-1):
			print(nao[i], end=', ')
		print(nao[len(nao)-1]);

	for i in invalido:
		print("Animal " + i + " solicitou procedimento não disponível.")
	print()

