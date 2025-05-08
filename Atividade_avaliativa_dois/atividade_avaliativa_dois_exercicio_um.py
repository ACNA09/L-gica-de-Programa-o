"""
1- Desenvolva o programa que classifique dois valores inteiros quaisquer em ordem crescente. Os
valores serão fornecidos pelo usuário. """


valor_1 = float(input("Digite um número qualquer: "))
valor_2 = float(input("Digite outro número qualquer: "))
if valor_1 > valor_2:
    print(f"A ordem crescente dos números digitados é: {valor_2} , {valor_1}")
elif valor_2 > valor_1:
    print(f"A ordem crescente dos números digitados é: {valor_1} , {valor_2} ")
else:
    print("Os números são iguais.")



