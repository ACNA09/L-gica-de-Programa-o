"""2.	Elabore a função (def) valor absoluto que recebe um número qualquer e retorna o valor absoluto (módulo)
 correspondente. O programa lê o número digitado pelo usuário, chama a função valor absoluto passando o
  número lido e depois gera a tela de saída com o valor retornado pela função valor absoluto.
  Lembrando que valor absoluto de um número positivo é ele mesmo e o valor absoluto de um número negativo é
  ele multiplicado por -1. Não use a função abs da linguagem."""

def valor_absoluto(numero):
    if numero > 0:
        return numero
    elif numero < 0 :
        return numero * (-1)
    else:
        return 0

if __name__ == '__main__':
    valor = float(input("Digite um número: "))
    print(f"O módulo desse número é: {valor_absoluto(valor)}")
