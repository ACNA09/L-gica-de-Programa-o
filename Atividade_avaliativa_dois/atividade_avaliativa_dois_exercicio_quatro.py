"""4- Elabore o programa que simule a calculadora com as quatro operações aritméticas básicas.
O usuário fornecerá dois números e a operação aritmética desejada.
Mostre o menu com estes símbolos (+ , - , * , / ) para o usuário escolher a operação aritmética. Utilize
o comando “se . . . senão . . . ” encadeado, ou seja, “if . . . else . . . ” encadeado. """

valor_1 = float(input("Digite um número: "))
valor_2 = float(input("Digite um número: "))
soma = "+"
subtracao = "-"
multipicacao = "*"
divisao = "/"
menu = str(input("Digite '+' para adição. \nDigite '-' para a subtração.\nDigite '*' para a multiplicação.\nDigite '/' para a divisão."))
print(f"A opção escolhida foi: {menu}")

if menu == soma :
    print(f"O resultado da multiplicação é { valor_1 + valor_2}")
elif menu == subtracao:
    print(f"O resultado da subtração é {valor_1 - valor_2}")
elif menu == multipicacao:
    print(f"O resultado da multiplicação é {valor_1 * valor_2}")
else:
    print(f"O resultado da divisão é {valor_1 / valor_2}")







