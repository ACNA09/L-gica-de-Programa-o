"""3.	Crie uma função para somar três valores. Ela recebe os três valores,
 calcula a soma e retorna o resultado do cálculo.
A função main lê os três valores inteiros, chama a função passando os valores lidos e
depois mostra o valor retornado pela função, ou seja, o resultado obtido.
"""
def soma_tres_valores(valor_um, valor_dois, valor_tres):
    soma = valor_um + valor_dois + valor_tres
    print(f"A soma dos valores digitados é: ", soma)

if __name__ == '__main__':
    valor_um = float(input("Digite um número: "))
    valor_dois = float(input("Digite um número: "))
    valor_tres = float(input("Digite um número: "))
    print(soma_tres_valores(valor_um,valor_dois,valor_tres))