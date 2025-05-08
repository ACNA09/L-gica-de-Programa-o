"""1. Desenvolva o programa que leia vários valores reais e no final mostre as seguintes informações:
A quantidade de valores digitados;
A soma dos valores digitados;
A média aritmética dos valores digitados;
E a quantidade de valores digitados maior que 20"""

contador = 0
soma = 0
ct = 0
print("Digite (0) para sair.")
while True:
     numero = float(input("Digite um número: "))
     if numero == 0:
         break
     if numero > 20:
         ct = ct + 1
     contador = contador + 1
     soma = soma + numero
media = soma/contador
print(f"A quantidade de valores digitados é: {contador}.")
print(f"A soma dos valores digitados é: {soma}.")
print(f"A média aritmética dos valores digitados é: {media}.")
print(f"A quantidade de valores digitados maior que 20 é: {ct}.")



