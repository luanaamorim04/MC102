from typing import List


def soma_vetores(v1: List[int], v2: List[int]) -> List[int]:
    while (len(v1) < len(v2)):
        v1.append(0)
    while (len(v2) < len(v1)):
        v2.append(0)
    for i in range(len(v1)):
        v1[i] += v2[i]
    return v1


def subtrai_vetores(v1: List[int], v2: List[int]) -> List[int]:
    while (len(v1) < len(v2)):
        v1.append(0)
    while (len(v2) < len(v1)):
        v2.append(0)
    for i in range(len(v1)):
        v1[i] -= v2[i]
    return v1


def multiplica_vetores(v1: List[int], v2: List[int]) -> List[int]:
    while (len(v1) < len(v2)):
        v1.append(1)
    while (len(v2) < len(v1)):
        v2.append(1)
    for i in range(len(v1)):
        v1[i] *= v2[i]
    return v1


def divide_vetores(v1: List[int], v2: List[int]) -> List[int]:
    while (len(v1) < len(v2)):
        v1.append(0)
    while (len(v2) < len(v1)):
        v2.append(1)
    for i in range(len(v1)):
        v1[i] //= v2[i]
    return v1


def multiplicacao_escalar(v1: List[int], x: int) -> List[int]:
    for i in range(len(v1)):
        v1[i] *= x
    return v1


def n_duplicacao(v1: List[int], x: int) -> List[int]:
    return v1*x


def soma_elementos(v1: List[int]) -> int:
    soma: int = 0
    for i in v1:
        soma += i
    return soma


def produto_interno(v1: List[int], v2: List[int]) -> int:
    return soma_elementos(multiplica_vetores(v1, v2))


def multiplica_todos(v1: List[int], v2: List[int]) -> List[int]:
    for i in range(len(v1)):
        soma: int = 0
        for x in v2:
            soma += (v1[i]*x)
        v1[i] = soma
    return v1


def correlacao_cruzada(v1: List[int], mask: List[int]) -> List[int]:
    r: List[int] = []
    for i in range(len(v1) - len(mask) + 1):
        soma = 0
        for j in range(len(mask)):
            soma += (v1[i + j] * mask[j])
        r.append(soma)
    return r


def main() -> None:
    v1: List[int] = [int(i) for i in input().split(',')]
    op: str = input()
    while (op != "fim"):
        if (op == "soma_vetores"):
            v2 = [int(i) for i in input().split(',')]
            v1 = soma_vetores(v1, v2)
        elif (op == "subtrai_vetores"):
            v2 = [int(i) for i in input().split(',')]
            v1 = subtrai_vetores(v1, v2)
        elif (op == "multiplica_vetores"):
            v2 = [int(i) for i in input().split(',')]
            v1 = multiplica_vetores(v1, v2)
        elif (op == "divide_vetores"):
            v2 = [int(i) for i in input().split(',')]
            v1 = divide_vetores(v1, v2)
        elif (op == "multiplicacao_escalar"):
            v1 = list(multiplicacao_escalar(v1, int(input())))
        elif (op == "n_duplicacao"):
            v1 = n_duplicacao(v1, int(input()))
        elif (op == "produto_interno"):
            v2 = [int(i) for i in input().split(',')]
            tmp: List[int] = v1
            v1 = []
            v1.append(produto_interno(tmp, v2))
        elif (op == "multiplica_todos"):
            v2 = [int(i) for i in input().split(',')]
            v1 = multiplica_todos(v1, v2)
        elif (op == "correlacao_cruzada"):
            v2 = [int(i) for i in input().split(',')]
            v1 = correlacao_cruzada(v1, v2)
        elif (op == "soma_elementos"):
            tmp = v1
            v1 = []
            v1.append(soma_elementos(tmp))
        print(v1)
        op = input()


if __name__ == "__main__":
    main()
