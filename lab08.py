n = int(input())
filmes = []
notas = []
media = []
qtd = []
mapa = {}
categorias = {
	"filme que causou mais bocejos": 0,
	"filme que foi mais pausado": 1,
	"filme que mais revirou olhos": 2,
	"filme que não gerou discussão nas redes sociais": 3,
	"enredo mais sem noção": 4,
}

for i in range(n):
	filme = input().split()
	nome = ""
	for j in filme:
		nome += j
		nome += ' '
	mapa[nome[: len(nome)-1]] = i
	filmes.append(nome[: len(nome)-1])
	notas.append([[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]])
	qtd.append(0)
	media.append(0)

q = int(input())
for i in range(q):
	av = input().split(', ')
	notas[mapa[av[2]]][categorias[av[1]]][0] += 1
	notas[mapa[av[2]]][categorias[av[1]]][1] += int(av[3])

print("#### abacaxi de ouro ####")
print()
print("categorias simples")
for i in range(5):
	for idx in categorias:
		if (categorias[idx] == i):
			print("categoria: " + idx)
			break
	maior = 0
	resp = -1
	for j in range(n):
		if (notas[j][i][0] == 0):
			continue
		media[j] += (notas[j][i][1]//notas[j][i][0])
		if (maior < (notas[j][i][1]//notas[j][i][0])):
			maior = (notas[j][i][1]//notas[j][i][0])
			resp = j
		elif (maior == (notas[j][i][1]//notas[j][i][0])):
			if (notas[j][i][0] > notas[resp][i][0]):
				resp = j
	print("- " + filmes[resp])
	qtd[resp] += 1

resp = 0
print()
print("categorias especiais")
print("prêmio pior filme do ano")
for i in range(n):
	if (qtd[i] > qtd[resp]):
		resp = i
	elif (qtd[i] == qtd[resp]):
		if (media[i] > media[resp]):
			resp = i

print("- " + filmes[resp])
# print(qtd[resp])

print("prêmio não merecia estar aqui")
r = []
for i in range(n):
	resp = 0
	for j in range(5):
		resp |= notas[i][j][0]

	if (resp == 0):
		r.append(filmes[i])

print("- ", end='')
if (len(r) == 0):
	print("sem ganhadores")
else:
	for i in range(len(r)):
		print(r[i], end='')
		if (i != len(r) - 1):
			print(", ", end='')
	print()

















