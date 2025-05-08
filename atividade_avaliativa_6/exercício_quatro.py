"""4.	Elabore o problema (o enunciado) de um problema que usa função e resolva o problema proposto, ou seja,
 faça a implementação da função def e da função principal (main). """

#Elaboração do problema
"""Crie uma função que receba dois valores que serão digitados pelo usuário. Ela recebe dois valores e 
faz as quatro operações básicas com os valores, na função main mostre todas as operações.A função main lê os dois valores, 
chama a função passando os valores lidos e
depois mostra o valor retornado pela função, ou seja, o resultado das operações básicas.
Atenção: o divisor não pode ser igual a zero
"""

def operacoes_basicas(valor_um, valor_dois):
    soma = valor_um + valor_dois
    subtracao = valor_um - valor_dois
    multiplicacao = valor_um * valor_dois
    print("A soma dos valores digitados é: ", soma)
    print("A subtração dos valores digitados é: ", subtracao)
    print("A multiplicação dos valores digitados é: ", multiplicacao)

    if valor_dois != 0:
        divisao = valor_um / valor_dois
        print("A divisão dos valores digitados é: ", divisao)
    else:
        print("Erro: Divisão por zero")




if __name__ == '__main__':
    valor_um = float(input("Digite um número: "))
    valor_dois = float(input("Digite um número: "))
    operacoes_basicas(valor_um, valor_dois)