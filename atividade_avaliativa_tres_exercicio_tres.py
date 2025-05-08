"""3. Construa o programa que calcule a média aritmética dos números pares e a média aritmética dos
números ímpares. O usuário fornecerá os valores de entrada que pode ser um número qualquer par
ou ímpar. A condição de saída será o número 0 (zero)."""

contador_pares = 0
contador_impares = 0
soma_pares = 0
soma_impares = 0
print("Digite (0) para sair.")
while True:
    numero = int(input("Digite um número: "))
    if numero == 0:
        break
    resto = numero % 2
    if resto == 0:
        contador_pares = contador_pares + 1
        soma_pares = soma_pares + numero
        media_pares = soma_pares / contador_pares
    else:
        contador_impares = contador_impares + 1
        soma_impares = soma_impares + numero
        media_impares = soma_impares / contador_impares
print(f"A média aritmética dos número PARES é: {media_pares}")
print(f"A média aritmética dos números ÍMPARES é: {media_impares}.")