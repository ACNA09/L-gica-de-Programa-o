"""1. A conversão de graus Fahrenheit para graus Celsius é obtida pela fórmula abaixo.
Calcule a conversão e construa o relatório de saída tabular (em forma de tabela de duas colunas)
de graus Celsius em função de graus Fahrenheit que que variam de 45 a 80 de 1 em 1.
Fórmula: c = 5 ( f - 32 )
"""

print("  ºF | Conversão de fahrenheit para celsius")
for fahrenheit in range(45, 81, 1):
    formula = ((5/9) * (fahrenheit - 32))
    print(f"{fahrenheit}º| {formula:.2f}º")