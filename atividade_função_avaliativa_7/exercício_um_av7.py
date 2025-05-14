"""1.	Desenvolva a função (def) positivo nulo negativo que recebe um número qualquer real e não retorna nada.
Ela mostra a mensagem “Valor Positivo”, se o número recebido for positivo; mostra a mensagem “Valor nulo”,
 se o número recebido for nulo e mostra a mensagem “Valor negativo”,
 se o número recebido for negativo. O programa (main) lê o número,
 chama a função positivo nulo negativo passando o valor lido (argumento).
"""

def positivo_nulo_negativo(valor):
    if valor > 0:
        print("Valor positivo.")
    elif valor < 0:
        print("Valor negativo.")
    else:
        print("Valor nulo.")

if __name__ == '__main__':
    numero = float(input("Digite um número: "))
    positivo_nulo_negativo(numero)
