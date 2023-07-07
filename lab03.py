n = int(input())
arr = input().split()
resp = []
interval = input().split()
val = 0
pos = 0
empate = 0
idx = 0

for i in range(n):
	arr[i] = int(arr[i])

for i in range(0, n<<1, 2):
	l = int(interval[i])
	r = int(interval[i+1])
	if idx < ((n+1)>>1):
		arr[idx] *= (r-l)
	else:
		arr[idx] += (r-l)
	idx += 1

for i in range(n):
	if arr[i] > val:
		val = arr[i]
		empate = 0
		pos = i
	elif arr[i] == val:
		empate = 1

if empate == 1:
	print("Rodada de cerveja para todos os jogadores!")
else:
	print("O jogador número " + str(pos+1) + " vai receber o melhor bolo da cidade pois venceu com " + str(val) + " ponto(s)!")

