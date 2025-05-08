"""
4. Desenvolva o programa que classifique dois valores inteiros quaisquer em ordem crescente. Os
valores serão fornecidos pelo usuário.
"""

numero_1 = float(input("Digite um número qualquer: "))
numero_2 = float(input("Digite outro número qualquer: "))
if numero_1 > numero_2:
    print(f"A ordem crescente dos números digitados é: {numero_2} , {numero_1}")
elif numero_2 > numero_1:
    print(f"A ordem crescente dos números digitados é: {numero_1} , {numero_2} ")
else:
    print("Os números são iguais.")