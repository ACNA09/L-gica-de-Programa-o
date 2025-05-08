"""4. Elabore o programa para somar todos os números inteiros que são ao mesmo
tempo ímpar e múltiplo de três que se encontram no intervalo de um a quinhentos."""

soma = 0
for numero in range(1,501,1):
    if numero % 2 != 0 and numero % 3 == 0:
       print(numero)
       soma = soma + numero
print(f"A soma dos números ímpare e múltiplos de três é que se encontram no intervalo de um até quihentos é: {soma}")


