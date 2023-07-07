vida_tot = 0
vida_now = 0
q_flechas = {}
tot_monstro = 0
vida_monstro = []
monstros = []

vida_tot = int(input())
ent = input().split()
idx = 0
for i in range(1, len(ent), 2):
	q_flechas[ent[i-1]] = int(ent[i])
	idx += 1
tot_monstro = int(input())

def morreu(vida_now):
	if (vida_now <= 0):
		return 1
	return 0

def tem_flecha(tipo, qtd):
	if (tipo not in qtd):
		return 0
	return (1 if qtd[tipo] > 0 else 0)

def achar_coord(idx, tipo, monstros):
	return [int(monstros[idx][3][tipo][3]), int(monstros[idx][3][tipo][4])]

def dano_monstro(idx_monstro, corpo, tipo_flecha, a1, b1, a2, b2, monstros):
	dano_max = int(monstros[idx_monstro][3][corpo][2])
	tipo_monstro = monstros[idx_monstro][3][corpo][1]
	d = max(0, dano_max - (abs(a1-a2) + abs(b2-b1)))
	if (tipo_monstro == tipo_flecha or tipo_monstro == "todas"):
		return [(a1 == a2 and b1 == b2), d]
	return [(a1 == a2 and b1 == b2), d//2]

def acha_idx(monstros, corpo):
	return monstros[3][corpo][5]

def imprime(saida, monstros):
	resp = []
	idx = 0
	vis = []
	for i in range(1, len(saida)):
		saida[i][1] = acha_idx(monstros[saida[i][0]], saida[i][1])
	saida.sort()
	
	for i in range(1, len(saida)):
		if (saida[i] == saida[i-1]):
			resp[len(resp)-1][3] += 1
		else:
			resp.append([saida[i][0], saida[i][2], saida[i][3], 1])
	
	for i in range(len(resp)):
		if resp[i][0] not in vis:
			print("Máquina " + str(resp[i][0]) + ":")
			vis.append(resp[i][0])
		print("- (" + str(resp[i][1]) + ", " + str(resp[i][2]) + "): " + str(resp[i][3]) + "x")
		
def jogando():
	t = 0
	kills = 0
	vida_now = vida_tot
	while (kills < tot_monstro):
		print("Combate " + str(t) + ", vida = " + str(vida_now))
		q_monstro = int(input())
		monstros = []
		vida_monstro = []
		dano = 0
		q_flechas_now = {}
		saida = [[]]
		kills_now = 0
		q_ataques = 0
		for i in q_flechas:
			q_flechas_now[i] = q_flechas[i]
		for i in range(q_monstro):
			ent = [int(i) for i in input().split()]
			monstros.append(ent)
			vida_monstro.append(int(ent[0]))
			dano += ent[1]
			mapa = {}
			for j in range(ent[2]):
				ent2 = input().split(', ')
				mapa[ent2[0]] = ent2 + [j]
			monstros[i].append(mapa)

		while (kills_now < q_monstro):
			q_ataques += 1
			ent = input().split(', ')
			i_monstro = int(ent[0])
			parte_corpo = ent[1]
			flecha_tipo = ent[2]
			c1 = int(ent[3])
			c2 = int(ent[4])

			if (tem_flecha(flecha_tipo, q_flechas_now) == 0):
				# print('a')
				return 0
			
			q_flechas_now[flecha_tipo] -= 1

			dead = 1
			for i in q_flechas_now:
				dead &= (q_flechas_now[i] == 0)

			par = achar_coord(i_monstro, parte_corpo, monstros)
			aaa = dano_monstro(i_monstro, parte_corpo, flecha_tipo, c1, c2, par[0], par[1], monstros)
			vida_monstro[i_monstro] -= int(aaa[1])
			if (aaa[0] == 1):
				saida.append([i_monstro, parte_corpo, c1, c2])
			
			if (morreu(vida_monstro[i_monstro])):
				kills_now += 1
				kills += 1
				dano -= monstros[i_monstro][1]
				print("Máquina " + ent[0] + " derrotada")

			if (q_ataques % 3 == 0):
				vida_now -= dano
				if (morreu(vida_now)):
					return 1

			if (dead):
				print("Vida após o combate = " + str(vida_now))
				vida_now = min(vida_tot, vida_now + (vida_tot//2))
				return 0

		print("Vida após o combate = " + str(vida_now))
		vida_now = min(vida_tot, vida_now + (vida_tot//2))


		print("Flechas utilizadas:")
		for i in q_flechas:
			if (q_flechas[i] != q_flechas_now[i]):
				print("- " + i + ": " + str(q_flechas[i]-q_flechas_now[i]) + "/" + str(q_flechas[i]))
		
		if (len(saida) > 1):
			print("Críticos acertados:")
			imprime(saida, monstros)
		
		t += 1
	return -1

resp = jogando()
if (resp == -1):
	print("Aloy provou seu valor e voltou para sua tribo.")
elif (resp == 0):
	print("Aloy ficou sem flechas e recomeçará sua missão mais preparada.")
else:
	print("Vida após o combate = 0")
	print("Aloy foi derrotada em combate e não retornará a tribo.")