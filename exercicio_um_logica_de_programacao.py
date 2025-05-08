"""
1. Implemente o programa que calcule o volume de uma esfera de raio R. O usuário fornecerá o
dado necessário. Onde: volume = 4 * pi * r**3 / 3
"""

raio = float(input("Insira o raio da esfera para o cálculo do volume ser realizado: " ))
pi = 3.14
volume_esfera = (4 * pi * (raio**3)) / 2
print(f"O volume da esfera é: {volume_esfera} ")