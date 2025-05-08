"""2. Melhore o programa anterior para torná-lo mais abrangente.
Agora, o usuário fornecerá os valores inicial e final de graus Fahrenheit.
Calcule a conversão e gere o relatório de saída tabular (em forma de tabela) considerando o intervalo digitado.
Gere o relatório na ordem crescente, se o valor inicial for menor ou igual ao valor final.
E na ordem decrescente, se valor inicial for maior que o valor final.
"""

graus_fahrenheit_valor_inicial = int(input("Digite o primeiro valor em graus Fahrenheit: "))
graus_fahrenheit_valor_final = int(input("Digite o segundo valor em graus Fahrenheit: "))

print(" ºF |   ºC")
if graus_fahrenheit_valor_inicial <= graus_fahrenheit_valor_final:
    for fahrenheit in range(graus_fahrenheit_valor_inicial, graus_fahrenheit_valor_final + 1, 1):
        formula = (5 / 9) * (fahrenheit - 32)
        print(f"{fahrenheit}º | {formula:.2f}º")
else:
    for fahrenheit in range(graus_fahrenheit_valor_inicial, graus_fahrenheit_valor_final - 1, -1):
        formula = (5 / 9) * (fahrenheit - 32)
        print(f"{fahrenheit}º | {formula:.2f}ºC")
