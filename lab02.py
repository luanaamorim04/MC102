import sys
def opcao():
	print('(0) Não')
	print('(1) Sim')
def erro():
	print('Opção inválida, recomece o questionário.')
	sys.exit(0)

print('Este é um sistema que irá te ajudar a escolher a sua próxima Distribuição Linux. Responda a algumas poucas perguntas para ter uma recomendação.')
print('Seu SO anterior era Linux?')
opcao()
n = int(input())
resp = 0

if n == 1:
	print('É programador/ desenvolvedor ou de áreas semelhantes?')
	opcao()
	print('(2) Sim, realizo testes e invasão de sistemas')
	n = int(input())
	resp |= 8
	if n == 1:
		print('Gostaria de algo pronto para uso ao invés de ficar configurando o SO?')
		opcao()
		n = int(input())
		resp |= 4
		if n == 1:
			print('Já utilizou Debian ou Ubuntu?')
			opcao()
			n = int(input())
			resp |= 2
			if n == 1:
				resp |= 1
			elif n != 0:
				erro()
		elif n == 0:
			print('Já utilizou Arch Linux?')
			opcao()
			n = int(input())
			if n == 1:
				resp |= 1
			elif n != 0:
				erro()
		else:
			erro()
	elif n == 2:
		resp |= 16
	elif n != 0:
		erro()
elif n == 0:
	print('Seu SO anterior era um MacOS?')
	opcao()
	n = int(input())
	if n == 1:
		resp |= 4
	elif n != 0:
		erro()

else:
	erro()

mapa = {
	0: "Você passará pelo caminho daqueles que decidiram abandonar sua zona de conforto, as distribuições recomendadas são: Ubuntu Mate, Ubuntu Mint, Kubuntu, Manjaro.",
	4: "Você passará pelo caminho daqueles que decidiram abandonar sua zona de conforto, as distribuições recomendadas são: ElementaryOS, ApricityOS.",
	8: "Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições que servirão de base para seu aprendizado são: Ubuntu Mint, Fedora.",
	8 + 4: "Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições que servirão de base para seu aprendizado são: Antergos, Arch Linux.",
	8 + 4 + 2: "Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições que servirão de base para seu aprendizado são: OpenSuse, Ubuntu Mint, Ubuntu Mate, Ubuntu.",
	8 + 4 + 1: "Suas escolhas te levaram a um caminho repleto de desafios, para você recomendamos as distribuições: Gentoo, CentOS, Slackware.",
	8 + 4 + 2 + 1: "Suas escolhas te levaram a um caminho repleto de desafios, para você recomendamos as distribuições: Manjaro, ApricityOS.",
	8 + 16: "Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições que servirão de base para seu aprendizado são: Kali Linux, Black Arch.",
	-1: ""
}

print(mapa[resp])
















