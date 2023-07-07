s1 = input()
s2 = input()

if s1 == s2:
    print("empate")
else:
    mapa = {'tesoura': ['papel', 'lagarto'],
            'papel': ['pedra', 'spock'],
            'pedra': ['lagarto', 'tesoura'],
            'lagarto': ['spock', 'papel'],
            'spock': ['tesoura', 'pedra']}

    if s2 in mapa[s1]:
        print("Interestelar")
    else:
        print("Jornada nas Estrelas")
