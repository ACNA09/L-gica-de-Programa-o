"""2.	Implemente uma função que calcula a idade de uma pessoa.
Ela recebe o ano de nascimento da pessoa, faz o cálculo e retorna à idade.
A função principal (main) lê o ano de nascimento digitado pelo usuário,
chama a função e mostra o valor retornado pela função calcula."""


def calcula_idade(ano_atual, ano_nascimento):
    idade = ano_atual- ano_nascimento
    print("Você tem",idade, "anos")

if __name__ == '__main__':
    ano_atual = int(input("Digite o ano em que estamos: "))
    ano_nascimento = int(input("Digite o ano que você nasceu: "))
    calcula_idade(ano_atual, ano_nascimento)