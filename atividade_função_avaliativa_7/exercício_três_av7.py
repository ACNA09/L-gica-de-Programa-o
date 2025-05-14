"""3.	Simule uma calculadora com as quatro operações aritméticas.
Implemente uma função para cada operação aritmética.
Ela recebe dois valores e não retorna nada.
A função executa o cálculo e mostra o resultado do cálculo.
O usuário fornecerá a operação desejada (operador: +, -, x, / ) e
os dois valores dentro do programa (função main) que chamará uma das quatro funções.
O resultado do cálculo será mostrado dentro de cada função. Use variável local."""

def operacao_soma(valor_um, valor_dois):
    soma = valor_um + valor_dois
    print("A soma dos valores digitados é: ", soma)

def operacao_subtracao(valor_um, valor_dois):
    subtracao = valor_um - valor_dois
    print("A subtração dos valores digitados é: ", subtracao)
def operacao_multiplicacao(valor_um, valor_dois):
    multiplicacao = valor_um * valor_dois
    print("A multiplicação dos valores digitados é: ", multiplicacao)

def operacao_divisao(valor_um, valor_dois):
    if valor_dois != 0:
        divisao = valor_um / valor_dois
        print("A divisão dos valores digitados é: ", divisao)
    else:
        print("Erro: Divisão por zero")


if __name__ == '__main__':
    valor_um = float(input("Digite um número: "))
    valor_dois = float(input("Digite um número: "))
    operacao_desejada = str(input("Digite [+] para adição\n"+
                                  "Digite [-] para subtração\n"+
                                  "Digite [*] para multiplicação\n"+
                                  "Digite [/] para divisão\n"+
                                  "Qual operação você quer realizar?"))

    if operacao_desejada == "+":
        operacao_soma(valor_um, valor_dois)
    elif operacao_desejada == "-":
        operacao_subtracao(valor_um, valor_dois)
    elif operacao_desejada == "*":
        operacao_multiplicacao(valor_um, valor_dois)
    else:
        operacao_divisao(valor_um, valor_dois)