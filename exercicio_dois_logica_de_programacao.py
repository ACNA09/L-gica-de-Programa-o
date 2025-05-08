"""
2. - A água é um nutriente essencial. Sem ela, o corpo não pode funcionar com perfeição. Cada pessoa
precisa de uma quantidade diferente de água para hidratar o corpo. A dose ideal, ou seja, a
necessidade diária em litros é calculada através da fórmula: massa (em kg) vezes 0,03. Elabore
o programa que realize esse cálculo.
"""

print("Quantidade ideal de água que você precisa.")
print("A quantidade ideal de água se obtém através da multiplicação do seu peso por 0,03")
massa = float(input("Digite o seu peso em kg:"))
valor = 0.03
quantidade_ideal_de_agua = massa * valor
print(f"A quantidade ideal de água para você é de {quantidade_ideal_de_agua:.2f} litros.")