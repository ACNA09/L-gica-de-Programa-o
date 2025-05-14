"""4.	Elabore a função fatorial que recebe o valor inteiro e retorna seu fatorial.
O valor será lido no programa (função main) que chama a função fatorial passando o valor lido.
O programa (função main) recebe o valor retornado pela função fatorial e gera a tela de saída.
Lembre-se que fatorial de n ( n! ) é a multiplicação dos números naturais de 1 até n.
0! = 1		1! = 1			n! = 1 x 2 x 3 x . . . x (n - 1) x n.
"""

def fatorial(valor):
    resultado = 1
    for n in range(1, valor+1):
        resultado = resultado * n
    return resultado

if __name__ == '__main__':
    numero = int(input("Digite um número: "))
    print(f"{numero}! é : {fatorial(numero)}")