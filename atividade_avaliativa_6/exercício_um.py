"""1.	Desenvolva uma função que recebe uma mensagem e um número,
ela mostra a mensagem e o número e não retorna nada.
A função main chama a função passando os dois argumentos lidos, ou seja, digitados pelo usuário. """

def recebe_mensagem_numero(mensagem, valor):
    print(f"A mensagem é: {mensagem}")
    print(f"O número é: {valor}")

if __name__ == '__main__':
    mensagem_um = str(input("Digite uma mensagem: " ))
    valor_um = float(input("Digite um número: "))
    print(recebe_mensagem_numero(mensagem_um, valor_um))
