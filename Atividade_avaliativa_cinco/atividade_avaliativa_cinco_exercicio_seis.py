"""6. Vamos tornar o programa anterior mais interessante. Agora, o programa deve gerar
a tabuada de multiplicação de um número inteiro qualquer fornecido pelo usuário."""

num = int(input("Digite um número: "))
for numero in range(1, 11, 1):
    multiplicacao = num * numero
    print(f"{num} * {numero} = {multiplicacao}")
