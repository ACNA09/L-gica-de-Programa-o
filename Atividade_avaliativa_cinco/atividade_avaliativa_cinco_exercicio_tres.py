"""3. Elabore o programa para somar todos os números inteiros que se
encontram no intervalo de um a quinhentos."""
soma = 0
for numero in range(1,501,1):
    print(numero)
    soma = soma + numero
print(f"A soma de todos os números de um a quinhentos é: {soma}")